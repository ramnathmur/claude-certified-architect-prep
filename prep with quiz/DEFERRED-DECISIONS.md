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

## DD-2: Hard-timed exam mode — DEFERRED

**Decision:** the generated HTML captures timing passively (per-question + total) but imposes no countdown and never withholds feedback.
**Why deferred:** Ram's explicit design call (2026-07-06) — this is a learning tool; per-question rationales are the point. Realism lives in style/coverage/structure.
**Reopen when:** Ram asks for a dress-rehearsal mode (e.g., final week before the sitting). The results-JSON timing data collected meanwhile will show whether pace is even a risk (budget: 2 min/question).

## DD-3: Spaced repetition of missed questions — NOT PLANNED

**Decision:** missed-question re-surfacing stays at the insights-round level (repeated-trap flagging), not per-question scheduling.
**Why:** the dedup rule (never repeat a stem) is load-bearing for exam realism; per-question repetition would rewrite it. Quiz-Builder v3 hit the same conflict (its v3.1 note).
**Reopen when:** the exam date is set and >3 weeks out, and insights rounds show the same Key Distinctions missed across 3+ exams — then consider a separate flashcard artifact (NOT a mock exam) for those specific traps.
