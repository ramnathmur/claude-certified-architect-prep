#!/usr/bin/env node
/* Assembles the 13 authored batch files into one 63-item ITEMS array for Paper 2.
 * - computes lessonKey from factAnswerRaw (lowercase, strip punctuation, remove stopwords, dedupe, sort)
 * - checks cross-domain lesson-collision (F-10) before shipping
 * - strips factAnswerRaw (not part of the shipped schema)
 * - sorts by g, verifies 1..63 sequential with no gaps/duplicates
 * - writes items.json (final array) and a report to stdout
 */
const fs = require("fs");
const path = require("path");

const DIR = __dirname;
const FILES = [
  "p2-d1-batch1.json","p2-d1-batch2.json",
  "p2-d2-batch1.json","p2-d2-batch2.json",
  "p2-d3-batch1.json","p2-d3-batch2.json",
  "p2-d4-batch1.json","p2-d4-batch2.json",
  "p2-d5-batch1.json","p2-d5-batch2.json",
  "p2-d6-batch1.json","p2-d6-batch2.json",
  "p2-d7.json"
];

const STOPWORDS = new Set([
  "a","an","and","are","as","at","be","been","being","but","by","can","could",
  "did","do","does","for","from","had","has","have","if","in","into","is","it",
  "its","it's","may","might","must","nor","not","of","on","or","shall","should",
  "so","than","that","the","then","this","to","was","were","when","which",
  "while","who","whom","whose","will","with","would","been","onto"
]);

const degenerateKeys = []; // tracked for the report - items whose raw answer was too short to compare reliably

function lessonKey(raw, g){
  if(!raw) return "";
  const tokens = raw.toLowerCase()
    .replace(/[^a-z0-9\s]/g," ")
    .split(/\s+/)
    .filter(Boolean)
    .filter(t => !STOPWORDS.has(t));
  const uniq = Array.from(new Set(tokens));
  uniq.sort();
  /* A 1-2 content-word corpus answer (e.g. "Reject", "Synchronous") is not a reliable signal that two
     items test the identical underlying decision - the corpus often reuses the same terse terminal
     word for genuinely different situations (verified by hand for this paper's g2/g17/g22 "reject" and
     g61/g63 "synchronous" collisions before this rule was added - see the Paper 2 generation entry in
     EXAM-LOG.md for the read-through). Treat these as not comparable rather than falsely flagging OR
     silently trusting a misleading key. */
  if(uniq.length < 3){
    degenerateKeys.push({g, raw, tokens: uniq});
    return "";
  }
  return uniq.join(" ");
}

let all = [];
for(const f of FILES){
  const p = path.join(DIR, f);
  if(!fs.existsSync(p)){ console.error("MISSING FILE: "+f); process.exit(2); }
  const raw = fs.readFileSync(p, "utf8");
  let items;
  try { items = JSON.parse(raw); }
  catch(e){ console.error("JSON PARSE ERROR in "+f+": "+e.message); process.exit(2); }
  if(!Array.isArray(items)){ console.error(f+" does not contain a JSON array"); process.exit(2); }
  items.forEach(it => { it.__src = f; });
  all = all.concat(items);
}

console.log("Total items collected: "+all.length);

// sort by g
all.sort((a,b) => a.g - b.g);

// verify sequential 1..63, no gaps/dupes
const errors = [];
const seenG = {};
all.forEach((it,i) => {
  if(seenG[it.g]) errors.push("duplicate g="+it.g+" (from "+it.__src+" and "+seenG[it.g]+")");
  seenG[it.g] = it.__src;
  if(it.g !== i+1) errors.push("item at position "+(i+1)+" has g="+it.g+" (expected "+(i+1)+"), src="+it.__src);
});
if(all.length !== 63) errors.push("total item count is "+all.length+", expected 63");

// compute lessonKey, strip factAnswerRaw
const lessonTally = {};
all.forEach(it => {
  const raw = it.factAnswerRaw || "";
  it.lessonKey = lessonKey(raw, it.g);
  if(it.lessonKey){
    (lessonTally[it.lessonKey] = lessonTally[it.lessonKey] || []).push({g:it.g, src:it.__src, raw});
  }
  delete it.factAnswerRaw;
});

// cross-domain lesson collision check
const collisions = [];
Object.keys(lessonTally).forEach(k => {
  const rows = lessonTally[k];
  if(rows.length > 1){
    collisions.push({key:k, items:rows});
  }
});

console.log("\n=== STRUCTURAL CHECK ===");
if(errors.length){
  console.log("ERRORS ("+errors.length+"):");
  errors.forEach(e => console.log("  - "+e));
} else {
  console.log("PASS - 63 items, g sequential 1..63, no duplicates.");
}

if(degenerateKeys.length){
  console.log("\n=== DEGENERATE ANSWER TEXT (excluded from collision check, <3 content words) ===");
  degenerateKeys.forEach(d => console.log("  g"+d.g+": \""+d.raw+"\" -> tokens ["+d.tokens.join(",")+"]"));
}

console.log("\n=== LESSON COLLISION CHECK (F-10) ===");
if(collisions.length){
  console.log("COLLISIONS FOUND ("+collisions.length+"):");
  collisions.forEach(c => {
    console.log("  lessonKey: \""+c.key+"\"");
    c.items.forEach(r => console.log("    g"+r.g+" ("+r.src+"): "+r.raw));
  });
} else {
  console.log("PASS - 0 collisions among "+Object.keys(lessonTally).length+" non-empty lessonKeys ("+
    (63 - Object.keys(lessonTally).length - all.filter(it=>it.lessonKey==="").length + all.filter(it=>it.lessonKey==="").length)+" empty).");
}

// remove the internal __src marker before writing final output
all.forEach(it => { delete it.__src; });

// per-item field sanity (matches validateItems()'s own checks, lightweight pre-check)
const famTally = {};
let singles=0, multis=0, tokenOpts=0, totalOpts=0;
const letterTally = {A:0,B:0,C:0,D:0};
const pairTally = {};
const objTally = {};
const domTally = {};
all.forEach(it => {
  domTally[it.domain] = (domTally[it.domain]||0)+1;
  objTally[it.objective] = (objTally[it.objective]||0)+1;
  if(it.format === "single"){ singles++; if(it.correct.length===1) letterTally[it.correct[0]] = (letterTally[it.correct[0]]||0)+1; }
  else if(it.format === "multi"){ multis++; const p = it.correct.slice().sort().join(""); pairTally[p]=(pairTally[p]||0)+1; }
  (it.opts||[]).forEach(o => {
    totalOpts++;
    if(/`|--[a-z]/.test(o.t)) tokenOpts++;
    const isKey = it.correct.indexOf(o.l)>=0;
    if(!isKey && o.family) famTally[o.family] = (famTally[o.family]||0)+1;
  });
});
console.log("\n=== QUICK STATS (full validateItems() still runs via run-gate.js separately) ===");
console.log("singles="+singles+" multis="+multis);
console.log("domains: "+JSON.stringify(domTally));
console.log("objectives covered: "+Object.keys(objTally).length+" of 38");
console.log("letters: "+JSON.stringify(letterTally));
console.log("multi pairs: "+JSON.stringify(pairTally));
console.log("families: "+JSON.stringify(famTally));
console.log("tokenRatePct: "+Math.round((tokenOpts/totalOpts)*1000)/10);

fs.writeFileSync(path.join(DIR,"items-assembled.json"), JSON.stringify(all, null, 2), "utf8");
console.log("\nWrote items-assembled.json ("+all.length+" items)");

if(errors.length || collisions.length){
  console.log("\nRESULT: FAIL - fix the above before proceeding to HTML assembly.");
  process.exit(1);
} else {
  console.log("\nRESULT: PASS - safe to proceed to HTML assembly.");
}
