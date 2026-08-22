# -*- coding: utf-8 -*-
import json, re

BASE = "../mock-exams/CCA-Prep_MockTest-10_v1.html"
OUT = "../mock-exams/CCA-Prep_MockTest-11_v1.html"

html = open(BASE, encoding="utf-8").read()
data = json.load(open("exam11-verified.json", encoding="utf-8"))

# ---------- 1. Title ----------
html = html.replace(
    "<title>CCA-F Mock Test 10 · Foundations Practice</title>",
    "<title>CCA-F Mock Test 11 · Foundations Practice</title>",
)

# ---------- 2. Header comment block ----------
stem_lines = []
for q in data["questions"]:
    stem_lines.append(f'  {q["g"]}. [{q["domain"]}] {q["stem"]}')
stems_block = "\n".join(stem_lines)

header_comment = f"""<!--
  CCA-Prep Mock Test 11 -- CCA-F Foundations
  Format: FULL-60 (4 scenario blocks x 15) | Generated 2026-07-29
  Generated from v2 corpus via orchestration-prompt v10 logic (per-option rationales,
  generic scenario framing, pre-planned balanced correct-answer letters, Fidelity
  Verification Gate, live running-accuracy percentage in the sticky nav).

  LEARNER SIGNAL THIS CYCLE: Exam 10 was scored 2026-07-29 (54/60, 910/1000
  scaled, results-JSON source). The Professor's Note -- Intent for Exam 11
  (EXAM-LOG.md) and Insights Round 2 (fired the same session, exams_scored
  reaching 6) are both consumed here. D3 §3.1 and §3.6 both RECOVERED in
  Exam 10 after missing twice each -- a closed chapter, tested only for
  routine periodic confirmation this exam. D4 §4.6 missed a THIRD straight
  time (Exam 7, 8, 10) -- confirmed stubborn per Insights Round 2's Focus
  Recommendation, re-tested here a FOURTH time with a genuinely new
  mechanism (the reverse direction: a scenario where "any" is actually
  correct, to check whether the learner over-generalized "always force
  specific" from the last two misses). D3 §3.11 missed a SECOND time
  (fresh miss Exam 8, re-test miss Exam 10) -- re-tested here a second
  formal time via a category-mismatch facet (path-scoped content wrongly
  bundled into a Skill), distinct from both priors' half-split framing.
  D2 showed a genuine 3-exam declining trend (100% -> 90.9% -> 81.8%,
  Exam 7/8/10) that no single-exam Professor's Note had caught in
  isolation -- Insights Round 2's secondary focus. Base FULL-60 quota kept
  unchanged (D2's decline is real but was only a single exam as sole-
  weakest, not yet meeting the two-consecutive-exam confirmed-weakness
  bar); D2 instead gets its fullest-ever breadth this exam, spread across
  two independently-authored blocks (Customer Support 5, Developer
  Productivity 6) covering all 9 D2 sections.

  Scenario draw (official bank of 6): Customer Support Resolution Agent;
  Developer Productivity with Claude; Claude Code for Continuous
  Integration; Structured Data Extraction. This is the FIRST exam with no
  rotation-based tiebreaker -- all six scenarios were tied at count 6 after
  Exam 10. Code Generation with Claude Code and Multi-Agent Research
  System were deliberately rested: both had been drawn in BOTH Exam 9 and
  Exam 10 (a two-exam-running streak), the highest convergence risk in the
  pool per this project's own "Weak Patterns" precedent (a scenario's
  self-QA needing heavy rewriting once it reaches its 4th+ use in close
  succession). The four scenarios drawn instead give every domain exactly
  two primary-carrying blocks (D1: Customer Support + Developer
  Productivity; D2: Customer Support + Developer Productivity; D3:
  Developer Productivity + Claude Code CI; D4: Claude Code CI + Structured
  Data Extraction; D5: Customer Support + Structured Data Extraction) --
  the most structurally balanced draw this project has produced, directly
  serving both this exam's real priorities (D2 breadth, D4/§4.6 no longer
  concentrated in a single block).

  Four scenario blocks authored in PARALLEL by delegated sub-agents this
  session (no usage-limit risk was flagged, so the standard 4.b.6/4.b.7
  pattern was used rather than Exam 10's serial fallback), each against a
  centrally pre-planned block x domain allocation table and a pre-planned
  correct-answer-letter sequence per block (exam-wide exactly 15/15/15/15).

  A REAL CONTENT COLLISION WAS FOUND AND FIXED THIS SESSION -- the first
  time the manual cross-block content read (not the automated citation
  tally or Jaccard scan) caught something on the FIRST post-assembly pass
  rather than after a prior exam had already shipped it. D2's 11 questions
  over 9 sections forced two repeats; both were originally drafted by
  independently-dispatched blocks reskinning the IDENTICAL underlying
  lesson with different tool names (§2.3's business-rule-denial facet
  tested twice; §2.8's only teachable lesson -- the section is ~4 lines of
  corpus content with no second facet available -- tested twice). Neither
  the citation tally nor a 0.30-threshold Jaccard scan flagged either
  pair. Fixed directly: one §2.3 question was rewritten onto the corpus's
  distinct "valid empty results vs. access failure" facet; the §2.8 repeat
  was reassigned entirely to §2.6 (MCP primitive taxonomy, a facet
  distinct from this exam's other §2.6 question), since §2.8 has no second
  facet to offer. The D2 repeat pair is therefore {{§2.3, §2.6}}, not the
  originally-planned {{§2.3, §2.8}} -- a valid substitution, since the
  requirement is two genuinely distinct facets among D2's repeats, not any
  specific two sections.

  Fidelity Verification Gate results (all Pass, computed programmatically,
  re-run after the collision fix above): (1) invented names: 0 instances;
  (2) correct-answer tally: each block within 1 of 4/4/4/3, exam-wide
  exactly 15/15/15/15; (3) word counts: stems min 43 / median 54 / max 67
  (band 50-55, cap 95), options min 8 / max 33 (cap 35); (4) domain tally
  vs. primary domains: every block's primary-domain minimum exceeds its
  non-primary maximum, exam-wide quota exact (D1 16/D2 11/D3 12/D4 12/D5
  9); (5) inline code/config token rate: 56/240 = 23.3% (band 20-25%);
  (6) scenario-rotation disclosure: present on the landing card below.
  Supplementary: full-exam Jaccard near-duplicate scan found ZERO pairs
  above a 0.30 threshold across all 60 stems, both before and after the
  collision fix (the collision was invisible to this check, as expected --
  it was a same-lesson-different-vocabulary case, not a lexical
  near-duplicate).

  KD budget note: 8 Key Distinctions seeded (#4, #12, #15, #19, #20, #21,
  #25, #27) -- above the Session 13 tightening target of 4-6 (each of the
  four independently-dispatched blocks stayed within its own 1-2 KD
  instruction, but 4 blocks x 2 sums above the intended exam-wide
  ceiling). Still comfortably within the hard 15-question cap; every seed
  is a genuine natural fit, none forced.

  Question stems (deduplication seed for future exams):
{stems_block}
-->"""

old_comment_match = re.search(r"<!--\n  CCA-Prep Mock Test 10.*?\n-->", html, re.S)
assert old_comment_match, "could not find header comment block to replace"
html = html[: old_comment_match.start()] + header_comment + html[old_comment_match.end() :]

# ---------- 3. Landing card ----------
old_card_match = re.search(
    r'<div class="start-card" id="startCard">.*?<div class="start-actions"><button class="btn" onclick="goToQuestion\(1\)">Begin exam →</button></div>',
    html,
    re.S,
)
assert old_card_match, "could not find landing card"

new_card = """<div class="start-card" id="startCard">
    <div class="kicker">Before you begin</div>
    <h3>Exam 11 · Generated 2026-07-29</h3>
    <p>This is a learning tool, not a timed simulator. There is no countdown — the timer just records your pace so you can see it later. Answers lock when you pick them, and the feedback appears immediately. Read every rationale, including on the questions you get right; the distractors are the traps the real exam uses.</p>
    <div class="start-facts">
      <div class="sf"><div class="k">Format</div><div class="v">60 questions · 4 blocks</div></div>
      <div class="sf"><div class="k">Domain weights (base)</div><div class="v">D1 16 · D2 11 · D3 12 · D4 12 · D5 9</div></div>
      <div class="sf"><div class="k">Last scored exam</div><div class="v">Exam 10: 54/60 (910/1000) · Exam 9 generated 2026-07-19, still unattempted</div></div>
      <div class="sf"><div class="k">Pass line</div><div class="v">720 / 1000 scaled</div></div>
    </div>
    <div class="sf" style="margin-top:12px;background:rgba(255,255,255,0.6)"><div class="k">Scenarios drawn (4 of the official 6)</div>
      <ul class="scen-list">
        <li>Customer Support Resolution Agent</li><li>Developer Productivity with Claude</li><li>Claude Code for Continuous Integration</li><li>Structured Data Extraction</li>
      </ul>
      <p style="font-size:12px;color:var(--ink3);margin-top:8px;line-height:1.6;">These 4 were curated to guarantee coverage across your exams — the real exam draws 4 of 6 at random each sitting, with no such guarantee.</p>
    </div>
    <div class="sf" style="margin-top:12px;background:rgba(255,255,255,0.6)"><div class="k">Targeting this paper — a stubborn trap re-tested a 4th time, plus D2 breadth</div><div class="v" style="font-weight:400;font-size:13px;line-height:1.6;">Exam 10 scored 54/60 (910/1000): D3 §3.1 and §3.6 both <strong>recovered</strong> after missing twice each — a closed chapter, touched only for routine confirmation here. D4 §4.6 (<code>tool_choice</code> forcing a specific tool vs. <code>"any"</code>) missed a <strong>third consecutive time</strong> (Exam 7, 8, 10) — confirmed stubborn, re-tested a fourth time with a genuinely new mechanism. D3 §3.11 (CLAUDE.md/Skills organization) missed a second time — re-tested formally again. D2 showed a real 3-exam decline (100% → 90.9% → 81.8%) that only a 3-exam Insights Round could see — so this paper keeps the <strong>base FULL-60 distribution</strong> unchanged and instead gives D2 its fullest-ever breadth, spread across two blocks covering all 9 of its sections.</div></div>
    <div class="start-actions"><button class="btn" onclick="goToQuestion(1)">Begin exam →</button></div>"""

html = html[: old_card_match.start()] + new_card + html[old_card_match.end() :]

# ---------- 4. KEY ----------
html = html.replace('const KEY = "cca-mock-10";', 'const KEY = "cca-mock-11";')

# ---------- 5. DATA block ----------
data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
old_data_match = re.search(r"const DATA = \{.*?\};\n", html, re.S)
assert old_data_match, "could not find DATA block"
html = html[: old_data_match.start()] + f"const DATA = {data_json};\n" + html[old_data_match.end() :]

# ---------- 6. Remaining "Mock Test 10" text mentions ----------
html = html.replace("Mock Test 10", "Mock Test 11")

open(OUT, "w", encoding="utf-8").write(html)
print("Wrote", OUT, "-", len(html), "bytes")
