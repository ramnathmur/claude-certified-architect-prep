#!/usr/bin/env node
/*
 * Paper 3 assembly. Loads all 13 sub-batch files, validates against plan.json, computes
 * lessonKey (F-18's minimum-token-floor fix folded in from the start), runs the cross-domain
 * lesson-collision check, adds the correct[] field from the plan, strips factAnswerRaw, and
 * reports the family tally so an over-cap family can be fixed before the gate runs (F-19).
 */
const fs = require("fs");

const BATCH_FILES = [
  "p3-d1-batch1.json", "p3-d1-batch2.json", "p3-d2-batch1.json", "p3-d2-batch2.json",
  "p3-d3-batch1.json", "p3-d3-batch2.json", "p3-d4-batch1.json", "p3-d4-batch2.json",
  "p3-d5-batch1.json", "p3-d5-batch2.json", "p3-d6-batch1.json", "p3-d6-batch2.json",
  "p3-d7.json",
];

const plan = JSON.parse(fs.readFileSync("plan.json", "utf8"));
const planByG = {};
plan.forEach((p) => (planByG[p.g] = p));

let allItems = [];
let allNotes = [];
for (const f of BATCH_FILES) {
  const raw = JSON.parse(fs.readFileSync(f, "utf8"));
  if (!Array.isArray(raw.items)) throw new Error(`${f}: no items array`);
  raw.items.forEach((it) => (it._srcFile = f));
  allItems.push(...raw.items);
  (raw.notes || []).forEach((n) => allNotes.push(`[${f}] ${n}`));
}

if (allItems.length !== 63) throw new Error(`Total items ${allItems.length} != 63`);

// Sort by g, verify g sequential 1-63 unique
allItems.sort((a, b) => a.g - b.g);
for (let i = 0; i < 63; i++) {
  if (allItems[i].g !== i + 1) throw new Error(`g sequence broken at index ${i}: got g=${allItems[i].g}`);
}

// --- lessonKey computation (F-18: <3 content-word tokens => "") ---
const STOPWORDS = new Set([
  "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with", "at", "by", "from",
  "is", "are", "be", "this", "that", "it", "its", "as", "not", "no",
]);
function computeLessonKey(rawAnswer) {
  if (!rawAnswer) return "";
  const tokens = rawAnswer
    .toLowerCase()
    .replace(/[^\w\s]/g, " ")
    .split(/\s+/)
    .filter(Boolean)
    .filter((t) => !STOPWORDS.has(t));
  const unique = [...new Set(tokens)].sort();
  if (unique.length < 3) return ""; // F-18 floor: too short to be a reliable duplicate signal
  return unique.join(" ");
}

for (const it of allItems) {
  it.lessonKey = computeLessonKey(it.factAnswerRaw || "");
}

// --- correct[] from plan ---
for (const it of allItems) {
  const p = planByG[it.g];
  if (!p) throw new Error(`g${it.g}: no plan entry`);
  if (it.format === "multi") {
    it.correct = p.correctPair.split("");
  } else {
    it.correct = [p.correctLetter];
  }
  // sanity: the option(s) marked family:null should match
  const nullOpts = (it.opts || []).filter((o) => o.family === null || o.family === undefined).map((o) => o.l);
  const mismatch = it.correct.length !== nullOpts.length || !it.correct.every((l) => nullOpts.includes(l));
  if (mismatch) {
    allNotes.push(`WARNING g${it.g}: plan says correct=${it.correct.join(",")} but family:null opts=${nullOpts.join(",")}`);
  }
}

// --- strip factAnswerRaw, _srcFile ---
allItems.forEach((it) => {
  delete it.factAnswerRaw;
  delete it._srcFile;
});

// --- cross-domain lesson-collision check ---
const byLessonKey = {};
allItems.forEach((it) => {
  if (!it.lessonKey) return;
  (byLessonKey[it.lessonKey] = byLessonKey[it.lessonKey] || []).push(it.g);
});
const collisions = Object.entries(byLessonKey).filter(([k, gs]) => gs.length > 1);

// --- family tally ---
const familyTally = {};
let totalDistractors = 0;
allItems.forEach((it) => {
  (it.opts || []).forEach((o) => {
    if (o.family) {
      familyTally[o.family] = (familyTally[o.family] || 0) + 1;
      totalDistractors++;
    }
  });
});

// --- domain/letter/shape/section-triple tallies for sanity ---
const domainTally = {};
allItems.forEach((it) => (domainTally[it.domain] = (domainTally[it.domain] || 0) + 1));
const letterTally = {};
allItems.filter((it) => it.format === "single").forEach((it) => (letterTally[it.correct[0]] = (letterTally[it.correct[0]] || 0) + 1));
const shapeTally = {};
allItems.forEach((it) => (shapeTally[it.shape] = (shapeTally[it.shape] || 0) + 1));

fs.writeFileSync("items-assembled.json", JSON.stringify(allItems, null, 1));
fs.writeFileSync("assembly-notes.json", JSON.stringify(allNotes, null, 1));

console.log("=== ASSEMBLY REPORT ===");
console.log("Total items:", allItems.length);
console.log("Domain tally:", JSON.stringify(domainTally));
console.log("Letter tally (single-answer):", JSON.stringify(letterTally));
console.log("Shape tally:", JSON.stringify(shapeTally));
console.log("Total distractors:", totalDistractors);
console.log("Family tally:", JSON.stringify(familyTally, null, 1));
console.log("\nLesson-key collisions:", collisions.length);
collisions.forEach(([k, gs]) => console.log(`  "${k}" -> g${gs.join(", g")}`));
console.log("\nCorrect/family mismatches + author notes:", allNotes.length);
allNotes.forEach((n) => console.log("  - " + n));
console.log("\nWrote items-assembled.json, assembly-notes.json");
