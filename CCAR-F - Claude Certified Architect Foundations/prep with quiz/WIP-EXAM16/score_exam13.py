"""Score Exam 13 into the ledgers. Append-only apart from the pending header lines inside the
Exam 13 entry. Refuses to run twice.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOG = os.path.join(ROOT, "EXAM-LOG.md")
JSONL = os.path.join(ROOT, "DASHBOARD-DATA.jsonl")

t = open(LOG, encoding="utf-8").read()
if "## Exam 13 — SCORED" in t:
    raise SystemExit("REFUSING: Exam 13 already scored in EXAM-LOG.md")

# ---- patch the pending header lines inside the Exam 13 entry only ----
start = t.index("## Exam 13 — Generated")
end = t.index("## Exam 14", start)
seg = t[start:end]
old = ("**Attempt date:** Not yet attempted\n"
       "**Score source:** Pending\n"
       "**Total score:** Pending")
assert seg.count(old) == 1, f"header block not uniquely found in the Exam 13 entry ({seg.count(old)} hits)"
new = ("**Attempt date:** 2026-08-12\n"
       "**Score source:** results-json\n"
       "**Total score:** 57 / 60 correct (estimated scaled: 955 / 1000; pass line 720) — best of ten\n"
       "**Total time:** 35:53 (35.9s/question — 30% of the 120-minute allowance)")
t = t[:start] + seg.replace(old, new) + t[end:]

entry = """

---

## Exam 13 — SCORED 2026-08-12

**Score source:** results-json (full per-question data)
**Total:** 57 / 60 correct · estimated scaled 955 / 1000 · pass line 720 — **the best result across ten
scored attempts**, ahead of Exams 7 and 11 at 55/60 (925).
**Time:** 2,153s = 35:53 (35.9s/question). Fastest full single sitting on record, and the highest score.
Speed and accuracy moved together, not against each other.

### Domain Breakdown

| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | 16 | 100% | no |
| D2 Tool Design & MCP | 11 | 10 | 91% | no |
| D3 Claude Code Config | 12 | 11 | 92% | no |
| D4 Prompt Engineering | 12 | 11 | 92% | no |
| D5 Context Management | 9 | 9 | 100% | no |

**D1 at 16/16 is a first** — the heaviest domain (27% of the exam) clean, on a base-quota paper.

### Block Breakdown

| Block | Scenario | Correct |
|---|---|---|
| 1 | Customer Support Resolution Agent | 15 / 15 |
| 2 | Multi-Agent Research System | 14 / 15 |
| 3 | Code Generation with Claude Code | 14 / 15 |
| 4 | Structured Data Extraction | 14 / 15 |

### Weakest domain — do not act on it

Nominally D2 at 90.9%. **This is the denominator artefact Insights Round 3 warned about, one day later:**
D2, D3 and D4 each lost **exactly one question**; D2 only ranks lowest because it has 11 questions to
D3/D4's 12. A one-question difference in denominator, not performance. Prior scored paper by attempt
chronology is Exam 12 (weakest D3/D4), so the two-consecutive gate is not met and **no confirmed weakness
exists — base quota stands for Exam 17.** exams_scored = 10; the next Insights Round falls at 12.

### The three misses

| Q | Dom | § | Picked | Key | Time |
|---|---|---|---|---|---|
| 19 | D2 | §2.2 | D — return an error instead of a partial document | C — expand the description to state formats, the 40-page truncation, and the auth boundary | 35s |
| 41 | D3 | §3.11 | B — split background to README, standards to `.claude/rules/` | C — cut the background and culture prose; keep the operative instructions | 43s |
| 46 | D4 | §4.6 | A — `tool_choice: "auto"` plus a prompt instruction | C — `tool_choice: "any"` | 28s |

### Observations — both watch-items from the Exam 12 note recurred

**1. Q46 repeats Exam 12's Q33 exactly, and this is the headline result.** Both ask which configuration
*guarantees* a tool call; both offer `auto` + a prompt instruction as the trap and `any` as the key. Ram
picked the trap both times — on 2026-08-11 and again on 2026-08-12, roughly fourteen hours apart, **having
read the full rationale for Q33 in between** (the papers give per-question feedback on lock-in).

The two stems measure **0.118 Jaccard** — far below the archetype gate's 0.40 reskin threshold, and the
two questions sit in different scenarios (Developer Productivity vs Structured Data Extraction), different
domains as tagged (D2 §2.5 vs D4 §4.6), and different surface framings (posting a work-tracker record vs
extracting from an unknown document type). **He is not pattern-matching a repeated question; he holds an
actively wrong preference for `auto` + instruction over `any`.** That is the most valuable single finding
in ten scored papers, because it is precisely the kind of error that survives more practice papers and
only dies to targeted drilling.

**2. `.claude/rules/` is now a confirmed reflex — third wrong pick in two papers.** Exam 12 Q1 (where the
answer was a diagnostic, `/memory`), Exam 12 Q56 (where the answer was `.claude/commands/`), and now
Exam 13 Q41 (where the answer was to delete prose from `CLAUDE.md`). Three different correct answers, one
recurring wrong instinct: reaching for path-scoped rules whenever the question smells like "where should
this live?".

**3. The compensating-mechanism pattern survived a fresh paper — but attenuated.** The Exam 12 note asked
whether the reflex would disappear on an unfamiliar paper or persist, which would make it a genuine
reasoning habit. Verdict: **it persisted.** Q46 chose a probabilistic control over an available guarantee,
and Q19 changed the tool's runtime behaviour rather than fixing the description that is the model's only
view of scope. Notably he did *not* take Q19's obvious workaround option (a post-processing check that
flags truncated documents) — so the pull toward pure symptom-patching has weakened, while the pull away
from *fixing the signal* has not.

**4. Everything else is clean.** D1 16/16 including the whole Customer Support block; D5 9/9; no block
below 14/15. Nine of the ten scored attempts now sit at 49–57 raw.

### Professor's Note — Intent for Exam 17 (second note, after Exam 13)

Written after Exam 13 (attempted 2026-08-12). Based on results-json. Extends rather than replaces the note
written after Exam 12 — that note's targeting is unchanged, and this one narrows it. **Still numbered 17
because Exams 14, 15 and 16 were all generated before either score arrived.**

- Misconceptions revealed:
  1. **`tool_choice` `any` vs `auto` + instruction (D2 §2.5 / D4 §4.6) — missed twice in fourteen hours on
     genuinely distinct questions.** Promote this from "a section to cover" to **the single highest-priority
     item in the corpus for this learner.** It is not a coverage gap; feedback has already been read and
     the wrong preference survived it.
  2. **`.claude/rules/` as the default answer to "where should this live?" (D3 §3.2 crowding out §3.1,
     §3.4 and §3.11) — three wrong picks across two papers.**
  3. **Fixing tool behaviour rather than the tool description (D2 §2.2)** — the description is the model's
     only view of scope and boundaries.
- Weakest this paper: **nominally D2 at 91%, but disregard it** — D2, D3 and D4 each lost exactly one
  question and the ranking is a denominator effect. No confirmed weakness; base quota for Exam 17.
- Intent for next paper: give the `tool_choice` distinction **three separate items in three different
  scenarios**, including one where `auto` is genuinely correct and one where the forced-specific-tool form
  is correct, so the discrimination cannot be answered by a memorised slogan. Give the where-does-this-live
  family a three-way discrimination in one item. Keep building items where a plausible workaround sits
  beside the root-cause fix.
- Watch next: whether the `tool_choice` error survives a **third** exposure. If it does after targeted
  drilling, it is a durable mental model rather than a lapse, and warrants a written one-line rule Ram
  carries into the sitting.

### Operational note — the drill deck cannot consume this result

`prep with quiz/drill/CCA-Prep_Drill_v1.html` still carries a mock map for Exams 2, 3, 4 and the Exam-2
retrofit only. Pasting Exam 12's or Exam 13's results boosts nothing, so the mechanism that would normally
turn a repeated miss into spaced repetition is **not running at the exact moment it would pay for itself.**
Fix is recorded in SESSION-STATE.md: rebuild the deck from the main checkout, not a worktree, using
`Outputs/_packbuild/remap_deck.py` for the citation-vocabulary normalisation.
"""

before = len(open(LOG, encoding="utf-8").read())
out = t + entry
assert len(out) > before, "refusing to shrink EXAM-LOG.md"
assert "## Exam 16 —" in out and "## Exam 4 —" in out and "## Insights Round 3 —" in out, "refusing to write a truncated log"
with open(LOG, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"EXAM-LOG.md: {before} -> {len(out)} chars (+{len(out)-before})")

rows = [json.loads(l) for l in open(JSONL, encoding="utf-8") if l.strip()]
hit = [r for r in rows if r["exam_n"] == 13]
assert len(hit) == 1
if hit[0].get("total_correct") is not None:
    raise SystemExit("REFUSING: exam_n 13 already scored in DASHBOARD-DATA.jsonl")
hit[0].update({
    "attempted_date": "2026-08-12", "score_source": "results-json",
    "total_correct": 57, "estimated_scaled": 955, "total_seconds": 2153,
    "domain_scores": {"D1": {"correct": 16, "of": 16}, "D2": {"correct": 10, "of": 11},
                      "D3": {"correct": 11, "of": 12}, "D4": {"correct": 11, "of": 12},
                      "D5": {"correct": 9, "of": 9}},
    "weakest_domain": "D2 (nominal only — D2/D3/D4 each lost exactly one question)",
    "confirmed_weakness": False, "insight_round_due": False,
})
rows.sort(key=lambda r: r["exam_n"])
with open(JSONL, "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"DASHBOARD-DATA.jsonl: {len(rows)} rows, "
      f"{sum(1 for r in rows if r.get('total_correct') is not None)} scored")
