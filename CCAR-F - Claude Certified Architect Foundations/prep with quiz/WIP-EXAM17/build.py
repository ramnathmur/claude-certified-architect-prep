import json, os, re, sys, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXAM_N = 17
OUT = os.path.join(ROOT, "mock-exams", f"CCA-Prep_MockTest-{EXAM_N}_v1.html")

# PRE-FLIGHT: never overwrite a numbered artifact by accident.
if os.path.exists(OUT) and "--force" not in sys.argv:
    sys.exit(f"REFUSING TO OVERWRITE: {OUT} already exists. Increment the version, or pass --force to rebuild.")

DATA = json.load(open(os.path.join(HERE, f"exam{EXAM_N}-data.json"), encoding="utf-8"))
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


prim = {
    "Customer Support Resolution Agent": "primary D1, D2, D5",
    "Multi-Agent Research System": "primary D1, D2, D5",
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
    "  Rested here: Code Generation with Claude Code, Developer Productivity with Claude -- both drawn by",
    "  Exam 18, so the two papers together cover all six scenarios.",
    "  Counts before this paper (Exams 2-16): DP 11, CS 10, MR 10, CI 10, SD 10, CG 9.",
    "  Selection: this is one of only two UNUSED feasible 4-of-6 draws left after fifteen papers. Solved as",
    "  a constraint problem over all 15 draws -- CS+CG+MR+DP is unused but INFEASIBLE (no D4-primary block),",
    "  and CS+CG+CI+SD is unused but carries only one D1-primary block against a 16-question D1 quota.",
    "",
    "  DOMAIN QUOTA (base weights -- no confirmed-weakness adjustment applies):",
    "    D1 16 | D2 11 | D3 12 | D4 12 | D5 9 = 60",
    "  Driver: Exam 13's nominal weakest (D2 at 91%) was a denominator artefact -- D2, D3 and D4 each lost",
    "  exactly one question. No confirmed weakness, so the base quota stands.",
    "",
    "  BLOCK x DOMAIN ALLOCATION (primary domains in brackets):",
    "    1. Customer Support        [D1 D2 D5]  D1 4 / D2 4 / D3 2 / D4 2 / D5 3",
    "    2. Multi-Agent Research    [D1 D2 D5]  D1 5 / D2 6 / D3 1 / D4 1 / D5 2",
    "    3. Claude Code for CI      [D3 D4]     D1 4 / D2 0 / D3 6 / D4 5 / D5 0",
    "    4. Structured Extraction   [D4 D5]     D1 3 / D2 1 / D3 3 / D4 4 / D5 4",
    "  Solved as a constraint problem: every primary domain STRICTLY outnumbers every non-primary in its",
    "  own block (gate 4 requires >, not >=). The first drafted allocation tied in all four blocks and",
    "  failed; five questions were rewritten to a different domain rather than re-tagged -- Q13 D4->D2,",
    "  Q28 D3->D2, Q40 D2->D3, Q43 D5->D4, Q59 D2->D5. Each now tests a different corpus section.",
    "",
    "  ITEM FORMATS: 52 single-answer (4 options) + 8 multiple-response (2 per block, select-2-of-4),",
    "    scored all-or-nothing.",
    "",
    "  CORRECT-ANSWER LETTER PRE-PLAN (single-answer items, fixed before options were drafted):",
    "    block 1 CCDBBCBAADAAD   block 2 DBADABBCABDCC",
    "    block 3 DDCCBBCBDACAA   block 4 BACAADBCDCDBD",
    "    Exam-wide A13 B13 C13 D13 = 52. Achieved sequences match the pre-plan exactly.",
    "",
    "  PROFESSOR'S NOTES CONSUMED (Intent for Exam 17, both notes -- after Exam 12 and after Exam 13):",
    "    1. tool_choice promoted to the highest-priority corpus item. The note asked for THREE items in",
    "       THREE scenarios with three different keys, so a slogan cannot answer them:",
    "         Q21 (Multi-Agent Research)  -> 'any' is correct   (structured output required, tool unknown)",
    "         Q36 (CI)                    -> forced-specific    (one named tool is the pipeline contract)",
    "         Q48 (Structured Extraction) -> 'auto' is correct  (mixed conversational/data workload)",
    "       Plus Q14, where forcing 'any' on every loop iteration is the DEFECT -- it removes the model's",
    "       ability to signal completion. Four items, four different correct directions.",
    "    2. where-does-this-live three-way discrimination -> Q9 and Q41, each separating CLAUDE.md from",
    "       .claude/rules/ from a skill on the when-should-this-load axis rather than by lookup.",
    "    3. D2 SS2.1 tool_result id correlation -> Q11, keyed on the tool_use_id pairing specifically.",
    "    4. D2 SS2.2 fix the description, not the behaviour -> Q6.",
    "    5. Compensating-mechanism geometry (five of Exam 12's seven misses, spanning four domains, which",
    "       no domain quota can target): every block carries items where a plausible workaround sits",
    "       beside the root-cause fix -- Q1, Q3, Q6, Q17, Q21, Q32, Q34, Q37, Q39, Q43, Q46, Q49, Q52.",
    "",
    "  DELIBERATE SLOGAN-BREAKERS (same corpus point, opposite correct answer, same paper):",
    "    Q29 vs Q44 -- adaptive decomposition is correct for the open-ended investigation (Q29) and WRONG",
    "      for the fully-known CI check sequence (Q44). D1 SS1.7 tested in both directions.",
    "    Q21 / Q36 / Q48 / Q14 -- the four tool_choice directions above.",
    "",
    "  SITE-vs-CORPUS CONFLICTS FOUND AND NOT USED (recorded in the coverage report):",
    "    The mirror's D1 traps 1.30/1.32/1.34 call --resume after file changes a trap and prescribe a fresh",
    "    session with summary injection. Corpus D1 SS1.16's worked exam pattern says the opposite for the",
    "    3-of-50-files case: resume and TELL the agent which files changed. Official framing wins, so no",
    "    question was built on that point at all.",
    "    The mirror's D2 glossary says MCP transport selection may be tested. The official out-of-scope list",
    "    bars server-sent events and MCP hosting. No transport question appears on this paper.",
    "",
    "  DEDUPLICATION: all 60 stems checked by Jaccard against 886 prior stems (810 from EXAM-LOG Exams",
    "    2-16 + the 76 community stems in PRACTICE-TEST-STEMS_v1.md SS2). Highest single similarity 0.367",
    "    (Q27), mean max-similarity 0.153, zero stems at or above the 0.40 reskin threshold.",
    "",
    "  INLINE TOKEN RATE: 27.5% of options carry a code/config token -- inside the gate's 15-30% pass band,",
    "    above the 20-25% target. Driven by this paper's deliberate concentration on tool_choice values, MCP",
    "    configuration and CLI flags, all of which render as code. Reported rather than tuned away.",
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
