#!/usr/bin/env node
/*
 * CCAR-P fidelity gate — check 1 runner, plus (from Paper 4) checks 10 and 11, mechanized per
 * the orchestration prompt's closing note in Phase 6: "Build the script at Paper 4, when check
 * 11 is running Jaccard against a ledger of 237 stems and hand-checking stops being reliable."
 * Checks 10 (distractor-family caps) and 11 (stem-Jaccard vs STEM-LEDGER.md, plus (shape,
 * section, facet) triple reuse vs ARCHETYPE-LEDGER.md) were proven correct as one-off scripts
 * across Papers 2-4 (each paper's own _PAPERn-STAGING/extra-checks.js) — this folds that same
 * logic into the committed gate so a future paper doesn't need to recreate it. Checks 2-9, 12-13
 * are unchanged one-off/manual checks; folding them in is future work, not done here.
 *
 *   node tools/run-gate.js mock-exams/CCAR-P_MockTest-1_v1.html 63
 *
 * Extracts the shipped paper's script block, runs it in a vm with a DOM stub, and calls the
 * paper's own validateItems(). Exits 0 when the paper is clean and 1 on any error, so it can
 * be used as a shell gate before a paper is recorded as generated.
 *
 * Pass the expected item count as the second argument. Omit it (or pass 0) to run the
 * item-level checks only and skip the paper-level ones — that is the right mode for the
 * TEMPLATE, which carries four demo items rather than a full paper. Checks 10/11 below also
 * skip automatically when expectCount is not passed, since they need a full paper's ITEMS.
 *
 * Why this is a committed file rather than an inline `node -e`: the template documents this
 * command inside its own script block, and a literal opening script tag written there splits
 * the file at the wrong offset and silently truncates the extracted source. That bug was
 * shipped once, in the first version of this template, and caught by running it.
 */

const fs = require("fs");
const vm = require("vm");
const path = require("path");

const file = process.argv[2];
const expectCount = Number(process.argv[3] || 0) || null;

if (!file) {
  console.error("usage: node tools/run-gate.js <paper.html> [expectedItemCount]");
  process.exit(2);
}
if (!fs.existsSync(file)) {
  console.error("no such file: " + path.resolve(file));
  process.exit(2);
}

const OPEN = "<" + "script>";
const CLOSE = "</" + "script>";

const src = fs.readFileSync(file, "utf8");

/* Take the LAST script block and the LAST closing tag, so a documentation comment mentioning
   either tag cannot move the boundary. */
const openAt = src.lastIndexOf(OPEN);
const closeAt = src.lastIndexOf(CLOSE);
if (openAt < 0 || closeAt < 0 || closeAt < openAt) {
  console.error("could not locate a script block in " + file);
  process.exit(2);
}
/* Top-level `const` and `let` in a vm script are script-scoped and never become properties of
   the context object — only `var` and function declarations do. ITEMS is a const, so it has to
   be handed out explicitly by an appended epilogue. */
const js =
  src.slice(openAt + OPEN.length, closeAt) +
  "\n;globalThis.__GATE__ = {items: ITEMS, validate: validateItems};\n";

const elStub = () => ({
  classList: { add() {}, remove() {}, toggle() {}, contains: () => false },
  style: {},
  querySelectorAll: () => [],
  setAttribute() {},
  getAttribute: () => null,
  textContent: "",
  innerHTML: "",
  disabled: false,
});

const ctx = {
  document: { getElementById: elStub, querySelectorAll: () => [] },
  localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
  window: { scrollTo() {} },
  setInterval: () => 0,
  clearInterval() {},
  confirm: () => false,
  location: { reload() {} },
  console,
  module: undefined,
};
ctx.globalThis = ctx;

vm.createContext(ctx);
try {
  vm.runInContext(js, ctx, { filename: file });
} catch (e) {
  console.error("script block failed to evaluate: " + e.message);
  process.exit(2);
}

const gate = ctx.__GATE__;
if (!gate || typeof gate.validate !== "function" || !Array.isArray(gate.items)) {
  console.error("file does not expose validateItems() and ITEMS");
  process.exit(2);
}

const r = gate.validate(gate.items, { expectCount });

const label = expectCount
  ? `full paper checks, expecting ${expectCount} items`
  : "item-level checks only (paper-level checks skipped — pass an item count to enable them)";

console.log(`\nCCAR-P fidelity gate · check 1 · ${path.basename(file)}`);
console.log(label);
console.log("");
console.log(`ERRORS   ${r.errors.length}`);
r.errors.forEach((e) => console.log("  - " + e));
console.log(`WARNINGS ${r.warnings.length}`);
r.warnings.forEach((w) => console.log("  - " + w));
console.log("");
console.log("STATS");
console.log(JSON.stringify(r.stats, null, 1));
console.log("");
console.log(r.errors.length ? "RESULT: FAIL — paper may not ship." : "RESULT: PASS — check 1 clear.");

// --- Checks 10/11, mechanized from Paper 4 onward. Only meaningful for a full paper. ---
let extraErrors = [];
if (expectCount) {
  const STOPWORDS = new Set([
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with", "at", "by", "from",
    "is", "are", "be", "this", "that", "it", "its", "as", "not", "no",
  ]);
  const sig = (s) =>
    new Set(s.toLowerCase().replace(/[^\w\s]/g, " ").split(/\s+/).filter(Boolean).filter((t) => !STOPWORDS.has(t)));
  const jaccard = (a, b) => {
    const inter = [...a].filter((x) => b.has(x)).length;
    const union = new Set([...a, ...b]).size;
    return union ? inter / union : 0;
  };

  console.log("\n--- Check 10: distractor-family caps ---");
  const familyTally = {};
  let totalDistractors = 0;
  gate.items.forEach((it) => (it.opts || []).forEach((o) => {
    if (o.family) { familyTally[o.family] = (familyTally[o.family] || 0) + 1; totalDistractors++; }
  }));
  console.log("family tally:", JSON.stringify(familyTally), `(${totalDistractors} distractors)`);
  // Fixed thresholds per the orchestration prompt Phase 5.2/ARCHETYPE-LEDGER.md, calibrated
  // against a 189-distractor (63-item, 3-distractor) baseline -- NOT recomputed against the
  // actual total, which varies slightly (181 this paper, same as Papers 2-3) since multi-
  // response items carry only 2 distractors each. Using a live percentage here was a bug caught
  // while building this: ceil(181*0.05)=10 would fail a paper sitting exactly at the real 9 floor.
  if (Object.values(familyTally).some((n) => n > 47)) extraErrors.push(`a family exceeds the 47 cap (25% of 189): ${JSON.stringify(familyTally)}`);
  if ((familyTally["EVIDENCE-MISMATCH"] || 0) < 15) extraErrors.push(`EVIDENCE-MISMATCH ${familyTally["EVIDENCE-MISMATCH"] || 0} below floor 15`);
  if ((familyTally["DETECTIVE-FOR-PREVENTIVE"] || 0) < 9) extraErrors.push(`DETECTIVE-FOR-PREVENTIVE ${familyTally["DETECTIVE-FOR-PREVENTIVE"] || 0} below floor 9`);
  if ((familyTally["ARCHITECTED"] || 0) > 19) extraErrors.push(`ARCHITECTED ${familyTally["ARCHITECTED"] || 0} above ceiling 19`);
  console.log(extraErrors.length ? "family-cap issues found (see below)" : "family caps: PASS");

  console.log("\n--- Check 11: stem-Jaccard vs STEM-LEDGER.md (threshold 0.30) + within-paper ---");
  const ledgerPath = path.join(__dirname, "..", "STEM-LEDGER.md");
  // If this paper's own rows are already appended to the ledger (Phase 8 runs the ledger rebuild
  // AFTER gate verification, but the gate should stay safe to re-run any time after that too),
  // exclude them -- otherwise every item scores a guaranteed 1.000 against its own ledger row.
  const paperNumMatch = path.basename(file).match(/MockTest-(\d+)_/);
  const selfPrefix = paperNumMatch ? `P${paperNumMatch[1]}-` : null;
  if (fs.existsSync(ledgerPath)) {
    const ledgerRaw = fs.readFileSync(ledgerPath, "utf8");
    const ledgerSigs = [];
    for (const line of ledgerRaw.split("\n")) {
      const m = line.match(/^\|\s*`([\w-]+)`\s*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*`([^`]*)`\s*\|/);
      if (m && !(selfPrefix && m[1].startsWith(selfPrefix))) ledgerSigs.push({ id: m[1], sig: new Set(m[2].split(/\s+/).filter(Boolean)) });
    }
    const flagged = [];
    gate.items.forEach((it) => {
      const s = sig(it.stem);
      ledgerSigs.forEach((row) => {
        const score = jaccard(s, row.sig);
        if (score >= 0.3) flagged.push(`g${it.g} vs ${row.id}: ${score.toFixed(3)}`);
      });
    });
    for (let i = 0; i < gate.items.length; i++) {
      for (let j = i + 1; j < gate.items.length; j++) {
        const score = jaccard(sig(gate.items[i].stem), sig(gate.items[j].stem));
        if (score >= 0.3) flagged.push(`g${gate.items[i].g} vs g${gate.items[j].g} (within-paper): ${score.toFixed(3)}`);
      }
    }
    if (flagged.length) extraErrors.push(...flagged.map((f) => `stem-Jaccard >= 0.30: ${f}`));
    console.log(flagged.length ? `${flagged.length} pair(s) >= 0.30 (see below)` : "stem-Jaccard: PASS, 0 pairs >= 0.30");
  } else {
    console.log("STEM-LEDGER.md not found at " + ledgerPath + " — skipped");
  }

  console.log("\n--- Check 11 (triples): (shape, section, facet) reuse > 2 vs ARCHETYPE-LEDGER.md ---");
  const archetypePath = path.join(__dirname, "..", "ARCHETYPE-LEDGER.md");
  if (fs.existsSync(archetypePath)) {
    const archRaw = fs.readFileSync(archetypePath, "utf8");
    const tripleCount = {};
    // Same self-row exclusion as the stem-Jaccard check above: skip rows already tagged with this
    // paper's own number, so the check stays safe to re-run after the ledger rebuild too.
    const selfPaperNum = paperNumMatch ? paperNumMatch[1] : null;
    for (const line of archRaw.split("\n")) {
      const m = line.match(/^\|\s*(S\d)\s*\|\s*([\d.]+)\s*\|\s*([FM]-[\d.]+(?:-\d+)?(?:\+[FM]-[\d.]+-\d+)?)\s*\|\s*(normal|inverted)\s*\|\s*(\d+)\s*\|/);
      if (m && !(selfPaperNum && m[5] === selfPaperNum)) {
        const key = `${m[1]}|${m[2]}|${m[3]}`;
        tripleCount[key] = (tripleCount[key] || 0) + 1;
      }
    }
    gate.items.forEach((it) => {
      const key = `${it.shape}|${it.section}|${it.facet}`;
      tripleCount[key] = (tripleCount[key] || 0) + 1;
    });
    const overTriple = Object.entries(tripleCount).filter(([, v]) => v > 2);
    if (overTriple.length) extraErrors.push(`(shape,section,facet) triples used >2 times: ${JSON.stringify(overTriple)}`);
    console.log(overTriple.length ? "triple reuse issues found (see below)" : "triple reuse: PASS");
  } else {
    console.log("ARCHETYPE-LEDGER.md not found at " + archetypePath + " — skipped");
  }

  if (extraErrors.length) {
    console.log("\nEXTRA-CHECK ERRORS (10/11):", extraErrors.length);
    extraErrors.forEach((e) => console.log("  - " + e));
  }
}

const finalFail = r.errors.length > 0 || extraErrors.length > 0;
console.log("\n" + (finalFail ? "OVERALL RESULT: FAIL" : "OVERALL RESULT: PASS (checks 1, 10, 11 clear)"));

process.exit(finalFail ? 1 : 0);
