#!/usr/bin/env node
/*
 * Rebuilds FACET-LEDGER.md's "used" column from all four shipped papers directly (never from
 * the ledger's own prior content). Fix vs Papers 1-3's rebuild scripts: those hardcoded
 * "P<n>:normal:?" regardless of the item's actual direction -- harmless while every item was
 * normal-direction, but wrong now that Paper 4 ships 17 genuinely inverted items, and this
 * ledger is what future papers' facet-reuse-ban tracking (shape,section,facet,direction) reads.
 */
const fs = require("fs");
const priorPapers = JSON.parse(fs.readFileSync("prior-papers-analysis.json", "utf8"));
const p4items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

const usedBy = {}; // facetId -> Set of "P1:normal" / "P4:inverted" etc.
function record(facetId, paperTag, direction) {
  if (!facetId) return;
  for (const id of facetId.split("+")) {
    (usedBy[id] = usedBy[id] || new Set()).add(`${paperTag}:${direction || "normal"}`);
  }
}
priorPapers["1"].forEach((it) => record(it.facet, "P1", it.direction));
priorPapers["2"].forEach((it) => record(it.facet, "P2", it.direction));
priorPapers["3"].forEach((it) => record(it.facet, "P3", it.direction));
p4items.forEach((it) => record(it.facet, "P4", it.direction));

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
    const newUsedCol = " " + [...marks].map((tag) => `${tag}:?`).join(", ") + " ";
    return `| \`${facetId}\` |${m[2]}|${newUsedCol}|`;
  } else {
    const mm = line.match(MISC_ROW_RE);
    if (!mm) return line;
    const unitId = mm[1];
    const p4Item = p4items.find((it) => (it.facet || "").split("+").includes(unitId));
    if (!p4Item) return line;
    changedMiscRows++;
    if (line.trimEnd().endsWith("|")) {
      return line.replace(/\|\s*$/, ` **[used: P4:${p4Item.direction}:?]** |`);
    }
    return line;
  }
});

fs.writeFileSync("../FACET-LEDGER.md", out.join("\n"));
console.log("Facet rows updated:", changedFacetRows);
console.log("Misconception rows marked used:", changedMiscRows);
console.log("Line count in:", lines.length, "out:", out.length);
