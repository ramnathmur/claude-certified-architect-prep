#!/usr/bin/env node
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("plan.json", "utf8"));

let md = `# Paper 3 — Central Plan (Slots)\n\n`;
md += `Computed centrally, before any authoring dispatch, per Phase 6 of\n`;
md += `\`Outputs/CCAR-P_Paper-3-4-Generation-Prompt_v1.md\`. Untargeted diagnostic — Papers 1 and 2 are\n`;
md += `generated but neither has been sat, confirmed with Ram before generating (§2). Mode: AUTHOR.\n`;
md += `All 63 items \`direction: "normal"\` (direction inversion doesn't start until Paper 4).\n\n`;
md += `Every item ships \`deepDive: null\` at generation time (§5.5 correction, Paper 2 onward).\n\n`;

const DOMAIN_ORDER = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"];
for (const d of DOMAIN_ORDER) {
  const domainItems = items.filter((i) => i.domain === d);
  md += `## ${d} (${domainItems.length} items, g${domainItems[0].g}-g${domainItems[domainItems.length - 1].g})\n\n`;
  md += `| g | section | objective | source | pass | shape | format | correct |\n`;
  md += `|---|---|---|---|---|---|---|---|\n`;
  for (const it of domainItems) {
    const src = it.kind === "facet" ? it.id : `${it.id} (misconception unit)`;
    const correct = it.format === "multi" ? `MULTI selectN:2, pair ${it.correctPair}` : it.correctLetter;
    md += `| g${it.g} | ${it.section} | ${it.objective} | ${src} | ${it.pass} | ${it.shape} | ${it.format} | ${correct} |\n`;
  }
  md += `\n`;
}

const letterTally = {};
items.filter((i) => i.format === "single").forEach((i) => (letterTally[i.correctLetter] = (letterTally[i.correctLetter] || 0) + 1));
const pairTally = {};
items.filter((i) => i.format === "multi").forEach((i) => (pairTally[i.correctPair] = (pairTally[i.correctPair] || 0) + 1));
const shapeTally = {};
items.forEach((i) => (shapeTally[i.shape] = (shapeTally[i.shape] || 0) + 1));

md += `## Pre-plan tallies (gate checks 2, 5, 6, 7 targets)\n\n`;
md += `- **Domain quota**: 11/8/12/10/9/9/4 — no confirmed-weakness adjustment (no scored papers exist yet to confirm one).\n`;
md += `- **Correct-letter tally (55 single-answer)**: ${JSON.stringify(letterTally)} — Paper 3's short letter is B (P1 short D, P2 short C, P3 short B, P4 short A).\n`;
md += `- **Multi-response pairs (8 items)**: ${JSON.stringify(pairTally)} — each pair used at most twice.\n`;
md += `- **Shape tally**: ${JSON.stringify(shapeTally)} — all within the 6-9 target band (hard floor 4, hard ceiling 11). Soft guidance only: an authoring sub-batch may substitute a better-fitting shape for a specific facet's content; keep the paper-wide count for any shape from falling below 4 or rising above 11 if you do.\n`;
md += `- **Objective floor**: all 38 objectives covered exactly once at minimum; discretionary pass caps every objective at 3 items total this paper.\n`;
md += `- **Distractor family paper-wide floors to keep in mind while drafting** (checked and fixed centrally at assembly per F-19 — do not force it per-batch, but do not default to WRONG-AXIS/HALF-MOVE for convenience either): EVIDENCE-MISMATCH >= 15 of ~189 distractors (8%), DETECTIVE-FOR-PREVENTIVE >= 9 (5%), no family > 47 (25%), ARCHITECTED <= 19 (10%). D3/D5/D7 items about removing/restricting a capability are natural DETECTIVE-FOR-PREVENTIVE homes (a distractor that monitors/logs the misuse instead of removing the capability). Items where the stem states specific evidence that itself rules out a plausible-sounding cause are natural EVIDENCE-MISMATCH homes.\n\n`;

md += `## D2 note — misconception-unit fallback invoked for the first time\n\n`;
md += `D2 has only 18 facets against an 8-item/paper quota (F-01). After Papers 1-2 consumed 16 of\n`;
md += `18, only 2 fresh decision-table facets remain (F-2.2-03, F-2.3-02). Per Phase 4 rule 5, the other\n`;
md += `6 of D2's 8 items draw on that section's **misconception unit** instead of a facet:\n`;
md += `M-2.1, M-2.2, M-2.4, M-2.6, M-2.7, M-2.8. A misconception-unit item is built from the section's\n`;
md += `\`Misconception\` block (a stated wrong belief + its correction), not a \`Situation | Answer | Why\`\n`;
md += `row — read that block in \`CCAR-P_Domain-2_v1.md\` fresh for each one; do not paraphrase from\n`;
md += `\`FACET-LEDGER.md\`'s truncated excerpt. Leave \`facet\` as the \`M-<section>\` string and \`lessonKey\`\n`;
md += `as \`""\` for these six items (no decision-table answer text exists to derive a lessonKey from).\n`;
md += `This leaves M-2.3, M-2.5, M-2.9 in reserve for Papers 4-5. **The D2 corpus-expansion decision\n`;
md += `(F-01) is not due until the Paper 4 Insights Round** — this is expected, mechanized behaviour,\n`;
md += `not a stop-and-ask condition, but worth a clear note in the Paper 3 generation entry since it is\n`;
md += `the first paper where the fallback actually fires.\n`;

fs.writeFileSync("p3-slots.md", md);
console.log("Wrote p3-slots.md");
