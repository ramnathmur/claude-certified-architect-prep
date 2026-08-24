import json, os, re, sys, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXAM_N = 18
OUT = os.path.join(ROOT, "mock-exams", f"CCA-Prep_MockTest-{EXAM_N}_v1.html")

# PRE-FLIGHT: never overwrite a numbered artifact by accident.
if os.path.exists(OUT) and "--force" not in sys.argv:
    sys.exit(f"REFUSING TO OVERWRITE: {OUT} already exists. Increment the version, or pass --force to rebuild.")

DATA = json.load(open(os.path.join(HERE, f"exam{EXAM_N}-data.json"), encoding="utf-8"))
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


prim = {
    "Code Generation with Claude Code": "primary D3, D5",
    "Developer Productivity with Claude": "primary D2, D3, D1",
    "Claude Code for Continuous Integration": "primary D3, D4",
    "Structured Data Extraction": "primary D4, D5",
}

lines = [
    f"  CCA-Prep Mock Test {EXAM_N} -- CCA-F Foundations",
    "  Format: FULL-60 (4 scenario blocks x 15 = 60 questions)",
    "  Generated: 2026-08-14 from the v2 corpus, seeded from an independent trap inventory",
    "",
    "  SEED SOURCE (new for this paper):",
    "    Questions were seeded from 121 'Exam Trap' blocks extracted from the claudecertificationguide.com",
    "    mirror at Outputs/ccg-mirror/ -- a SECOND community author writing against the same 30 official",
    "    task statements. Registered as source-authority item 4 in CCA-Prep_Corpus-Index_v2.md (v2.2).",
    "    The traps supplied DISTRACTOR GEOMETRY only. Every whyRight/whyWrong still cites the v2 corpus,",
    "    and where the site contradicts the corpus the corpus wins -- see the CONFLICTS note below.",
    "",
    "  SCENARIOS DRAWN (4 of the official 6):",
]
for i, b in enumerate(DATA["blocks"], 1):
    lines.append(f"    {i}. {b['label']:<42s}({prim.get(b['label'], '')})")
lines += [
    "  Rested here: Customer Support Resolution Agent, Multi-Agent Research System -- both drawn by Exam 17,",
    "  so the two papers together cover all six official scenarios.",
    "  Counts before Exam 17 (Exams 2-16): DP 11, CS 10, MR 10, CI 10, SD 10, CG 9.",
    "  Selection: the SECOND of the two unused feasible 4-of-6 draws. Exam 17 took the other. After this",
    "  paper the only unused draws left are CS+CG+MR+DP (infeasible -- no D4-primary block) and",
    "  CS+CG+CI+SD (one D1-primary block against a 16-question D1 quota).",
    "",
    "  DOMAIN QUOTA (base weights -- no confirmed-weakness adjustment applies):",
    "    D1 16 | D2 11 | D3 12 | D4 12 | D5 9 = 60",
    "",
    "  BLOCK x DOMAIN ALLOCATION (primary domains in brackets):",
    "    1. Code Generation        [D3 D5]      D1 3 / D2 2 / D3 4 / D4 2 / D5 4",
    "    2. Developer Productivity [D1 D2 D3]   D1 6 / D2 5 / D3 2 / D4 1 / D5 1",
    "    3. Claude Code for CI     [D3 D4]      D1 4 / D2 1 / D3 5 / D4 5 / D5 0",
    "    4. Structured Extraction  [D4 D5]      D1 3 / D2 3 / D3 1 / D4 4 / D5 4",
    "  Solved as a constraint problem under the gate's STRICT primacy rule: every primary domain outnumbers",
    "  every non-primary in its own block. Max cell 6, one empty cell.",
    "",
    "  ITEM FORMATS: 52 single-answer (4 options) + 8 multiple-response (2 per block, select-2-of-4),",
    "    scored all-or-nothing.",
    "",
    "  CORRECT-ANSWER LETTER PRE-PLAN (single-answer items, fixed before options were drafted):",
    "    block 1 CCBADACDBDCBA   block 2 ACBDBAADCBCDD",
    "    block 3 DCABCBDBAADCA   block 4 BBCCACBADADBD",
    "    Exam-wide A13 B13 C13 D13 = 52. Achieved sequences match the pre-plan exactly.",
    "",
    "  RELATIONSHIP TO EXAM 17: same 121-block trap inventory, disjoint halves. Exam 17 concentrated on",
    "    tool_choice; this paper concentrates on the configuration-location family and on session state.",
    "    Deliberate slogan-breakers, where the same corpus point has the OPPOSITE correct answer:",
    "      Q11 -- resume the session and NAME the 3 changed files (3 of 50 files stale: corpus D1 SS1.16).",
    "      Q44 -- start FRESH with an injected summary (a long-lived CI session, broadly stale: same SS1.16).",
    "      This is the point where the ccg mirror contradicts the corpus. Its D1 traps 1.30/1.32/1.34 call",
    "      --resume-after-changes a trap outright. The corpus draws the line at how stale the prior context",
    "      is, and the corpus wins -- so both directions are tested rather than the site's single rule.",
    "      Q10 vs Exam 17 Q28 -- plan mode is WRONG for a one-file fix with a clear stack trace (Q10) and",
    "      RIGHT for a twelve-file restructure with two candidate designs (Exam 17 Q28).",
    "      Q4 vs Q11 vs Q44 -- fork, resume-and-inform, and fresh-plus-summary, one item each.",
    "",
    "  CONFIGURATION-LOCATION FAMILY (five items, each on the when-does-this-load axis):",
    "    Q1  user scope vs project scope -- why a clone carries nothing from ~/.claude/",
    "    Q3  /memory is a diagnostic, not a loader",
    "    Q6  a skill is a DIRECTORY with SKILL.md; a loose .md in .claude/skills/ is not picked up",
    "    Q23 task workflows belong in skills, not in an always-loaded CLAUDE.md",
    "    Q28 .claude/rules/ vs a paths-scoped skill -- background guidance vs invoked workflow",
    "    Q41 @path imports as the supported way to modularise CLAUDE.md",
    "",
    "  DEDUPLICATION: all 60 stems checked by Jaccard against 886 prior stems (810 from EXAM-LOG Exams",
    "    2-16 + the 76 community stems in PRACTICE-TEST-STEMS_v1.md SS2). Highest single similarity 0.196,",
    "    mean max-similarity 0.136, zero stems at or above the 0.40 reskin threshold. Also checked against",
    "    Exam 17 by the archetype gate.",
    "",
    "  INLINE TOKEN RATE: 17.1% of options carry a code/config token -- inside the gate's 15-30% pass band,",
    "    below the 20-25% target. This paper's subject matter runs to mechanisms and locations rather than",
    "    parameter values, so fewer options name a literal token. Reported rather than padded.",
    "",
   "  QUESTIONS USED (deduplication ledger for Exam 19+):",
]
for q in DATA["questions"]:
    tag = f"[{q['domain']}]" + (f"[select-{q['selectN']}]" if q.get("selectN") else "")
    body = f"{q['g']}. {tag} {plain(q['stem'])}"
    lines += textwrap.wrap(body, width=120, initial_indent="  ", subsequent_indent="     ")

header = "\n".join(lines).replace("-->", "- ->")  # never let the ledger close the comment early

html = tpl.replace("__HEADER_COMMENT__", "\n" + header + "\n")
html = html.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(html)

print(f"wrote {OUT}")
print(f"  size: {os.path.getsize(OUT)/1024:.1f} KB")
print(f"  placeholders remaining: {html.count('__DATA__') + html.count('__HEADER_COMMENT__')}")
