# Authoring brief — D1 Agentic Architecture & Orchestration (27%) · building: The control tower

Corpus depth file: `prep with quiz/CCA-Prep_Domain-1_v2.md`. Official guide text: `prep with quiz/source/CCA-F-Official-Exam-Guide_text.txt` (task statements 1.1–1.x and the sample questions).

25 cards, in this order (ids fixed):

## D1-01 — The agentic loop runs on stop_reason
Home task statement: TS 1.1 — Design and implement agentic loops for autonomous task execution
Gist (the concept, to be written as one flat sentence): Send the request, read stop_reason: tool_use means run the tool and go round again; end_turn means the loop is finished.
Official-guide bullets this card must cover:
- [1.1-K1] The agentic loop lifecycle: sending requests to Claude, inspecting stop_reason ("tool_use" vs "end_turn"), executing requested tools, and returning results for the next iteration
- [1.1-S1] Implementing agentic loop control flow that continues when stop_reason is "tool_use" and terminates when stop_reason is "end_turn"
Appendix items it also serves: [APP-I1] Agentic loop implementation: Control flow based on stop_reason, tool result handling, loop…; [APP-T5] Claude API — tool_use with JSON schemas, tool_choice options ("auto", "any", forced tool s…; [APP-T1] Claude Agent SDK — Agent definitions, agentic loops, stop_reason handling, hooks (PostTool…

Key Distinction to weave into `tested` / `remember`:
```
KD #5 — `stop_reason: "tool_use"` vs `stop_reason: "end_turn"`
| | `tool_use` | `end_turn` |
|---|---|---|
| Meaning | Claude wants to call a tool | Claude finished response |
| Action | Execute tool, append result, continue loop | Stop loop, return response to user |

**Exam trap:** "Parse Claude's text for 'I'm done'" → Wrong. Use structured `stop_reason`, not natural language parsing.

---
```

## D1-02 — Tool results are appended to the conversation
Home task statement: TS 1.1 — Design and implement agentic loops for autonomous task execution
Gist (the concept, to be written as one flat sentence): Each tool result goes back into the message history so the next iteration can reason over it.
Official-guide bullets this card must cover:
- [1.1-K2] How tool results are appended to conversation history so the model can reason about the next action
- [1.1-S2] Adding tool results to conversation context between iterations so the model can incorporate new information into its reasoning
Appendix items it also serves: [APP-I1] Agentic loop implementation: Control flow based on stop_reason, tool result handling, loop…

## D1-03 — Model-driven decisions, not a hard-coded decision tree
Home task statement: TS 1.1 — Design and implement agentic loops for autonomous task execution
Gist (the concept, to be written as one flat sentence): Claude decides which tool to call next from context; a pre-configured tool sequence is not an agent.
Official-guide bullets this card must cover:
- [1.1-K3] The distinction between model-driven decision-making (Claude reasons about which tool to call next based on context) and pre-configured decision trees or tool sequences

## D1-04 — Loop-termination anti-patterns
Home task statement: TS 1.1 — Design and implement agentic loops for autonomous task execution
Gist (the concept, to be written as one flat sentence): Do not end the loop on parsed text, an iteration cap, or the presence of assistant text — only on stop_reason.
Official-guide bullets this card must cover:
- [1.1-S3] Avoiding anti-patterns such as parsing natural language signals to determine loop termination, setting arbitrary iteration caps as the primary stopping mechanism, or checking for assistant text content as a completion indicator
Appendix items it also serves: [APP-I1] Agentic loop implementation: Control flow based on stop_reason, tool result handling, loop…

Key Distinction to weave into `tested` / `remember`:
```
KD #5 — `stop_reason: "tool_use"` vs `stop_reason: "end_turn"`
| | `tool_use` | `end_turn` |
|---|---|---|
| Meaning | Claude wants to call a tool | Claude finished response |
| Action | Execute tool, append result, continue loop | Stop loop, return response to user |

**Exam trap:** "Parse Claude's text for 'I'm done'" → Wrong. Use structured `stop_reason`, not natural language parsing.

---
```

## D1-05 — Hub-and-spoke: every message goes through the coordinator
Home task statement: TS 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns
Gist (the concept, to be written as one flat sentence): Subagents never talk to each other; the coordinator routes all communication, errors and information.
Official-guide bullets this card must cover:
- [1.2-K1] Hub-and-spoke architecture where a coordinator agent manages all inter-subagent communication, error handling, and information routing
- [1.2-S4] Routing all subagent communication through the coordinator for observability, consistent error handling, and controlled information flow
Appendix items it also serves: [APP-I2] Multi-agent orchestration: Coordinator-subagent patterns, task decomposition, parallel sub…

Key Distinction to weave into `tested` / `remember`:
```
KD #6 — Coordinator pattern vs Direct subagent communication
| | Coordinator hub | Direct inter-agent |
|---|---|---|
| Visibility | Coordinator sees all | Blind to other agents' exchanges |
| Error handling | Centralized, uniform | Each agent handles its own |
| Information control | Coordinator decides what each agent sees | Each agent sees only what was sent directly |
| Correctness | ✅ Correct pattern | ❌ Breaks hub-and-spoke |

---
```

## D1-06 — Subagents start with an empty context
Home task statement: TS 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns
Gist (the concept, to be written as one flat sentence): A subagent inherits nothing; everything it needs must be written into its prompt.
Official-guide bullets this card must cover:
- [1.2-K2] How subagents operate with isolated context—they do not inherit the coordinator's conversation history automatically
- [1.3-K2] That subagent context must be explicitly provided in the prompt—subagents do not automatically inherit parent context or share memory between invocations
- [1.3-S1] Including complete findings from prior agents directly in the subagent's prompt (e.g., passing web search results and document analysis outputs to the synthesis subagent)
Appendix items it also serves: [APP-I3] Subagent context management: Explicit context passing, structured state persistence, crash…; [APP-T13] Session management — Session resumption, fork_session, named sessions, session context iso…

## D1-07 — The coordinator decomposes, delegates, aggregates — and chooses
Home task statement: TS 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns
Gist (the concept, to be written as one flat sentence): The coordinator breaks the task down, picks which subagents to invoke for this query, and merges results; it does not run the full pipeline every time.
Official-guide bullets this card must cover:
- [1.2-K3] The role of the coordinator in task decomposition, delegation, result aggregation, and deciding which subagents to invoke based on query complexity
- [1.2-S1] Designing coordinator agents that analyze query requirements and dynamically select which subagents to invoke rather than always routing through the full pipeline
Appendix items it also serves: [APP-I2] Multi-agent orchestration: Coordinator-subagent patterns, task decomposition, parallel sub…

## D1-08 — Narrow decomposition leaves coverage gaps
Home task statement: TS 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns
Gist (the concept, to be written as one flat sentence): When every subagent succeeds and the answer is still incomplete, the coordinator's decomposition was too narrow.
Official-guide bullets this card must cover:
- [1.2-K4] Risks of overly narrow task decomposition by the coordinator, leading to incomplete coverage of broad research topics

Key Distinction to weave into `tested` / `remember`:
```
KD #7 — Root cause: narrow decomposition vs subagent performance
When all subagents succeed but output is incomplete/wrong-domain → **coordinator's task decomposition**, not subagent capability.

Research system finds only visual art content even though subagents work correctly → coordinator decomposed into visual art subtasks only. Fix the coordinator prompt, not the subagents.

---
```

## D1-09 — Partition scope so subagents do not duplicate work
Home task statement: TS 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns
Gist (the concept, to be written as one flat sentence): Give each subagent a distinct subtopic or source type.
Official-guide bullets this card must cover:
- [1.2-S2] Partitioning research scope across subagents to minimize duplication (e.g., assigning distinct subtopics or source types to each agent)

## D1-10 — Iterative refinement: evaluate, re-delegate, re-synthesise
Home task statement: TS 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns
Gist (the concept, to be written as one flat sentence): The coordinator checks the synthesis for gaps, sends targeted queries back to search/analysis, and re-runs synthesis until coverage is sufficient.
Official-guide bullets this card must cover:
- [1.2-S3] Implementing iterative refinement loops where the coordinator evaluates synthesis output for gaps, re-delegates to search and analysis subagents with targeted queries, and re-invokes synthesis until coverage is sufficient
Appendix items it also serves: [APP-I2] Multi-agent orchestration: Coordinator-subagent patterns, task decomposition, parallel sub…

## D1-11 — Task tool + allowedTools includes "Task"
Home task statement: TS 1.3 — Configure subagent invocation, context passing, and spawning
Gist (the concept, to be written as one flat sentence): Subagents are spawned with the Task tool; a coordinator whose allowedTools omits "Task" cannot delegate.
Official-guide bullets this card must cover:
- [1.3-K1] The Task tool as the mechanism for spawning subagents, and the requirement that allowedTools must include "Task" for a coordinator to invoke subagents
Appendix items it also serves: [APP-T1] Claude Agent SDK — Agent definitions, agentic loops, stop_reason handling, hooks (PostTool…

## D1-12 — AgentDefinition: description, system prompt, tool restrictions
Home task statement: TS 1.3 — Configure subagent invocation, context passing, and spawning
Gist (the concept, to be written as one flat sentence): Each subagent type is configured with a description, its own system prompt and the tools it may use.
Official-guide bullets this card must cover:
- [1.3-K3] The AgentDefinition configuration including descriptions, system prompts, and tool restrictions for each subagent type
Appendix items it also serves: [APP-T1] Claude Agent SDK — Agent definitions, agentic loops, stop_reason handling, hooks (PostTool…

## D1-13 — Content and metadata travel in separate fields
Home task statement: TS 1.3 — Configure subagent invocation, context passing, and spawning
Gist (the concept, to be written as one flat sentence): Pass findings between agents in structured form so source URLs, document names and page numbers survive.
Also serves TS 5.6.
Official-guide bullets this card must cover:
- [1.3-S2] Using structured data formats to separate content from metadata (source URLs, document names, page numbers) when passing context between agents to preserve attribution

## D1-14 — Parallel subagents = multiple Task calls in ONE response
Home task statement: TS 1.3 — Configure subagent invocation, context passing, and spawning
Gist (the concept, to be written as one flat sentence): Emit all Task calls in a single coordinator turn; one per turn is sequential.
Official-guide bullets this card must cover:
- [1.3-S3] Spawning parallel subagents by emitting multiple Task tool calls in a single coordinator response rather than across separate turns
Appendix items it also serves: [APP-I2] Multi-agent orchestration: Coordinator-subagent patterns, task decomposition, parallel sub…

## D1-15 — Coordinator prompts state goals and quality criteria, not procedures
Home task statement: TS 1.3 — Configure subagent invocation, context passing, and spawning
Gist (the concept, to be written as one flat sentence): Give subagents the research goal and what good looks like; a step-by-step script removes their ability to adapt.
Official-guide bullets this card must cover:
- [1.3-S4] Designing coordinator prompts that specify research goals and quality criteria rather than step-by-step procedural instructions, to enable subagent adaptability

## D1-16 — Programmatic enforcement vs prompt guidance
Home task statement: TS 1.4 — Implement multi-step workflows with enforcement and handoff patterns
Gist (the concept, to be written as one flat sentence): When a sequence must hold (identity check before a refund), enforce it in code — hooks or prerequisite gates — because prompt compliance has a non-zero failure rate.
Official-guide bullets this card must cover:
- [1.4-K1] The difference between programmatic enforcement (hooks, prerequisite gates) and prompt-based guidance for workflow ordering
- [1.4-K2] When deterministic compliance is required (e.g., identity verification before financial operations), prompt instructions alone have a non-zero failure rate
- [1.4-S1] Implementing programmatic prerequisites that block downstream tool calls until prerequisite steps have completed (e.g., blocking process_refund until get_customer has returned a verified customer ID)
- [1.5-K3] The distinction between using hooks for deterministic guarantees versus relying on prompt instructions for probabilistic compliance
- [1.5-S3] Choosing hooks over prompt-based enforcement when business rules require guaranteed compliance

Key Distinction to weave into `tested` / `remember`:
```
KD #11 — Prompt instructions vs Programmatic preconditions for critical sequencing
| | Prompt instruction | Programmatic precondition |
|---|---|---|
| Reliability | Probabilistic (LLM may not follow) | Deterministic (code enforces) |
| When to use | Default for general guidance | When sequencing is safety/security critical |
| Example | "Always call get_customer first" | Block `lookup_order` until `get_customer` succeeds |

---
```

## D1-17 — Structured handoff to a human
Home task statement: TS 1.4 — Implement multi-step workflows with enforcement and handoff patterns
Gist (the concept, to be written as one flat sentence): An escalation carries customer ID, root cause, amount and recommended action, because the human cannot see the transcript.
Official-guide bullets this card must cover:
- [1.4-K3] Structured handoff protocols for mid-process escalation that include customer details, root cause analysis, and recommended actions
- [1.4-S3] Compiling structured handoff summaries (customer ID, root cause, refund amount, recommended action) when escalating to human agents who lack access to the conversation transcript

## D1-18 — Multi-concern requests: split, investigate in parallel, synthesise
Home task statement: TS 1.4 — Implement multi-step workflows with enforcement and handoff patterns
Gist (the concept, to be written as one flat sentence): Decompose a message with several issues into items, work them in parallel with shared context, then answer once.
Official-guide bullets this card must cover:
- [1.4-S2] Decomposing multi-concern customer requests into distinct items, then investigating each in parallel using shared context before synthesizing a unified resolution

## D1-19 — Two-tool token binding vs a dry_run flag
Home task statement: TS 1.4 — Implement multi-step workflows with enforcement and handoff patterns
Gist (the concept, to be written as one flat sentence): A mandatory preview is guaranteed only when the execute tool needs a token that the preview tool issues; a boolean can be skipped.
Note: Practice-test distinction adjacent to TS 1.4/1.5 (enforcement in code).

Key Distinction to weave into `tested` / `remember`:
```
KD #12 — Two-tool token-binding vs `dry_run` boolean parameter
| | Two-tool token-binding | Single tool with `dry_run: bool` |
|---|---|---|
| Can skip preview? | ❌ Architecturally impossible — no token without preview | ✅ Agent can call with `dry_run=false` directly |
| Enforcement | Code-level guarantee | Prompt-level hope |
| Correct for mandatory preview | ✅ Yes | ❌ No |

---
```

## D1-20 — PostToolUse hooks normalise tool results
Home task statement: TS 1.5 — Apply Agent SDK hooks for tool call interception and data normalization
Gist (the concept, to be written as one flat sentence): A PostToolUse hook rewrites heterogeneous formats (Unix timestamps, ISO 8601, numeric codes) before the model sees them.
Official-guide bullets this card must cover:
- [1.5-K1] Hook patterns (e.g., PostToolUse) that intercept tool results for transformation before the model processes them
- [1.5-S1] Implementing PostToolUse hooks to normalize heterogeneous data formats (Unix timestamps, ISO 8601, numeric status codes) from different MCP tools before the agent processes them
Appendix items it also serves: [APP-T1] Claude Agent SDK — Agent definitions, agentic loops, stop_reason handling, hooks (PostTool…

## D1-21 — Intercept outgoing tool calls to block and redirect
Home task statement: TS 1.5 — Apply Agent SDK hooks for tool call interception and data normalization
Gist (the concept, to be written as one flat sentence): A hook on the outgoing call blocks a policy violation (refund over $500) and redirects to escalation.
Official-guide bullets this card must cover:
- [1.5-K2] Hook patterns that intercept outgoing tool calls to enforce compliance rules (e.g., blocking refunds above a threshold)
- [1.5-S2] Implementing tool call interception hooks that block policy-violating actions (e.g., refunds exceeding $500) and redirect to alternative workflows (e.g., human escalation)
Appendix items it also serves: [APP-T1] Claude Agent SDK — Agent definitions, agentic loops, stop_reason handling, hooks (PostTool…

## D1-22 — Prompt chaining vs adaptive decomposition
Home task statement: TS 1.6 — Design task decomposition strategies for complex workflows
Gist (the concept, to be written as one flat sentence): Fixed sequential chains suit predictable multi-aspect reviews; open-ended investigation needs subtasks generated from what each step finds.
Official-guide bullets this card must cover:
- [1.6-K1] When to use fixed sequential pipelines (prompt chaining) versus dynamic adaptive decomposition based on intermediate findings
- [1.6-K3] The value of adaptive investigation plans that generate subtasks based on what is discovered at each step
- [1.6-S1] Selecting task decomposition patterns appropriate to the workflow: prompt chaining for predictable multi-aspect reviews, dynamic decomposition for open-ended investigation tasks
- [1.6-S3] Decomposing open-ended tasks (e.g., "add comprehensive tests to a legacy codebase") by first mapping structure, identifying high-impact areas, then creating a prioritized plan that adapts as dependencies are discovered
Appendix items it also serves: [APP-T11] Prompt chaining — Sequential task decomposition into focused passes…

## D1-23 — --resume <session-name> continues a named session
Home task statement: TS 1.7 — Manage session state, resumption, and forking
Gist (the concept, to be written as one flat sentence): Named sessions let you pick up a specific prior investigation across work sessions.
Official-guide bullets this card must cover:
- [1.7-K1] Named session resumption using --resume <session-name> to continue a specific prior conversation
- [1.7-S1] Using --resume with session names to continue named investigation sessions across work sessions
Appendix items it also serves: [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…; [APP-T13] Session management — Session resumption, fork_session, named sessions, session context iso…

## D1-24 — fork_session branches from a shared baseline
Home task statement: TS 1.7 — Manage session state, resumption, and forking
Gist (the concept, to be written as one flat sentence): Fork one analysed session into independent branches to compare approaches without re-analysing.
Official-guide bullets this card must cover:
- [1.7-K2] fork_session for creating independent branches from a shared analysis baseline to explore divergent approaches
- [1.7-S2] Using fork_session to create parallel exploration branches (e.g., comparing two testing strategies or refactoring approaches from a shared codebase analysis)
- [1.3-K4] Fork-based session management for exploring divergent approaches from a shared analysis baseline
Appendix items it also serves: [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…; [APP-T13] Session management — Session resumption, fork_session, named sessions, session context iso…

## D1-25 — Resume, or start fresh with a summary — and say what changed
Home task statement: TS 1.7 — Manage session state, resumption, and forking
Gist (the concept, to be written as one flat sentence): Resume when prior context is still valid; start a new session with a structured summary when tool results are stale; on resume, name the files that changed.
Official-guide bullets this card must cover:
- [1.7-K3] The importance of informing the agent about changes to previously analyzed files when resuming sessions after code modifications
- [1.7-K4] Why starting a new session with a structured summary is more reliable than resuming with stale tool results
- [1.7-S3] Choosing between session resumption (when prior context is mostly valid) and starting fresh with injected summaries (when prior tool results are stale)
- [1.7-S4] Informing a resumed session about specific file changes for targeted re-analysis rather than requiring full re-exploration
Appendix items it also serves: [APP-T13] Session management — Session resumption, fork_session, named sessions, session context iso…
