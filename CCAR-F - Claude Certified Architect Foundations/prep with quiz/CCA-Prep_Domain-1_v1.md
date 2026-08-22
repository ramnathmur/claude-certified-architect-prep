# Domain 1: Agentic Architecture & Orchestration (27%)

**Source:** guide_en.MD — Chapters 1–3, Scenario: Multi-agent Research System  
**Version:** 1.0 | 2026-06-27

---

## 1.1 The Agentic Loop

### Core Concept
An agentic loop is a sequence of API calls where Claude's response drives the next action. The orchestrator inspects `stop_reason` after each call to decide whether to continue or stop.

### `stop_reason` Values
| Value | Meaning | Action |
|---|---|---|
| `end_turn` | Claude finished its response | Stop the loop; return output to user |
| `tool_use` | Claude wants to call a tool | Execute the tool; append result; call Claude again |
| `max_tokens` | Response hit token limit | Handle gracefully — may need to continue |
| `stop_sequence` | A custom stop sequence was hit | Application-defined behavior |

**Exam pattern:** "What determines when to stop the agent loop?" → Check `stop_reason`, not text content, not iteration count.

### Agent Loop Structure
```
1. Send message to Claude (with tools available)
2. Receive response
3. If stop_reason == "tool_use":
   a. Extract tool_use content blocks
   b. Execute each tool
   c. Append tool_result blocks to messages
   d. Loop back to step 1
4. If stop_reason == "end_turn": return final text to user
```

---

## 1.2 Hub-and-Spoke (Coordinator-Subagent) Architecture

### Core Concept
One coordinator agent orchestrates multiple specialized subagents. Subagents never communicate directly with each other — all inter-agent communication flows through the coordinator.

### Why Hub-and-Spoke
- **Visibility:** The coordinator observes all interactions
- **Uniform error handling:** Coordinator decides retry vs skip vs escalate
- **Information control:** Coordinator decides what context each subagent receives
- **Separation of responsibilities:** Each subagent has a narrow, well-defined scope

### Spawning Subagents: The `Task` Tool
- Subagents are spawned by including `"Task"` in the coordinator's `allowedTools`
- Each `Task` call is an independent agent with its own context
- Multiple `Task` calls in a single response = **parallel execution**
- The coordinator aggregates results when all `Task` calls complete

### Context Passing Principle
Subagents have **isolated context** — they do not see the coordinator's conversation history unless the coordinator explicitly includes it in the subagent's prompt.

**Exam pattern:** "The synthesis agent lacks context about what the web-search agent found" → coordinator must pass results explicitly in the subagent prompt.

---

## 1.3 Task Decomposition

### The Coordinator's Most Critical Responsibility
If the coordinator decomposes a task too narrowly, subagents execute correctly but cover the wrong ground. Root cause = coordinator prompt, not subagent performance.

**Exam scenario:** Research system asked about "AI impact on creative industries" — coordinator decomposes into only visual art subtasks. Every subagent returns correct results. Output misses music, literature, film.
- ✅ Root cause: **coordinator's task decomposition was too narrow**
- ❌ Not: web-search agent query quality, synthesis agent gap detection, document analysis filters

### Partitioning Principle
The coordinator must **explicitly partition the research space** before delegating — assign distinct subtopics or source types to each agent. This prevents duplication and missed coverage.

**Exam pattern:** Two agents investigate the same subtopics → tokens wasted, no extra depth. Fix: coordinator partitions before delegating, not deduplication after.

---

## 1.4 Error Propagation in Multi-Agent Systems

### Principle: Structured Error Context
When a subagent fails, it must return **structured error context** to the coordinator — not a generic failure status, not silence.

Required error payload:
- **Failure type** (timeout vs syntax error vs access denied)
- **What was attempted** (query string, parameters used)
- **Partial results** (whatever was completed before failure)
- **Potential alternatives** (retry with different query? alternative source?)

**Why:** The coordinator needs this to make intelligent recovery decisions — retry, reroute, continue with partial results, or escalate.

### Distinguishing Error Types
| Error Type | Recovery | Example |
|---|---|---|
| Transient (timeout, network) | Retry with same/modified params | Patent database timeout |
| Permanent (syntax, auth) | Don't retry; log and continue | Malformed query string |
| Valid empty result | Accept as finding | "0 results" from industry reports |

**Exam trap:** "0 results" ≠ failure. It's a valid, informative response. Distinguish from a timeout (access failure requiring retry decision).

### Where to Handle Errors
- **At the subagent level:** Transient failures the subagent can resolve (retry + backoff)
- **Escalate to coordinator:** Errors the subagent cannot resolve — with full context and partial progress
- **Never:** Catch and silently return success. Never terminate the entire workflow for one subagent failure.

---

## 1.5 Coverage Annotations (Graceful Degradation)

When upstream inputs are incomplete (some sources timed out, some succeeded), the synthesis agent should:
1. Complete synthesis using available data
2. **Annotate coverage** — mark which conclusions are well-supported vs where gaps exist
3. Propagate uncertainty upward

**Exam pattern:** "Web search returned 3/5 source categories — what should synthesis agent do?"
- ✅ Structure output with coverage annotations showing where data is missing
- ❌ Return error because input is incomplete
- ❌ Proceed without noting the gaps

---

## 1.6 Least Privilege for Subagent Tools

Each subagent should have **only the tools it needs** for its defined scope.

**Exam scenario:** Synthesis agent needs to verify 85% simple facts, 15% complex research.
- ✅ Give synthesis agent a limited `verify_fact` tool for simple checks; route complex verification through coordinator
- ❌ Give synthesis agent full web-search access (breaks separation of responsibilities)
- ❌ Batch all verification to end (blocking — later synthesis steps may need earlier verified facts)

**Exam scenario:** Document analysis agent given `fetch_url` starts doing ad-hoc web search.
- ✅ Replace `fetch_url` with `load_document` that validates URL points to document format (fixes root cause at interface level)
- ❌ Add prompt instructions to not use `fetch_url` for search (probabilistic, not deterministic)

---

## 1.7 When to Escalate to Human

Escalation is warranted when:
1. **Policy gap** — agent cannot determine what the correct action is within defined policies
2. **Explicit user request** — user asks to speak with a human
3. **Unable to make progress** — multiple retries failed, cannot resolve the task
4. **High-stakes ambiguity** — wrong decision could cause significant harm

**Exam pattern:** Customer requests competitor price matching. Policy covers own-site price drops but says nothing about competitors.
- ✅ Escalate — policy interpretation required; agent must not invent policy
- ❌ Apply own-site pricing rules (wrong interpretation)
- ❌ Refuse with "we don't match competitor prices" (not stated in policy)

---

## 1.8 Critical Sequencing and Preconditions

When correct sequencing is mandatory (e.g., verify identity before taking action), use **programmatic preconditions** — not prompt instructions.

**Exam scenario:** Support agent skips `get_customer` and calls `lookup_order` directly using customer-provided order number. Wrong account selected 15% of the time.
- ✅ Programmatic precondition: block `lookup_order` until `get_customer` returns verified identifier
- ❌ Strengthen system prompt to always call `get_customer` first (probabilistic)
- ❌ Few-shot examples showing correct sequence (probabilistic)

**Principle:** For security-critical sequencing, enforce at code level, not at prompt level.

---

## 1.9 Parallel Execution

Multiple `Task` calls in a single coordinator response execute in parallel. Use this for:
- Independent research tasks
- Multi-issue customer requests
- Multi-dimensional analysis

**Exam pattern:** Complex billing dispute (billed twice + discount not applied + cancel order):
- ✅ Decompose into 3 separate issues, investigate in parallel with shared customer context, synthesize resolution
- ❌ Sequential investigation (high tool-call count, redundant data fetching)

---

## 1.10 Independent Review Instances

To avoid confirmation bias in automated review/generation:
- Run a **second independent instance** with no access to the first instance's reasoning
- This mirrors human peer review — fresh perspective catches what the author rationalized away

**Exam pattern:** Claude Code generates code, considers edge cases in reasoning, concludes its approach is correct. Non-obvious bugs only caught in PR review.
- ✅ Second independent Claude Code instance reviews changes without seeing generator's reasoning
- ❌ Extended thinking on the generation stage (doesn't fix the self-check limitation)
- ❌ Add self-review instructions to generation prompt (same instance, same confirmation bias)

---

## 1.11 Key Architecture Patterns (Named)

| Pattern | Description |
|---|---|
| Hub-and-spoke | Central coordinator + specialized subagents; no direct inter-agent comms |
| Agentic loop | stop_reason-driven API loop; tool_use → execute → continue; end_turn → stop |
| Parallel execution | Multiple Task calls in one coordinator response |
| Context isolation | Subagents receive only what coordinator explicitly passes |
| Evaluator-optimizer | Two-stage: generator → independent critic/reviewer |
| Structured error propagation | Failure type + attempted params + partial results + alternatives |
| Coverage annotation | Synthesis marks which conclusions are well-supported vs data-gap |
| Least-privilege tooling | Each agent gets minimum tools needed for its scope |
