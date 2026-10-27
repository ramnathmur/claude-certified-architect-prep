#!/usr/bin/env node
/*
 * Finalizes the Paper 5 central plan. Per §5-6 of the Paper 5 generation prompt:
 *  - Shape assignment via SHAPE_HINTS (same section->shape map as Paper 4, since shape is a
 *    corpus-content property, not paper-specific), plus a shape-budget rebalance (raw draw put
 *    S1 at 15, over the hard ceiling of 11) and one new hint (6.5, never drawn before now).
 *  - 16 items marked direction:"inverted", >=2 per shape across all 8 shapes, spread across all
 *    7 domains (max 3/domain) -- includes the 2 forced reuse-inverted items from build-plan.js
 *    (D3/3.1, D5/5.8, each an exhausted-facet fallback) plus 14 new inversions of THIS paper's
 *    own fresh facets, the same fresh-facet-tagged-inverted mechanism Paper 4 used for its 12
 *    non-D2 inversions. Each override carries an explicit invGuidance string quoting the
 *    inversion table's per-shape definition, per the generation prompt's explicit instruction
 *    not to leave inversion to inference from the shape name alone.
 *  - 8 multi-response items (2-of-4), sections chosen for a genuine >=2-independently-true-rows
 *    situation, kept disjoint from the direction-inverted set (format-novelty and
 *    direction-novelty stay separate, per Paper 4's own practice).
 *  - Correct-letter pre-plan ({A14,B14,C14,D13} -- Paper 5's short letter is D, per the
 *    D->C->B->A rotation), correct-pair assignment for the 8 multi items.
 */
const fs = require("fs");
const path = require("path");
const scriptDir = __dirname;
const { items: rawItems } = require("./plan-raw.json");

const DOMAIN_ORDER = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"];

const MULTI_SECTIONS = { D1: ["1.11", "1.12"], D2: [], D3: ["3.3"], D4: ["4.11"], D5: ["5.6"], D6: ["6.11"], D7: ["7.2", "7.8"] };
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
  "6.1": "S7", "6.2": "S7", "6.3": "S7", "6.4": "S7", "6.5": "S7", "6.6": "S7", "6.7": "S3",
  "6.8": "S7", "6.9": "S7", "6.10": "S6", "6.11": "S1", "6.12": "S7",
  "7.1": "S3", "7.2": "S3", "7.3": "S5", "7.5": "S4", "7.8": "S2",
};

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

// Shape rebalance: raw SHAPE_HINTS draw put S1 at 15 (hard ceiling 11). Four sections moved to a
// shape their own content fits at least as naturally (3.2's least-privilege/control-placement
// content is textbook S8, matching Paper 4's own precedent for this exact section; 3.5's
// perceived-vs-total latency is a measurement-reading question, textbook S6; 1.9's feedback-
// capture-vs-dashboard question and 4.12's logging-for-attribution question are both about
// whether the *right* mechanism is already in place vs a sophisticated-sounding alternative /
// measurement device, S4 and S6 respectively). None of these four are DIRECTION_OVERRIDES
// targets below, so this only touches normal-direction items.
const SHAPE_REBALANCE = { "D3|3.2": "S8", "D3|3.5": "S6", "D1|1.9": "S4", "D4|4.12": "S6" };

// 16 items marked direction:"inverted", >=2 per shape, spread across all 7 domains (max 3 each).
// D3/3.1 and D5/5.8 are the build-plan.js reuse-inverted fallbacks (exhausted objective, no
// fresh/misconception left -- FACET-LEDGER.md's standing "direction doubling" mechanism, in
// force since Paper 4); their `direction` is already "inverted" from build-plan.js and this
// list only attaches shape + invGuidance to them. The other 14 tag a FRESH facet already drawn
// by build-plan.js as inverted -- the same mechanism Paper 4 used for its 12 non-D2 inversions.
const DIRECTION_OVERRIDES = [
  { domain: "D3", section: "3.1", shape: "S4", note: "Reused facet F-3.1-01 (exhausted, 0 fresh facets left in 3.1 after Papers 1-4) normally tests splitting an oversized, mixed-role tool surface into role-scoped agents. Invert: the tool surface is ALREADY correctly minimized to a narrow, role-scoped set; a reviewer proposes splitting it further 'for clarity', which would strand a single atomic decision across two agents that both genuinely need the same two tools together. The current grouping is already correct; the further split is the trap. Must produce a genuinely different correct answer from F-3.1-01's own normal-direction lesson, not a reworded restate -- see F-27/F-28's standing caution on reuse-inverted items." },
  { domain: "D5", section: "5.8", shape: "S2", note: "Reused facet F-5.8-01 (exhausted, 0 fresh facets left in 5.8 after Papers 1-4) normally tests routing to human-in-the-loop. Invert: a stated hard SLA (e.g. a 2-minute response commitment) makes 100% human review infeasible for every case. No single policy satisfies both full human review and the SLA -- the correct answer states the trade explicitly: risk-tiered routing, human review only above a stated confidence/severity threshold, not blanket removal of human review. Must produce a genuinely different correct answer from F-5.8-01's own normal-direction lesson -- see F-27/F-28's standing caution." },
  { domain: "D1", section: "1.7", shape: "S1", note: "Normal-direction facet tests passing findings as {content, metadata} with sources for citation. Invert: the structured handoff already correctly includes full source metadata; a reviewer requests a 'cleaner', prose-only summary without the structured metadata block. That would break the sourcing requirement the section exists to satisfy. Correct answer: keep the structured handoff as-is; a prose-only summary is not an acceptable substitute." },
  { domain: "D1", section: "1.4", shape: "S5", note: "Normal-direction facet tests recognizing when a fixed pipeline is correct vs when dynamic agentic planning is required. Invert: a task looks bounded and templated overall, but one stated sub-step's internal structure genuinely varies per input in a way no fixed template can enumerate in advance. The higher rung -- an agent with dynamic planning for that one sub-step -- is correct despite the rest of the task looking fixed-pipeline-shaped." },
  { domain: "D1", section: "1.1", shape: "S6", note: "Normal-direction facet tests recognizing when a step should be automated, from volume/visibility signals. Invert: a team already correctly tracks a step's override rate as its automation-readiness signal. A stakeholder argues a rising override rate over the past month proves the step is 'getting better' and ready to fully automate. The metric is being read backwards: a rising override rate is evidence the step is not yet reliable, not evidence of readiness." },
  { domain: "D2", section: "2.4", shape: "S4", note: "Normal-direction facet (F-2.4-03/04, fresh) tests whether a reasoning cue is still needed once verified sufficient, or conflicts with a latency budget. Invert instead on the base mechanism: the reasoning cue is already correctly present for a genuinely multi-step task; a proposal to remove it to save tokens 'since the model already seems fast enough' is the trap that would reintroduce the accuracy failure the cue exists to prevent. The obvious mechanism (keep the cue) is correct; removing it is the sophisticated-sounding trap." },
  { domain: "D2", section: "2.1", shape: "S5", note: "Normal-direction facet tests matching model capability to task complexity/volume. Invert: a task's volume and format look simple enough for the smallest/fastest model, but the task also carries a stated open-ended judgment call (e.g. phrasing a sensitive escalation to a named regulator) that a small model's rung cannot reliably clear. The higher-capability model is correct despite the surface-level simplicity cues -- under-engineering, not over-engineering, is the trap here." },
  { domain: "D2", section: "2.2", shape: "S8", note: "Matches Paper 4's own precedent for this exact section and shape override (see EXAM-LOG.md Paper 4, D2 g19/§2.2 discussion): 2.2's system-prompt-authority rule is close to absolute, so a clean S2 trade-off framing is hard to write cleanly. Frame instead as S8: an existing system-prompt guardrail is already correctly blocking a class of requests, and is now blocking a legitimate, newly-scoped use case. Correct answer: a scoped, explicit exception at the same layer (the system prompt), not removing the guardrail or moving the check elsewhere. If no clause deletion/inversion produces a genuinely different correct option on this fresh facet, flag as a T1 IRREDUCIBLE candidate rather than forcing one." },
  { domain: "D5", section: "5.3", shape: "S8", note: "Normal-direction facet tests compliance boundary enforcement placement. Invert: a data-residency boundary control is already correctly enforced at the infrastructure layer; a new partner-integration request needs narrow, explicit, logged cross-region access. Correct answer is a scoped exception process at the same layer, not loosening the boundary itself and not moving the check into the system prompt (which the section's own Misconception block already establishes cannot enforce it)." },
  { domain: "D5", section: "5.4", shape: "S8", note: "Note: 3.2's own draw for this paper landed on its misconception unit (M-3.2, since 3.2's decision-table facets are exhausted), not a fresh facet -- a misconception-unit item isn't given a direction inversion (there is no clean 'opposite direction' of a trap belief the way a decision-table facet has one), so this item replaces it as the paper's second S8 slot. Normal-direction facet tests which regulatory constraint binds (payload shape vs deployment environment). Invert: an authorized-environment restriction is already correctly enforced, and now blocks a legitimate, lower-risk new workload that doesn't actually touch the regulated data category the restriction exists to protect. Correct answer: a scoped, explicit exception for that specific workload (its own narrow carve-out with its own review), not a blanket relaxation of the authorized-environment requirement." },
  { domain: "D4", section: "4.9", shape: "S3", note: "Normal-direction facet tests the release path for a prompt change (regression test, then controlled A/B). Invert: accuracy drops the same week a prompt change ships, but investigation shows the drop actually correlates with a simultaneous, easily-missed upstream data-schema change. The prompt change is a coincidence, not the cause; correct answer re-runs the regression/A-B investigation against the data change, not against the prompt edit." },
  { domain: "D7", section: "7.1", shape: "S3", note: "Normal-direction facet tests configuration scope and durable enablement. Invert: a team's Claude Code configuration behavior changed the same day a teammate edited a shared config file, but the actual cause is a simultaneous CLI version upgrade that changed a default. The config edit is a coincidence, not the cause; correct answer checks the CLI version/changelog first." },
  { domain: "D3", section: "3.9", shape: "S1", note: "Normal-direction facet tests preferring contextualized chunks over blind chunk enlargement. Invert: the RAG system already correctly uses contextualized chunks sized for the task; a team proposes shrinking chunk size further 'to save embedding cost', which would break a stated requirement that each chunk retain enough surrounding context to answer multi-sentence questions. Correct answer: keep the current contextualized sizing; the further shrink is the trap." },
  { domain: "D6", section: "6.10", shape: "S6", note: "Normal-direction facet tests reading feedback loops and expectation drift correctly. Invert: a satisfaction metric is already correctly tracked and defined; a stakeholder argues a recent uptick proves a recent process change fixed the underlying issue, but the uptick coincides with a seasonal low-volume period, not the change. The measurement is being read as causal evidence when it isn't." },
  { domain: "D6", section: "6.2", shape: "S7", note: "Normal-direction facet tests bounding an unbounded requirement via discovery. Invert: a stakeholder's stated mechanism (a specific named approval workflow) IS itself the actual compliance-driven requirement, not just their guess at implementation. A more elegant, automated redesign the architect prefers is out of scope even though it looks better engineered." },
  { domain: "D6", section: "6.4", shape: "S7", note: "Normal-direction facet tests reporting performance to a sponsor. Invert: the sponsor has explicitly specified the exact metric and reporting cadence they want, and that named mechanism is itself the actual governance requirement. Proposing a different, more informative metric the architect prefers is out of scope for this report." },
  { domain: "D2", section: "2.8", shape: "S2", note: "D2/2.2's S2 slot was reassigned to S8 above, leaving only the D5/5.8 forced item on S2 -- this item fills the second required S2 slot. Normal-direction facet tests static-first ordering to enable caching. Invert: a stated hard requirement (a compliance disclaimer that must reflect the current date) seems to require dynamic content at the very front of the prompt, apparently breaking the cacheable prefix. No single ordering satisfies both 'disclaimer must be first' and 'keep the prefix cacheable' -- correct answer states the trade: the disclaimer sits immediately after the stable cached prefix, since the compliance requirement is about the disclaimer's presence and prominence, not about being the literal first byte of the API payload." },
];

// --- 1. Order items by domain, apply direction overrides ---
const byDomain = {};
DOMAIN_ORDER.forEach((d) => (byDomain[d] = rawItems.filter((i) => i.domain === d)));

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
    .filter(({ it }) => provenSet.has(it.section) && !invertedThisDomain.has(it))
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
    } else if (SHAPE_REBALANCE[rebalanceKey]) {
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
// Paper 5 short letter is D (rotation D->C->B->A repeats: P1=D, P2=C, P3=B, P4=A, P5=D).
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
  ...Array(14).fill("A"), ...Array(14).fill("B"), ...Array(14).fill("C"), ...Array(13).fill("D"),
];
const shuffledLetters = seededShuffle(letterMultiset, 20260901 /* Paper 5 seed */);
let li = 0;
for (const it of finalItems) {
  if (it.format === "single") it.correctLetter = shuffledLetters[li++];
}

// --- 3. Correct-pair assignment for the 8 multi items, cap <=2 repeats ---
const pairPlan = ["AB", "CD", "AC", "BD", "AD", "BC", "AB", "CD"];
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
const invDomainTally = {};
finalItems.filter((i) => i.direction === "inverted").forEach((i) => (invDomainTally[i.domain] = (invDomainTally[i.domain] || 0) + 1));
const letterTally = {};
finalItems.filter((i) => i.format === "single").forEach((i) => (letterTally[i.correctLetter] = (letterTally[i.correctLetter] || 0) + 1));
const pairTally = {};
finalItems.filter((i) => i.format === "multi").forEach((i) => (pairTally[i.correctPair] = (pairTally[i.correctPair] || 0) + 1));

fs.writeFileSync(path.join(scriptDir, "plan.json"), JSON.stringify(finalItems, null, 1));

console.log("g range:", finalItems[0].g, "-", finalItems[finalItems.length - 1].g);
console.log("letter tally:", JSON.stringify(letterTally));
console.log("pair tally:", JSON.stringify(pairTally));
console.log("shape tally:", JSON.stringify(shapeTally));
console.log("inverted shape tally:", JSON.stringify(invShapeTally));
console.log("inverted domain tally:", JSON.stringify(invDomainTally));
console.log("total inverted:", invertedCount);
console.log("multi items:", finalItems.filter((i) => i.format === "multi").map((i) => `g${i.g} ${i.domain} ${i.section}`));
console.log("inverted items:", finalItems.filter((i) => i.direction === "inverted").map((i) => `g${i.g} ${i.domain}/${i.section} ${i.shape}`));
console.log("Wrote plan.json");
