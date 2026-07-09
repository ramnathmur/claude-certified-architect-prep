# CCA-F Generation Intelligence Log
Last updated: 2026-07-09 (Open Findings Ledger + Question Pattern Library patched by audit-driven fix, not a formal /cca-exam session) | Sessions recorded: 2

> AI-to-AI learning log. Records generation-quality observations so each run starts from accumulated intelligence rather than cold. EXAM-LOG.md is the audit trail; this file is the living intelligence document (overwritten in full each session per orchestration prompt Phase 5a.5).

## Key Distinctions Coverage Tracker
<!-- One row per of the 29 Key Distinctions from CCA-Prep_Key-Distinctions_v1.md. Cycle starts at 1 when first used. -->
| # | Domain | Cycle | Used In Exam(s) | Learner Signal | Notes |
|---|---|---|---|---|---|
| 1 | D3 | 1 | Exam 2 (Q15) | unknown | project vs user CLAUDE.md scope, team-shared conventions |
| 2 | D2 | 1 | Exam 2 (Q4) | unknown | .mcp.json + ${VAR} env substitution, shared config w/ per-dev tokens |
| 3 | D3 | 1 | Exam 3 (Block B) | unknown | .claude/rules/ vs CLAUDE.md vs Skills — quarterly-close checklist split |
| 4 | D3 | 1 | Exam 3 (Block B) | unknown | project vs personal skill precedence, same name collides |
| 5 | D1 | 1 | Exam 2 (Q1) | unknown | stop_reason tool_use vs end_turn loop control |
| 6 | D1 | — | not yet used | — | coordinator-vs-direct multi-agent comms |
| 7 | D1 | 1 | Exam 3 (Block A) | unknown | root cause: narrow task decomposition |
| 8 | D1 | 1 | Exam 3 (Block A, Block D) | unknown | structured error context vs generic failure |
| 9 | D1 | 1 | Exam 3 (Block A) | unknown | transient vs permanent errors |
| 10 | D2 | 1 | Exam 2 (Q16 area); Exam 3 (Block A) | unknown | fix tool descriptions vs add routing layer |
| 11 | D1 | 1 | Exam 3 (Block A) | unknown | programmatic preconditions vs prompt instructions |
| 12 | — | — | not yet used | — | — |
| 13 | D3 | — | not yet used | — | context: fork (touched only as a distractor in Exam 3 Block B Q1, not seeded as a primary question) |
| 14 | D4 | 1 | Exam 2 (Q area); Exam 3 (Block D) | unknown | batch vs synchronous API selection / batches + tool use accuracy note |
| 15 | D3 | 1 | Exam 3 (Block C) | unknown | `-p`/`--print` vs nonexistent CLAUDE_HEADLESS/--batch/stdin-redirect |
| 16 | D4 | 1 | Exam 2 (Q area) | unknown | few-shot vs instruction refinement |
| 17 | D1 | 1 | Exam 2 (Q area) | unknown | per-file passes vs single-pass review |
| 18 | — | — | not yet used | — | — |
| 19 | — | — | not yet used | — | — |
| 20 | D5 | 1 | Exam 2 (Q area) | unknown | structured error context vs generic failure |
| 21 | — | — | not yet used | — | case-facts block (skipped twice now — poor fit for both extraction blocks so far) |
| 22 | — | 1 | Exam 3 (Block B) | unknown | Explore subagent isolation vs main-session survey |
| 23 | — | — | not yet used | — | — |
| 24 | D5 | 1 | Exam 2 (Q area) | unknown | aggregate-accuracy masking / stratified sampling |
| 25 | — | — | not yet used | — | — |
| 26 | D2 | — | not yet used | — | Grep vs Glob (content search vs path pattern) |
| 27 | D2 | — | not yet used | — | Edit vs Read+Write fallback (non-unique anchor) |
| 28 | D2 | — | not yet used | — | incremental investigation (Grep→Read) vs bulk read upfront |
| 29 | D2 | — | not yet used | — | MCP tool vs built-in tool preference (fix description, don't remove) |

**Coverage after 2 exams:** 17 of 29 KDs touched at least once ({1,2,3,4,5,7,8,9,10,11,14,15,16,17,20,22,24}). 12 remain completely untouched: {6,12,13,18,19,21,23,25,26,27,28,29}. **Sub-optimality noted:** KD#10 and KD#14 were reused in Exam 3 rather than drawing from the untouched KDs — both fit their block's scenario well, but future sessions should check the "not yet used" list before reaching for an already-seeded KD a second time, purely to spread first-pass coverage faster. Not a defect, just a missed optimization. **Priority for Exam 4:** #26–29 (built-in tools) are the natural seed set for any block drawing the Developer Productivity scenario — they exist specifically to close that scenario's previous KD gap and have not yet seeded a single question.

Learner signals remain "unknown" — no exam has been scored yet (see EXAM-LOG.md; Exam 1 and Exam 2 both still Pending). Exam 3 does not change this.

## Scenario Block Rotation
| Scenario (official bank of 6) | Used in Exams | Count |
|---|---|---|
| Customer Support Resolution Agent | Exam 2 | 1 |
| Code Generation with Claude Code | Exam 3 | 1 |
| Multi-Agent Research System | Exam 3 | 1 |
| Developer Productivity with Claude | Exam 2 | 1 |
| Claude Code for Continuous Integration | Exam 2, Exam 3 | 2 |
| Structured Data Extraction | Exam 2, Exam 3 | 2 |

All 6 official scenarios have now appeared at least once. **Rotation guidance for Exam 4:** prioritise the four scenarios still at count 1 — Customer Support Resolution Agent, Code Generation with Claude Code, Multi-Agent Research System, Developer Productivity with Claude — and avoid drawing Claude Code for CI or Structured Data Extraction a third consecutive time unless the confirmed-weakness rule specifically points there.

## Corpus Section Freshness
<!-- Computed from GROUND TRUTH: primary whyRight citations extracted directly from the embedded DATA JSON in both CCA-Prep_MockTest-2_v1.html and CCA-Prep_MockTest-3_v1.html (120 questions total), not from self-reported summaries. This is more reliable than prose-tallying and should be the standard method going forward — re-run the same extraction after every exam. -->

### Heavy (3+ primary uses across Exam 2 + Exam 3 — de-prioritise, max 1/exam)
D1 §1.7, §1.9, §1.13, §1.15, §1.16, §1.17 · D2 §2.3, §2.5, §2.6, §2.9 · D3 §3.7, §3.8, §3.9 · D4 §4.1, §4.11 · D5 §5.5, §5.9

### Moderate (2 uses)
D2 §2.7, §2.8 · D3 §3.1, §3.10, §3.11 · D4 §4.5, §4.9, §4.16, §4.17 · D5 §5.8, §5.11, §5.12

### Used once
D1 §1.1, §1.2, §1.4, §1.5, §1.6, §1.8, §1.11, §1.12, §1.14 · D2 §2.2 · D3 §3.2, §3.3, §3.4, §3.5, §3.6 · D4 §4.2, §4.6, §4.7, §4.8, §4.10, §4.14, §4.15, §4.18, §4.19 · D5 §5.2, §5.4, §5.6, §5.7, §5.10, §5.13

### Fresh (never a primary answer citation — prioritise for Exam 4, 14 sections)
D1 §1.3, §1.10, §1.18 · D2 §2.1, §2.4 · D3 §3.12 · D4 §4.3, §4.4, §4.12, §4.13, §4.20 · D5 §5.1, §5.3, §5.14

## Distractor Quality Notes
<!-- Verbatim distractor options that were too easy to reject — never reuse -->
- (none flagged — every distractor across both exams grounds in a documented misconception with a corpus citation)

## Question Pattern Library
### Effective Patterns (use these)
- "Same-tools-progressing-narrative continuity" — one recurring tool/config/system-under-test with progressing metrics across a block's ~15 questions (e.g., a tightening latency SLO, a rising batch-error rate). Produced coherent block flow in Exam 2 and Exam 3. CORRECTED 2026-07-09: both exams also wrapped this in an invented company/agent name ("Aria"/"Northwind Freight" in Exam 2, "Compendium"/"Fernbank" in Exam 3) — an independent cold audit against all 76 known real-exam question texts (PRACTICE-TEST-STEMS_v1.md §2, which already includes the official PDF's 12 samples) found that framing in ZERO of them (see Weak Patterns, below). The naming was never what produced the coherence; keep the metric/tool continuity, drop the invented names.
- "Concrete percentage/count anchor in the stem" (12% of cases, 388/400 batch results, 61%/55%/6%/22% dismissal rates) — matches the official sample-question register.
- "Self-caught positional-bias reshuffle" — Exam 3's Block A and Block C authors independently noticed an early draft clustering correct answers on one letter and reshuffled option order (not content) before finalizing. This should be a standard, explicit step every block author runs, not an incidental catch.

### Weak Patterns (avoid these)
- Same-scenario-same-failure-mode framing that drifts toward the official practice-test stems. Four Exam-2 questions were caught by the automated Jaccard dedup gate as near-clones and replaced (see Session 1). Exam 3's authors pre-empted this better — several (Block A, Block D) report catching and rewriting their own near-clones against the corpus's own canonical worked examples *before* submitting, which is a step up from Session 1.
- **Skipping the answer-position QA step entirely.** Exam 3's Block D author validated schema, quota, and dedup thoroughly but never checked correct-answer position distribution — all 15 of its questions landed on option A (a severe, exploitable "always guess A" pattern), while Blocks A and C explicitly ran and reported this check. This was caught only by the coordinating session's own aggregate verification, not by any block author's self-QA. **Every block author must explicitly check and report its own correct-index distribution before declaring done — this is now a required step, not an optional nicety.**
- **Invented company/product/agent names in the Situation opening** (e.g., "Aria", "Meridian Retail", "Northwind Freight", "Compendium", "Fernbank"). An independent cold audit against all 76 known real-exam question texts (PRACTICE-TEST-STEMS_v1.md §2, which already includes the official PDF's 12 samples) found this pattern in ZERO of them — the corpus uses generic "your agent" / "the pipeline" / "production logs show" framing throughout. Exam 2 and Exam 3 both used named fictional systems throughout, which had been mis-logged as an Effective Pattern above; corrected 2026-07-09 (see CCA-Orchestration-Prompt_v9.md Phase 4.b and 4.e for the binding rule). Keep the same-tools-progressing-metrics continuity within a block; never invent a proper-noun company, product, or persona name for it.

## Rationale Quality Notes
- All 120 questions across Exam 2 + Exam 3 carry whyRight + 3 whyWrong with corpus citations; no question has failed the "distractor must name a documented misconception" gate.

## Open Findings Ledger
<!-- Structured, gate-checked. Every PROCESS_BUG and CORPUS_GAP finding from any
     Session Reflections entry gets a row here on the session it's first noticed,
     and stays until its Status is FIXED, DEFERRED — [reason], or (CORPUS_GAP only)
     VERIFIED-STILL-OPEN. This table, not prose in Session Reflections, is what the
     Phase 5a.5 promotion gate checks every session — see CCA-Orchestration-
     Prompt_v7.md Phase 5a.5 step vii. Status must be re-verified against the real
     target file each session, never copied forward from the prior session's row. -->

| ID | Type | First noted | Finding (one line) | Target file(s) | Status | Notes |
|---|---|---|---|---|---|---|
| PB-01 | PROCESS_BUG | S2 | Nested background-agent parent stalls (~250K tokens/stall) waiting on children with no auto-wake | Orchestration Phase 4 | FIXED (v7, Phase 4.7) | Documented as a known architecture property with an explicit stall-watch instruction, not left as a surprise to rediscover |
| PB-02 | PROCESS_BUG | S2 | Block-level correct-answer-position-distribution self-check not enforced in blueprint/verification — one exam block shipped all 15 questions at option A | CLAUDE.md Step 4; Orchestration Phase 4.e + self_verification | FIXED (CLAUDE.md v2.1; Orchestration v7) | |
| PB-03 | PROCESS_BUG | S2 | Coordinator's own dedup-verification regex silently dropped untagged stems (undercounted, caught only by a count mismatch) | Orchestration Phase 2.d | FIXED (v7) | Standing count-mismatch sanity check added |
| PB-04 | PROCESS_BUG | S2 | Sibling sub-agents cannot address each other directly for cross-block name-collision checks | Orchestration Phase 4.6 | FIXED (v7) | Documented as a known limitation; coordinator retains cross-block collision-checking responsibility |
| PB-05 | PROCESS_BUG | S1 | Block authors not given scenario-specific practice stems + explicit "different failure mode, not just wording" instruction | Orchestration Phase 4.6 | FIXED (v7) | Folded into the new delegation task-spec step |
| PB-06 | PROCESS_BUG | S2 | Corpus-freshness tally method (ground-truth JSON citation extraction) was a norm only in this file's prose, not bound in the orchestration prompt | Orchestration Phase 5a.5 | FIXED (v7) | |
| CG-01 | CORPUS_GAP | S1 | No Key Distinction covered built-in-tool selection for the Developer Productivity scenario | CCA-Prep_Key-Distinctions_v1.md | FIXED (v1.1, 2026-07-06, §Built-in Tools #26–29) | Independently re-verified against the live file on 2026-07-07 — confirmed on disk. Session 2 mis-reported this as still open one full session after it had already landed; this is the exact "logged-and-forgotten" failure this ledger exists to prevent. |
| CG-02 | CORPUS_GAP | audit | Every "25 high-yield exam traps" reference (CLAUDE.md, CCA-Prep_Corpus-Index_v2.md, all orchestration-prompt versions) is stale — the file now has 29 entries | CLAUDE.md; CCA-Prep_Corpus-Index_v2.md; CCA-Orchestration-Prompt (current version) | FIXED (Ram approved 2026-07-07; count corrected to 29 in all three files; KD tracker above extended with rows 26–29) | First corpus-content fix processed through the new gate — routed to Pending Corpus Decisions, Ram explicitly approved, then applied. Demonstrates the gate working end to end. |
| PB-07 | PROCESS_BUG | audit (2026-07-07, Ram: "not able to locate" the exam) | Output directory for generated exam HTML files was never stated in CLAUDE.md or the orchestration prompt — only followed as an unstated convention inherited from Exam 1's placement in a project-root `practice/` folder that holds unrelated static practice materials. Result: Exams 2 and 3 landed somewhere disconnected from the generator system and Ram couldn't find them. | CLAUDE.md Step 6; CCA-Orchestration-Prompt Phase 4.f | FIXED (CLAUDE.md v2.2; Orchestration v8) | Output directory now explicit: `mock-exams/` inside `prep with quiz/`, alongside the system that generates it. Exams 2 and 3 moved there; every cross-reference (EXAM-LOG.md, SESSION-STATE.md, resume-prompt.md, the student-facing MCQ guide) updated. Caught outside a formal `/cca-exam` session — this ledger applies regardless of how a finding surfaces. |
| PB-08 | PROCESS_BUG | audit (2026-07-09) | Orchestration prompt Phase 4.b and 4.e instructed writing an invented, per-block company/agent name (e.g. "Aria", "Northwind Freight") as part of each scenario narrative. An independent cold audit against all 76 known real-exam question texts (PRACTICE-TEST-STEMS_v1.md §2, which already includes the official PDF's 12 samples) found this pattern in ZERO of them — the real exam uses generic "your agent"/"production logs show" framing. GENERATION-INTELLIGENCE.md's Question Pattern Library had also mis-recorded named-system narratives as an Effective Pattern (corrected above, same session). | GENERATION-INTELLIGENCE.md Question Pattern Library; CLAUDE.md Step 2/Step 4; CCA-Orchestration-Prompt Phase 4.b, 4.b.6, 4.e | FIXED (GENERATION-INTELLIGENCE.md, CLAUDE.md v2.3, Orchestration v9, this session) | Keep same-tools-progressing-metrics continuity within a block; drop invented proper-noun company/product/persona names in favor of generic framing. |
| PB-09 | PROCESS_BUG | audit (2026-07-09) | Correct-answer letter distribution was only checked post-hoc, per block, with a threshold tuned to catch single-block extremes. Exam 2 shipped with 33% of its 60 correct answers on option A — no single block was extreme enough to trip the existing check, but a mild, direction-consistent lean across 3 of 4 blocks compounded into a visible bias in the exam-wide aggregate. Exam 2 predates the check entirely (built via orchestration-prompt v5, before v2.1 added it) — this was never a case of the check being skipped. | CLAUDE.md Step 4; CCA-Orchestration-Prompt Phase 4.d.5/4.e/4.e.5/4.b.6/4.e.6 | FIXED (CLAUDE.md v2.3, Orchestration v9, this session) | Correct-answer-letter sequence is now pre-planned per block (balanced multiset) BEFORE any option text is written — the primary balance mechanism. The prior post-hoc distribution count is retained as a verification backstop against the pre-plan, not the sole mechanism. Does not apply retroactively to Exam 2 or Exam 3. |
| PB-10 | PROCESS_BUG | audit (2026-07-09) | A scenario block's domain tally can contradict its own scenario's official primary domains. Exam 3's Structured Data Extraction block (official primary domains D4/D5) shipped D2=5 outnumbering D5=2 more than 2-to-1, even though Step 4 already said to "skew toward primary domains" — nothing checked it before shipping. | CLAUDE.md Step 4; CCA-Orchestration-Prompt Phase 4.b.6/4.e.6 | FIXED (CLAUDE.md v2.3, Orchestration v9, this session) | New required self-check: tally each block's domain distribution against its scenario's official primary domains before shipping; a non-primary domain outnumbering a primary domain must be fixed by swapping in newly-seeded primary-domain questions. |
| PB-11 | PROCESS_BUG | audit (2026-07-09) | Inline code/config token rate in options has no target and drifts freely — Exam 2 shipped at 9.6% of options, Exam 3 at 24.6%, against a ~21% reference rate PRACTICE-TEST-STEMS_v1.md §3 derives from the real 76-question community corpus. | CLAUDE.md Step 4; CCA-Orchestration-Prompt Phase 4.a.5/4.e.6 | FIXED (CLAUDE.md v2.3, Orchestration v9, this session) | New explicit target band: 20-25% of options exam-wide should carry an inline code/config token, concentrated naturally in D2/D3 content; required exam-wide tally before shipping. |

**Coverage:** 13 of 13 rows FIXED this session (9 carried forward already-FIXED from prior sessions; 4 new rows — PB-08 through PB-11 — opened and FIXED in the same session per the 2026-07-09 independent audit); zero rows carried forward silently unresolved. F3 (stem/option word-count budget) and F6 (scenario-rotation disclosure) from the same audit did not get ledger rows — F3 is a style-calibration tightening, not a process bug, and F6 is a landing-card disclosure/UX fix, not a generation-logic defect; both were still applied to CLAUDE.md v2.3 and Orchestration v9 this session.

## Pending Corpus Decisions
<!-- Every CORPUS_GAP row from the Open Findings Ledger with Status = PENDING,
     OPEN, or VERIFIED-STILL-OPEN lands here as a decision-ready item for Ram.
     Never auto-resolved by a generating session, regardless of how mechanical
     the fix looks. Cleared only when Ram confirms a fix landed (re-checked via
     the ledger's VERIFIED-STILL-OPEN mechanism the next session) or explicitly
     declines it. Surfaced verbatim in the Session Start block (Phase 1 Step 2.5)
     and the Session Close Summary every session until resolved. -->

*(None pending. CG-02 was approved and applied 2026-07-07 — see Open Findings Ledger above. This table is empty by default; it fills only when a new CORPUS_GAP finding surfaces.)*

## Session Reflections

### Session 1 — 2026-07-06
- **What worked:** Parallel per-block authoring (one agent per scenario, disjoint KD ranges + domain quotas assigned up front) produced an exact exam-level domain total (16/11/12/12/9) with no rebalancing. Automated Jaccard dedup + structural validation caught 4 near-clones the block authors' own self-checks missed — the QA gate is load-bearing, keep it.
- **What to do differently next session:** Give block authors the specific practice-test stems for their scenario AND an explicit "different failure mode, not just different wording" instruction, to reduce the near-clone rate before the QA gate.
- **Corpus gap noticed:** No Key Distinction covers built-in tool selection (§2.9), even though Developer Productivity is a first-class scenario. Flagged to Ram; a background task to add built-in-tool KDs was started separately.
- **Blueprint ambiguity:** None blocking.
- **Recommended next action:** Rotate to the two unused scenarios (Code Generation, Multi-Agent Research); have Ram attempt Exam 2 and paste results.

### Session 2 — 2026-07-07 (Exam 3 — first standalone run of orchestration v6)
- **What worked:** This was the first time the full 5-phase orchestration prompt was handed to a genuinely fresh agent (no session history) and asked to execute it as `/cca-exam` would. It correctly parsed Phase 1's branch logic (recognized Branch B — prior SESSION-STATE.md closed cleanly — and correctly reasoned that exams_scored=0 doesn't trigger the Phase 3 insight round), correctly resolved the routing/format gates it was given in advance, and independently chose to delegate the 60-question authoring load across 4 parallel sub-agents — the same architecture a human orchestrator used for Exam 2, converged on with zero awareness that Exam 2 was built that way. That convergence is a good signal the orchestration prompt specifies the work clearly enough to drive consistent engineering decisions regardless of who (or what) is executing it. Content quality was excellent: every block ran its own dedup pass against both ledgers, several self-caught and rewrote near-clones against the corpus's own canonical examples before submitting, and cross-block name-collision checking was attempted (with mixed success — see below).
- **What broke and had to be fixed by the coordinating session, not the delegated agent:**
  1. **Nested background-agent coordination has a real gap.** The dispatched agent, after spawning its own 4 child sub-agents in the background, stopped its own turn twice reporting "waiting for children, nothing further I can do" — burning roughly 250K tokens each time on what was effectively a no-op status report. Its own children's individual completions surfaced to the coordinating session as ordinary task-notifications, but the *parent* agent was never automatically woken by them; each stall required an explicit external resume message. If `/cca-exam` is ever invoked by Ram directly in an interactive session, and it independently chooses this same delegation strategy, this is a real risk of the session appearing to hang.
  2. **One block skipped a required self-check.** Block D validated schema, dedup, and domain quota meticulously but never checked its own correct-answer position distribution — it shipped all 15 questions with the correct option at index A, an exploitable pattern the other two blocks that self-reported this check would have caught. Found only by the coordinating session's post-hoc aggregate check, not by any single block's own QA.
  3. **My own first dedup verification pass had a bug.** A first attempt at independently re-checking all 60 new stems against EXAM-LOG.md used a regex that only matched Exam 2's `[D#]`-tagged stem format and silently missed Exam 1's 30 untagged stems, meaning a genuine near-duplicate against Exam 1 could have slipped through undetected. Caught by noticing the extracted-stem count (60) didn't match the expected total (90) before trusting the "zero overlaps" result. Corrected extraction re-confirmed zero overlaps against the full 166-stem universe (90 ledger + 76 practice-test).
  4. **A peer sub-agent tried and failed to reach its sibling agents for a cross-block name check** ("the peer session isn't directly addressable by that generic name") — two different block authors hit this independently. Cross-block collision checking currently depends on the coordinating session doing it after the fact (which happened here, and found zero collisions), not on the delegated agents doing it themselves.
- **What to do differently next session:** (1) If delegating to parallel sub-agents, the coordinating session should proactively watch for and resume a stalled parent rather than waiting for an automatic wake that may not come — or write the block outputs to a shared, coordinator-monitored location so the coordinator can proceed even if the parent stalls. (2) Make "report your own correct-answer position distribution" an explicit, required line item in every block author's task, not an assumed-standard practice. (3) Re-run the section-freshness tally from ground-truth citations (as done this session) rather than from prose self-reports — it's more reliable and was straightforward to script.
- **Corpus gap noticed:** Same as Session 1 (built-in-tool Key Distinctions) — still open as of this session; a background task to add them was started by Ram separately and had not yet landed at the time Exam 3 was generated.
- **Blueprint ambiguity:** None blocking. The scenario-rotation and confirmed-weakness rules both applied cleanly (no confirmed weakness existed yet, so Phase 4c's adjustment correctly did not fire).
- **Recommended next action before Exam 4:** (1) Have Ram actually take Mock Test 2 or Mock Test 3 and paste the results JSON — this closes the feedback loop for the first time and populates every "unknown" Learner Signal cell above. (2) Once the built-in-tool KD task lands, fold KD#6, #12, #18, #19, #21, #23, #25 (the 7 still fully untouched, non-built-in-tool KDs) into Exam 4's seeding pool ahead of any KD reuse. (3) Consider whether `/cca-exam` needs an explicit instruction to avoid nested nested-agent delegation, or whether the delegation pattern should simply be documented as expected behavior with a coordinator-side stall-detection step built into the Phase 4 instructions themselves.
