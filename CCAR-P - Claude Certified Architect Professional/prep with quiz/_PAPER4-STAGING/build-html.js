#!/usr/bin/env node
/*
 * Builds mock-exams/CCAR-P_MockTest-4_v1.html from the TEMPLATE. Fixes all three known
 * template-artifact spots (landing h1/banner/stat, sticky-nav .brand text, fDemoCount JS
 * override line) in one pass -- per the Paper 4 prompt §4f checklist.
 */
const fs = require("fs");

const TEMPLATE = "../mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html";
const OUT = "../mock-exams/CCAR-P_MockTest-4_v1.html";

let src = fs.readFileSync(TEMPLATE, "utf8");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));
if (items.length !== 63) throw new Error(`expected 63 items, got ${items.length}`);

// --- 1. <title> ---
src = src.replace("<title>CCAR-P Mock Test — TEMPLATE</title>", "<title>CCAR-P Mock Test 4</title>");

// --- 2. Head comment block ---
const oldHeadComment = `<!--
  CCAR-P MOCK TEST ENGINE — TEMPLATE v1
  Built 2026-08-29 from Outputs/CCAR-P_Mock-Exam-Engine-Audit_v1.md Part C.

  TO MAKE A REAL PAPER:
    1. Replace PAPER_N, KEY, and the ITEMS array. Change nothing else.
    2. ITEMS must hold 63 items. The four below are DEMO CONTENT and are not
       corpus-generated - they exist so the engine can be verified before a paper exists.
    3. Run validateItems() in Node before shipping - see the block at the foot of this file.
    4. EXAM_MODE stays false unless the paper is Paper 8 or Paper 10.

  DESIGN STANCE: Practice Mode is the default. Exam Mode is a narrow exception for the two
  dress-rehearsal papers. A faithful port of the Exam Mode mechanism WITHOUT its scope once
  inverted this default for a whole project - see sop/SOP_Mock-Exam-Engine_v1.md.
-->`;
const newHeadComment = `<!--
  CCAR-P MOCK TEST 4 — Practice Mode, AUTHOR mode, untargeted diagnostic (Papers 1, 2 and 3 all
  generated but none sat/scored at generation time -- confirmed with Ram before generating, per
  Outputs/CCAR-P_Paper-4-Generation-Prompt_v1.md §3).
  Generated 2026-08-31 from mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html per
  prep with quiz/CCAR-P-Orchestration-Prompt_v2.md. 63 items, all source:"AUTHORED".

  Direction inversion begins this paper (orchestration prompt §7.2, Papers 4-7): 17 items ship
  direction:"inverted", at least 2 per shape across all 8 shapes, per ARCHETYPE-LEDGER.md's
  inversion table.

  deepDive ships null on every item (orchestration prompt §5.5 correction) -- populated later,
  only for items Ram actually misses, once the paper is scored (Phase 9).

  D2 note: Domain 2's decision-table facet supply is fully exhausted after Papers 1-3 (0 of 18
  facets fresh). Per Ram's approved decision, 3 of D2's 8 items use the last unused misconception
  units (M-2.3, M-2.5, M-2.9); the other 5 (sections 2.1, 2.2, 2.4, 2.7, 2.8) are direction-
  inverted reuse of an already-shipped facet as an anchor. Section 2.2's item is a documented
  IRREDUCIBLE case (T1/T2 do not cleanly resolve -- the section's rule is absolute, matching
  Paper 2's g14/g15 precedent).

  Fidelity gate: node tools/run-gate.js mock-exams/CCAR-P_MockTest-4_v1.html 63 - see EXAM-LOG.md
  for the full 13-check result.

  DESIGN STANCE: Practice Mode is the default. Exam Mode is a narrow exception for the two
  dress-rehearsal papers. A faithful port of the Exam Mode mechanism WITHOUT its scope once
  inverted this default for a whole project - see sop/SOP_Mock-Exam-Engine_v1.md.
-->`;
if (!src.includes(oldHeadComment)) throw new Error("head comment block not found verbatim");
src = src.replace(oldHeadComment, newHeadComment);

// --- 3. PAPER_N / KEY ---
src = src.replace(
  'const PAPER_N   = 0;                    /* 0 = template. A real paper sets its own number. */',
  "const PAPER_N   = 4;"
);
src = src.replace('const KEY       = "ccarp-mocktest-template-v1";', 'const KEY       = "ccarp-mocktest-4-v1";');
// EXAM_MODE stays false -- Paper 4 is not Paper 8 or 10

// --- 4. Landing page: h1 / sub / demo-banner / fDemoCount stat ---
const oldLanding = `  <header class="doc">
    <h1>CCAR-P Mock Test — Template</h1>
    <p class="sub">Claude Certified Architect – Professional · engine template, not a paper</p>
  </header>

  <div class="demo-banner">
    <strong>This file is the engine, not an exam.</strong> The four questions below are demo content
    written to verify that scoring, multi-response handling, the fidelity fields, and the three exports
    work. They are not drawn from the corpus and must not be sat as practice. A real paper replaces the
    <code>ITEMS</code> array with 63 corpus-generated items and nothing else.
  </div>

  <div class="facts">
    <div class="sf"><div class="k">Real paper length</div><div class="v">63 items · 120 minutes</div></div>
    <div class="sf"><div class="k">This template</div><div class="v" id="fDemoCount">4 demo items</div></div>`;
const newLanding = `  <header class="doc">
    <h1>CCAR-P Mock Test 4</h1>
    <p class="sub">Claude Certified Architect – Professional · untargeted diagnostic, direction inversion begins</p>
  </header>

  <div class="demo-banner">
    <strong>Paper 4 — a third untargeted diagnostic, and the first with direction inversion.</strong>
    63 items generated from the CCAR-P corpus at the confirmed 17/13/19/16/14/14/7 weighting, one
    item for each of the 38 official objectives. Papers 1-3 were all generated but not yet sat when
    this paper was built, so no Professor's Note exists yet to target from — Ram confirmed
    generating another diagnostic rather than pausing to sit an existing paper first. New this
    paper: 17 items test each shape's normal-direction lesson with its logic deliberately
    inverted, so recognising the shape alone stops being enough to answer it. Practice Mode, so
    feedback arrives per question.
  </div>

  <div class="facts">
    <div class="sf"><div class="k">Length</div><div class="v">63 items · 120 minutes</div></div>
    <div class="sf"><div class="k">Objectives covered</div><div class="v" id="fDemoCount">38 of 38</div></div>`;
if (!src.includes(oldLanding)) throw new Error("landing block not found verbatim");
src = src.replace(oldLanding, newLanding);

// --- 4b. Sticky top-nav brand text ---
src = src.replace(
  '<div class="brand">CCAR-P <span>Mock Test TEMPLATE</span></div>',
  '<div class="brand">CCAR-P <span>Mock Test 4</span></div>'
);

// --- 4c. fDemoCount JS override ---
src = src.replace(
  'document.getElementById("fDemoCount").textContent = ITEMS.length + " demo items";',
  'document.getElementById("fDemoCount").textContent = new Set(ITEMS.map(function(x){return x.objective;})).size + " of 38";'
);

// --- 5. ITEMS schema comment ---
const oldSchemaIntro = `/* ================= ITEMS =================
   DEMO CONTENT - four items written to the measured official style so the engine can be
   verified. Replace wholesale with 63 corpus-generated items.

   Schema, per CCAR-P-Orchestration-Prompt_v2.md 5.5:`;
const newSchemaIntro = `/* ================= ITEMS =================
   63 items, AUTHORED, Paper 4 -- generated per prep with quiz/_PAPER4-STAGING/plan.json.
   17 items carry direction:"inverted" (>=2 per shape, all 8 shapes).

   Schema, per CCAR-P-Orchestration-Prompt_v2.md 5.5:`;
if (!src.includes(oldSchemaIntro)) throw new Error("schema intro not found verbatim");
src = src.replace(oldSchemaIntro, newSchemaIntro);

// --- 6. Replace the ITEMS array itself ---
const marker = "const ITEMS = [";
const startAt = src.indexOf(marker);
if (startAt < 0) throw new Error("const ITEMS = [ not found");
const closeMarker = "\n];";
const closeAt = src.indexOf(closeMarker, startAt);
if (closeAt < 0) throw new Error("closing ]; not found");

const itemsJs = JSON.stringify(items, null, 1);
const newBlock = marker + "\n" + itemsJs.slice(1, -1).trim() + "\n];";

const before = src.slice(0, startAt);
const after = src.slice(closeAt + closeMarker.length);
src = before + newBlock + after;

fs.writeFileSync(OUT, src);
console.log("Wrote", OUT, "-", src.length, "bytes");
