#!/usr/bin/env node
/* Appends Paper 4's 63 stems to STEM-LEDGER.md, matching the Paper 1-3 append format exactly. */
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));

const STOPWORDS = new Set(["the","a","an","and","or","of","to","in","on","for","with","at","by","from","is","are","be","this","that","it","its","as","not","no"]);
function sig(stem) {
  const tokens = stem.toLowerCase().replace(/[^\w\s]/g, " ").split(/\s+/).filter(Boolean).filter((t) => !STOPWORDS.has(t));
  return [...new Set(tokens)].sort().join(" ");
}
function excerpt(stem) {
  const words = stem.split(/\s+/);
  const short = words.slice(0, 9).join(" ");
  return (short.length < stem.length ? short + "…" : short);
}

let table = "\n### Paper 4 — appended 2026-08-31\n\n";
table += "| id | src | domain | words | excerpt | token signature |\n";
table += "|---|---|---|---|---|---|\n";
items.forEach((it) => {
  const id = `P4-${String(it.g).padStart(2, "0")}`;
  const words = it.stem.split(/\s+/).length;
  table += `| \`${id}\` | Paper 4 | ${it.domain} | ${words} | ${excerpt(it.stem)} | \`${sig(it.stem)}\` |\n`;
});

const ledger = fs.readFileSync("../STEM-LEDGER.md", "utf8");
const marker = "## Append rule";
const idx = ledger.indexOf(marker);
if (idx < 0) throw new Error("marker not found");
const out = ledger.slice(0, idx) + table.trimStart() + "\n\n" + ledger.slice(idx);
fs.writeFileSync("../STEM-LEDGER.md", out);
console.log("Appended 63 Paper 4 rows to STEM-LEDGER.md");
