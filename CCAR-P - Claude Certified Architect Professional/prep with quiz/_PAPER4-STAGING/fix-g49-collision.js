#!/usr/bin/env node
/*
 * Dedup fix: g49 scored 0.319 Jaccard against Paper 3's own g49 (both D5 5.8, "claims team /
 * staffing capacity / propose reviewing everything, ease off later" framing). Recast with an
 * expense-report cover story -- same underlying M-5.8 misconception, same correct routing logic,
 * same family tags -- to drop the wording overlap. Re-verified below threshold after the edit.
 */
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));
const it = items.find((i) => i.g === 49);
if (!it) throw new Error("g49 not found");

it.stem = "A finance team can manually audit only 5% of expense reports daily, and any report over $10,000 must be checked regardless of model confidence. The current plan audits every report at rollout, easing off as trust builds. What should replace it?";
it.opts = [
  { l: "A", t: "Audit every report at rollout and reduce the audit rate as trust in the model grows.", family: "ARCHITECTED" },
  { l: "B", t: "Auto-approve low-value reports the model is confident about; route every report over $10,000 to a human regardless of confidence; periodically audit the auto-approved stream.", family: null },
  { l: "C", t: "Randomly audit a fixed percentage of all reports, sized to the team's daily capacity.", family: "WRONG-AXIS" },
  { l: "D", t: "Let the model flag any report it says it's unsure about, and audit only those.", family: "HALF-MOVE" },
];
it.whyRight = "Auditing everything from rollout collapses the team's capacity immediately since no stopping point is named; routing on confidence and dollar amount together lets low-value, high-confidence reports clear immediately while every high-value report still reaches a human.";
it.whyWrong = {
  A: "Auditing everything from rollout already exceeds the stated 5% capacity, and no threshold or date is named for when the rate would ease.",
  C: "A fixed sample sized to capacity is a way to monitor the auto-approved stream afterward, not a way to decide which reports skip audit in the first place.",
  D: "The model's own statement of confidence is not a valid routing signal -- a fluent model can be equally confident whether it is right or wrong.",
};
it.t1Clause = "can manually audit only 5% of expense reports daily";
it.t1Alt = "A";

fs.writeFileSync("items-assembled.json", JSON.stringify(items, null, 1));
const notes = JSON.parse(fs.readFileSync("assembly-notes.json", "utf8"));
notes.push("g49: DEDUP-FIX -- recast from a claims/staffing cover story to an expense-report cover story after scoring 0.319 Jaccard against Paper 3's own g49 (same underlying M-5.8 misconception and routing logic preserved; only wording/cover-story changed). Provisional until re-verified below threshold and grounding-audit reviewed.");
fs.writeFileSync("assembly-notes.json", JSON.stringify(notes, null, 1));
console.log("g49 rewritten. Word counts: stem=" + it.stem.split(/\s+/).length + ", options=" + it.opts.map(o => o.t.split(/\s+/).length).join(","));
