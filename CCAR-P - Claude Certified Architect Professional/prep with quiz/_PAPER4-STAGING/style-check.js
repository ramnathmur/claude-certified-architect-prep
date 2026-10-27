#!/usr/bin/env node
/* Independent check 8/9 sweep -- do not trust each sub-batch's self-reported word counts. */
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

function wc(s) { return s.trim().split(/\s+/).filter(Boolean).length; }

console.log("=== Check 8: style budget ===");
let stemViol = [], optViol = [], spreadViol = [];
let stemLens = [];
items.forEach((it) => {
  const sl = wc(it.stem);
  stemLens.push(sl);
  if (sl > 45) stemViol.push(`g${it.g} stem=${sl}`);
  const optLens = it.opts.map((o) => wc(o.t));
  optLens.forEach((l, i) => { if (l > 20) optViol.push(`g${it.g}-${it.opts[i].l}=${l}`); });
  const spread = Math.max(...optLens) - Math.min(...optLens);
  if (spread > 8) spreadViol.push(`g${it.g} spread=${spread} (${optLens.join(",")})`);
});
console.log("stems >45 words:", stemViol.length ? stemViol : "none");
console.log("options >20 words:", optViol.length ? optViol : "none");
console.log("within-item spread >8:", spreadViol.length ? spreadViol : "none");
stemLens.sort((a, b) => a - b);
const median = stemLens[Math.floor(stemLens.length / 2)];
const outsideBand = stemLens.filter((l) => l < 28 || l > 40).length;
console.log(`stem median: ${median} (soft band 28-40); ${outsideBand}/63 outside soft band (guidance only, not a gate failure)`);

let whyRightViol = [], whyWrongViol = [];
items.forEach((it) => {
  const wr = wc(it.whyRight);
  if (wr < 35 || wr > 50) whyRightViol.push(`g${it.g} whyRight=${wr}`);
  Object.entries(it.whyWrong).forEach(([l, t]) => {
    const n = wc(t);
    if (n < 15 || n > 30) whyWrongViol.push(`g${it.g}-${l}=${n}`);
  });
});
console.log("whyRight outside 35-50:", whyRightViol.length ? whyRightViol : "none");
console.log("whyWrong outside 15-30:", whyWrongViol.length ? whyWrongViol : "none");

console.log("\n=== Check 9: framing and token rate ===");
const codeTokenPattern = /`[^`]+`|\b[a-z]+(?:[A-Z][a-z]*)+\b|\.(json|js|md|yaml|yml|py|ts)\b|~\/\.|--[a-z-]+\b/;
let d1d5d6Tokens = [];
let totalOpts = 0, tokenOpts = 0;
items.forEach((it) => {
  it.opts.forEach((o) => {
    totalOpts++;
    if (codeTokenPattern.test(o.t)) {
      tokenOpts++;
      if (["D1", "D5", "D6"].includes(it.domain)) d1d5d6Tokens.push(`g${it.g}-${it.l} (${it.domain}): ${o.t}`);
    }
  });
});
console.log(`inline code/config tokens: ${tokenOpts}/${totalOpts} (${(100 * tokenOpts / totalOpts).toFixed(1)}%, cap 15%)`);
console.log("D1/D5/D6 tokens found (must be zero):", d1d5d6Tokens.length ? d1d5d6Tokens : "none");

// Named entities: look for capitalized multi-word phrases that aren't known real terms
const KNOWN_REAL_TERMS = /\b(Claude|Claude Code|API|MCP|RAG|SLA|GDPR|HIPAA|FedRAMP|LLM|PII|SLA|SDK|CLI|CoT|SSO)\b/g;
let suspiciousCapPhrases = new Set();
items.forEach((it) => {
  const allText = it.stem + " " + it.opts.map((o) => o.t).join(" ");
  const stripped = allText.replace(KNOWN_REAL_TERMS, "");
  const matches = stripped.match(/\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b/g) || [];
  matches.forEach((m) => suspiciousCapPhrases.add(`g${it.g}: ${m}`));
});
console.log("\nCapitalized multi-word phrases not in the known-real-terms list (check for invented names):");
console.log([...suspiciousCapPhrases].length ? [...suspiciousCapPhrases] : "none");

// Second person rate
let secondPersonStems = items.filter((it) => /\byou(r|'re|'ll)?\b/i.test(it.stem)).length;
console.log(`\nSecond-person stems: ${secondPersonStems}/63 (${(100*secondPersonStems/63).toFixed(1)}%, cap ~15%)`);
