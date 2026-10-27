#!/usr/bin/env node
/*
 * Applies all confirmed fixes from the 7 independent grounding audits (all 63 items covered).
 * Content reworks (real defects): g1 (not a genuine inversion -> reworked into one),
 * g13 (audit found it resolves, not IRREDUCIBLE -> reworded option A per audit's own suggestion),
 * g19 (cosmetic restate of Paper 1's already-shipped lesson -> reworked into a genuine
 * irreconcilable-constraint inversion), g22 (SLA "no slack" contradicted its own correct answer),
 * g45 (never established an AI/LLM system), g56 (mis-cited to 6.2, content is actually 6.6),
 * g60 (structural near-duplicate of Paper 1's own g60 -> reworked scenario specifics).
 * Tag-only fixes (family/shape/objective mislabels): g2-C, g5-D, g15, g21-D... wait g21-B,
 * g46, g57 (t1Clause typo).
 * g63 is NOT force-fixed: two independent readers (the author and the auditor) agree T1 does
 * not resolve -- left as a documented IRREDUCIBLE exception, per standing project practice.
 */
const fs = require("fs");
const path = "items-assembled.json";
const items = JSON.parse(fs.readFileSync(path, "utf8"));
const byG = {};
items.forEach((i) => (byG[i.g] = i));

const STOPWORDS = new Set(["the","a","an","and","or","of","to","in","on","for","with","at","by","from","is","are","be","this","that","it","its","as","not","no"]);
function lessonKey(raw) {
  if (!raw) return "";
  const tokens = raw.toLowerCase().replace(/[^\w\s]/g, " ").split(/\s+/).filter(Boolean).filter((t) => !STOPWORDS.has(t));
  const unique = [...new Set(tokens)].sort();
  return unique.length < 3 ? "" : unique.join(" ");
}
function wc(s) { return s.trim().split(/\s+/).filter(Boolean).length; }

// ---------- g1: rework into a genuine S6 inversion (measurement exists, read wrongly) ----------
{
  // Correct answer must land on letter C -- g1 was pre-planned as a "C" slot in the paper's
  // balanced 55-item letter tally; changing which letter is correct without preserving that
  // would unbalance the pre-plan (gate check 6).
  const it = byG[1];
  it.stem = "An insurer tracks underwriter override rate as the correctly-defined proxy for a risk-tier model's 12-month loss ratio. The rate has fallen from 9% to under 1% in two months, and a stakeholder calls this proof of accuracy. What should the team check first?";
  it.opts = [
    { l: "A", t: "Stand up a quarterly audit sampling overridden and non-overridden calls to formally validate the trend.", family: "ARCHITECTED" },
    { l: "B", t: "Whether the 12-month loss ratio has already improved, since that would confirm the override trend.", family: "EVIDENCE-MISMATCH" },
    { l: "C", t: "Whether underwriters are still reviewing calls closely enough to catch a wrong tier, since a falling rate can mean disengagement.", family: null },
    { l: "D", t: "Whether the model's self-reported confidence scores have risen over the same period.", family: "WRONG-AXIS" },
  ];
  it.whyRight = "Override rate is a proxy for whether underwriters still catch wrong tiers; a falling rate is exactly as consistent with reviewers disengaging as with the model improving, so review engagement is the first thing to rule out before crediting the trend to accuracy.";
  it.whyWrong = {
    A: "An elaborate quarterly audit is a real check eventually, but it is not the first, most direct one; whether reviewers are still engaged needs answering before building a bigger validation mechanism.",
    B: "The loss ratio takes 12 months to resolve and only two have passed; the stem gives no reason to expect it has moved yet, so checking it first contradicts the stated timeline.",
    D: "The model's own confidence score is not a validated proxy for anything in this section; a model can report high confidence while still being wrong.",
  };
  it.t1Clause = "over two months";
  it.t1Alt = "B";
  it.lessonKey = lessonKey("Whether underwriters are still reviewing calls closely enough to catch a wrong tier since a falling rate can also mean disengagement");
}

// ---------- g2-C: family REPAIR -> EVIDENCE-MISMATCH (content unchanged) ----------
byG[2].opts.find((o) => o.l === "C").family = "EVIDENCE-MISMATCH";

// ---------- g5-D: family OVERSPEC -> ARCHITECTED (content unchanged) ----------
byG[5].opts.find((o) => o.l === "D").family = "ARCHITECTED";

// ---------- g13: reword option A to make the no-op explicit (audit: resolves, not IRREDUCIBLE) ----------
{
  const it = byG[13];
  const a = it.opts.find((o) => o.l === "A");
  a.t = "Leave the guardrail's trigger conditions and language exactly as configured; the boundary already does what it needs to.";
  a.family = "HALF-MOVE";
  it.whyWrong.A = "Leaving the guardrail unchanged keeps blocking the approved fraud-investigation case exactly like every other after-hours request, which does not accommodate the exception leadership has actually authorized.";
}

// ---------- g15: shape S6 -> S3 (content unchanged, textbook post-change diagnosis) ----------
byG[15].shape = "S3";

// ---------- g19: rework into a genuine S2 inversion (irreconcilable constraint, not a restate) ----------
{
  // Correct answer must land on letter B -- g19 was pre-planned as a "B" slot in the paper's
  // balanced 55-item letter tally.
  const it = byG[19];
  it.stem = "A regulator requires a live, per-request audit token as the first element in every request to a compliance-sensitive endpoint, non-negotiable. The same endpoint also sends an identical 4,000-token policy preamble every call, and the team wants caching to cut cost. What should the architect recommend?";
  it.opts = [
    { l: "A", t: "Move the audit token after the policy preamble so the preamble is cached, treating the first-position rule as a formality.", family: "DISCARD" },
    { l: "B", t: "Accept that this request type cannot use prompt caching, since the per-request token breaks the stable prefix caching needs.", family: null },
    { l: "C", t: "Cache the audit token itself alongside the preamble, since it is required on every call.", family: "EVIDENCE-MISMATCH" },
    { l: "D", t: "Drop the audit token from this call, relying on a separate compliance log to record the disclosure after the fact.", family: "DETECTIVE-FOR-PREVENTIVE" },
  ];
  it.whyRight = "The regulator's per-request-first rule and caching's byte-identical-prefix requirement genuinely conflict for this call; the honest recommendation accepts caching does not apply here rather than reordering around a stated non-negotiable rule or logging around it after the fact.";
  it.whyWrong = {
    A: "Reordering around a rule the stem states is non-negotiable discards the actual requirement to recover the caching benefit, instead of resolving the conflict honestly.",
    C: "The stem states the token is generated per request; caching a value that changes on every call contradicts the one thing caching needs, a byte-identical, stable prefix.",
    D: "A log entry made afterward does not put the required token in the request itself; the rule is about what the request carries, not what gets recorded elsewhere.",
  };
  it.t1Clause = "as the first element in every request to a compliance-sensitive endpoint, non-negotiable";
  it.t1Alt = "A";
  it.lessonKey = lessonKey("Accept that this request type cannot use prompt caching since the per request token breaks the stable prefix caching needs");
}

// ---------- g21-B: family ARCHITECTED -> HALF-MOVE (content unchanged) ----------
byG[21].opts.find((o) => o.l === "B").family = "HALF-MOVE";

// ---------- g22: fix the SLA "no slack" contradiction ----------
{
  const it = byG[22];
  it.stem = "A risk-classification service faces a regulator-mandated p95 latency SLA of 2,000ms, currently running at 1,970ms with roughly 30ms of slack. Compliance also wants a 6-point accuracy gain, but every available accuracy lever adds latency. What should the architect recommend?";
  it.opts[1].t = "Apply the cheapest accuracy-per-millisecond lever that fits inside the remaining slack, accept a smaller gain, and report the shortfall.";
  it.whyRight = "The SLA is regulator-mandated and the remaining slack is small, so the only defensible move is the cheapest lever that stays inside that budget, taking a smaller accuracy gain and reporting the remaining shortfall honestly to the business.";
  it.whyWrong.C = "The stem states the SLA is already met with only about 30ms of slack; a larger model adds far more latency than the budget can absorb.";
}

// ---------- g46: objective O5.4 -> O5.5 ----------
byG[46].objective = "O5.5";

// ---------- g45: tie the network-layer control explicitly to an AI/LLM data flow ----------
{
  const it = byG[45];
  it.stem = "A financial-services firm enforces data-residency at the network layer, blocking outbound cross-region traffic from its Claude-based assistant's inference calls. A vetted partner integration now needs the assistant to read specific records from one approved partner region. What should the team do?";
}

// ---------- g56: re-cite to the section its content actually tests (6.6, not 6.2) ----------
{
  const it = byG[56];
  it.section = "6.6";
  it.facet = "F-6.6-04";
  it.objective = "O6.2";
  it.cite = it.domain + " " + it.section; // was missed on first pass -- caught by browser re-verification
}

// ---------- g57: t1Clause exact-substring fix ----------
byG[57].t1Clause = "No regulator or sign-off rule governs the segment";

// ---------- g60: rework scenario specifics to reduce structural duplication with Paper 1's g60 ----------
{
  const it = byG[60];
  it.stem = "A 40-engineer platform team's incident-triage skill can invoke a package-publish command that should never run automatically, and its log-scanning step floods context with raw output before the on-call engineer sees a diagnosis, missing the 15-minute incident SLA. Select two fixes.";
  it.opts = [
    { l: "A", t: "Scope `allowed-tools` in the skill's SKILL.md frontmatter to exclude the publish command.", family: null },
    { l: "B", t: "Set `context: fork` for the log-scanning step so only its diagnosis returns to the main conversation.", family: null },
    { l: "C", t: "Add a `deny` rule for the publish command to `settings.json`, blocking it project-wide for every skill.", family: "OVERSPEC" },
    { l: "D", t: "Add an instruction to the skill's body telling it never to publish packages automatically.", family: "REPAIR" },
  ];
  it.whyRight = "Scoping `allowed-tools` removes the skill's own access to the publish command, and forking the log-scanning step keeps its raw output from crowding the diagnosis out of context — each fix targets the specific mechanism the requirement actually depends on.";
  it.whyWrong = {
    C: "A project-wide deny rule blocks the command for every skill and tool; nothing here calls for restricting the whole project, only this one skill's own access.",
    D: "Prose in the skill body asks the model to police itself and competes with everything else in context; it does not change what the skill is actually permitted to run.",
  };
  it.t1Clause = "a package-publish command that should never run automatically";
  it.t1Alt = "C";
  it.lessonKey = lessonKey("allowed tools frontmatter scope skill exclude publish command context fork log scanning step");
}

// ---------- g59-A: family ARCHITECTED -> DISCARD (cap-driven fix, per F-19/F-25: option D
// already carries HALF-MOVE, so A needs a different family. The reasoning -- a general
// narrative "does not flag" the one specific load-bearing threshold -- fits DISCARD (solves
// the documentation problem by throwing away the specific detail that mattered) at least as
// well as ARCHITECTED; ARCHITECTED sat at 20, one over the 19 ceiling, after g1's rework
// added a genuine new ARCHITECTED instance) ----------
byG[59].opts.find((o) => o.l === "A").family = "DISCARD";

// ---------- g63: no content change -- document as IRREDUCIBLE (2 independent readers agree T1 fails) ----------
byG[63].t1IrreducibleNote = "IRREDUCIBLE per independent grounding audit, confirming the author's own flagged doubt: no stem clause negation promotes option B to correct without also removing the scenario's premise. t1Clause/t1Alt kept as the author's best-effort attempt, not a resolved T1.";

fs.writeFileSync(path, JSON.stringify(items, null, 1));

// ---------- Sanity: word caps on every edited item ----------
const touched = [1, 13, 19, 22, 45, 56, 60];
console.log("Word-cap check on reworked items:");
touched.forEach((g) => {
  const it = byG[g];
  const optLens = it.opts.map((o) => wc(o.t));
  console.log(`g${g}: stem=${wc(it.stem)} opts=${JSON.stringify(optLens)} spread=${Math.max(...optLens) - Math.min(...optLens)} whyRight=${wc(it.whyRight)} whyWrong=${JSON.stringify(Object.fromEntries(Object.entries(it.whyWrong).map(([k, v]) => [k, wc(v)])))}`);
});

const citeMismatches = items.filter((it) => it.cite !== `${it.domain} ${it.section}`);
console.log("\ncite/section mismatches (should be none):", citeMismatches.length ? citeMismatches.map((i) => `g${i.g}: cite="${i.cite}" but section="${i.section}"`) : "none");

const familyTally = {};
items.forEach((it) => (it.opts || []).forEach((o) => { if (o.family) familyTally[o.family] = (familyTally[o.family] || 0) + 1; }));
console.log("\nFinal family tally:", JSON.stringify(familyTally));
const shapeTally = {};
items.forEach((it) => (shapeTally[it.shape] = (shapeTally[it.shape] || 0) + 1));
console.log("Final shape tally:", JSON.stringify(shapeTally));
console.log("\nDone.");
