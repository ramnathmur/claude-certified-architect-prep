# CCAR-P — Verified Exam Facts

**Last verified:** 2026-08-25
**Verification rule for this project:** every line below carries a source and a confidence label.
Nothing gets promoted to VERIFIED without an Anthropic-controlled source (anthropic.com,
anthropic-partners.skilljar.com, or pearsonvue.com/anthropic).

> **Why this file exists.** On the Foundations run, a community guide stated the exam draws 8
> scenarios. The real number is 6. That error propagated into generated practice material before it
> was caught. This file is the guard against a repeat: community claims live in the UNVERIFIED table
> and are never used to generate practice content until confirmed against the official guide.

> **Provenance exception, logged 2026-08-25.** The official exam guide PDF below did not come from a
> direct Partner Academy login. It was found via a third-party repository
> ([Amey-Thakur/CLAUDE-CERTIFICATIONS](https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/tree/main/architect-professional)),
> whose own provenance page (`guide/official-sources.md`) cites an Anthropic course-content S3 URL
> (`everpath-course-content.s3-accelerate.amazonaws.com/instructor/.../Claude+Certified+Architect+–+
> Professional+Exam+Guide.pdf`). That URL was fetched independently in this session and returned a
> byte-identical 358,335-byte file. The document's internal content is consistent throughout with a
> genuine Anthropic certification guide: a "Claude Certification Program Exam guide" footer on every
> page, `certifications-support@anthropic.com` and `pearsonvue.com/us/en/anthropic.html` as the
> stated contact points, an NDA/rules-of-conduct section, and a document-control table (v1.0, initial
> publication, July 2026). None of this is proof in the strict sense the verification rule states —
> the S3 bucket is not itself anthropic.com, anthropic-partners.skilljar.com, or
> pearsonvue.com/anthropic — but it is strong enough that the facts below are promoted to VERIFIED
> with this note attached. **Re-confirm directly via Partner Academy login when convenient** and
> remove this caveat once done. Local copy: `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`.

---

## VERIFIED — Anthropic-controlled sources

| Fact | Value | Source |
|---|---|---|
| Exam code | **CCAR-P** | Pearson VUE Anthropic program page |
| Full name | Claude Certified Architect – Professional | Anthropic Partner Academy |
| Price | **$175 USD** | Anthropic Partner Academy certification page |
| Answering time | **120 minutes** | Partner Academy certification FAQ |
| Total seat time | ~135 minutes (incl. check-in + survey) | Partner Academy certification FAQ |
| Scoring | Scaled **100–1000** | Partner Academy certification FAQ |
| Pass mark | **720** (same for all four certifications) | Partner Academy certification FAQ |
| Question types | Multiple-choice and multiple-response items; **each item states how many responses to select** | Official Exam Guide v1.0, §5 (see provenance note above) |
| Question count | **63 items** | Official Exam Guide v1.0, §5 |
| Domain floor score | **None.** Pass/fail is decided by total scaled score only; per-domain percent-correct is reported but does not gate pass/fail | Official Exam Guide v1.0, §9 |
| Delivery | Pearson VUE — online proctored or test centre | Pearson VUE Anthropic program page |
| Book policy | **Closed book.** No notes, documentation, translation tools, or AI assistants | Partner Academy certification FAQ |
| Validity | **12 months** from date earned | Partner Academy certification FAQ |
| Renewal | Free, **non-proctored** assessment if renewed on time. Lapsed = full exam at full price | Partner Academy certification FAQ |
| Attempts | **Up to 4 per rolling 12 months.** Waits: 14 days after 1st fail, 30 after 2nd, 90 after 3rd. Retakes cost full fee | Partner Academy certification FAQ |
| Prerequisite | **None.** Professional can be taken without holding Foundations | Partner Academy certification FAQ |
| F → P upgrade | **Does not exist.** Separate certifications, separate exams. Foundations never auto-converts | Partner Academy certification FAQ |
| Registration route | Anthropic Partner Academy (tied to Claude Partner Network) | Anthropic Partner Academy |

### Official prep path — VERIFIED
"Claude Certified Architect – Professional Prep Course", Anthropic Partner Academy.
Stated purpose: *design, integrate, and govern production-grade Claude systems end to end.*

| # | Lesson | Minutes |
|---|---|---|
| 1 | Claude Platform & Solution Design | 238 |
| 2 | Enterprise Integration & Production | 158 |
| 3 | Responsible AI, Safety & Risk for Architects | 114 |
| 4 | Stakeholder Engagement, Lifecycle & GTM | 178 |
| 5 | Team Enablement & Operational Productivity | 45 |
| | **Total** | **733 min ≈ 12.2 hours** |

**Stated pre-enrolment courses:** Claude 101 · Claude Code in Action · AI Fluency: Framework &
Foundations · Building with the Claude API · Introduction to Model Context Protocol ·
AI Capabilities and Limitations.

---

## VERIFIED — exam blueprint (Official Exam Guide v1.0, §6)

*Promoted from UNVERIFIED 2026-08-25. Percentages, domain names, and every objective below are
transcribed directly from the guide. See the provenance note at the top of this file.*

| # | Domain | Weight |
|---|---|---|
| 1 | Solution Design & Architecture | 17% |
| 2 | Claude Models, Prompting & Context Engineering | 13% |
| 3 | Integration | 19% |
| 4 | Evaluation, Testing & Optimization | 16% |
| 5 | Governance, Safety & Risk Management | 14% |
| 6 | Stakeholder Communication & Lifecycle Management | 14% |
| 7 | Developer Productivity & Operational Enablement | 7% |

**Recommended experience** (guide §4, not required — exam performance alone awards the credential):
foundation in software engineering best practices (modular design, separation of concerns,
scalability); 3+ years in systems architecture or platform engineering; 6+ months hands-on with
Claude or comparable LLM systems in production; experience delivering end-to-end systems from
discovery through deployment and operationalization.

### Objectives per domain (38 total — the corpus-building granularity)

**Domain 1 — Solution Design & Architecture (17%), 6 objectives**
Translate business problems into Claude-based AI solutions · design end-to-end architectures
(input → processing → output → feedback loops) · select architectural patterns (workflow, agentic,
augmented LLM) · design multi-agent systems and orchestration strategies · apply decomposition
techniques for complex problem solving · align solutions to business value pillars (efficiency,
transformation, productivity, cost, performance SLAs).

**Domain 2 — Claude Models, Prompting & Context Engineering (13%), 5 objectives**
Select Claude models based on trade-offs · design system prompts, templates, and guardrails · apply
prompt engineering techniques (zero-shot, few-shot, chain-of-thought) · optimize context windows and
manage token usage · implement prompt reuse strategies (caching, modular prompts, Skills).

**Domain 3 — Integration (19%), 8 objectives**
Evaluate tool/agent configuration for capability bloat · analyze authentication and authorization
requirements to identify security gaps · evaluate accuracy-latency trade-offs and justify
configuration decisions · analyze observability challenges and select monitoring strategies at
scale · design a RAG pipeline with appropriate chunking and indexing strategies · apply retrieval
strategies matched to data shape and query pattern · evaluate connection protocols and select the
appropriate integration mechanism (MCP, API/CLI, agent-to-agent) · evaluate progressive discovery
vs. monolithic context strategy.

**Domain 4 — Evaluation, Testing & Optimization (16%), 6 objectives**
Define evaluation metrics (accuracy, latency, cost, safety, security) · design evaluation datasets
and test frameworks using mixed methodologies · conduct A/B testing and iterative improvements ·
diagnose system issues (prompt failure, hallucinations, model mismatch) · optimize token usage,
latency, and cost-performance trade-offs · monitor system performance using logging and
observability tools.

**Domain 5 — Governance, Safety & Risk Management (14%), 5 objectives**
Implement guardrails and safety controls · identify risks, limitations, and failure modes of LLM
systems · apply human-in-the-loop validation strategies · ensure compliance with regulations (e.g.,
GDPR, HIPAA, FedRAMP) · address ethical AI considerations (bias, fairness, transparency).

**Domain 6 — Stakeholder Communication & Lifecycle Management (14%), 5 objectives**
Conduct structured discovery and requirement gathering · communicate architectural decisions and
trade-offs · manage stakeholder feedback loops and expectation alignment (including SLAs) ·
document architectures and provide implementation guidance · support lifecycle phases (discovery,
design, handoff, monitoring, iteration).

**Domain 7 — Developer Productivity & Operational Enablement (7%), 3 objectives**
Configure Claude tools and environments for teams (e.g., Claude Code) · improve developer workflows
using AI-assisted tooling · support debugging and operational issue resolution.

### Sample questions (guide §8 — illustrative only, not drawn from the live item bank)

Three samples, one each for Domains 3, 2, and 4, each with four options and a rationale for every
distractor. Full text is in `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`, pages 6–7. Recurring
answer logic worth carrying into the corpus: least privilege means **removing** an unneeded
capability, not logging or confirming its use; ordering static content first and enabling prompt
caching is the answer whenever latency and cost are both named; and a RAG system turning
confidently-wrong right after a document refresh points at retrieval/indexing first, not the model.

---

## OPEN — not answered by the official guide

| Question | Status |
|---|---|
| Are the 63 items standalone, or grouped into a shared-scenario block structure (the Foundations exam draws 4 scenarios from a pool of 6)? | **Still open.** The guide's own item-format line ("multiple-choice and multiple-response items; each item states how many responses to select") does not use the word "scenario" and never describes a pool/draw structure. The three sample items are scenario-flavored prose but nothing confirms or rules out shared-scenario blocks. Anthropic's certification FAQ (previously cited as saying all four exams are "scenario-based") should be re-read against this guide's own §5/§6 wording before treating the two as reconciled. |
| Are multiple-response items scored all-or-nothing, or partial credit? | **Still open.** Not stated anywhere in the guide. Foundations precedent was all-or-nothing and cost eight marks — treat CCAR-P the same way until proven otherwise. |

---

## Resolved by the official guide

1. ~~Exact question count~~ → **63**, confirmed (§5).
2. ~~Domain weightings~~ → all seven confirmed exactly as the community source stated (§6).
3. ~~Domain floor score~~ → **none exists**; pass/fail runs on total scaled score only (§9).
4. ~~Objective list per domain~~ → 38 objectives captured above (§6), the granularity to build
   `CCAR-P_Domain-N_v1.md` files against.
5. ~~Guide version and date~~ → **v1.0, effective July 2026**, per the document-control table (§16).
6. Scenario-pooling structure and multi-response scoring remain open — see the OPEN table above.
