#!/usr/bin/env node
/*
 * Central plan builder for Paper 4 (untargeted diagnostic, per §3 of the Paper 4 generation
 * prompt -- confirmed with Ram: Papers 1-3 are generated but none sat yet). Implements:
 *   - D2 HARD-CODED per Ram's approved decision (§2): 3 items from the unused misconception
 *     units (M-2.3, M-2.5, M-2.9), 5 items from direction-inverted reuse of an already-used
 *     facet in a section with zero fresh facets left (2.1, 2.2, 2.4, 2.7, 2.8).
 *   - D1, D3-D7: same freshness-greedy floor+discretionary algorithm Papers 2-3 used, facet
 *     exclusion list computed from Papers 1-3's actually-shipped HTML (facet-supply.json).
 * Output: plan-raw.json.
 */
const fs = require("fs");

const supply = JSON.parse(fs.readFileSync("facet-supply.json", "utf8"));
const objMapRaw = fs.readFileSync("../CCAR-P_Objective-Map_v1.md", "utf8");

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
const DISCRETIONARY = { D1: 5, D2: 0, D3: 4, D4: 4, D5: 4, D6: 4, D7: 1 }; // D2 fully hard-coded

// --- D2: hard-coded per Ram's approved decision, 2026-08-31 ---
// Reuse anchor = the section's own primary (01) facet; the authoring sub-batch inverts the
// axis per the shape's inversion definition (ARCHETYPE-LEDGER.md), producing a genuinely
// different correct answer -- not a restate of the anchor facet's own lesson.
const D2_PLAN = [
  { domain: "D2", objective: "O2.1", section: "2.1", pass: "floor", kind: "reuse-inverted", id: "F-2.1-01", direction: "inverted" },
  { domain: "D2", objective: "O2.2", section: "2.2", pass: "floor", kind: "reuse-inverted", id: "F-2.2-01", direction: "inverted" },
  { domain: "D2", objective: "O2.3", section: "2.3", pass: "floor", kind: "misconception", id: "M-2.3", direction: "normal" },
  { domain: "D2", objective: "O2.4", section: "2.5", pass: "floor", kind: "misconception", id: "M-2.5", direction: "normal" },
  { domain: "D2", objective: "O2.5", section: "2.9", pass: "floor", kind: "misconception", id: "M-2.9", direction: "normal" },
  { domain: "D2", objective: "O2.3", section: "2.4", pass: "discretionary", kind: "reuse-inverted", id: "F-2.4-01", direction: "inverted" },
  { domain: "D2", objective: "O2.4", section: "2.7", pass: "discretionary", kind: "reuse-inverted", id: "F-2.7-01", direction: "inverted" },
  { domain: "D2", objective: "O2.5", section: "2.8", pass: "discretionary", kind: "reuse-inverted", id: "F-2.8-01", direction: "inverted" },
];

// --- Generic algorithm for D1, D3-D7 (unchanged from Paper 3) ---
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

const items = [...D2_PLAN];
const objItemCount = {};
D2_PLAN.forEach((it) => (objItemCount[it.objective] = (objItemCount[it.objective] || 0) + 1));
// D2 sections are hard-coded above; keep sectionCountThisPaper in sync so nothing double-books.
D2_PLAN.forEach((it) => (sectionCountThisPaper[it.section] = (sectionCountThisPaper[it.section] || 0) + 1));

const genericDomains = Object.keys(QUOTA).filter((d) => d !== "D2");

// Floor pass: one item per objective, D1/D3-D7 only (D2 objectives already satisfied above)
for (const o of objectives) {
  if (o.domain === "D2") continue;
  const sec = bestSection(o.sections);
  if (!sec) throw new Error(`Floor pass: no section available for ${o.id}`);
  const pick = pickFromSection(sec);
  if (!pick) throw new Error(`Floor pass: pickFromSection failed for ${sec}`);
  sectionCountThisPaper[sec] = (sectionCountThisPaper[sec] || 0) + 1;
  objItemCount[o.id] = (objItemCount[o.id] || 0) + 1;
  items.push({ domain: o.domain, objective: o.id, section: sec, pass: "floor", direction: "normal", ...pick });
}

// Discretionary pass, D1/D3-D7 only
for (const domain of genericDomains) {
  const domainObjs = objectives.filter((o) => o.domain === domain);
  let need = DISCRETIONARY[domain];
  while (need > 0) {
    const candidateObjs = domainObjs.filter((o) => (objItemCount[o.id] || 0) < 3);
    if (candidateObjs.length === 0) throw new Error(`Discretionary pass: ${domain} objective caps exhausted with ${need} still needed`);
    candidateObjs.sort((a, b) => (objItemCount[a.id] || 0) - (objItemCount[b.id] || 0) || a.id.localeCompare(b.id));
    let placed = false;
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

fs.writeFileSync("plan-raw.json", JSON.stringify({ items, sectionCountThisPaper, objItemCount }, null, 1));

console.log(`Built ${items.length} items across ${Object.keys(byDomainCount).length} domains.`);
console.log("Domain counts:", JSON.stringify(byDomainCount));
console.log("D2 items (hard-coded):", JSON.stringify(D2_PLAN.map((i) => `${i.section}:${i.kind}:${i.id}`)));
console.log("Sections used, D1/D3-D7:", JSON.stringify(
  items.filter((i) => i.domain !== "D2").map((i) => `${i.domain}/${i.section}(${i.objective})`)
));
console.log("Wrote plan-raw.json");
