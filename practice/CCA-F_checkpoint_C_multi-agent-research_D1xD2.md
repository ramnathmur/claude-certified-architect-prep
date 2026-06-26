# CCA-F Integration Checkpoint C — Multi-Agent Research System (D1 × D2)
_Cross-domain · exam Scenario 3 · ~20 min · design cold, then compare_

## Why this checkpoint exists

Domain 1 (orchestrator-workers, delegation, the constructed-prompt channel, parallel-elapsed = max) and Domain 2 (tool design, the three MCP primitives, error surfaces by category) are taught in separate modules — but Scenario 3 fuses them: a coordinator that delegates to specialist subagents, each of which calls tools or MCP servers. The transfer failure this checkpoint hunts for is a design that gets *one* domain right and the other wrong — a clean orchestration tree wired to a broken tool/error contract (e.g. retrying an uncertain write), or a flawless tool layer hung off an orchestration that passes raw 100K-token dumps between agents. You only pass by making both halves correct *and* coherent at the seam where they meet.

## The scenario

You're architecting a **multi-agent research system**. A **coordinator (lead) agent** receives an open-ended research question ("Compare the regulatory exposure of three named fintech firms and produce a sourced brief"). It must:

- Decompose the question and **delegate to specialist subagents**: a **web-search worker** (or several), a **document-analysis worker** that reads an internal corpus, and a **synthesis/citation worker** that assembles the final report.
- Back each worker with the right knowledge surface: a **live web-search tool**, a **document corpus** (internal filings, a schema describing each firm's record shape), and tools that hit external APIs (a filings API, a market-data API).
- Run independent work **in parallel** and dependent work **in sequence**.
- Pass context between agents **structurally** (summaries + source indexes), never as raw transcript dumps.
- Carry **provenance** on every finding so the final brief is attributable.
- Handle **tool errors by category** (a 500 from the filings API is not the same as a 404 or a duplicate-write risk).
- **Degrade gracefully** if any one subagent fails — partial, honest output beats a fake-success report or a generic error.

## Design it cold (do this before scrolling)

1. **Pattern + justification.** Which of the five orchestration patterns is the spine here, and *why* this one over routing or static parallelization? What makes a research question the textbook fit?
2. **The delegation channel.** Exactly what does each subagent receive? What does it *not* receive from the coordinator (prior turns? the coordinator's tool results? its system prompt?) — and what must therefore be packed into the delegation prompt itself?
3. **Parallel vs sequential.** Which workers run concurrently and which must wait? What is the *elapsed time* of the parallel phase — sum or max? When would parallelizing actually be *wrong* here?
4. **Tool vs resource vs prompt.** For each knowledge surface — live web search, the document corpus / firm-record schemas, a reusable "produce-a-sourced-brief" workflow — pick the correct MCP primitive and say who controls it.
5. **The error surface.** A filings-API call returns HTTP 500. Then one returns a 404 (firm not found). Then a write/submit tool times out *after* the request may have committed. Give the architected handling for each — transient retry-in-tool? structured error for the model to fix? non-retryable? report-uncertainty-don't-retry?
6. **Provenance.** What does each finding carry so the final brief is attributable, and *where* in the architecture is attribution enforced?
7. **Partial failure.** The document-analysis worker dies mid-run. What does the coordinator deliver, and what must it never claim?

---

## Model architecture (compare your design)

### 1. Pattern — orchestrator-workers (D1)
The spine is **orchestrator-workers**: "a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results" (source: building-effective-agents). The defining reason research fits: "the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input" (source: building-effective-agents). A research question's sub-questions can't be hardcoded — the lead decides them at runtime. This is exactly Anthropic's production Research architecture: "a lead agent coordinates the process while delegating to specialized subagents that operate in parallel" (source: multi-agent-research-system). Routing would only classify-and-dispatch one input; static parallelization would fix the sub-tasks in code. Orchestrator-workers is correct because the breakdown is input-dependent.

Phasing is the canonical **serial decomposition → parallel execution → serial synthesis** (EXAM-DIGEST D1). Note the no-nesting constraint: "Subagents cannot spawn their own subagents" (source: subagents-as-sdk-primitive) — the tree is one level deep, so the coordinator owns all delegation.

### 2. The delegation channel — constructed prompt only (D1)
A subagent's context "starts fresh (no parent conversation)... The only channel from parent to subagent is the Agent tool's prompt string" (source: subagents-as-sdk-primitive). The worker **receives** its own system prompt + the Agent-tool prompt string + project CLAUDE.md (if loaded) + its tool definitions. It **does not receive** the parent's conversation history, the parent's tool results, or the parent's system prompt (source: subagents-as-sdk-primitive). Therefore every delegation must be **self-contained**: pack the objective, output format, tool/source guidance, and clear task boundaries into the prompt — "Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information" (source: orchestrator-worker-at-scale). Pass **structured summaries + source indexes, never raw 100K-token dumps** (EXAM-DIGEST D1). On return, "only its final message returns to the parent" — intermediate tool calls and results stay isolated inside the worker (source: subagents-as-sdk-primitive), which is the compression mechanism: workers "facilitate compression by operating in parallel with their own context windows... before condensing the most important tokens for the lead research agent" (source: multi-agent-research-system).

### 3. Parallel vs sequential — elapsed = max (D1)
The independent web-search and document-analysis workers run **concurrently** — "Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously" (source: multi-agent-research-system); parallelism "cut research time by up to 90% for complex queries" (source: orchestrator-worker-at-scale). **Elapsed time of the parallel phase = max(worker durations), not the sum** (EXAM-DIGEST D1) — the batch is gated by the slowest worker: "the entire system can be blocked while waiting for a single subagent to finish searching" (source: orchestrator-worker-at-scale). The **synthesis/citation worker is sequential** — it depends on the others' output, so it cannot be parallelized: "Don't parallelize when task B needs task A's output" (EXAM-DIGEST D1). Scale worker count to complexity rather than fanning out blindly: simple fact-finding ≈ 1 agent / 3–10 tool calls; direct comparisons ≈ 2–4 subagents / 10–15 calls each; complex research ≈ >10 subagents with clearly divided responsibilities (source: orchestrator-worker-at-scale).

### 4. Tool vs resource vs prompt — the MCP primitive split (D2)
The MAU control model (source: mcp-at-a-builder-level):
- **Live web search → Tool (model-controlled).** "Functions that your LLM can actively call... call external APIs." It's an *action* taken at runtime against fresh data. (Note: in the Anthropic stack `web_search` is a *server-executed* tool — you enable it and read the result; you never construct a `tool_result` for it (source: tool-use-agent-loop).)
- **The document corpus + firm-record schemas → Resources (application-controlled).** "Passive data sources that provide read-only access to information for context, such as file contents, database schemas, or API documentation." The corpus and schemas are *what is true and stable* — read like context, no tool call needed to "use" them. Using a tool where a resource fits is a named anti-pattern (EXAM-DIGEST D2).
- **The reusable "produce-a-sourced-brief" workflow → Prompt (user-controlled).** "Pre-built instruction templates," surfaced as slash commands, "requiring explicit invocation rather than automatic triggering" (source: mcp-at-a-builder-level).

Rule of thumb: **resources for "what is true & stable," tools for "what actions can be taken"** (EXAM-DIGEST D2). And remember MCP "does NOT auto-solve" auth, rate-limiting, retries, caching, or authorization — you build those (EXAM-DIGEST D2); tool annotations (`readOnlyHint`, `destructiveHint`) are "untrusted UI hints, NOT security boundaries."

### 5. The error surface — by category, architected not hoped (D2)
Two tiers first: **protocol errors** (JSON-RPC, pre-execution — unknown tool, malformed JSON, missing param) vs **tool execution errors** (`isError:true` — the tool ran but failed: 404/503/business-rule/rate-limit) (EXAM-DIGEST D2). Then handle each *execution* error by category (source category mapping: EXAM-DIGEST D2):

- **Filings-API 500 (transient infra, a read):** retry *inside the tool* with backoff; the worker shouldn't see a flaky 500 it has to reason about.
- **404 firm-not-found (validation/business-rule):** non-retryable — return a **structured error** (`category`, `retryable:false`, `message`) so the model can adapt (drop that firm, note the gap), not throw an exception.
- **Write/submit timeout where the request may have committed (uncertain write state):** **report the uncertainty, do NOT auto-retry** — retrying risks duplicates (EXAM-DIGEST D2). This is the highest-yield trap in the scenario.

The governing principle: **"Recoverable-vs-escalate is an architectural decision encoded in the error surface — not 'Claude just retries'"** (EXAM-DIGEST D2, logged Module-4 gap). Return structured errors, never raw exceptions for expected business failures; **empty result ≠ error** (an empty filings list is a valid finding, not a failure). At the orchestration layer this pairs with model-driven graceful degradation: "letting the agent know when a tool is failing and letting it adapt works surprisingly well" (source: orchestrator-worker-at-scale).

### 6. Provenance — architecturally separated (D1 × D2)
Every finding carries its **source attribution** (source URL/quote/`source_location`), and citation is a **distinct worker role**, not an afterthought baked into search. Anthropic runs a dedicated **CitationAgent** that "processes the documents and research report to identify specific locations for citations," so "verification is architecturally separated from research" (source: orchestrator-worker-at-scale). Practically: workers return findings *with* source indexes in their structured summary; the synthesis/citation worker maps each claim back to a source before the brief ships. (Grounding fields like `source_location` / `source_quote` are the D3 mechanism for attribution; making an absent source field *required* creates hallucination pressure — keep it grounded but not coercive.)

### 7. Partial failure — graceful degradation (D1)
If the document-analysis worker dies, the coordinator delivers a **partial, honest** result: state what was verified, what couldn't complete, and offer next steps. **Partial completion > fake success or a generic error**, and **never claim a side effect happened if it didn't** (EXAM-DIGEST D1). Architecturally: prefer **resume-from-failure over full restart** — "we built systems that can resume from where the agent was when the errors occurred" (source: orchestrator-worker-at-scale); subagents can be resumed and "pick up exactly where [they] stopped" via captured `session_id` + `agentId` (source: subagents-as-sdk-primitive). Back it with deterministic safeguards (retries, checkpoints) and full production tracing for diagnosis (source: orchestrator-worker-at-scale).

## The cross-domain traps this checkpoint tests

- **Passing raw outputs across the seam.** Designing the orchestration well but dumping a worker's raw 100K-token tool output into the next agent's prompt — instead of structured summaries + source indexes. Context isolation exists *so* you compress; defeating it re-bloats the parent (D1 × D2).
- **Expecting a subagent to see the parent's tool results.** A worker only gets the constructed prompt — not the coordinator's prior turns, tool results, or system prompt. Any design assuming shared state at the seam is broken (D1).
- **Using a tool where a resource fits.** Modeling the document corpus / firm-record schemas as a *tool call* rather than an application-controlled *resource* — the corpus is stable context, not an action (D2).
- **Retrying an uncertain write.** Treating a timed-out submit/write like a transient read 500 and retrying — producing duplicates. Reads retry-in-tool; uncertain writes report uncertainty and stop (D2).
- **"Claude just retries" instead of an architected error surface.** Leaving recoverable-vs-escalate to the model's improvisation rather than encoding `category` / `retryable` in the tool's structured return (D2).
- **Parallelizing dependent steps.** Running the synthesis/citation worker concurrently with the searches it depends on — and/or quoting elapsed time as the *sum* of worker durations instead of **max** (D1).

## Self-score

Target — you should have named all five, unprompted:

| # | Did you name it? | The answer |
|---|---|---|
| 1 | The pattern | **Orchestrator-workers** — runtime, input-dependent decomposition |
| 2 | The context-passing rule | Subagent sees **only the constructed prompt**; pass structured summaries + source indexes, not raw dumps |
| 3 | Parallel timing | Independent workers parallel; **elapsed = max**, not sum; synthesis is sequential (depends on outputs) |
| 4 | The MCP primitive split | Web search = **tool**; corpus + schemas = **resource**; brief workflow = **prompt** |
| 5 | The error-surface decision | By category: read 500 retry-in-tool · 404 non-retryable structured error · **uncertain write → report, don't retry** |

Bonus: provenance as a **separate citation stage**; graceful degradation via **resume-from-failure + honest partial output**.

**Scoring:** 5/5 named cold = exam-ready on Scenario 3. Miss #4 (tool-vs-resource) or #5 (uncertain write) → these are the logged Module-4 gaps; **log every miss to `../GAPS.md`** with the trap name, so spaced repetition re-surfaces it.
