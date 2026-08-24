"""Append the Exam 16 skeleton entry to EXAM-LOG.md and its row to DASHBOARD-DATA.jsonl.

Append-only. Refuses to run twice.
"""
import json, os, re, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOG = os.path.join(ROOT, "EXAM-LOG.md")
JSONL = os.path.join(ROOT, "DASHBOARD-DATA.jsonl")

DATA = json.load(open(os.path.join(HERE, "exam16-data.json"), encoding="utf-8"))

log = open(LOG, encoding="utf-8").read()
if "## Exam 16 —" in log:
    raise SystemExit("REFUSING: EXAM-LOG.md already carries an Exam 16 entry.")

def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()

entry = """

---

## Exam 16 — Generated 2026-08-11

**File:** `mock-exams/CCA-Prep_MockTest-16_v1.html`
**Format:** FULL60 (4 scenario blocks x 15 = 60 questions) — 47 single-answer + 13 multiple-response
**Scenarios drawn:** Customer Support Resolution Agent; Multi-Agent Research System; Developer Productivity with Claude; Claude Code for Continuous Integration
**Attempt date:** Not yet attempted
**Score source:** Pending
**Total score:** Pending

**Purpose:** generated the same evening as a compute expiry, and the concern was put on the record first —
Exams 12, 13, 14 and 15 were already unattempted with the sitting on 2026-08-18. Ram's call, and generation
is cheap against losing the compute. **Five papers are now unattempted: 12, 13, 14, 15 and 16.**

What this paper adds that the others cannot: **it is the flattest domain load the scenario bank permits.**
No block carries more than five questions of any one domain. Exam 15's extraction block ran twelve of its
fifteen questions in D4, and Exam 14's margins were 3/3/3/4. A block that is 80% one domain lets the
candidate settle into a single mode for fifteen questions, which the real exam's blocks do not reward.

**Quota:** base weights — D1 16 / D2 11 / D3 12 / D4 12 / D5 9. No confirmed-weakness adjustment (Exam 9
weakest D2 attempted 2026-08-09, Exam 11 weakest D5 attempted 2026-08-10 — different domains by attempt
chronology, so the two-consecutive gate is not met).

**Scenario draw — solved as a constraint problem over all 15 possible 4-of-6 sets, not chosen by hand.**
Counts entering this paper: Structured Data Extraction 10, Developer Productivity 10, the other four 9
each. The rotation preference (the four least-used) is `{CS, CG, MARS, CI}` — but that set was already
used by Exam 7, so rotation and the never-used-combination rule conflict here for the first time. Ten of
the fifteen sets are used across Exams 2–15. Of the five unused, `{CG, CS, DP, MARS}` is **infeasible**:
it contains no D4-primary block at all, and D4 needs twelve questions. The four survivors all level the
rotation to 9–11, so rotation could not discriminate between them either; the tiebreak used was the
minimum-maximum-cell criterion — the draw in which no block must absorb more than five questions of a
single domain. Only `{CS, MARS, DP, CI}` achieves 5; the others need 6 or 7. Rests Code Generation and
Structured Data Extraction, both of which Exam 15 drew. Post-Exam-16 spread: Customer Support 10,
Multi-Agent Research 10, Developer Productivity 11, Claude Code CI 10, Code Generation 9,
Structured Data Extraction 10.

**Block x domain allocation:**

| Block | Scenario | Primary domains | Allocation | Margin |
|---|---|---|---|---|
| 1 | Customer Support Resolution Agent | D1, D2, D5 | D1 5 / D2 3 / D5 3 · D3 2 / D4 2 | 1 |
| 2 | Multi-Agent Research System | D1, D2, D5 | D1 4 / D2 3 / D5 4 · D3 2 / D4 2 | 1 |
| 3 | Developer Productivity with Claude | D2, D3, D1 | D1 4 / D2 4 / D3 4 · D4 3 / D5 0 | 1 |
| 4 | Claude Code for Continuous Integration | D3, D4 | D3 4 / D4 5 · D1 3 / D2 1 / D5 2 | 1 |

Every block satisfies gate 4 with a margin of exactly 1, which is what "flattest" costs: the allocation
sits right on the constraint rather than comfortably inside it. Totals D1 16 / D2 11 / D3 12 / D4 12 / D5 9.

**Correct-answer letter pre-plan (fixed before any option was drafted, single-answer items only):**

| Block | Short letter | Sequence | Tally |
|---|---|---|---|
| 1 | — | `BDACDBACBDCA` | A3 B3 C3 D3 |
| 2 | — | `CADBACBDABDC` | A3 B3 C3 D3 |
| 3 | — | `DBCABDCADCAB` | A3 B3 C3 D3 |
| 4 | A | `CDBCADBDCBA` | A2 B3 C3 D3 |

Exam-wide A11 B12 C12 D12 = 47. Because 13 of the 60 items are multiple-response, three blocks hold 12
single-answer items (which divide evenly by four, so no short letter is needed) and block 4 holds 11.
Achieved sequences match the pre-plan **exactly** — verified mechanically in `WIP-EXAM16/assemble.py`,
which fails the build on any divergence rather than reporting it afterwards.

**Item formats:** 47 single-answer + 13 multiple-response (9 select-2-of-5, 4 select-3-of-6), scored
all-or-nothing. Same share as Exams 14 and 15, so the three papers stay comparable on format.

**Professor's Note consumed — Intent for Exam 13** (written after Exam 11 scored 55/60 on 2026-08-10; still
the most recent note, since nothing has been scored since). All three named sections are covered, each in
a shape the learner has not seen:

| Note item | Where | Shape used |
|---|---|---|
| D2 §2.8 composite vs prompt bundling — missed on Exams 5, 8, 10, 11 | Q38 | select-3, starting from a team that **already built** the composite and is now paying a second-order cost (ban-list BF-2 approved re-frame). The corpus's own slogan is one of the options to evaluate rather than recall. |
| D1 §1.18 evaluator-optimizer vs context isolation | Q59 | select-2 direct disambiguation — two proposals, name each pattern, with the two names crossed over as distractors. |
| D5 §5.8 over-escalation of a resolvable ambiguity | Q3 | multiple-match disambiguation with "escalate to a human at once" as the trap option. |

**Fresh-section coverage:** all four D3 §3.7 subsections appear — the least-used sections in the whole
corpus at 2–3 prior uses each. §3.7.1 interview pattern Q32, §3.7.2 test-driven iteration Q49, §3.7.3
concrete I/O examples Q36, §3.7.4 batching interdependent feedback Q57. **58 distinct corpus sections**
carry the whyRight citation across 60 questions; only D2 §2.3 and §2.9 appear twice, which is forced —
D2 has nine sections and an eleven-question quota — and each pair tests a different facet (§2.3
business-rule error Q2 vs empty-result-versus-access-failure Q56; §2.9 Grep-vs-Glob Q31 vs the
Edit→Read+Write fallback Q34).

**Fidelity gates — computed by `tools/archetype_gate.py` against the shipped HTML, not hand-tallied.**
All seven pass:

| Check | Result |
|---|---|
| 1 · no invented names | 0 flagged |
| 2 · letter tally (SA only) | A11 B12 C12 D12 |
| 3 · word counts | stem min 43 / median 54 / max 62; option max 25 (caps 95 and 35) |
| 4 · block vs primary domains | holds in all four blocks |
| 5 · inline code/config token rate | 53/257 options = 20.6% (target band 20–25%) |
| 6 · multiple-response validity | 13 well-formed MR items |
| 7 · archetype collision | **0** stems at/above 0.40 Jaccard against **893** prior stems (Exams 2–15); 0 intra-paper; top closing formula 2×, top opening formula 1× |

**The gate caught six real defects before shipping**, all in one pass: four invented-name flags the
generic-framing rule should have caught during drafting (`Briefings` and `Yesterday` as sentence openers
that appear nowhere in lower case, and `Monday` twice — weekday names are not in the allowed-proper list);
a stem median of 46 against the binding 50–55 band, fixed by adding concrete situational detail to 49
stems rather than padding; an inline-token rate of 14.4% against the 15–30% floor; a multiple-response
stem (Q59) whose select-count was phrased "Select the two named patterns", which the validity check
cannot read — reworded to close on "Select two."; and two questions in block 2 closing on the identical
sentence. Every fix is recorded as an asserted fragment replacement in `WIP-EXAM16/patch_gates.py`, so
the edit set is auditable rather than a silent rewrite.

**Industry territory — all four new**, generically framed per the naming rule: university student
services (tuition instalments, enrolment, accommodation charges); fisheries stock assessment (survey
reports, quota filings); a payroll and time-and-attendance platform (award interpretation, shift
penalties, leave accrual); and online grocery fulfilment CI (picking routes, substitution rules,
chilled-chain compliance).

**Verified in a browser through the page's own event handlers** (localhost:8768): landing card with the
verbatim rotation-disclosure line; single-answer lock-and-reveal on both the correct and the wrong path,
every rationale carrying its citation; post-lock clicks ignored; multiple-response toggle on and off with
in-progress selections persisted under a `pending` key so a mid-selection resume works; commit at exactly
N; the wrong-path multiple-response feedback including the "belongs in the answer" state for correct
options that were not picked; all three resume branches (fresh → landing, partial → first unanswered,
complete → results); Back disabled on question 1, Next disabled until answered, "Show my results" in the
final slot; jump map with 60 chips across four block rows carrying answered/current/multi states; the
running-accuracy pill exact at the 620/900 threshold — 31/45 = 68.889% renders green `pass`, 30/45 =
66.7% renders red `fail`; the pass boundary exact at 42/60 = 730 "Above pass line" and 41/60 = 715 "Below
pass line"; print-all rendering all 60 questions with 4 block headers and 180 locked rationale rows before
tearing its container down; and the export JSON carrying `item_formats`, per-question `type`
(`single` / `multi-2` / `multi-3`) and comma-joined `selected` letters. Console clean on an organic
session apart from a favicon 404. `localStorage` was cleared afterwards, so the file ships unstarted.

**One cosmetic defect found in Exam 15 while building this — not fixed.** Exam 15's four block narratives
contain literal `<code>` tags in the DATA payload. The template escapes HTML before converting backticks,
so those render to the reader as visible `<code>` text rather than styled code. It affects the four
narrative cards only, never a stem, option or rationale. Left alone because Exam 15 is unattempted and Ram
may still sit it; recorded here so a future session can decide. Exam 16 uses backticks throughout and was
checked for the same fault.

### Questions Used (deduplication ledger for Exam 17+)

"""

lines = []
for q in DATA["questions"]:
    tag = f"[{q['domain']}]" + (f"[select-{q['selectN']}]" if q.get("selectN") else "")
    body = f"{q['g']}. {tag} {plain(q['stem'])}"
    lines.append(body)

entry += "\n".join(lines) + "\n"

with open(LOG, "a", encoding="utf-8") as fh:
    fh.write(entry)
print(f"appended Exam 16 entry to EXAM-LOG.md (+{len(entry)} chars)")

rows = [json.loads(l) for l in open(JSONL, encoding="utf-8") if l.strip()]
if any(r["exam_n"] == 16 for r in rows):
    raise SystemExit("REFUSING: DASHBOARD-DATA.jsonl already carries exam_n 16.")
rows.append({
    "exam_n": 16, "format": "FULL60", "generated_date": "2026-08-11", "attempted_date": None,
    "score_source": None, "total_correct": None, "total_questions": 60, "estimated_scaled": None,
    "total_seconds": None, "domain_scores": None, "weakest_domain": None,
    "confirmed_weakness": None, "insight_round_due": False,
})
rows.sort(key=lambda r: r["exam_n"])
with open(JSONL, "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"DASHBOARD-DATA.jsonl now holds {len(rows)} rows, sorted by exam_n")
