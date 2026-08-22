# Extension Material — Evaluation & Recommendation (Stage 1)

**Status:** Awaiting Ram's approval before any extension files are built.
**Created:** 2026-06-05
**Scope:** Level up the two shipped courses (Claude 101, Introduction to Subagents) with linked, researched "extension" HTML that takes a learner from course-level → architect-level for the CCA-F exam.
**Researcher designated:** the live `web-researcher` agent **embodying the Senior Research Analyst persona** (the persona library's Research Analyst is a conceptual analysis role with no web access; the actual searching is done by the web-researcher agent under that persona's rigor). Both research passes are source-cited below.

---

## 1. Evaluation of the two existing files

Rubric (4 dimensions): **Coverage depth · Worked-example density · Exam-domain alignment · Conceptual-scaffolding gaps.**

### Course 1 — Claude 101
| Dimension | Assessment |
|---|---|
| Coverage depth | Broad **product/usage** coverage of claude.ai surfaces. Strong on *what features exist*, deliberately silent on *how they work underneath*. |
| Worked-example density | Good conceptual examples (prompt anatomy, role use-cases) but **no code, no API, no structured-output mechanics**. |
| Exam-domain alignment | Touches all 5 domains at the surface. **Under-serves Domain 4 (Tool Use/MCP, 18%) and Domain 5 (Context Mgmt, 15%)** at the builder level, and prompt-engineering depth (Domain 3). |
| Scaffolding gaps | No agent/tool loop, no Messages API, no prompt caching, no context economics, no model-selection judgment. |

**Verdict:** Excellent foundation/vocabulary; the next rung is the **API/builder layer** the exam tests but claude.ai users never see.

### Course 2 — Introduction to Subagents
| Dimension | Assessment |
|---|---|
| Coverage depth | Focused and solid on the **single-subagent CLI** model (`/agents`, config, design patterns, decision rule). |
| Worked-example density | Strong (YAML config, structured-output format, JWT summary). **No multi-agent orchestration example.** |
| Exam-domain alignment | Partial on **Domain 1 (Agentic Architecture, 27% — the heaviest)**: has delegation + anti-patterns, but lacks the named pattern vocabulary, the formal agent loop, and SDK generalization. |
| Scaffolding gaps | The five orchestration patterns; orchestrator-worker at scale; system-level failure modes; subagent-as-SDK-primitive; the observe-think-act loop. |

**Verdict:** Great on one subagent in the CLI; the next rung is **multi-agent orchestration + the SDK/loop formalization** — squarely the 27% domain.

---

## 2. Recommended extension files

Capped to a prioritized set per course; each is **researched + source-cited + visibly labeled "Extension — beyond the Academy course"**, and cross-linked to the base lessons. Off-exam enrichment is flagged.

### For Claude 101 (builder/API layer)
| # | Extension file | Next-level topics | CCA-F domain | Why it matters | Key sources |
|---|---|---|---|---|---|
| C-E1 | **The Tool-Use Agent Loop** | `stop_reason: tool_use` → execute → `tool_result` → repeat; client vs server tools; `tool_choice`; `strict` schemas | Domain 4 (18%) | The biggest cliff between claude.ai user and architect | platform.claude.com tool-use overview + how-tool-use-works |
| C-E2 | **Context Management & Reliability** | context windows, linear token accumulation, context rot, compaction, context editing, token budgeting | Domain 5 (15%) | Reliability backbone of any production agent | context-windows, compaction, effective-context-engineering |
| C-E3 | **MCP at a Builder Level** | tools/resources/prompts primitives; stdio vs Streamable HTTP/SSE; JSON-RPC; discovery | Domain 4 (18%) | Turns "USB-C for AI" into real protocol knowledge | modelcontextprotocol.io architecture; mcp-connector |
| C-E4 | **Prompt Caching Economics** | `cache_control`, breakpoint order tools→system→messages, write/read multipliers, 1024-token min | Domain 5 (15%) | Applied cost/latency lever, likely scenario-tested | prompt-caching; pricing |
| C-E5 *(optional)* | **Prompt Engineering Depth + Model Selection** | few-shot, CoT/extended thinking, XML structuring, prefilling, JSON output; Opus/Sonnet/Haiku tradeoffs | Domain 3 (20%) + cross-cut | Architect judgment = picking the model | prompt-engineering best-practices; models overview |

### For Introduction to Subagents (orchestration/SDK layer)
| # | Extension file | Next-level topics | CCA-F domain | Why it matters | Key sources |
|---|---|---|---|---|---|
| S-E1 | **The Five Orchestration Patterns (decision framework)** | workflow vs agent; prompt chaining, routing, parallelization (sectioning+voting), orchestrator-workers, evaluator-optimizer | Domain 1 (27%) | Highest exam ROI — the named vocabulary the 27% domain is built on | anthropic.com/engineering/building-effective-agents |
| S-E2 | **Subagents as a Programmable Primitive (CLI → Agent SDK)** | `AgentDefinition` (description/prompt/tools/model/maxTurns/background); fresh-but-not-empty context; prompt-string = only channel; no nested subagents; Workflow-tool graduation | Domain 1 (27%) + Domain 2 (20%) | Converts `/agents` knowledge into the SDK/loop mental model the exam probes | code.claude.com agent-sdk/subagents; building-agents-with-the-claude-agent-sdk |
| S-E3 | **Orchestrator-Worker at Scale + Failure Modes** | Anthropic's multi-agent research system (lead+workers+citation agent, effort heuristics, 90% time / 15× token facts); named failure modes + reliability patterns | Domain 1 (27%) + Domain 5 (15%) | Concrete reference architecture + the "broken system" scenarios the exam favors | multi-agent-research-system; building-effective-agents |
| (woven) | **The Observe-Think-Act Loop** | the formal agent loop; a subagent as a nested loop whose intermediate steps are discarded | Domain 1 (27%) | The conceptual spine connecting all the above | building-effective-agents; exam guide |

---

## 3. The seamless basics → advanced ladder

A single path from foundation upward (base courses in **bold**, extensions indented):

1. **Claude 101** (product vocabulary)
   - C-E1 Tool-Use Agent Loop → C-E2 Context Management → C-E3 MCP builder-level → C-E4 Prompt Caching → C-E5 Prompt depth + model selection *(optional)*
2. **Introduction to Subagents** (single-subagent CLI)
   - S-E1 Orchestration Patterns → S-E2 Subagents as SDK primitive → S-E3 Orchestrator-worker at scale + failure modes

Rationale: Claude 101's extensions build the **builder/API layer** (tool loop, context, MCP) that you *need* before subagent orchestration makes deep sense — so the global order is coherent, not just per-course.

---

## 4. Open questions / decisions for Ram

1. **Build-first pilot (validate the extension format on ONE before scaling):** two strong candidates —
   - **S-E1 Orchestration Patterns** = highest exam ROI (27% domain), or
   - **C-E1 Tool-Use Agent Loop** = truest "next rung from basics" / foundational.
2. **Extension set size:** build the full recommended set, the core only (C-E1, C-E2, S-E1, S-E2, S-E3), or a custom subset?
3. **Optional C-E5** (prompt depth + model selection): include or skip?

---

## 5. Flags (from the research, carry into the build)

- **Model-version drift:** Claude 101's captured source says *Opus 4.7 / Sonnet 4.7*; live docs (June 2026) say *Opus 4.8 / Sonnet 4.6 / Haiku 4.5* with 1M-token context. Extensions should cite live docs but **flag version-sensitive facts** and stay internally consistent with what the exam expects. Re-verify model names/prices at build time.
- **Domain weightings** (27/20/20/18/15) are community-sourced (exam-guide blog), not a published Anthropic page — verify against the official Exam Guide PDF if accessible.
- **Doc host moved:** `docs.anthropic.com` now redirects to `platform.claude.com` — extensions should link the live host.
- **Grounding rule for extensions (differs from base courses):** every substantive claim must trace to a cited source; each extension gets a `source/<slug>_citations.md` notes file that QA Gate 1 diffs against (the analog of the base courses' capture file). No fabrication; no invented exam questions.
