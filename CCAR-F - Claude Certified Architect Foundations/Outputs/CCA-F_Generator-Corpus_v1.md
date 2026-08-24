# CCA-F Grounding Corpus

**What this is.** The complete subject-matter corpus for the Anthropic Claude Certified
Architect - Foundations exam (official exam code CCAR-F), in one file. It is the source of
truth for generating practice questions: every question written from it must trace to a
numbered section here.

**How sections are numbered.** Sections run §1.1 through §5.x, grouped by exam domain,
plus a final set of high-yield traps. Cite them in the form `Corpus §1.6`. Keep the
§ symbol - the practice-test renderer matches on it to build a live link, and a citation
without it renders as dead plain text.

**Where it comes from.** Written against Anthropic's official CCA-F Exam Guide - its five
domains and weights, its thirty task statements, its six exam scenarios, and its in-scope
and out-of-scope lists. A community study guide
(github.com/paullarionov/claude-certified-architect) was used as a depth source for
explanation, never as authority on exam facts. Where the two disagree, the official guide
wins.

**Currency.** Authored against Exam Guide v0.2 and re-checked against v1.0 (effective
July 2026). A measured diff found the domain weights, all six scenarios, all thirty task
statements and both scope lists identical between the two. Anything decision-critical
should still be confirmed against the guide currently published on the Anthropic Partner
Academy.

**Not affiliated with, endorsed by, or sponsored by Anthropic.** This is study material.
It contains no real exam questions.

---

## Contents

| Part | Covers | Sections |
|---|---|---|
| 0 | Exam mechanics - format, weights, scenario bank, scope lists, scoring | - |
| 1 | D1 Agentic Architecture & Orchestration (27%) | §1.1-§1.18 |
| 2 | D2 Tool Design & MCP Integration (18%) | §2.1-§2.9 |
| 3 | D3 Claude Code Configuration & Workflows (20%) | §3.1-§3.12 |
| 4 | D4 Prompt Engineering & Structured Output (20%) | §4.1-§4.20 |
| 5 | D5 Context Management & Reliability (15%) | §5.1-§5.14 |
| 6 | Key Distinctions - 29 documented exam traps | - |

---



# Part 0 - Exam mechanics

## Format (official, Exam Guide v1.0 §3)

| Attribute | Value |
|---|---|
| Credential | Claude Certified Architect – Foundations |
| Number of questions | **60** |
| Time limit | **120 minutes** (~2 min/question) |
| Item format | **Multiple-choice AND multiple-response items; each item states how many responses to select.** Caveat worth holding: "multiple-response" appears exactly once in the whole guide with no elaboration, and all 12 official sample questions are still single-answer with 4 options. v0.2 said "one correct answer and three incorrect options" and carried a Response Types section asserting every question was single-answer; both were removed in v1.0. |
| Exam structure | **4 scenarios drawn at random from a bank of 6** |
| Content domains | 5 (weights below) |
| Delivery | Online proctored or at a test center (Pearson VUE administers, effective 2026-06-30) |
| Exam fee | $125 USD |
| Scoring | Scaled 100–1,000; **minimum passing score 720** |
| Validity | **12 months** from award date |
| Result reporting | **Pass/fail with scaled score (100–1,000), plus percent-correct by domain on the score report.** Section-level percentages are informational — pass/fail is decided by the total scaled score alone (v1.0 §10). v0.2 said "Pass or fail" only. |
| Answering | **v1.0 no longer states whether questions can be skipped.** v0.2 said the platform requires an answer before advancing; that sentence was removed. What still holds: there is no penalty for a wrong answer, so guessing costs nothing and an unsure answer should always be submitted. |
| Retakes | Max **4 attempts per rolling 12 months**; waiting periods of **14 days** after the first failure, **30** after the second, **90** after the third. Limits are per exam. (Now guide-official — v1.0 §12; previously cited from Pearson VUE policy pages.) |
| Recertification | Valid 12 months. Renew **on time** via a **free, non-proctored assessment** on the Anthropic Partner Academy. If the credential lapses, the **full exam at full fee** is required. Anthropic may also mandate a full retake instead of the renewal assessment if exam content changes significantly. (v1.0 §15 — absent from v0.2.) |

## Domain weights (official)

| Domain | Weight |
|---|---|
| D1 Agentic Architecture & Orchestration | 27% |
| D2 Tool Design & MCP Integration | 18% |
| D3 Claude Code Configuration & Workflows | 20% |
| D4 Prompt Engineering & Structured Output | 20% |
| D5 Context Management & Reliability | 15% |

Domain-weighted scoring: D1 questions collectively carry the most scored content. No partial credit per question. Scaled scoring equates difficulty across exam forms.

---

## Scenario Bank — the official 6 (Exam Guide v0.2 pp.4–5)

Every exam sitting presents 4 of these 6, at random. Each scenario frames a block of questions (~15 per scenario at 60 questions / 4 scenarios).

### Scenario 1: Customer Support Resolution Agent
Agent SDK agent for high-ambiguity requests (returns, billing disputes, account issues); custom MCP tools `get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`; target 80%+ first-contact resolution while knowing when to escalate.
**Primary domains:** D1, D2, D5.

### Scenario 2: Code Generation with Claude Code
Claude Code for code generation, refactoring, debugging, documentation; custom slash commands, CLAUDE.md configurations, plan mode vs direct execution.
**Primary domains:** D3, D5.

### Scenario 3: Multi-Agent Research System
Coordinator delegates to web-search, document-analysis, synthesis, and report-generation subagents; produces comprehensive cited reports.
**Primary domains:** D1, D2, D5.

### Scenario 4: Developer Productivity with Claude *(was missing from corpus v1)*
Agent SDK tools helping engineers explore unfamiliar codebases, understand legacy systems, generate boilerplate, automate repetitive tasks; uses **built-in tools (Read, Write, Bash, Grep, Glob)** and MCP servers.
**Primary domains:** D2, D3, D1.
**Key themes:** built-in tool selection (Grep vs Glob vs Read/Write/Edit), incremental investigation strategy, Edit→Read+Write fallback, MCP tool descriptions vs built-in preference — see §2.9.

### Scenario 5: Claude Code for Continuous Integration
Claude Code in CI/CD: automated code reviews, test generation, PR feedback; actionable feedback with minimal false positives.
**Primary domains:** D3, D4.

### Scenario 6: Structured Data Extraction *(was missing from corpus v1)*
Extraction from unstructured documents, JSON-schema validation, high accuracy, graceful edge-case handling, downstream integration.
**Primary domains:** D4, D5.
**Key themes:** tool_use + JSON schema as the output guarantee, tool_choice "any"/forced, nullable fields to prevent fabrication, retry-with-feedback and its limits, batch strategies with custom_id, confidence calibration and human-review routing — see Domain 4 and Domain 5.

**Non-official scenarios:** the community guide documents a "Conversational AI Architecture Patterns" scenario (its #7) and an "Agentic AI Tools" placeholder (its #8). These are candidate-reported, NOT in the official bank of 6. Content under them remains useful study material (it maps to D1/D5 task statements) but the generator must not present them as exam scenarios.

---

## Answer Pattern Heuristics

From practice-test analysis (v1, retained) plus the official sample-question rationales (Exam Guide pp.24–31):

| Heuristic | When it applies |
|---|---|
| Fix the root cause, not the symptom | Misrouting → fix tool descriptions, not add a classifier |
| Proportionate first response | Try the prompt/description fix before adding infrastructure (classifiers, routing layers, bigger models) |
| Programmatic enforcement for critical sequences | Identity-verification-before-refund → hook/precondition, never prompt-only (prompt compliance is probabilistic) |
| Least privilege | Scoped verify_fact for synthesis agent, not full web-search access |
| Deterministic over probabilistic | Hooks/gates for guaranteed compliance; prompts for guidance |
| Structured error context > generic failure | Return failure type, attempted query, partial results, alternatives |
| Parallel with shared context > sequential | Multi-issue requests: decompose and parallelize |
| Coordinator as hub | Subagents never talk to each other directly |
| Independence for review passes | Second instance without the generator's reasoning context |
| Match the API to the latency requirement | Blocking pre-merge → synchronous; overnight reports → batch |
| Coverage gaps trace upstream | Complete-looking subagent outputs + missing topics → check the coordinator's decomposition |
| Attention dilution → split passes | Inconsistent 14-file review → per-file passes + integration pass, not a bigger context window |

---

## Question Style Calibration

The register reference for generated questions is twofold:
1. **Official sample questions** — 12 samples with answer rationales, Exam Guide pp.24–31 (drawn from the practice test). Stem shape: 2–5 sentence Situation with concrete telemetry ("12% of cases", "55% first-contact resolution", "14 files"), then a single decision question ("What change would most effectively address...", "What's the most likely root cause?", "How should you evaluate this proposal?"). Options are full clauses, grammatically parallel, each plausible to a candidate with incomplete knowledge; rationales explain why each wrong option fails (symptom-level fix, over-engineering, wrong problem, non-existent feature).
2. **the shipped practice tests.

**Dedup constraint:** every stem in the shipped practice tests.

---

## Official In-Scope Topics (Exam Guide v0.2 Appendix — generator's topic whitelist)

Agentic loop implementation (stop_reason control flow, tool result handling, termination) · multi-agent orchestration (coordinator-subagent, decomposition, parallel execution, iterative refinement) · subagent context management (explicit passing, state persistence, crash-recovery manifests) · tool interface design (descriptions, split vs consolidate, naming) · MCP tool and resource design (resources as catalogs, tools as actions) · MCP server configuration (project vs user scope, env-var expansion, multi-server) · error handling and propagation (structured responses, transient/business/permission, local recovery) · escalation decision-making (explicit criteria, honoring customer preference, policy gaps) · CLAUDE.md configuration (hierarchy, @import, .claude/rules/ globs) · custom commands and skills (scopes, context: fork, allowed-tools, argument-hint) · plan mode vs direct execution · iterative refinement (I/O examples, test-driven, interview pattern, sequential vs batch issue fixing) · structured output via tool_use (schema design, tool_choice, nullable fields) · few-shot prompting (ambiguity targeting, format consistency, false-positive reduction) · batch processing (appropriateness, latency tolerance, custom_id failure handling) · context window optimization (trimming tool outputs, fact extraction, position-aware ordering) · human review workflows (confidence calibration, stratified sampling, per-segment accuracy) · information provenance (claim-source mappings, temporal data, conflict annotation, coverage gaps).

### Technologies list (Appendix "Technologies and Concepts")
Claude Agent SDK (AgentDefinition, agentic loops, stop_reason, PostToolUse + interception hooks, Task tool, allowedTools) · MCP (servers, tools, resources, isError, .mcp.json, env-var expansion) · Claude Code (CLAUDE.md hierarchy, .claude/rules/, .claude/commands/, .claude/skills/ frontmatter, plan mode, /memory, /compact, --resume, fork_session, Explore subagent) · CLI (-p/--print, --output-format json, --json-schema) · Claude API (tool_use, tool_choice auto/any/forced, stop_reason values, max_tokens, system prompts) · Message Batches API (50% savings, 24h window, custom_id, polling, no multi-turn tool calling within a request) · JSON Schema (required/optional, enums, nullable, "other"+detail) · Pydantic (validation, retry loops) · built-in tools (Read, Write, Edit, Bash, Grep, Glob) · few-shot · prompt chaining · context management (token budgets, summarization, lost-in-the-middle, scratchpads) · session management · confidence scoring (field-level, calibration, stratified sampling).

---

## Out-of-Scope Topics (official — will NOT appear; generator hard constraint)

- Fine-tuning or training custom Claude models
- Claude API authentication, billing, or account management
- Language/framework-specific implementation details (beyond tool/schema config)
- Deploying or hosting MCP servers (infrastructure, networking, containers)
- Claude's internal architecture, training process, or model weights
- Constitutional AI, RLHF, or safety training methodologies
- Embedding models or vector database implementation details
- Computer use (browser automation, desktop interaction)
- Image analysis / Vision capabilities
- Streaming API or server-sent events
- Rate limiting, quotas, or detailed API cost calculations
- OAuth, API key rotation, or authentication protocol details
- Cloud-provider-specific configurations (AWS, GCP, Azure)
- Performance benchmarks or model comparison metrics
- Prompt caching implementation details (beyond knowing it exists)
- Token counting algorithms or tokenization specifics

---

## Scoring Context

- Scale 100–1,000; pass 720; score report returns pass/fail + the scaled score + percent-correct per domain (the per-domain figures are informational, not part of the pass decision)
- Criterion-referenced: measured against a fixed standard set by a formal standard-setting study of minimally-qualified-candidate performance — not graded on a curve against other candidates (v1.0 §10)
- Scaled scoring equates across exam forms of slightly different difficulty — a raw-percentage → scaled conversion is therefore an approximation; the generator's estimate formula must carry that caveat
- No partial credit; no penalty for a wrong answer (guessing costs nothing)
- Domain-weighted: getting D1 wrong hurts most (27%), D5 least (15%)

## Docs Currency

Product behavior facts in the corpus are periodically re-verified against live Anthropic docs — divergences and the exam-vs-current-docs posture per item live in the currency notes. Generator rule: where the official Exam Guide and current docs conflict, the official guide's framing wins for question authoring.



# Part 1 - Domain 1: Agentic Architecture & Orchestration (27%)

## §1.1 The Agentic Loop

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

## §1.2 Hub-and-Spoke (Coordinator-Subagent) Architecture

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

## §1.3 AgentDefinition Configuration

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

## §1.4 Coordinator Prompts: Goal-Oriented vs Procedural

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

## §1.5 Structured Context Passing & Attribution

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

## §1.6 Task Decomposition

### The Coordinator's Most Critical Responsibility
If the coordinator decomposes a task too narrowly, subagents execute correctly but cover the wrong ground. Root cause = coordinator prompt, not subagent performance.

**Exam scenario:** Research system asked about "AI impact on creative industries" — coordinator decomposes into only visual art subtasks. Every subagent returns correct results. Output misses music, literature, film.
- ✅ Root cause: **coordinator's task decomposition was too narrow**
- ❌ Not: web-search agent query quality, synthesis agent gap detection, document analysis filters

### Partitioning Principle
The coordinator must **explicitly partition the research space** before delegating — assign distinct subtopics or source types to each agent. This prevents duplication and missed coverage.

**Exam pattern:** Two agents investigate the same subtopics → tokens wasted, no extra depth. Fix: coordinator partitions before delegating, not deduplication after.

---

## §1.7 Decomposition Strategy: Fixed Pipelines vs Dynamic Adaptive

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

## §1.8 Coordinator Iterative Refinement Loop

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

## §1.9 Error Propagation in Multi-Agent Systems

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

## §1.10 Coverage Annotations (Graceful Degradation)

When upstream inputs are incomplete (some sources timed out, some succeeded), the synthesis agent should:
1. Complete synthesis using available data
2. **Annotate coverage** — mark which conclusions are well-supported vs where gaps exist
3. Propagate uncertainty upward

**Exam pattern:** "Web search returned 3/5 source categories — what should synthesis agent do?"
- ✅ Structure output with coverage annotations showing where data is missing
- ❌ Return error because input is incomplete
- ❌ Proceed without noting the gaps

---

## §1.11 Least Privilege for Subagent Tools

Each subagent should have **only the tools it needs** for its defined scope.

**Exam scenario:** Synthesis agent needs to verify 85% simple facts, 15% complex research.
- ✅ Give synthesis agent a limited `verify_fact` tool for simple checks; route complex verification through coordinator
- ❌ Give synthesis agent full web-search access (breaks separation of responsibilities)
- ❌ Batch all verification to end (blocking — later synthesis steps may need earlier verified facts)

**Exam scenario:** Document analysis agent given `fetch_url` starts doing ad-hoc web search.
- ✅ Replace `fetch_url` with `load_document` that validates URL points to document format (fixes root cause at interface level)
- ❌ Add prompt instructions to not use `fetch_url` for search (probabilistic, not deterministic)

---

## §1.12 When to Escalate to Human

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

## §1.13 Structured Handoff Protocols (Mid-Process Escalation)

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

## §1.14 Critical Sequencing and Preconditions

When correct sequencing is mandatory (e.g., verify identity before taking action), use **programmatic preconditions** — not prompt instructions.

**Exam scenario:** Support agent skips `get_customer` and calls `lookup_order` directly using customer-provided order number. Wrong account selected 15% of the time.
- ✅ Programmatic precondition: block `lookup_order` until `get_customer` returns verified identifier
- ❌ Strengthen system prompt to always call `get_customer` first (probabilistic)
- ❌ Few-shot examples showing correct sequence (probabilistic)

**Principle:** For security-critical sequencing, enforce at code level, not at prompt level.

---

## §1.15 Parallel Execution

Multiple `Task` calls in a single coordinator response execute in parallel. Use this for:
- Independent research tasks
- Multi-issue customer requests
- Multi-dimensional analysis

**Exam pattern:** Complex billing dispute (billed twice + discount not applied + cancel order):
- ✅ Decompose into 3 separate issues, investigate in parallel with shared customer context, synthesize resolution
- ❌ Sequential investigation (high tool-call count, redundant data fetching)

**Note:** Parallel spawning requires emitting the multiple `Task` calls **in a single coordinator response** — issuing them across separate turns runs them sequentially.

---

## §1.16 Session Management: Resume, Fork, Fresh Start

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

## §1.17 Independent Review Instances

To avoid confirmation bias in automated review/generation:
- Run a **second independent instance** with no access to the first instance's reasoning
- This mirrors human peer review — fresh perspective catches what the author rationalized away

**Exam pattern:** Claude Code generates code, considers edge cases in reasoning, concludes its approach is correct. Non-obvious bugs only caught in PR review.
- ✅ Second independent Claude Code instance reviews changes without seeing generator's reasoning
- ❌ Extended thinking on the generation stage (doesn't fix the self-check limitation)
- ❌ Add self-review instructions to generation prompt (same instance, same confirmation bias)

---

## §1.18 Key Architecture Patterns (Named)

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



# Part 2 - Domain 2: Tool Design & MCP Integration (18%)

## §2.1 Claude API Tool Use

### How Tool Calling Works
1. Define tools in API request with `name`, `description`, and `input_schema` (JSON Schema)
2. Claude returns a response with `stop_reason: "tool_use"` and a `tool_use` content block
3. Application executes the tool
4. Application appends a `tool_result` content block to the conversation
5. Claude continues from the result

### `tool_use` Content Block Structure
```json
{
  "type": "tool_use",
  "id": "toolu_abc123",
  "name": "lookup_order",
  "input": {"order_id": "12345"}
}
```
Key fields: `id` (for matching to `tool_result`), `name`, `input`

### `tool_choice` Parameter
| Value | Behavior |
|---|---|
| `{"type": "auto"}` | Claude decides whether to use a tool (default) |
| `{"type": "any"}` | Claude must use at least one tool |
| `{"type": "tool", "name": "X"}` | Claude must use tool X specifically |

Configuration depth — when to use each value — is covered in §2.5.

---

## §2.2 Tool Description Design

### The Primary Lever for Tool Selection
Tool descriptions are the **primary input** Claude uses to decide which tool to call. When misrouting occurs, **check descriptions first** before adding classifiers or few-shot examples.

### Description Quality Requirements
A good tool description specifies:
- **What it does** (purpose, not just name)
- **What input it accepts** (formats, ID types, examples)
- **When to use it** vs similar tools
- **When NOT to use it** (boundary cases)

**Exam scenario:** `analyze_content` (web-search agent) vs `analyze_document` (doc-analysis agent) — names nearly identical → misrouting 45% of time.
- ✅ Rename web-search tool to `extract_web_results`, update description to explicitly reference "web search and URLs"
- ❌ Add pre-routing classifier (adds infrastructure without fixing root cause)

**Exam scenario:** `get_customer` vs `lookup_order` both have 1-line descriptions, similar ID formats → `get_customer` called for order queries.
- ✅ Expand both descriptions with input formats, example queries, edge cases, and boundaries
- ❌ Combine into single `lookup_entity` tool (loses semantic precision)

---

## §2.3 Structured Tool Errors

### `isError` Flag in MCP
MCP tools return results with an optional `isError: true` flag to signal failure. The agent receives this and decides how to proceed.

### The Four Error Categories
The exam distinguishes four categories of tool error — each demands a different agent response:

| Category | Example | Retryable? | Correct agent response |
|---|---|---|---|
| **Transient** | Timeout, service temporarily unavailable | Yes | Retry (ideally handled inside the tool/subagent first) |
| **Validation** | Invalid input, malformed ID | No (as-is) | Fix the input and re-call |
| **Business** | Policy violation (e.g., refund exceeds policy limit) | **No** | Explain the policy outcome to the user — never retry |
| **Permission** | Auth failure, access denied | No | Escalate or switch credentials — retrying is wasted effort |

### Structured Error Response Design
Tool errors should include:
```json
{
  "isError": true,
  "errorCategory": "transient | validation | business | permission",
  "isRetryable": true,
  "description": "Patent database connection timed out after 30s",
  "partialResults": [...],
  "alternatives": ["Try with shorter query", "Use alternate endpoint"]
}
```

**Exam principle:** Returning a `retryable` boolean flag is BETTER than forcing the agent to guess from error text, but WORSE than handling transient errors internally and only surfacing the ones requiring coordinator decision.

### Business-Rule Errors: A Distinct Category
A business-rule violation (policy limit exceeded, action not allowed for this account tier) is **not a failure of the tool** — it is a valid answer that the requested action is disallowed. Structure it as:
- `retriable: false` — signals the agent that re-invoking cannot change the outcome
- A **customer-friendly explanation** in the payload — so the agent can communicate the policy outcome appropriately without paraphrasing internal jargon

**Exam scenario:** Support agent's `process_refund` tool rejects a refund because it exceeds the 30-day policy window. The agent keeps retrying the call.
- ✅ Return `retriable: false` + customer-friendly explanation ("Refunds are available within 30 days of purchase; this order is outside that window") so the agent stops retrying and explains the policy to the customer
- ❌ Return a generic `"Operation failed"` — the agent cannot distinguish policy denial from a transient outage, so it retries or escalates incorrectly
- ❌ Classify it as a transient error with `isRetryable: true` — wastes retry attempts on an outcome that can never change

### Valid Empty Results vs Access Failures
An **empty result is a successful query** with no matches — not an error. Conflating the two corrupts agent decision-making in both directions:

| Situation | Correct signal | Wrong signal causes |
|---|---|---|
| Query ran, zero matches | Success, empty result set (`isError` absent/false) | Agent retries or escalates a query that worked fine |
| Query could not run (DB down, access denied) | `isError: true` with category | Agent reports "no data found" when data may exist |

- ✅ `search_orders` returns `{"results": [], "isError": false}` when the customer genuinely has no orders — the agent confidently reports "no orders found"
- ❌ Return `isError: true` for zero matches (agent treats a valid answer as a failure and retries)
- ❌ Return an empty list when the database connection failed (agent tells the customer "you have no orders" — a false statement caused by masking an access failure)

### Error Handling at the Right Level
- **Inside the tool:** Handle transient failures (retry + backoff) before surfacing
- **Inside the subagent:** Local recovery for transient failures; propagate to the coordinator only errors it cannot resolve locally, along with partial results and what was attempted
- **Return to agent:** Only when the error requires a decision only the agent can make (skip? retry with different params? escalate?)
- **Never:** Return success with embedded error metadata — masks failures

---

## §2.4 Two-Tool Token-Binding Pattern

For operations that must always be preceded by a preview/dry-run:

**Problem:** `dry_run: boolean` parameter on a single tool — agent bypasses dry run by calling with `dry_run=false` directly.

**Solution:** Replace with two tools:
1. `preview_remove_member` → returns impact details + a **single-use confirmation token**
2. `execute_remove_member` → requires that token as a parameter

This makes it **architecturally impossible** to execute without a prior preview — the token only exists after a preview call.

**Why this beats alternatives:**
- Server-side timing heuristic (A) — fragile to timing conditions
- Orchestration-layer confirmation prompt (B) — requires extra infrastructure
- Prompt instruction + examples (C) — probabilistic, not guaranteed

---

## §2.5 Tool Distribution Across Agents & tool_choice Configuration

### Too Many Tools Degrades Selection Reliability
Giving an agent access to too many tools (the official guide's own numbers: **18 instead of 4–5**) degrades tool selection reliability by increasing decision complexity. Each additional tool is another candidate the model must discriminate between on every turn — more overlap, more near-miss descriptions, more misrouting.

**Exam scenario:** A subagent with 18 tools frequently calls the wrong one; a peer agent with 5 role-scoped tools selects correctly.
- ✅ Restrict each subagent's tool set to the 4–5 tools relevant to its role
- ❌ Keep all 18 tools and add more detailed descriptions to every one (descriptions help, but tool count itself is the root cause — reduce the decision space first)
- ❌ Give every agent the full tool catalog "for flexibility" (agents with tools outside their specialization tend to misuse them — e.g., a synthesis agent attempting web searches)

### Least Privilege in Tool Design
Each agent or component should have **only the tools it needs** for its scope. Giving broader tools leads to scope creep and unintended behavior.

**Exam scenario:** Document analysis agent has `fetch_url` → starts downloading search engine results pages.
- ✅ Replace with `load_document` that validates URL points to a document format (replacing a generic tool with a **constrained alternative** enforces the boundary at the interface level)
- ❌ Add prompt instruction (probabilistic)
- ❌ Block known search-engine domains (fragile, not future-proof)

### Scoped Cross-Role Tools for High-Frequency Needs
Strict role scoping has one sanctioned exception: when an agent has a **high-frequency need** that would otherwise force constant round-trips through the coordinator, give it a **narrowly scoped cross-role tool** — while **complex cases still route through the coordinator**.

**Exam scenario:** Synthesis agent frequently needs to confirm individual facts while writing its report.
- ✅ Give it a `verify_fact` tool scoped to simple lookups; complex research questions still go back through the coordinator to the research agents
- ❌ Give the synthesis agent full `web_search` access (cross-specialization misuse: it starts doing open-ended research instead of synthesizing)
- ❌ Route every single fact check through the coordinator (correct scoping, but the round-trip overhead on a high-frequency need is exactly what scoped cross-role tools exist to avoid)

### tool_choice Configuration Depth
| Value | Guarantees | When to use |
|---|---|---|
| `{"type": "auto"}` | Nothing — model may answer in plain text | Default for most agentic loops |
| `{"type": "any"}` | The model **will call some tool** — never returns conversational text | When you need guaranteed structured output; with multiple extraction tools, the model still picks the best one |
| `{"type": "tool", "name": "extract_metadata"}` | The model **will call that specific tool** | When a specific first step must be guaranteed (execution order) |

**Forced-first-step pattern:** Force `extract_metadata` on the first turn (`{"type": "tool", "name": "extract_metadata"}`), then process subsequent steps — enrichment tools, follow-ups — in **follow-up turns** where `tool_choice` is relaxed back to `"auto"` or `"any"`.

**Exam scenario:** A pipeline must always extract document metadata before any enrichment tool runs, but a prompt instruction is only followed ~90% of the time.
- ✅ Set `tool_choice: {"type": "tool", "name": "extract_metadata"}` on the first request, then continue with `"auto"` for the rest of the workflow
- ❌ Strengthen the prompt instruction ("ALWAYS call extract_metadata first") — probabilistic, not guaranteed
- ❌ Leave `tool_choice` forced on every turn — the model can then never call the enrichment tools at all

**Exam scenario:** An extraction agent sometimes replies with prose instead of calling any extraction tool.
- ✅ Set `tool_choice: {"type": "any"}` — guarantees a tool call instead of conversational text
- ❌ Set `tool_choice: {"type": "auto"}` and add "you must use a tool" to the prompt (auto permits text responses; the instruction is probabilistic)

---

## §2.6 Model Context Protocol (MCP)

### Three MCP Primitives
| Primitive | Purpose | Analogous to |
|---|---|---|
| **Tools** | Actions Claude can call | API endpoints |
| **Resources** | Read-only data Claude can access | Files/databases |
| **Prompts** | Pre-built prompt templates | Reusable instructions |

Tools from **all configured MCP servers are discovered at connection time** and are available to the agent simultaneously.

### Configuration Files
| File | Scope | Purpose |
|---|---|---|
| `.mcp.json` (project root) | Project-wide, version-controlled | Shared team MCP configuration |
| `~/.claude.json` (user home) | User-specific | Personal overrides, personal auth, experimental servers |

**Exam pattern:** Team uses shared MCP server. Each developer has their own GitHub token.
- ✅ Add server to `.mcp.json` with `${GITHUB_TOKEN}` environment variable substitution; document the variable in README
- ❌ Each developer adds server in user scope (inconsistent tooling)
- ❌ Commit a placeholder token (security risk)

### Environment Variable Substitution
`.mcp.json` supports `${VAR_NAME}` syntax. At runtime, Claude Code substitutes the variable from the environment. This lets project config be version-controlled while credentials stay out of the repo.

### MCP Resources as Content Catalogs
Resources expose **content catalogs** — issue summaries, documentation hierarchies, database schemas — giving the agent an immediate "map" of what data exists **without exploratory tool calls**.

**Exam scenario:** An agent working against a project tracker burns many turns calling `search_issues` with guessed queries just to discover what issues exist.
- ✅ Expose an issue-summary catalog as an MCP **resource** — the agent reads the catalog for visibility into available data, then makes targeted tool calls
- ❌ Add a `list_everything` tool the agent must remember to call first (a resource provides the map as readable context; a tool adds an LLM call and relies on the agent thinking to use it)
- ❌ Paste the full issue database into the system prompt (resources are requested on demand; a static dump bloats context and goes stale)

### Community Servers vs Custom Servers
- ✅ For **standard integrations** (Jira, GitHub, Slack), prefer **existing community MCP servers**
- ✅ Build **custom servers only for unique, team-specific workflows** that no existing server covers
- ❌ Build a custom Jira MCP server from scratch "for control" (reinvents a maintained standard integration; custom effort belongs on workflows unique to your team)

### MCP Tool Descriptions vs Built-in Tools
Agents may **prefer built-in tools (like Grep, Read) over MCP tools** with similar-sounding functionality, because tool selection runs on descriptions. If the MCP tool's description does not make its superior capability explicit, the agent falls back to the familiar built-in.

**Exam scenario:** A code-search MCP server offers semantic, index-backed search, but the agent keeps using built-in Grep instead.
- ✅ Enhance the MCP tool's description to explain its capabilities and outputs in detail — highlight concrete advantages, unique data, or context built-in tools cannot provide
- ❌ Remove or disable Grep so the agent has no alternative (breaks legitimate content-search use cases; the root cause is an under-specified description, not the built-in tool's existence)
- ❌ Add a system prompt rule "always prefer MCP tools" (blunt, keyword-sensitive instruction that can misroute cases where the built-in genuinely is the right tool)

---

## §2.7 Hooks: PostToolUse and PreToolUse

### What Hooks Do
Hooks are deterministic code that runs around tool calls. They intercept tool interactions without relying on the LLM.

| Hook | Fires | Use for |
|---|---|---|
| `PreToolUse` | Before tool executes | Validate, block, modify params |
| `PostToolUse` | After tool returns | Transform output, log, normalize |

### PostToolUse — Primary Use Case: Output Normalization
When multiple tools return different data formats (Unix timestamps, ISO 8601 dates, numeric status codes) from sources you cannot modify:
- ✅ Use `PostToolUse` hook to intercept and normalize all outputs centrally
- ❌ Modify tools you control + create wrappers for third-party tools (fragmented maintenance)
- ❌ Create a `normalize_data` tool the agent calls after every retrieval (adds LLM call overhead)
- ❌ Document formats in system prompt (relies on LLM interpretation)

### PreToolUse — Primary Use Case: Threshold Enforcement
Block operations above a defined threshold (e.g., bulk deletion affecting >50 records) and route to escalation. This is **deterministic** — it fires regardless of LLM behavior.

**Exam distinction:** Hooks are deterministic. System prompt instructions are probabilistic. For safety-critical enforcement, use hooks.

---

## §2.8 Tool Bundling / Composite Tools

When agents frequently call multiple tools in sequence for the same operation, consider creating composite tools.

**But:** The preferred approach (from practice test) is to **prompt the agent to bundle tool requests into one turn** rather than creating composite tools, as the agent can naturally request multiple tools simultaneously.

**Exam scenario:** Support agent calls `get_customer` and `lookup_order` in separate sequential turns even when both are needed.
- ✅ Instruct Claude in prompt to bundle related tool requests into one turn
- Not preferred: Create `get_customer_with_orders` composite tool (hides the composition)

---

## §2.9 Built-in Tools: Read, Write, Edit, Bash, Grep, Glob

### Tool Selection Reference
| Task | Tool | Example |
|---|---|---|
| Find files by name/extension pattern | **Glob** | `**/*.test.tsx`, `src/components/**/*.ts` |
| Search within file contents | **Grep** | Function names, error messages, import statements |
| Read a file in full | **Read** | Load a file for analysis |
| Write a new file (or full replacement) | **Write** | Create a file from scratch |
| Targeted modification of an existing file | **Edit** | Replace a specific snippet via **unique text match** |
| Run a shell command | **Bash** | git, npm, run tests, build |

### Grep vs Glob — The Core Distinction
- **Grep = content search.** Searches *inside* files for patterns: function names, error messages, import statements. "Find all callers of `processPayment`" → Grep.
- **Glob = file-path pattern matching.** Finds files *by name or extension pattern*: "Find all test files" → Glob `**/*.test.tsx`.

**Exam scenario:** Locate every file that references a deprecated `formatDate` function.
- ✅ Grep for `formatDate` across the codebase (the target is file *content*)
- ❌ Glob for `**/formatDate*` (Glob matches file *paths*, not what's inside files — this only finds files *named* formatDate)

**Exam scenario:** Apply a convention change to all TypeScript test files.
- ✅ Glob `**/*.test.tsx` to enumerate the files by naming pattern
- ❌ Grep for the word "test" in file contents (matches unrelated files mentioning "test"; misses test files that don't contain the literal word)

### Incremental Investigation Strategy
Build codebase understanding **incrementally** — never read all files upfront:

```
1. Grep: find entry points (function definition, export)
2. Read: read the found files
3. Grep: find usages (imports, call sites)
4. Read: read consumer files, follow imports, trace flows
5. Repeat until the picture is complete
```

- ✅ Start with Grep to locate entry points, then Read to follow imports and trace flows
- ❌ Read every file in the repository first to "get full context" (burns context window on irrelevant files; the exam treats upfront bulk reading as the anti-pattern)
- ❌ Glob the whole tree and Read each match before searching (same anti-pattern — discovery should be driven by content search, then targeted reads)

### Edit Failure on Non-Unique Matches → Read + Write Fallback
**Edit works by unique text matching.** If the anchor text appears more than once in the file, Edit fails — it cannot decide which occurrence to modify. The reliable fallback:

1. **Read** — load the full file content
2. Modify the content programmatically
3. **Write** — write the updated version

- ✅ When Edit cannot find a unique anchor, fall back to Read + Write for a reliable full-file modification
- ❌ Retry Edit with a shorter, more generic anchor string (shorter anchors are *more* likely to be non-unique, not less)
- ❌ Use Bash with `sed` to force the replacement (bypasses the tool designed for the job; the exam's sanctioned fallback is Read + Write)

### Tracing Function Usage Across Wrapper Modules
When a function is re-exported or wrapped by intermediate modules, searching only for the original name misses call sites that use the wrapper's name.

**Strategy:** first **identify all exported names** (the original plus every wrapper/re-export alias), then **search for each name** across the codebase.

**Exam scenario:** `calculateTax` is wrapped by `utils/tax.ts` as `getTax` and re-exported from `index.ts`. A rename must update every caller.
- ✅ First Grep/Read the wrapper modules to collect all exported names (`calculateTax`, `getTax`), then Grep for each name to find all call sites
- ❌ Grep only for `calculateTax` and conclude those are all the callers (misses every consumer that imports the `getTax` wrapper)

---

**Section count:** 9 major sections (§2.1–§2.9)



# Part 3 - Domain 3: Claude Code Configuration & Workflows (20%)

## §3.1 CLAUDE.md Hierarchy, `@import`, and Memory Diagnosis

### Levels (concatenated load order, root → working directory)
1. **User-level** — `~/.claude/CLAUDE.md` — applies to all projects for this user
2. **Project-level** — `<project-root>/CLAUDE.md` or `<project-root>/.claude/CLAUDE.md` — applies to entire project
3. **Directory-level** — `CLAUDE.md` in any subdirectory — applies when working with files in that directory
4. **Rules files** — `.claude/rules/*.md` with YAML frontmatter — path-scoped conditional loading

### Critical Semantics: Concatenation, NOT Override Precedence
Current official docs (code.claude.com/docs, verified 2026-07-06) describe the hierarchy as a **concatenated load order**: all discovered CLAUDE.md files are concatenated into context, from the root down to the working directory. Every discovered file contributes its instructions — a "lower" file does not silently replace a "higher" one.

- ✅ All levels load together; instructions accumulate. If two files conflict, Claude sees both — resolve conflicts by editing the files, not by relying on one level "winning."
- ❌ **Misconception:** "Lower levels override higher levels — a directory-level CLAUDE.md replaces the project-level one for that directory." Wrong. The files are concatenated, not overridden. There is no documented override-precedence mechanism between CLAUDE.md levels.

### Critical Rule: Shared vs Personal
- **Project-level config** is checked into version control → available to ALL team members
- **User-level config** lives in `~/.claude/CLAUDE.md` → only for that developer; **NOT shared via version control**

**Exam scenario:** Three developers follow "always include comprehensive error handling." Fourth (new) doesn't. All use same repo.
- Root cause: ✅ Guidance is in the original developers' `~/.claude/CLAUDE.md`, not in the project `.claude/CLAUDE.md`
- Fix: Move instruction to project-level config
- Diagnosis workflow: run `/memory` on the new teammate's machine to list which memory files are actually loaded — the project instruction will be visibly absent

### `@import` Syntax — Modular CLAUDE.md
CLAUDE.md can reference external files with `@path`, keeping configuration modular:

```markdown
# CLAUDE.md
Coding standards: @./standards/coding-style.md
Test requirements: @./standards/testing-requirements.md
Project overview: @README.md
```

Rules for `@path`:
- `@` immediately before the path (no space); relative and absolute paths supported
- Relative paths resolve relative to the file containing the import
- Maximum import nesting depth is **5** per the community study guide — see the currency note below

> **⚠ Currency note — import depth is contested, do not key a question on it** (added 2026-08-11)
>
> - **This corpus / the community study guide line 589:** "Maximum import nesting depth is 5."
> - **Current product docs (verbatim):** "Imported files can recursively import other files, with a maximum depth of **four hops**." Source: https://code.claude.com/docs/en/memory (re-retrieved 2026-08-11; already recorded in the currency notes §"D4 — CLAUDE.md hierarchy semantics" on 2026-08-09).
> - **Official Exam Guide v1.0:** silent. Task Statement 3.1 names "the `@import` syntax for referencing external files" and the Appendix names "`@import` patterns"; neither states any depth number. Verified against the official Exam Guide.
>
> **Generator rule:** treat this the same way as a `[CONFLICT-RISK]` delta item. Never write a question whose correct answer turns on the digit, and never write a distractor that is wrong only because it says 4 instead of 5. Exam 4 Q22 did key on it and should not be repeated.
>
> **Learner posture:** if a question does turn on it, answer **5**, because the paper is scored against its own guide. What is stable and testable here is the syntax: `@` immediately before the path with no space, relative and absolute paths both work, and a relative path resolves against the file containing the import rather than the working directory.

Use `@import` to selectively include only the standards files relevant to each package — e.g., each package's CLAUDE.md imports the standards files its maintainers know apply to that package, instead of every package loading one giant global file.

### `/memory` — Verifying What Is Loaded
`/memory` shows and manages the memory files loaded in the current session.
- Use it to **verify which memory files are loaded** and to **diagnose inconsistent behavior across sessions** (e.g., an instruction that works on one machine but not another)
- First diagnostic step whenever "Claude follows rule X sometimes but not always": check whether the file holding rule X is actually in the loaded set

**Exam scenario:** Claude applies a convention in some sessions but not others.
- ✅ Run `/memory` to check which memory files are loaded in each session — the convention likely lives in a file that isn't consistently discovered (wrong level, wrong directory)
- ❌ Repeat the instruction louder in the prompt each session (treats symptom, not root cause)

---

## §3.2 `.claude/rules/` — Path-Scoped Conditional Rules

### Structure
```
.claude/rules/
  testing.md          # glob: **/*.test.*
  api-conventions.md  # glob: src/api/**/*.ts
  react.md            # glob: src/components/**/*.tsx
```

### YAML Frontmatter
```yaml
---
paths:
  - "**/*.test.tsx"
  - "**/*.test.ts"
---
# Testing Conventions
...
```

Rules load automatically **only** when Claude works on files matching the glob patterns — irrelevant rules stay out of context, saving tokens.

### When to Use `.claude/rules/` vs CLAUDE.md

| Use Case | Best Location |
|---|---|
| Conventions that apply always | Root `CLAUDE.md` |
| Conventions scoped to file type/directory | `.claude/rules/` with glob patterns |
| Workflow-specific guidance (PR review, deploy) | Skills in `.claude/skills/` |

**Exam scenario:** React components use hooks, API handlers use async/await, DB models use repository pattern. Tests co-located next to code.
- ✅ `.claude/rules/` with glob patterns — ensures correct conventions regardless of which directory you're in
- ❌ Root CLAUDE.md under headings (relies on model inference, not deterministic file-path matching)
- ❌ Separate CLAUDE.md in every subdirectory (doesn't work well when files are spread across many dirs)

---

## §3.3 Skills — `.claude/skills/`

### Skill Structure
```
.claude/skills/
  commit/
    SKILL.md
  migration/
    SKILL.md
```

### SKILL.md Frontmatter Options
```yaml
---
description: Generate a database migration file
argument-hint: "<migration-name>"
context: fork
allowed-tools: [Write, Read]
---
```

| Frontmatter Key | Purpose |
|---|---|
| `description` | Shown in slash command menu |
| `argument-hint` | Displayed when invoking command, prompts for required args |
| `context: fork` | Runs skill in isolated subagent context (protects main session) |
| `allowed-tools` | Scopes tool access during skill execution — see the dual framing below |

### `allowed-tools` Semantics — Two Framings (answer the exam with the official one)
**Official Exam Guide framing (v0.2, task 3.2 — this is what the exam tests):** `allowed-tools` **restricts tool access during skill execution** — e.g., "limiting to file write operations to prevent destructive actions." Exam questions about scoping a skill's capabilities expect `allowed-tools` as the answer.

**Current product docs framing (code.claude.com/docs/en/skills, verified 2026-07-06):** `allowed-tools` lists tools Claude can use **without asking the user for permission** while the skill is active — a permission pre-grant; unlisted tools follow the normal permission flow rather than being hard-blocked.

Both framings agree on the exam-relevant judgment: `allowed-tools` is the SKILL.md frontmatter key you reach for to scope what a skill may do.

- ✅ Exam answer: to limit a skill to safe file operations, set `allowed-tools` in its SKILL.md frontmatter (e.g., `[Write, Read]`)
- ✅ Real-world nuance: the mechanism is permission pre-granting, so scope it minimally — anything unlisted still surfaces a permission prompt
- ❌ **Misconception:** "tool scoping for a skill is configured in `.mcp.json`, `CLAUDE.md`, or a `config.json` commands array." Wrong — it lives in SKILL.md frontmatter.

### `context: fork` — Critical Use Case
When a skill generates large output or exploration context, `context: fork` runs it in an **isolated subagent context** so the output does not pollute the main conversation window.

**Exam scenario:** `/analyze-codebase` skill causes Claude to lose context of original task.
- ✅ Add `context: fork` in skill frontmatter
- ❌ Switch to faster model (doesn't fix context pollution)
- ❌ Compress results to short summary (loses analysis capability)

**Exam scenario:** `/explore-alternatives` skill — rejected approaches bleed into subsequent implementation.
- ✅ Add `context: fork` — exploration runs in isolation; results summarized back
- ❌ Split into two skills (doesn't prevent context leakage)

---

## §3.4 Custom Slash Commands — `.claude/commands/`

### Location
- **Project-wide** (available to all team members): `.claude/commands/` in the repo — version-controlled
- **Personal** (just for you): `~/.claude/commands/` — not shared via VCS

**Exam scenario:** Team wants `/review` command available to everyone who clones the repo.
- ✅ Create in `.claude/commands/` — version-controlled, auto-available

### `$ARGUMENTS` Variable
The text typed after the command name is available as `$ARGUMENTS` inside the command file.

Note: in current Claude Code, `.claude/commands/` (legacy, still supported) and `.claude/skills/` (current) are unified — both create `/name` commands.

---

## §3.5 Personal vs Project Skill Precedence

Personal skills override project skills with the **same name**.

**Exam scenario:** Developer wants to customize `/commit` without affecting teammates.
- ✅ Create personal skill at `~/.claude/skills/commit/SKILL.md` — same command name, personal override
- ❌ Create `~/.claude/skills/my-commit/SKILL.md` — creates new `/my-commit` command, loses familiar name

---

## §3.6 Planning Mode vs Direct Execution

### Planning Mode
- Use when: large scope, architectural decisions, multiple approaches possible, complex changes across many files
- Claude explores, understands, designs — presents a plan before executing (Read/Grep/Glob only, no side effects)
- Avoids expensive rework from premature execution

### Direct Execution Mode
- Use when: scope is clear, approach is defined, changes are routine
- Claude implements immediately

### Combined Approach
1. Planning mode for investigation and design → 2. User approves plan → 3. Direct execution to implement

**Exam scenarios:**
| Situation | Correct Mode |
|---|---|
| Restructure monolith into microservices (dozens of files) | Planning mode |
| Add Slack support (multiple valid integration approaches) | Planning mode |
| Library migration affecting 45+ files | Planning mode |
| Implement function with well-defined input/output spec | Direct execution |
| Single-file bug fix with a clear stack trace | Direct execution |

**Exam trap:** "Start in direct execution and switch to planning when it gets hard" → Wrong. Reactive switching is expensive. Plan upfront when the task demands it.

---

## §3.7 Iterative Refinement — Progressive Improvement (Official Task 3.5)

Four named techniques for converging on correct output faster than blind re-prompting.

### 3.7.1 The Interview Pattern
Instead of letting Claude generate from an underspecified brief and then iterating on wrong output, have Claude **interview YOU first** — ask clarifying questions to surface considerations you may not have anticipated before it implements anything.

```
Claude: "Before implementing caching for the API, a few questions:
1. Which cache invalidation strategy — TTL or event-based?
2. Is stale data acceptable when the cache is unavailable?
3. Should caching be per-user or global?
4. What is the expected data volume to cache?"
```

**When it pays off:**
- Unfamiliar domains (fintech, healthcare, legal) where you don't know what you don't know
- Tasks with non-obvious implications (cache invalidation strategies, failure modes)
- Multiple viable approaches where the best choice depends on context only you have

**Exam scenario:** Developer asks for a caching layer in an unfamiliar domain; first three generated versions each miss a different requirement (invalidation, stale reads, multi-tenancy).
- ✅ Restart with the interview pattern — "ask me what you need to know before implementing" — requirements are gathered up front instead of discovered through failed iterations
- ❌ Keep iterating on the generated code one missed requirement at a time (slow, and each fix can disturb the last)
- ❌ **Misconception:** "Asking Claude to interview you wastes a turn — it's faster to generate first and correct after." Wrong. For underspecified tasks, one interview turn replaces several correction cycles; requirements surfaced up front prevent rework.

### 3.7.2 Test-Driven Iteration
Write the test suite **first** — covering expected behavior, edge cases, and performance requirements — then iterate by sharing test failures until everything is green.

- Tests are an objective, machine-checkable definition of "done"; prose acceptance criteria are not
- Each iteration feeds Claude the concrete failures, so refinement is targeted, not guesswork
- Providing a specific failing test case with example input and expected output is the fastest way to fix an edge case (e.g., null values in a migration script)

**Exam scenario:** Migration script mishandles null values; the developer keeps describing the bug in prose and gets partial fixes.
- ✅ Provide a concrete test case: sample input row containing nulls + exact expected output; iterate until the test passes
- ❌ Re-describe the bug more emphatically ("really handle ALL nulls") — prose descriptions of edge cases are interpreted inconsistently
- ❌ **Misconception:** "Write tests after generation to verify the result." That's verification, not test-driven iteration — writing tests first anchors generation to the spec and gives every iteration a concrete failure signal.

### 3.7.3 Concrete Input/Output Examples (2–3)
When natural-language descriptions of a transformation are interpreted inconsistently, provide **2–3 concrete input/output example pairs**. Examples are the most effective way to communicate expected transformations — they unambiguously show format and decision logic, and the model generalizes the pattern to new cases rather than just repeating the examples.

**Exam scenario:** A data-transformation prompt described in prose produces a differently-shaped output on each run.
- ✅ Add 2–3 concrete input→output example pairs to the prompt to anchor the transformation
- ❌ Lengthen the prose description with more adjectives (still ambiguous)
- ❌ **Misconception:** "Examples make the model copy the samples instead of generalizing." Wrong. Well-chosen examples demonstrate the pattern; the model applies it to novel inputs.

### 3.7.4 Batching Feedback: One Message vs Sequential
- **Interacting/interdependent issues → one detailed message.** When fixes affect each other, fixing them separately can conflict — fix A can invalidate or collide with fix B. Presenting all interacting issues together lets Claude design one coherent change.
- **Independent issues → sequential iteration.** When fixes don't interact, one-at-a-time keeps each iteration focused and easy to verify.

**Exam scenario:** Review found three issues in one function: a locking bug, a retry bug that depends on the locking behavior, and an unrelated typo in a log string.
- ✅ Send the locking + retry issues together in one detailed message (they interact — fixing retry without knowing the new locking design produces a conflicting patch); the typo can go separately or ride along
- ❌ Feed all three strictly one at a time — the sequential locking fix and retry fix can contradict each other, forcing another round
- ❌ **Misconception:** "Always report one issue per message so Claude can focus." Wrong for interdependent issues — separate fixes to interacting problems can conflict; interdependent fixes belong in a single message.

---

## §3.8 CI/CD Integration — `-p` / `--print` and Pipeline Practices

### Non-Interactive Mode
To run Claude Code in a CI/CD pipeline (no user interaction):
```bash
claude -p "Analyze this pull request for security issues"
```

- `-p` (or `--print`) processes the prompt, prints to stdout, and exits
- Without `-p`, Claude Code waits for interactive input → pipeline hangs

**Exam trap options to reject:**
- `--batch` — does not exist
- `CLAUDE_HEADLESS=true` — does not exist
- `stdin < /dev/null` — Unix workaround, not the documented approach

### Re-Runs: Include Prior Review Results
When a review re-runs after new commits, **include the prior review's findings in the prompt** and instruct Claude to report only new or still-unaddressed issues.
- Keeps the reviewer consistent across runs instead of re-litigating previously settled findings
- Prevents duplicate inline PR comments on unchanged code

**Exam scenario:** CI review posts near-duplicate comments (with slightly different wording) every time the author pushes a follow-up commit.
- ✅ Feed the previous run's findings into the re-run prompt; instruct: report only new or unresolved issues
- ❌ **Misconception:** "Each re-run should start from a blank slate so the review stays objective." Wrong. A blank-slate re-run re-litigates old findings and floods the PR with duplicates; prior findings in context keep the reviewer consistent.

### Session Context Isolation for Review
The same Claude session that generated code is **less effective at reviewing its own changes** — it retains its reasoning context and is less likely to challenge its own decisions. Use an independent instance for review.

### Context for CI-Invoked Claude
- **CLAUDE.md** is the mechanism for giving CI-invoked Claude project context: testing standards, fixture conventions, review criteria — improves test-generation quality and reduces low-value output
- **Existing test files in context** when generating tests → avoids suggesting duplicate scenarios already covered by the suite

---

## §3.9 Structured Output from Claude Code CLI

```bash
claude -p "Review this PR for security" --output-format json --json-schema schema.json
```

- `--output-format json` — forces JSON output
- `--json-schema` — enforces schema (guarantees well-formed output parseable by downstream tools)

**Exam scenario:** Team wants to auto-post each finding as an inline GitHub PR comment (needs file path, line number, severity, suggested fix).
- ✅ `--output-format json` with `--json-schema` — reliable structured output for GitHub API parsing
- ❌ Add "Output Format" section to CLAUDE.md (not guaranteed consistent)
- ❌ Format instruction in prompt (variable compliance)

---

## §3.10 Message Batches API

### When to Use Batch vs Real-Time

| Use Case | API | Reason |
|---|---|---|
| Blocking pre-merge checks | Synchronous | Developers waiting; must complete quickly |
| Overnight tech-debt reports | Batch API | Flexible deadline; 50% cost savings |
| Nightly test generation | Batch API | Scheduled task; 24h window acceptable |
| Weekly security audits | Batch API | Not blocking; scheduled |

### Batch API Properties
- **Cost:** 50% savings vs synchronous
- **Latency:** Up to 24 hours (no SLA)
- **Identifier:** `custom_id` per request for matching outputs to inputs
- **Limitation:** No multi-turn tool calling — batch is fire-and-forget; cannot execute a tool mid-request and return results

**Exam trap:** Iterative code review that fetches related files via tool calls mid-analysis → **cannot use batch API** because batch cannot execute tools during a request and return results to Claude.

---

## §3.11 CLAUDE.md Content Organization Best Practices

**Exam scenario:** CLAUDE.md grew to 400+ lines mixing coding standards, PR checklists, deploy instructions, migration procedures.

- ✅ Keep universal standards in CLAUDE.md; create Skills for workflow-specific guidance (PR review, deploy, migrations) with trigger keywords
- Why: CLAUDE.md content loads in every session; Skills are invoked on demand
- Not preferred: Move everything to Skills (universal standards would need explicit invocation each time)
- Not preferred: Split CLAUDE.md into `.claude/rules/` (rules are path-scoped, not workflow-scoped)

**Exam scenario:** CLAUDE.md 500+ lines, hard to navigate.
- ✅ Create separate Markdown files in `.claude/rules/`, each covering one topic (testing.md, api-conventions.md, deployment.md)
- This is the supported modularization approach for instruction organization
- `@import` (see §3.1) is the complementary approach when content should remain part of the concatenated CLAUDE.md context but live in separate files

---

## §3.12 Session Management

| Feature | Purpose |
|---|---|
| `--resume` | Resume a previous (named) Claude Code session with saved context |
| `fork_session` | Create a branch of the current session — both forks inherit context up to the branch point, then diverge (useful for comparing approaches) |
| `/compact` | Compress context while preserving essential information — risk: exact numeric values, dates, and specific details can be lost in summarization |
| `/memory` | Verify which memory files are loaded; manage persistent memory (see §3.1) |

**When to start a NEW session instead of resuming:** tool results are stale (files changed since), or context has degraded — better to restart with a short summary of prior findings than resume with old tool data.

**Exam scenario:** Discovery phase fills context window before implementation phase.
- ✅ Use Explore subagent for discovery (isolates verbose output), returns summary to main session
- ❌ Use `/compact` mid-task (loses precision; implementation needs the full context)



# Part 4 - Domain 4: Prompt Engineering & Structured Output (20%)

## §4.1 Few-Shot Prompting

### When to Use
Few-shot examples are the most effective technique when:
- **Prose instructions produce inconsistent output** — examples show exact expected format
- **Ambiguous tool selection** — examples for the specific ambiguous cases (not generic cases)
- **Multi-issue request handling** — examples demonstrate correct decomposition and sequencing
- **Escalation calibration** — examples show "escalate this / don't escalate this"

### Critical Principle: Target the Ambiguous Cases
Do not add 10–15 examples of clear, unambiguous cases. Target the 4–6 examples at exactly the cases where the model gets it wrong.

**Exam scenario:** Agent misroutes "I need help with my recent purchase" — ambiguous between `get_customer` and `lookup_order`.
- ✅ Add 4–6 examples targeted at ambiguous scenarios, each with rationale for why one tool was chosen over alternatives
- ❌ Add 10–15 examples of clear, unambiguous requests (doesn't help with the edge cases)

**Exam scenario:** Automated review generates inconsistent feedback format despite instructions.
- ✅ Add 3–4 few-shot examples showing exact required format: identified issue, location in code, concrete fix
- ❌ Further refine instructions with more explicit requirements (instructions are already failing)

---

## §4.2 Chain-of-Thought / Reasoning Cues

### Step-by-Step Instruction
Including "Think step by step before answering" improves accuracy on multi-step reasoning tasks.

### When Required (R5 in Compliance Checklist)
Add a reasoning cue when the task requires:
- Multi-step mathematical reasoning
- Multi-stage analysis
- Comparison across N items
- Step-wise transformation

Do NOT add for single-step tasks (e.g., "translate this sentence to French").

---

## §4.3 System Prompt Design

### Persistent Behavioral Constraints Belong in the System Prompt
The system prompt is the correct location for:
- Tone and persona constraints
- Behavioral rules that apply for the entire conversation
- Response format requirements

**Exam scenario:** "Where should enthusiasm, reasoning transparency, and clarifying-question requirements live?"
- ✅ System prompt
- ❌ First user message (loses authority mid-conversation)
- ❌ Environment variables (no effect on model behavior)
- ❌ First assistant message (model can deviate from its own prior statements)

---

## §4.4 Prefilling (Response Seeding)

### What It Is
Including the beginning of an assistant message in the API call so Claude continues from it, rather than generating a new response from scratch.

### Use Cases
1. **Suppress filler phrases** ("Certainly!", "I'd be happy to help!") — append a direct opening partial response; Claude continues from it
2. **Inject real-time context** into next response — prefix the next user message with the event data ("Your package has shipped. Now: [user message]")

**Exam scenario:** Users report repetitive "Certainly!" openings.
- ✅ Append a partial assistant message with a direct response opening (prefilling)
- ❌ Lower temperature (controls randomness, not specific phrases)
- ❌ Post-process to remove greetings (fragile workaround)
- ❌ System prompt instruction to avoid those phrases (less reliable)

**Exam scenario:** Webhook fires during active chat session — package has shipped.
- ✅ Append the status update as a prefix to the next user message
- ❌ Modify the system prompt (requires rebuilding session)
- ❌ Send a synthetic user message (breaks natural dialogue flow)

---

## §4.5 JSON Schema Design for Tool Use / Structured Output

### Key Schema Design Decisions

| Situation | Schema Design |
|---|---|
| Field always present and never null | `required: [field]`, type is not nullable |
| Field sometimes absent | Omit from `required`; make nullable or use `anyOf: [type, null]` |
| Field has known values but might have new ones | `enum: ["A", "B", "other"]` with a companion `detail` field |
| Model cannot confidently pick a category | Add `"unclear"` to the enum — honest `"unclear"` beats a confident wrong category |
| Confidence score per field | Add `field_confidence: float [0,1]` alongside each field |
| Unclear from source | `nullable: true` — preserve ambiguity in output |

### Why Nullable Matters: Fabrication Prevention
Mark fields as `required` only if the information is **always** available in the source. A required, non-nullable field pushes the model to **fabricate values** to satisfy the schema when the data is missing. Nullable fields (`"type": ["string", "null"]`) let the model return `null` instead of hallucinating.

- ✅ Optional/nullable fields for information that may be absent → model returns `null`
- ❌ "Make every field required so the output is always complete" — completeness by fabrication, not extraction

### Format Normalization
Include format normalization rules **in the prompt** alongside the strict output schema when source documents have inconsistent formatting (dates, currencies, informal measurements). The schema constrains the shape; the prompt governs how messy inputs map into it.

---

## §4.6 Guaranteeing Structured Output: tool_use + tool_choice

### The Mechanism That Guarantees Structure
Defining a tool whose **input schema** is your desired output structure, then reading the structured data from the `tool_use` block, is the **most reliable** way to get schema-compliant structured output. The tool doesn't need to "do" anything — it exists to force schema-conformant JSON.

This **eliminates JSON syntax errors** (missing braces, trailing commas, wrong field types). Contrast with asking nicely in the prompt ("respond only with valid JSON matching this schema"), which the model may or may not honor — prompt-based JSON requests can still return prose preambles, markdown fences, or malformed JSON.

### tool_choice Modes

| Value | Behavior | When to use |
|---|---|---|
| `{"type": "auto"}` | Model decides whether to call a tool or answer in text | Default conversational use — **no structure guarantee** |
| `{"type": "any"}` | Model **must** call some tool | Guaranteed structured output when multiple extraction schemas exist and document type is unknown — model picks the best-fitting tool, but you always get structured output |
| `{"type": "tool", "name": "extract_metadata"}` | Model **must** call that specific tool | Forcing a particular extraction to run (e.g., metadata extraction before enrichment steps) |

**Exam scenario:** Pipeline must always receive schema-valid JSON; documents may be invoices, receipts, or contracts (three extraction tools defined).
- ✅ `tool_choice: {"type": "any"}` — model must call one of the tools; output is always structured
- ❌ `tool_choice: {"type": "auto"}` — model may answer in free text instead of calling a tool
- ❌ Prompt instruction "always respond with JSON" — no guarantee; syntax errors and prose wrappers still occur
- ❌ Post-process free-text responses with a JSON repair library (treats the symptom; tool_use removes the problem at the source)

**Exam scenario:** Enrichment step keeps running before metadata extraction has produced its output.
- ✅ Force the specific tool: `tool_choice: {"type": "tool", "name": "extract_metadata"}` on the first call
- ❌ `tool_choice: "any"` (guarantees *a* tool call, not *that* tool)

### ❌ Misconception
"tool_use with a strict JSON schema guarantees the output is **correct**." — It guarantees the output is **syntactically valid and schema-shaped**. Values can still be semantically wrong (see §4.7). Schema compliance ≠ content correctness.

---

## §4.7 Syntax vs Semantic Errors

The exam's core distinction for extraction quality:

| Error type | Examples | Detected by | Fixed by |
|---|---|---|---|
| **Syntax** | Malformed JSON (missing brace, trailing comma), wrong field type, missing required field — schema violations | Programmatic validators (JSON Schema, Pydantic) — deterministic, catches 100% | `tool_use` with a JSON schema **eliminates** these; otherwise retry-with-feedback fixes them |
| **Semantic** | Valid JSON but wrong content: line items don't sum to `total`, value placed in the wrong field, hallucinated value, wrong category | Business-rule validation, cross-field checks, self-correction fields | Validation checks + retry with the specific error; self-correction patterns (§4.10); sometimes human review |

**Key insight:** strict schemas via tool use eliminate the entire syntax class but do **nothing** for the semantic class. A response can pass schema validation perfectly and still claim an invoice total of $150 when the line items sum to $145.

**Exam scenario:** Extraction pipeline moved to tool_use with strict schemas; JSON parse failures dropped to zero, but downstream reconciliation still finds totals that don't match line items.
- ✅ Expected behavior — schemas eliminated syntax errors; the remaining failures are semantic and need validation + feedback loops
- ❌ "The schema must be wrong — tighten it further" (no schema constraint can verify that numbers sum correctly)
- ❌ "Tool use is unreliable, revert to prompt-based JSON" (would reintroduce the syntax error class on top of the semantic one)

### ❌ Misconception
"A validator that passes means the extraction is correct." — A schema validator proves only structural validity. Semantic errors sail through schema validation by definition: the JSON is valid, the content is wrong.

---

## §4.8 Programmatic Validation: Pydantic / Typed Schemas

The validation layer sits **in your code, after** receiving JSON from Claude — never trust model output unvalidated.

### What Pydantic (or equivalent typed-schema validation) Gives You
1. **Structural validation** — types, requiredness, enum membership checked deterministically in code
2. **Semantic validation** — custom validators encode business logic: `sum(line_items) == total`, `start_date < end_date`
3. **Validate–retry loops** — on validation failure, Pydantic's error message becomes the feedback for the retry prompt (§4.9)
4. **Single source of truth** — Pydantic models can **generate the JSON Schema** used in the tool definition, so the tool's input schema and your code's validator can never drift apart

**Exam scenario:** Team maintains the tool's JSON schema by hand and a separate validation class; they keep drifting out of sync.
- ✅ Generate the tool's JSON Schema from the Pydantic model — one definition drives both the tool_use contract and post-hoc validation
- ❌ Add a code-review checklist item to update both files (process patch for an architecture problem)

### ❌ Misconception
"tool_use already enforces the schema, so validating again in code is redundant." — Tool use enforces structure at generation time, but your code should still validate: (a) semantic/business rules that no JSON schema can express, and (b) defense-in-depth for anything downstream consumes. The schema constrains shape; Pydantic validators check meaning.

---

## §4.9 Retry-with-Feedback Loop — and Its Limits

### The Loop
When extraction fails validation:
```
1. Send: document + extraction prompt
2. Receive: extracted JSON
3. Validate against schema + business rules (Pydantic)
4. If invalid: retry with original document + incorrect extraction + specific validation error
5. Repeat until valid or max retries reached
```

**Critical:** Include the **specific validation error** in the retry prompt, not just "try again."
> "Field 'total' = 150, but sum(line_items) = 145. Re-check values."

The retry request contains three things: the original document, the previous (failed) extraction, and the specific error.

### When Retry WILL Help
- **Format errors** — date in the wrong format, wrong number representation
- **Structural errors** — a value placed in the wrong field
- **Arithmetic inconsistencies** — the model can re-check and re-derive

### When Retry Will NOT Help
- **The information is genuinely absent from the source document** — no number of retries can extract what isn't there
- **The required context is external** — the data lives in another document that wasn't provided

Retrying in these cases **burns tokens for nothing** — and worse, pressure to fill a required field can push the model into fabrication. The correct design: nullable/optional fields (§4.5) so the model returns `null`/absent, and your pipeline treats "not found" as a legitimate answer, not a failure to retry.

**Exam scenario:** Extraction of `purchase_order_number` fails validation on 40 documents; investigation shows those documents never contained a PO number.
- ✅ Make the field nullable; accept `null`; stop retrying — the information is absent, retries waste tokens and invite fabrication
- ❌ Increase max retries from 3 to 10 (absent information stays absent)
- ❌ Strengthen the retry feedback message (no feedback can conjure missing data)
- ❌ Keep the field required "for data quality" (guarantees fabricated values)

### detected_pattern Tracking Across Retries and Findings
Add a `detected_pattern` field to structured findings/extractions identifying **which construct triggered the finding**. This enables systematic analysis:
- When developers dismiss findings, group dismissals by `detected_pattern` to find which patterns drive false positives
- Across retries, track which patterns repeatedly fail validation to identify systematic prompt/schema weaknesses rather than treating each failure as an isolated event

**Exam scenario:** Review tool's findings are frequently dismissed but the team can't tell which finding types are noise.
- ✅ Add a `detected_pattern` field to each finding; analyze dismissal rates per pattern
- ❌ Ask developers to write a free-text reason on every dismissal (unstructured; doesn't aggregate)

### ❌ Misconception
"If validation fails, retrying with feedback always converges on a correct answer." — Retry-with-feedback only fixes errors the model *can* correct from the provided context (format, structure, arithmetic). For absent information, retry is pure waste; the fix is schema design (nullable) not loop tuning.

---

## §4.10 Self-Correction Patterns

Have the model **re-derive and compare** within a single structured output, so internal contradictions surface as data instead of hiding.

### stated_total vs calculated_total
```json
{
  "stated_total": "$150.00",
  "calculated_total": "$145.00",
  "conflict_detected": true,
  "line_items": [
    {"name": "Widget A", "price": 75.00},
    {"name": "Widget B", "price": 70.00}
  ]
}
```
- `stated_total` — the value as written in the document
- `calculated_total` — the model re-derives the total from the extracted line items
- `conflict_detected` — boolean flag when they disagree

This catches **arithmetic drift** (extraction picked up the wrong number, or the source document itself is inconsistent) and lets your pipeline route conflicts to review instead of silently trusting either number. The same pattern generalizes: extract both the claimed value and an independently derived value; flag disagreement with a boolean.

**Exam scenario:** Invoice pipeline occasionally reports totals that don't match line items, discovered weeks later in reconciliation.
- ✅ Extract `calculated_total` alongside `stated_total` with a `conflict_detected` flag; route conflicts for handling at extraction time
- ❌ Post-hoc monthly reconciliation report (detection weeks late; the pattern moves it to extraction time)
- ❌ Prompt "be careful with totals" (vague instruction; no detection mechanism)

### ❌ Misconception
"Self-correction means asking the model 'are you sure?' after it answers." — The exam pattern is **structural**: build the re-derivation into the output schema (stated vs calculated + conflict boolean) so checking happens on every extraction and produces machine-readable signals — not an optional conversational follow-up.

---

## §4.11 Batch Processing Strategy (Message Batches API)

### Core Facts

| Attribute | Value |
|---|---|
| Cost | **50% discount** vs synchronous calls |
| Processing window | Up to **24 hours**; most batches complete much faster — but there is **no latency SLA** |
| Correlation | `custom_id` per request — the join key between requests and results |
| Tool use / multi-turn | **Supported** — batch requests can include tools and full multi-turn message histories (see accuracy note below) |

### Batch vs Synchronous — Match API to Latency Tolerance

| Task | API | Why |
|---|---|---|
| Pre-merge PR check | **Synchronous** | The developer is waiting; up to 24h is unacceptable |
| Overnight tech-debt report | **Batch** | Result needed by morning; 50% savings |
| Weekly security audit | **Batch** | Not urgent; 50% savings |
| Interactive code review | **Synchronous** | Immediate response required |
| Processing 10,000 documents | **Batch** | Bulk; savings are significant |

Batch is for **non-blocking, latency-tolerant** workloads (overnight reports, weekly audits, nightly test generation); synchronous for anything a human or pipeline is blocking on.

### custom_id: The Join Key (Required Discipline)
Batch results **can arrive in any order** — there is no guaranteed correspondence between submission order and result order. `custom_id` is how you match each result back to its originating request:
- Link the result to the original document (`"custom_id": "doc-invoice-2024-001"`)
- Identify exactly which items failed
- Avoid re-processing successful items

- ✅ Assign a meaningful, unique `custom_id` to every request in every batch
- ❌ Rely on result ordering to match results to inputs (ordering is not guaranteed — this silently mis-joins data)

### Selective Re-submission After Partial Failure
```
1. Submit a batch of 100 documents
2. 95 succeed; 5 fail (e.g., context limit exceeded)
3. Identify the 5 failures by custom_id
4. Modify strategy for those items (e.g., chunk the long documents)
5. Re-submit ONLY the 5 failed documents
```
- ✅ Re-submit only failures, identified by `custom_id`, with an appropriate modification
- ❌ Re-submit the entire batch of 100 (pays again for 95 successes; may produce duplicate results downstream)
- ❌ Re-submit the 5 failures unchanged (they failed for a reason — fix the cause, e.g., chunking, before retrying)

### SLA Planning: Budget the 24-Hour Worst Case
Plan submission windows against the **worst case** (24h), not the typical case:
- Need results within 30 hours? Submission window = 30 − 24 = **6 hours**. Batches must be submitted no later than 24 hours before the downstream deadline.
- For a recurring pipeline with a 30-hour SLA, split submissions into 4-hour windows so every batch has the full 24h buffer before its deadline.

- ✅ Submission deadline = downstream deadline − 24h
- ❌ Plan around "batches usually finish in an hour" (no SLA — the one batch that takes 23 hours blows your deadline)

### Sample-First Iteration
Before committing a large batch, validate the prompt on a **small synchronous sample**:
1. Run the extraction prompt synchronously on a representative sample (fast feedback)
2. Refine prompt/schema until the sample passes validation
3. Only then submit the full batch

This maximizes first-pass success and avoids paying (and waiting up to 24h) to discover a prompt defect replicated across 10,000 requests.

- ✅ Refine on a synchronous sample set first, then batch the volume
- ❌ Submit the full 10,000-document batch and iterate on the whole batch (each iteration costs a full batch and up to 24h)

### ⚠️ Accuracy Note: Tool Use in Batches (verified against platform.claude.com docs, 2026-07-06)
The Batch API **does support tool use and multi-turn conversations** — a batch request's `params` are the same as a regular Messages API call, including `tools` and multi-message histories. Older study materials claiming "batches cannot use tools" are **wrong**.

What batches cannot do is **interactive back-and-forth within one request's processing**: each batch request is self-contained — if the model responds with `tool_use`, that batch request completes with that response. Your client cannot execute the tool and return a `tool_result` *mid-request*; continuing the loop requires submitting a follow-up request (in a new batch or synchronously) with the tool result appended.

- ✅ Batch request with `tools` defined and a multi-turn history → valid; response may end in `tool_use`
- ❌ "The Batch API doesn't support tools" (outdated/false)
- ❌ Expecting the batch to pause while your client answers a mid-request tool call (each request is one shot: submit → single model response)

### ❌ Misconception
"Batch = 50% cheaper synchronous API with a delay, so use it everywhere and just poll faster." — Batch has **no latency SLA**; anything blocking (pre-merge checks, interactive flows) must stay synchronous, and every batch deadline calculation must absorb the full 24-hour worst case.

---

## §4.12 Multi-Pass Review Architecture

When a single pass over many items produces inconsistent results (attention dilution):

**Problem:** Single-pass review of 14-file PR produces:
- Detailed comments on some files, shallow on others
- Missed obvious bugs
- Contradictory feedback (same pattern flagged in one file, approved in another)

**Root cause:** Attention dilution when processing many items at once.

**Solution:** Focused passes
1. Per-file pass: review each file individually for local issues
2. Integration pass: separate pass examining cross-file data flows

**Exam trap:** "Switch to a larger model with bigger context window" — wrong. Larger context does not fix attention quality. The attention quality issue exists regardless of window size.

---

## §4.13 Multi-Instance Independent Review

### Why Self-Review Falls Short
A model that generated code **retains the reasoning context from generation**. Within the same session, it is anchored to its own decisions and less likely to question them — the same blind spots that produced a bug tend to survive a same-session re-check.

### The Pattern: True Independence
Send the generated output to a **second Claude instance with no access to the first instance's reasoning** — a fresh request containing only the artifact to review (plus review criteria), not the generation conversation. Without the generator's justifications in context, the reviewer evaluates the code on its own merits and catches subtle issues the generator rationalized away.

**Exam scenario:** Generated code passes its own "review your work carefully" step but bugs keep reaching production.
- ✅ Route the output to a second, independent Claude instance that never sees the generator's reasoning
- ❌ Add "review your own code thoroughly before finishing" to the generator's prompt (self-review inside the same context inherits the same anchoring)
- ❌ Enable extended thinking on the generator (more reasoning by the same anchored instance ≠ independent scrutiny)
- ❌ Ask for a "second pass" in the same conversation (see misconception below)

### Confidence-Calibrated Routing
In verification passes, have the reviewing model **self-report confidence alongside each finding** so downstream routing can be calibrated — e.g., high-confidence findings auto-comment, low-confidence findings route to human review.

### ❌ Misconception
"Asking the same conversation for a second review pass gives you an independent review." — It does not. A second pass **in the same conversation** still carries the full generation reasoning in context; the model re-reads its own justifications and confirms them. Independence requires a **separate instance/request without the first's reasoning context**. Same-conversation second pass ≠ independent review.

---

## §4.14 Prompt Chaining

Break complex tasks into sequential focused prompts where each step's output feeds the next.

**Examples from practice scenarios:**
- Step 1: Identify issues in code
- Step 2: Generate fixes for identified issues
- Result: More focused, consistent output at each stage

---

## §4.15 Escalation and Confidence Routing

### When to Escalate (Explicit Criteria Approach)
Add explicit escalation criteria with few-shot examples to the system prompt showing:
- "Escalate when: [scenario]"
- "Resolve autonomously when: [scenario]"

**Exam scenario:** Agent escalates simple standard replacements (photo-proven damage) but tries to handle complex policy exceptions autonomously. First-contact resolution 55%, target 80%.
- ✅ Add explicit escalation criteria with few-shot examples distinguishing simple vs complex
- ❌ Self-confidence rating + automatic routing threshold (adds infrastructure without addressing root cause)
- ❌ Separate classifier model (overkill; root cause is unclear decision boundaries in prompt)

---

## §4.16 Instruction Specificity vs Abstraction

When vague instructions produce inconsistent output, move from abstract to concrete.

| Problem | Abstract instruction | Concrete fix |
|---|---|---|
| Review flags wrong comments | "Check that comments are accurate" | "Flag comments only when the behavior they claim contradicts the code's actual behavior" |
| Review has inconsistent severity | "Rate severity appropriately" | Define explicit criteria for critical/high/medium/low with examples |

**Exam pattern:** Replace vague intent ("check accuracy") with explicit, testable criteria ("flag only when claimed behavior contradicts actual behavior").

---

## §4.17 Trust Restoration via Category Management

**Exam scenario:** Automated review has 52% false positives on style, 48% on documentation, 8% on security, 18% on performance. Developers dismiss all findings.

- ✅ **Temporarily disable high-false-positive categories** (style, naming, documentation); keep only high-precision categories while improving prompts
- ❌ Display confidence scores (still shows all findings; trust still eroded)
- ❌ Add few-shot examples across all categories over several weeks (slow; trust continues to erode)
- ❌ Uniform strictness reduction (damages high-precision categories unnecessarily)

**Why:** High-false-positive categories cause developers to dismiss everything, including real findings in accurate categories. Surgical disabling stops the trust bleed while you fix the noisy categories.

---

## §4.18 Context-Aware Suggestions (Deduplication)

**Exam scenario:** Automated tool suggests 10 test cases for a PR, but 6 duplicate existing tests.
- ✅ Include the existing test file in context — Claude can only avoid duplicates if it knows what exists
- ❌ Reduce requested count to 5 (assumes priority ordering)
- ❌ Post-process with keyword matching (fragile, misses semantic duplicates)

---

## §4.19 Clarification Strategy — Proceed vs Ask

**When users send vague requests:**
- Do NOT ask 4+ clarifying questions (causes 35–40% abandonment)
- ✅ State assumptions explicitly and proceed, inviting corrections
- ❌ Ask all questions in one compound message (still demands effort from user)
- ❌ Use hidden defaults (user unaware of what was assumed)

**Exam pattern:** "Can you help with the report?" / "Book a venue for the party"
- ✅ Proceed with stated reasonable assumptions
- This applies both to user-facing assistants AND multi-agent systems (synthesis agent should not block awaiting coordinator clarification on all gaps)

---

## §4.20 Behavioral Drift Mitigation

### What It Is
As assistant responses accumulate in conversation history, system prompt influence dilutes relative to the growing body of assistant-generated content. The model increasingly pattern-matches its own prior outputs.

### Fixes

| Fix | When |
|---|---|
| Inject user-role reminder messages at conversation breakpoints | Persistent behavioral constraint drift |
| Replace verbose rules with few-shot examples | Long system prompt with abstract rules that fail after 10–15 turns |
| Prefill partial assistant response | Suppressing specific response patterns |

**Exam scenario:** Contractor persona assistant gives generic advice by turn 7, conversation only 2,500 tokens.
- Root cause: ✅ Accumulated assistant responses dilute system prompt influence (not context window overflow, not "system prompt only applies once")

**Exam scenario:** AI tutor 2,800-token system prompt; ignores proficiency levels after 12 turns.
- ✅ Replace verbose rules with few-shot examples demonstrating proficiency-level adaptation
- ❌ Periodic reminder injection every 4–5 turns (addresses symptoms, not root cause)



# Part 5 - Domain 5: Context Management & Reliability (15%)

## §5.1 Stateless API — The Fundamental Constraint

Claude's API is **fully stateless**. Every API call is independent. Claude has no server-side memory or session state.

**Implication:** Every request must include the complete conversation history in the `messages` array. Without this, Claude has no knowledge of prior turns.

**Exam scenario:** User says "I love jazz" in turn 1. Two turns later, Claude asks "What genres do you enjoy?"
- Root cause: ✅ Application is not including prior messages in the `messages` array
- Not: context window exceeded (impossible in a 3-turn conversation)
- Not: Claude needs a `session_id` parameter (doesn't exist)
- Not: Claude needs a vector database for memory (not the core API behavior)

**Exam scenario:** Latency and cost increase as conversations grow past 50 turns.
- Root cause: ✅ The entire conversation history is included with each API request — more turns = more tokens = more cost and latency
- Not: model generates progressively longer responses
- Not: database operations slowing down

---

## §5.2 "Lost in the Middle" Phenomenon

### What It Is
When large input is provided, Claude reliably processes content at the **beginning and end** of the context but has degraded attention on content in the **middle** of long inputs.

### Mitigation Strategies

1. **Key-findings summary at the start** — put the most critical information in the most reliably processed position (primacy)
2. **Explicit section headings** throughout — help the model navigate mid-input content
3. **Structured data over verbose content** — have upstream agents return key facts + citations rather than full page content + reasoning traces

**Exam scenario:** Synthesis agent processing 75K token input reliably uses first 15K (headlines) and last 10K (conclusions) but misses critical findings in middle 50K.
- ✅ Place key-findings summary at the start; add explicit section headings throughout
- ❌ Summarize to under 20K (might lose critical information)
- ❌ Alternate which agent appears first (rotation doesn't fix the fundamental attention pattern)

**Exam scenario:** 155K token combined output (85K web + 70K docs) but synthesis works best under 50K.
- ✅ Modify upstream agents to return structured data (key facts, quotes, relevance scores) instead of verbose content and reasoning traces — fixes root cause at the source
- ❌ Add intermediate summarization agent (adds latency, another potential point of failure)

---

## §5.3 Context Window Management Strategies

### Hybrid Approach (Most Tested)
For long conversations needing context management:
1. **Extract critical structured data** (amounts, dates, IDs, allergies, agreed prices) into a compact structured block — preserved verbatim
2. **Summarize general discussion** — compress lower-information-density exchanges
3. **Keep recent exchanges verbatim** — maintain conversational coherence for current turn

**Why not pure summarization:** Precision is lost. Amounts like "the 15% discount I mentioned" become "promotional pricing was discussed."

**Exam scenario:** 40-minute cooking session reaches 78K tokens. Contains: allergies, recipe scaling, clarified terms, general chatter.
- ✅ Extract allergies/quantities into structured block, summarize general discussion, keep recent exchanges verbatim
- ❌ Summarize entire history (loses allergy precision — safety risk)
- ❌ Keep only most recent 20K tokens (loses allergies if mentioned early)

---

## §5.4 Transactional Facts Persistence

**Problem pattern:** In long customer support conversations, precise amounts/dates/numbers get summarized into vague references.
- "The 15% discount I mentioned 20+ turns ago" → "promotional pricing was discussed"

**Solution:** Extract transactional facts into a **persistent "case facts" block** included in every prompt, outside the summarized history.

```
=== CASE FACTS (updated whenever a new fact appears) ===
Customer ID: CUST-12345
Order ID: ORD-67890
Order Amount: $89.99
Issue: Damaged item on delivery
Status: Pending manager approval
===
```

**Exam pattern:**
- ✅ Case facts block outside summarization (survives context compression)
- ❌ Increase summarization threshold (still eventually gets compressed)
- ❌ Revise summarization prompt to preserve numbers (still relies on summarizer being perfect)
- ❌ External storage + retrieval (overkill for session-level facts)

---

## §5.5 Trimming Verbose Tool Outputs

Tool results accumulate in context and **consume tokens disproportionately to their relevance**. A single `lookup_order` call can return 40+ fields when only 5 matter for the current task — and every one of those fields stays in the conversation for every subsequent turn.

**Solution:** Trim tool outputs to only the relevant fields **before** they enter context — e.g., via a `PostToolUse` hook:

```python
# PostToolUse hook: keep only return-relevant fields
@hook("PostToolUse", tool="lookup_order")
def trim_order_fields(result):
    return {
        "order_id": result["order_id"],
        "status": result["status"],
        "total": result["total"],
        "items": result["items"],
        "return_eligible": result["return_eligible"]
    }
```

This conserves context and reduces noise — the model isn't distracted by irrelevant fields, and long multi-issue sessions don't exhaust the window on tool clutter.

**Exam pattern:**
- ✅ PostToolUse hook filters tool results to relevant fields before they accumulate in context
- ❌ Ask the model in the system prompt to "ignore irrelevant fields" (the tokens are still consumed; attention cost remains)
- ❌ Summarize the whole conversation more aggressively (treats the symptom — verbose tool results keep flooding in)
- ❌ Increase the context window / switch to a larger model (cost goes up; noise problem remains)

---

## §5.6 Context Isolation with Subagents

Subagents receive only what the coordinator explicitly passes. This is both a constraint and a feature.

**As a feature (context isolation for exploration):**
- Use an Explore subagent to run verbose discovery (hundreds of call sites, large output)
- Subagent returns a concise summary to the main conversation
- Main session context preserved for design and implementation phases

**Exam scenario:** Adding error-handling wrappers across 120-file codebase. Phase 1 (discovery) fills context window before completion.
- ✅ Use Explore subagent for Phase 1 to isolate verbose output; returns summary; Phases 2–3 run in main conversation
- ❌ Use `/compact` mid-task (loses precision needed for implementation)
- ❌ Multiple sessions with `--continue` (coordination overhead, consistency risk)

---

## §5.7 Long-Term Conversation Memory

For conversations spanning many sessions (e.g., book club discussions over 3 months, 85K tokens):
- Rolling window: loses early sessions
- Progressive summarization: loses specific quoted conclusions
- ✅ **Semantic retrieval** (embeddings over full history) — retrieves specifically relevant past exchanges on demand

**Exam scenario:** "What did we conclude about the theme of isolation?" — needs specific past exchange.
- ✅ Semantic embeddings with retrieval of relevant exchanges
- ❌ Rolling window (discards most history)
- ❌ Progressive summarization (compresses specific conclusions into abstractions)
- ❌ XML tags marking discussion conclusions (doesn't solve retrieval at this scale)

---

## §5.8 Escalation and Ambiguity Resolution

### Reliable Escalation Triggers (Structural Signals)

| Situation | Action |
|---|---|
| Customer explicitly asks for a human/manager | Escalate immediately; do NOT attempt to solve first |
| Policy is silent or ambiguous on the request | Escalate (e.g., competitor price matching when policy only covers own-site adjustments) |
| Agent cannot make meaningful progress | Escalate after a reasonable number of attempts |
| Financial operation above a threshold | Escalate — preferably enforced via a hook, not just a prompt |
| Repeated tool/lookup failures | Escalate with what was attempted |

### Unreliable Complexity Proxies

**Sentiment and model self-confidence are NOT reliable escalation signals:**

| Unreliable proxy | Why it fails |
|---|---|
| Sentiment analysis | Customer mood does not correlate with case complexity — a calm message can describe a genuinely complex case; an angry one can be trivially resolvable |
| Model self-rated confidence (e.g., 1–10) | The model can be confidently wrong; uncalibrated self-reported confidence is poorly correlated with actual difficulty |
| Automatic complexity classifier | Overengineering; requires training data you likely don't have |

Escalate on **structural signals** — policy limits, missing data, explicit human requests, repeated failures — not on inferred emotion or self-assessed confidence.

### Escalation Patterns

**Immediate escalation** (explicit request):
```
Customer: "I want to speak to a manager"
Agent: [immediately calls escalate_to_human]
NOT: "I can help with your issue, let me first..."
```

**Nuanced escalation** (frustration ≠ human request):
```
Customer: "This is outrageous, I'm very unhappy!"
Agent: [acknowledges frustration] → [offers concrete resolution]
Customer: "No, I want to talk to someone!"
Agent: [customer reiterates → escalate immediately]
```
Key principle: acknowledge emotion, propose a solution, escalate only if the customer reiterates the desire for a human. First expression of dissatisfaction is not a request for a manager.

### Multiple-Match Disambiguation

When a customer lookup returns **several matching records**, the agent must **request additional identifiers** (email, order number, phone) — never pick a match by heuristic.

**Exam pattern:**
- ✅ "I found several accounts under that name — could you confirm the email or order number?" (clarification via additional identifiers)
- ❌ Select the most recently active account (heuristic selection → misidentified accounts, incorrect refunds)
- ❌ Select the first result returned by the tool (arbitrary; same misidentification risk)
- ❌ Escalate to a human immediately (unnecessary — the ambiguity is resolvable by asking)

**Exam pattern (escalation design):**
- ✅ Add explicit escalation criteria with few-shot examples to the system prompt showing when to escalate vs. resolve autonomously
- ❌ Escalate whenever sentiment analysis detects anger (mood ≠ complexity; floods human queue with resolvable cases)
- ❌ Have the model rate its own confidence 1–10 and escalate below 7 (self-reported confidence is uncalibrated and unreliable)
- ❌ Never escalate until three resolution attempts have been made (violates the immediate-escalation rule for explicit human requests)

---

## §5.9 Human Oversight and Confidence Calibration

For high-volume extraction/processing systems (e.g., document data extraction), design the human review workflow around **calibrated confidence** and **stratified measurement** — official task 5.5.

### Field-Level Confidence Scores, Calibrated

1. **Field-level confidence:** the model outputs a confidence score per extracted field (not one score per document)
2. **Calibration:** tune review thresholds against a **labeled validation set** — raw self-reported confidence is unreliable until calibrated against ground truth
3. **Routing:**
   - High confidence + validated stable accuracy → automated processing
   - Low confidence, or ambiguous/contradictory source documents → human review

This prioritizes limited reviewer capacity where it matters most.

### Stratified Random Sampling

Even for high-confidence extractions, **regularly audit a random sample** — stratified across document types and field categories, not just the top of the review queue. This measures the true error rate of the automated path and detects **novel error patterns** before they compound.

### The Aggregate-Accuracy Masking Trap

**An aggregate 97% accuracy can hide a 40% failure rate on one rare document type.** Overall metrics average away segment-level failures. Before reducing human review, validate accuracy **by document type and by field** — every segment must independently meet the bar.

**Exam scenario:** Extraction system shows 97% overall accuracy; team proposes auto-processing all high-confidence extractions.
- ✅ First analyze accuracy by document type and field segment; implement stratified random sampling of high-confidence extractions for ongoing error measurement
- ❌ Auto-process everything above the aggregate confidence threshold (aggregate masks per-segment failure — a rare document type may fail 40% of the time)
- ❌ Trust the model's self-reported confidence directly without calibration (uncalibrated confidence is unreliable; thresholds must be tuned on a labeled validation set)
- ❌ Review only the extractions flagged lowest-confidence and skip auditing the high-confidence stream (novel error patterns in the automated path go undetected)
- ❌ Sample only from the most common document type (the rare, worst-performing segments are exactly the ones under-sampled)

**Exam pattern (review routing):**
- ✅ Route low-confidence and ambiguous/contradictory-source extractions to human review; auto-process only segments with validated accuracy
- ❌ Route a fixed 10% of all documents to review at random, unstratified (wastes reviewer capacity on easy segments, undersamples problem segments)
- ❌ Have humans re-review every document (defeats automation; doesn't scale — the point of calibration is targeted oversight)

---

## §5.10 Conflict Detection and Source Attribution

When processing multiple conflicting sources, the agent should **not resolve conflicts autonomously**. Instead:
1. Complete analysis with both conflicting values
2. Explicitly annotate the conflict with source attribution
3. Let the coordinator (or human) reconcile

**Exam scenario:** Document analysis agent finds government report = 40% growth, industry analysis = 12% growth. Both credible.
- ✅ Complete analysis with both values, explicitly mark conflict with source attribution, let coordinator decide reconciliation
- ❌ Apply heuristics to pick most likely correct value (abandons responsibility for a decision above its scope)
- ❌ Stop and ask coordinator before completing analysis (blocks pipeline unnecessarily)

---

## §5.11 Provenance: Claim→Source Mapping, Dates, and Rendering

Official task 5.6 goes beyond conflict annotation: provenance must **survive synthesis**.

### The Attribution Loss Problem

Source attribution is lost during summarization when findings are compressed without preserving claim→source mappings:

```
Bad:  "The AI music market is estimated at $3.2B."   (no source, no year)

Good:
{
  "claim": "The AI music market is estimated at $3.2B.",
  "source_url": "https://example.com/report",
  "source_name": "Global AI Music Report 2024",
  "publication_date": "2024-06-15",
  "confidence": 0.9
}
```

Require subagents to output **structured claim→source mappings** (source URL/document name + relevant excerpt/location), and require downstream synthesis agents to **preserve and merge** these mappings — so the final report can attribute every claim.

### Publication Dates Prevent False Contradictions

Without dates, **temporal differences get misinterpreted as contradictions**:

```
Bad:  "Source A says 10%, source B says 15%. Contradiction."
Good: "Source A (2023) says 10%, source B (2024) says 15%. Likely +5% growth over a year."
```

Require publication or data-collection dates in every structured output. Two sources "disagreeing" may simply describe different time periods.

### Render by Content Type

Don't flatten everything to uniform prose in synthesis outputs:
- Financial/tabular data → **tables**
- News and analysis → **prose**
- Technical findings → **structured lists**
- Time series → **chronological ordering**

**Exam pattern:**
- ✅ Subagents emit structured claim→source mappings with publication dates; synthesis preserves them; report renders each content type appropriately
- ❌ Have the synthesis agent add a general bibliography at the end (individual claims are no longer traceable to specific sources)
- ❌ Flag every numeric disagreement between sources as a conflict (without dates, normal temporal change is misreported as contradiction)
- ❌ Convert all findings to uniform narrative prose for consistency (tabular financial data becomes imprecise and harder to verify)
- ❌ Re-derive attributions at the end by searching sources again (expensive, error-prone; the mapping should be preserved through the pipeline, not reconstructed)

Also structure final reports with explicit sections distinguishing **well-established findings** from **contested ones**, preserving original source characterizations and methodological context.

---

## §5.12 Scratchpad Files and Structured State Persistence

### Scratchpad Files for Large Tasks

For tasks requiring state across many tool calls (large migrations, refactoring projects, long investigations):
- Write intermediate state and key findings to a scratchpad file rather than holding it all in context
- Read from scratchpad at the start of each continuation
- This allows the task to survive context limits — and counteracts **context degradation**, where the model starts giving inconsistent answers and referencing "typical patterns" instead of the specific classes it discovered earlier

```
# investigation-scratchpad.md
## Key findings
- PaymentProcessor in src/payments/processor.ts inherits from BaseProcessor
- refund() is called from 3 places: OrderController, AdminPanel, CronJob
- External PaymentGateway API has a rate limit of 100 req/min
```

### Structured State Persistence for Crash Recovery

In multi-agent systems, each agent **exports its state to a known location**, and the coordinator **loads a manifest on resume**:

```json
// agent-state/web-search-agent.json
{ "status": "completed", "queries_executed": [...], "key_findings": [...],
  "coverage": ["music composition"], "gaps": ["music licensing"] }

// agent-state/manifest.json
{ "web-search": "completed", "doc-analysis": "in_progress", "synthesis": "not_started" }
```

On crash or restart, the coordinator reads the manifest, injects persisted findings into agent prompts, and **resumes from the checkpoint** instead of re-running the full investigation.

**Exam pattern:**
- ✅ Each agent exports structured state (status, findings, coverage, gaps) to a known location; coordinator loads manifest on resume and injects summaries into agent prompts
- ❌ Rely on conversation history to survive the crash (the API is stateless; an interrupted session's context is gone)
- ❌ Re-run the entire investigation from scratch after every failure (wastes hours of completed work that could have been persisted)
- ❌ Have agents keep all findings in their own context windows (context fills; nothing survives a crash)

---

## §5.13 Conversation-Level State Management

### The Sliding Window Problem
Keeping only the last N message pairs drops early preferences that may be critical later.

**Hybrid window approach:**
- Keep recent exchanges verbatim (sliding window)
- Maintain a running summary of earlier exchanges (compressed)
- Never drop the structured facts block

### System Prompt Instruction Drift
As conversations lengthen, system prompt authority diminishes relative to accumulated assistant responses.

**Preventive patterns:**
- Inject reminder messages at conversation breakpoints (reinforcement)
- Keep system prompt rules concrete and minimal (abstract rules drift faster than examples)
- Replace verbose rule lists with few-shot examples (examples maintain behavioral pattern longer)

---

## §5.14 Reliability Patterns Summary

| Problem | Root Cause | Solution Pattern |
|---|---|---|
| Agent loop never terminates | Not checking `stop_reason` | Check `stop_reason: "end_turn"` to exit loop |
| Precision lost in long conversations | Transactional facts compressed in summarization | Persistent case-facts block outside summarized history |
| Context bloat from tool calls | Verbose tool results (40+ fields) accumulate turn after turn | PostToolUse hook trims results to relevant fields |
| Subagent lacks upstream results | Context isolation — subagent doesn't inherit coordinator's history | Coordinator explicitly passes needed results in subagent prompt |
| Critical info missed in large input | Lost in the middle | Key-findings summary at start + section headings |
| Context window exhausted during discovery | Discovery output floods main session | Explore subagent for discovery; returns summary |
| Human queue flooded / wrong cases escalated | Sentiment or self-rated confidence used as complexity proxy | Escalate on structural signals: explicit requests, policy gaps, repeated failures |
| Wrong customer actioned | Heuristic selection among multiple lookup matches | Request additional identifiers to disambiguate |
| Errors slip through automated processing | Aggregate accuracy masks per-segment failure | Calibrated field-level confidence + stratified sampling + per-type/per-field accuracy tracking |
| Final report can't attribute claims | Claim→source mapping lost in summarization | Structured claim→source mappings preserved through synthesis |
| Sources falsely flagged as contradicting | Missing publication dates hide temporal differences | Require publication/collection dates in structured outputs |
| Work lost on crash | No persisted agent state | Structured state exports + manifest loaded on resume |
| Behavioral drift after many turns | Accumulated assistant responses dilute system prompt | Inject reminders at breakpoints; use few-shot over verbose rules |
| Data format inconsistency across tools | Multiple tools return different formats | PostToolUse hook for centralized normalization |



# Part 6 - Key Distinctions: high-yield exam traps

**Purpose:** Each entry is a documented exam trap — a pair of options that look similar but have a decisive difference. Understand the WHY, not just the answer.

## Configuration & File Location

### 1. Project scope vs User scope for CLAUDE.md

| | Project scope | User scope |
|---|---|---|
| Location | `.claude/CLAUDE.md` or root `CLAUDE.md` | `~/.claude/CLAUDE.md` |
| Version-controlled | ✅ Yes | ❌ No |
| Available to all team members | ✅ Yes | ❌ Only that user |
| Use for | Shared conventions, team standards | Personal preferences, personal workflow |

**Exam trap:** New team member doesn't follow convention that existing members do → convention is in `~/.claude/CLAUDE.md`, not the project file.

---

### 2. `.mcp.json` vs `~/.claude.json`

| | `.mcp.json` | `~/.claude.json` |
|---|---|---|
| Location | Project root | User home directory |
| Scope | Project | User across all projects |
| Version-controlled | ✅ Yes | ❌ No |
| Use for | Shared MCP server config | Personal auth, personal overrides |

**Exam pattern:** Team shares MCP server, each developer has their own token → `.mcp.json` with `${GITHUB_TOKEN}` env var substitution.

---

### 3. `.claude/rules/` vs CLAUDE.md vs Skills

| | CLAUDE.md | `.claude/rules/` | Skills |
|---|---|---|---|
| When loaded | Every session | When working on matching file paths | On-demand (slash command) |
| Best for | Universal standards | Path-scoped conventions | Workflow-specific guidance |
| Trigger | Always | Glob pattern match | User invokes `/skillname` |

---

### 4. Project skills vs Personal skills (same name)

Personal skill at `~/.claude/skills/commit/SKILL.md` **overrides** project skill `.claude/skills/commit/SKILL.md` when they share a name.

**Why:** Allows individual customization without forking the team command or creating an unfamiliar command name.

---

## Agent Architecture

### 5. `stop_reason: "tool_use"` vs `stop_reason: "end_turn"`

| | `tool_use` | `end_turn` |
|---|---|---|
| Meaning | Claude wants to call a tool | Claude finished response |
| Action | Execute tool, append result, continue loop | Stop loop, return response to user |

**Exam trap:** "Parse Claude's text for 'I'm done'" → Wrong. Use structured `stop_reason`, not natural language parsing.

---

### 6. Coordinator pattern vs Direct subagent communication

| | Coordinator hub | Direct inter-agent |
|---|---|---|
| Visibility | Coordinator sees all | Blind to other agents' exchanges |
| Error handling | Centralized, uniform | Each agent handles its own |
| Information control | Coordinator decides what each agent sees | Each agent sees only what was sent directly |
| Correctness | ✅ Correct pattern | ❌ Breaks hub-and-spoke |

---

### 7. Root cause: narrow decomposition vs subagent performance

When all subagents succeed but output is incomplete/wrong-domain → **coordinator's task decomposition**, not subagent capability.

Research system finds only visual art content even though subagents work correctly → coordinator decomposed into visual art subtasks only. Fix the coordinator prompt, not the subagents.

---

### 8. Structured error context vs Generic failure status

| | Structured error context | Generic "search unavailable" |
|---|---|---|
| Includes | Failure type + attempted query + partial results + alternatives | Only: "failed" |
| Enables | Intelligent coordinator recovery (retry with modified query? continue partial?) | Only: retry or abort |
| Correct choice | ✅ Always | ❌ Never return generic status |

---

### 9. Transient vs Permanent errors (MCP tool design)

| | Transient (timeout, network) | Permanent (syntax error, not found) |
|---|---|---|
| Retry? | ✅ Yes, with backoff | ❌ No — will always fail |
| Handle where? | Inside the tool before surfacing | Immediately return error with details |
| "0 results" | Valid result (NOT an error) | — |
| Timeout | Access failure (needs coordinator decision) | — |

**Exam trap:** "0 results" and "timeout" look similar but require completely different responses. Distinguish them explicitly.

---

## Tool Design

### 10. Fix tool descriptions vs Add routing layer

When tool misrouting occurs:
- ✅ Fix tool descriptions first (root cause: descriptions don't distinguish similar tools)
- ❌ Add pre-routing classifier (adds infrastructure without fixing the underlying ambiguity)

**Rule:** Fix the signal (description) before adding a new layer that compensates for the bad signal.

---

### 11. Prompt instructions vs Programmatic preconditions for critical sequencing

| | Prompt instruction | Programmatic precondition |
|---|---|---|
| Reliability | Probabilistic (LLM may not follow) | Deterministic (code enforces) |
| When to use | Default for general guidance | When sequencing is safety/security critical |
| Example | "Always call get_customer first" | Block `lookup_order` until `get_customer` succeeds |

---

### 12. Two-tool token-binding vs `dry_run` boolean parameter

| | Two-tool token-binding | Single tool with `dry_run: bool` |
|---|---|---|
| Can skip preview? | ❌ Architecturally impossible — no token without preview | ✅ Agent can call with `dry_run=false` directly |
| Enforcement | Code-level guarantee | Prompt-level hope |
| Correct for mandatory preview | ✅ Yes | ❌ No |

---

### 13. `context: fork` in skills vs Running in main session

| | `context: fork` | Main session |
|---|---|---|
| Output stored | Isolated subagent context | Main conversation |
| Effect on subsequent turns | None — isolation prevents contamination | Large output or rejected alternatives bleed into next responses |
| Use for | Discovery, analysis, exploration, brainstorming | Implementation, design, conversation |

---

## API and Integration

### 14. Message Batches API vs Synchronous API

| | Synchronous | Batches API |
|---|---|---|
| Cost | Standard | 50% savings |
| Latency | Immediate | Up to 24 hours (no SLA) |
| Multi-turn tool calls | ✅ Supported | ❌ Not supported — fire-and-forget |
| Use for | Blocking checks, interactive use | Scheduled, non-blocking tasks |

**Exam trap:** Iterative code review (fetches related files mid-review via tool calls) → **cannot use batch API**. Batch is fire-and-forget; it cannot execute tools during a request and return results to Claude.

---

### 15. `-p` / `--print` flag vs Other approaches for CI/CD

| | `-p` flag | `CLAUDE_HEADLESS=true` | `--batch` | `stdin < /dev/null` |
|---|---|---|---|---|
| Makes Claude non-interactive? | ✅ Yes — documented approach | ❌ Does not exist | ❌ Does not exist | Workaround, not documented |
| Print output to stdout? | ✅ Yes | — | — | — |

---

## Prompt Engineering

### 16. Few-shot examples vs Instruction refinement for format consistency

When instructions produce inconsistent output format:
- ✅ Few-shot examples showing exact required format (gives model a concrete pattern)
- ❌ More detailed / explicit instructions (already failing; adding more text doesn't help)

---

### 17. Per-file review passes vs Single-pass full-PR review

| | Per-file + integration pass | Single-pass all files |
|---|---|---|
| Attention quality | High per file | Diluted across all files |
| Local issue detection | Consistent depth | Variable — some files shallow, some deep |
| Cross-file issues | Separate integration pass | Included but may be missed |
| Correct for large PRs | ✅ Yes | ❌ No |

**Exam trap:** "Use a larger model with bigger context window" → Wrong. Larger context does not fix attention quality. More tokens available ≠ consistent attention per token.

---

### 18. Target ambiguous examples vs Generic examples for misrouting

- ✅ 4–6 examples targeted at the specific ambiguous cases where misrouting occurs, with rationale
- ❌ 10–15 examples of clear, unambiguous requests for each tool (doesn't address the ambiguous edge cases)

---

### 19. State explicit assumptions vs Ask multiple clarifying questions

For vague user requests:
- ✅ Proceed with stated reasonable assumptions, invite corrections (eliminates abandonment)
- ❌ Ask 4+ clarifying questions (causes 35–40% abandonment rate)
- ❌ Use hidden defaults without stating them (user confused when response doesn't match intent)

---

## Context Management

### 20. "Lost in the middle" mitigation

- ✅ Key-findings summary at the start + explicit section headings
- ❌ Rotation of which agent's output appears first (doesn't fix the attention pattern)
- ❌ Summarize everything to under 20K (may lose critical information)

---

### 21. Persistent case-facts block vs Summarization improvements

For preserving precise numbers/amounts across long conversations:
- ✅ Extract transactional facts into a case-facts block outside summarized history (survives compression)
- ❌ Revise summarization prompt to preserve numbers (still relies on perfect execution)
- ❌ Increase summarization threshold (buys time but doesn't fix the fundamental precision loss)

---

### 22. Subagent isolation for discovery vs Main-session discovery

For verbose discovery that would exhaust main context:
- ✅ Explore subagent: isolates verbose output, returns concise summary to main session
- ❌ Use `/compact` mid-task (loses precision needed for implementation phase)

---

### 23. Behavioral drift: accumulated responses vs Context window overflow

When system prompt behavior degrades across turns at short token counts (2,500 tokens, 7 turns):
- Root cause: ✅ Accumulated assistant responses dilute system prompt influence
- Not: context window overflow (impossible at 2,500 tokens)
- Not: system prompt "only applies to the first turn" (false — it's included in every request)

---

### 24. Semantic retrieval vs Progressive summarization for long-term recall

For specific recall from months of conversation history (85K tokens):
- ✅ Semantic embeddings with retrieval of relevant exchanges
- ❌ Progressive summarization (compresses specific conclusions into abstractions that can't be recalled precisely)

---

### 25. Stateless API memory pattern

Claude has **no server-side memory**. The only way Claude "remembers" prior conversation is because the application includes prior messages in the `messages[]` array.

**Exam trap:** "Claude needs a `session_id` parameter" → False. The API is stateless; the application manages conversation state.

**Exam trap:** "Claude needs a vector database to maintain conversation memory" → False. Simple conversation memory is the `messages[]` array. Vector databases are for retrieval over long histories (months), not standard multi-turn conversations.

---

## Built-in Tools

*(Grounded in Domain-2 §2.9 and official Exam Guide task 2.5 — built-in tool selection for the Developer Productivity scenario.)*

### 26. Grep (content search) vs Glob (path pattern match)

| | Grep | Glob |
|---|---|---|
| Searches | *Inside* files — content | File *names / paths* — patterns |
| Finds | Function names, error strings, import statements, call sites | Files by name or extension (`**/*.test.tsx`) |
| "Find all callers of `processPayment`" | ✅ Grep the symbol across the codebase | ❌ Wrong tool |
| "Enumerate all TypeScript test files" | ❌ Wrong tool | ✅ Glob `**/*.test.tsx` |

**Exam trap:** Locate every file that references a deprecated `formatDate` function → Grep for `formatDate` (target is file *content*). ❌ Glob `**/formatDate*` only matches files *named* formatDate, not files that use it. Conversely, Grepping for the word "test" to find test files matches unrelated files and misses test files that don't contain the literal word — that's a Glob job.

---

### 27. Edit (unique-text match) vs Read + Write fallback when the anchor is non-unique

| | Edit | Read + Write fallback |
|---|---|---|
| Mechanism | Replace via a **unique** text anchor | Load full file → modify → write full file |
| Fails when | Anchor appears more than once (can't decide which) | — |
| Correct for | Targeted single-occurrence modification | Modification where no unique anchor exists |

**Exam trap:** Edit fails because the anchor isn't unique →
- ✅ Fall back to Read + Write for a reliable full-file modification
- ❌ Retry Edit with a *shorter* anchor — shorter strings are *more* likely to be non-unique, not less
- ❌ Force it with Bash `sed` — bypasses the tool designed for the job; the sanctioned fallback is Read + Write

---

### 28. Incremental investigation (Grep → Read) vs reading all files upfront

| | Incremental (Grep → Read) | Bulk read upfront |
|---|---|---|
| Discovery driver | Content search locates entry points, then targeted reads follow imports/flows | Read every file "for full context" first |
| Context window | Spent only on relevant files | Burned on irrelevant files |
| Exam verdict | ✅ Correct pattern | ❌ Anti-pattern |

**Exam trap:** To understand a codebase, "Read every file first to get full context" → Wrong. Start with Grep to find entry points, then Read to trace. ❌ Globbing the whole tree and Reading each match before searching is the *same* anti-pattern — discovery should be driven by content search, then targeted reads, not exhaustive upfront reading.

---

### 29. MCP tool vs built-in tool preference — fix the description, don't remove the built-in

Agents may **default to a familiar built-in (Grep, Read) over a more capable MCP tool** because selection runs on descriptions. If the MCP tool's description doesn't make its superior capability explicit, the agent falls back to the built-in.

**Exam trap:** A semantic, index-backed code-search MCP server exists, but the agent keeps using built-in Grep →
- ✅ Enhance the MCP tool's description — spell out its unique capability, outputs, and what built-in tools *cannot* provide
- ❌ Remove or disable Grep so the agent has no alternative (breaks legitimate content-search cases; root cause is an under-specified description, not the built-in's existence)
- ❌ Add a "always prefer MCP tools" system-prompt rule (blunt and keyword-sensitive; misroutes cases where the built-in genuinely is right)

**Rule (mirrors #10):** Fix the signal (description) before adding a layer — or removing a tool — to compensate for the bad signal.
