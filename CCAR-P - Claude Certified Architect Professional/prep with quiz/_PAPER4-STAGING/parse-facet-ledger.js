#!/usr/bin/env node
/*
 * Parses ../FACET-LEDGER.md into structured facet + misconception-unit rows, cross-references
 * with prior-papers-analysis.json (ground truth of what Papers 1-3 actually shipped, per §4a of
 * the Paper 4 generation prompt) to compute remaining fresh supply per section/domain.
 */
const fs = require("fs");

const ledger = fs.readFileSync("../FACET-LEDGER.md", "utf8").split("\n");
const priorPapers = JSON.parse(fs.readFileSync("prior-papers-analysis.json", "utf8"));

const usedFacets = new Set();
const usedMisconceptions = new Set();
for (const p of ["1", "2", "3"]) {
  priorPapers[p].forEach((it) => {
    if (it.facet && it.facet.startsWith("F-")) usedFacets.add(it.facet);
    if (it.facet && it.facet.startsWith("M-")) usedMisconceptions.add(it.facet);
    if (it.facet && it.facet.includes("+")) {
      it.facet.split("+").forEach((f) => { if (f.startsWith("F-")) usedFacets.add(f); });
    }
  });
}

let domain = null;
const facets = [];
const misconceptions = [];
let inMisconceptionTable = false;

for (const line of ledger) {
  const dm = line.match(/^### (D\d)/);
  if (dm) { domain = dm[1]; continue; }
  if (line.startsWith("## Misconception units")) { inMisconceptionTable = true; domain = null; continue; }
  if (line.startsWith("## Canonical worked examples")) { inMisconceptionTable = false; continue; }

  if (!inMisconceptionTable) {
    const fm = line.match(/^\|\s*`(F-[\d.]+-\d+)`\s*\|\s*([\d.]+)\s*\|\s*(O[\d.]+)\s*\|/);
    if (fm && domain) {
      facets.push({ id: fm[1], sec: fm[2], obj: fm[3], domain });
    }
  } else {
    const mm = line.match(/^\|\s*`(M-[\d.]+)`\s*\|\s*([\d.]+)\s*\|\s*(O[\d.]+)\s*\|/);
    if (mm) {
      const sec = mm[2];
      const d = "D" + sec.split(".")[0];
      misconceptions.push({ id: mm[1], sec, obj: mm[3], domain: d });
    }
  }
}

const sections = {};
for (const f of facets) {
  if (!sections[f.sec]) sections[f.sec] = { domain: f.domain, obj: f.obj, total: 0, usedCount: 0, fresh: [], usedIds: [] };
  sections[f.sec].total++;
  if (usedFacets.has(f.id)) { sections[f.sec].usedCount++; sections[f.sec].usedIds.push(f.id); }
  else sections[f.sec].fresh.push(f.id);
}

for (const sec of Object.keys(sections)) {
  sections[sec].whollyUntouched = sections[sec].usedCount === 0;
  sections[sec].exhausted = sections[sec].fresh.length === 0 && sections[sec].total > 0;
}

const misconceptionsBySection = {};
misconceptions.forEach((m) => (misconceptionsBySection[m.sec] = { ...m, used: usedMisconceptions.has(m.id) }));

fs.writeFileSync(
  "facet-supply.json",
  JSON.stringify({ facets, misconceptions, sections, misconceptionsBySection, usedFacetsCount: usedFacets.size, usedMisconceptionsCount: usedMisconceptions.size }, null, 1)
);

const byDomain = {};
Object.entries(sections).forEach(([sec, s]) => {
  (byDomain[s.domain] = byDomain[s.domain] || []).push({ sec, ...s });
});
for (const d of Object.keys(byDomain).sort()) {
  console.log(`\n=== ${d} ===`);
  byDomain[d].sort((a, b) => a.sec.localeCompare(b.sec, undefined, { numeric: true }));
  byDomain[d].forEach((s) => {
    const mUnit = misconceptionsBySection[s.sec];
    console.log(
      `  ${s.sec} (${s.obj}): total=${s.total} used=${s.usedCount} fresh=${s.fresh.length}` +
        `${s.exhausted ? " EXHAUSTED" : ""}${s.whollyUntouched ? " UNTOUCHED" : ""}` +
        (mUnit ? ` [M-unit: ${mUnit.id} ${mUnit.used ? "USED" : "avail"}]` : "")
    );
  });
}
console.log(
  "\nD2 sections with NO fresh facet (direction-inverted-reuse candidates):",
  Object.entries(sections)
    .filter(([sec, s]) => s.domain === "D2" && s.fresh.length === 0)
    .map(([sec, s]) => {
      const mUnit = misconceptionsBySection[sec];
      return `${sec}${mUnit && !mUnit.used ? " (M-unit still avail)" : " (fully exhausted)"}`;
    })
);
console.log("\nWrote facet-supply.json");
