# Citations & Research Notes — Orchestrator-Worker at Scale + Failure Modes (S-E3)

## Manifest
- **Date researched:** 2026-06-06 · **Re-verified 2026-06-09** (core facts confirmed; MAST %s remain unverifiable; additive drifts in the addendum at the end. Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`)
- **Lesson:** "Orchestrator-Worker at Scale + Failure Modes" (extension S-E3, building on Anthropic's "Introduction to Subagents" course)
- **CCA-F domains reinforced:** Domain 1 (Agentic Architecture & Orchestration, 27%); Domain 5 (Context Management & Reliability, 15%)
- **Sources consulted:**
  1. `https://www.anthropic.com/engineering/building-effective-agents` — Anthropic's foundational "Building Effective Agents" guide; defines workflows vs. agents and the orchestrator-workers pattern. **[PRIMARY — Anthropic]**
  2. `https://www.anthropic.com/engineering/multi-agent-research-system` — "How we built our multi-agent research system"; the central case study for this lesson (lead/subagent/citation architecture, token economics, reliability lessons). **[PRIMARY — Anthropic]**
  3. `https://code.claude.com/docs/en/agent-sdk/subagents` — "Subagents in the SDK" (Claude Agent SDK docs; redirected from docs.claude.com → platform.claude.com → code.claude.com). Defines subagents as a primitive, the `AgentDefinition` config shape, context isolation/inheritance, resuming, and the `Workflow` tool for large-scale orchestration. **[PRIMARY — Anthropic]**
  4. `https://galileo.ai/blog/multi-agent-llm-systems-fail` — Galileo engineering blog enumerating multi-agent failure modes and coordination-interaction scaling math. **[SECONDARY]**
  5. `https://arxiv.org/abs/2503.13657` — Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (UC Berkeley group: Keutzer, Klein, Ramchandran, Zaharia, Gonzalez, Stoica). The MAST failure taxonomy. **[SECONDARY — academic]**

> **Sourcing convention:** Every substantive claim below carries an inline `(source: URL)`. Anthropic-primary claims are unmarked as to reliability; secondary claims are tagged **[SECONDARY]**. Version-sensitive or uncertain facts are flagged `[VERIFY]` inline and collected at the bottom.

---

## Section A — Recap: What Orchestrator-Worker Is
*(Reinforces Domain 1)*

**Verbatim definition (Anthropic):** In the orchestrator-workers workflow, "a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results." (source: https://www.anthropic.com/engineering/building-effective-agents)

**When it fits:** It is "well-suited for complex tasks where you can't predict the subtasks needed" and where "subtasks aren't pre-defined, but determined by the orchestrator based on the specific input." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Workflows vs. agents — the framing this pattern sits inside (verbatim):**
- **Workflows** are "systems where LLMs and tools are orchestrated through predefined code paths." (source: https://www.anthropic.com/engineering/building-effective-agents)
- **Agents** are "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks." (source: https://www.anthropic.com/engineering/building-effective-agents)
- Anthropic's selection rule: "Workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale." (source: https://www.anthropic.com/engineering/building-effective-agents)

**How it differs from static parallelization (the key architectural distinction):** The parallelization workflow has two variations — "Sectioning: Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs." (source: https://www.anthropic.com/engineering/building-effective-agents) In plain parallelization the subtasks are **fixed in code**; in orchestrator-workers the **central LLM decides at runtime** what the subtasks are. That dynamic, LLM-driven decomposition is the defining feature — the orchestrator adapts the breakdown to each specific input rather than executing a predetermined fan-out. (source: https://www.anthropic.com/engineering/building-effective-agents)

**SDK realization — subagents as the primitive:** In the Claude Agent SDK, "Subagents are separate agent instances that your main agent can spawn to handle focused subtasks." (source: https://code.claude.com/docs/en/agent-sdk/subagents) Use them "to isolate context for focused subtasks, run multiple analyses in parallel, and apply specialized instructions without adding to the main agent's prompt." (source: https://code.claude.com/docs/en/agent-sdk/subagents)

---

## Section B — Why Scale to Multi-Agent
*(Reinforces Domain 1 and Domain 5)*

Anthropic productionized orchestrator-workers in their Research feature: "a lead agent coordinates the process while delegating to specialized subagents that operate in parallel." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**The three rationales for going multi-agent:**

1. **Context isolation / compression.** "Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent." (source: https://www.anthropic.com/engineering/multi-agent-research-system) The SDK echoes this: "Each subagent runs in its own fresh conversation. Intermediate tool calls and results stay inside the subagent; only its final message returns to the parent." (source: https://code.claude.com/docs/en/agent-sdk/subagents)

2. **Separation of concerns.** "Each subagent also provides separation of concerns—distinct tools, prompts, and exploration trajectories—which reduces path dependency and enables thorough, independent investigations." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

3. **Parallelism / speed.** "Parallel tool calling transforms speed and performance. These changes cut research time by up to 90% for complex queries, allowing Research to do more work in minutes instead of hours." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**The headline facts (each with exact source):**

- **~90% performance lift over single-agent:** "our internal evaluations show that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%" on their internal research eval. (source: https://www.anthropic.com/engineering/multi-agent-research-system) `[VERIFY: figure 90.2%, model names "Claude Opus 4" / "Claude Sonnet 4" — version-sensitive]`

- **Token usage explains ~80% of variance:** "three factors explained 95% of the performance variance" in their analysis, and "token usage by itself explains 80% of the variance." (source: https://www.anthropic.com/engineering/multi-agent-research-system) `[VERIFY: 95% and 80% figures]` (The other two factors are number of tool calls and model choice — implied by the framing; the article explicitly names token usage as the dominant single factor.)

- **~15× token cost:** "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats." (source: https://www.anthropic.com/engineering/multi-agent-research-system) `[VERIFY: 4× and 15× multipliers — dated/usage-dependent]`

**Why this performance comes at all:** It is fundamentally a token story — more agents exploring in parallel means more tokens spent, and since token usage explains ~80% of performance variance, the multi-agent architecture wins largely because it is a mechanism for spending more tokens productively in parallel. (source: https://www.anthropic.com/engineering/multi-agent-research-system)

---

## Section C — The Orchestrator's Job at Scale
*(Reinforces Domain 1)*

The lead agent "analyzes [the query], develops a strategy, and spawns subagents to explore different aspects simultaneously." Subagents work "iteratively using search tools to gather information" and return findings; the system then "passes all findings to a CitationAgent" before returning results. (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**1. Decomposition + delegation with detailed task descriptions.** "Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries. Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information." (source: https://www.anthropic.com/engineering/multi-agent-research-system) Anthropic learned this the hard way: vague instructions like "research the semiconductor shortage" caused subagents to misinterpret the task or perform "the exact same searches as other agents." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**2. Effort heuristics — scale subagent count and tool-call budget to query complexity.** "Agents struggle to judge appropriate effort for different tasks, so we embedded scaling rules in the prompts." (source: https://www.anthropic.com/engineering/multi-agent-research-system) The explicit rules given:
- **Simple fact-finding:** "just 1 agent with 3-10 tool calls"
- **Direct comparisons:** "2-4 subagents with 10-15 calls each"
- **Complex research:** "more than 10 subagents" with clearly divided responsibilities

  (source: https://www.anthropic.com/engineering/multi-agent-research-system) `[VERIFY: exact tool-call counts]`

The SDK exposes effort directly as a field: `effort` accepts `'low' | 'medium' | 'high' | 'xhigh' | 'max'` or a number, and `maxTurns` caps "Maximum number of agentic turns before the agent stops." (source: https://code.claude.com/docs/en/agent-sdk/subagents) `[VERIFY: effort enum values — SDK-version-sensitive]`

**3. Result synthesis.** The lead agent gathers subagent findings and condenses them; subagents are designed to return only "the most important tokens for the lead research agent." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**4. Citation / verification stage.** A dedicated "CitationAgent" "processes the documents and research report to identify specific locations for citations," ensuring claims are attributed before delivery. (source: https://www.anthropic.com/engineering/multi-agent-research-system) This is a distinct worker role — verification is architecturally separated from research.

**Prompt-engineering principles for the orchestrator (verbatim names from Anthropic):**
- "Think like your agents" — build an accurate mental model of agent behavior to make impactful prompt changes obvious. (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- "Teach the orchestrator how to delegate" — each subagent needs objective, output format, tool/source guidance, and boundaries. (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- "Scale effort to query complexity" — embed scaling rules in the prompt. (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- "Let agents improve themselves" — "the Claude 4 models can be excellent prompt engineers… given a prompt and a failure mode, they are able to diagnose why the agent is failing and suggest improvements." (source: https://www.anthropic.com/engineering/multi-agent-research-system) `[VERIFY: "Claude 4 models"]`
- "Start wide, then narrow down" — search strategy should "mirror expert human research: explore the landscape before drilling into specifics." (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- "Guide the thinking process" — extended thinking acts as "a controllable scratchpad"; "The lead agent uses thinking to plan its approach." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

---

## Section D — Failure Modes at Scale (the heart of the lesson)
*(Reinforces Domain 5, with Domain 1 architectural framing)*

Each failure mode below is given as **name → mechanism → symptom → mitigation**. Anthropic-primary mechanisms are cited to the multi-agent writeup; secondary taxonomy framing is tagged.

**(1) Error compounding in stateful, multi-step agents.**
- *Mechanism:* "Agents are stateful and errors compound. Agents can run for long periods of time, maintaining state across many tool calls." (source: https://www.anthropic.com/engineering/multi-agent-research-system) Chaining steps means errors propagate forward instead of canceling out. [SECONDARY] confirms: "errors often compound rather than cancel when you chain agents sequentially." (source: https://galileo.ai/blog/multi-agent-llm-systems-fail)
- *Symptom:* "Without effective mitigations, minor system failures can be catastrophic for agents." (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- *Mitigation:* Durable execution + resume-from-failure; deterministic safeguards (retries, checkpoints) — see Section E. (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**(2) Context-window exhaustion / context overflow across workers.**
- *Mechanism:* Long-horizon runs blow past the context window. Anthropic: "if the context window exceeds 200,000 tokens it will be truncated and it is important to retain the plan." (source: https://www.anthropic.com/engineering/multi-agent-research-system) `[VERIFY: 200,000-token figure]` "As conversations extend, standard context windows become insufficient." (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- *Symptom:* Plan/context truncated; agent loses the thread of its own strategy; degraded or incoherent output.
- *Mitigation:* (a) External memory — "The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context." (source: https://www.anthropic.com/engineering/multi-agent-research-system) (b) Summarize-and-store — "agents summarize completed work phases and store essential information in external memory before proceeding to new tasks." (source: https://www.anthropic.com/engineering/multi-agent-research-system) (c) Clean-context handoffs — "When context limits approach, agents can spawn fresh subagents with clean contexts while maintaining continuity through careful handoffs." (source: https://www.anthropic.com/engineering/multi-agent-research-system) (d) Subagent context isolation by design — subagent intermediate results never enter the parent context (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**(3) Token-cost blowup (the 15× economics).**
- *Mechanism:* Multi-agent systems "use about 15× more tokens than chats." (source: https://www.anthropic.com/engineering/multi-agent-research-system) Every spawned subagent multiplies token consumption.
- *Symptom:* Cost per query that may not justify the result; the architecture stops paying for itself on low-value or non-parallelizable tasks.
- *Mitigation:* Gate on value + parallelizability — "Multi-agent systems excel at valuable tasks that involve heavy parallelization." (source: https://www.anthropic.com/engineering/multi-agent-research-system) Scale effort to complexity (Section C); fall back to single-agent or a fixed workflow when the task doesn't clear the gate (Section F).

**(4) Coordination / synchronization overhead.**
- *Mechanism:* "Multi-agent systems have key differences from single-agent systems, including a rapid growth in coordination complexity." (source: https://www.anthropic.com/engineering/multi-agent-research-system) Anthropic's lead agents "execute subagents synchronously, waiting for each set of subagents to complete before proceeding… the entire system can be blocked while waiting for a single subagent to finish searching." (source: https://www.anthropic.com/engineering/multi-agent-research-system) [SECONDARY] quantifies the interaction explosion: "2 agents = 1 potential interaction; 4 agents = 6 potential interactions; 10 agents = 45 potential interactions." (source: https://galileo.ai/blog/multi-agent-llm-systems-fail) (This is n·(n−1)/2 pairwise growth.)
- *Symptom:* Latency bottlenecks (slowest worker blocks the batch); the lead "can't steer subagents [and] subagents can't coordinate." (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- *Mitigation:* Synchronous execution as a deliberate simplification ("This simplifies coordination"); parallel tool calling to cut wall-clock time. Async execution would add parallelism but "adds challenges in result coordination, state consistency, and error propagation across the subagents." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**(5) Duplicated or conflicting work between workers.**
- *Mechanism:* Vague delegation → overlapping mandates. Real Anthropic example: "One subagent explored the 2021 automotive chip crisis while 2 others duplicated work investigating current 2025 supply chains, without an effective division of labor." (source: https://www.anthropic.com/engineering/multi-agent-research-system) Subagents do not share context with each other, so they cannot self-deconflict at runtime (source: https://code.claude.com/docs/en/agent-sdk/subagents).
- *Symptom:* Wasted tokens, gaps in coverage, redundant or contradictory findings.
- *Mitigation:* Detailed task descriptions with "clear task boundaries" and explicit division of labor in the orchestrator's delegation. (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**(6) Partial failure / one worker fails.**
- *Mechanism:* In synchronous fan-out, a single failing subagent can block or corrupt the batch; cascading downstream failures occur when one agent's bad output feeds others. [SECONDARY] names "Single Agent Failures Cascading Downstream." (source: https://galileo.ai/blog/multi-agent-llm-systems-fail)
- *Symptom:* Whole run stalls or returns incomplete results despite most workers succeeding.
- *Mitigation:* Resume-from-failure rather than full restart (source: https://www.anthropic.com/engineering/multi-agent-research-system); model-driven graceful degradation — "letting the agent know when a tool is failing and letting it adapt works surprisingly well" (source: https://www.anthropic.com/engineering/multi-agent-research-system); deterministic retry logic + checkpoints (source: https://www.anthropic.com/engineering/multi-agent-research-system).

**(7) Non-determinism making debugging hard.**
- *Mechanism:* Agents make different decisions on different runs; failures are hard to reproduce. [SECONDARY] lists "Inadequate Observability and Debugging" as a core failure mode. (source: https://galileo.ai/blog/multi-agent-llm-systems-fail)
- *Symptom:* Cannot reproduce or root-cause failures from logs alone.
- *Mitigation:* "Adding full production tracing let us diagnose why agents failed and fix issues systematically." (source: https://www.anthropic.com/engineering/multi-agent-research-system) Evaluate end-state, not every step (Section E).

**(8) Deployment coordination of long-running stateful agents.**
- *Mechanism:* Deploying a new version mid-run can disrupt agents that are hours into a stateful task.
- *Symptom:* Running agents broken or lost on deploy.
- *Mitigation:* "we use rainbow deployments to avoid disrupting running agents, by gradually shifting traffic from old to new versions" — i.e., keep old and new versions running simultaneously and migrate traffic gradually so in-flight agents finish on the version they started on. (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**Secondary taxonomy cross-reference (for lesson breadth, mark clearly as academic):** Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (UC Berkeley group) identify **14 unique failure modes** across **3 categories** — "(i) system design issues, (ii) inter-agent misalignment, and (iii) task verification" — derived from **1600+ annotated traces** across **7 MAS frameworks**, with inter-annotator agreement kappa = 0.88 on a 150-trace subset. (source: https://arxiv.org/abs/2503.13657) `[VERIFY: the often-cited 41.8% / 36.9% / 21.3% category split was NOT confirmed on the abstract page fetched — do not state percentages as fact without checking the paper body.]` [SECONDARY]

---

## Section E — Reliability Patterns to Design Around the Failures
*(Reinforces Domain 5)*

1. **Durable / resumable execution.** "When errors occur, we can't just restart from the beginning: restarts are expensive and frustrating for users. Instead, we built systems that can resume from where the agent was when the errors occurred." (source: https://www.anthropic.com/engineering/multi-agent-research-system) The SDK supports this concretely: "Subagents can be resumed to continue where they left off. Resumed subagents retain their full conversation history… The subagent picks up exactly where it stopped rather than starting fresh," via capturing `session_id` + `agentId` and passing `resume: sessionId`. (source: https://code.claude.com/docs/en/agent-sdk/subagents)

2. **Checkpointing + retries + deterministic safeguards.** "We combine the adaptability of AI agents built on Claude with deterministic safeguards like retry logic and regular checkpoints." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

3. **Model-driven graceful degradation.** "We also use the model's intelligence to handle issues gracefully: for instance, letting the agent know when a tool is failing and letting it adapt works surprisingly well." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

4. **External memory / context persistence.** Save the plan and completed-phase summaries to memory so context-window truncation doesn't destroy strategy. (source: https://www.anthropic.com/engineering/multi-agent-research-system) SDK note: "When the main conversation compacts, subagent transcripts are unaffected. They're stored in separate files," and persist within their session. (source: https://code.claude.com/docs/en/agent-sdk/subagents)

5. **Full production tracing / observability.** "Adding full production tracing let us diagnose why agents failed and fix issues systematically." (source: https://www.anthropic.com/engineering/multi-agent-research-system) In the SDK, subagent invocation is observable via `tool_use` blocks named `"Agent"` and a `parent_tool_use_id` field on messages from within a subagent. (source: https://code.claude.com/docs/en/agent-sdk/subagents) `[VERIFY: "Agent" vs older "Task" tool name — renamed in Claude Code v2.1.63]`

6. **End-state (not step-by-step) evaluation + LLM-as-judge.** "evaluate whether it achieved the correct final state… focus on end-state evaluation rather than turn-by-turn analysis." (source: https://www.anthropic.com/engineering/multi-agent-research-system) For complex workflows: "break evaluation into discrete checkpoints where specific state changes should have occurred, rather than attempting to validate every intermediate step." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

7. **Rainbow deployments.** Gradually shift traffic old→new to avoid disrupting in-flight stateful agents. (source: https://www.anthropic.com/engineering/multi-agent-research-system)

8. **Worker effort/turn limits + tool restrictions.** Set `maxTurns`, `effort`, and a restricted `tools` list per subagent to bound cost and blast radius; e.g., a read-only analysis agent gets only `["Read","Grep","Glob"]`. (source: https://code.claude.com/docs/en/agent-sdk/subagents)

9. **Move large fan-outs out of the conversation.** "Subagents work well for a few delegated tasks per turn. For runs that coordinate dozens to hundreds of agents, use the `Workflow` tool, which moves the orchestration into a script the runtime executes outside the conversation context." (source: https://code.claude.com/docs/en/agent-sdk/subagents) `[VERIFY: Workflow tool requires TypeScript Agent SDK v0.3.149+]`

---

## Section F — When NOT to Use Orchestrator-Worker at Scale
*(Reinforces Domain 1 and Domain 5)*

1. **Fails the economics gate.** Multi-agent costs ~15× the tokens of a chat (source: https://www.anthropic.com/engineering/multi-agent-research-system). Only use it for "valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools." (source: https://www.anthropic.com/engineering/multi-agent-research-system) If the task isn't valuable *and* parallelizable enough to justify the spend, don't.

2. **Tasks needing shared state / tight coordination.** "Some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today. For instance, most coding tasks involve fewer truly parallelizable tasks than research." (source: https://www.anthropic.com/engineering/multi-agent-research-system) Because subagents don't share context with each other (source: https://code.claude.com/docs/en/agent-sdk/subagents), tightly-coupled work suffers.

3. **Low-latency needs.** Synchronous fan-out means the system "can be blocked while waiting for a single subagent" (source: https://www.anthropic.com/engineering/multi-agent-research-system) — bad for latency-sensitive use cases. Spawning agents and synthesizing results adds overhead a single agent avoids.

4. **The default-to-simplest principle.** Anthropic's overarching guidance: "When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed." (source: https://www.anthropic.com/engineering/building-effective-agents) And: "Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense." (source: https://www.anthropic.com/engineering/building-effective-agents) Fall back to a **single agent** or a **fixed workflow** (predefined code paths) when the dynamic, multi-agent machinery isn't earning its cost. (source: https://www.anthropic.com/engineering/building-effective-agents)

---

## [VERIFY] List (all version-sensitive / uncertain facts in one place)

- **90.2%** performance improvement of multi-agent over single-agent Claude Opus 4 (source: multi-agent-research-system) — figure may date.
- Model names **"Claude Opus 4"** (lead) and **"Claude Sonnet 4"** (subagents) — model lineup is version-sensitive; current models may differ.
- **"Claude 4 models"** as good prompt engineers — version-sensitive phrasing.
- **95%** of performance variance from three factors; **80%** from token usage alone.
- Token multipliers: **~4×** (single agent vs chat) and **~15×** (multi-agent vs chat) — usage-data-dependent, may change.
- Effort heuristic counts: **1 agent / 3–10 tool calls**, **2–4 subagents / 10–15 calls each**, **>10 subagents** for complex research.
- **200,000-token** context-window truncation threshold cited in the Research feature — model/config-specific.
- MAST taxonomy split (commonly cited as **41.8% / 36.9% / 21.3%**) was **NOT** confirmed on the arXiv abstract page fetched; only the 3 category names, 14 modes, 1600+ traces, and kappa=0.88 were confirmed. Verify percentages against the paper body before citing.
- SDK `effort` enum (`'low'|'medium'|'high'|'xhigh'|'max'|number`), `maxTurns`, `AgentDefinition` field set — SDK-version-sensitive.
- Agent tool name **renamed from `"Task"` to `"Agent"` in Claude Code v2.1.63**; older SDKs emit `"Task"`.
- **`Workflow` tool** available in **TypeScript Agent SDK v0.3.149+** only.
- SDK constraint: **"Subagents cannot spawn their own subagents"** (source: code.claude.com subagents doc) — verify still true in current SDK.
- Docs URL chain: `docs.claude.com` → `platform.claude.com` → `code.claude.com` (302/307 redirects observed 2026-06-06); canonical host may shift again.

---

## Re-verification addendum — 2026-06-09 sweep (additive drifts, not reversals)
*(from `QA-VERIFY-SWEEP_2026-06-09.md`)*

- **No per-turn subagent concurrency cap** outside the Workflow runtime — the **16-concurrent / 1,000-total** limits cited in this file are **Workflow-runtime-only**; ordinary Agent-tool parallelism has no documented per-turn cap.
- **Fork subagents** (Claude Code v2.1.117+, `/fork` default from v2.1.161) **inherit the full parent context** — qualifies any blanket "subagents always start fresh" framing (still true for standard Agent-tool spawns).
- **Agent teams** now exist as a higher-level construct above orchestrator → subagent delegation.
- **MAST category split (41.8/36.9/21.3)** — still NOT confirmable from the arXiv abstract; leave flagged as-is.

---

### Quick source reference (for the lesson's "Sources" footer)
- [Building Effective Agents — Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [How we built our multi-agent research system — Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Subagents in the SDK — Claude Docs](https://code.claude.com/docs/en/agent-sdk/subagents)
- [Why Do Multi-Agent LLM Systems Fail? (Cemri et al., UC Berkeley) — arXiv](https://arxiv.org/abs/2503.13657) *(secondary/academic)*
- [Why Do Multi-Agent LLM Systems Fail — Galileo](https://galileo.ai/blog/multi-agent-llm-systems-fail) *(secondary)*
