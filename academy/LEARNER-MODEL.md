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
| D1.1 | Agentic loop fundamentals (`stop_reason`, stateless model) | ⚪ | — | — | |
| D1.2 | `AgentDefinition` + least privilege | ⚪ | — | — | |
| D1.3 | Hub-and-spoke / coordinator responsibilities | ⚪ | — | — | |
| D1.4 | `Task` tool + explicit context passing + parallel spawn | ⚪ | — | — | |
| D1.5 | Hooks (Pre/PostToolUse; deterministic vs probabilistic) ★ | ⚪ | — | — | |
| D1.6 | Escalation patterns + structured handoff ★ | ⚪ | — | — | |
| D1.7 | Session mgmt (`--resume`, `fork_session`) ★ | ⚪ | — | — | |
| D1.8 | Task decomposition (fixed vs dynamic; multi-pass) | ⚪ | — | — | |

### Domain 3 — Claude Code Configuration & Workflows (20%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D3.1 | CLAUDE.md hierarchy + `@path` imports | ⚪ | — | — | |
| D3.2 | Path-specific rules (`.claude/rules/`, glob `paths:`) | ⚪ | — | — | |
| D3.3 | Skills frontmatter (`context:fork`, `allowed-tools`, `argument-hint`) ★ | ⚪ | — | — | Watch the `allowed-tools` = pre-approve (not restrict) trap |
| D3.4 | Planning mode vs direct + Explore subagent | ⚪ | — | — | |
| D3.5 | `/compact` and `/memory` | ⚪ | — | — | |
| D3.6 | CI/CD: `-p` / `--bare` / `--output-format json` ★ | ⚪ | — | — | Watch the `-p` vs `--bare` trap |

### Domain 4 — Prompt Engineering & Structured Output (20%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D4.1 | Few-shot prompting (5 types) | ⚪ | — | — | |
| D4.2 | Explicit criteria vs vague instructions | ⚪ | — | — | |
| D4.3 | Prompt chaining (attention dilution) | ⚪ | — | — | |
| D4.4 | The "interview" pattern | ⚪ | — | — | |
| D4.5 | `tool_use` + JSON Schema (syntactic vs semantic) | ⚪ | — | — | |
| D4.6 | `tool_choice` (auto / any / forced) | ⚪ | — | — | |
| D4.7 | Syntax vs semantic errors | ⚪ | — | — | |
| D4.8 | Validation, retry-with-feedback, self-correction ★ | ⚪ | — | — | |
| D4.9 | Message Batches API ★ | ⚪ | — | — | |
| D4.10 | Multi-instance / multi-pass review ★ | ⚪ | — | — | |

### Domain 2 — Tool Design & MCP Integration (18%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D2.1 | Tool description as the selection mechanism ★ | ⚪ | — | — | |
| D2.2 | MCP fundamentals (tools / resources / prompts) | ⚪ | — | — | |
| D2.3 | MCP server config (`.mcp.json` vs `~/.claude.json`) | ⚪ | — | — | |
| D2.4 | `isError` structured errors (+ JSON-RPC vs tool-exec channel) ★ | ⚪ | — | — | Watch the two-error-channel trap |
| D2.5 | Tool allocation + `tool_choice` (too-many-tools problem) ★ | ⚪ | — | — | |
| D2.6 | Built-in tool selection + incremental investigation | ⚪ | — | — | |

### Domain 5 — Context Management & Reliability (15%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D5.1 | Context window risks (lost-in-the-middle, accumulation) | ⚪ | — | — | |
| D5.2 | Fact extraction + tool-result trimming + position-aware input | ⚪ | — | — | |
| D5.3 | Scratchpad files + structured state persistence ★ | ⚪ | — | — | |
| D5.4 | Confidence calibration + stratified sampling ★ | ⚪ | — | — | |
| D5.5 | Provenance preservation + conflicting data ★ | ⚪ | — | — | |

---

## 2. Reinforcement Queue (spaced repetition — read at session start)

> The Spaced-Repetition Flash and any gap-fill drills are drawn from the TOP of this queue.
> Rule: list everything whose **Next review due ≤ the upcoming session**, sorted weakest-first (🔴 → 🟡 → 🟢).

| Priority | Concept | State | Due | Why it's queued |
|---|---|---|---|---|
| — | *(empty — program not started)* | — | — | Populate after the first genuine comprehension check |

---

## 3. Strengths (anchor new teaching to these)

> Concepts Ram reliably nails (🟢 / ✅). Use them as the *known* side of a new analogy — bridge from a strength to a new concept.

- *(none recorded yet)*

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

- *(none recorded yet — add the first entry after Session 1's baseline diagnostic)*
- **Known context to leverage:** Ram is a Solution Architect at Infosys (Claude Partner) with hands-on agent/Claude Code experience. Prefer enterprise-delivery and systems-architecture analogies over consumer ones; he can reason from real production trade-offs.

---

## 6. Domain Confidence Summary (recompute at each sign-off)

> One-line read of where the program stands per domain. Used for Go/No-Go judgement alongside mock scores.

| Domain | Weight | Concepts ✅/🟢 | Concepts 🟡 | Concepts 🔴 | Untested | Read |
|---|---|---|---|---|---|---|
| D1 | 27% | 0 | 0 | 0 | 8 | Not started |
| D2 | 18% | 0 | 0 | 0 | 6 | Not started |
| D3 | 20% | 0 | 0 | 0 | 6 | Not started |
| D4 | 20% | 0 | 0 | 0 | 10 | Not started |
| D5 | 15% | 0 | 0 | 0 | 5 | Not started |
