# Held-Out Mock Bank (Mock A + Mock B)

**Purpose:** two full 60-question mock exams used as the **readiness gate** (Sessions 35 & 37). These are deliberately **held-out** — every question is original and does **not** reuse or paraphrase any stem from the `practice/` banks, the integration checkpoints, the study-guide samples, or the academy teaching examples. That is what makes a mock a valid predictor: it measures readiness, not recognition of material already studied.

> **Do not study these files.** Treat them like a sealed exam. Reading the questions/answers before a mock converts them back into recognition practice and destroys the held-out property. Only the Exam Coach opens them, at mock time.

---

## Composition (domain-weighted to the exam blueprint)

Each mock is 60 questions, distributed by domain weight. The two mocks are independent (no shared items).

| Domain | Weight | Mock A | Mock B | File |
|---|---:|---:|---:|---|
| D1 — Agentic Architecture & Orchestration | 27% | 16 | 16 | [held-out_D1.md](held-out_D1.md) |
| D2 — Tool Design & MCP Integration | 18% | 11 | 11 | [held-out_D2.md](held-out_D2.md) |
| D3 — Claude Code Configuration & Workflows | 20% | 12 | 12 | [held-out_D3.md](held-out_D3.md) |
| D4 — Prompt Engineering & Structured Output | 20% | 12 | 12 | [held-out_D4.md](held-out_D4.md) |
| D5 — Context Management & Reliability | 15% | 9 | 9 | [held-out_D5.md](held-out_D5.md) |
| **Total** | **100%** | **60** | **60** | |

**Question IDs:** `A-D{n}-NN` = Mock A, Domain n; `B-D{n}-NN` = Mock B, Domain n. Each domain file holds its Mock-A questions, its Mock-B questions, then a separate Answer Key. To run **Mock A**, the Exam Coach pulls all `A-…` questions across the five files (60 total); for **Mock B**, all `B-…` (60 total).

**Style:** ~65% scenario / anti-pattern ("what's wrong with this design?" / "most effective fix?"), ~20% concept+application, ~15% recall — matching the real exam's judgment-over-recall weighting. Single best answer; distractors are plausible to a half-knowledgeable candidate. Each answer-key entry explains why the key is right and why each distractor fails.

**Scenario coverage:** the official exam has **6 scenarios** (Customer Support, Code Generation, Multi-Agent Research, Developer Productivity, Claude Code CI/CD, Structured Data Extraction). Questions are tagged to these. Some questions carry a "Conversational AI" tag — treat that as a multi-turn/context cross-domain framing, **not** a 7th official scenario. There is no Scenario 7 or 8 (the earlier community guide was wrong). For the most exam-accurate Mock #1, prefer the **official Skilljar practice exam**.

---

## How to run a mock (Exam Coach)

1. **Timed, sequential, no feedback during the exam.** Present questions one at a time; the learner answers before seeing the next. 60 questions / 120 minutes. Remind at 30 min and 10 min remaining.
2. **Do not reveal the answer key until all 60 are submitted.**
3. **Score against the full Go/No-Go gate** (see `academy/ENGAGEMENT-PROTOCOL.md`):
   - Total scaled-equivalent ≥ 720 (≈ 43/60), **AND**
   - No single domain below 70%, **AND**
   - No scenario family below 70%.
4. **Produce a domain-AND-scenario breakdown**, not just the total. A passing total with a failing domain/scenario floor → targeted remediation on that segment, then re-test it.
5. **Log results** to `academy/PROGRESS.md` (Mock Exam Scores) and weak items to `academy/GAPS.md` / `academy/LEARNER-MODEL.md`.

**Order:** Mock A at Session 35, Mock B at Session 37. Never run both back-to-back — Session 36 remediation sits between them. Once a mock has been taken, its questions are "burned" for prediction purposes; if a third attempt is needed, author a fresh held-out set rather than reusing these.

---

## Provenance

Authored by five parallel domain specialists, one per domain, each grounded only in `academy/CURRICULUM.md` (its domain), `EXAM-DIGEST.md`, and an explicit overlap-check against the existing `practice/` banks, checkpoints, `guide_en.MD` samples, and `SESSION-PLAN.md` teaching examples. Volatile facts (model IDs, hook roster, permission modes, MCP terms, scenario count) may drift — verify against live Anthropic docs / Skilljar before exam day, per the pre-mock verification step in `ENGAGEMENT-PROTOCOL.md`.
