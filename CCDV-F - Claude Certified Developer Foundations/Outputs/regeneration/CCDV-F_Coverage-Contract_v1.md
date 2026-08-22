# CCDV-F — Coverage Contract v1

**Date:** 2026-08-22
**What this is:** a phrase-level coverage audit of the CCDV-F teaching design against the official
exam blueprint, and the build contract that results from it. It answers one question only — *does
every named sub-topic in the guide's published scope have exactly one chapter that owns it?* It does
not judge whether the design is good.

**Built from:**
- **Blueprint (ground truth):** `EXAM-FACTS_v1.md` §2 — 8 domains, 25 skills, each with a "Scope as
  published" cell transcribed from `sources/CCDV-F_Official-Exam-Guide_v1.0.pdf`. §§1, 5, 6 read for
  item-style context.
- **Design under audit:** `Outputs/regeneration/CCDV-F_Pedagogy-Design_v2.md` — 34 chapters, 79,200
  words. Authoritative for the chapter list and budgets.
- `CCDV-F_Pedagogy-Design_v1.md` §§4, 6 consulted for reasoning only. Its chapter list was not
  audited. `Outputs/classes/` was not read.

**Why this audit exists.** The previous audit tested each skill's allocated word count against its
published weight. That test passed Claude API Mechanics at +2.4% while a phrase bolded in its
published scope — "invoking Claude through third-party vendors" — appeared in no chapter of the
design. Word-count parity with a published weight is a different claim from covering the published
scope. This audit tests the second claim, phrase by phrase.

---

## 0. Method — how the cells were atomised

Ground truth is the "Scope as published" cell, verbatim. Each cell was partitioned into sub-topics so
that the atoms reconstruct the cell with no words dropped and none counted twice.

**Split rules applied:**

1. **Split at every top-level comma and semicolon.** `Tokens, context windows, sampling, …` is five
   atoms, not one.
2. **Split enumerations inside parentheses and after em-dashes** when the members are separately
   nameable topics. `usage patterns (agentic harness dispatch, client- vs server-side tools, approval
   patterns)` yields three atoms; `agentic abstraction frameworks — Strands, LangGraph, PydanticAI`
   yields the parent plus three.
3. **Keep together phrases joined by `and` / `vs` / `versus` that form one compound concept or one
   decision.** `managed agent deployment (self-hosted vs Anthropic-hosted)` is one atom.
   `Secrets, credentials and API keys across dev and production` is one atom — three near-synonyms
   for one thing plus a scope qualifier.
4. **A parent label is kept as its own atom only when it carries meaning beyond its list.**
   `agentic abstraction frameworks` is kept (it names a layer). `usage patterns` and `communication
   patterns` are dropped as bare labels — their children carry all the content. These are the only
   two guide phrases that appear in no atom, and both are label-only.
5. **Bolded phrases are never merged into a neighbour.** Every bold span in the guide is at least one
   atom of its own.

**Confidence scale used in the mapping:**

- **explicit** — the chapter's one-line description (or its title) names the sub-topic, or names it in
  words a reader would recognise as the same thing.
- **implied** — the chapter's topic clearly contains the sub-topic, but the chapter line does not name
  it. An author writing that chapter from the brief alone could omit it and still feel finished.
- **absent** — no chapter's topic contains it.

---

## 1. The atomised blueprint

**153 sub-topics across 25 skills.** Counts by domain:

| Domain | Skills | Sub-topics |
|---|---|---|
| 1 Agents and Workflows (14.7%) | 3 | 18 |
| 2 Applications and Integration (33.1%) | 6 | 40 |
| 3 Claude Code (3.1%) | 1 | 13 |
| 4 Eval, Testing, and Debugging (2.6%) | 1 | 4 |
| 5 Model Selection and Optimization (16.8%) | 4 | 21 |
| 6 Prompt and Context Engineering (11.0%) | 3 | 16 |
| 7 Security and Safety (8.1%) | 4 | 19 |
| 8 Tools and MCPs (10.6%) | 3 | 22 |
| **Total** | **25** | **153** |

Per-skill: 6 · 4 · 8 | 10 · 7 · 10 · 5 · 3 · 5 | 13 | 4 | 3 · 10 · 4 · 4 | 7 · 5 · 4 |
8 · 6 · 4 · 1 | 8 · 5 · 9 = 153.

---

## 2. The mapping — all 153 sub-topics

Sub-topics are quoted verbatim from the guide's cells. Bracketed qualifiers such as `[MCP]` are
disambiguators added by this audit and are not the guide's words.

### Domain 1 — Agents and Workflows

| Sub-topic (verbatim) | Skill | % | Chapter | Confidence |
|---|---|---|---|---|
| Principles | Agent Architecture | 4.5 | 15 | implied |
| patterns | Agent Architecture | 4.5 | 15 | explicit |
| tradeoffs | Agent Architecture | 4.5 | 15 | implied |
| **Decision criteria for workflow vs agent** | Agent Architecture | 4.5 | 15 | explicit |
| manager/supervisor hierarchies | Agent Architecture | 4.5 | 15 | explicit |
| role of subagents | Agent Architecture | 4.5 | 15 | implied |
| Claude Agent SDK | Agent Construction with Claude | 5.3 | 16 | explicit |
| custom agent loops and harnesses | Agent Construction with Claude | 5.3 | 17 | explicit |
| **managed agent deployment (self-hosted vs Anthropic-hosted)** | Agent Construction with Claude | 5.3 | 16 | explicit |
| hooks for deterministic actions | Agent Construction with Claude | 5.3 | 19 | explicit |
| Tool-use loops | Agent Patterns and Frameworks | 4.9 | 10 | explicit |
| sub-agents | Agent Patterns and Frameworks | 4.9 | 18 | explicit |
| memory | Agent Patterns and Frameworks | 4.9 | 18 | explicit |
| context-window management | Agent Patterns and Frameworks | 4.9 | 18 | implied |
| **agentic abstraction frameworks** | Agent Patterns and Frameworks | 4.9 | 16 | explicit |
| **Strands** | Agent Patterns and Frameworks | 4.9 | 16 | explicit |
| **LangGraph** | Agent Patterns and Frameworks | 4.9 | 16 | explicit |
| **PydanticAI** | Agent Patterns and Frameworks | 4.9 | 16 | explicit |

### Domain 2 — Applications and Integration

| Sub-topic (verbatim) | Skill | % | Chapter | Confidence |
|---|---|---|---|---|
| How Claude interprets instructions **across interfaces** | Claude Application Design | 8.6 | 22 | explicit |
| **Claude Code** [interface] | Claude Application Design | 8.6 | 22 | explicit |
| **Desktop** [interface] | Claude Application Design | 8.6 | 22 | explicit |
| **claude.ai** [interface] | Claude Application Design | 8.6 | 22 | explicit |
| **API** [interface] | Claude Application Design | 8.6 | 22 | explicit |
| **SDKs** [interface] | Claude Application Design | 8.6 | 22 | explicit |
| content boundaries | Claude Application Design | 8.6 | 23 | explicit |
| schema design | Claude Application Design | 8.6 | 23 | explicit |
| session hygiene | Claude Application Design | 8.6 | 24 | explicit |
| plugin management | Claude Application Design | 8.6 | 24 | explicit |
| **REST APIs** | Software Engineering Foundations | 7.4 | 4 | explicit |
| **JSON** | Software Engineering Foundations | 7.4 | 4 | explicit |
| **asynchronous programming** | Software Engineering Foundations | 7.4 | 5 | explicit |
| **version control** | Software Engineering Foundations | 7.4 | 34 | explicit |
| **SDLC integration** | Software Engineering Foundations | 7.4 | 34 | explicit |
| **code review** | Software Engineering Foundations | 7.4 | 33 | explicit |
| **small- and large-scale refactoring** | Software Engineering Foundations | 7.4 | 34 | explicit |
| Messages | Claude API Mechanics | 6.8 | 10 | implied |
| tools | Claude API Mechanics | 6.8 | 10 | explicit |
| streaming | Claude API Mechanics | 6.8 | 12 | explicit |
| **vision** | Claude API Mechanics | 6.8 | 25 | explicit |
| **thinking** | Claude API Mechanics | 6.8 | 3 | explicit |
| **caching** | Claude API Mechanics | 6.8 | 9 | explicit |
| **invoking Claude through third-party vendors** | Claude API Mechanics | 6.8 | 4 | explicit |
| Messages API data access patterns | Claude API Mechanics | 6.8 | 5 | implied |
| batch API | Claude API Mechanics | 6.8 | 5 | explicit |
| realtime-vs-batch tradeoffs | Claude API Mechanics | 6.8 | 5 | explicit |
| CLAUDE.md | Configuration Management | 4.1 | 21 | explicit |
| settings.json | Configuration Management | 4.1 | 21 | implied |
| **model version pinning** | Configuration Management | 4.1 | 21 | explicit |
| **prompt versioning** | Configuration Management | 4.1 | 21 | explicit |
| **plugin dependencies** | Configuration Management | 4.1 | 21 | explicit |
| Functional and infrastructure requirements | Understanding Requirements | 3.4 | 32 | explicit |
| business requirements | Understanding Requirements | 3.4 | 32 | explicit |
| solution architecture | Understanding Requirements | 3.4 | 32 | implied |
| Life-cycle management concepts and frameworks | Systems Life Cycle | 2.8 | 34 | explicit |
| developing | Systems Life Cycle | 2.8 | 34 | implied |
| implementing | Systems Life Cycle | 2.8 | 34 | implied |
| operating | Systems Life Cycle | 2.8 | 34 | implied |
| maintaining | Systems Life Cycle | 2.8 | 34 | explicit |

### Domain 3 — Claude Code

| Sub-topic (verbatim) | Skill | % | Chapter | Confidence |
|---|---|---|---|---|
| Rules | Claude Code Operation | 3.1 | 21 | explicit |
| Skills | Claude Code Operation | 3.1 | 20 | implied |
| Commands | Claude Code Operation | 3.1 | 20 | implied |
| Agents | Claude Code Operation | 3.1 | 21 | explicit |
| Agent Memory | Claude Code Operation | 3.1 | 18 | implied |
| session management | Claude Code Operation | 3.1 | 20 | implied |
| built-in and custom slash commands | Claude Code Operation | 3.1 | 20 | implied |
| headless mode | Claude Code Operation | 3.1 | 20 | explicit |
| streaming mode | Claude Code Operation | 3.1 | 20 | explicit |
| auto-mode | Claude Code Operation | 3.1 | 20 | explicit |
| **the CLAUDE.md hierarchy** | Claude Code Operation | 3.1 | 21 | implied |
| repository initialization | Claude Code Operation | 3.1 | 20 | explicit |
| settings.json | Claude Code Operation | 3.1 | 21 | implied |

### Domain 4 — Eval, Testing, and Debugging

| Sub-topic (verbatim) | Skill | % | Chapter | Confidence |
|---|---|---|---|---|
| Error type identification | Debugging and Error Handling | 2.6 | 28 | explicit |
| recovery strategy selection | Debugging and Error Handling | 2.6 | 28 | explicit |
| **trace analysis** | Debugging and Error Handling | 2.6 | 27 | explicit |
| isolating problem origin **between the integration layer and model output** | Debugging and Error Handling | 2.6 | 27 | explicit |

### Domain 5 — Model Selection and Optimization

| Sub-topic (verbatim) | Skill | % | Chapter | Confidence |
|---|---|---|---|---|
| Foundational technical concepts for AI application development | Technical Fundamentals | 6.1 | 4 | implied |
| **integrating with SDKs that wrap REST APIs** | Technical Fundamentals | 6.1 | 4 | explicit |
| **websockets** | Technical Fundamentals | 6.1 | 5 | explicit |
| Tokens | LLM Fundamentals | 5.2 | 1 | explicit |
| context windows | LLM Fundamentals | 5.2 | 1 | explicit |
| sampling | LLM Fundamentals | 5.2 | 2 | explicit |
| non-determinism | LLM Fundamentals | 5.2 | 2 | explicit |
| next-token generation | LLM Fundamentals | 5.2 | 2 | implied |
| **fast mode** | LLM Fundamentals | 5.2 | 3 | explicit |
| **extended thinking** | LLM Fundamentals | 5.2 | 3 | implied |
| **adaptive thinking** | LLM Fundamentals | 5.2 | 3 | explicit |
| **effort levels** | LLM Fundamentals | 5.2 | 3 | explicit |
| zero-/single-/multi-shot prompting | LLM Fundamentals | 5.2 | 6 | explicit |
| Token usage tracking | Cost and Token Management | 2.8 | 9 | implied |
| cost modelling | Cost and Token Management | 2.8 | 9 | implied |
| **prompt caching** | Cost and Token Management | 2.8 | 9 | explicit |
| **cache check-pointing** | Cost and Token Management | 2.8 | 9 | implied |
| Opus vs Sonnet vs Haiku use cases | Model Selection and Tradeoffs | 2.7 | 3 | implied |
| adaptive thinking support | Model Selection and Tradeoffs | 2.7 | 3 | implied |
| quality/latency/cost tradeoffs | Model Selection and Tradeoffs | 2.7 | 3 | implied |
| **breaking behaviour changes across model releases** | Model Selection and Tradeoffs | 2.7 | 3 | explicit |

### Domain 6 — Prompt and Context Engineering

| Sub-topic (verbatim) | Skill | % | Chapter | Confidence |
|---|---|---|---|---|
| Instruction clarity | Prompt Engineering | 4.6 | 6 | implied |
| few-shot examples | Prompt Engineering | 4.6 | 6 | explicit |
| **system vs user placement** | Prompt Engineering | 4.6 | 6 | explicit |
| output constraints | Prompt Engineering | 4.6 | 6 | implied |
| placement across components | Prompt Engineering | 4.6 | 6 | explicit |
| iterative refinement | Prompt Engineering | 4.6 | 6 | explicit |
| input sanitization | Prompt Engineering | 4.6 | 6 | explicit |
| Context-window management | Context Engineering | 3.8 | 8 | explicit |
| **preventing context drift and bloat** | Context Engineering | 3.8 | 8 | implied |
| **tool output pruning** | Context Engineering | 3.8 | 8 | explicit |
| **compaction** | Context Engineering | 3.8 | 8 | explicit |
| context isolation through subagents or multi-step workflows | Context Engineering | 3.8 | 8 | explicit |
| Structured output patterns | Output Handling | 2.6 | 7 | explicit |
| response validation | Output Handling | 2.6 | 7 | implied |
| **defensive parsing** | Output Handling | 2.6 | 7 | explicit |
| **skepticism toward confident output** | Output Handling | 2.6 | 7 | implied |

### Domain 7 — Security and Safety

| Sub-topic (verbatim) | Skill | % | Chapter | Confidence |
|---|---|---|---|---|
| **Prompt injection awareness and mitigation** | AI Application Security | 3.2 | 29 | explicit |
| jailbreak defence | AI Application Security | 3.2 | 30 | implied |
| untrusted input handling | AI Application Security | 3.2 | 29 | explicit |
| data leakage prevention | AI Application Security | 3.2 | 29 | explicit |
| PII handling | AI Application Security | 3.2 | 29 | explicit |
| authN/authZ | AI Application Security | 3.2 | 31 | implied |
| confidentiality | AI Application Security | 3.2 | 29 | explicit |
| integrity | AI Application Security | 3.2 | **29 (assigned)** | **absent** |
| Content policy | Guardrails and Safe Deployment | 2.3 | 30 | explicit |
| **guardrail layering** | Guardrails and Safe Deployment | 2.3 | 30 | explicit |
| secure-by-design | Guardrails and Safe Deployment | 2.3 | 31 | implied |
| privacy | Guardrails and Safe Deployment | 2.3 | 31 | implied |
| IAM | Guardrails and Safe Deployment | 2.3 | 31 | implied |
| least privilege | Guardrails and Safe Deployment | 2.3 | 31 | explicit |
| Secrets, credentials and API keys across dev and production | Identity, Secrets, and Key Management | 1.6 | 31 | explicit |
| identity validation | Identity, Secrets, and Key Management | 1.6 | 31 | explicit |
| access approval and level verification | Identity, Secrets, and Key Management | 1.6 | 31 | implied |
| authorized-access monitoring | Identity, Secrets, and Key Management | 1.6 | 31 | implied |
| Hooks as guardrails to **prevent destructive actions** | Claude Hooks | 1.0 | 19 | explicit |

### Domain 8 — Tools and MCPs

| Sub-topic (verbatim) | Skill | % | Chapter | Confidence |
|---|---|---|---|---|
| Tool use and function calling | Tool Implementation | 4.4 | 10 | explicit |
| configuration for external systems | Tool Implementation | 4.4 | 11 | implied |
| **tool description writing** | Tool Implementation | 4.4 | 11 | explicit |
| error handling | Tool Implementation | 4.4 | 28 | explicit |
| agentic harness dispatch | Tool Implementation | 4.4 | 10 | implied |
| client- vs server-side tools | Tool Implementation | 4.4 | 11 | explicit |
| approval patterns | Tool Implementation | 4.4 | 11 | explicit |
| tool-set construction | Tool Implementation | 4.4 | 11 | explicit |
| **built-in Tools** | Agentic Customization | 4.1 | 13 | explicit |
| **custom Tools** | Agentic Customization | 4.1 | 13 | explicit |
| **Skills** | Agentic Customization | 4.1 | 13 | explicit |
| **MCPs** | Agentic Customization | 4.1 | 13 | explicit |
| selecting the right one for a use case | Agentic Customization | 4.1 | 13 | explicit |
| Server authoring | MCP Server Development | 2.1 | 14 | explicit |
| deployment | MCP Server Development | 2.1 | 14 | implied |
| integration | MCP Server Development | 2.1 | 14 | explicit |
| MCP resources | MCP Server Development | 2.1 | 14 | explicit |
| tools [MCP] | MCP Server Development | 2.1 | 14 | explicit |
| prompts [MCP] | MCP Server Development | 2.1 | 14 | explicit |
| **stdio** | MCP Server Development | 2.1 | 14 | explicit |
| **sockets** | MCP Server Development | 2.1 | 14 | implied |
| **client vs server** | MCP Server Development | 2.1 | 14 | implied |

**Confidence tally:** 108 explicit · 44 implied · 1 absent = 153.

---

## 3. The failures

### 3.1 UNPLACED — 1 sub-topic

| Sub-topic | Skill | % | Goes in | Words needed |
|---|---|---|---|---|
| **integrity** | AI Application Security | 3.2 | **Ch.29** | ~250 |

The guide's cell ends `…confidentiality, integrity`. Ch.29 was repaired in v2 to add "confidentiality
as a design property" and stopped one word short. No chapter line in the design names integrity, and
no chapter's topic contains it: ch.29 is scoped to untrusted content, the action boundary, PII and
data leakage; ch.30 to content policy and layering; ch.7 to defensive parsing of a response. Integrity
in the sense the guide pairs it with confidentiality — that the data, the tool result and the output
have not been altered in transit or by an injected instruction — has no home.

No new chapter is required. Ch.29 already teaches the action boundary, which is the natural anchor:
confidentiality is what an attacker can *read*, integrity is what an attacker can *change*.

### 3.2 IMPLIED-ONLY — 44 sub-topics

Ordered by risk: the ones an author working only from the chapter line would most plausibly never
write. **Nine of these are bolded in the guide**, marked ⚠.

**Highest risk — the chapter line points somewhere else entirely**

| Sub-topic | Skill | % | Ch | Why it can be missed |
|---|---|---|---|---|
| ⚠ **cache check-pointing** | Cost and Token Management | 2.8 | 9 | Ch.9's line covers "what invalidates it" — the opposite operation. Nothing points at placing multiple breakpoints. |
| ⚠ **sockets** | MCP Server Development | 2.1 | 14 | Ch.14's line says "stdio versus **HTTP**". The guide says "stdio, **sockets**". The design substituted a different word for a bolded one. |
| ⚠ **extended thinking** | LLM Fundamentals | 5.2 | 3 | Ch.3's line names *adaptive* thinking, effort and fast mode. The guide names extended thinking as a separate item from adaptive thinking. An author reads ch.3 and writes only adaptive. |
| built-in and custom slash commands | Claude Code Operation | 3.1 | 20 | Ch.20's line is permission modes, deny rules, headless/streaming/auto-mode and repo init. Slash commands appear nowhere. |
| Commands | Claude Code Operation | 3.1 | 20 | Same. Listed by the guide as one of five Claude Code primitives; ch.20's line names none of the five. |
| Skills | Claude Code Operation | 3.1 | 20 | Same. Covered as a *capability choice* in ch.13, never as a Claude Code primitive. |
| session management | Claude Code Operation | 3.1 | 20 | Same. Ch.24 covers application session hygiene, which is a different thing. |
| ⚠ **the CLAUDE.md hierarchy** | Claude Code Operation | 3.1 | 21 | Ch.21 names "CLAUDE.md and its dilution point" — a property of one file, not the enterprise/project/user precedence order the guide bolds. |
| settings.json | Configuration Management | 4.1 | 21 | Named in two skills' scopes and in no chapter line in the design. |
| settings.json | Claude Code Operation | 3.1 | 21 | Same file, second skill, same absence. |
| Token usage tracking | Cost and Token Management | 2.8 | 9 | Ch.9's line is caching plus "measuring context pressure before a request goes out" — pre-flight sizing, not reading the usage block after. |
| cost modelling | Cost and Token Management | 2.8 | 9 | No chapter line names cost modelling. Ch.1 names "price" once, as a definition. |
| Opus vs Sonnet vs Haiku use cases | Model Selection and Tradeoffs | 2.7 | 3 | Ch.3 says "model tier is one decision" and never names a tier. The three model names are the guide's words. |
| quality/latency/cost tradeoffs | Model Selection and Tradeoffs | 2.7 | 3 | The classic triangle is not named in ch.3's line. |
| ⚠ **skepticism toward confident output** | Output Handling | 2.6 | 7 | Ch.7's line is structured outputs, strict tool use, defensive parsing, `stop_reason` — all mechanical. The judgement half of the bold span is absent. |
| ⚠ **preventing context drift and bloat** | Context Engineering | 3.8 | 8 | Ch.8 names four instruments. "Drift" — the session slowly losing the instruction — is a distinct failure from "bloat" and neither word appears. |
| agentic harness dispatch | Tool Implementation | 4.4 | 10 | Named in the guide's parenthetical; ch.10's line describes the loop without naming dispatch as the harness's job. |
| solution architecture | Understanding Requirements | 3.4 | 32 | Ch.32 covers "a sentence from a business stakeholder". The guide names **two** input sources; the design names one. |
| authorized-access monitoring | Identity, Secrets, and Key Management | 1.6 | 31 | Ch.31's line has identity validation and credential types but no ongoing monitoring. |
| access approval and level verification | Identity, Secrets, and Key Management | 1.6 | 31 | Same. Not the same thing as ch.11 tool approval or ch.19 HITL approval. |
| authN/authZ | AI Application Security | 3.2 | 31 | Ch.31 has OAuth vs service credential and least privilege; the authN/authZ *distinction* is never stated as such. |
| IAM | Guardrails and Safe Deployment | 2.3 | 31 | Term not used; ch.31's title says "Identity" instead. |
| secure-by-design | Guardrails and Safe Deployment | 2.3 | 31 | The umbrella term the guide uses for the privacy/IAM/least-privilege triad appears in no chapter. |
| privacy | Guardrails and Safe Deployment | 2.3 | 31 | Substantively taught in ch.29 (PII, confidentiality) under a different skill; not named as a secure-by-design pillar. |
| jailbreak defence | AI Application Security | 3.2 | 30 | Neither ch.29 nor ch.30 names it. Ch.29 is scoped to third-party content, which is injection, not jailbreak. |
| configuration for external systems | Tool Implementation | 4.4 | 11 | Ch.11 is entirely about selection and description. Wiring a custom tool to a real endpoint is not in its line. *Guide phrasing is ambiguous here — see §3.4.* |
| deployment | MCP Server Development | 2.1 | 14 | Ch.14 covers scope and permissions; where and how the server runs is only implied by "stdio versus HTTP". |
| ⚠ **client vs server** [MCP] | MCP Server Development | 2.1 | 14 | Bolded. Ch.14 describes servers exposing things but never states the client's half of the contract. |
| Messages | Claude API Mechanics | 6.8 | 10 | Ch.10 names the block-pairing contract, which is one property of a message. Roles, content-block types and turn structure are not named. |
| Messages API data access patterns | Claude API Mechanics | 6.8 | 5 | *Guide phrasing is ambiguous — see §3.4.* |
| next-token generation | LLM Fundamentals | 5.2 | 2 | Ch.2 says "sampling from a distribution" without saying what the distribution is over. |
| Instruction clarity | Prompt Engineering | 4.6 | 6 | Ch.6 lists placement, shot count, refinement, sanitisation. Clarity — the first thing the guide names — is not among them. |
| output constraints | Prompt Engineering | 4.6 | 6 | Not in ch.6's line. Ch.7 covers API-level guarantees, which is the alternative to prompt-level constraints, not the same thing. |
| response validation | Output Handling | 2.6 | 7 | Ch.7 names defensive parsing, which overlaps but is narrower — parsing tolerates malformed shape, validation rejects wrong content. |
| Agent Memory | Claude Code Operation | 3.1 | 18 | Ch.18's 400 Claude Code words are unmistakably for this, but the line names only generic memory types. |
| context-window management | Agent Patterns and Frameworks | 4.9 | 18 | Ch.18's line is memory types and isolation; the agent-loop budget problem is not named. |
| role of subagents | Agent Architecture | 4.5 | 15 | Ch.15's line covers hierarchies and orchestrator-worker but never states what a subagent is *for* architecturally. |
| Principles | Agent Architecture | 4.5 | 15 | Framing atom. Placed for completeness. |
| tradeoffs | Agent Architecture | 4.5 | 15 | Framing atom. Ch.15 has "what its token multiple buys", which is a tradeoff unlabelled. |
| Foundational technical concepts for AI application development | Technical Fundamentals | 6.1 | 4 | *Unenumerable in the guide — see §3.4. v2 §6 note 1 already flags this as open.* |
| developing | Systems Life Cycle | 2.8 | 34 | Ch.34 names only "the maintain phase". Three of the guide's four named phases are unnamed. |
| implementing | Systems Life Cycle | 2.8 | 34 | Same. |
| operating | Systems Life Cycle | 2.8 | 34 | Same. |
| adaptive thinking support | Model Selection and Tradeoffs | 2.7 | 3 | Adaptive thinking is named in ch.3; *which models support it* — the Model Selection angle — is not. |

### 3.3 DOUBLE-OWNED — 13 sub-topics or clusters

Two or more chapters both claim the ground. Each row names the chapter that should own it.

| Contested ground | Claimed by | Should be owned by | Boundary for the other chapter |
|---|---|---|---|
| **streaming** | ch.5 ("streaming" as one of five request shapes), ch.12 (assembling events, message-close semantics) | **ch.12** | Ch.5 may name streaming only inside the choose-a-shape decision; all mechanics belong to ch.12. |
| **Claude Agent SDK** | ch.4 ("the Anthropic SDK versus the Agent SDK"), ch.16 ("Agent SDK") | **ch.16** | Ch.4 names it only to contrast two SDK layers; what the Agent SDK does is ch.16's. |
| **settings.json** | ch.20 (Claude Code operation), ch.21 (configuration surfaces) | **ch.21** | Ch.20 may reference the file; the schema, precedence and what belongs in it are ch.21's. |
| **input sanitization** | ch.6 (technique), ch.29 (untrusted content, action boundary) | **ch.6** | Already resolved in v2 §1 FR3 — ch.6 teaches the minimal mechanism, ch.29 deepens it into the action boundary. Preserve that split. |
| **context isolation through subagents** | ch.8 ("subagent handoff" as one of four instruments), ch.18 ("subagent context isolation") | **ch.8** | Ch.8 owns why isolation is a context-budget instrument; ch.18 may use it as a state mechanism without re-arguing the budget. |
| **context-window management** | ch.1 (the window as a fixed pot), ch.8 (the instruments), ch.18 (the agent loop) | **ch.8** | Ch.1 owns the concept of a fixed pot only. Ch.18 owns only what an agent loop must carry forward. |
| **Skills** | ch.13 (one of four ways to hand Claude a capability), ch.20 (a Claude Code primitive) | **ch.13** | Ch.20 must name Skills as a CC primitive and point at ch.13 rather than re-explaining what one is. |
| **hooks** | ch.19 (deterministic guardrail), ch.21 (a durable-instruction surface) | **ch.19** | Ch.21 owns hooks only as a place configuration lives; every "what a hook prevents" claim is ch.19's. |
| **secrets** | ch.14 ("why the secret never goes in the config file"), ch.31 ("secrets that can be rotated") | **ch.31** | Ch.14 states the MCP-specific rule and stops. Rotation, dev/prod separation and storage are ch.31's. |
| **subagents** (3 atoms: "role of subagents" ch.15, "sub-agents" ch.18, "Agents" ch.21) | ch.8, ch.15, ch.18, ch.21 | **ch.18** owns the mechanism | Ch.15 owns the *architectural* role only (when a hierarchy needs one). Ch.21 owns them only as a configuration artefact. Ch.8 owns handoff-as-instrument. |
| **session management vs session hygiene** | ch.20 (CC session), ch.24 (application session) | **both, with a stated discriminator** | These are two guide atoms from two skills, and the student will confuse them. Ch.20 must say "the CLI session"; ch.24 must say "the application's own session". Neither may use the bare word "session" as its unit. |
| **approval patterns vs deny/ask/allow** | ch.11 (tool approval patterns), ch.19 (HITL insertion points) | **ch.11** owns tool approval | Ch.19 owns *where the human stands* — the insertion-point decision — not the approval mechanism itself. |
| **MCP** | ch.13 (choose MCP over the other three), ch.14 (build one) | **ch.13** owns the choice | Ch.14 must open from "you have already decided it is an MCP server" and never re-run the comparison. |

**Same-chapter wording collisions** (not double-owned, but the author will otherwise write them
twice): "caching" and "prompt caching" both land in ch.9; "tools" and "Tool use and function calling"
both land in ch.10; "thinking", "extended thinking", "adaptive thinking" and "adaptive thinking
support" all land in ch.3; "Skills" appears as an atom of two different skills. In each case write it
once.

### 3.4 Three guide phrases that are genuinely ambiguous

Per the rules, these were placed rather than dropped, and the ambiguity is recorded.

1. **"Messages API data access patterns"** (Claude API Mechanics 6.8) — could mean how data is fed
   into and pulled out of a call (files, documents, citations → ch.25) or the access shapes of the
   call itself (sync / stream / batch → ch.5). Placed in **ch.5**, because in the guide's cell it sits
   between vendor invocation and `batch API, realtime-vs-batch tradeoffs`, and ch.5 is the chapter
   whose entire subject is choosing among API access shapes.
2. **"Foundational technical concepts for AI application development"** (Technical Fundamentals 6.1) —
   an unenumerable scope statement followed by two examples. Placed in **ch.4**. v2 §6 note 1 already
   records this as open and says it needs a breadth strategy, not a depth allocation. This audit
   cannot close it, because the guide does not say what the concepts are.
3. **"configuration for external systems"** (Tool Implementation 4.4) — could mean "tools are the
   mechanism by which you configure Claude to reach external systems" (in which case ch.10 + ch.11
   cover it wholesale) or "configuring a specific tool to reach a specific system" (endpoint, auth,
   timeout — which no chapter line covers). Placed in **ch.11** as implied. If the second reading is
   right, ch.11 needs ~300 words it does not currently have a line for.

---

## 4. The build contract

One row per chapter. Every sub-topic from §2 appears exactly once.

| Ch | Chapter | Sub-topics this chapter owns | # |
|---|---|---|---|
| 1 | The one budget everything spends | Tokens · context windows | 2 |
| 2 | Why the same prompt answers twice differently | sampling · non-determinism · next-token generation | 3 |
| 3 | Two dials, not one | thinking · fast mode · extended thinking · adaptive thinking · effort levels · Opus vs Sonnet vs Haiku use cases · adaptive thinking support · quality/latency/cost tradeoffs · breaking behaviour changes across model releases | 9 |
| 4 | What is actually on the wire | REST APIs · JSON · invoking Claude through third-party vendors · Foundational technical concepts for AI application development · integrating with SDKs that wrap REST APIs | 5 |
| 5 | Who is waiting? | asynchronous programming · Messages API data access patterns · batch API · realtime-vs-batch tradeoffs · websockets | 5 |
| 6 | Diagnosing a prompt by its failure | zero-/single-/multi-shot prompting · Instruction clarity · few-shot examples · system vs user placement · output constraints · placement across components · iterative refinement · input sanitization | 8 |
| 7 | When asking nicely stops working | Structured output patterns · response validation · defensive parsing · skepticism toward confident output | 4 |
| 8 | Keeping a long session inside the budget | Context-window management · preventing context drift and bloat · tool output pruning · compaction · context isolation through subagents or multi-step workflows | 5 |
| 9 | Paying once for what does not change | caching · Token usage tracking · cost modelling · prompt caching · cache check-pointing | 5 |
| 10 | The loop your code owns | Messages · tools · Tool-use loops · Tool use and function calling · agentic harness dispatch | 5 |
| 11 | Why Claude picked the wrong tool | configuration for external systems · tool description writing · client- vs server-side tools · approval patterns · tool-set construction | 5 |
| 12 | Streaming without corrupting state | streaming | 1 |
| 13 | Four ways to hand Claude a capability | built-in Tools · custom Tools · Skills · MCPs · selecting the right one for a use case | 5 |
| 14 | Build once, connect many | Server authoring · deployment · integration · MCP resources · tools [MCP] · prompts [MCP] · stdio · sockets · client vs server | 9 |
| 15 | Workflow or agent | Principles · patterns · tradeoffs · Decision criteria for workflow vs agent · manager/supervisor hierarchies · role of subagents | 6 |
| 16 | Who runs the loop | Claude Agent SDK · managed agent deployment (self-hosted vs Anthropic-hosted) · agentic abstraction frameworks · Strands · LangGraph · PydanticAI | 6 |
| 17 | Building the loop by hand | custom agent loops and harnesses | 1 |
| 18 | State that outlives a turn | sub-agents · memory · context-window management [Agent Patterns] · Agent Memory | 4 |
| 19 | Where the human stands | hooks for deterministic actions · Hooks as guardrails to prevent destructive actions | 2 |
| 20 | Claude Code as a governed agent | Skills [CC Op] · Commands · session management · built-in and custom slash commands · headless mode · streaming mode · auto-mode · repository initialization | 8 |
| 21 | Four places a durable instruction can live | Rules · Agents · the CLAUDE.md hierarchy · settings.json [CC Op] · CLAUDE.md · settings.json [Config Mgmt] · model version pinning · prompt versioning · plugin dependencies | 9 |
| 22 | The same model, five front doors | How Claude interprets instructions across interfaces · Claude Code · Desktop · claude.ai · API · SDKs | 6 |
| 23 | Contracts inside your own application | content boundaries · schema design | 2 |
| 24 | What an application remembers | session hygiene · plugin management | 2 |
| 25 | Sending Claude things that are not text | vision | 1 |
| 26 | Defining done before you build it | *(none — see note below)* | 0 |
| 27 | Finding where it broke | trace analysis · isolating problem origin between the integration layer and model output | 2 |
| 28 | Failures you can wait out, failures you cannot | Error type identification · recovery strategy selection · error handling [Tool Impl] | 3 |
| 29 | Untrusted content and the action boundary | Prompt injection awareness and mitigation · untrusted input handling · data leakage prevention · PII handling · confidentiality · **integrity (newly assigned, ~250 w)** | 6 |
| 30 | Layered guardrails | jailbreak defence · Content policy · guardrail layering | 3 |
| 31 | Identity, secrets, and the reviewer's three questions | authN/authZ · secure-by-design · privacy · IAM · least privilege · Secrets, credentials and API keys across dev and production · identity validation · access approval and level verification · authorized-access monitoring | 9 |
| 32 | From business requirement to functional and infrastructure requirement | Functional and infrastructure requirements · business requirements · solution architecture | 3 |
| 33 | Reading and reviewing code you did not write | code review | 1 |
| 34 | Changing a live system without breaking it | version control · SDLC integration · small- and large-scale refactoring · Life-cycle management concepts and frameworks · developing · implementing · operating · maintaining | 8 |
| | | **Total** | **153** |

### The arithmetic

```
Sub-topics atomised from the 25 published scope cells   153
Sub-topics placed in the contract table                 153
Placed exactly once                                     153
Placed more than once                                     0
Placed zero times                                         0
                                                    ---------
Difference                                                0
```

Row-by-row: 2+3+9+5+5+8+4+5+5+5+5+1+5+9+6+6+1+4+2+8+9+6+2+2+1+0+2+3+6+3+9+3+1+8 = **153**.

Cross-check by skill (atoms in, atoms out): 6+4+8 = 18 · 10+7+10+5+3+5 = 40 · 13 · 4 ·
3+10+4+4 = 21 · 7+5+4 = 16 · 8+6+4+1 = 19 · 8+5+9 = 22. Sum **153**. Match.

### Two neutral observations, no judgement attached

- **Ch.26 carries no published sub-topic.** This is not an error in the design. `EXAM-FACTS_v1.md` §2
  states it directly: despite Domain 4's title, v1.0 lists no eval-design skill — only Debugging and
  Error Handling. Ch.26's 1,800 words are attributed to that skill but teach evals, which the
  blueprint does not name. Recorded, not challenged.
- **Four chapters own a single sub-topic each** — ch.12 (streaming, 1,800 w), ch.17 (custom agent
  loops and harnesses, 1,800 w), ch.25 (vision, 2,200 w), ch.33 (code review, 2,000 w). Ch.25's line
  also promises PDFs and the Files API, which the guide's cells do not name anywhere. Recorded as a
  fact about coverage density, not as a criticism.
- **No new chapter is needed.** Every one of the 153 sub-topics has a plausible home among the
  existing 34.

---

## 5. What was verified against the guide text, and what was judged

**Verified — read directly off `EXAM-FACTS_v1.md` §2 and off the v2 chapter lines:**

- All 25 "Scope as published" cells, transcribed verbatim into atoms. No sub-topic in §2 of this
  document is paraphrased.
- Every bold span in the guide's cells. All nine bolded phrases flagged in §3.2 were checked
  word-for-word against the chapter line that was supposed to carry them.
- Every "explicit" verdict — 108 of them — means the chapter's one-line description or title in v2 §2
  contains the sub-topic in recognisable words. Each was checked against the line, not from memory.
- Every "the chapter line does not name it" claim in §3.2. Ch.20's line naming none of the five
  Claude Code primitives, ch.21 not containing "settings.json", ch.14 saying "HTTP" where the guide
  says "sockets", ch.3 naming adaptive but not extended thinking, ch.9 naming neither usage tracking
  nor cost modelling nor checkpointing, ch.29 naming confidentiality but not integrity — all read off
  the text.
- The domain and skill percentages, and the chapter list and budgets, taken from the two source
  files unaltered.

**Judged — my calls, defensible but not read off the page:**

- **The atomisation rules in §0**, and therefore the number 153. A different splitting convention
  yields a different total. The rules are stated so the count can be reproduced or disputed. The two
  places the count is most sensitive: whether "Principles, patterns, tradeoffs" is three atoms or one
  (I chose three), and whether "developing, implementing, operating and maintaining" is four atoms or
  one (I chose four).
- **The explicit / implied / absent boundary.** "Implied" means I judged the chapter's topic to
  contain the sub-topic. Several are close calls — "response validation" against ch.7's "defensive
  parsing", "IAM" against ch.31's "Identity", "patterns" against ch.15's "four workflow sub-patterns".
- **The single UNPLACED verdict on "integrity".** I judged that ch.29's action boundary does not
  already contain it. Someone could argue the action boundary *is* integrity control, which would
  make it implied-only rather than unplaced. I took the stricter reading because the guide names
  confidentiality and integrity as a pair and the design named only one of them.
- **Every DOUBLE-OWNED ownership assignment in §3.3.** The contested ground is verified; who should
  own it is my call. The one exception is `input sanitization`, where v2 §1 FR3 already states the
  split and I adopted it rather than deciding.
- **The three ambiguity resolutions in §3.4**, especially placing "Messages API data access patterns"
  in ch.5 rather than ch.25. The guide's phrasing does not settle it; the neighbouring items in the
  cell were my evidence.
- **The ~250-word estimate for integrity.** An estimate, sized against the neighbouring
  confidentiality treatment already in ch.29.

**Not done:** I did not audit whether the design is pedagogically sound, whether the budgets are
right, or whether v1's reasoning holds. I did not read `Outputs/classes/`. I did not verify the
`EXAM-FACTS_v1.md` transcription against the source PDF — that file is treated as ground truth per
the project's source-of-truth rule.
