#!/usr/bin/env python3
"""Assemble CCA-Prep_MockTest-20_v1.html from the Exam 19 (Exam-Mode) template."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MOCK_EXAMS = os.path.dirname(HERE)
TEMPLATE = os.path.join(MOCK_EXAMS, "CCA-Prep_MockTest-19_v1.html")
OUT = os.path.join(MOCK_EXAMS, "CCA-Prep_MockTest-20_v1.html")
COMBINED = os.path.join(HERE, "combined.json")

with open(COMBINED, encoding="utf-8") as f:
    data = json.load(f)

QUOTA = {"D1": 16, "D2": 11, "D3": 12, "D4": 12, "D5": 9}
DOMAIN_NAMES = {
    "D1": "Agentic Architecture & Orchestration",
    "D2": "Tool Design & MCP Integration",
    "D3": "Claude Code Configuration & Workflows",
    "D4": "Prompt Engineering & Structured Output",
    "D5": "Context Management & Reliability",
}

data["exam_n"] = 20
data["format"] = "FULL60"
data["generated"] = "2026-08-16"
data["quota"] = QUOTA
data["domainNames"] = DOMAIN_NAMES

DATA_JSON = json.dumps(data, ensure_ascii=False)

with open(TEMPLATE, encoding="utf-8") as f:
    html = f.read()

orig_len = len(html)


def sub_once(pattern, replacement, text, flags=0, label=""):
    matches = list(re.finditer(pattern, text, flags))
    assert len(matches) == 1, f"anchor {label!r} matched {len(matches)} times, expected 1"
    m = matches[0]
    return text[: m.start()] + replacement + text[m.end() :]


# 1. title
html = sub_once(
    re.escape("<title>CCA-F Mock Test 19 · Foundations Practice</title>"),
    "<title>CCA-F Mock Test 20 · Foundations Practice</title>",
    html,
    label="title",
)

# 2. h1
html = sub_once(
    re.escape("<h1>Mock Test <em>19</em></h1>"),
    "<h1>Mock Test <em>20</em></h1>",
    html,
    label="h1",
)

# 3. top JS/HTML comment block (lines 7-299 in the template: from "<!--\n  CCA-Prep Mock Test 19"
#    through the closing "-->" right before "<script>" ... actually before "<html" body; it's the
#    block right after <html><head>... no -- it's the very first comment in the file, right after <html lang="en">.
with open(os.path.join(HERE, "stem_ledger.txt"), encoding="utf-8") as f:
    stem_ledger = f.read().rstrip("\n")

block_lines = []
for b in data["blocks"]:
    tally = {}
    for q in data["questions"]:
        pass
for i, b in enumerate(data["blocks"]):
    dom_tally = {}
    for q in data["questions"]:
        if q["block"] == i:
            dom_tally[q["domain"]] = dom_tally.get(q["domain"], 0) + 1
    tally_str = " / ".join(f"{d} {dom_tally.get(d,0)}" for d in ["D1", "D2", "D3", "D4", "D5"])
    block_lines.append(f"    {i+1}. {b['label']:<38} {tally_str}")

letter_plans = {
    "Multi-Agent Research System": "C A B C A C B A B D D D A",
    "Developer Productivity with Claude": "C C B A B B B A C D D A D",
    "Structured Data Extraction": "C D A D D B C B C A B C A",
    "Claude Code for Continuous Integration": "C B B A D A C D C A B D D",
}
letter_lines = [f"    {b['label']}: {letter_plans[b['label']]}" for b in data["blocks"]]

comment = f"""<!--
  CCA-Prep Mock Test 20 -- CCA-F Foundations
  Format: FULL-60 (4 scenario blocks x 15 = 60 questions)
  Generated: 2026-08-16, immediately after Exam 19 was scored (56/60, 940) the same session.
  Mode: EXAM MODE (see EXAM-MODE-DESIGN_v1.md) -- no per-question feedback, 120:00 countdown,
  full results/rationale review only after the final question. Same variant as Exam 19.

  GENERATION METHOD: 4 parallel scenario-block sub-agents dispatched by a coordinating session,
  per CCA-Orchestration-Prompt_v10.md Phase 4.b.6. All four sub-agents stalled simultaneously on
  first dispatch (a documented infrastructure failure mode -- see GENERATION-INTELLIGENCE.md
  Session 7/9 for the same pattern on Exams 7 and 8) and were resumed, not restarted; all four
  completed cleanly on resume with no rework.

  FULL HISTORICAL REVIEW PRECEDED GENERATION (at the user's explicit request). This surfaced two
  things no single-exam Professor's Note had caught:
    1. Insights Round 4 was due 2026-08-15 (exams_scored hit 12 after Exam 14) and never ran --
       run retroactively this session, window Exam 13 -> Exam 17 -> Exam 14. See EXAM-LOG.md.
    2. Exam 19's own confirmed-weakness check (logged the same session, before this review) had
       compared against the wrong prior exam (Exam 17 instead of Exam 14, the true immediate
       predecessor by attempt date) -- corrected in EXAM-LOG.md. The correction surfaced a real,
       accidental finding: D3 was confirmed weak Exam 17->14 (75%->67%, the `.claude/rules/`
       default-reach reflex, six instances total) and then recovered cleanly to 12/12 on Exam 19,
       untargeted.

  SCENARIOS DRAWN (4 of the official 6):
{chr(10).join(f"    {i+1}. {b['label']}" for i, b in enumerate(data['blocks']))}
  Rested: Customer Support Resolution Agent, Code Generation with Claude Code.
  Rotation counts entering this exam: Claude Code CI 13, Structured Data Extraction 13 (tied
  most-used) / Customer Support 12, Developer Productivity 12 / Code Generation 11, Multi-Agent
  Research 11 (tied least-used). Rotation preference would rest both CI and SDE (most-used), but
  D4's quota (12, >0) needs a primary-carrying block and no domain with quota >15 can be carried
  by fewer than ceil(quota/15) primary blocks -- D1 (16) needs >=2 D1-primary blocks, which only
  Multi-Agent Research and Developer Productivity supply among the 6. Deliberately drew BOTH D4
  carriers (Structured Data Extraction + Claude Code CI) despite their higher usage, precedented
  by Exam 11 doing the same for the same reason (a D4 trap needing a fresh, uncrowded block) --
  this gives D4's two targeted sections (see below) genuine both-directions spread across two
  blocks instead of forcing both into one. Cost: Code Generation stays at 11 (still least-used),
  a natural anchor for Exam 21.

  DOMAIN QUOTA (base weights -- no confirmed-weakness adjustment; no domain is confirmed weak
  against its true immediate predecessor as of Exam 19):
    D1 16 | D2 11 | D3 12 | D4 12 | D5 9 = 60

  BLOCK x DOMAIN ALLOCATION (every primary domain outnumbers every non-primary domain in its own
  block, verified by tools/archetype_gate.py check 4):
{chr(10).join(block_lines)}

  CORRECT-ANSWER LETTER PRE-PLAN (13 single-answer questions per block; 2 multi-response items
  per block at local positions 6 and 12 are exempt). Fixed before any option was drafted:
{chr(10).join(letter_lines)}
  Exam-wide achieved tally (tools/archetype_gate.py check 2): A=13 B=13 C=13 D=13 -- exact.

  ITEM FORMATS: 52 single-answer (4 options) + 8 multiple-response (2 per block, select-2-of-4).

  PROFESSOR'S NOTE CONSUMED -- reconciled from TWO chains this session (see EXAM-LOG.md
  "Insights Round 4" finding 6 for the full reconciliation):
    1. TOP PRIORITY -- D2 SS2.8 (composite tool vs. prompt bundling), the single oldest
       unresolved misconception in the corpus: missed on Exams 5, 8, 10, 11, 14 (five times).
       Tested from BOTH directions across two different blocks: Multi-Agent Research Q7/Q12
       (composite justified vs. corpus's own preference baited as a distractor) and Developer
       Productivity Q21 (the opposite polarity -- bundling correct, composite would over-fetch).
    2. D4 SS4.5 (prevention vs. after-the-fact repair) -- confirmed on 2 different surfaces
       (Exam 17 hooks, Exam 19 schema typing). Three genuinely distinct facets in Structured
       Data Extraction: Q32 (numeric precision), Q38 (retry-loop-into-enum), Q41 (nullable
       fields) -- none touching Exam 19 Q58's date-format territory.
    3. D4 SS4.6 (`tool_choice` over-specification direction) -- 1 miss so far (Exam 19 Q23).
       Three distinct CI situations in Claude Code CI: Q48, Q53, Q60, each varying which
       over-specified setting is offered and which pipeline step is at issue.
    4. D2 SS2.1/SS2.2 (parameter description vs. worked examples) -- 1 miss (Exam 19 Q53).
       Note: the original Professor's Note mislabeled this SS2.1; the actual corpus grounding is
       SS2.2 (Tool Description Design) -- corrected during Block 1 authoring, see EXAM-LOG.md.
       One test: Multi-Agent Research Q10.
    5. D3 SS3.1/SS3.8 (`.claude/rules/`-as-default-reach) -- ONE confirmatory item only, per the
       D3 recovery finding above (not a domain-wide push). Claude Code CI Q52, a single-guidance-
       item trap distinct in shape from Exam 14's Q18 (diagnostic, /memory-first) and Q38
       (context-supply, multi-item).

  FIDELITY VERIFICATION GATE (tools/archetype_gate.py, all 7 checks -- ALL PASS):
    1. No invented names: 0 flagged (2 false-positive flags on sentence-initial common words
       "Despite"/"Authors" fixed by rewording, not by widening the allow-list).
    2. Correct-answer letter tally: exact 13/13/13/13 exam-wide.
    3. Word counts: stem min/median/max 40/55/78 (within the 50-55 median band, cap 95); option
       max 35 (at cap). Eleven stems trimmed for verbosity (content/facts/citations unchanged)
       to pull the exam-wide median from 59 down to 55.
    4. Block vs. primary domains: all four blocks pass with real margins.
    5. Inline code/config token rate: 70/240 = 29.2% (within the 15-30% acceptable band, upper
       half of it).
    6. Multiple-response validity: all 8 items well-formed.
    7. Archetype collision: 0 collisions against 1,133 prior stems (Exams 2-19 + the 76 locked
       community practice-test stems), 0 intra-paper duplicates, no closing/opening formula over
       its cap. Each of the four block sub-agents independently caught and rewrote several of its
       own near-collisions against specific prior exams before returning (see EXAM-LOG.md).

  QUESTIONS USED (deduplication ledger for Exam 21+):
{stem_ledger}
-->"""

pattern = r"<!--\n  CCA-Prep Mock Test 19.*?\n-->"
matches = list(re.finditer(pattern, html, re.DOTALL))
assert len(matches) == 1, f"comment-block anchor matched {len(matches)} times"
m = matches[0]
html = html[: m.start()] + comment + html[m.end() :]

# 4. KEY
html = sub_once(
    re.escape('const KEY = "cca-mock-19";'),
    'const KEY = "cca-mock-20";',
    html,
    label="KEY",
)

# 5. landing card
old_card = r"""    <h3>Exam 19 · Generated 2026-08-14 · the guarantee-strength paper</h3>
    <p>Built from the Professor's Note written after Exam 17.*?</p>
    <div class="start-facts">
      <div class="sf"><div class="k">Format</div><div class="v">60 questions · 4 blocks · 52 single-answer \+ 8 multiple-response</div></div>
      <div class="sf"><div class="k">Domain quota \(base weights\)</div><div class="v">D1 16 · D2 11 · D3 12 · D4 12 · D5 9</div></div>
      <div class="sf"><div class="k">Last scored exam</div><div class="v">Exam 17: 51/60 \(865\), attempted 2026-08-14 — nine misses, all targeted here</div></div>
      <div class="sf"><div class="k">Pass line</div><div class="v">720 / 1000 scaled</div></div>
      <div class="sf" style="border-color:var\(--coral\)"><div class="k">⏱ Exam Mode</div><div class="v">No per-question feedback — explanations and scoring arrive only after you finish, with a 120:00 countdown\. Matches real exam conditions for this final pre-exam sitting\.</div></div>
    </div>
    <div class="sf flag" style="margin-top:12px"><div class="k">Multiple-response items</div><div class="v" style="font-weight:400;font-size:13px;line-height:1\.6;">Eight items here are multiple-response.*?</div></div>
    <div class="sf" style="margin-top:12px;background:rgba\(255,255,255,0\.6\)"><div class="k">Scenarios drawn \(4 of the official 6\)</div>
      <ul class="scen-list"><li>Customer Support Resolution Agent</li><li>Code Generation with Claude Code</li><li>Claude Code for Continuous Integration</li><li>Structured Data Extraction</li></ul>
      <p style="font-size:12px;color:var\(--ink3\);margin-top:8px;line-height:1\.6;">These 4 were curated to guarantee coverage across your exams — the real exam draws 4 of 6 at random each sitting, with no such guarantee\.</p>
    </div>
    <div class="sf" style="margin-top:12px;background:rgba\(255,255,255,0\.6\)"><div class="k">How this paper was targeted</div><div class="v" style="font-weight:400;font-size:13px;line-height:1\.6;">Base weighting again.*?</div></div>"""

scen_items = "".join(f"<li>{b['label']}</li>" for b in data["blocks"])

new_card = f'''    <h3>Exam 20 · Generated 2026-08-16 · the reconciliation paper</h3>
    <p>Built the same session Exam 19 was scored (56/60, 940), after a full historical review Ram asked for. That review found an overdue Insights Round (due 2026-08-15, never run) and a chronology error in Exam 19's own confirmed-weakness check -- both fixed in EXAM-LOG.md before this paper was planned. Five priorities came out of the reconciliation: D2 &sect;2.8 composite-vs-bundling (the corpus's oldest unresolved trap, five misses running), D4 &sect;4.5 prevention-vs-repair and &sect;4.6 tool_choice over-specification (both confirmed on Exam 17/19), D2 &sect;2.2 parameter descriptions, and one confirmatory item on the D3 &lsquo;.claude/rules/&rsquo; reflex that recovered cleanly on Exam 19 but has a six-instance history.</p>
    <div class="start-facts">
      <div class="sf"><div class="k">Format</div><div class="v">60 questions · 4 blocks · 52 single-answer + 8 multiple-response</div></div>
      <div class="sf"><div class="k">Domain quota (base weights)</div><div class="v">D1 16 · D2 11 · D3 12 · D4 12 · D5 9</div></div>
      <div class="sf"><div class="k">Last scored exam</div><div class="v">Exam 19: 56/60 (940), attempted 2026-08-16 — highest score on record, first sitting under Exam Mode</div></div>
      <div class="sf"><div class="k">Pass line</div><div class="v">720 / 1000 scaled</div></div>
      <div class="sf" style="border-color:var(--coral)"><div class="k">⏱ Exam Mode</div><div class="v">No per-question feedback — explanations and scoring arrive only after you finish, with a 120:00 countdown. Matches real exam conditions for this final pre-exam sitting.</div></div>
    </div>
    <div class="sf flag" style="margin-top:12px"><div class="k">Multiple-response items</div><div class="v" style="font-weight:400;font-size:13px;line-height:1.6;">Eight items here are multiple-response, two per block, each asking for two of four options and scored all-or-nothing. Every one states its count in the stem and shows a &ldquo;Select N&rdquo; banner. The official guide names the format in its specification table and demonstrates it in none of its twelve samples, so treat the count as the thing to read first — the common way to lose these is answering the right idea with the wrong number of picks.</div></div>
    <div class="sf" style="margin-top:12px;background:rgba(255,255,255,0.6)"><div class="k">Scenarios drawn (4 of the official 6)</div>
      <ul class="scen-list">{scen_items}</ul>
      <p style="font-size:12px;color:var(--ink3);margin-top:8px;line-height:1.6;">These 4 were curated to guarantee coverage across your exams — the real exam draws 4 of 6 at random each sitting, with no such guarantee.</p>
    </div>
    <div class="sf" style="margin-top:12px;background:rgba(255,255,255,0.6)"><div class="k">How this paper was targeted</div><div class="v" style="font-weight:400;font-size:13px;line-height:1.6;">Base weighting — no domain is confirmed weak against its true immediate predecessor. Draws both D4-carrier scenarios (Structured Data Extraction, Claude Code CI) deliberately, despite both being the most-used pair, so the two D4 priorities above get real both-directions spread across two blocks instead of crowding one. Rests Customer Support and Code Generation, both least-pressing right now. Every priority section is tested by a genuinely fresh situation, verified against the specific prior questions it must not resemble (Exam 17/19's misses, Exam 14's rules-reflex instances) before this paper shipped.</div></div>'''

matches = list(re.finditer(old_card, html, re.DOTALL))
assert len(matches) == 1, f"landing-card anchor matched {len(matches)} times"
m = matches[0]
html = html[: m.start()] + new_card + html[m.end() :]

# 6. DATA object (the giant single-line const DATA = {...};)
m_start = re.search(r"const DATA = \{", html)
assert m_start, "DATA start anchor not found"
start = m_start.start()
# find matching closing brace for the object literal, then the following ';'
depth = 0
instr = False
esc = False
i = m_start.end() - 1  # position of the opening '{'
end = None
for j in range(i, len(html)):
    c = html[j]
    if instr:
        if esc:
            esc = False
        elif c == "\\":
            esc = True
        elif c == '"':
            instr = False
        continue
    if c == '"':
        instr = True
    elif c == "{":
        depth += 1
    elif c == "}":
        depth -= 1
        if depth == 0:
            end = j + 1
            break
assert end is not None, "could not find matching close brace for DATA"
assert html[end] == ";", f"expected ';' after DATA object, found {html[end]!r}"
end += 1
html = html[:start] + "const DATA = " + DATA_JSON + ";" + html[end:]

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"wrote {OUT}  ({len(html)} bytes, template was {orig_len} bytes)")

# post-build regression check (PB-20 discipline): no stray literal "19" that should be "20"
stray = []
for pat in [r'"cca-mock-19"', r"Mock Test 19\b", r"\bExam 19 · Generated"]:
    for mm in re.finditer(pat, html):
        stray.append((pat, mm.start()))
print("stray-19 scan:", stray if stray else "clean")
