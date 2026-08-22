# Domain 1: Agentic Architecture & Orchestration (27%)

**Source:** guide_en.MD — Chapters 1–3, 5.10, 8, 9.3, Scenario: Multi-agent Research System; CCA-F Official Exam Guide — Task Statements 1.1–1.7  
**Version:** 2.0 | 2026-07-06  
**Changelog v2:** Added §1.3 (AgentDefinition Configuration), §1.4 (Goal-Oriented vs Procedural Coordinator Prompts), §1.5 (Structured Context Passing & Attribution), §1.7 (Fixed Pipelines vs Dynamic Adaptive Decomposition), §1.8 (Coordinator Iterative Refinement Loop), §1.13 (Structured Handoff Protocols), §1.16 (Session Management: Resume, Fork, Fresh Start). Renumbered v1 sections accordingly; extended pattern table (§1.18). All v1 content retained.

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

## 1.3 AgentDefinition Configuration

### Core Concept
`AgentDefinition` is the agent configuration object in the Claude Agent SDK. Every subagent type is defined by its **description**, **system prompt**, and **tool restrictions** — the three levers that shape what an agent is, how it behaves, and what it can touch.

```python
agent = AgentDefinition(
    name="customer_support",
    description="Handles customer requests for returns and order issues",
    system_prompt="You are a customer support agent...",
    allowed_tools=["get_customer", "lookup_order", "process_refund", "escalate_to_human"],
)
```

### Key Parameters
| Parameter | Role |
|---|---|
| `name` / `description` | Identification; the description tells the orchestration layer what this agent type is for |
| `system_prompt` | Behavioral instructions for the agent |
| `allowed_tools` | Whitelist of tools — enforce least privilege per subagent type |

### The Coordinator Requirement
A coordinator's `allowedTools` **must include `"Task"`** — without it, the coordinator cannot spawn subagents at all:

```python
coordinator_agent = AgentDefinition(
    allowed_tools=["Task", "get_customer"]
)
```

**Exam pattern:** "Coordinator never delegates; it attempts everything itself" →
- ✅ Check that `"Task"` is present in the coordinator's `allowedTools`
- ❌ Rewrite the coordinator's system prompt to instruct it to delegate (the prompt cannot grant a tool the configuration withholds)
- ❌ Add subagent descriptions to the coordinator's system prompt (descriptions don't enable spawning; the `Task` tool does)

**Exam pattern:** "Each subagent type should be given the full tool set for flexibility" →
- ❌ Wrong — tool restrictions per subagent type ARE the mechanism for separation of responsibilities and least privilege (see §1.11)

---

## 1.4 Coordinator Prompts: Goal-Oriented vs Procedural

### Core Concept
Coordinator prompts should specify **research goals and quality criteria**, NOT step-by-step procedural instructions. Goal-oriented prompts let subagents adapt their approach as findings emerge; procedural prompts lock the system into a fixed script that breaks when reality deviates from it.

| Prompt style | Example | Effect |
|---|---|---|
| **Goal-oriented ✅** | "Produce a comprehensive, cited overview of AI's impact on the music industry. Quality criteria: ≥3 independent sources per claim, coverage of production, distribution, and composition." | Subagents adapt search strategy to what they discover |
| **Procedural ❌** | "Step 1: search 'AI music'. Step 2: open the first 5 results. Step 3: summarize each in 100 words..." | Brittle; fails when step results don't match expectations; no adaptability |

**Why:** This is model-driven decision-making (the same principle as the agentic loop, §1.1) applied at the orchestration level — Claude reasons about the next action based on context, rather than executing a pre-configured decision tree.

**Exam pattern:** "Research coordinator produces shallow, checklist-like results" →
- ✅ Rewrite the coordinator prompt to state goals and quality criteria, letting it decide decomposition dynamically
- ❌ Add more detailed step-by-step instructions (deepens the rigidity that caused the problem)
- ❌ Increase the number of subagents (more agents executing a bad script doesn't fix the script)

---

## 1.5 Structured Context Passing & Attribution

### Core Concept
When passing context between agents, use **structured data formats that separate content from metadata** (source URLs, document names, page numbers). This preserves attribution through the pipeline — without it, "claim → source" mappings are lost during aggregation and summarization.

```json
{
  "content": "AI-generated music revenue grew 300% in 2024",
  "metadata": {
    "source_url": "https://example.com/report",
    "document_name": "Music Industry Annual Report",
    "page_number": 42,
    "retrieved_date": "2026-06-15"
  }
}
```

### Rules
- Include **complete findings** from prior agents directly in the subagent's prompt (e.g., pass web-search results AND document-analysis outputs to the synthesis subagent)
- Require subagents to include metadata (dates, sources) in their structured outputs
- On conflicting statistics between sources: preserve **both** values with attribution and annotate the conflict — let the coordinator decide; never arbitrarily pick one

**Exam pattern:** "Final report contains claims but citations are wrong or missing" →
- ✅ Root cause: content and metadata were passed as merged free text; attribution was lost in aggregation. Fix: structured format separating content from source metadata
- ❌ Instruct the synthesis agent to "remember to cite sources" (it cannot cite metadata it never received in structured form)
- ❌ Have the report agent re-search the web to find sources for each claim (duplicated work, may attribute to wrong sources)

---

## 1.6 Task Decomposition

### The Coordinator's Most Critical Responsibility
If the coordinator decomposes a task too narrowly, subagents execute correctly but cover the wrong ground. Root cause = coordinator prompt, not subagent performance.

**Exam scenario:** Research system asked about "AI impact on creative industries" — coordinator decomposes into only visual art subtasks. Every subagent returns correct results. Output misses music, literature, film.
- ✅ Root cause: **coordinator's task decomposition was too narrow**
- ❌ Not: web-search agent query quality, synthesis agent gap detection, document analysis filters

### Partitioning Principle
The coordinator must **explicitly partition the research space** before delegating — assign distinct subtopics or source types to each agent. This prevents duplication and missed coverage.

**Exam pattern:** Two agents investigate the same subtopics → tokens wasted, no extra depth. Fix: coordinator partitions before delegating, not deduplication after.

---

## 1.7 Decomposition Strategy: Fixed Pipelines vs Dynamic Adaptive

### Core Concept
Two named decomposition patterns — choosing the right one is an exam skill:

| Pattern | Structure | When to use |
|---|---|---|
| **Fixed sequential pipeline (prompt chaining)** | Steps defined in advance: `Document → Metadata extraction → Data extraction → Validation → Enrichment → Output` | Task structure is predictable; all steps known up front; stability and reproducibility needed (e.g., reviews that always follow the same template) |
| **Dynamic adaptive decomposition** | Subtasks generated from intermediate findings | Open-ended investigation; full scope unknown up front; each step depends on the previous step's results |

### Adaptive Investigation Plans
Adaptive decomposition generates subtasks from discoveries at each step:

```
1. "Add tests for a legacy codebase"
2. → First: map the structure (Glob, Grep)
3. → Found: 3 modules with no tests, 2 with partial coverage
4. → Prioritize: start with the payments module (high risk)
5. → During work: discovered a dependency on an external API
6. → Adapt: add a mock for the external API before writing tests
```

Pattern: **map structure first → identify high-impact areas → create a prioritized plan that adapts as dependencies are discovered.**

### Multi-pass Code Review (Prompt Chaining Applied)
For PRs with 10+ files, split into per-file local passes plus a separate cross-file integration pass:

```
Pass 1 (per-file): analyze each file individually → local issues
Pass 2 (integration): analyze relationships → cross-file issues
  (inconsistent types, circular dependencies)
```

**Why a single pass over 14 files fails:** attention dilution (deep on some files, shallow on others), inconsistent comments (pattern flagged in one file, approved in another), missed bugs from cognitive overload.

**Exam pattern:** "Which decomposition for an open-ended task like 'add comprehensive tests to a legacy codebase'?" →
- ✅ Dynamic adaptive: map first, prioritize, adapt the plan as dependencies surface
- ❌ Fixed pipeline with predetermined steps (scope is unknown up front; a fixed script can't react to discoveries)
- ❌ One giant single-pass prompt covering everything (attention dilution)

**Exam pattern:** "Which decomposition for a review that always follows the same template?" →
- ✅ Fixed sequential pipeline / prompt chaining (predictable, reproducible)
- ❌ Dynamic decomposition (unnecessary complexity for a predictable structure)

---

## 1.8 Coordinator Iterative Refinement Loop

### Core Concept
Synthesis is not necessarily one-shot. The coordinator runs a **refinement loop**:

```
1. Delegate research → subagents return findings
2. Invoke synthesis subagent
3. Coordinator EVALUATES synthesis output for gaps
4. If gaps found: RE-DELEGATE to search/analysis subagents
   with TARGETED queries aimed at the specific gaps
5. RE-INVOKE synthesis with the enriched findings
6. Repeat until coverage is sufficient
```

The coordinator owns gap evaluation and loop termination — this is part of its aggregation-and-validation responsibility (§1.2), not the synthesis agent's job.

**Exam pattern:** "Synthesis output has coverage gaps — what should the architecture do?" →
- ✅ Coordinator evaluates output, re-delegates targeted queries to search/analysis agents, re-invokes synthesis until coverage is sufficient
- ❌ Have the synthesis agent search the web itself to fill the gaps (breaks separation of responsibilities and least-privilege tooling, §1.11)
- ❌ Ship the report and note "further research needed" when re-delegation is available (coverage annotation is for *unrecoverable* gaps, §1.10 — not a substitute for the refinement loop)
- ❌ Loop indefinitely without a sufficiency criterion (coordinator needs defined quality criteria — see §1.4 — to know when to stop)

---

## 1.9 Error Propagation in Multi-Agent Systems

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

## 1.10 Coverage Annotations (Graceful Degradation)

When upstream inputs are incomplete (some sources timed out, some succeeded), the synthesis agent should:
1. Complete synthesis using available data
2. **Annotate coverage** — mark which conclusions are well-supported vs where gaps exist
3. Propagate uncertainty upward

**Exam pattern:** "Web search returned 3/5 source categories — what should synthesis agent do?"
- ✅ Structure output with coverage annotations showing where data is missing
- ❌ Return error because input is incomplete
- ❌ Proceed without noting the gaps

---

## 1.11 Least Privilege for Subagent Tools

Each subagent should have **only the tools it needs** for its defined scope.

**Exam scenario:** Synthesis agent needs to verify 85% simple facts, 15% complex research.
- ✅ Give synthesis agent a limited `verify_fact` tool for simple checks; route complex verification through coordinator
- ❌ Give synthesis agent full web-search access (breaks separation of responsibilities)
- ❌ Batch all verification to end (blocking — later synthesis steps may need earlier verified facts)

**Exam scenario:** Document analysis agent given `fetch_url` starts doing ad-hoc web search.
- ✅ Replace `fetch_url` with `load_document` that validates URL points to document format (fixes root cause at interface level)
- ❌ Add prompt instructions to not use `fetch_url` for search (probabilistic, not deterministic)

---

## 1.12 When to Escalate to Human

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

## 1.13 Structured Handoff Protocols (Mid-Process Escalation)

### Core Concept
Escalating mid-process is not just calling `escalate_to_human` — the agent must compile a **structured handoff summary**. The human agent **does not have access to the conversation transcript**; the summary is everything they see, so it must be complete and self-contained.

### Required Handoff Payload
```json
{
  "customer_id": "CUST-12345",
  "customer_name": "Ivan Petrov",
  "issue_summary": "Refund request for a damaged item",
  "order_id": "ORD-67890",
  "root_cause": "Item arrived damaged; photos attached",
  "actions_taken": [
    "Verified customer via get_customer",
    "Confirmed order via lookup_order",
    "Offered a standard replacement — customer insists on a refund"
  ],
  "refund_amount": "$89.99",
  "recommended_action": "Approve a full refund",
  "escalation_reason": "Customer requested to speak with a manager"
}
```

Core fields the exam names: **customer ID, root cause analysis, refund/amount, recommended action** — plus actions already taken and the escalation reason.

**Exam pattern:** "Human agents receiving escalations keep re-asking customers for information the AI agent already collected" →
- ✅ Root cause: escalation passed only a generic flag or free-text note; fix: structured handoff summary with customer ID, root cause, amount, actions taken, and recommended action
- ❌ Give human agents access to the raw transcript (they lack transcript access by design; and a raw transcript forces re-reading the entire conversation)
- ❌ Have the human agent re-run the AI agent's tools to rebuild context (duplicated work, slower resolution)
- ❌ Escalate earlier so less context accumulates (doesn't fix the information loss; degrades autonomous resolution rate)

---

## 1.14 Critical Sequencing and Preconditions

When correct sequencing is mandatory (e.g., verify identity before taking action), use **programmatic preconditions** — not prompt instructions.

**Exam scenario:** Support agent skips `get_customer` and calls `lookup_order` directly using customer-provided order number. Wrong account selected 15% of the time.
- ✅ Programmatic precondition: block `lookup_order` until `get_customer` returns verified identifier
- ❌ Strengthen system prompt to always call `get_customer` first (probabilistic)
- ❌ Few-shot examples showing correct sequence (probabilistic)

**Principle:** For security-critical sequencing, enforce at code level, not at prompt level.

---

## 1.15 Parallel Execution

Multiple `Task` calls in a single coordinator response execute in parallel. Use this for:
- Independent research tasks
- Multi-issue customer requests
- Multi-dimensional analysis

**Exam pattern:** Complex billing dispute (billed twice + discount not applied + cancel order):
- ✅ Decompose into 3 separate issues, investigate in parallel with shared customer context, synthesize resolution
- ❌ Sequential investigation (high tool-call count, redundant data fetching)

**Note:** Parallel spawning requires emitting the multiple `Task` calls **in a single coordinator response** — issuing them across separate turns runs them sequentially.

---

## 1.16 Session Management: Resume, Fork, Fresh Start

### Named Session Resumption: `--resume <session-name>`
```bash
claude --resume investigation-auth-bug
```
- Continues a specific prior conversation with its saved context
- Useful for long-running investigations that span multiple work sessions
- **Risk:** if files changed since the prior session, its tool results are stale

### `fork_session`: Divergent Branches from a Shared Baseline
```
Codebase investigation
         |
    fork_session
    /           \
Approach A:      Approach B:
Redux            Context API
```
- Both forks inherit context **up to the branch point**, then diverge independently
- Use to **compare two approaches** (e.g., two testing strategies or refactoring approaches) from one shared, expensive codebase analysis — without re-analyzing twice, and without the two explorations contaminating each other

### Choosing: Resume vs Fresh Session with Injected Summary
| Situation | Correct choice |
|---|---|
| Prior context is mostly still valid | `--resume` the named session |
| Prior tool results are stale (files changed significantly, long time elapsed, context degraded) | Start a **new session** and inject a structured summary: "Here is a short summary of what we found: ..." |

**Why fresh-plus-summary beats resuming with stale data:** a resumed session reasons over old tool results as if they were current — a structured summary carries the *conclusions* forward without the stale *evidence*.

### Informing a Resumed Session About File Changes
If you do resume after code modifications, **tell the agent exactly which files changed** so it performs targeted re-analysis of just those files — rather than trusting stale results or re-exploring the entire codebase.

**Exam pattern:** "Yesterday's session analyzed the codebase; today three files were refactored. How to continue?" →
- ✅ Resume the named session and explicitly inform it which three files changed, for targeted re-analysis
- ❌ Resume and continue as-is (agent reasons over stale tool results for the changed files)
- ❌ Always start from scratch and re-analyze the whole codebase (wasteful when most context is still valid)

**Exam pattern:** "Team wants to evaluate two refactoring strategies starting from the same completed analysis" →
- ✅ `fork_session` — two independent branches from the shared analysis baseline
- ❌ Run both strategies sequentially in one session (the second evaluation is biased by the first's reasoning and conclusions)
- ❌ Two brand-new sessions (each must redo the shared baseline analysis)

---

## 1.17 Independent Review Instances

To avoid confirmation bias in automated review/generation:
- Run a **second independent instance** with no access to the first instance's reasoning
- This mirrors human peer review — fresh perspective catches what the author rationalized away

**Exam pattern:** Claude Code generates code, considers edge cases in reasoning, concludes its approach is correct. Non-obvious bugs only caught in PR review.
- ✅ Second independent Claude Code instance reviews changes without seeing generator's reasoning
- ❌ Extended thinking on the generation stage (doesn't fix the self-check limitation)
- ❌ Add self-review instructions to generation prompt (same instance, same confirmation bias)

---

## 1.18 Key Architecture Patterns (Named)

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
| Goal-oriented delegation | Coordinator prompts state goals + quality criteria, not step-by-step procedures |
| Content/metadata separation | Structured formats carry source URLs, doc names, page numbers alongside content for attribution |
| Prompt chaining | Fixed sequential pipeline for predictable multi-step/multi-aspect workflows |
| Dynamic adaptive decomposition | Subtasks generated from intermediate findings; plan adapts as discoveries emerge |
| Iterative refinement loop | Coordinator evaluates synthesis for gaps → re-delegates targeted queries → re-invokes synthesis until coverage sufficient |
| Structured handoff | Self-contained escalation summary (customer ID, root cause, amount, recommended action) for humans without transcript access |
| Session forking | fork_session branches diverge independently from a shared analysis baseline to compare approaches |
| Fresh-plus-summary | New session with injected structured summary when prior tool results are stale, instead of resuming |
