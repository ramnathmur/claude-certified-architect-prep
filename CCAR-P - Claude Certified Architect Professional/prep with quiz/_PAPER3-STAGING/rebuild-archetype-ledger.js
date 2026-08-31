#!/usr/bin/env node
/* Appends Paper 3's 63 shape-instance rows to ARCHETYPE-LEDGER.md Part 1, and adds Paper 3's row
   to the family instance table in Part 2. Both are append operations to existing tables. */
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

let ledger = fs.readFileSync("../ARCHETYPE-LEDGER.md", "utf8");

// --- Part 1: shape instance rows ---
// Find the last row of the existing shape-instance table (a line starting with "| S" followed by
// section/facet/direction/paper/outcome/notes) and insert after it.
const shapeRowRe = /^\| S\d \|.*\| shipped \|.*\|$/gm;
let lastMatch = null;
let m;
while ((m = shapeRowRe.exec(ledger)) !== null) lastMatch = m;
if (!lastMatch) throw new Error("no existing shape-instance rows found");
const insertAt = lastMatch.index + lastMatch[0].length;

let newRows = "\n";
items.forEach((it) => {
  // facet field may be compound (F-x+F-y) or a misconception unit (M-x.y) -- record as-is, this
  // ledger's own convention (see Paper 1/2 rows) is one row per (shape, section, facet, direction).
  newRows += `| ${it.shape} | ${it.section} | ${it.facet} | normal | 3 | shipped | |\n`;
});
ledger = ledger.slice(0, insertAt) + newRows.replace(/\n$/, "") + ledger.slice(insertAt);

// --- Part 2: family instance table ---
const familyTally = { "HALF-MOVE": 0, "WRONG-AXIS": 0, REPAIR: 0, DISCARD: 0, ARCHITECTED: 0, OVERSPEC: 0, "EVIDENCE-MISMATCH": 0, "DETECTIVE-FOR-PREVENTIVE": 0 };
items.forEach((it) => it.opts.forEach((o) => { if (o.family) familyTally[o.family]++; }));

const familyRowRe = /^\| 2 \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \|$/m;
const fm = ledger.match(familyRowRe);
if (!fm) throw new Error("Paper 2 family row not found");
const newFamilyRow = `| 3 | ${familyTally["HALF-MOVE"]} | ${familyTally["WRONG-AXIS"]} | ${familyTally.REPAIR} | ${familyTally.DISCARD} | ${familyTally.ARCHITECTED} | ${familyTally.OVERSPEC} | ${familyTally["EVIDENCE-MISMATCH"]} | ${familyTally["DETECTIVE-FOR-PREVENTIVE"]} |`;
ledger = ledger.replace(familyRowRe, fm[0] + "\n" + newFamilyRow);

// --- header line: update Instances note ---
ledger = ledger.replace(
  "**Instances:** Paper 1 populated both instance tables 2026-08-30 (63 shape rows, 8-family tally); Paper 2 appended 2026-08-31 (63 more shape rows, 8-family tally). Rebuilt from the shipped HTML files, not from a session's own account.",
  "**Instances:** Paper 1 populated both instance tables 2026-08-30 (63 shape rows, 8-family tally); Paper 2 appended 2026-08-31 (63 more shape rows, 8-family tally); Paper 3 appended 2026-08-31 (63 more shape rows, 8-family tally). Rebuilt from the shipped HTML files, not from a session's own account."
);

fs.writeFileSync("../ARCHETYPE-LEDGER.md", ledger);
console.log("Appended 63 shape-instance rows and Paper 3's family tally row.");
console.log("family tally:", JSON.stringify(familyTally));
