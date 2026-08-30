#!/usr/bin/env node
/*
 * CCAR-P fidelity gate — check 1 runner.
 *
 *   node tools/run-gate.js mock-exams/CCAR-P_MockTest-1_v1.html 63
 *
 * Extracts the shipped paper's script block, runs it in a vm with a DOM stub, and calls the
 * paper's own validateItems(). Exits 0 when the paper is clean and 1 on any error, so it can
 * be used as a shell gate before a paper is recorded as generated.
 *
 * Pass the expected item count as the second argument. Omit it (or pass 0) to run the
 * item-level checks only and skip the paper-level ones — that is the right mode for the
 * TEMPLATE, which carries four demo items rather than a full paper.
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

process.exit(r.errors.length ? 1 : 0);
