#!/usr/bin/env node
/*
 * Finalizes the Paper 3 central plan: g-numbering, multi-response designation (8 of 63, chosen
 * from sections already proven multi-capable in Papers 1-2), correct-letter pre-plan for the 55
 * single-answer items ({A x14, B x13, C x14, D x14} -- Paper 3's short letter is B), correct-pair
 * assignment for the 8 multi items (cap <=2 repeats), and a shape suggestion per item (soft
 * target 6-9/shape, per ARCHETYPE-LEDGER.md's documented shape<->section affinities).
 * Writes plan.json (machine) and p3-slots.md (human-readable) -- the durable artifact every
 * authoring sub-batch is handed, per Phase 6 of the Paper 3/4 generation prompt.
 */
const fs = require("fs");
const { items: rawItems } = require("./plan-raw.json");

const DOMAIN_ORDER = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"];

// Sections proven to hold >=2 independently-true rows for one situation, evidenced by their use
// as a P1 or P2 multi-response item's section (see prior-papers-analysis.json).
const PROVEN_MULTI_SECTIONS = {
  D1: ["1.6", "1.5"], D2: ["2.2"], D3: ["3.11", "3.3", "3.10"],
  D4: ["4.9"], D5: ["5.6", "5.5"], D6: ["6.12", "6.11"], D7: ["7.2", "7.8"],
};
// How many multi items each domain supplies this paper (8 total; D7 supplies 2, matching both
// prior papers' pattern of one domain absorbing the "extra" multi item).
const MULTI_COUNT = { D1: 1, D2: 1, D3: 1, D4: 1, D5: 1, D6: 1, D7: 2 };

// Shape affinity hints, from ARCHETYPE-LEDGER.md Part 1's "Official evidence" / "Corpus" column.
// Soft guidance only -- authors may substitute a better-fitting shape for the actual facet text.
const SHAPE_HINTS = {
  "1.3": "S5", "1.4": "S5", "1.1": "S6", "1.2": "S6", "1.9": "S1", "1.10": "S4", "1.11": "S5",
  "1.12": "S2", "1.5": "S5", "1.6": "S1", "1.7": "S1", "1.8": "S4",
  "2.1": "S5", "2.2": "S2", "2.3": "S1", "2.4": "S4", "2.5": "S6", "2.6": "S2", "2.7": "S2",
  "2.8": "S2", "2.9": "S8",
  "3.1": "S4", "3.2": "S1", "3.3": "S2", "3.4": "S5", "3.5": "S1", "3.6": "S1", "3.7": "S6",
  "3.8": "S4", "3.9": "S1", "3.10": "S3", "3.11": "S4", "3.12": "S1", "3.13": "S4", "3.14": "S1",
  "4.1": "S6", "4.2": "S3", "4.3": "S6", "4.4": "S6", "4.5": "S6", "4.6": "S1", "4.7": "S1",
  "4.8": "S6", "4.9": "S3", "4.10": "S4", "4.11": "S1", "4.12": "S1",
  "5.1": "S1", "5.2": "S8", "5.3": "S8", "5.4": "S8", "5.5": "S2", "5.6": "S3", "5.7": "S1",
  "5.8": "S2", "5.9": "S1", "5.10": "S6", "5.11": "S1",
  "6.1": "S7", "6.2": "S7", "6.3": "S7", "6.4": "S7", "6.6": "S7", "6.7": "S3", "6.8": "S7",
  "6.9": "S7", "6.10": "S6", "6.11": "S1", "6.12": "S7",
  "7.1": "S3", "7.2": "S3", "7.3": "S5", "7.5": "S4", "7.8": "S2",
};

// --- 1. Order items by domain, mark multi-response slots ---
const byDomain = {};
DOMAIN_ORDER.forEach((d) => (byDomain[d] = rawItems.filter((i) => i.domain === d)));

let g = 1;
const finalItems = [];
for (const d of DOMAIN_ORDER) {
  const domainItems = [...byDomain[d]];
  // Pick multi-response candidates: items whose section is in PROVEN_MULTI_SECTIONS, preferring
  // the facet-kind picks (a real decision-table row) over a misconception-unit pick.
  const provenSet = new Set(PROVEN_MULTI_SECTIONS[d] || []);
  const candidates = domainItems
    .map((it, idx) => ({ it, idx }))
    .filter(({ it }) => provenSet.has(it.section))
    .sort((a, b) => (a.it.kind === "facet" ? 0 : 1) - (b.it.kind === "facet" ? 0 : 1));
  const chosenIdx = new Set();
  const need = MULTI_COUNT[d] || 0;
  const usedSections = new Set();
  for (const c of candidates) {
    if (chosenIdx.size >= need) break;
    if (usedSections.has(c.it.section)) continue; // spread across distinct sections if possible
    chosenIdx.add(c.idx);
    usedSections.add(c.it.section);
  }
  domainItems.forEach((it, idx) => {
    it.format = chosenIdx.has(idx) ? "multi" : "single";
    it.selectN = chosenIdx.has(idx) ? 2 : 1;
    it.shape = SHAPE_HINTS[it.section] || "S1";
    it.g = g++;
    finalItems.push(it);
  });
}

// --- 2. Correct-letter pre-plan for the 55 single-answer items ---
// Paper 3 short letter is B: {A x14, B x13, C x14, D x14}. Deterministic shuffle (seeded LCG so
// the plan is reproducible if re-run).
function seededShuffle(arr, seed) {
  let s = seed;
  const rnd = () => {
    s = (s * 1103515245 + 12345) % 2147483648;
    return s / 2147483648;
  };
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
const letterMultiset = [
  ...Array(14).fill("A"), ...Array(13).fill("B"), ...Array(14).fill("C"), ...Array(14).fill("D"),
];
const shuffledLetters = seededShuffle(letterMultiset, 3130831 /* Paper 3 seed */);
let li = 0;
for (const it of finalItems) {
  if (it.format === "single") it.correctLetter = shuffledLetters[li++];
}

// --- 3. Correct-pair assignment for the 8 multi items, cap <=2 repeats ---
const PAIRS = ["AB", "AC", "AD", "BC", "BD", "CD"];
const pairPlan = ["AB", "AC", "BD", "AD", "BC", "CD", "AB", "CD"]; // 8 slots, each pair <=2x
let pi = 0;
for (const it of finalItems) {
  if (it.format === "multi") it.correctPair = pairPlan[pi++];
}

// --- Sanity ---
const singleCount = finalItems.filter((i) => i.format === "single").length;
const multiCount = finalItems.filter((i) => i.format === "multi").length;
if (singleCount !== 55) throw new Error(`single count ${singleCount} != 55`);
if (multiCount !== 8) throw new Error(`multi count ${multiCount} != 8`);
const letterTally = {};
finalItems.filter((i) => i.format === "single").forEach((i) => (letterTally[i.correctLetter] = (letterTally[i.correctLetter] || 0) + 1));
const pairTally = {};
finalItems.filter((i) => i.format === "multi").forEach((i) => (pairTally[i.correctPair] = (pairTally[i.correctPair] || 0) + 1));
const shapeTally = {};
finalItems.forEach((i) => (shapeTally[i.shape] = (shapeTally[i.shape] || 0) + 1));

fs.writeFileSync("plan.json", JSON.stringify(finalItems, null, 1));

console.log("g range:", finalItems[0].g, "-", finalItems[finalItems.length - 1].g);
console.log("letter tally:", JSON.stringify(letterTally));
console.log("pair tally:", JSON.stringify(pairTally));
console.log("shape tally:", JSON.stringify(shapeTally));
console.log("multi items:", finalItems.filter((i) => i.format === "multi").map((i) => `g${i.g} ${i.domain} ${i.section}`));
console.log("Wrote plan.json");
