#!/usr/bin/env node
/*
 * Appends Paper 4's 63 shape-instance rows to ARCHETYPE-LEDGER.md Part 1, and adds Paper 4's row
 * to the family instance table in Part 2. Fix vs Papers 1-3's scripts: those hardcoded "normal"
 * for every row's direction column -- this one uses each item's real `direction` field, since
 * Paper 4 is the first to actually ship inverted rows and future papers' 2-use ban tracking
 * needs the real direction to mean anything.
 */
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

let ledger = fs.readFileSync("../ARCHETYPE-LEDGER.md", "utf8");

const shapeRowRe = /^\| S\d \|.*\| shipped \|.*\|$/gm;
let lastMatch = null;
let m;
while ((m = shapeRowRe.exec(ledger)) !== null) lastMatch = m;
if (!lastMatch) throw new Error("no existing shape-instance rows found");
const insertAt = lastMatch.index + lastMatch[0].length;

let newRows = "\n";
items.forEach((it) => {
  newRows += `| ${it.shape} | ${it.section} | ${it.facet} | ${it.direction} | 4 | shipped | |\n`;
});
ledger = ledger.slice(0, insertAt) + newRows.replace(/\n$/, "") + ledger.slice(insertAt);

const familyTally = { "HALF-MOVE": 0, "WRONG-AXIS": 0, REPAIR: 0, DISCARD: 0, ARCHITECTED: 0, OVERSPEC: 0, "EVIDENCE-MISMATCH": 0, "DETECTIVE-FOR-PREVENTIVE": 0 };
items.forEach((it) => it.opts.forEach((o) => { if (o.family) familyTally[o.family]++; }));

const familyRowRe = /^\| 3 \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \|$/m;
const fm = ledger.match(familyRowRe);
if (!fm) throw new Error("Paper 3 family row not found");
const newFamilyRow = `| 4 | ${familyTally["HALF-MOVE"]} | ${familyTally["WRONG-AXIS"]} | ${familyTally.REPAIR} | ${familyTally.DISCARD} | ${familyTally.ARCHITECTED} | ${familyTally.OVERSPEC} | ${familyTally["EVIDENCE-MISMATCH"]} | ${familyTally["DETECTIVE-FOR-PREVENTIVE"]} |`;
ledger = ledger.replace(familyRowRe, fm[0] + "\n" + newFamilyRow);

ledger = ledger.replace(
  "**Instances:** Paper 1 populated both instance tables 2026-08-30 (63 shape rows, 8-family tally); Paper 2 appended 2026-08-31 (63 more shape rows, 8-family tally); Paper 3 appended 2026-08-31 (63 more shape rows, 8-family tally). Rebuilt from the shipped HTML files, not from a session's own account.",
  "**Instances:** Paper 1 populated both instance tables 2026-08-30 (63 shape rows, 8-family tally); Paper 2 appended 2026-08-31 (63 more shape rows, 8-family tally); Paper 3 appended 2026-08-31 (63 more shape rows, 8-family tally); Paper 4 appended 2026-08-31 (63 more shape rows, 8-family tally, first paper with real per-row direction values). Rebuilt from the shipped HTML files, not from a session's own account."
);

fs.writeFileSync("../ARCHETYPE-LEDGER.md", ledger);
console.log("Appended 63 shape-instance rows and Paper 4's family tally row.");
console.log("family tally:", JSON.stringify(familyTally));
