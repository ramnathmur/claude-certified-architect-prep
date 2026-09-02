#!/usr/bin/env node
/*
 * Runs the parts of Phase 6's fidelity gate that tools/run-gate.js's mechanized checks (1, 10,
 * 11, 14) do not cover: objective cap, multi-pair repeat cap, t1Clause/t1Alt presence/validity.
 * Also runs the D7 §7.2 structural-duplication check the Paper 5 dispatch specifically asked
 * for (F-29: only two positive mechanism rows exist there, so any two papers' 7.2 multi-response
 * items tend to converge on the same pairing).
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

console.log("\n=== D7 §7.2 structural-duplication check (F-29) ===");
const d72 = items.find((i) => i.section === "7.2");
if (d72) {
  console.log(`This paper's 7.2 item: g${d72.g}, facet=${d72.facet}, format=${d72.format}, correct=${d72.correct}`);
  const priorAll = JSON.parse(fs.readFileSync("prior-papers-analysis.json", "utf8"));
  console.log("Prior papers' own 7.2/7.8 items (facet + section), for a structural-pairing comparison:");
  for (const pnum of ["1", "2", "3", "4"]) {
    priorAll[pnum].forEach((pi) => {
      if (pi.section === "7.2" || pi.section === "7.8") {
        console.log(`  Paper ${pnum} g${pi.g}: section ${pi.section}, facet ${pi.facet}, format ${pi.format}`);
      }
    });
  }
  console.log("Manually compare g" + d72.g + "'s stem/mechanism-pairing against each row above before shipping.");
} else {
  console.log("No 7.2 item this paper -- check N/A.");
}
