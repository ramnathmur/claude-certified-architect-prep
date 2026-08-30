# CCAR-P Objective Map — v1

**Built:** 2026-08-29 · **Source:** the seven `CCAR-P_Domain-N_v1.md` corpus files, read-only.
**Status of this file:** derived index. It assigns every corpus section to one of the 38 official
objectives so the generator can run an objective-level floor pass. It carries no exam facts and no
standing. `EXAM-FACTS_v1.md` remains the authority for the objective list itself.

## Why this file exists rather than an edit to the corpus

Only **62 of 78** sections carry an `| Objective |` row, and the strings that are present resolve to
**41 distinct spellings for 38 objectives** — `Select appropriate architectural patterns` and
`Select appropriate architectural patterns (workflow, agentic, augmented LLM)` are one objective
written two ways. Normalising that inside the corpus would edit all seven domain files. This map
does the same work without touching them, so corpus section numbering and content stay exactly as
they were last reviewed.

**Basis column:** `declared` = the section's own Objective row, normalised to a canonical ID.
`assigned` = the section carries no Objective row and is mapped here on subject matter.
`declared-dual` = the section's own row names two objectives.

Every `assigned` row is a judgement made during the engine build, not a corpus fact. Sixteen
sections are in that category. They are listed together in the audit section at the foot of this
file so they can be reviewed as a set.

## The 38 objectives

| ID | Domain | Objective | Sections | Facets |
|---|---|---|---|---|
| **O1.1** | D1 | Translate business problems into Claude-based AI solutions | 1.1, 1.2 | 9 |
| **O1.2** | D1 | Design end-to-end architectures (input - processing - output - feedback loops) | 1.9, 1.10 | 11 |
| **O1.3** | D1 | Select architectural patterns (workflow, agentic, augmented LLM) | 1.3, 1.4 | 9 |
| **O1.4** | D1 | Design multi-agent systems and orchestration strategies | 1.5, 1.6, 1.7, 1.8 | 21 |
| **O1.5** | D1 | Apply decomposition techniques for complex problem solving | 1.11 | 6 |
| **O1.6** | D1 | Align solutions to business value pillars | 1.12 | 6 |
| **O2.1** | D2 | Select Claude models based on trade-offs | 2.1 | 3 |
| **O2.2** | D2 | Design system prompts, templates, and guardrails | 2.2 | 4 |
| **O2.3** | D2 | Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought) | 2.3, 2.4 | 5 |
| **O2.4** | D2 | Optimize context windows and manage token usage | 2.5, 2.6, 2.7 | 4 |
| **O2.5** | D2 | Implement prompt reuse strategies (caching, modular prompts, Skills) | 2.8, 2.9 | 2 |
| **O3.1** | D3 | Evaluate tool/agent configuration for capability bloat | 3.1 | 5 |
| **O3.2** | D3 | Analyze authentication and authorization requirements to identify security gaps | 3.2, 3.3 | 8 |
| **O3.3** | D3 | Evaluate accuracy-latency trade-offs and justify configuration decisions | 3.4, 3.5 | 9 |
| **O3.4** | D3 | Analyze observability challenges and select monitoring strategies at scale | 3.6, 3.7 | 9 |
| **O3.5** | D3 | Design a RAG pipeline with appropriate chunking and indexing strategies | 3.8, 3.9, 3.10 | 13 |
| **O3.6** | D3 | Apply retrieval strategies matched to data shape and query pattern | 3.11, 3.12 | 10 |
| **O3.7** | D3 | Evaluate connection protocols and select the integration mechanism (MCP, API/CLI, agent-to-agent) | 3.13 | 6 |
| **O3.8** | D3 | Evaluate progressive discovery vs. monolithic context strategy | 3.14 | 5 |
| **O4.1** | D4 | Define evaluation metrics (accuracy, latency, cost, safety, security) | 4.1, 4.2 | 10 |
| **O4.2** | D4 | Design evaluation datasets and test frameworks using mixed methodologies | 4.3, 4.4, 4.5, 4.6, 4.7, 4.8 | 32 |
| **O4.3** | D4 | Conduct A/B testing and iterative improvements | 4.9 | 7 |
| **O4.4** | D4 | Diagnose system issues (prompt failure, hallucinations, model mismatch) | 4.10 | 7 |
| **O4.5** | D4 | Optimize token usage, latency, and cost-performance trade-offs | 4.11 | 7 |
| **O4.6** | D4 | Monitor system performance using logging and observability tools | 4.12 | 7 |
| **O5.1** | D5 | Implement guardrails and safety controls | 5.1, 5.2 | 8 |
| **O5.2** | D5 | Identify risks, limitations, and failure modes of LLM systems | 5.6, 5.7, 5.9 | 18 |
| **O5.3** | D5 | Apply human-in-the-loop validation strategies | 5.8 | 5 |
| **O5.4** | D5 | Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP) | 5.3, 5.4, 5.5 | 12 |
| **O5.5** | D5 | Address ethical AI considerations (bias, fairness, transparency) | 5.10, 5.11 | 9 |
| **O6.1** | D6 | Conduct structured discovery and requirement gathering | 6.1, 6.2, 6.3 | 12 |
| **O6.2** | D6 | Communicate architectural decisions and trade-offs | 6.4, 6.6 | 8 |
| **O6.3** | D6 | Manage stakeholder feedback loops and expectation alignment (including SLAs) | 6.5, 6.9, 6.10 | 8 |
| **O6.4** | D6 | Document architectures and provide implementation guidance | 6.7, 6.8 | 8 |
| **O6.5** | D6 | Support lifecycle phases (discovery, design, handoff, monitoring, iteration) | 6.11, 6.12 | 9 |
| **O7.1** | D7 | Configure Claude tools and environments for teams (e.g., Claude Code) | 7.1, 7.2, 7.8 | 25 |
| **O7.2** | D7 | Improve developer workflows using AI-assisted tooling | 7.3, 7.4, 7.5, 7.6 | 14 |
| **O7.3** | D7 | Support debugging and operational issue resolution | 7.7, 7.8 | 8 |

Every one of the 38 has at least one section. The objective floor pass in the orchestration prompt
is therefore satisfiable.

## Section to objective

| Section | Title | Primary | Secondary | Basis | Facets | Scenarios |
|---|---|---|---|---|---|---|
| 1.1 | Translating a Business Outcome into an Automatable Decision | O1.1 |  | declared | 5 | 1 |
| 1.2 | Baseline and Value Unit Before Design | O1.1 |  | declared | 4 | 1 |
| 1.3 | The Pattern Ladder — Selecting the Rung | O1.3 |  | declared | 5 | 1 |
| 1.4 | Workflow vs Agent — The Reverse Direction | O1.3 |  | declared | 4 | 1 |
| 1.5 | Single Agent vs Multi-Agent | O1.4 |  | declared | 5 | 1 |
| 1.6 | Coordinator Responsibilities and Root-Cause Location | O1.4 |  | assigned | 6 | 1 |
| 1.7 | Context Passing and Structured Handoff | O1.4 |  | assigned | 5 | 1 |
| 1.8 | Orchestration Topology — Parallel, Sequential, Iterative Refinement | O1.4 |  | declared | 5 | 1 |
| 1.9 | The Feedback Stage | O1.2 |  | declared | 5 | 1 |
| 1.10 | Input Boundary and Output Contract | O1.2 |  | declared | 6 | 1 |
| 1.11 | Decomposition Granularity and Technique Choice | O1.5 |  | declared | 6 | 1 |
| 1.12 | Business Value Pillars and SLA-Driven Design | O1.6 |  | declared | 6 | 1 |
| 2.1 | Model Selection Trade-offs | O2.1 |  | declared | 3 | 1 |
| 2.2 | System Prompt Design & Guardrails | O2.2 |  | declared | 4 | 1 |
| 2.3 | Few-Shot Prompting | O2.3 |  | assigned | 3 | 1 |
| 2.4 | Chain-of-Thought Reasoning Cues | O2.3 |  | assigned | 2 | 1 |
| 2.5 | Stateless API — The Fundamental Constraint | O2.4 |  | assigned | 2 | 1 |
| 2.6 | "Lost in the Middle" | O2.4 |  | assigned | 1 | 1 |
| 2.7 | Context Window Management Strategy | O2.4 |  | assigned | 1 | 1 |
| 2.8 | Prompt Caching | O2.5 |  | assigned | 1 | 1 |
| 2.9 | Modular Prompts & Skills | O2.5 |  | declared | 1 | 1 |
| 3.1 | Tool Surface Sizing & Capability Bloat | O3.1 |  | declared | 5 | 1 |
| 3.2 | Least Privilege — Removal vs Compensating Control | O3.2 |  | declared | 4 | 1 |
| 3.3 | Authorization Enforcement Point & Identity Propagation | O3.2 |  | declared | 4 | 1 |
| 3.4 | Accuracy–Latency Budgeting | O3.3 |  | declared | 5 | 1 |
| 3.5 | Perceived Latency vs Total Latency | O3.3 |  | declared | 4 | 1 |
| 3.6 | Observability — Trace Depth | O3.4 |  | declared | 4 | 1 |
| 3.7 | Trace Sampling Strategy at Scale | O3.4 |  | declared | 5 | 1 |
| 3.8 | RAG Chunk Boundaries | O3.5 |  | declared | 5 | 1 |
| 3.9 | Chunk Contextualization vs Chunk Enlargement | O3.5 |  | declared | 4 | 1 |
| 3.10 | Index Coupling & Post-Refresh Degradation | O3.5 |  | declared | 4 | 1 |
| 3.11 | Retrieval Mechanism vs Data Shape & Query Pattern | O3.6 |  | declared | 6 | 1 |
| 3.12 | Retrieval Depth vs Reranking | O3.6 |  | declared | 4 | 1 |
| 3.13 | Connection Protocol Selection | O3.7 |  | declared | 6 | 1 |
| 3.14 | Progressive Discovery vs Monolithic Context | O3.8 |  | declared | 5 | 1 |
| 4.1 | Metric Definition — Threshold Declared in Advance | O4.1 |  | declared | 5 | 1 |
| 4.2 | Metric Family — Safety vs Security | O4.1 |  | assigned | 5 | 1 |
| 4.3 | Evaluation Dataset Composition — Coverage over Count | O4.2 |  | declared | 6 | 1 |
| 4.4 | Stratified Reporting — the Aggregate-Accuracy Mask | O4.2 |  | assigned | 5 | 1 |
| 4.5 | Grader Selection — Deterministic First | O4.2 |  | assigned | 6 | 1 |
| 4.6 | Model-Graded Evaluation — Out-of-Family and Human-Calibrated | O4.2 |  | assigned | 5 | 1 |
| 4.7 | Two-Layer Evaluation — RAG and Agentic | O4.2 |  | assigned | 5 | 1 |
| 4.8 | Reliability Aggregation — pass@k vs pass^k | O4.2 |  | assigned | 5 | 1 |
| 4.9 | Prompt Change Release Path — Regression, Then Controlled A/B | O4.3 |  | declared | 7 | 1 |
| 4.10 | Diagnosis Order — Data and Retrieval Before Model | O4.4 |  | declared | 7 | 1 |
| 4.11 | Cost and Latency Optimization — Caching First | O4.5 |  | declared | 7 | 1 |
| 4.12 | Observability — Logging for Attribution | O4.6 |  | declared | 7 | 1 |
| 5.1 | Guardrail Layering | O5.1 |  | declared | 4 | 1 |
| 5.2 | Least Privilege in Tool Scoping | O5.1 |  | declared | 4 | 1 |
| 5.3 | Compliance Boundary Enforcement | O5.4 |  | declared | 4 | 1 |
| 5.4 | Regulatory Regimes — What Each Forces Into the Design | O5.4 |  | assigned | 4 | 1 |
| 5.5 | Retention & Auditability | O5.4 |  | declared | 4 | 1 |
| 5.6 | LLM Failure-Mode Diagnosis | O5.2 |  | assigned | 10 | 1 |
| 5.7 | Prompt Injection & Untrusted Retrieved Content | O5.2 |  | declared | 4 | 1 |
| 5.8 | Human-in-the-Loop Routing | O5.3 |  | declared | 5 | 1 |
| 5.9 | Independent Verification of Confident Output | O5.2 |  | declared | 4 | 1 |
| 5.10 | Bias & Fairness Measurement | O5.5 |  | declared | 5 | 1 |
| 5.11 | Transparency — Disclosure vs Explainability | O5.5 |  | declared | 4 | 1 |
| 6.1 | Discovery — Eliciting the Decision Behind the Request | O6.1 |  | declared | 4 | 1 |
| 6.2 | Bounding an Unbounded Requirement | O6.1 |  | declared | 4 | 1 |
| 6.3 | Error Cost Asymmetry as a Design Driver | O6.1 |  | declared | 4 | 1 |
| 6.4 | Reporting Performance to a Sponsor | O6.2 |  | declared | 4 | 1 |
| 6.5 | Metric Selection for a Stakeholder | O6.3 |  | declared | 0 ⚠ | 1 |
| 6.6 | Explaining the Limits of Automation | O6.2 |  | declared | 4 | 1 |
| 6.7 | Architecture Decision Records | O6.4 |  | declared | 4 | 1 |
| 6.8 | Implementation Guidance for a Receiving Team | O6.4 |  | declared | 4 | 1 |
| 6.9 | Service Commitments on a Probabilistic System | O6.3 |  | declared | 4 | 1 |
| 6.10 | Feedback Loops and Expectation Drift | O6.3 |  | declared | 4 | 1 |
| 6.11 | Pilot to Scale — the Assumption Audit | O6.5 |  | declared | 4 | 1 |
| 6.12 | Handoff, Monitoring, and Iteration | O6.5 |  | declared | 5 | 1 |
| 7.1 | Configuration Scope & Durable Enablement | O7.1 |  | declared | 7 | 1 |
| 7.2 | Configuration Mechanism Selection | O7.1 |  | declared | 10 | 1 |
| 7.3 | Plan Mode vs Direct Execution | O7.2 |  | declared | 7 | 1 |
| 7.4 | Workflow Refinement Technique Selection | O7.2 |  | declared | 0 ⚠ | 1 |
| 7.5 | AI Tooling in the Pipeline | O7.2 |  | declared | 7 | 1 |
| 7.6 | Measuring AI Tooling Value | O7.2 |  | declared | 0 ⚠ | 1 |
| 7.7 | Operational Debugging — Which Layer Owns the Symptom | O7.3 |  | declared | 0 ⚠ | 1 |
| 7.8 | Deterministic Enforcement — Hooks and Permission Rules | O7.1 | O7.3 | declared-dual | 8 | 2 |

⚠ = the section has no decision table, so it can supply items only through its exam scenario and
its misconception block. Four sections are in this state: 6.5, 7.4, 7.6, 7.7.

## Objective coverage per domain, against the paper quota

| Domain | Quota | Objectives | Floor items | Discretionary | Sections | Facets |
|---|---|---|---|---|---|---|
| D1 | 11 | 6 | 6 | 5 | 12 | 62 |
| D2 | 8 | 5 | 5 | 3 | 9 | 18 |
| D3 | 12 | 8 | 8 | 4 | 14 | 65 |
| D4 | 10 | 6 | 6 | 4 | 12 | 70 |
| D5 | 9 | 5 | 5 | 4 | 11 | 52 |
| D6 | 9 | 5 | 5 | 4 | 12 | 45 |
| D7 | 4 | 3 | 3 | 1 | 8 | 39 |

The floor pass costs 38 of the 63 items and fits inside every domain quota. The narrowest margin is
D7: 3 objectives against 4 items, leaving 1 discretionary item.

## Sections assigned here rather than declared in the corpus

| Section | Title | Assigned to | Reasoning |
|---|---|---|---|
| 1.6 | Coordinator Responsibilities and Root-Cause Location | O1.4 | Coordinator responsibilities and root-cause location are orchestration-design decisions. |
| 1.7 | Context Passing and Structured Handoff | O1.4 | Structured handoff between agents is an orchestration-strategy decision. |
| 2.3 | Few-Shot Prompting | O2.3 | Few-shot prompting is named in the objective text. |
| 2.4 | Chain-of-Thought Reasoning Cues | O2.3 | Chain-of-thought is named in the objective text. |
| 2.5 | Stateless API — The Fundamental Constraint | O2.4 | The stateless-API constraint is the reason context must be managed per request. |
| 2.6 | "Lost in the Middle" | O2.4 | Lost-in-the-middle is a context-window positioning concern. |
| 2.7 | Context Window Management Strategy | O2.4 | Context window management is named in the objective text. |
| 2.8 | Prompt Caching | O2.5 | Caching is named in the objective text. |
| 4.2 | Metric Family — Safety vs Security | O4.1 | Distinguishing the safety and security metric families is metric definition. |
| 4.4 | Stratified Reporting — the Aggregate-Accuracy Mask | O4.2 | Stratified reporting is a property of the evaluation framework's design. |
| 4.5 | Grader Selection — Deterministic First | O4.2 | Grader selection is a test-framework design decision. |
| 4.6 | Model-Graded Evaluation — Out-of-Family and Human-Calibrated | O4.2 | Model-graded evaluation is one of the mixed methodologies named in the objective. |
| 4.7 | Two-Layer Evaluation — RAG and Agentic | O4.2 | Two-layer RAG and agentic evaluation is a test-framework structure. |
| 4.8 | Reliability Aggregation — pass@k vs pass^k | O4.2 | pass@k versus pass^k is an evaluation-framework aggregation decision. |
| 5.4 | Regulatory Regimes — What Each Forces Into the Design | O5.4 | Regulatory regimes and what each forces into the design is compliance. |
| 5.6 | LLM Failure-Mode Diagnosis | O5.2 | Failure-mode diagnosis is the objective's own subject. |

Sixteen sections. If any assignment is wrong, the cost is that one objective is over-covered and
another under-covered on every paper — visible immediately in fidelity-gate check 5, and correctable
here without touching a corpus file.
