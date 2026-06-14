# CCA-F Practice Bank

**Created:** 2026-06-09 · **51 original, exam-style questions** weighted to the real domain blueprint.

These are **original** scenario/anti-pattern questions authored against this project's verified materials (`EXAM-DIGEST.md` + the per-domain citation files), **not** copied from any third-party bank. The real exam over-weights "what's wrong with this design?" and scenario judgment over definition recall — so do these, not flashcards.

## The bank

| File | Domain | Exam weight | Questions |
|---|---|---|---|
| [`CCA-F_practice_d1-agentic-architecture.md`](CCA-F_practice_d1-agentic-architecture.md) | 1 — Agentic Architecture & Orchestration | 27% | 14 |
| [`CCA-F_practice_d2-claude-code.md`](CCA-F_practice_d2-claude-code.md) | 2 — Claude Code Configuration & Workflows | 20% | 10 |
| [`CCA-F_practice_d3-prompt-engineering.md`](CCA-F_practice_d3-prompt-engineering.md) | 3 — Prompt Engineering & Structured Output | 20% | 10 |
| [`CCA-F_practice_d4-tools-mcp.md`](CCA-F_practice_d4-tools-mcp.md) | 4 — Tool Design & MCP Integration | 18% | 9 |
| [`CCA-F_practice_d5-context-reliability.md`](CCA-F_practice_d5-context-reliability.md) | 5 — Context Management & Reliability | 15% | 8 |
| **Total** | | **100%** | **51** |

Each file: a **Questions** section (answer-free, so it supports genuine active recall) and an **Answer Key** with the correct letter, why the tempting distractor fails, the sub-topic, and a difficulty tag.

## Cross-domain integration checkpoints (do these AFTER the per-domain banks)

The exam's hardest items combine two domains in one scenario — and the course teaches domains in isolation. These three **integrative design checkpoints** force the combination: you design the architecture *cold* from memory, then compare against the model answer and the named cross-domain traps. They sit between the per-domain bank and the timed mock.

| File | Scenario | Domains | The collision it drills |
|---|---|---|---|
| [`CCA-F_checkpoint_A_support-agent_D1xD5.md`](CCA-F_checkpoint_A_support-agent_D1xD5.md) | 1 — Customer Support Agent | D1 × D5 | escalation + multi-turn compaction/caching (don't compact away the complaint the handoff needs; don't cache per-conversation content; escalate by category not fail-count) |
| [`CCA-F_checkpoint_B_ci-cd_D2xD3.md`](CCA-F_checkpoint_B_ci-cd_D2xD3.md) | 5 — Claude Code in CI/CD | D2 × D3 | headless flags + Structured-Outputs guarantee + reproducibility (`--bare`/auth coupling; a permission prompt hanging CI; prompt-only JSON in an unattended pipeline) |
| [`CCA-F_checkpoint_C_multi-agent-research_D1xD4.md`](CCA-F_checkpoint_C_multi-agent-research_D1xD4.md) | 3 — Multi-Agent Research | D1 × D4 | orchestration + tool/error design (raw dumps across the seam; subagent context isolation; tool-vs-resource; retrying uncertain writes; parallel-elapsed=max) |

> **Order:** per-domain banks → integration checkpoints (A/B/C) → timed mock. Integration *before* the mock, so the mock confirms rather than first-teaches.

## How to use (active recall, no peeking)

1. Pick a domain (start with **D1 — 27%**, the heaviest).
2. Answer **every** question before scrolling to the Answer Key. Write your letters down.
3. Score it. **Target ≥ 70% per domain** (the real exam is 720/1000 scaled).
4. For every miss, log it to [`../GAPS.md`](../GAPS.md): what was asked, what you picked, the correct mental model, the one-line pattern to remember.
5. Re-test a domain after a gap of a day+ (spaced repetition). Move a gap to "Resolved" only after 3 clean recalls.

> Want me to run any domain **live** as an interactive drill (I ask, you answer, I score + log gaps automatically)? Just say "run the D1 practice."

## External supplements (optional)
- **claudecertifications.com** — 25 practice Qs + 6 scenario walkthroughs + an 18-item anti-patterns cheatsheet: https://claudecertifications.com/claude-certified-architect *(their content — work it on their site; not reproduced here.)*
- **daronyondem/claude-architect-exam-guide** — the full guide these were grounded in (digested in [`../EXAM-DIGEST.md`](../EXAM-DIGEST.md)).

## Provenance
Authored 2026-06-09 by 5 parallel item-writers, one per domain, each grounded only in `EXAM-DIGEST.md` and that domain's verified `*_citations.md`. Volatile facts (model IDs, hook roster, permission modes, MCP scope renames) may drift — the citation files carry the `[VERIFY]` flags.
