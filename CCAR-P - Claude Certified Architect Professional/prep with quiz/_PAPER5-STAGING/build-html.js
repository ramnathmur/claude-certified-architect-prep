#!/usr/bin/env node
/*
 * Builds mock-exams/CCAR-P_MockTest-5_v1.html from the TEMPLATE. Fixes all three known
 * template-artifact spots (landing h1/banner/stat, sticky-nav .brand text, fDemoCount JS
 * override line) in one pass, exactly as every prior paper needed (F-30's standing lesson).
 */
const fs = require("fs");

const TEMPLATE = "../mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html";
const OUT = "../mock-exams/CCAR-P_MockTest-5_v1.html";

let src = fs.readFileSync(TEMPLATE, "utf8");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));
if (items.length !== 63) throw new Error(`expected 63 items, got ${items.length}`);

// --- 1. <title> ---
src = src.replace("<title>CCAR-P Mock Test — TEMPLATE</title>", "<title>CCAR-P Mock Test 5</title>");

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
  CCAR-P MOCK TEST 5 — Practice Mode, AUTHOR mode, a fifth untargeted diagnostic (Papers 1-4 all
  generated but none sat/scored at generation time -- confirmed with Ram before generating, per
  Outputs/CCAR-P_Paper-5-Generation-Prompt_v1.md §3).
  Generated 2026-09-01 from mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html per
  prep with quiz/CCAR-P-Orchestration-Prompt_v2.md. 63 items, all source:"AUTHORED".

  D2 corpus expansion (Ram's decision, 2026-09-01): CCAR-P_Domain-2_v1.md gained 21 new
  decision-table rows across all 9 sections before this paper was planned, closing D2's own
  facet-supply crisis (0/18 fresh after Paper 4). D2 now holds 39 facets and needed no
  reuse-inversion or misconception fallback at all this paper -- every D2 item is built from a
  genuinely fresh facet, the same as every other domain.

  Direction inversion continues (orchestration prompt §7.2, Papers 4-7): 16 items ship
  direction:"inverted", at least 2 per shape across all 8 shapes, per ARCHETYPE-LEDGER.md's
  inversion table (one fewer than planned -- D5 §5.4 was flipped back to normal during the
  independent grounding audit, see below). Two of the 16 (D3 §3.1, D5 §5.8) are the standing
  "direction doubling"
  fallback -- their objectives' own facets were fully exhausted with no misconception unit left,
  so they reuse an already-shipped facet as an anchor but test the inverted direction.

  Gate check 14 (shape-budget floor 4 / ceiling 11, ARCHETYPE-LEDGER.md) is formalized this
  paper in tools/run-gate.js, closing a gap that let Paper 2 ship a silent violation undetected.

  deepDive ships null on every item (orchestration prompt §5.5 correction) -- populated later,
  only for items Ram actually misses, once the paper is scored (Phase 9).

  Fidelity gate: node tools/run-gate.js mock-exams/CCAR-P_MockTest-5_v1.html 63 - see EXAM-LOG.md
  for the full 14-check result.

  DESIGN STANCE: Practice Mode is the default. Exam Mode is a narrow exception for the two
  dress-rehearsal papers. A faithful port of the Exam Mode mechanism WITHOUT its scope once
  inverted this default for a whole project - see sop/SOP_Mock-Exam-Engine_v1.md.
-->`;
if (!src.includes(oldHeadComment)) throw new Error("head comment block not found verbatim");
src = src.replace(oldHeadComment, newHeadComment);

// --- 3. PAPER_N / KEY ---
src = src.replace(
  'const PAPER_N   = 0;                    /* 0 = template. A real paper sets its own number. */',
  "const PAPER_N   = 5;"
);
src = src.replace('const KEY       = "ccarp-mocktest-template-v1";', 'const KEY       = "ccarp-mocktest-5-v1";');
// EXAM_MODE stays false -- Paper 5 is not Paper 8 or 10

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
    <h1>CCAR-P Mock Test 5</h1>
    <p class="sub">Claude Certified Architect – Professional · untargeted diagnostic, D2 corpus expansion</p>
  </header>

  <div class="demo-banner">
    <strong>Paper 5 — a fifth untargeted diagnostic.</strong>
    63 items generated from the CCAR-P corpus at the confirmed 17/13/19/16/14/14/7 weighting, one
    item for each of the 38 official objectives. Papers 1-4 were all generated but not yet sat when
    this paper was built, so no Professor's Note exists yet to target from — Ram confirmed
    generating another diagnostic rather than pausing to sit an existing paper first. D2's corpus
    was expanded (21 new decision-table rows) before this paper was planned, closing its
    facet-supply crisis. 16 items test each shape's normal-direction lesson with its logic
    deliberately inverted, so recognising the shape alone stops being enough to answer it.
    Practice Mode, so feedback arrives per question.
  </div>

  <div class="facts">
    <div class="sf"><div class="k">Length</div><div class="v">63 items · 120 minutes</div></div>
    <div class="sf"><div class="k">Objectives covered</div><div class="v" id="fDemoCount">38 of 38</div></div>`;
if (!src.includes(oldLanding)) throw new Error("landing block not found verbatim");
src = src.replace(oldLanding, newLanding);

// --- 4b. Sticky top-nav brand text ---
src = src.replace(
  '<div class="brand">CCAR-P <span>Mock Test TEMPLATE</span></div>',
  '<div class="brand">CCAR-P <span>Mock Test 5</span></div>'
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
   63 items, AUTHORED, Paper 5 -- generated per prep with quiz/_PAPER5-STAGING/plan.json.
   16 items carry direction:"inverted" (>=2 per shape, all 8 shapes). D2's corpus expansion
   (2026-09-01) means every D2 item here is a fresh facet, not a reuse or misconception pick.

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
