# CCDV-F — Verified Exam Facts

**Source of record:** `sources/CCDV-F_Official-Exam-Guide_v1.0.pdf` — **Version 1.0, effective July
2026**, 14 pages. Filed and reconciled 2026-08-19.
**Status:** ✅ **Phase 0 closed.** Every open question below has been answered from the official guide,
except the two explicitly marked STILL OPEN.

> **Re-check quarterly.** The guide states it "is subject to change without notice," and its Document
> Control section records v1.0 as the initial publication. The CCAR-F guide moved to v1.0 in July 2026
> and silently dropped a whole section, which is how that project learned to diff versions rather than
> trust a cached read.

---

## 1. Exam mechanics — VERIFIED against the official guide

| Fact | Value |
|---|---|
| Exam code | **CCDV-F** |
| Full name | Claude Certified Developer – Foundations |
| Number of items | **53** |
| Item format | **Multiple-choice and multiple-response. Each item states how many responses to select** |
| Time limit | **120 minutes** |
| Passing score | **720** on a scaled range of **100–1,000** |
| Scoring model | Criterion-referenced — measured against a fixed standard, not against other candidates |
| Exam fee | **$125 USD** |
| Validity | **12 months** from the date awarded |
| Delivery | Proctored — online proctored and/or Pearson VUE test centre |
| Result reporting | Pass/fail with scaled score, **plus percent-correct by domain** |
| Domain floors | **None.** Section percentages "are not used to determine your pass or fail result" |
| Prerequisites | **None mandatory.** No required course. Credential awarded on exam performance alone |
| Retakes | 4 attempts per rolling 12 months. Waits: 14 days after 1st fail, 30 after 2nd, 90 after 3rd. Fee applies per attempt |
| Reschedule | Up to 24 h before. Inside 24 h forfeits the fee |
| Renewal | Free, non-proctored assessment on the Partner Academy if renewed on time. Lapsed = full exam at full fee |
| Book policy | **Closed book.** Workspace clear of notes, books, phones, secondary monitors. Prohibited: mobile phones, smart watches, headphones, study materials, recording devices |
| ID | Valid unexpired government photo ID, name matching registration exactly |
| NDA | Confidentiality agreement accepted before the exam starts; declining ends the session with no refund |
| Appeals | Within 14 days. Standard-setting outcome and individual item content are not appealable |

### Two things that change exam-day tactics

**"Each item states how many responses to select."** Multiple-response items tell you the count. That
removes the guess about whether a question wants two answers or three, which is a meaningful share of
where multiple-response marks leak.

**No domain floor.** Pass/fail is total scaled score only. A weak 2.6% domain cannot fail you on its
own — so effort follows weight, not anxiety.

### STILL OPEN — the guide does not say

1. **Whether multiple-response items are scored all-or-nothing or with partial credit.** Not stated
   anywhere in v1.0. On CCAR-F it was all-or-nothing and cost eight marks. **Keep assuming
   all-or-nothing.**
2. **Whether the score report breaks down below domain level.** The guide says "percentage of items
   you answered correctly within each content domain" — that reads as 8 domains, not the 25 published
   skills. The CCAR-F report exposed 37 objectives, so this may be less granular than last time.

---

## 2. Content blueprint — VERIFIED, with published skill-level weights

The guide publishes **8 domains and 25 skills, each with its own percentage.** Skill weights sum
exactly to their domain, and the domains sum to 100.0 (checked). Item counts below are the weight
applied to 53 items — the guide gives percentages, not counts, so these are arithmetic, not stated.

| # | Domain | Weight | ≈ items |
|---|---|---|---|
| 1 | Agents and Workflows | 14.7% | 7.8 |
| 2 | **Applications and Integration** | **33.1%** | **17.5** |
| 3 | Claude Code | 3.1% | 1.6 |
| 4 | Eval, Testing, and Debugging | 2.6% | 1.4 |
| 5 | Model Selection and Optimization | 16.8% | 8.9 |
| 6 | Prompt and Context Engineering | 11.0% | 5.8 |
| 7 | Security and Safety | 8.1% | 4.3 |
| 8 | Tools and MCPs | 10.6% | 5.6 |

### Domain 1 — Agents and Workflows (14.7%)

| Skill | % | Scope as published |
|---|---|---|
| Agent Architecture | 4.5 | Principles, patterns, tradeoffs. **Decision criteria for workflow vs agent**, manager/supervisor hierarchies, role of subagents |
| Agent Construction with Claude | 5.3 | Claude Agent SDK, custom agent loops and harnesses, **managed agent deployment (self-hosted vs Anthropic-hosted)**, hooks for deterministic actions |
| Agent Patterns and Frameworks | 4.9 | Tool-use loops, sub-agents, memory, context-window management; **agentic abstraction frameworks — Strands, LangGraph, PydanticAI** |

### Domain 2 — Applications and Integration (33.1%) · the largest domain

| Skill | % | Scope as published |
|---|---|---|
| Claude Application Design | 8.6 | How Claude interprets instructions **across interfaces (Claude Code, Desktop, claude.ai, API, SDKs)**, content boundaries, schema design, session hygiene, plugin management |
| Software Engineering Foundations | 7.4 | **REST APIs, JSON, asynchronous programming, version control, SDLC integration, code review, small- and large-scale refactoring** |
| Claude API Mechanics | 6.8 | Messages, tools, streaming, **vision, thinking, caching, invoking Claude through third-party vendors**, Messages API data access patterns, batch API, realtime-vs-batch tradeoffs |
| Configuration Management | 4.1 | CLAUDE.md, settings.json, **model version pinning, prompt versioning, plugin dependencies** |
| Understanding Requirements | 3.4 | Functional and infrastructure requirements from business requirements and solution architecture |
| Systems Life Cycle | 2.8 | Life-cycle management concepts and frameworks for developing, implementing, operating and maintaining IT systems |

### Domain 3 — Claude Code (3.1%)

| Skill | % | Scope as published |
|---|---|---|
| Claude Code Operation | 3.1 | Rules, Skills, Commands, Agents, Agent Memory; session management, built-in and custom slash commands, headless mode, streaming mode, auto-mode; **the CLAUDE.md hierarchy**, repository initialization, settings.json |

### Domain 4 — Eval, Testing, and Debugging (2.6%)

| Skill | % | Scope as published |
|---|---|---|
| Debugging and Error Handling | 2.6 | Error type identification, recovery strategy selection, **trace analysis**, isolating problem origin **between the integration layer and model output** |

> Note what is *not* here. Despite the domain title, v1.0 lists **no eval-design skill** — only
> debugging and error handling. Designing and running evals appears in the credential description and
> in the prep advice, but the only examinable skill under this domain is debugging.

### Domain 5 — Model Selection and Optimization (16.8%)

| Skill | % | Scope as published |
|---|---|---|
| Technical Fundamentals | 6.1 | Foundational technical concepts for AI application development — **integrating with SDKs that wrap REST APIs, websockets** |
| LLM Fundamentals | 5.2 | Tokens, context windows, sampling, non-determinism, next-token generation; **fast mode, extended thinking, adaptive thinking, effort levels**; zero-/single-/multi-shot prompting |
| Cost and Token Management | 2.8 | Token usage tracking, cost modelling, **prompt caching and cache check-pointing** |
| Model Selection and Tradeoffs | 2.7 | Opus vs Sonnet vs Haiku use cases, adaptive thinking support, quality/latency/cost tradeoffs, **breaking behaviour changes across model releases** |

### Domain 6 — Prompt and Context Engineering (11.0%)

| Skill | % | Scope as published |
|---|---|---|
| Prompt Engineering | 4.6 | Instruction clarity, few-shot examples, **system vs user placement**, output constraints, placement across components, iterative refinement, input sanitization |
| Context Engineering | 3.8 | Context-window management, **preventing context drift and bloat (tool output pruning, compaction)**, context isolation through subagents or multi-step workflows |
| Output Handling | 2.6 | Structured output patterns, response validation, **defensive parsing, skepticism toward confident output** |

### Domain 7 — Security and Safety (8.1%)

| Skill | % | Scope as published |
|---|---|---|
| AI Application Security | 3.2 | **Prompt injection awareness and mitigation**, jailbreak defence, untrusted input handling, data leakage prevention, PII handling, authN/authZ, confidentiality, integrity |
| Guardrails and Safe Deployment | 2.3 | Content policy, **guardrail layering**, secure-by-design — privacy, IAM, least privilege |
| Identity, Secrets, and Key Management | 1.6 | Secrets, credentials and API keys across dev and production; identity validation, access approval and level verification, authorized-access monitoring |
| Claude Hooks | 1.0 | Hooks as guardrails to **prevent destructive actions** |

### Domain 8 — Tools and MCPs (10.6%)

| Skill | % | Scope as published |
|---|---|---|
| Tool Implementation | 4.4 | Tool use and function calling, configuration for external systems, **tool description writing**, error handling, usage patterns (agentic harness dispatch, client- vs server-side tools, approval patterns), tool-set construction |
| Agentic Customization | 4.1 | **Tradeoffs among built-in Tools, custom Tools, Skills, and MCPs** — selecting the right one for a use case |
| MCP Server Development | 2.1 | Server authoring, deployment, integration; MCP resources, tools and prompts; **communication patterns — stdio, sockets, client vs server** |

> **No MCP specification revision is named anywhere in v1.0.** The 2025-11-25 and 2026-07-28 revisions
> differ in breaking ways. The published skill scope is conceptual (resources/tools/prompts, stdio vs
> sockets, client vs server) and none of it turns on revision-specific detail — learn the concepts,
> and treat spec-version trivia as out of scope.

---

## 3. What the guide settled — the three blocking questions

**"Applications and Integration" at 33.1% is not a Claude catch-all.** It is six named skills, and
**13.6 of its 33.1 points are general software engineering and solution work** that is not
Claude-specific at all: Software Engineering Foundations (7.4), Understanding Requirements (3.4), and
Systems Life Cycle (2.8) — REST, JSON, async, version control, SDLC, code review, refactoring,
requirements analysis, life-cycle frameworks. That is **roughly 7 items of the 53** on ground that
favours an experienced consultant and architect.

**Eval at 2.6% and Claude Code at 3.1% are correct as published.** The prep-path lesson minutes simply
do not map to exam weight — Anthropic teaches Claude Code and evals at length and tests them lightly
as standalone domains, with the material redistributed into Applications and Integration and Agents.

**"Accelerators & IP Contribution" is not on the blueprint.** That 155-minute lesson — 20% of the
official prep path — maps to no domain and no skill. Treat it as partner enablement, **not exam
preparation.**

---

## 4. Corrections to what this file said before the guide arrived

Recorded rather than quietly overwritten, because the pre-guide version drove planning for a day.

**The skill count was wrong in this file, and in four others, for one day.** This file said the guide
publishes **21 skills**. It publishes **25**. Counting the Section 6 objective pages directly:
3 + 6 + 1 + 1 + 4 + 3 + 4 + 3 = 25, and those 25 weights sum exactly to their domains and to 100.0.
Found 2026-08-20 by an agent building the mock-exam template, and verified against the guide text
before correcting. Corrected in `CLAUDE.md` (both levels), `ROADMAP.md`, `README.md` (both levels),
`notes/README.md`, `prep with quiz/CCDV-F_Corpus-Index_v1.md`, `prep with quiz/EXAM-LOG.md` and
`Outputs/CCDV-F_Syllabus_v1.md`.

**Nothing structural moved.** The corpus index's section map already listed all 25 sections under a
heading that said 21 — the map was right and its label was wrong. Section numbering is untouched, so
the miss log stays durable. What was wrong was a count, repeated confidently, that nobody had counted.

**The community weightings were exactly right.** All eight domain figures, the 53-item count, the
120-minute limit, the $125 fee, 720/100–1,000, and the 12-month validity match the official guide
precisely. `claudecertificationguide.com` and `ravikirans.com` were transcribing this document.

**The "contradiction" flagged here was real but pointed the wrong way.** This file argued that Eval at
2.6% and Claude Code at 3.1% conflicted with the official lesson minutes, and that "either the domain
absorbs less of that lesson than its title suggests, or the figure is wrong." The first branch was
correct and the doubt was misdirected — the numbers were never wrong. Holding quotas until the guide
landed was still the right call procedurally; the inference that the numbers looked suspect was not.

**The item structure is standalone, as the community source said.** No scenario blocks. The
program-wide FAQ language about "scenario-based multiple response questions" does not describe this
exam's structure — items are individual, each stating its own response count. **The block architecture
CCAR-F used is not needed here.**

**The exam tests judgement, not code production.** See the next section. This is the correction that
matters most for planning.

---

## 5. Item style — what the three sample questions show

The guide includes three samples, stated to "show the style and cognitive level of the exam."

| Sample | Domain | Shape |
|---|---|---|
| 1 | Applications and Integration | 10,000 documents overnight, cost-sensitive → choose Batch API over parallel sync, lowering `max_tokens`, or downsizing the model |
| 2 | Security and Safety | Hidden prompt-injection text in a user-submitted page → isolate untrusted content + guardrails, over temperature, a polite system-prompt request, or a bigger model |
| 3 | Tools and MCPs | Internal REST service, reusable across apps, independently maintained → build an MCP server, over prompt hard-coding, pasting data, or a built-in tool |

**None of the three shows a line of code, and none asks the candidate to produce one.** All three are
short scenarios with four options, testing whether you pick the right approach under a stated
constraint. The distractors are recognisable families: a plausible-but-irrelevant lever, a
non-enforceable control, a bigger-hammer answer.

That matches the blueprint's own language, which runs on *principles, patterns, tradeoffs, decision
criteria, techniques, practices, considerations* throughout. Nothing in the 25 published skills
requires recalling a parameter name or writing a call from memory, and the format is
multiple-choice/multiple-response — you select, you do not produce.

**Confidence and its limit.** Three items is thin, and the guide calls them illustrative. But
Anthropic chose them to represent cognitive level, and they agree with the blueprint's phrasing and
with the item format. Treat the exam as judgement-shaped — much closer to CCAR-F than to a coding
test — while staying alert for code-bearing stems, which the format permits even if these samples do
not show one.

---

## 6. How Anthropic says to prepare — quoted from Section 7

There is **no single required course**, and Anthropic "does not guarantee that any particular resource
ensures a passing result." The guide recommends:

- Study the Section 6 blueprint and **self-assess against each objective**
- Review official documentation for the Claude API, models, prompt engineering, Claude Code, Skills, MCP
- **Build and operate at least one Claude application** that exercises the API, integrates one or more
  tools, applies basic prompt and context engineering, and includes simple security and evaluation
  practices
- Practise the competencies: writing prompts and system instructions, building agents and workflows,
  configuring Claude Code, managing tokens and cost, implementing guardrails, creating custom tools or
  MCP servers
- Complete the sample questions to familiarise yourself with item style

Note the scope of the build advice: **one application**, exercising several areas. Not a portfolio.
