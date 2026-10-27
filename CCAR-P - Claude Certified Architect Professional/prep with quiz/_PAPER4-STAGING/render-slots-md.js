#!/usr/bin/env node
const fs = require("fs");
const items = JSON.parse(fs.readFileSync("plan.json", "utf8"));

let md = `# Paper 4 — Central Plan (Slots)\n\n`;
md += `Computed centrally, before any authoring dispatch, per Phase 6/§6 of\n`;
md += `\`Outputs/CCAR-P_Paper-4-Generation-Prompt_v1.md\`. Untargeted diagnostic — Papers 1, 2 and 3 are\n`;
md += `all generated but none has been sat, confirmed with Ram before generating (§3). Mode: AUTHOR.\n`;
md += `**Direction inversion begins this paper** — 17 items ship \`direction: "inverted"\`, >=2 per shape,\n`;
md += `each with an \`invGuidance\` string quoting the exact inversion definition. Every item ships\n`;
md += `\`deepDive: null\` at generation time.\n\n`;

const DOMAIN_ORDER = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"];
for (const d of DOMAIN_ORDER) {
  const domainItems = items.filter((i) => i.domain === d);
  md += `## ${d} (${domainItems.length} items, g${domainItems[0].g}-g${domainItems[domainItems.length - 1].g})\n\n`;
  md += `| g | section | objective | source | pass | shape | direction | format | correct |\n`;
  md += `|---|---|---|---|---|---|---|---|---|\n`;
  for (const it of domainItems) {
    const src = it.kind === "facet" ? it.id : it.kind === "reuse-inverted" ? `${it.id} (REUSE ANCHOR, invert)` : `${it.id} (misconception unit)`;
    const correct = it.format === "multi" ? `MULTI selectN:2, pair ${it.correctPair}` : it.correctLetter;
    md += `| g${it.g} | ${it.section} | ${it.objective} | ${src} | ${it.pass} | ${it.shape} | ${it.direction} | ${it.format} | ${correct} |\n`;
  }
  md += `\n`;
  const inverted = domainItems.filter((i) => i.direction === "inverted");
  if (inverted.length) {
    md += `### ${d} inversion guidance\n\n`;
    inverted.forEach((it) => {
      md += `**g${it.g}** (${it.section}, ${it.shape}): ${it.invGuidance}\n\n`;
    });
  }
}

const letterTally = {};
items.filter((i) => i.format === "single").forEach((i) => (letterTally[i.correctLetter] = (letterTally[i.correctLetter] || 0) + 1));
const pairTally = {};
items.filter((i) => i.format === "multi").forEach((i) => (pairTally[i.correctPair] = (pairTally[i.correctPair] || 0) + 1));
const shapeTally = {};
items.forEach((i) => (shapeTally[i.shape] = (shapeTally[i.shape] || 0) + 1));
const invShapeTally = {};
items.filter((i) => i.direction === "inverted").forEach((i) => (invShapeTally[i.shape] = (invShapeTally[i.shape] || 0) + 1));

md += `## Pre-plan tallies (gate checks 2, 5, 6, 7 targets)\n\n`;
md += `- **Domain quota**: 11/8/12/10/9/9/4 — no confirmed-weakness adjustment (no scored papers exist yet to confirm one).\n`;
md += `- **Correct-letter tally (55 single-answer)**: ${JSON.stringify(letterTally)} — Paper 4's short letter is A (P1 short D, P2 short C, P3 short B, P4 short A, then repeats).\n`;
md += `- **Multi-response pairs (8 items)**: ${JSON.stringify(pairTally)} — each pair used at most twice.\n`;
md += `- **Shape tally**: ${JSON.stringify(shapeTally)} — all within the hard floor 4 / hard ceiling 11 (rebalanced from a raw SHAPE_HINTS draw that put S1 at 15 and S8 at 3 — three normal-direction items at D3/3.2 and D5/5.1(x2) were moved from S1 to S8, and D4/4.6 from S1 to S6, since those sections fit the reassigned shape at least as naturally). Soft guidance only beyond that: an authoring sub-batch may substitute a better-fitting shape for a specific facet's content, but do not let any shape fall below 4 or rise above 11.\n`;
md += `- **Inverted-direction shape tally**: ${JSON.stringify(invShapeTally)} — all 8 shapes have >=2 inverted instances, spread across 6 of 7 domains (D2 supplies 5, structurally forced by its supply crisis; the other 12 spread across D1/D3/D4/D5/D6).\n`;
md += `- **Objective floor**: all 38 objectives covered exactly once at minimum; discretionary pass caps every objective at 3 items total this paper.\n`;
md += `- **Distractor family paper-wide floors to keep in mind while drafting** (checked and fixed centrally at assembly per F-19 — do not force it per-batch, but do not default to WRONG-AXIS/HALF-MOVE for convenience either): EVIDENCE-MISMATCH >= 15 of ~189 distractors (8%), DETECTIVE-FOR-PREVENTIVE >= 9 (5%), no family > 47 (25%), ARCHITECTED <= 19 (10%). D3/D5/D7 items about removing/restricting a capability are natural DETECTIVE-FOR-PREVENTIVE homes. Items where the stem states specific evidence that itself rules out a plausible-sounding cause are natural EVIDENCE-MISMATCH homes.\n\n`;

md += `## D2 note — direction-inverted reuse fires for the first time, Ram's approved decision\n\n`;
md += `D2's real decision-table facet supply is fully exhausted (0 of 18 facets fresh across Papers\n`;
md += `1-3). Per Ram's decision recorded in \`EXAM-LOG.md\`'s Paper 4 entry: 3 of D2's 8 items use the\n`;
md += `last unused misconception units (M-2.3, M-2.5, M-2.9, sections 2.3/2.5/2.9), built normally. The\n`;
md += `other 5 (sections 2.1, 2.2, 2.4, 2.7, 2.8) reuse an already-shipped facet as an anchor but must\n`;
md += `test the inverted direction — see the D2 inversion guidance above and \`p4-shared-brief.md\`'s D2\n`;
md += `section. Section 2.2 is flagged as a likely IRREDUCIBLE case (Paper 2's g14/g15 already found no\n`;
md += `conditional row there); attempt the best defensible inversion but document honestly if it does\n`;
md += `not resolve, per the shared brief's honesty rule.\n`;

fs.writeFileSync("p4-slots.md", md);
console.log("Wrote p4-slots.md");
