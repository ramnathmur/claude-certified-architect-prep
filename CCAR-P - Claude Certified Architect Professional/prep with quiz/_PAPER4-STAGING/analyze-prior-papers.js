#!/usr/bin/env node
/*
 * One-off analysis script for Paper 4 central planning. Extracts ITEMS from Papers 1, 2 and 3's
 * shipped HTML (same extraction mechanism as tools/run-gate.js) and dumps ground-truth facet /
 * section / shape / direction / family / letter / objective usage to JSON. Per the Paper 4
 * generation prompt §4a, this is the ground truth for facet exclusion lists, not FACET-LEDGER.md's
 * own "used" column.
 */
const fs = require("fs");
const vm = require("vm");

function loadItems(file) {
  const src = fs.readFileSync(file, "utf8");
  const OPEN = "<" + "script>";
  const CLOSE = "</" + "script>";
  const openAt = src.lastIndexOf(OPEN);
  const closeAt = src.lastIndexOf(CLOSE);
  const js =
    src.slice(openAt + OPEN.length, closeAt) +
    "\n;globalThis.__GATE__ = {items: ITEMS};\n";
  const elStub = () => ({
    classList: { add() {}, remove() {}, toggle() {}, contains: () => false },
    style: {}, querySelectorAll: () => [], setAttribute() {}, getAttribute: () => null,
    textContent: "", innerHTML: "", disabled: false,
  });
  const ctx = {
    document: { getElementById: elStub, querySelectorAll: () => [] },
    localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
    window: { scrollTo() {} }, setInterval: () => 0, clearInterval() {},
    confirm: () => false, location: { reload() {} }, console, module: undefined,
  };
  ctx.globalThis = ctx;
  vm.createContext(ctx);
  vm.runInContext(js, ctx, { filename: file });
  return ctx.__GATE__.items;
}

const files = {
  1: "../mock-exams/CCAR-P_MockTest-1_v1.html",
  2: "../mock-exams/CCAR-P_MockTest-2_v1.html",
  3: "../mock-exams/CCAR-P_MockTest-3_v1.html",
};

const out = {};
for (const [paperN, file] of Object.entries(files)) {
  const items = loadItems(file);
  out[paperN] = items.map((it) => ({
    g: it.g, domain: it.domain, section: it.section, facet: it.facet, objective: it.objective,
    shape: it.shape, direction: it.direction, format: it.format, selectN: it.selectN,
    correct: it.correct, families: (it.opts || []).map((o) => o.family).filter(Boolean),
  }));
}

fs.writeFileSync("prior-papers-analysis.json", JSON.stringify(out, null, 1));

// Summaries
for (const paperN of Object.keys(out)) {
  const items = out[paperN];
  console.log(`\n=== Paper ${paperN}: ${items.length} items ===`);
  const facets = new Set(items.map((i) => i.facet).filter(Boolean));
  const sections = new Set(items.map((i) => i.section));
  console.log(`distinct facets used: ${facets.size}`);
  console.log(`distinct sections used: ${sections.size}`);
  const domainCounts = {};
  items.forEach((i) => (domainCounts[i.domain] = (domainCounts[i.domain] || 0) + 1));
  console.log("domain counts:", JSON.stringify(domainCounts));
  const letterCounts = {};
  items.forEach((i) => {
    if (i.format === "single" || !i.selectN || i.selectN === 1) {
      (i.correct || []).forEach((l) => (letterCounts[l] = (letterCounts[l] || 0) + 1));
    }
  });
  console.log("single-answer letter counts:", JSON.stringify(letterCounts));
  const shapeCounts = {};
  items.forEach((i) => (shapeCounts[i.shape] = (shapeCounts[i.shape] || 0) + 1));
  console.log("shape counts:", JSON.stringify(shapeCounts));
  const familyCounts = {};
  items.forEach((i) => i.families.forEach((f) => (familyCounts[f] = (familyCounts[f] || 0) + 1)));
  console.log("family counts:", JSON.stringify(familyCounts));
  const objCounts = {};
  items.forEach((i) => (objCounts[i.objective] = (objCounts[i.objective] || 0) + 1));
  console.log("distinct objectives used:", Object.keys(objCounts).length);
}
console.log("\nWrote prior-papers-analysis.json");
