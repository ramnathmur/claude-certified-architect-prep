#!/usr/bin/env node
/*
 * Rebuilds FACET-LEDGER.md's "used" column from all five shipped papers directly (never from
 * the ledger's own prior content), continuing Paper 4's fix of using each item's real
 * `direction` field rather than hardcoding "normal".
 */
const fs = require("fs");
const priorPapers = JSON.parse(fs.readFileSync("prior-papers-analysis.json", "utf8")); // Papers 1-4
const p5items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

const usedBy = {}; // facetId -> Set of "P1:normal" / "P5:inverted" etc.
function record(facetId, paperTag, direction) {
  if (!facetId) return;
  for (const id of facetId.split("+")) {
    (usedBy[id] = usedBy[id] || new Set()).add(`${paperTag}:${direction || "normal"}`);
  }
}
priorPapers["1"].forEach((it) => record(it.facet, "P1", it.direction));
priorPapers["2"].forEach((it) => record(it.facet, "P2", it.direction));
priorPapers["3"].forEach((it) => record(it.facet, "P3", it.direction));
priorPapers["4"].forEach((it) => record(it.facet, "P4", it.direction));
p5items.forEach((it) => record(it.facet, "P5", it.direction));

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
    const p5Item = p5items.find((it) => (it.facet || "").split("+").includes(unitId));
    if (!p5Item) return line;
    changedMiscRows++;
    if (/\*\*\[used:/.test(line)) return line; // already marked used by an earlier paper (e.g. Paper 3)
    if (line.trimEnd().endsWith("|")) {
      return line.replace(/\|\s*$/, ` **[used: P5:${p5Item.direction}:?]** |`);
    }
    return line;
  }
});

fs.writeFileSync("../FACET-LEDGER.md", out.join("\n"));
console.log("Facet rows updated:", changedFacetRows);
console.log("Misconception rows marked used:", changedMiscRows);
console.log("Line count in:", lines.length, "out:", out.length);
