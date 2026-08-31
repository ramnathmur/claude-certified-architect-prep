#!/usr/bin/env node
/*
 * Builds mock-exams/CCAR-P_MockTest-3_v1.html from the TEMPLATE: swaps PAPER_N/KEY, the landing
 * page title/banner/stat (so Paper 3 doesn't ship with the template's stale placeholder text --
 * see the flagged Paper 2 defect this session found while building this), the ITEMS array with
 * the 63 assembled items, and the ITEMS schema comment header.
 */
const fs = require("fs");

const TEMPLATE = "../mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html";
const OUT = "../mock-exams/CCAR-P_MockTest-3_v1.html";

let src = fs.readFileSync(TEMPLATE, "utf8");
const items = JSON.parse(fs.readFileSync("items-assembled.json", "utf8"));
if (items.length !== 63) throw new Error(`expected 63 items, got ${items.length}`);

// --- 1. <title> ---
src = src.replace("<title>CCAR-P Mock Test — TEMPLATE</title>", "<title>CCAR-P Mock Test 3</title>");

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
  CCAR-P MOCK TEST 3 — Practice Mode, AUTHOR mode, untargeted diagnostic (Papers 1 and 2 both
  generated but neither sat/scored at generation time -- confirmed with Ram before generating,
  per Outputs/CCAR-P_Paper-3-4-Generation-Prompt_v1.md §2).
  Generated 2026-08-31 from mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html per
  prep with quiz/CCAR-P-Orchestration-Prompt_v2.md. 63 items, all source:"AUTHORED".

  deepDive ships null on every item (orchestration prompt §5.5 correction, 2026-08-30) --
  populated later, only for items Ram actually misses, once the paper is scored (Phase 9).

  D2 note: Domain 2's decision-table facet supply is nearly exhausted after Papers 1-2 (18
  facets total, 16 already used). 6 of D2's 8 items on this paper draw on a section's
  Misconception block instead of a decision-table row, per Phase 4 rule 5 of the orchestration
  prompt -- expected, documented behaviour (GENERATION-INTELLIGENCE.md F-01), not a defect.

  Fidelity gate: node tools/run-gate.js mock-exams/CCAR-P_MockTest-3_v1.html 63 - see EXAM-LOG.md
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
  "const PAPER_N   = 3;"
);
src = src.replace('const KEY       = "ccarp-mocktest-template-v1";', 'const KEY       = "ccarp-mocktest-3-v1";');
// EXAM_MODE stays false -- no change needed (Paper 3 is not Paper 8 or 10)

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
    <h1>CCAR-P Mock Test 3</h1>
    <p class="sub">Claude Certified Architect – Professional · untargeted diagnostic</p>
  </header>

  <div class="demo-banner">
    <strong>Paper 3 — another untargeted diagnostic.</strong> 63 items generated from the CCAR-P
    corpus at the confirmed 17/13/19/16/14/14/7 weighting, one item for each of the 38 official
    objectives. Papers 1 and 2 were both generated but not yet sat when this paper was built, so
    no Professor's Note exists yet to target from — Ram confirmed generating another diagnostic
    rather than pausing to sit an existing paper first. Practice Mode, so feedback arrives per
    question.
  </div>

  <div class="facts">
    <div class="sf"><div class="k">Length</div><div class="v">63 items · 120 minutes</div></div>
    <div class="sf"><div class="k">Objectives covered</div><div class="v" id="fDemoCount">38 of 38</div></div>`;
if (!src.includes(oldLanding)) throw new Error("landing block not found verbatim");
src = src.replace(oldLanding, newLanding);

// --- 4b. Sticky top-nav brand text (missed on Papers 2 and, on the first pass, this build too --
// verified in-browser after the first build, per Paper 1's precedent at line 180 of MockTest-1) ---
src = src.replace(
  '<div class="brand">CCAR-P <span>Mock Test TEMPLATE</span></div>',
  '<div class="brand">CCAR-P <span>Mock Test 3</span></div>'
);

// --- 4c. fDemoCount JS override -- the template unconditionally sets this at runtime to
// "N demo items", overwriting whatever the static landing HTML says. Paper 1's fix (verified in its
// shipped file) computes distinct objectives covered instead. ---
src = src.replace(
  'document.getElementById("fDemoCount").textContent = ITEMS.length + " demo items";',
  'document.getElementById("fDemoCount").textContent = new Set(ITEMS.map(function(x){return x.objective;})).size + " of 38";'
);

// --- 5. ITEMS schema comment: drop "DEMO CONTENT" framing ---
const oldSchemaIntro = `/* ================= ITEMS =================
   DEMO CONTENT - four items written to the measured official style so the engine can be
   verified. Replace wholesale with 63 corpus-generated items.

   Schema, per CCAR-P-Orchestration-Prompt_v2.md 5.5:`;
const newSchemaIntro = `/* ================= ITEMS =================
   63 items, AUTHORED, Paper 3 -- generated per prep with quiz/_PAPER3-STAGING/plan.json.

   Schema, per CCAR-P-Orchestration-Prompt_v2.md 5.5:`;
if (!src.includes(oldSchemaIntro)) throw new Error("schema intro not found verbatim");
src = src.replace(oldSchemaIntro, newSchemaIntro);

// --- 6. Replace the ITEMS array itself ---
const marker = "const ITEMS = [";
const startAt = src.indexOf(marker);
if (startAt < 0) throw new Error("const ITEMS = [ not found");
// Find the matching close: the array is followed by a line "];" at top level. Locate the next
// occurrence of "\n];" after startAt.
const closeMarker = "\n];";
const closeAt = src.indexOf(closeMarker, startAt);
if (closeAt < 0) throw new Error("closing ]; not found");

const itemsJs = JSON.stringify(items, null, 1);
const newBlock = marker + "\n" + itemsJs.slice(1, -1).trim() + "\n];"; // strip JSON's outer [ ]

const before = src.slice(0, startAt);
const after = src.slice(closeAt + closeMarker.length);
src = before + newBlock + after;

fs.writeFileSync(OUT, src);
console.log("Wrote", OUT, "-", src.length, "bytes");
