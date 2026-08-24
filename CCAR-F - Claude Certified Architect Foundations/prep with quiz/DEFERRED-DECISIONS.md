# Deferred Decisions — CCA-F Mock Exam Generator

**Created:** 2026-07-06
**Purpose:** decisions consciously deferred, with the evidence trigger that reopens each. Review this file at every orchestration session start after the trigger condition could plausibly be met.

---

## DD-1: Difficulty-mix calibration — DEFERRED

**Decision:** do not build an easy/medium/hard quota layer into exam generation.
**Why deferred:** nothing published documents the real exam's difficulty distribution (Anthropic discloses the blueprint only at task-statement granularity). A heuristic difficulty quota would be invented calibration — worse than none, because it looks like evidence. The Quiz-Builder v3 blueprint reached the same conclusion independently (its "difficulty-tagging — dropped, fights the grounding constraint" scope decision).
**Reopen when BOTH hold:**
1. Ram has taken the official 76-question community practice test (scores in hand), and
2. 2–3 mocks are scored via results-JSON (exact per-question data).
**Then:** compare practice-test accuracy vs mock accuracy per domain. A consistent gap (mocks ≥10 points easier or harder) is the evidence a calibration layer would need — bring the gap data to a revision session.

## DD-2: Hard-timed exam mode — CLOSED, NOT NEEDED (2026-08-11)

**Decision:** the generated HTML captures timing passively (per-question + total) but imposes no countdown and never withholds feedback.
**Why deferred:** Ram's explicit design call (2026-07-06) — this is a learning tool; per-question rationales are the point. Realism lives in style/coverage/structure.
**Reopen when:** Ram asks for a dress-rehearsal mode (e.g., final week before the sitting). The results-JSON timing data collected meanwhile will show whether pace is even a risk (budget: 2 min/question).
**Checked against a separate suggestion 2026-07-09** (confidence-capture UI — "knew it" / "guessing" click, per the `MCQ-Quiz-Builder_Blueprint_v3.md` 2×2 confidence matrix, raised via the `academy/` project's migration audit): this is not actually a DD-2 collision on the letter of the decision — DD-2 is specifically about a countdown that withholds feedback; a self-rated confidence click does neither. The overlap is only in spirit (does self-rating add evaluative pressure?), and it's a soft one. Not implemented — it wasn't the audit's primary recommendation, and no one has asked for it directly. Worth reconsidering together with DD-4 if DD-4 ships, since option-level trap tracking and confidence self-rating are complementary signals, not a package deal.
**Partially honored elsewhere 2026-08-10:** the drill app (see DD-3) grades every card on a three-way scale — Missed / Guessed it / Knew it — which is the confidence-capture idea in its simplest form, and it drives scheduling directly (a guessed card returns tomorrow regardless of its box). This does not settle the question for the mock exams, where the 2×2 matrix would still be a new UI on a different artifact. DD-2 itself is unchanged: no countdown, no withheld feedback, in either tool.

**CLOSED 2026-08-11 — trigger fired, reviewed, decided against.** The reopen condition ("final week before the sitting") became true today: the exam is booked for 2026-08-18, seven days out. Raised to Ram by a `/sync-up` audit and closed on his call, on the evidence the deferral itself said to collect.

**The pace data the deferral was waiting for says pace is not a risk.** The budget is 7,200 seconds for 60 questions. Recent sittings, from the results-JSON `total_seconds` field in `DASHBOARD-DATA.jsonl`:

| Exam | Seconds | vs 7,200 budget |
|---|---|---|
| Exam 8 | 2,121 | 29% |
| Exam 9 | 2,529 | 35% |
| Exam 10 | 2,357 | 33% |
| Exam 11 | 2,418 | 34% |

Four consecutive sittings at roughly a third of the allowed time, none above 35%. A countdown would measure a constraint that is not binding, and building one this close to the exam would compete with actually sitting the three unattempted papers — which is the scarce activity. (Exams 4, 6 and 7 show much larger figures — 44,148 / 15,625 / 19,489 seconds — but those were multi-session sittings where the timer ran across breaks, so they measure elapsed wall-clock, not pace.)

**Reopen only if:** Ram sits a paper under genuine timed conditions and finishes above ~5,500 seconds, or a future exam-format change materially lengthens the questions. Neither is in view.

## DD-3: Spaced repetition of missed questions — SUPERSEDED (2026-08-10)

**Decision:** missed-question re-surfacing stays at the insights-round level (repeated-trap flagging), not per-question scheduling.
**Why:** the dedup rule (never repeat a stem) is load-bearing for exam realism; per-question repetition would rewrite it. Quiz-Builder v3 hit the same conflict (its v3.1 note).
**Reopen when:** the exam date is set and >3 weeks out, and insights rounds show the same Key Distinctions missed across 3+ exams — then consider a separate flashcard artifact (NOT a mock exam) for those specific traps.
**Reconsidered 2026-07-09** (cross-project suggestion via the sibling `academy/` project's migration audit, passed on by that project's session): re-verified against the reopen condition above, independently — not taken on the audit's summary of it, which stated the date threshold inverted (as "<3 weeks out" rather than the actual ">3 weeks out"). Verdict unchanged regardless of which direction that inequality runs: condition 2 (3+ scored exams showing the same Key Distinction missed) is nowhere close to met — zero exams have been scored across all four generated to date (see `EXAM-LOG.md`). Still NOT PLANNED.

**SUPERSEDED 2026-08-10 — by Ram's direct request, exam booked for 2026-08-18.** Ram asked for a flashcard/drill artifact as the final prep phase, saying the long HTML courseware is not sticking. A direct instruction outranks a deferral ledger, so this decision is closed rather than reopened on its trigger. Two notes for the record, since neither reopen condition was actually met:

- **Condition 1 (">3 weeks out") is now false in the other direction** — the exam is 8 days away, not 3+ weeks. The clause was written to stop a flashcard build from displacing exam generation too early in the runway; at 8 days the calculus inverts, since four unattempted mocks already exist and drilling is the scarce activity.
- **Condition 2 (repeated misses across 3+ scored exams) is still unmet** — zero exams scored. So the deck could not be targeted at empirically-repeated traps. It was instead grounded in the corpus as a whole, weighted by official domain weights, with extra weight on the eight documented weak points in `academy/LEARNER-MODEL.md` (real recorded misses, unlike the synthetic `GAPS.md`). The drill app ships with a results-JSON importer so that the moment a mock IS scored, missed questions boost the matching cards by citation — which is the mechanism this DD originally wanted, arrived at from the other end.

**What shipped:** `drill/CCA-Prep_Drill_v1.html` plus `drill/CARD-SPEC.md`, `drill/build_deck.py`, and `drill/deck/*.cards.json`. It is a separate artifact and touches no exam-generation rule: the never-repeat-a-stem dedup constraint that made per-question repetition unacceptable is untouched, because flashcard fronts are not exam stems and the build script actively checks card fronts against both stem ledgers for collisions.

## DD-4: Contrast-pair distractors + option-level trap tracking — RECOMMENDED, AWAITING RAM'S SIGN-OFF

**Origin:** raised 2026-07-09 via a migration audit from the sibling `academy/` project (delivers CCA-F content conversationally rather than through this HTML generator), passed on by that project's session for independent evaluation — not accepted on that session's authority; evaluated cold against this project's own files below.

**What it is:** (a) when writing a question's three distractors, deliberately designate one as the *contrast pair* — the most authoritative-sounding, closely-adjacent-concept misconception (not just any of the three documented ❌ patterns), and record which one in the DATA; (b) when a learner selects a wrong option, look up whether it was the contrast-pair option specifically, not just "wrong" — record it as a distinct, sharper signal than a generic miss; (c) let the Professor's Note (and future insights rounds) bias toward re-seeding that *exact trap form* for a Key Distinction the learner fell for via the adjacent-concept trap, rather than only tracking "this Key Distinction was missed" at the question level.

**Verified independently, not taken on the audit's word:**
- `results-JSON` already exports `selected` per question (confirmed against `CLAUDE.md`'s own schema block, unchanged) — the raw data this needs already exists.
- Current distractor rule (`CLAUDE.md` Step 4 / `CCA-Orchestration-Prompt_v9.md` Phase 4.e) requires three *documented misconceptions*, grammatically parallel, no giveaways — a real bar, but it never designates *which* of the three is the primary adjacent-concept trap, and nothing downstream reads that distinction.
- Phase 2d (score-entry cross-referencing) matches a wrong answer to a Key Distinction at the *question* level only ("this question, tagged to this KD, was missed") — it has no mechanism to distinguish "missed by falling for the authoritative-sounding trap" from "missed by picking an obviously-wrong option," even though both cases currently just look like "wrong."

**Why this doesn't collide with anything already decided:** no dedup rewrite (DD-3's objection) — this tags existing distractors and existing score data, it doesn't schedule question repetition. No timing/pressure change (DD-2's objection) — nothing about revealing or withholding feedback changes. No corpus-content edit — it's a process/authoring-instruction change plus an additive, backward-compatible results-JSON field, not a change to any Domain-N_v2.md fact.

**Why this is logged as a recommendation, not shipped:** the audit's own instructions said an "accept" verdict should become a version bump on my authority. I'm declining that specific instruction — this is a live tool shaping Ram's actual exam prep, the suggestion arrived through an unverified cross-session channel, and implementing it changes the DATA schema and the authoring rules for every future exam. That's Ram's call.

**If approved, the concrete change is:** (1) `CCA-Orchestration-Prompt_v9.md` Phase 4.e gets one new clause — when writing the three distractors, mark exactly one `"contrastPair": true` (the closest adjacent-concept misconception); (2) the results-JSON `questions[]` schema gains an optional `"fellForContrastPair": true|false|null` field, computed by the HTML at scoring time (null when the question was answered correctly or the DATA predates this field); (3) Phase 2d's cross-reference step reads that field when present and reports it in the Professor's Note distinctly from a generic miss. No changes needed to any Domain-N_v2.md corpus file.
