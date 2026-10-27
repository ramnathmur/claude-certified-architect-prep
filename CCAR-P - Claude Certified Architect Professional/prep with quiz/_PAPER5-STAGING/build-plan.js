#!/usr/bin/env node
/*
 * Central plan builder for Paper 5 (5th untargeted diagnostic, confirmed with Ram; §3 of the
 * Paper 5 generation prompt). D2 corpus expansion (2026-09-01) means D2 no longer needs the
 * hard-coded reuse-inversion/misconception mechanism Paper 4 required -- it runs through the
 * same generic freshness-greedy floor+discretionary algorithm as every other domain.
 * Output: plan-raw.json.
 */
const fs = require("fs");
const path = require("path");
const scriptDir = __dirname;

const supply = JSON.parse(fs.readFileSync(path.join(scriptDir, "facet-supply.json"), "utf8"));
const objMapRaw = fs.readFileSync(path.join(scriptDir, "../CCAR-P_Objective-Map_v1.md"), "utf8");

const objectives = [];
for (const line of objMapRaw.split("\n")) {
  const m = line.match(/^\|\s*\*\*(O[\d.]+)\*\*\s*\|\s*(D\d)\s*\|\s*([^|]+)\|\s*([\d.,\s]+)\|\s*(\d+)\s*\|/);
  if (m) {
    objectives.push({
      id: m[1], domain: m[2], text: m[3].trim(),
      sections: m[4].split(",").map((s) => s.trim()).filter(Boolean),
    });
  }
}

const QUOTA = { D1: 11, D2: 8, D3: 12, D4: 10, D5: 9, D6: 9, D7: 4 };
const DISCRETIONARY = { D1: 5, D2: 3, D3: 4, D4: 4, D5: 4, D6: 4, D7: 1 };

const freshPool = {};
Object.entries(supply.sections).forEach(([sec, s]) => (freshPool[sec] = [...s.fresh]));
const miscUsedThisPaper = new Set();
const sectionCountThisPaper = {};
const misconceptionBySection = {};
Object.entries(supply.misconceptionsBySection).forEach(([sec, m]) => {
  if (!m.used) misconceptionBySection[sec] = m.id;
});

function secInfo(sec) {
  return supply.sections[sec] || { usedCount: 0, fresh: [], total: 0 };
}

function pickFromSection(sec) {
  if (freshPool[sec] && freshPool[sec].length > 0) {
    const id = freshPool[sec].shift();
    consumedFacetIds.add(id);
    return { kind: "facet", id };
  }
  const mUnit = misconceptionBySection[sec];
  if (mUnit && !miscUsedThisPaper.has(mUnit)) {
    miscUsedThisPaper.add(mUnit);
    return { kind: "misconception", id: mUnit };
  }
  return null;
}

function bestSection(sections, { excludeAtCap = true } = {}) {
  const candidates = sections
    .map((sec) => ({
      sec,
      fresh: (freshPool[sec] || []).length,
      usedHist: secInfo(sec).usedCount,
      inPaper: sectionCountThisPaper[sec] || 0,
      hasMisc: !!misconceptionBySection[sec] && !miscUsedThisPaper.has(misconceptionBySection[sec]),
    }))
    .filter((c) => !excludeAtCap || c.inPaper < 2)
    .filter((c) => c.fresh > 0 || c.hasMisc);
  if (candidates.length === 0) return null;
  candidates.sort((a, b) => b.fresh - a.fresh || a.usedHist - b.usedHist || a.inPaper - b.inPaper || a.sec.localeCompare(b.sec, undefined, { numeric: true }));
  return candidates[0].sec;
}

// Reuse-inversion fallback (FACET-LEDGER.md "three ways out" #1, direction doubling, in force
// since Paper 4). Used only when an objective's every section is both fresh-exhausted AND its
// misconception unit already spent -- currently O3.1 (sole section 3.1) and O5.3 (sole section
// 5.8). Picks the section with the fewest already-inverted facets on record and reuses its
// numerically-first used facet, flagged reuse-inverted for finalize-plan.js's explicit
// per-instance inversion guidance and the independent audit's genuineness check (F-27/F-28).
const consumedFacetIds = new Set();

function bestExhaustedSection(sections, { excludeAtCap = true } = {}) {
  const candidates = sections
    .map((sec) => ({
      sec, inPaper: sectionCountThisPaper[sec] || 0,
      usedIds: (secInfo(sec).usedIds || []).filter((id) => !consumedFacetIds.has(id)),
    }))
    .filter((c) => !excludeAtCap || c.inPaper < 2)
    .filter((c) => c.usedIds.length > 0);
  if (candidates.length === 0) return null;
  candidates.sort((a, b) => a.inPaper - b.inPaper || a.sec.localeCompare(b.sec, undefined, { numeric: true }));
  return candidates[0];
}

const items = [];
const objItemCount = {};

const reuseInvertedPicks = [];

// Floor pass: one item per objective, all 7 domains
for (const o of objectives) {
  const sec = bestSection(o.sections);
  if (sec) {
    const pick = pickFromSection(sec);
    if (!pick) throw new Error(`Floor pass: pickFromSection failed for ${sec}`);
    sectionCountThisPaper[sec] = (sectionCountThisPaper[sec] || 0) + 1;
    objItemCount[o.id] = (objItemCount[o.id] || 0) + 1;
    items.push({ domain: o.domain, objective: o.id, section: sec, pass: "floor", direction: "normal", ...pick });
    continue;
  }
  // Every section for this objective is fresh-exhausted and misconception-spent. Fall back to
  // reuse-inversion (in-force standing mechanism, not a new decision -- see comment above).
  const fallback = bestExhaustedSection(o.sections);
  if (!fallback) throw new Error(`Floor pass: no section, fresh or reusable, for ${o.id}`);
  const facetId = fallback.usedIds[0];
  sectionCountThisPaper[fallback.sec] = (sectionCountThisPaper[fallback.sec] || 0) + 1;
  objItemCount[o.id] = (objItemCount[o.id] || 0) + 1;
  consumedFacetIds.add(facetId);
  const item = { domain: o.domain, objective: o.id, section: fallback.sec, pass: "floor", direction: "inverted", kind: "reuse-inverted", id: facetId };
  items.push(item);
  reuseInvertedPicks.push(item);
}

// Discretionary pass, all 7 domains
for (const domain of Object.keys(QUOTA)) {
  const domainObjs = objectives.filter((o) => o.domain === domain);
  let need = DISCRETIONARY[domain];
  while (need > 0) {
    const candidateObjs = domainObjs.filter((o) => (objItemCount[o.id] || 0) < 3);
    if (candidateObjs.length === 0) throw new Error(`Discretionary pass: ${domain} objective caps exhausted with ${need} still needed`);
    candidateObjs.sort((a, b) => (objItemCount[a.id] || 0) - (objItemCount[b.id] || 0) || a.id.localeCompare(b.id));
    let placed = false;
    // Pass 1: normal (fresh-facet or fresh-misconception) supply only, across ALL candidates,
    // before any candidate is allowed to fall back to reuse-inversion. This stops the tie-break
    // (lowest objItemCount first) from preferring an exhausted objective's lower-quality reuse
    // supply over a different objective in the same domain that still has genuine fresh supply.
    for (const o of candidateObjs) {
      const sec = bestSection(o.sections);
      if (!sec) continue;
      const pick = pickFromSection(sec);
      if (!pick) continue;
      sectionCountThisPaper[sec] = (sectionCountThisPaper[sec] || 0) + 1;
      objItemCount[o.id] = (objItemCount[o.id] || 0) + 1;
      items.push({ domain, objective: o.id, section: sec, pass: "discretionary", direction: "normal", ...pick });
      placed = true;
      break;
    }
    // Pass 2: only if literally no candidate objective in this domain has fresh supply left.
    if (!placed) {
      for (const o of candidateObjs) {
        const fallback = bestExhaustedSection(o.sections);
        if (!fallback) continue;
        const facetId = fallback.usedIds[0];
        consumedFacetIds.add(facetId);
        sectionCountThisPaper[fallback.sec] = (sectionCountThisPaper[fallback.sec] || 0) + 1;
        objItemCount[o.id] = (objItemCount[o.id] || 0) + 1;
        const item = { domain, objective: o.id, section: fallback.sec, pass: "discretionary", direction: "inverted", kind: "reuse-inverted", id: facetId };
        items.push(item);
        reuseInvertedPicks.push(item);
        placed = true;
        break;
      }
    }
    if (!placed) throw new Error(`Discretionary pass: domain ${domain} has no objective left that can supply an item (${need} still needed)`);
    need--;
  }
}

const byDomainCount = {};
items.forEach((i) => (byDomainCount[i.domain] = (byDomainCount[i.domain] || 0) + 1));
for (const d of Object.keys(QUOTA)) {
  if (byDomainCount[d] !== QUOTA[d]) throw new Error(`Domain ${d} count mismatch: got ${byDomainCount[d]}, want ${QUOTA[d]}`);
}
if (items.length !== 63) throw new Error(`Total items ${items.length} !== 63`);

fs.writeFileSync(path.join(scriptDir, "plan-raw.json"), JSON.stringify({ items, sectionCountThisPaper, objItemCount, reuseInvertedPicks }, null, 1));

console.log(`Built ${items.length} items across ${Object.keys(byDomainCount).length} domains.`);
console.log("Domain counts:", JSON.stringify(byDomainCount));
console.log("D2 items:", JSON.stringify(items.filter((i) => i.domain === "D2").map((i) => `${i.section}:${i.kind}:${i.id}`)));
console.log("Reuse-inverted fallback picks (exhausted objective, no fresh/misconception left):", JSON.stringify(reuseInvertedPicks.map((i) => `${i.domain}/${i.section}(${i.objective}):${i.id}`)));
console.log("Sections used per domain:", JSON.stringify(sectionCountThisPaper));
console.log("Wrote plan-raw.json");
