#!/usr/bin/env node
/*
 * Runs the parts of Phase 6's fidelity gate that tools/run-gate.js's validateItems() does not
 * cover: objective cap, multi-pair repeat cap, t1Clause/t1Alt presence, stem-Jaccard against
 * STEM-LEDGER.md (should now hold 48+63+63+63=237 stems), and (section, facet, shape) triple
 * reuse against ARCHETYPE-LEDGER.md's historical rows.
 */
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

console.log("=== Check 5: objective coverage (>3 is a violation) ===");
const objCounts = {};
items.forEach((i) => (objCounts[i.objective] = (objCounts[i.objective] || 0) + 1));
const over = Object.entries(objCounts).filter(([k, v]) => v > 3);
console.log("objectives with >3 items:", over.length ? over : "none");
console.log("distinct objectives used:", Object.keys(objCounts).length, "/ 38");

console.log("\n=== Check 7: multi-response pair repeats (>2 is a violation) ===");
const pairCounts = {};
items.filter((i) => i.format === "multi").forEach((i) => {
  const pair = i.correct.slice().sort().join("");
  pairCounts[pair] = (pairCounts[pair] || 0) + 1;
});
console.log("pair tally:", JSON.stringify(pairCounts));
const overPair = Object.entries(pairCounts).filter(([k, v]) => v > 2);
console.log("pairs >2:", overPair.length ? overPair : "none");

console.log("\n=== Check 12: t1Clause/t1Alt presence ===");
const missing = items.filter((i) => !i.t1Clause || !i.t1Alt);
console.log("items missing t1Clause or t1Alt:", missing.length ? missing.map((i) => i.g) : "none");

console.log("\n=== Check 12: t1Alt must be a letter present in opts ===");
const badAlt = items.filter((i) => !i.opts.some((o) => o.l === i.t1Alt));
console.log("items with t1Alt not matching any option letter:", badAlt.length ? badAlt.map((i) => `g${i.g}(${i.t1Alt})`) : "none");

console.log("\n=== Check 11a: (section, facet, shape) triple reuse (>2 historically is a violation) ===");
const archetypeRaw = fs.readFileSync("../ARCHETYPE-LEDGER.md", "utf8");
const historical = [];
for (const line of archetypeRaw.split("\n")) {
  const m = line.match(/^\|\s*(S\d)\s*\|\s*([\d.]+)\s*\|\s*([FM]-[\d.]+(?:-\d+)?(?:\+[FM]-[\d.]+-\d+)?)\s*\|\s*(normal|inverted)\s*\|/);
  if (m) historical.push({ shape: m[1], sec: m[2], facet: m[3] });
}
console.log("historical shape-instance rows parsed:", historical.length, "(expect ~189 from Papers 1-3)");
const tripleCount = {};
historical.forEach((h) => {
  const key = `${h.shape}|${h.sec}|${h.facet}`;
  tripleCount[key] = (tripleCount[key] || 0) + 1;
});
items.forEach((it) => {
  const key = `${it.shape}|${it.section}|${it.facet}`;
  tripleCount[key] = (tripleCount[key] || 0) + 1;
});
const overTriple = Object.entries(tripleCount).filter(([k, v]) => v > 2);
console.log("(shape,section,facet) triples now used >2 times total:", overTriple.length ? overTriple : "none");

console.log("\n=== Check 11b: stem-Jaccard vs STEM-LEDGER.md (threshold 0.30) ===");
const stemLedgerRaw = fs.readFileSync("../STEM-LEDGER.md", "utf8");
const ledgerSigs = [];
for (const line of stemLedgerRaw.split("\n")) {
  const m = line.match(/^\|\s*`([\w-]+)`\s*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*`([^`]*)`\s*\|/);
  if (m) ledgerSigs.push({ id: m[1], sig: new Set(m[2].split(/\s+/).filter(Boolean)) });
}
console.log("ledger signatures parsed:", ledgerSigs.length, "(expect 48+63+63=174 -- Papers 1-3 only, this paper checked separately below)");

const STOPWORDS = new Set(["the","a","an","and","or","of","to","in","on","for","with","at","by","from","is","are","be","this","that","it","its","as","not","no"]);
function sig(stem) {
  return new Set(
    stem.toLowerCase().replace(/[^\w\s]/g, " ").split(/\s+/).filter(Boolean).filter((t) => !STOPWORDS.has(t))
  );
}
function jaccard(a, b) {
  const inter = [...a].filter((x) => b.has(x)).length;
  const union = new Set([...a, ...b]).size;
  return union ? inter / union : 0;
}

let maxScore = 0, maxPair = null;
const flagged = [];
for (const it of items) {
  const s = sig(it.stem);
  for (const row of ledgerSigs) {
    const score = jaccard(s, row.sig);
    if (score > maxScore) { maxScore = score; maxPair = [`g${it.g}`, row.id]; }
    if (score >= 0.3) flagged.push({ g: it.g, against: row.id, score: score.toFixed(3) });
  }
}
console.log("max score vs ledger (Papers 1-3):", maxScore.toFixed(3), maxPair);
console.log("pairs >= 0.30:", flagged.length ? flagged : "none");

console.log("\n=== Check 11c: within-Paper-4 pairwise stem Jaccard (threshold 0.30) ===");
let maxIn = 0, maxInPair = null;
const flaggedIn = [];
for (let i = 0; i < items.length; i++) {
  for (let j = i + 1; j < items.length; j++) {
    const score = jaccard(sig(items[i].stem), sig(items[j].stem));
    if (score > maxIn) { maxIn = score; maxInPair = [`g${items[i].g}`, `g${items[j].g}`]; }
    if (score >= 0.3) flaggedIn.push({ pair: [`g${items[i].g}`, `g${items[j].g}`], score: score.toFixed(3) });
  }
}
console.log("max within-paper score:", maxIn.toFixed(3), maxInPair);
console.log("within-paper pairs >= 0.30:", flaggedIn.length ? flaggedIn : "none");

console.log("\n=== Specifically flagged pairs from sub-batch notes (checked regardless of threshold) ===");
const pairsToCheck = [[43, 48], [60, 62]];
for (const [gA, gB] of pairsToCheck) {
  const a = items.find((i) => i.g === gA);
  const b = items.find((i) => i.g === gB);
  const score = jaccard(sig(a.stem), sig(b.stem));
  console.log(`g${gA} vs g${gB}: Jaccard=${score.toFixed(3)} (threshold 0.30)`);
}
console.log("\ng60/g62 vs their own already-shipped sibling facets (F-7.2-01/03, F-7.8-01/03) across Papers 1-3:");
const priorAll = JSON.parse(fs.readFileSync("prior-papers-analysis.json", "utf8"));
for (const pnum of ["1", "2", "3"]) {
  priorAll[pnum].forEach((pi) => {
    if (["F-7.2-01", "F-7.2-03", "F-7.8-01", "F-7.8-03", "F-7.1-02"].includes(pi.facet)) {
      console.log(`  Paper ${pnum} g${pi.g}: facet ${pi.facet}, section ${pi.section}`);
    }
  });
}
