# CCAR-P — Background Material Index

**Compiled:** 2026-08-18 · **Covers:** the twelve months to the sitting
**Rule:** every entry states where it came from. Nothing here is recalled from memory — each URL was
retrieved in the session that built this file, or is marked as needing sign-in.

Material is tiered by how much it decides the outcome. Tier 0 blocks everything. Tier 1 is the
syllabus. Tier 2 is the primary technical spine. Tier 3 covers the 35% of this exam that Foundations
never touched. Tier 4 is what Ram already owns and should not rebuild.

---

## TIER 0 — Blocking. Nothing downstream is trustworthy without these.

| # | Item | Where | Status |
|---|---|---|---|
| 0.1 | **CCAR-P Official Exam Guide (PDF)** | Anthropic Partner Academy → Claude Certified Architect – Professional certification page | ⛔ Needs Partner Network sign-in. **Do this first.** |
| 0.2 | Certification terms & policies | Same page | ⛔ Needs sign-in |
| 0.3 | Pearson VUE CCAR-P exam detail page | pearsonvue.com/us/en/anthropic.html | ✅ Confirms exam code CCAR-P |

Drop 0.1 into `sources/` and every ⚠️ in `EXAM-FACTS_v1.md` resolves in one pass.

---

## TIER 1 — The official syllabus (Anthropic Partner Academy)

**Prep path: "Claude Certified Architect – Professional" — 5 lessons, 733 min (~12.2 h).**
Verified from the Academy path page.

| # | Lesson | Min | Maps to blueprint domain |
|---|---|---|---|
| 1.1 | Claude Platform & Solution Design | 238 | Solution Design & Architecture |
| 1.2 | Enterprise Integration & Production | 158 | Integration |
| 1.3 | Responsible AI, Safety & Risk for Architects | 114 | Governance, Safety & Risk |
| 1.4 | Stakeholder Engagement, Lifecycle & GTM | 178 | Stakeholder Comms & Lifecycle |
| 1.5 | Team Enablement & Operational Productivity | 45 | Developer Productivity & Enablement |

**Academy pre-enrolment courses** (stated on the path page). Ram has effectively covered the first
five through the Foundations run — confirm rather than re-sit:
Claude 101 · Claude Code in Action · AI Fluency: Framework & Foundations · Building with the Claude
API · Introduction to Model Context Protocol · AI Capabilities and Limitations.

> Note what is missing from that path: there is **no** dedicated evaluation/testing lesson, yet the
> community blueprint puts Evaluation, Testing & Optimisation at 16%. Either the guide folds it into
> lesson 1, or the weighting is wrong. Resolve against Tier 0.1.

---

## TIER 2 — Anthropic primary technical sources (public, free)

These are the spine for Integration, Solution Design, and Models/Prompting/Context — roughly 49% of
the paper under the community weightings.

**Engineering blog** — `anthropic.com/engineering`. All URLs below retrieved 2026-08-18.

| Article | Why it matters here |
|---|---|
| [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) | The canonical pattern vocabulary. Foundations tested it implicitly; Professional will test *choosing between* patterns under constraints |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context as finite resource — the Professional-level framing of D5 |
| [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Tool design + evaluating your own tools |
| [Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) | Named in the Foundations exam description as core technology |
| [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Production multi-agent, with the cost/latency trade-offs stated |
| [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Lifecycle + state persistence across sessions |
| [Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) | Deployment topology |
| [Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Skills as a config mechanism — a known weak spot (see below) |
| [Building Effective AI Agents — Architecture Patterns and Implementation Frameworks (PDF)](https://resources.anthropic.com/hubfs/Building%20Effective%20AI%20Agents-%20Architecture%20Patterns%20and%20Implementation%20Frameworks.pdf) | Long-form version, good for the Solution Design domain |

**Product documentation** — Claude Docs. Sections to work through: Messages API · tool use ·
Message Batches API · MCP · prompt engineering · context editing and management · Claude Code
configuration · Agent SDK · model selection and pricing.

---

## TIER 3 — The 35% Foundations never covered

Governance/Safety/Risk (14%) + Stakeholder Comms/Lifecycle (14%) + Developer Enablement (7%). This
is the genuine new ground and it needs the most calendar time.

### 3A · Governance, Safety & Risk — Anthropic-first

| Source | Note |
|---|---|
| [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) — and [v3.0, effective 2026-02-24](https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0) | The AI Safety Level (ASL) framework. Current version is v3.0 — check for a newer one before the sitting |
| [RSP v3.0 announcement](https://www.anthropic.com/news/responsible-scaling-policy-v3) | What changed and why — useful for the "defend the decision" framing |
| [Transparency Hub / voluntary commitments](https://www.anthropic.com/transparency/voluntary-commitments) | Anthropic's own stated obligations |
| Anthropic Usage Policy | Prohibited uses — likely direct exam content |
| Enterprise security controls: SSO, SCIM, audit logs, role-based permissions | Named in Anthropic's enterprise material; maps to the Integration + Governance overlap |
| ISO/IEC 42001:2023 (AI management systems) | Anthropic holds this certification. Worth knowing what the standard requires |
| Frontier Compliance Framework | Published alongside the RSP |

### 3B · Governance — external frameworks

The stated audience covers financial services, healthcare, retail, technology, education and
government. Regulated-sector questions usually assume a shared vocabulary:
- **NIST AI Risk Management Framework** (Govern / Map / Measure / Manage)
- **EU AI Act** risk tiers and obligations for high-risk systems
- Sector basics as they touch AI: data residency, PII handling, audit trail requirements

⚠️ None of this is confirmed as examinable. Treat as insurance, not syllabus, until Tier 0.1 lands.

### 3C · Stakeholder Communication & Lifecycle

Ram's professional home turf as an Infosys consultant — this domain should be a strength, not a
gap. What to convert from instinct into exam-shaped knowledge: build-vs-buy defence, TCO and
cost-per-outcome modelling for LLM systems, pilot→production gating, adoption metrics,
change management, and how to present a model-selection decision to a non-technical sponsor.

### 3D · Developer Productivity & Operational Enablement (7%)

Smallest domain. Team-level Claude Code adoption, shared configuration, onboarding, and measuring
whether an engineering org is actually getting value.

---

## TIER 4 — Assets Ram already owns (do not rebuild)

| Asset | Location | Reuse |
|---|---|---|
| Foundations corpus D1–D5 `_v2` (~155 KB) | `Projects\Claude Certified Architect Prep\prep with quiz\` | Direct feed for the Models/Prompting/Context domain (~13%) and parts of Solution Design |
| `EXAM-LOG.md` + orchestration prompt v10 | Same folder | The mock-generation engine that produced 14 papers. Port, don't reinvent |
| Full 64-card miss corpus | `CCA-Prep_Missed-Questions-Review_v1.html` | The habit-level errors carry over even though the syllabus doesn't |
| **Eval Design Blueprint** (~13.5k words) | `my blueprints\eval-blueprint\` | Directly serves Evaluation, Testing & Optimisation (16%) — the single biggest head start he has |
| Living Knowledge Layer blueprint | `my blueprints\Living Knowledge Layer\` | Lifecycle + operational enablement framing |
| AI-First Design Blueprint / PRD pipeline | `my blueprints\` + `/blueprint` skill | Solution Design domain |

---

## Carry-over weaknesses from the Foundations sitting

From the real CCAR-F score report, 2026-08-18. These are the objectives that scored 0%, and two of
them were open in the mock corpus for weeks:

1. **Selecting the Claude Code configuration mechanism** — CLAUDE.md vs `.claude/rules/` vs Skills
   vs hooks vs settings. Six mock instances across four papers, then 0% on the real paper. Still open.
2. **Agentic review architecture** — plan mode vs direct execution vs multi-phase. Flagged on Exam 8,
   marked recovered on Exam 10, 0% on the real paper.
3. Diagnosing misconfigured subagent spawning (tool permissions, AgentDefinition params, wiring).
4. Dynamic subtask decomposition that adapts as findings arrive.
5. Claude Code review configurations.
6. Context window optimisation — summarisation, sliding windows, structured state objects.

Items 3–6 never appeared as a miss in fourteen mock papers, so they are gaps in the *mock corpus*,
not in Ram. All six sit inside Professional's Models/Prompting/Context and Developer Enablement
domains. **Close these first — they are the only part of the Professional syllabus where a
documented, specific weakness already exists.**
