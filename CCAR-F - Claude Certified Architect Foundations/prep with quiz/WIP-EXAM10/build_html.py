# -*- coding: utf-8 -*-
import json, re

BASE = "../mock-exams/CCA-Prep_MockTest-9_v1.html"
OUT = "../mock-exams/CCA-Prep_MockTest-10_v1.html"

html = open(BASE, encoding="utf-8").read()
data = json.load(open("exam10-verified.json", encoding="utf-8"))

# ---------- 1. Title ----------
html = html.replace(
    "<title>CCA-F Mock Test 9 · Foundations Practice</title>",
    "<title>CCA-F Mock Test 10 · Foundations Practice</title>",
)

# ---------- 2. Header comment block (lines 7-138, between <!-- and --> before <style>) ----------
stem_lines = []
for q in data["questions"]:
    stem_lines.append(f'  {q["g"]}. [{q["domain"]}] {q["stem"]}')
stems_block = "\n".join(stem_lines)

header_comment = f"""<!--
  CCA-Prep Mock Test 10 -- CCA-F Foundations
  Format: FULL-60 (4 scenario blocks x 15) | Generated 2026-07-28
  Generated from v2 corpus via orchestration-prompt v10 logic (per-option rationales,
  generic scenario framing, pre-planned balanced correct-answer letters, Fidelity
  Verification Gate, live running-accuracy percentage in the sticky nav).

  LEARNER SIGNAL THIS CYCLE: Exam 8 was scored 2026-07-28 (52/60, 880/1000
  scaled, results-JSON source) -- the first result to arrive since Exam 7. This
  is the Professor's Note -- Intent for Exam 10 (EXAM-LOG.md), Exam 10 being the
  first ungenerated paper able to consume it (Exam 9 was already generated
  2026-07-19, before Exam 8 was scored, correctly as a broad no-signal paper).

  Three of Exam 7's four flagged sections missed AGAIN on Exam 8's fresh
  re-test -- D3 3.1 (/memory diagnostic vs. re-typing the instruction), D3 3.6
  (direct execution vs. plan mode on a fully-scoped one-liner), and D4 4.6
  (forcing a specific tool via tool_choice vs. "any", which only guarantees
  SOME tool). D4 4.4 (prefilling) recovered. D3 and D4 tied weakest at 75.0%
  for the SECOND consecutive scored exam (Exam 7 also tied them, at 83.3%),
  both declining -- a genuine two-exam signal, not attempt-specific noise.
  Fresh sections were also missed (D3 3.11, D4 4.2, D4 4.9), so the gap is
  domain-wide breadth, not four narrow traps. A recurring over-engineering /
  symptom-patch reflex ran through about half the misses (reaching for a hook,
  a re-typed reminder, plan mode, or a half-split where the proportionate
  direct fix was correct).

  confirmed_weakness = false in the mechanical sense: the orchestration rule
  requires a SINGLE domain unambiguously weakest across two consecutive exams,
  and a two-domain tie has no single +4 target, so the quota-adjustment lever
  structurally cannot apply. This is NOT read as "no real weakness" -- the
  correct lever is the section-bias mechanism (Phase 4c.5), which targets
  WHICH sections are tested without changing HOW MANY questions per domain,
  and can therefore serve both D3 and D4 at once. Exam 10 therefore ships the
  BASE FULL-60 distribution (D1 16 / D2 11 / D3 12 / D4 12 / D5 9, unchanged)
  with D3's 12 and D4's 12 biased toward: (a) a THIRD re-test of D3 3.1, D3
  3.6, and D4 4.6 -- two attempts have now failed each, so this decides
  whether the gap is stubborn or slowly closing; (b) broad coverage of the
  rest of D3/D4 including the fresh misses 3.11, 4.2, 4.9; (c) a deliberate
  3-question "proportionate response vs. over-engineering" cluster in D3
  (Code Generation block, g16/g23/g27).

  Scenarios drawn (official bank of 6): Customer Support Resolution Agent;
  Code Generation with Claude Code; Multi-Agent Research System; Structured
  Data Extraction. All four were at count 5 (the four least-used) after Exam
  9's draw, so all four were eligible; Structured Data Extraction was the
  natural anchor (the only scenario not used in either of the last two exams),
  and Developer Productivity with Claude / Claude Code for Continuous
  Integration (count 6 each) were rested per the standing rotation guidance.
  The D4-carrier constraint (D4 is primary in only two scenarios) is satisfied
  by Structured Data Extraction's inclusion.

  Four scenario blocks authored SERIALLY (not in parallel) by delegated
  sub-agents this session, each against a centrally pre-planned block x domain
  allocation table (verified as a constraint-satisfaction problem before
  dispatch) and a pre-planned correct-answer-letter sequence per block
  (exam-wide exactly 15/15/15/15). Serial dispatch was a deliberate choice:
  the learner's weekly usage limit was near exhaustion this session, and
  finishing each block to disk before starting the next means a mid-generation
  interruption loses at most one block's work, never all four.

  COLLISION PRE-EMPTION. With the corpus fully saturated (every section Heavy
  since Exam 8), D2's 11 questions cannot cover its 9 assigned sections
  without two repeats. The two repeat sections were chosen up front (2.3,
  2.6) and each block was told explicitly which facet it owned AND which
  facet its sibling owned, with hard do-not-write-about constraints: D2 2.3
  split into business-error-vs-protocol-error semantics (Customer Support, g4)
  versus machine-readable structured-error content for retry-with-feedback
  (Structured Data Extraction, g49); D2 2.6 split into MCP primitive
  capability-category taxonomy -- tools vs. resources vs. prompts (Customer
  Support, g3) versus .mcp.json project scope vs. ~/.claude.json user scope
  for an experimental server (Multi-Agent Research, g32). Both splits were
  independently re-verified after assembly by reading all four full question
  texts side by side -- confirmed genuinely distinct lessons, not just
  distinct citations (the failure mode a citation-only tally cannot see, per
  Exam 9's own finding).

  Fidelity Verification Gate results (all Pass, computed programmatically):
  (1) invented names: 0 instances; (2) correct-answer tally: each block within
  1 of 4/4/4/3, exam-wide exactly 15/15/15/15; (3) word counts: stems min 36 /
  median 53 / max 69 (band 50-55, cap 95), options min 9 / max 27 (cap 35);
  (4) domain tally vs. primary domains: every block's primary-domain minimum
  exceeds its non-primary maximum, exam-wide quota exact (D1 16/D2 11/D3
  12/D4 12/D5 9); (5) inline code/config token rate: 64/240 = 26.7% (band
  20-25%, acceptable 15-30%); (6) scenario-rotation disclosure: present on the
  landing card below. Supplementary: full-exam Jaccard near-duplicate scan
  found ZERO pairs above a 0.30 threshold across all 60 stems; the D2
  citation-collision tally found exactly the two pre-declared, cross-block-
  content-verified-distinct repeats above and no unplanned repeats anywhere
  else (every other domain's assigned sections each used exactly once).

  Question stems (deduplication seed for future exams):
{stems_block}
-->"""

old_comment_match = re.search(r"<!--\n  CCA-Prep Mock Test 9.*?\n-->", html, re.S)
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
    <h3>Exam 10 · Generated 2026-07-28</h3>
    <p>This is a learning tool, not a timed simulator. There is no countdown — the timer just records your pace so you can see it later. Answers lock when you pick them, and the feedback appears immediately. Read every rationale, including on the questions you get right; the distractors are the traps the real exam uses.</p>
    <div class="start-facts">
      <div class="sf"><div class="k">Format</div><div class="v">60 questions · 4 blocks</div></div>
      <div class="sf"><div class="k">Domain weights (base)</div><div class="v">D1 16 · D2 11 · D3 12 · D4 12 · D5 9</div></div>
      <div class="sf"><div class="k">Last scored exam</div><div class="v">Exam 8: 52/60 (880/1000) · Exam 9 generated 2026-07-19, still unattempted</div></div>
      <div class="sf"><div class="k">Pass line</div><div class="v">720 / 1000 scaled</div></div>
    </div>
    <div class="sf" style="margin-top:12px;background:rgba(255,255,255,0.6)"><div class="k">Scenarios drawn (4 of the official 6)</div>
      <ul class="scen-list">
        <li>Customer Support Resolution Agent</li><li>Code Generation with Claude Code</li><li>Multi-Agent Research System</li><li>Structured Data Extraction</li>
      </ul>
      <p style="font-size:12px;color:var(--ink3);margin-top:8px;line-height:1.6;">These 4 were curated to guarantee coverage across your exams — the real exam draws 4 of 6 at random each sitting, with no such guarantee.</p>
    </div>
    <div class="sf" style="margin-top:12px;background:rgba(255,255,255,0.6)"><div class="k">Targeting this paper — D3/D4 section bias, base quota unchanged</div><div class="v" style="font-weight:400;font-size:13px;line-height:1.6;">Exam 8 scored 52/60 (880/1000): D3 and D4 tied weakest at 75.0% for the <strong>second consecutive scored exam</strong>, both declining, and three of Exam 7's four flagged sections (D3 §3.1, D3 §3.6, D4 §4.6) missed again. A two-domain tie has no single unambiguous weakest, so the mechanical +4/−2/−2 quota adjustment cannot apply — but this is a real, strengthening signal, not "no weakness." So Exam 10 keeps the <strong>base FULL-60 distribution</strong> (D1 16 · D2 11 · D3 12 · D4 12 · D5 9) and instead biases <em>which</em> D3/D4 sections are tested: a third re-test of D3 §3.1, D3 §3.6, and D4 §4.6 (two straight misses each — this decides whether the gap is stubborn or closing), broad coverage of the rest of D3/D4 including fresh misses §3.11/§4.2/§4.9, and a deliberate 3-question proportionate-response-vs-over-engineering cluster in D3.</div></div>
    <div class="start-actions"><button class="btn" onclick="goToQuestion(1)">Begin exam →</button></div>"""

html = html[: old_card_match.start()] + new_card + html[old_card_match.end() :]

# ---------- 4. KEY ----------
html = html.replace('const KEY = "cca-mock-9";', 'const KEY = "cca-mock-10";')

# ---------- 5. DATA block ----------
data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
old_data_match = re.search(r"const DATA = \{.*?\};\n", html, re.S)
assert old_data_match, "could not find DATA block"
html = html[: old_data_match.start()] + f"const DATA = {data_json};\n" + html[old_data_match.end() :]

# ---------- 6. Remaining "Mock Test 9" / "Exam 9" text mentions ----------
html = html.replace("Mock Test 9", "Mock Test 10")

open(OUT, "w", encoding="utf-8").write(html)
print("Wrote", OUT, "-", len(html), "bytes")
