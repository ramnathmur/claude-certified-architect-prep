#!/usr/bin/env node
/*
 * Paper 5 central-planning analysis. Extracts ITEMS from Papers 1-4's shipped HTML (same
 * extraction mechanism as tools/run-gate.js and _PAPER4-STAGING/analyze-prior-papers.js) and
 * dumps ground-truth facet/section/shape/direction/family/letter/objective usage to JSON.
 * Per the Paper 5 generation prompt §1.7/§2, this is the ground truth for facet-level (section,
 * facet, direction) bookkeeping, not FACET-LEDGER.md's own "used" column or ARCHETYPE-LEDGER.md's
 * own instance table (both are cross-checked against this, not trusted ahead of it).
 */
const fs = require("fs");
const vm = require("vm");
const path = require("path");

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
  4: "../mock-exams/CCAR-P_MockTest-4_v1.html",
};

const scriptDir = __dirname;
const out = {};
for (const [paperN, rel] of Object.entries(files)) {
  const file = path.join(scriptDir, rel);
  const items = loadItems(file);
  out[paperN] = items.map((it) => ({
    g: it.g, domain: it.domain, section: it.section, facet: it.facet, objective: it.objective,
    shape: it.shape, direction: it.direction || "normal", format: it.format, selectN: it.selectN,
    correct: it.correct, families: (it.opts || []).map((o) => o.family).filter(Boolean),
  }));
}

fs.writeFileSync(path.join(scriptDir, "prior-papers-analysis.json"), JSON.stringify(out, null, 1));

// ---- D2-specific (section, facet, direction) bookkeeping, per the Paper 5 prompt's §2 ----
const d2Rows = [];
for (const paperN of Object.keys(out)) {
  out[paperN].forEach((it) => {
    if (it.domain === "D2") d2Rows.push({ paper: Number(paperN), ...it });
  });
}

const bySection = {};
d2Rows.forEach((r) => {
  if (!bySection[r.section]) bySection[r.section] = {};
  const facetKey = r.facet || "(misconception-unit)";
  if (!bySection[r.section][facetKey]) bySection[r.section][facetKey] = { normal: [], inverted: [] };
  const dir = r.direction === "inverted" ? "inverted" : "normal";
  bySection[r.section][facetKey][dir].push({ paper: r.paper, g: r.g, shape: r.shape });
});

fs.writeFileSync(path.join(scriptDir, "d2-facet-direction.json"), JSON.stringify(bySection, null, 1));

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
  const shapeCounts = {};
  items.forEach((i) => (shapeCounts[i.shape] = (shapeCounts[i.shape] || 0) + 1));
  console.log("shape counts:", JSON.stringify(shapeCounts));
  const dirCounts = {};
  items.forEach((i) => (dirCounts[i.direction] = (dirCounts[i.direction] || 0) + 1));
  console.log("direction counts:", JSON.stringify(dirCounts));
}

console.log("\n=== D2 (section, facet) -> direction usage, all 4 papers ===");
Object.keys(bySection).sort((a, b) => a.localeCompare(b, undefined, { numeric: true })).forEach((sec) => {
  console.log(`\n  ${sec}:`);
  Object.entries(bySection[sec]).forEach(([facet, dirs]) => {
    const n = dirs.normal.map((x) => `P${x.paper}/g${x.g}`).join(",") || "-";
    const i = dirs.inverted.map((x) => `P${x.paper}/g${x.g}`).join(",") || "-";
    console.log(`    ${facet}: normal=[${n}] inverted=[${i}]`);
  });
});

console.log("\nWrote prior-papers-analysis.json and d2-facet-direction.json");
