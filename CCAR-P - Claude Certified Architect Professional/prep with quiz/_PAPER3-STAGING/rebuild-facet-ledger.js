#!/usr/bin/env node
/*
 * Rebuilds FACET-LEDGER.md's "used" column from the three shipped papers directly (never from the
 * ledger's own prior content, which §3d of the Paper 3/4 generation prompt documented as having at
 * least one gap). Also marks which misconception units Paper 3 drew on -- the first paper to use
 * any. Handles the two Paper 3 multi-response items whose `facet` field is a compound
 * "F-x+F-y" string (both constituent rows are marked used).
 */
const fs = require("fs");
const priorPapers = JSON.parse(fs.readFileSync("prior-papers-analysis.json", "utf8"));
const p3items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

const usedBy = {}; // facetId -> Set of "P1"/"P2"/"P3"
function record(facetId, paperTag) {
  if (!facetId) return;
  for (const id of facetId.split("+")) {
    (usedBy[id] = usedBy[id] || new Set()).add(paperTag);
  }
}
priorPapers["1"].forEach((it) => record(it.facet, "P1"));
priorPapers["2"].forEach((it) => record(it.facet, "P2"));
p3items.forEach((it) => record(it.facet, "P3"));

const lines = fs.readFileSync("../FACET-LEDGER.md", "utf8").split("\n");
let changedFacetRows = 0;
let changedMiscRows = 0;
let inMisconceptionTable = false;

const FACET_ROW_RE = /^\|\s*`(F-[\d.]+-\d+)`\s*\|([^|]*\|[^|]*\|[^|]*\|[^|]*)\|([^|]*)\|\s*$/;
const MISC_ROW_RE = /^\|\s*`(M-[\d.]+)`\s*\|/;

const out = lines.map((line) => {
  if (line.startsWith("## Misconception units")) inMisconceptionTable = true;
  if (line.startsWith("## Canonical worked examples")) inMisconceptionTable = false;

  if (!inMisconceptionTable) {
    const m = line.match(FACET_ROW_RE);
    if (!m) return line;
    const facetId = m[1];
    const marks = usedBy[facetId];
    if (!marks) return line;
    changedFacetRows++;
    const newUsedCol = " " + [...marks].map((p) => `${p}:normal:?`).join(", ") + " ";
    return `| \`${facetId}\` |${m[2]}|${newUsedCol}|`;
  } else {
    const mm = line.match(MISC_ROW_RE);
    if (!mm) return line;
    const unitId = mm[1];
    const usedInP3 = p3items.some((it) => (it.facet || "").split("+").includes(unitId));
    if (!usedInP3) return line;
    changedMiscRows++;
    if (line.trimEnd().endsWith("|")) {
      return line.replace(/\|\s*$/, " **[used: P3:normal:?]** |");
    }
    return line;
  }
});

fs.writeFileSync("../FACET-LEDGER.md", out.join("\n"));
console.log("Facet rows updated:", changedFacetRows);
console.log("Misconception rows marked used:", changedMiscRows);

// sanity: confirm line count unchanged
console.log("Line count in:", lines.length, "out:", out.length);
