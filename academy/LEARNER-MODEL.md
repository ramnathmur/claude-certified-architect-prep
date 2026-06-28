# CCA-F Academy — Learner Model

**This is the Professor's persistent memory of Ram across the whole program.**
Read it at the **start** of every session. Update it at **every comprehension check** and at **sign-off**.

It answers, at any moment:
- Where is Ram **weak**? (🔴 in the Mastery Ledger)
- Where is he **strong**? (🟢 / ✅ in the Mastery Ledger + the Strengths list)
- What needs **reinforcement now**? (the Reinforcement Queue)
- Which concepts are **interlinked**? (the Interlink Map — use these to bridge new teaching)
- What durable **insights** about how he learns can improve later sessions? (the Insight Log)

> **Audience:** AI system only (non-human-facing working memory). Mechanics — the mastery state machine and review intervals — are defined in `ENGAGEMENT-PROTOCOL.md → Cross-Session Memory`.
> **Honesty rule:** synthetic / self-driven runs (see `GAPS.md`) do **NOT** count toward mastery. A concept only leaves ⚪ Untested after a genuine, learner-produced answer.

---

## Legend

| State | Meaning | How it is reached |
|---|---|---|
| ⚪ Untested | Never genuinely assessed | Default / only synthetic data exists |
| 🔴 Weak | Missed on the most recent check | Any state drops to 🔴 on a miss (even a prior 🟢) |
| 🟡 Developing | Right idea but needed prompting, OR 1 clean recall | — |
| 🟢 Strong | 2 clean unprompted recalls on **different** sessions | Spacing required |
| ✅ Exam-ready | 3 clean recalls across ≥2 sessions | Retires from active queue; final-week sweep only |

**Review intervals → "Next review due":** 🔴 next session · 🟡 in 1–2 sessions · 🟢 in ~3 sessions / ~1 week · ✅ final-week sweep.

---

## 1. Mastery Ledger

*Status at program start: all ⚪ Untested. The 2026-06-06 "synthetic batch run" in `GAPS.md` is excluded by the honesty rule.*

### Domain 1 — Agentic Architecture & Orchestration (27%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D1.1 | Agentic loop fundamentals (`stop_reason`, stateless model) | 🟢 | 2026-06-27 | Session 5 | 2 clean recalls: named stop_reason (S2); classified all 3 exit conditions correctly with reasoning (S3) |
| D1.2 | `AgentDefinition` + least privilege | ⚪ | — | — | |
| D1.3 | Hub-and-spoke / coordinator responsibilities | 🟡 | 2026-06-27 | Session 5 | Explicit context passing correct (S4); coordinator responsibilities: decompose/delegate/aggregate/error/user ✓; context isolation demonstrated implicitly — confirm vocabulary next session |
| D1.4 | `Task` tool + explicit context passing + parallel spawn | ⚪ | — | — | |
| D1.5 | Hooks (Pre/PostToolUse; deterministic vs probabilistic) ★ | ⚪ | — | — | |
| D1.6 | Escalation patterns + structured handoff ★ | ⚪ | — | — | |
| D1.7 | Session mgmt (`--resume`, `fork_session`) ★ | ⚪ | — | — | |
| D1.8 | Task decomposition (fixed vs dynamic; multi-pass) | ⚪ | — | — | |

### Domain 3 — Claude Code Configuration & Workflows (20%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D3.1 | CLAUDE.md hierarchy + `@path` imports | 🔴 | 2026-06-27 | Session 2 | Knows global+project levels; traversal, @path, rules/ unknown |
| D3.2 | Path-specific rules (`.claude/rules/`, glob `paths:`) | ⚪ | — | — | |
| D3.3 | Skills frontmatter (`context:fork`, `allowed-tools`, `argument-hint`) ★ | ⚪ | — | — | Watch the `allowed-tools` = pre-approve (not restrict) trap |
| D3.4 | Planning mode vs direct + Explore subagent | ⚪ | — | — | |
| D3.5 | `/compact` and `/memory` | ⚪ | — | — | |
| D3.6 | CI/CD: `-p` / `--bare` / `--output-format json` ★ | 🔴 | 2026-06-27 | Session 14 | "Headless" concept unknown — stated directly |

### Domain 4 — Prompt Engineering & Structured Output (20%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D4.1 | Few-shot prompting (5 types) | 🟡 | 2026-06-27 | Session 3 | Correct concept; "demonstrates a pattern" vs "describes in words" distinction not articulated |
| D4.2 | Explicit criteria vs vague instructions | ⚪ | — | — | |
| D4.3 | Prompt chaining (attention dilution) | ⚪ | — | — | |
| D4.4 | The "interview" pattern | ⚪ | — | — | |
| D4.5 | `tool_use` + JSON Schema (syntactic vs semantic) | 🔴 | 2026-06-27 | Session 2 | stop_reason cycle unknown; answered from user-facing perspective, not API layer |
| D4.6 | `tool_choice` (auto / any / forced) | ⚪ | — | — | |
| D4.7 | Syntax vs semantic errors | ⚪ | — | — | |
| D4.8 | Validation, retry-with-feedback, self-correction ★ | ⚪ | — | — | |
| D4.9 | Message Batches API ★ | ⚪ | — | — | |
| D4.10 | Multi-instance / multi-pass review ★ | ⚪ | — | — | |

### Domain 2 — Tool Design & MCP Integration (18%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D2.1 | Tool description as the selection mechanism ★ | 🔴 | 2026-06-27 | Session 2 | Core selection role understood; misconception: treats description as lazy-load gating, not always-present context |
| D2.2 | MCP fundamentals (tools / resources / prompts) | 🔴 | 2026-06-27 | Session 2 | USB analogy correct; three primitives, JSON-RPC, server config unknown |
| D2.3 | MCP server config (`.mcp.json` vs `~/.claude.json`) | ⚪ | — | — | |
| D2.4 | `isError` structured errors (+ JSON-RPC vs tool-exec channel) ★ | ⚪ | — | — | Watch the two-error-channel trap |
| D2.5 | Tool allocation + `tool_choice` (too-many-tools problem) ★ | ⚪ | — | — | |
| D2.6 | Built-in tool selection + incremental investigation | ⚪ | — | — | |

### Domain 5 — Context Management & Reliability (15%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D5.1 | Context window risks (lost-in-the-middle, accumulation) | 🔴 | 2026-06-27 | Session 2 | Symptom (things get buried) right; positional-bias mechanism wrong; described as temporal drift not positional |
| D5.2 | Fact extraction + tool-result trimming + position-aware input | ⚪ | — | — | Note: prompt caching also unknown (assessed indirectly via Q10) |
| D5.3 | Scratchpad files + structured state persistence ★ | ⚪ | — | — | |
| D5.4 | Confidence calibration + stratified sampling ★ | ⚪ | — | — | |
| D5.5 | Provenance preservation + conflicting data ★ | ⚪ | — | — | |

---

## 2. Reinforcement Queue (spaced repetition — read at session start)

> The Spaced-Repetition Flash and any gap-fill drills are drawn from the TOP of this queue.
> Rule: list everything whose **Next review due ≤ the upcoming session**, sorted weakest-first (🔴 → 🟡 → 🟢).

| Priority | Concept | State | Due | Why it's queued |
|---|---|---|---|---|
| 1 | D1.3 — Context isolation vocab ("clean context window") | 🟡 | Session 5 | Demonstrated understanding; confirm the explicit term next session SR flash |
| 2 | D1.1 — `stop_reason` anti-patterns (confirm 🟢) | 🟢 | Session 5 | 2 clean recalls — SR flash to confirm retention after gap |
| 3 | D2.1 — Tool description as selection mechanism | 🔴 | Session 10 | Lazy-loading misconception — teach when D2 block opens |
| 4 | D2.2 — MCP fundamentals (3 primitives) | 🔴 | Session 10 | Surface only; teach from scratch in D2 block |
| 5 | D3.1 — CLAUDE.md hierarchy + traversal | 🔴 | Session 10 | Surface level; teach in D3 block |
| 6 | D4.1 — Few-shot: pattern demonstration vs description | 🟡 | Session 16 | Right concept; mechanism not articulated — address in D4 block |
| 7 | D4.5 — `stop_reason` / tool_use API cycle (D4 angle) | 🔴 | Session 17 | Unknown from D4 angle (JSON schema, tool_choice) — address in D4 block |
| 8 | D5.1 — Lost-in-middle mechanism (positional bias) | 🔴 | Session 27 | Right symptom, wrong mechanism — teach in D5 block |
| 9 | D3.6 — CI/CD headless / `-p` flag | 🔴 | Session 14 | Fully unknown — teach from scratch in D3 block |

---

## 3. Strengths (anchor new teaching to these)

> Concepts Ram reliably nails (🟢 / ✅). Use them as the *known* side of a new analogy — bridge from a strength to a new concept.

- D1.1 — Agentic loop (🟢 — stop_reason cycle, stateless model, anti-patterns all confirmed)
- D1.3 — Orchestrator/subagent + explicit context passing (🟡 — confirm context isolation vocab at S5)

---

## 4. Concept Interlink Map

> When teaching a new concept, link it to a strong prior one — this is exactly what the exam's cross-domain scenarios test. Add a row whenever a genuine connection surfaces in a session.

| Concept A | ↔ | Concept B | The bridge to say out loud |
|---|---|---|---|
| Hooks — `PreToolUse` (D1.5) | ↔ | Escalation (D1.6) | "A PreToolUse hook that blocks a >$500 refund and an escalation are the two halves of the same decision: stop the unsafe action, hand it to a human." |
| Hooks — `PostToolUse` (D1.5) | ↔ | Tool-result trimming (D5.2) | "Trimming a 40-field order down to 5 is a context technique (D5) *implemented* with a D1 mechanism — same hook, different goal." |
| Determinism: hooks + preconditions (D1.5) | ↔ | Structured Outputs / `tool_use` (D4.5) | "Guarantee at the source, not by asking nicely — hooks for actions, schemas for output. Prompts are probabilistic; both of these are deterministic." |
| Tool descriptions (D2.1) | ↔ | Tool selection reliability + system-prompt associations (D1/D2.5) | "The description is how the model picks; the system prompt can quietly bias that pick. Same failure (wrong tool), two root causes." |
| Coordinator context isolation (D1.3/D1.4) | ↔ | Scratchpad + state persistence (D5.3) | "Subagents don't inherit history, so you pass context explicitly — and a scratchpad is how the coordinator remembers across that boundary." |
| Batch API (D4.9) | ↔ | CI/CD sync-vs-batch (D3.6) + no multi-turn tool calling (D2) | "Batch = 50% off but up to 24h and no mid-request tool loop → great for overnight audits, fatal for a blocking pre-merge check." |
| Lost-in-the-middle (D5.1) | ↔ | Position-aware multi-agent synthesis (D1.3) | "Key findings go at the TOP of the aggregated input — the same lost-in-the-middle rule that bites a single prompt bites the synthesis agent." |
| `isError` structured errors (D2.4) | ↔ | Error propagation to coordinator (D1/D5.3) | "A good `isError` payload (type, retryable, partial results) is what lets the coordinator decide retry vs escalate vs continue-with-gaps." |

---

## 5. Cross-Session Insight Log

> Durable observations about HOW Ram learns — which analogy domains land, recurring confusions, pacing, and where his real Infosys/solution-architect experience can be used as an anchor. Each entry: date · observation · how to apply it next time.

- **2026-06-27 — Systems-first thinker.** Ram's D1 answers described architecture (what talks to what, who persists, who is responsible) before mechanics. He'll absorb "why does this design exist" before "what is the syntax." Lead with design intent, not API detail.
- **2026-06-27 — Self-generated analogies.** He independently reached the USB analogy for MCP — the canonical one. When he reaches for an analogy himself, affirm it and build on it rather than replacing it.
- **2026-06-27 — Clear metacognition on gaps.** Said "I do not know" directly for headless and prompt caching rather than guessing. Trustworthy signal — his 🟡s are genuine partial knowledge, not bluffing.
- **2026-06-27 — Gap pattern: conceptual vs. technical.** Consistently strong on the "what it is and why" layer; consistently missing the "how the API actually signals it" layer (stop_reason, tool_use content blocks, cache_control fields). Bridge from his concept to the API shape. **UPDATE (S2–S4):** Technical layer is absorbing quickly once taught — stop_reason retained cleanly across two sessions same day. Gap pattern may narrow faster than expected.
- **2026-06-27 — Responds well to "what breaks if..."** His best answers came from failure-mode questions (stateless context drop, Analyst with no facts). Use this pattern: teach the mechanism, then ask what breaks if it's missing. He reasons from consequences, not from definitions.
- **Known context to leverage:** Ram is a Solution Architect at Infosys (Claude Partner) with hands-on agent/Claude Code experience. Prefer enterprise-delivery and systems-architecture analogies over consumer ones; he can reason from real production trade-offs.

---

## 6. Domain Confidence Summary (recompute at each sign-off)

> One-line read of where the program stands per domain. Used for Go/No-Go judgement alongside mock scores.

| Domain | Weight | Concepts ✅/🟢 | Concepts 🟡 | Concepts 🔴 | Untested | Read |
|---|---|---|---|---|---|---|
| D1 | 27% | 1 | 1 | 0 | 6 | After S2–S4: D1.1 🟢 (loop + stop_reason + anti-patterns); D1.3 🟡 (hub-and-spoke + context passing); D1.2/4/5/6/7/8 untested |
| D2 | 18% | 0 | 0 | 2 | 4 | Baseline: 🔴 — USB/MCP surface only; lazy-load misconception on D2.1 |
| D3 | 20% | 0 | 0 | 2 | 4 | Baseline: 🔴 — CLAUDE.md surface; headless mode unknown |
| D4 | 20% | 0 | 1 | 1 | 8 | Baseline: 🔴 — few-shot partial; stop_reason cycle unknown |
| D5 | 15% | 0 | 0 | 1 | 4 | Baseline: 🔴 — symptom right, mechanism wrong; caching unknown |
