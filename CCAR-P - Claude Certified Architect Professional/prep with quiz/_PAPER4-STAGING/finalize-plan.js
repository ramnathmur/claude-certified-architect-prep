#!/usr/bin/env node
/*
 * Finalizes the Paper 4 central plan. New this paper (§5a of the generation prompt):
 * DIRECTION_OVERRIDES marks 17 items "inverted" (>=2 per shape, all 8 shapes covered), each
 * with an explicit `invGuidance` string quoting ARCHETYPE-LEDGER.md's per-shape inversion
 * definition -- handed verbatim to the authoring sub-batch so inversion is never left to
 * inference from the shape name alone (per the generation prompt's explicit instruction).
 * D2's 5 reuse-inverted items (direction already set in build-plan.js) get the same treatment.
 * Also: g-numbering, multi-response selection (avoiding overlap with inverted-direction
 * items so no single item carries both a format novelty and a direction novelty), correct-
 * letter pre-plan ({A13,B14,C14,D14} -- Paper 4's short letter is A), correct-pair assignment.
 */
const fs = require("fs");
const { items: rawItems } = require("./plan-raw.json");

const DOMAIN_ORDER = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"];

// Multi-response sources, chosen to NOT overlap any DIRECTION_OVERRIDES target below.
const MULTI_SECTIONS = { D1: ["1.5", "1.6"], D2: [], D3: ["3.3"], D4: ["4.9"], D5: ["5.6"], D6: ["6.12"], D7: ["7.2", "7.8"] };
const MULTI_COUNT = { D1: 2, D2: 0, D3: 1, D4: 1, D5: 1, D6: 1, D7: 2 };

const SHAPE_HINTS = {
  "1.3": "S5", "1.4": "S5", "1.1": "S6", "1.2": "S6", "1.9": "S1", "1.10": "S4", "1.11": "S5",
  "1.12": "S2", "1.5": "S5", "1.6": "S1", "1.7": "S1", "1.8": "S4",
  "2.1": "S5", "2.2": "S2", "2.3": "S1", "2.4": "S4", "2.5": "S6", "2.6": "S2", "2.7": "S2",
  "2.8": "S2", "2.9": "S8",
  "3.1": "S4", "3.2": "S1", "3.3": "S2", "3.4": "S5", "3.5": "S1", "3.6": "S1", "3.7": "S6",
  "3.8": "S4", "3.9": "S1", "3.10": "S3", "3.11": "S4", "3.12": "S1", "3.13": "S4", "3.14": "S1",
  "4.1": "S6", "4.2": "S3", "4.3": "S6", "4.4": "S6", "4.5": "S6", "4.6": "S1", "4.7": "S1",
  "4.8": "S6", "4.9": "S3", "4.10": "S4", "4.11": "S1", "4.12": "S1",
  "5.1": "S1", "5.2": "S8", "5.3": "S8", "5.4": "S8", "5.5": "S2", "5.6": "S3", "5.7": "S1",
  "5.8": "S2", "5.9": "S1", "5.10": "S6", "5.11": "S1",
  "6.1": "S7", "6.2": "S7", "6.3": "S7", "6.4": "S7", "6.6": "S7", "6.7": "S3", "6.8": "S7",
  "6.9": "S7", "6.10": "S6", "6.11": "S1", "6.12": "S7",
  "7.1": "S3", "7.2": "S3", "7.3": "S5", "7.5": "S4", "7.8": "S2",
};

// Per-shape inversion definitions, quoted verbatim from ARCHETYPE-LEDGER.md Part 1's inversion
// table, so every sub-batch prompt states the exact test rather than leaving it to inference.
const INVERSION_DEF = {
  S1: "The principle is already correctly applied and a further restriction would break a stated requirement.",
  S2: "No single change satisfies both constraints; the answer is the one that satisfies the binding constraint and states the trade.",
  S3: "The recent change is a coincidence; the pinned variables point elsewhere.",
  S4: "The obvious mechanism is correct and the sophisticated alternative is the trap.",
  S5: "Under-engineering -- a stated requirement is genuinely non-enumerable and the higher rung is correct.",
  S6: "The measurement exists, is correctly defined, and is being read wrongly.",
  S7: "The stakeholder's stated mechanism IS the requirement and the architect's preferred redesign is out of scope.",
  S8: "The control is too high and is blocking a legitimate stated need.",
};

// Shape rebalance: the raw SHAPE_HINTS draw put S1 at 15 (hard ceiling 11) and S8 at 3 (hard
// floor 4) -- ARCHETYPE-LEDGER.md's per-paper shape budget. All four sections below fit their
// reassigned shape at least as naturally as S1 (3.2 and 5.1 are both control-placement/altitude
// decisions -- textbook S8; 4.6 is a measurement/grading decision -- textbook S6). None of these
// four are DIRECTION_OVERRIDES targets, so this only touches normal-direction items.
const SHAPE_REBALANCE = {
  "D3|3.2": "S8", "D5|5.1": "S8", "D4|4.6": "S6",
};
let rebalanceRemaining = { "D5|5.1": 2 }; // both 5.1 instances move to S8

// 17 items marked direction:inverted, keyed by (domain, section), matched to the FIRST plan-raw
// item found at that domain+section (sections drawn twice supply two candidates; either is fine).
// D2's 5 already carry direction:"inverted" from build-plan.js -- these entries only set their
// shape (overriding SHAPE_HINTS where the inversion needs a different shape than the section's
// normal-direction hint) and attach note text for the slots doc.
const DIRECTION_OVERRIDES = [
  // D2 (already direction:inverted from build-plan.js)
  { domain: "D2", section: "2.1", shape: "S5", note: "Normal-direction facet F-2.1-01 tests avoiding an oversized model for a bounded, high-volume task. Invert: state an explicit regulatory/compliance requirement (a named audit or certification mandate) that cannot be captured by an accuracy-bar test alone -- the higher-capability model is correct despite volume pressure toward the cheaper one. Must NOT reproduce F-2.1-02's already-shipped 'ambiguous multi-step synthesis' framing." },
  { domain: "D2", section: "2.2", shape: "S8", note: "Section 2.2's core rule (system prompt is the only durable-authority location) is absolute -- Paper 2's g14/g15 already found no conditional row supports a clean T1 inversion here. Attempt the best defensible S8-inverted framing (an existing system-prompt guardrail is over-broad and blocks a legitimate case) but if no clause deletion/inversion produces a genuinely different correct option, flag this item as a T1 IRREDUCIBLE candidate in t1Clause/t1Alt rather than forcing one -- document honestly, matching Paper 2's precedent." },
  { domain: "D2", section: "2.4", shape: "S1", note: "Normal-direction facet F-2.4-01 tests adding a reasoning cue for multi-step tasks. Invert: a chain-of-thought cue is already correctly present for a genuinely multi-step task; the trap option removes it 'to save tokens/cost', which would break the accuracy requirement the cue exists to satisfy. Correct answer: keep the cue." },
  { domain: "D2", section: "2.7", shape: "S1", note: "Normal-direction facet F-2.7-01 tests hybrid extraction for precision-critical facts. Invert: the conversation has NO precision-critical facts (pure open-ended discussion) and a stated cost/latency ceiling exists; applying the hybrid-extraction approach anyway is over-engineered overhead that would blow the ceiling for no benefit -- plain summarization is correct and sufficient. Punishes the 'sounds more careful' reflex directly." },
  { domain: "D2", section: "2.8", shape: "S2", note: "Normal-direction facet F-2.8-01 tests static-first ordering for caching. Invert: a stated hard requirement (a compliance disclaimer/audit stamp) must appear in every request and looks like it has to go first, seemingly breaking the cacheable prefix. Naive options either drop the stamp (breaks the requirement) or reorder in a way that kills caching for no reason. Correct answer states the trade: the stamp can go AFTER the stable cached prefix without weakening its effect, satisfying both constraints." },
  // Non-D2 (12 items, spread across D1/D3/D4/D5/D6)
  { domain: "D1", section: "1.1", shape: "S6", note: "Invert: the outcome metric is already correctly defined in advance; the trap is a superficially-similar proxy metric being treated as equivalent when it doesn't actually measure the stated business decision." },
  { domain: "D1", section: "1.2", shape: "S6", note: "Invert: the baseline/value-unit measurement is already correctly and stably defined; apparent 'drift' is the metric's own definition having silently changed upstream, not real performance change." },
  { domain: "D1", section: "1.10", shape: "S4", note: "Invert: the obvious mechanism (a straightforward schema/contract check at the input or output boundary) is already correct; a sophisticated addition (an extra LLM-based validation pass) is the unneeded, costlier trap." },
  { domain: "D1", section: "1.11", shape: "S5", note: "Invert: the stated subtask is genuinely non-enumerable (open-ended synthesis/judgment, not a checklist), so a coarser single-call approach is wrong and finer, named-step decomposition is actually required -- the higher rung, not the lower one." },
  { domain: "D3", section: "3.1", shape: "S4", note: "Invert: the obvious mechanism (a narrowly-scoped tool surface matched to the task) is already correct; granting a broader tool surface 'for flexibility' is the sophisticated-sounding trap that reintroduces capability bloat." },
  { domain: "D3", section: "3.4", shape: "S2", note: "Invert: a hard regulatory latency SLA is stated and cannot be relaxed. No single change satisfies both a stricter accuracy target and the SLA at once -- the correct answer accepts an explicit accuracy trade to hold the binding latency constraint, rather than chasing an option that claims to fix both." },
  { domain: "D3", section: "3.10", shape: "S3", note: "Invert: after an index refresh, degraded retrieval quality persists, but the refresh is a coincidence -- the pinned variables (chunking, embedding model) point elsewhere, e.g. an embedding-model version drift that happened in the same window. The reflex answer (re-check the refresh pipeline) is the trap." },
  { domain: "D4", section: "4.10", shape: "S3", note: "Invert: accuracy drops at the same time as a prompt-template edit, but investigation shows the drop actually correlates with a simultaneous, easily-missed upstream data-schema change -- the recent prompt edit is a coincidence, not the cause." },
  { domain: "D4", section: "4.11", shape: "S1", note: "Invert: caching is already correctly enabled via static-first ordering. The trap over-applies caching to content that is actually per-user/highly dynamic, which would serve stale or cross-user data -- a further 'more aggressive caching' restriction breaks a stated correctness/freshness requirement." },
  { domain: "D5", section: "5.3", shape: "S8", note: "Invert: a compliance-mandated boundary control (e.g. data-residency enforcement) is already correctly placed at the infrastructure/network layer and is now blocking a legitimate new use case (a partner integration needing controlled cross-region access). Correct answer: a scoped, explicit exception process at the same layer -- not moving the control down to the application layer to work around it." },
  { domain: "D6", section: "6.2", shape: "S7", note: "Invert: the stakeholder's stated mechanism (e.g. a specific named review workflow) is itself the actual compliance-driven requirement, not just their guess at implementation -- the architect's preferred, more elegant automated redesign is out of scope even though it looks better engineered." },
  { domain: "D6", section: "6.9", shape: "S7", note: "Invert: the requested SLA framing is the binding commitment already stated in a signed agreement -- re-negotiating a 'more technically honest' probabilistic framing is out of scope for this engagement, however defensible it would be in the abstract." },
];

// --- 1. Order items by domain ---
const byDomain = {};
DOMAIN_ORDER.forEach((d) => (byDomain[d] = rawItems.filter((i) => i.domain === d)));

// Apply direction overrides: for each override, find the first not-yet-claimed item at that
// domain+section and tag it.
const claimed = new Set();
const overrideByItem = new Map();
for (const ov of DIRECTION_OVERRIDES) {
  const pool = byDomain[ov.domain].filter((it) => it.section === ov.section);
  const target = pool.find((it) => !claimed.has(it));
  if (!target) throw new Error(`DIRECTION_OVERRIDES: no unclaimed item found for ${ov.domain}/${ov.section}`);
  claimed.add(target);
  target.direction = "inverted";
  overrideByItem.set(target, ov);
}

let g = 1;
const finalItems = [];
for (const d of DOMAIN_ORDER) {
  const domainItems = [...byDomain[d]];
  const provenSet = new Set(MULTI_SECTIONS[d] || []);
  const invertedThisDomain = new Set(domainItems.filter((it) => it.direction === "inverted"));
  const candidates = domainItems
    .map((it, idx) => ({ it, idx }))
    .filter(({ it }) => provenSet.has(it.section) && !invertedThisDomain.has(it)) // keep format-novelty and direction-novelty separate
    .sort((a, b) => (a.it.kind === "facet" ? 0 : 1) - (b.it.kind === "facet" ? 0 : 1));
  const chosenIdx = new Set();
  const need = MULTI_COUNT[d] || 0;
  const usedSections = new Set();
  for (const c of candidates) {
    if (chosenIdx.size >= need) break;
    if (usedSections.has(c.it.section)) continue;
    chosenIdx.add(c.idx);
    usedSections.add(c.it.section);
  }
  if (chosenIdx.size < need) throw new Error(`Domain ${d}: only found ${chosenIdx.size} of ${need} multi-response candidates`);
  domainItems.forEach((it, idx) => {
    it.format = chosenIdx.has(idx) ? "multi" : "single";
    it.selectN = chosenIdx.has(idx) ? 2 : 1;
    const ov = overrideByItem.get(it);
    const rebalanceKey = `${it.domain}|${it.section}`;
    if (ov) {
      it.shape = ov.shape;
    } else if (SHAPE_REBALANCE[rebalanceKey] && (rebalanceKey !== "D5|5.1" || rebalanceRemaining["D5|5.1"]-- > 0)) {
      it.shape = SHAPE_REBALANCE[rebalanceKey];
    } else {
      it.shape = SHAPE_HINTS[it.section] || "S1";
    }
    if (ov) {
      it.invGuidance = `${INVERSION_DEF[ov.shape]} ${ov.note}`;
    }
    it.g = g++;
    finalItems.push(it);
  });
}

// --- 2. Correct-letter pre-plan for the 55 single-answer items ---
// Paper 4 short letter is A: {A x13, B x14, C x14, D x14}.
function seededShuffle(arr, seed) {
  let s = seed;
  const rnd = () => {
    s = (s * 1103515245 + 12345) % 2147483648;
    return s / 2147483648;
  };
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
const letterMultiset = [
  ...Array(13).fill("A"), ...Array(14).fill("B"), ...Array(14).fill("C"), ...Array(14).fill("D"),
];
const shuffledLetters = seededShuffle(letterMultiset, 3130841 /* Paper 4 seed */);
let li = 0;
for (const it of finalItems) {
  if (it.format === "single") it.correctLetter = shuffledLetters[li++];
}

// --- 3. Correct-pair assignment for the 8 multi items, cap <=2 repeats ---
const pairPlan = ["AB", "CD", "AC", "BD", "AD", "BC", "AB", "CD"]; // 8 slots, each pair <=2x
let pi = 0;
for (const it of finalItems) {
  if (it.format === "multi") it.correctPair = pairPlan[pi++];
}

// --- Sanity ---
const singleCount = finalItems.filter((i) => i.format === "single").length;
const multiCount = finalItems.filter((i) => i.format === "multi").length;
if (singleCount !== 55) throw new Error(`single count ${singleCount} != 55`);
if (multiCount !== 8) throw new Error(`multi count ${multiCount} != 8`);
const invertedCount = finalItems.filter((i) => i.direction === "inverted").length;
if (invertedCount !== 17) throw new Error(`inverted count ${invertedCount} != 17 (got ${invertedCount})`);
const shapeTally = {};
finalItems.forEach((i) => (shapeTally[i.shape] = (shapeTally[i.shape] || 0) + 1));
for (const s of ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]) {
  const n = shapeTally[s] || 0;
  if (n < 4 || n > 11) throw new Error(`Shape ${s} count ${n} violates hard floor 4 / ceiling 11`);
}
const invShapeTally = {};
finalItems.filter((i) => i.direction === "inverted").forEach((i) => (invShapeTally[i.shape] = (invShapeTally[i.shape] || 0) + 1));
for (const s of Object.keys(INVERSION_DEF)) {
  if (!invShapeTally[s] || invShapeTally[s] < 2) throw new Error(`Shape ${s} has only ${invShapeTally[s] || 0} inverted items, need >=2`);
}
const letterTally = {};
finalItems.filter((i) => i.format === "single").forEach((i) => (letterTally[i.correctLetter] = (letterTally[i.correctLetter] || 0) + 1));
const pairTally = {};
finalItems.filter((i) => i.format === "multi").forEach((i) => (pairTally[i.correctPair] = (pairTally[i.correctPair] || 0) + 1));

fs.writeFileSync("plan.json", JSON.stringify(finalItems, null, 1));

console.log("g range:", finalItems[0].g, "-", finalItems[finalItems.length - 1].g);
console.log("letter tally:", JSON.stringify(letterTally));
console.log("pair tally:", JSON.stringify(pairTally));
console.log("shape tally:", JSON.stringify(shapeTally));
console.log("inverted shape tally:", JSON.stringify(invShapeTally));
console.log("total inverted:", invertedCount);
console.log("multi items:", finalItems.filter((i) => i.format === "multi").map((i) => `g${i.g} ${i.domain} ${i.section}`));
console.log("inverted items:", finalItems.filter((i) => i.direction === "inverted").map((i) => `g${i.g} ${i.domain}/${i.section} ${i.shape}`));
console.log("Wrote plan.json");
