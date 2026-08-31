#!/usr/bin/env node
/*
 * Family-cap fix, per F-19 (this happens every paper) and F-25 (any cap-driven relabel is
 * provisional until the grounding audit reviews it -- flagged explicitly below, not silently
 * applied). Content of whyWrong/opts[].t is UNCHANGED; only the family tag is corrected to
 * match what each option's own whyWrong text already argues.
 *
 * Fixes:
 *   g21-D (D3 3.2): HALF-MOVE -> DETECTIVE-FOR-PREVENTIVE (logs delete-calls instead of removing
 *     the unused delete privilege -- textbook definition, not a stretch)
 *   g28-C (D3 3.1): REPAIR -> DETECTIVE-FOR-PREVENTIVE (logs usage instead of pruning idle tools now)
 *   g44-A (D5 5.8): ARCHITECTED -> OVERSPEC (a confidence-model threshold substituting for the
 *     stated hard 5%-staffing constraint -- OVERSPEC's exact definition)
 * Net effect: ARCHITECTED 20->19 (ceiling), DETECTIVE-FOR-PREVENTIVE 7->9 (floor), OVERSPEC 8->9,
 * HALF-MOVE 34->33, REPAIR 21->20. Total distractors unchanged at 181.
 */
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

const FIXES = [
  { g: 21, letter: "D", from: "HALF-MOVE", to: "DETECTIVE-FOR-PREVENTIVE" },
  { g: 28, letter: "C", from: "REPAIR", to: "DETECTIVE-FOR-PREVENTIVE" },
  { g: 44, letter: "A", from: "ARCHITECTED", to: "OVERSPEC" },
];

const applied = [];
for (const fix of FIXES) {
  const it = items.find((i) => i.g === fix.g);
  if (!it) throw new Error(`g${fix.g} not found`);
  const opt = it.opts.find((o) => o.l === fix.letter);
  if (!opt) throw new Error(`g${fix.g} option ${fix.letter} not found`);
  if (opt.family !== fix.from) throw new Error(`g${fix.g}-${fix.letter}: expected family ${fix.from}, found ${opt.family}`);
  opt.family = fix.to;
  applied.push(`g${fix.g}-${fix.letter}: ${fix.from} -> ${fix.to} (FAMILY-CAP-FIX, provisional until grounding audit reviews it, per F-25)`);
}

const familyTally = {};
items.forEach((it) => (it.opts || []).forEach((o) => { if (o.family) familyTally[o.family] = (familyTally[o.family] || 0) + 1; }));

fs.writeFileSync("items-assembled.json", JSON.stringify(items, null, 1));
const notes = JSON.parse(fs.readFileSync("assembly-notes.json", "utf8"));
notes.push(...applied);
fs.writeFileSync("assembly-notes.json", JSON.stringify(notes, null, 1));

console.log("Applied fixes:", applied);
console.log("New family tally:", JSON.stringify(familyTally, null, 1));
const capViolations = [];
if (familyTally["ARCHITECTED"] > 19) capViolations.push(`ARCHITECTED ${familyTally["ARCHITECTED"]} > 19`);
if (familyTally["EVIDENCE-MISMATCH"] < 15) capViolations.push(`EVIDENCE-MISMATCH ${familyTally["EVIDENCE-MISMATCH"]} < 15`);
if (familyTally["DETECTIVE-FOR-PREVENTIVE"] < 9) capViolations.push(`DETECTIVE-FOR-PREVENTIVE ${familyTally["DETECTIVE-FOR-PREVENTIVE"]} < 9`);
Object.entries(familyTally).forEach(([f, n]) => { if (n > 47) capViolations.push(`${f} ${n} > 47 (25% cap)`); });
console.log("Remaining cap violations:", capViolations.length ? capViolations : "none");
