import json, os, re, sys, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "mock-exams", "CCA-Prep_MockTest-16_v1.html")

# PRE-FLIGHT: never overwrite a numbered artifact by accident. --force is only for
# rebuilding this session's own in-progress output after a template edit.
if os.path.exists(OUT) and "--force" not in sys.argv:
    sys.exit(f"REFUSING TO OVERWRITE: {OUT} already exists. Increment the version, or pass --force to rebuild.")

DATA = json.load(open(os.path.join(HERE, "exam16-data.json"), encoding="utf-8"))
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


prim = {
    "Customer Support Resolution Agent": "primary D1, D2, D5",
    "Multi-Agent Research System": "primary D1, D2, D5",
    "Developer Productivity with Claude": "primary D2, D3, D1",
    "Claude Code for Continuous Integration": "primary D3, D4",
}

lines = [
    "  CCA-Prep Mock Test 16 -- CCA-F Foundations",
    "  Format: FULL-60 (4 scenario blocks x 15 = 60 questions)",
    "  Generated: 2026-08-11 via CCA-Orchestration-Prompt_v10.md + QUESTION-ARCHETYPE-BANLIST.md",
    "",
    "  SCENARIOS DRAWN (4 of the official 6):",
]
for i, b in enumerate(DATA["blocks"], 1):
    lines.append(f"    {i}. {b['label']:<45s}({prim.get(b['label'],'')})")
lines += [
    "  Rested here: Code Generation with Claude Code, Structured Data Extraction -- both drawn by Exam 15.",
    "  Counts before this paper: Structured Data Extraction 10, Developer Productivity 10, the other four 9.",
    "  Selection: of the 15 possible 4-of-6 draws, 10 were already used across Exams 2-15 and one more",
    "  (Code Generation + Customer Support + Developer Productivity + Multi-Agent Research) is INFEASIBLE",
    "  at this quota because it contains no D4-primary block. Of the four unused feasible draws, this is",
    "  the only one in which no block has to absorb more than 5 questions of any single domain -- solved",
    "  as a constraint problem over all 15 draws, not chosen by hand.",
    "",
    "  DOMAIN QUOTA (base weights -- no confirmed-weakness adjustment applies):",
    "    D1 16 | D2 11 | D3 12 | D4 12 | D5 9 = 60",
    "  Driver: the two most recent scored papers named different weakest domains by attempt chronology",
    "  (Exam 9: D2, attempted 2026-08-09; Exam 11: D5, attempted 2026-08-10), so nothing is confirmed.",
    "",
    "  BLOCK x DOMAIN ALLOCATION (primary domains in brackets):",
    "    1. Customer Support        [D1 D2 D5]  D1 5 / D2 3 / D3 2 / D4 2 / D5 3",
    "    2. Multi-Agent Research    [D1 D2 D5]  D1 4 / D2 3 / D3 2 / D4 2 / D5 4",
    "    3. Developer Productivity  [D2 D3 D1]  D1 4 / D2 4 / D3 4 / D4 3 / D5 0",
    "    4. Claude Code for CI      [D3 D4]     D1 3 / D2 1 / D3 4 / D4 5 / D5 2",
    "  Flattest allocation the bank allows: max cell 5, versus 12 in Exam 15's extraction block.",
    "",
    "  ITEM FORMATS: 47 single-answer (4 options) + 13 multiple-response.",
    "    9 x select-2-of-5, 4 x select-3-of-6, scored all-or-nothing. Same share as Exams 14 and 15.",
    "",
    "  CORRECT-ANSWER LETTER PRE-PLAN (single-answer items, fixed before options were drafted):",
    "    block 1 BDACDBACBDCA   block 2 CADBACBDABDC",
    "    block 3 DBCABDCADCAB   block 4 CDBCADBDCBA (short A)",
    "    Exam-wide A11 B12 C12 D12 = 47. Achieved sequences match the pre-plan exactly.",
    "",
    "  PROFESSOR'S NOTE CONSUMED (Intent for Exam 13, written after Exam 11 scored 55/60):",
    "    D2 SS2.8 composite vs prompt-bundling  -> Q38, rebuilt as a select-3 starting from a team that",
    "      already built the composite and is now paying a second-order cost (ban-list BF-2 re-frame).",
    "    D1 SS1.18 evaluator-optimizer vs context isolation -> Q59, a direct two-pattern disambiguation.",
    "    D5 SS5.8 over-escalation of a resolvable ambiguity -> Q3, with escalate-immediately as a distractor.",
    "",
    "  FRESH-SECTION COVERAGE: all four D3 SS3.7 subsections (the least-used sections in the corpus at",
    "    2-3 prior uses each) appear -- SS3.7.1 Q32, SS3.7.2 Q49, SS3.7.3 Q36, SS3.7.4 Q57.",
    "    58 distinct corpus sections carry the whyRight citation; only D2 SS2.3 and SS2.9 appear twice,",
    "    which is forced (D2 has 9 sections and an 11-question quota) and each pair tests a different facet.",
    "",
    "  ARCHETYPE BAN-LIST APPLIED (see QUESTION-ARCHETYPE-BANLIST.md):",
    "    All nine banned reskin families avoided; their corpus points re-tested from approved angles.",
    "    Verified by tools/archetype_gate.py against 893 prior stems (Exams 2-15): all 7 gates pass --",
    "    0 invented names; SA letters A11 B12 C12 D12; stems 43/54/62 with option max 25;",
    "    block primacy holds in all four blocks; inline token rate 20.6%; 13 well-formed MR items;",
    "    0 archetype collisions vs priors and 0 intra-paper.",
    "",
    "  QUESTIONS USED (deduplication ledger for Exam 17+):",
]
for q in DATA["questions"]:
    tag = f"[{q['domain']}]" + (f"[select-{q['selectN']}]" if q.get("selectN") else "")
    body = f"{q['g']}. {tag} {plain(q['stem'])}"
    lines += textwrap.wrap(body, width=120, initial_indent="  ", subsequent_indent="     ")

header = "\n".join(lines).replace("-->", "- ->")  # never let the ledger close the comment early

html = tpl.replace("__HEADER_COMMENT__", "\n" + header + "\n")
html = html.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(html)

print(f"wrote {OUT}")
print(f"  size: {os.path.getsize(OUT)/1024:.1f} KB")
print(f"  placeholders remaining: {html.count('__DATA__') + html.count('__HEADER_COMMENT__')}")
