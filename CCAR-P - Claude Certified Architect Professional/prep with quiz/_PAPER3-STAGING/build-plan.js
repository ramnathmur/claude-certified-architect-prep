#!/usr/bin/env node
/*
 * Central plan builder for Paper 3 (untargeted diagnostic, per §2 of the Paper 3/4 generation
 * prompt — Papers 1 and 2 are both generated but not yet sat). Implements:
 *   - objective floor pass (38 items, 1 per objective)
 *   - discretionary pass (25 items, cap 3/objective)
 *   - facet freshness (excludes every facet used in Papers 1-2; falls back to a section's
 *     misconception unit once that section's facets are exhausted, per Phase 4 rule 5)
 *   - section cap <=2 items/paper
 * Output: plan.json (machine) + p3-slots.md (human-readable, written to disk per §0).
 */
const fs = require("fs");

const supply = JSON.parse(fs.readFileSync("facet-supply.json", "utf8"));
const objMapRaw = fs.readFileSync("../CCAR-P_Objective-Map_v1.md", "utf8");

// Parse the 38-objective table (id, domain, objective text, sections)
const objectives = []; // {id, domain, text, sections: [secIds]}
for (const line of objMapRaw.split("\n")) {
  const m = line.match(/^\|\s*\*\*(O[\d.]+)\*\*\s*\|\s*(D\d)\s*\|\s*([^|]+)\|\s*([\d.,\s]+)\|\s*(\d+)\s*\|/);
  if (m) {
    objectives.push({
      id: m[1],
      domain: m[2],
      text: m[3].trim(),
      sections: m[4].split(",").map((s) => s.trim()).filter(Boolean),
    });
  }
}

const QUOTA = { D1: 11, D2: 8, D3: 12, D4: 10, D5: 9, D6: 9, D7: 4 };
const DISCRETIONARY = { D1: 5, D2: 3, D3: 4, D4: 4, D5: 4, D6: 4, D7: 1 };

// Working copies of section fresh-facet pools (mutated as we allocate)
const freshPool = {}; // sec -> [facetIds] (mutable)
Object.entries(supply.sections).forEach(([sec, s]) => (freshPool[sec] = [...s.fresh]));
const miscUsedThisPaper = new Set(); // M-unit ids already claimed this paper
const sectionCountThisPaper = {}; // sec -> count
const misconceptionBySection = {};
supply.misconceptions.forEach((m) => (misconceptionBySection[m.sec] = m.id));

function secInfo(sec) {
  // Sections with no decision table (6.5, 7.4, 7.6, 7.7) have no entry in supply.sections —
  // they can only supply items via their misconception unit.
  return supply.sections[sec] || { usedCount: 0, fresh: [], total: 0 };
}

function pickFromSection(sec) {
  // Prefer a fresh facet; else fall back to that section's (unused-this-paper) misconception unit.
  if (freshPool[sec] && freshPool[sec].length > 0) {
    const id = freshPool[sec].shift();
    return { kind: "facet", id };
  }
  const mUnit = misconceptionBySection[sec];
  if (mUnit && !miscUsedThisPaper.has(mUnit)) {
    miscUsedThisPaper.add(mUnit);
    return { kind: "misconception", id: mUnit };
  }
  return null; // section genuinely cannot supply another item this paper
}

function bestSection(sections, { excludeAtCap = true } = {}) {
  // Rank candidate sections: prefer higher fresh count, then lower usedCount (less drawn on
  // historically), then lower current in-paper count, then section id for determinism.
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

const items = []; // {domain, objective, section, facetOrMisc, kind}
const objItemCount = {};

// --- Floor pass: exactly one item per objective ---
for (const o of objectives) {
  const sec = bestSection(o.sections);
  if (!sec) throw new Error(`Floor pass: no section available for ${o.id}`);
  const pick = pickFromSection(sec);
  if (!pick) throw new Error(`Floor pass: pickFromSection failed for ${sec}`);
  sectionCountThisPaper[sec] = (sectionCountThisPaper[sec] || 0) + 1;
  objItemCount[o.id] = (objItemCount[o.id] || 0) + 1;
  items.push({ domain: o.domain, objective: o.id, section: sec, pass: "floor", ...pick });
}

// --- Discretionary pass: per domain, spread across its own objectives, cap 3/objective ---
for (const domain of Object.keys(QUOTA)) {
  const domainObjs = objectives.filter((o) => o.domain === domain);
  let need = DISCRETIONARY[domain];
  while (need > 0) {
    // pick the objective in this domain with fewest items so far (ties: id order)
    const candidateObjs = domainObjs.filter((o) => (objItemCount[o.id] || 0) < 3);
    if (candidateObjs.length === 0) throw new Error(`Discretionary pass: ${domain} objective caps exhausted with ${need} still needed`);
    candidateObjs.sort((a, b) => (objItemCount[a.id] || 0) - (objItemCount[b.id] || 0) || a.id.localeCompare(b.id));
    // Try objectives in fewest-items-first order; skip one that has no section left to give
    // (e.g. a single-section D2 objective whose one section and one misconception unit are
    // both already spent this paper) rather than treating that as a hard planning failure.
    let placed = false;
    for (const o of candidateObjs) {
      const sec = bestSection(o.sections);
      if (!sec) continue;
      const pick = pickFromSection(sec);
      if (!pick) continue;
      sectionCountThisPaper[sec] = (sectionCountThisPaper[sec] || 0) + 1;
      objItemCount[o.id] = (objItemCount[o.id] || 0) + 1;
      items.push({ domain, objective: o.id, section: sec, pass: "discretionary", ...pick });
      placed = true;
      break;
    }
    if (!placed) throw new Error(`Discretionary pass: domain ${domain} has no objective left that can supply an item (${need} still needed) — real corpus supply exhaustion, needs Ram's decision`);
    need--;
  }
}

// Sanity checks
const byDomainCount = {};
items.forEach((i) => (byDomainCount[i.domain] = (byDomainCount[i.domain] || 0) + 1));
for (const d of Object.keys(QUOTA)) {
  if (byDomainCount[d] !== QUOTA[d]) throw new Error(`Domain ${d} count mismatch: got ${byDomainCount[d]}, want ${QUOTA[d]}`);
}
if (items.length !== 63) throw new Error(`Total items ${items.length} !== 63`);

fs.writeFileSync("plan-raw.json", JSON.stringify({ items, sectionCountThisPaper, objItemCount }, null, 1));

console.log(`Built ${items.length} items across ${Object.keys(byDomainCount).length} domains.`);
console.log("Domain counts:", JSON.stringify(byDomainCount));
console.log("Misconception units used this paper:", [...miscUsedThisPaper].sort());
console.log("Wrote plan-raw.json");
