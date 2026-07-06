# CCA-F Generation Intelligence Log
Last updated: 2026-07-06 | Sessions recorded: 1

> AI-to-AI learning log. Records generation-quality observations so each run starts from accumulated intelligence rather than cold. EXAM-LOG.md is the audit trail; this file is the living intelligence document (overwritten in full each session per orchestration prompt Phase 5a.5).

## Key Distinctions Coverage Tracker
<!-- One row per of the 25 Key Distinctions from CCA-Prep_Key-Distinctions_v1.md. Cycle starts at 1 when first used. -->
| # | Domain | Cycle | Used In Exam(s) | Learner Signal | Notes |
|---|---|---|---|---|---|
| 1 | D3 | 1 | Exam 2 (Q15) | unknown | project vs user CLAUDE.md scope, team-shared conventions |
| 2 | D2 | 1 | Exam 2 (Q4) | unknown | .mcp.json + ${VAR} env substitution, shared config w/ per-dev tokens |
| 3 | D3 | — | not yet used | — | rules/ glob precedence |
| 4 | D3 | — | not yet used | — | — |
| 5 | D1 | 1 | Exam 2 (Q1) | unknown | stop_reason tool_use vs end_turn loop control |
| 6 | D1 | — | not yet used | — | coordinator-vs-direct multi-agent comms |
| 7 | — | — | not yet used | — | — |
| 8 | — | — | not yet used | — | — |
| 9 | — | — | not yet used | — | — |
| 10 | D2 | 1 | Exam 2 (Q16 area) | unknown | fix tool descriptions vs add routing layer |
| 11 | — | — | not yet used | — | — |
| 12 | — | — | not yet used | — | — |
| 13 | D3 | — | not yet used | — | context: fork (skipped as poor fit for Exam 2 blocks) |
| 14 | D4 | 1 | Exam 2 (Q area) | unknown | batch vs synchronous API selection |
| 15 | — | — | not yet used | — | — |
| 16 | D4 | 1 | Exam 2 (Q area) | unknown | few-shot vs instruction refinement |
| 17 | D1 | 1 | Exam 2 (Q area) | unknown | per-file passes vs single-pass review |
| 18 | — | — | not yet used | — | — |
| 19 | — | — | not yet used | — | — |
| 20 | D5 | 1 | Exam 2 (Q area) | unknown | structured error context vs generic failure |
| 21 | — | — | not yet used | — | case-facts block (skipped — poor fit for extraction block) |
| 22 | — | — | not yet used | — | — |
| 23 | — | — | not yet used | — | — |
| 24 | D5 | 1 | Exam 2 (Q area) | unknown | aggregate-accuracy masking / stratified sampling |
| 25 | — | — | not yet used | — | — |

Note: Exam 2 seeded ~9 KDs (well under the 15-per-FULL-60 cap), leaving the majority fresh for Exam 3. Learner signals are "unknown" pending Ram's first scored attempt.

## Scenario Block Rotation
| Scenario (official bank of 6) | Used in Exams | Count |
|---|---|---|
| Customer Support Resolution Agent | Exam 2 (Block A) | 1 |
| Code Generation with Claude Code | — | 0 |
| Multi-Agent Research System | — | 0 |
| Developer Productivity with Claude | Exam 2 (Block B) | 1 |
| Claude Code for Continuous Integration | Exam 2 (Block C) | 1 |
| Structured Data Extraction | Exam 2 (Block D) | 1 |

**Rotation guidance for Exam 3:** prioritise the two unused scenarios — **Code Generation with Claude Code** and **Multi-Agent Research System** — plus two least-recently-used from Exam 2.

## Corpus Section Freshness
### Heavy (used 3+ times — de-prioritise)
- (none yet — only one FULL-60 generated)

### Moderate (used 1–2 times)
- D1 §1.1, §1.7, §1.12, §1.13, §1.14, §1.15, §1.16, §1.17 — Exam 2
- D2 §2.2, §2.3, §2.5, §2.6, §2.8, §2.9 — Exam 2
- D3 §3.1, §3.2, §3.3, §3.6, §3.7, §3.8 — Exam 2
- D4 §4.1, §4.5, §4.6, §4.7, §4.9, §4.10, §4.11, §4.13, §4.16 — Exam 2
- D5 §5.4, §5.5, §5.8, §5.9, §5.11, §5.13 — Exam 2

### Fresh (not yet used — prioritise for Exam 3)
- D1 §1.2–§1.6, §1.8–§1.11, §1.18 (multi-agent coordinator patterns — fit the Multi-Agent Research scenario)
- D2 §2.1, §2.4, §2.7 (hooks)
- D3 §3.4, §3.5, §3.9–§3.12
- D4 §4.2–§4.4, §4.8, §4.12, §4.14, §4.15, §4.17–§4.20
- D5 §5.1–§5.3, §5.6, §5.7, §5.10, §5.12, §5.14

## Distractor Quality Notes
<!-- Verbatim distractor options that were too easy to reject — never reuse -->
- (none flagged this session — distractors were held to documented-misconception grounding)

## Question Pattern Library
### Effective Patterns (use these)
- "Named-system evolving narrative with per-question telemetry" — e.g., "Aria" / "Pathfinder" / "Northwind Freight" carrying one system across 15 questions with progressing metrics. Produced coherent block flow.
- "Concrete percentage/count anchor in the stem" (12% of cases, 15% wrong account, 388/400 batch results) — matches the official sample-question register.

### Weak Patterns (avoid these)
- Same-scenario-same-failure-mode framing that drifts toward the official practice-test stems. Four Exam-2 questions (A2, A3, A7, C4) were caught by the automated Jaccard dedup gate as near-clones of practice stems and replaced. **Lesson: block authors must diversify the FAILURE MODE, not just surface wording, when a topic overlaps the practice test's scenarios (Customer Support and CI overlap most).**

## Rationale Quality Notes
- All 60 questions carry whyRight + 3 whyWrong with corpus citations; no question failed the "distractor must name a documented misconception" gate on final pass.

## Session Reflections
### Session 1 — 2026-07-06
- **What worked:** Parallel per-block authoring (one agent per scenario, disjoint KD ranges + domain quotas assigned up front) produced an exact exam-level domain total (16/11/12/12/9) with no rebalancing. Automated Jaccard dedup + structural validation caught 4 near-clones the block authors' own self-checks missed — the QA gate is load-bearing, keep it.
- **What to do differently next session:** Give block authors the specific practice-test stems for their scenario AND an explicit "different failure mode, not just different wording" instruction, to reduce the near-clone rate before the QA gate. Consider a lighter first-pass dedup inside each block author.
- **Corpus gap noticed:** The Key-Distinctions file (25 traps) is oriented toward Customer-Support and Multi-Agent-Research scenarios; it has NO distinction covering built-in tool selection (§2.9 Grep/Glob/Edit-fallback/wrapper-tracing), even though Developer Productivity is now a first-class official scenario. Two independent block authors flagged this. **Recommended action: add ~3–5 built-in-tool Key Distinctions so Scenario-4 blocks can seed KDs as densely as the others.**
- **Blueprint ambiguity:** None blocking. The FULL-60 block×domain allocation worked cleanly with the per-block domain mixes chosen (A: D1×6/D2×3/D5×4/D3×1/D4×1; B: D2×5/D3×4/D1×4/D5×1/D4×1; C: D3×6/D4×5/D1×3/D2×1; D: D4×5/D5×4/D1×3/D2×2/D3×1).
- **Recommended next action before Exam 3:** (1) Add built-in-tool Key Distinctions to close the seeding gap. (2) Rotate to the two unused scenarios (Code Generation, Multi-Agent Research) — the latter unlocks the many fresh D1 multi-agent sections. (3) Have Ram attempt Exam 2 and paste the results JSON so the first real learner signals populate this tracker.
