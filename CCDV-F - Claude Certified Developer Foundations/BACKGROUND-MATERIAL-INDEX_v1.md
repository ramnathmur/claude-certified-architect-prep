# CCDV-F — Background Material Index

**Compiled:** 2026-08-19 · **Reconciled against the official guide v1.0 the same day.**
**Rule:** every entry states where it came from. Nothing here is recalled from memory — each URL was
retrieved in the session that built this file, or in the CCAR-P session of 2026-08-18 as marked.

Material is tiered by how much it decides the outcome. **Tier 0 is closed.** Tier 1 is the syllabus.
Tier 2 is the technical spine, now mapped to published skill weights. Tier 3 is the build work. Tier 4
is what Ram already owns.

---

## TIER 0 — Blocking. ✅ CLOSED 2026-08-19

| # | Item | Status |
|---|---|---|
| 0.1 | **CCDV-F Official Exam Guide** | ✅ **Held.** `sources/CCDV-F_Official-Exam-Guide_v1.0.pdf` — v1.0, effective July 2026, 14 pages. Fully reconciled into `EXAM-FACTS_v1.md` |
| 0.2 | Certification Terms and Conditions (PDF) | ⬜ Still behind Partner Network sign-in. Not blocking |
| 0.3 | Anthropic Certification Exam Policy (PDF) | ⬜ Same. Section 11–13 of the guide already covers the substance |
| 0.4 | [Pearson VUE Anthropic program page](https://www.pearsonvue.com/us/en/anthropic.html) | ✅ Retrieved 2026-08-19 |

**Re-download the guide quarterly.** v1.0 is the initial publication and states it is "subject to
change without notice." File any new revision alongside v1.0 rather than replacing it — having both
CCAR-F guide versions is what made its silent section drop visible.

---

## TIER 1 — The official syllabus

**Prep path: 5 lessons, 774 min.** Retrieved from the Academy path page 2026-08-19.

| # | Lesson | Min | Examinable? |
|---|---|---|---|
| 1.1 | MSO Foundations | 57 | ✅ |
| 1.2 | Production-Grade Prompting, Agents & Tool Use | 209 | ✅ |
| 1.3 | Claude Code, MCP & Integration | 142 | ✅ |
| 1.4 | Production Engineering, Evals & Security | 211 | ✅ |
| 1.5 | **Accelerators & IP Contribution** | 155 | ❌ **Not on the blueprint. Skip it.** |

> **The 155-minute saving.** Lesson 5 maps to no domain and no skill in the guide's Section 6. It is
> partner enablement, not exam preparation. Skipping it cuts the path from 774 to **619 minutes**.

✅ **All four examinable modules are captured locally — `sources/course-transcripts/`.** The modules
are written HTML, not video, so the full teaching text is extractable and the corpus can be built
against a fixed local source rather than by re-watching. **~381,000 characters across 83 screens**,
each module verified against its own declared screen count. Free-text checkpoint model answers are
included; select-two and drag-match items carry questions and options but no key (derivable from the
teaching screen that precedes each).

**This changes what Phase 1 costs.** The syllabus no longer has to be consumed at video pace — it can
be read, searched, and converted to decision rules directly from these files.

Each module carries three screen types the corpus wants directly:

- **Teaching** — decision tables, worked examples, tradeoff comparisons.
- **Watch Out** — a named production failure plus its postmortem (*"The description that sent Claude
  to the wrong tool"*, *"The agent that filled the window on session four"*). These convert almost
  one-for-one into ❌ Misconception blocks.
- **Checkpoints** — exam-shaped items from the authoritative source, with model answers.

**Lesson minutes do not predict exam weight.** Anthropic teaches Claude Code and evals at length —
lesson 1.3 is 142 min and lesson 1.4 is 211 min — and tests them at 3.1% and 2.6% as standalone
domains. The material is redistributed into Applications and Integration (33.1%) and Agents (14.7%).
Watch the lessons for content; allocate revision time by the blueprint.

### Prerequisite courses — none are required

The guide is explicit: *"There are no mandatory prerequisites or courses required to sit this exam.
The experience above is recommended, not required."* The Academy path lists nine. Six were covered on
the CCAR-F run. Three were not, and two of those are worth the time on weight grounds:

| Course | Verdict |
|---|---|
| **Model Context Protocol: Advanced Topics** | **Sit it.** Feeds Tools and MCPs (10.6%), where MCP Server Development is entirely new |
| **Claude Code 101** | **Sit it.** Feeds the documented 0% — Configuration Management (4.1%) + Claude Code Operation (3.1%) |
| **Claude Platform 101** | Optional. Overlaps Claude Application Design (8.6%), which needs building regardless |

---

## TIER 2 — Technical spine, mapped to skill weights

Read in weight × gap order. The full priority list is in `ROADMAP.md`; this is where the sources live.

### 2A · Claude Application Design (8.6%) — largest skill, entirely new

Published scope: *how Claude interprets instructions across interfaces (Claude Code, Desktop,
claude.ai, API, SDKs), content boundaries, schema design, session hygiene, plugin management.*

The cross-interface question is the distinctive one and it is not well covered by any single document.
Work `platform.claude.com/docs` for the API and SDK behaviour, `code.claude.com/docs` for Claude Code,
and the Help Centre for Desktop and claude.ai. **The examinable idea is that the same instruction
behaves differently depending on where it is placed** — build a comparison table across the five
interfaces and drill it.

### 2B · Claude API Mechanics (6.8%) + Technical Fundamentals (6.1%) — 12.9 points

`platform.claude.com/docs`, confirmed live 2026-08-19. Sections to work:

Messages API · tool use · streaming · **vision** · **extended thinking** · prompt caching ·
Message Batches API · **Messages API data access patterns** · **invoking Claude through third-party
vendors** · model selection and pricing.

Technical Fundamentals adds *SDKs that wrap REST APIs, and websockets* — general integration
mechanics, not Claude-specific.

> The guide's own Sample 1 is a batch-vs-sync tradeoff. That decision axis — latency-tolerant and
> cost-primary versus a user waiting — is worth knowing cold in both directions.

### 2C · Security and Safety (8.1%) — four skills, all new

| Skill | % | Where to read |
|---|---|---|
| AI Application Security | 3.2 | Prompt injection and jailbreak defence, untrusted input handling, PII, data leakage. Anthropic Usage Policy; the guide's own Sample 2 is a prompt-injection item |
| Guardrails and Safe Deployment | 2.3 | Content policy, guardrail layering, secure-by-design — privacy, IAM, least privilege. [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) for vocabulary; CCAR-P's Responsible-AI lesson covers this ground |
| Identity, Secrets, and Key Management | 1.6 | Secrets and API keys across dev and production, identity validation, access approval, authorized-access monitoring |
| Claude Hooks | 1.0 | [Claude Code hooks docs](https://code.claude.com/docs) — hooks as guardrails preventing destructive actions. Also appears under Agent Construction |

**Sample 2's rationale is the model answer to memorise the shape of:** isolate untrusted content from
trusted instructions, enforce least-privilege guardrails. And note its warning — a more
instruction-following model can be *more* susceptible to injection, not less.

### 2D · Agents and Workflows (14.7%)

**Anthropic engineering blog** — URLs retrieved 2026-08-18 in the CCAR-P session.

| Article | Feeds |
|---|---|
| [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) | Agent Architecture (4.5%) — **workflow vs agent decision criteria**, supervisor hierarchies, subagents |
| [Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) | Agent Construction (5.3%) — the SDK this skill is named for |
| [Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) | Agent Construction — **self-hosted vs Anthropic-hosted deployment**, named explicitly in the skill |
| [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Agent Construction — custom loops and harnesses |
| [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Agent Patterns (4.9%) — cost and latency tradeoffs stated concretely |

**New and not covered by any of the above:** the skill names **Strands, LangGraph, PydanticAI** as
agentic abstraction frameworks. None is an Anthropic product and none appears in the CCAR-F corpus.
Read each project's own documentation far enough to answer *when would you reach for this rather than
a custom loop* — that is the level the blueprint asks for.

### 2E · Tools and MCPs (10.6%)

`modelcontextprotocol.io`, retrieved 2026-08-19. Published scope is conceptual: server authoring,
deployment, integration, MCP resources/tools/prompts, and communication patterns — **stdio, sockets,
client vs server**.

| Source | Note |
|---|---|
| [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25) | For the concepts, not the version detail |
| [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/) · [MCP TypeScript SDK](https://ts.sdk.modelcontextprotocol.io/) | Build one — see Tier 3 |
| [MCP Feature Reference Server](https://example-server.modelcontextprotocol.io/) | Working reference implementation |
| [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Tool Implementation (4.4%) — **tool description writing** is named in the skill |
| [Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Agentic Customization (4.1%) — the built-in vs custom vs Skills vs MCP tradeoff |

> ✅ **Version risk resolved.** The guide names **no MCP specification revision**, and nothing in the
> published scope turns on revision-specific detail. The 2026-07-28 spec's breaking changes are not
> examinable. Learn the concepts.

### 2F · Software Engineering Foundations, Requirements, Life Cycle (13.6%) — cheapest points

Published scope: *REST APIs, JSON, asynchronous programming, version control, SDLC integration, code
review, small- and large-scale refactoring* · *functional and infrastructure requirements from business
requirements and solution architecture* · *life-cycle management concepts and frameworks*.

**None of this is Claude-specific, and Ram works on this ground professionally.** No reading list is
needed. What it needs is **exam-shaping**: turn known practice into stated decisions with
discriminators, the way every other corpus section is written. Roughly 7 items of the 53 sit here.

### 2G · Model Selection and Optimization (16.8%) — mostly owned

LLM Fundamentals (5.2%), Model Selection and Tradeoffs (2.7%) and Cost and Token Management (2.8%)
are largely CCAR-F ground. Newer surface to check: **fast mode, extended thinking, adaptive thinking,
effort levels**, and **breaking behaviour changes across model releases**. `platform.claude.com/docs`
model pages plus release notes.

---

## TIER 3 — The build work

**Right-sized to what the guide recommends**, quoted from Section 7:

> *"Build and operate at least one Claude application that exercises the API, integrates one or more
> tools, applies basic prompt and context engineering, and includes simple security and evaluation
> practices."*

One application, exercising five areas. Plus, on weight grounds, one MCP server and client (Domain 8
is 10.6%) and one Agent SDK agent with a hook (Agent Construction is 5.3% and entirely new).

**Assisted building is fine.** The value is the tradeoff intuitions — which the Domain 1 and Domain 8
items turn on — and those come from having shipped the thing, not from having typed it unaided. The
earlier version of this file called for unassisted reps; that was preparing for a code-production exam
the samples show this is not.

---

## TIER 4 — Assets Ram already owns (do not rebuild)

| Asset | Location | Feeds |
|---|---|---|
| CCAR-F `Domain-4_v2` (prompting) + `Domain-5_v2` (context) | `..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\` | §6.1 Context Engineering, §6.2 Prompt Engineering — 8.4% |
| CCAR-F `Domain-1_v2` (agentic architecture) | Same folder | §1.1 Agent Architecture, §1.3 Agent Patterns — 9.4% |
| CCAR-F `Domain-2_v2` (tools / MCP) | Same folder | §8.1 Tool Implementation — 4.4% |
| CCAR-F `Domain-3_v2` (Claude Code config) | Same folder | §2.6, §3.1 — **and the documented 0% lives here** |
| CCAR-F extraction-schema material | Same folder | §6.3 Output Handling — scored 100% on the real paper |
| `EXAM-LOG.md` + `CCA-Orchestration-Prompt_v10.md` | Same folder | The engine, ported here and re-quota'd to the real blueprint |
| Full 64-card miss corpus | `..\CCAR-F - ...\prep with quiz\CCA-Prep_Missed-Questions-Review_v1.html` | Habit-level errors carry over directly |
| Eval Design Blueprint (~13.5k words) | `my blueprints\eval-blueprint\` | §4.1 Debugging — **but note v1.0 lists no eval-design skill**, only debugging and error handling. Most of this blueprint is out of scope |
| Consulting practice — requirements, SDLC, architecture | — | §2.1, §2.2, §2.4 — 13.6%, needs shaping not learning |

---

## Carry-over weaknesses from the CCAR-F sitting

Six objectives scored 0% on the real CCAR-F paper. **All six sit inside CCDV-F scope**, and between
them they touch roughly **17% of the paper**.

| CCAR-F 0% objective | Lands in | Weight |
|---|---|---|
| **Claude Code configuration mechanism** — CLAUDE.md vs `.claude/rules/` vs Skills vs hooks vs settings. Six mock instances across four papers, then 0%. **Still open** | §2.6 Configuration Management + §3.1 Claude Code Operation | 7.2% |
| **Agentic review architecture** — plan mode vs direct execution vs multi-phase. Flagged Exam 8, marked recovered Exam 10, 0% on the real paper | §1.1 Agent Architecture | 4.5% |
| Diagnosing misconfigured subagent spawning | §1.1 + §1.2 | — |
| Dynamic subtask decomposition | §1.3 Agent Patterns | 4.9% |
| Claude Code review configurations | §3.1 Claude Code Operation | 3.1% |
| Context window optimisation | §6.1 Context Engineering | 3.8% |

Items 3–6 never appeared as a miss in fourteen mock papers, so they are gaps in the *mock corpus*, not
demonstrated gaps in Ram. **Close all six first**, whatever the build order otherwise says. Note that
the guide names *the CLAUDE.md hierarchy* explicitly under §3.1 — the exact thing that cost marks.

Behaviour-level habits across all 64 documented misses:

1. Reaching for a workaround beside a mechanism instead of a narrow adjustment to it.
2. Losing multiple-response items by being majority-right — all-or-nothing scoring cost eight marks.
   *(One relief: this exam states how many responses to select on every such item.)*
3. Choosing an option because of how it *sounds* rather than because it matches the stated requirement.
   **This is the single most relevant habit for this exam**, whose distractors are legitimate
   techniques that do not fit the stated constraint.

---

## Community sources — now redundant

| Source | Verdict |
|---|---|
| `claudecertificationguide.com/developer-foundations` | Accurate — every figure matched the official guide. **Superseded. Use the guide.** |
| `ravikirans.com` CCDV-F study guide | Same. Superseded |

Both were transcribing the real document. They were right, which is luck rather than vindication —
they were unverifiable at the time, and the discipline that held quotas until the guide landed stays.
