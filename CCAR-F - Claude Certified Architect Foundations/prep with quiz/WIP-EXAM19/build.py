import json, os, re, sys, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXAM_N = 19
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
    "Code Generation with Claude Code": "primary D3, D5",
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
    "  Rested here: Multi-Agent Research System, Developer Productivity with Claude.",
    "  Counts after this paper: CI 13, SD 13, CS 12, DP 12, CG 11, MR 11.",
    "  Selection: this is the LAST unused feasible 4-of-6 draw. After Exam 19 the only unused draw left is",
    "  CS+CG+MR+DP, which is INFEASIBLE -- it contains no D4-primary block against a 12-question D4 quota.",
    "  The draw is D1-tight by construction (CS is its only D1-primary block against a 16-question D1 quota),",
    "  which is why block 1 carries 7 D1 questions and no D4 at all.",
    "",
    "  DOMAIN QUOTA (base weights):",
    "    D1 16 | D2 11 | D3 12 | D4 12 | D5 9 = 60",
    "  Driver: Exam 17 returned D2 73% and D3 75% -- within one fifth of a question of each other, so they",
    "  are treated as TIED rather than ranked. Each concentrates in two sections, so the Professor's Note",
    "  targets sections rather than raising a domain quota. Base quota stands.",
    "",
    "  BLOCK x DOMAIN ALLOCATION (primary domains in brackets):",
    "    1. Customer Support       [D1 D2 D5]  D1 7 / D2 5 / D3 1 / D4 0 / D5 2",
    "    2. Code Generation        [D3 D5]     D1 3 / D2 3 / D3 4 / D4 1 / D5 4",
    "    3. Claude Code for CI     [D3 D4]     D1 4 / D2 1 / D3 5 / D4 5 / D5 0",
    "    4. Structured Extraction  [D4 D5]     D1 2 / D2 2 / D3 2 / D4 6 / D5 3",
    "  Solved under the gate's strict primacy rule: every primary domain outnumbers every non-primary in",
    "  its own block.",
    "",
    "  ITEM FORMATS: 52 single-answer (4 options) + 8 multiple-response (2 per block, select-2-of-4).",
    "",
    "  CORRECT-ANSWER LETTER PRE-PLAN (fixed before options were drafted):",
    "    block 1 DABBCDCACDBAB   block 2 ACCBCAADDBDBA",
    "    block 3 DDBDBCCBAACAD   block 4 ADCDDCBCBAACB",
    "    Exam-wide A13 B13 C13 D13 = 52. Achieved sequences match the pre-plan exactly.",
    "",
    "  PROFESSOR'S NOTE CONSUMED (Intent for Exam 19, written after Exam 17 scored 51/60):",
    "    1. THE GUARANTEE-STRENGTH LADDER -- four items, four scenarios, and the discrimination runs in",
    "       BOTH directions, which is what Exam 17 did not test:",
    "         Q2  (Customer Support)    -> auto is too WEAK      -> any        (record is mandatory,",
    "                                                                 which of three is not knowable)",
    "         Q23 (Code Generation)     -> any is too STRONG     -> auto       (mixed conversational turns)",
    "         Q32 (CI)                  -> one named tool IS the contract -> forced-specific",
    "                                                                 (the exact rung missed on Exam 17 Q36)",
    "         Q46 (Structured Extraction) -> forced is too STRONG -> any       (NEW DIRECTION: a guarantee",
    "                                                                 already in place that exceeds the",
    "                                                                 requirement and must be RELAXED)",
    "       Exam 17 proved the old error -- probabilistic control preferred over an available guarantee --",
    "       is closed: Q21 was answered correctly after 138 seconds. What replaced it is under-specifying",
    "       the rung, so Q46 inverts it and tests over-specifying as well.",
    "    2. PREVENTION vs AFTER-THE-FACT DETECTION, WITH NO MENTION OF HOOKS ANYWHERE (the Exam 17 transfer",
    "       failure: Q2 right when asked as PostToolUse-vs-PreToolUse, Q19 wrong when the same distinction",
    "       was dressed as tool design):",
    "         Q6  an uncapped credit tool plus a nightly reconciliation that reverses over-limit credits",
    "         Q18 an unrestricted shell tool plus a weekly log review that reverts inappropriate commands",
    "         Q15 / Q57 over-broad retrieval tools narrowed at the interface rather than filtered after",
    "       Neither hook event is named on this paper.",
    "    3. D3 SS3.7 WITH WRONG-AXIS DISTRACTORS rather than wrong facts (both Exam 17 SS3.7 misses were",
    "       axis errors, not knowledge gaps):",
    "         Q16 technique selection -- the axis is whether the target can already be stated, and the",
    "             distractors offer thoroughness, breadth of change, and a blanket rule",
    "         Q22 feedback batching -- the axis is whether the issues interact, and the distractors offer",
    "             severity order, mechanical-vs-substantive (the exact wrong axis picked on Exam 17 Q54),",
    "             and file order",
    "    4. RE-TESTS of the other Exam 17 misses in fresh frames: Q35 semantic-vs-syntax defect classes",
    "       (Q42), Q9 / Q40 the where-does-this-live family (Q41), Q1 the agent loop (Q7). Q30 inverts the",
    "       edit-recovery point Ram missed on Exam 17 Q53 -- here read-plus-write IS correct, because six",
    "       byte-identical blocks leave neither a wider anchor nor replace-all able to isolate one.",
    "    5. Workaround-beside-root-cause geometry retained throughout -- it still caught three of nine.",
    "",
    "  DEDUPLICATION -- and a process fix. The first draft passed a dedup check against 886 stems and then",
    "    FAILED the archetype gate with 27 collisions against Exams 17 and 18, because the hand-built ledger",
    "    predated both papers. The ledger is now rebuilt from drill/deck/gen/mock-qbank.json, which the drill",
    "    pipeline parses from every mock-exam HTML on disk, so it cannot go stale again: 1,156 stems across",
    "    Exams 2-18 plus the 76 community stems. Final state: 0 collisions on the gate (1,073 prior stems),",
    "    0 at or above 0.40 on the word-level check, mean max-similarity 0.233.",
    "    Twenty-seven stems were rewritten and seven questions replaced outright with different corpus",
    "    sections -- Q23, Q30, Q31, Q38, Q54, Q58, Q60 -- rather than reskinned.",
    "",
    "  INLINE TOKEN RATE: 22.5% of options carry a code/config token -- inside the 20-25% target band.",
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
