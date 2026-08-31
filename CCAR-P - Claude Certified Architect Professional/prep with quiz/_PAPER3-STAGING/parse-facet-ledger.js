#!/usr/bin/env node
/*
 * Parses ../FACET-LEDGER.md into structured facet + misconception-unit rows, cross-references
 * with prior-papers-analysis.json (ground truth of what Papers 1-2 actually shipped, per §3d of
 * the Paper 3/4 generation prompt) to compute remaining fresh supply per section/domain.
 */
const fs = require("fs");

const ledger = fs.readFileSync("../FACET-LEDGER.md", "utf8").split("\n");
const priorPapers = JSON.parse(fs.readFileSync("prior-papers-analysis.json", "utf8"));

const usedFacets = new Set();
for (const p of ["1", "2"]) {
  priorPapers[p].forEach((it) => { if (it.facet) usedFacets.add(it.facet); });
}

let domain = null;
const facets = []; // {id, sec, obj, domain}
const misconceptions = []; // {id, sec, obj, domain}
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

// Per-section aggregation
const sections = {}; // sec -> {domain, obj, total, used, fresh: []}
for (const f of facets) {
  if (!sections[f.sec]) sections[f.sec] = { domain: f.domain, obj: f.obj, total: 0, usedCount: 0, fresh: [] };
  sections[f.sec].total++;
  if (usedFacets.has(f.id)) sections[f.sec].usedCount++;
  else sections[f.sec].fresh.push(f.id);
}

// Which sections are wholly untouched by P1+P2 (best fresh material)
for (const sec of Object.keys(sections)) {
  sections[sec].whollyUntouched = sections[sec].usedCount === 0;
  sections[sec].exhausted = sections[sec].fresh.length === 0 && sections[sec].total > 0;
}

const misconceptionsBySection = {};
misconceptions.forEach((m) => (misconceptionsBySection[m.sec] = m));

fs.writeFileSync(
  "facet-supply.json",
  JSON.stringify({ facets, misconceptions, sections, usedFacetsCount: usedFacets.size }, null, 1)
);

// Report per domain
const byDomain = {};
Object.entries(sections).forEach(([sec, s]) => {
  (byDomain[s.domain] = byDomain[s.domain] || []).push({ sec, ...s });
});
for (const d of Object.keys(byDomain).sort()) {
  console.log(`\n=== ${d} ===`);
  byDomain[d].sort((a, b) => a.sec.localeCompare(b.sec, undefined, { numeric: true }));
  byDomain[d].forEach((s) => {
    console.log(
      `  ${s.sec} (${s.obj}): total=${s.total} used=${s.usedCount} fresh=${s.fresh.length}` +
        `${s.exhausted ? " EXHAUSTED" : ""}${s.whollyUntouched ? " UNTOUCHED" : ""}` +
        (misconceptionsBySection[s.sec] ? ` [M-unit: ${misconceptionsBySection[s.sec].id} avail]` : "")
    );
  });
}
console.log("\nWrote facet-supply.json");
