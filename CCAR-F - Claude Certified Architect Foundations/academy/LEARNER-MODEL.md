# CCA-F Academy — Learner Model

**This is the Professor's persistent memory of Ram across the whole program.**
Read it at the **start** of every session. Update it at **every comprehension check** and at **sign-off**.

It answers, at any moment:
- Where is Ram **weak**? (🔴 in the Mastery Ledger)
- Where is he **strong**? (🟢 / ✅ in the Mastery Ledger + the Strengths list)
- What needs **reinforcement now**? (the Reinforcement Queue)
- Which concepts are **interlinked**? (the Interlink Map — use these to bridge new teaching)
- What durable **insights** about how he learns can improve later sessions? (the Insight Log)

> **Audience:** AI system only (non-human-facing working memory). Mechanics — the mastery state machine and review intervals — are defined in `ENGAGEMENT-PROTOCOL.md → Cross-Session Memory`.
> **Honesty rule:** synthetic / self-driven runs (see `GAPS.md`) do **NOT** count toward mastery. A concept only leaves ⚪ Untested after a genuine, learner-produced answer.

---

## Legend

| State | Meaning | How it is reached |
|---|---|---|
| ⚪ Untested | Never genuinely assessed | Default / only synthetic data exists |
| 🔴 Weak | Missed on the most recent check | Any state drops to 🔴 on a miss (even a prior 🟢) |
| 🟡 Developing | Right idea but needed prompting, OR 1 clean recall | — |
| 🟢 Strong | 2 clean unprompted recalls on **different** sessions | Spacing required |
| ✅ Exam-ready | 3 clean recalls across ≥2 sessions | Retires from active queue; final-week sweep only |

**Review intervals → "Next review due":** 🔴 next session · 🟡 in 1–2 sessions · 🟢 in ~3 sessions / ~1 week · ✅ final-week sweep.

---

## 1. Mastery Ledger

*Status at program start: all ⚪ Untested. The 2026-06-06 "synthetic batch run" in `GAPS.md` is excluded by the honesty rule.*

### Domain 1 — Agentic Architecture & Orchestration (27%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D1.1 | Agentic loop fundamentals (`stop_reason`, stateless model) | 🟡 | 2026-07-10 | Session 36 | S24 regression → 🔴. S30 cleared → 🟡. S34 Q5 ✗ (chose "content blocks" over stop_reason) — CORRECTED lineage: this miss should have dropped state to 🔴 per the mastery rule (any miss drops even a prior 🟢/🟡ˇ— no trap-resistance exception), which the S34 write-up failed to apply. S35 warm-up Q1 ✅ confident: correctly named stop_reason as the authoritative signal, content blocks as derived/redundant — 🔴→🟡 (one clean recall). One more clean recall in a later session for 🟢. |
| D1.2 | `AgentDefinition` + least privilege | 🔴 | 2026-07-11 | Session 36 | First genuine test: S35 Mock 4 Q34 ✗ (subagent must explore freely but never modify a file, even if prompted to). Chose a system-prompt instruction or full-catalog-with-description reliance instead of `AgentDefinition.allowed_tools` scoped to Read/Grep/Glob. Rule: least privilege is enforced by the tool whitelist, not by prompt wording — a prompt instruction is probabilistic, `allowed_tools` is structural. |
| D1.3 | Hub-and-spoke / coordinator responsibilities | 🟢 | 2026-06-30 | Session 12-13 | 2nd clean recall S7: context isolation, clean context window vocab. Next review ~S12. |
| D1.4 | `Task` tool + explicit context passing + parallel spawn | 🟢 | 2026-06-30 | Session 12-13 | 2nd clean recall S7: 5 explicit context elements named correctly + failure consequences. Next review ~S12. |
| D1.5 | Hooks (Pre/PostToolUse; deterministic vs probabilistic) ★ | 🟢 | 2026-06-30 | Session 12-13 | 2nd clean recall S7: deterministic vs probabilistic unprompted; financial/legal rule correct. Next review ~S12. |
| D1.6 | Escalation patterns + structured handoff ★ | 🔴 | 2026-07-11 | Session 36 | S9: payload incomplete. S22 SR flash ✅ + S33 MCQ1+2 ✅ → 🟢. S35 Mock 4 Q14 ✗: 42-order bulk refund, high-stakes ambiguity with nothing explicitly prohibiting it — chose to proceed or over-clarify instead of escalating. MISS drops 🟢→🔴 per the honesty rule (this session's own correction precedent applies here too: prior evidence was on handoff PAYLOAD structure; this miss is on the TRIGGER condition — same named sub-domain, different facet, still counts). Rule: "not explicitly forbidden" ≠ safe to act autonomously when scale/ambiguity risk is high. |
| D1.7 | Session mgmt (`--resume`, `fork_session`) ★ | 🟡 | 2026-06-30 | Session 10 | First clean check S8: resume/fork/fresh decision rules correct; self-extended concept (each fork independently subject to resume-vs-fresh decision). |
| D1.8 | Task decomposition (fixed vs dynamic; multi-pass) | 🔴 | 2026-07-11 | Session 36 | First check S8/S9. S17 SR flash: "attention dilution" produced cold — first clean production, 🟡. S35 Mock 4 Q39 ✗: 3 subagents all report success but combined map misses 2 of 4 subtopics — chose a tooling/interference explanation instead of "the coordinator's own decomposition never assigned those subtopics." Rule: when subagents all succeed but coverage is wrong, the root cause is the coordinator's task list, not subagent execution. |

### Domain 3 — Claude Code Configuration & Workflows (20%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D3.1 | CLAUDE.md hierarchy + `@path` imports | 🔴 | 2026-07-11 | Session 36 | First clean recall S10. MCQ1 S15 miss → recovered S33 MCQ4 (directory-scoped path rules) → 🟡. S35 Mock 4: TWO independent misses in one sitting. Q22 ✗: `@import` max nesting depth is 5 — chose a fabricated rule (same-directory-only, root-imports-only, absolute-path-only) instead. Q46 ✗: root + subdirectory CLAUDE.md both concatenate into context, neither overrides the other — chose "subdirectory silently replaces root" (the exact misconception the question was designed to catch). Two mechanical facts of the same feature both missed — needs direct re-teaching, not just a flash review. |
| D3.2 | Path-specific rules (`.claude/rules/`, glob `paths:`) | 🟡 | 2026-07-04 | Session 16 | Needed direct teaching before recall. MCQ 4 S15 MISS: chose "all .ts files project-wide" — confused paths: as a project-scope filter rather than file-being-edited trigger. Conditional loading mechanism needs reinforcement. |
| D3.3 | Skills frontmatter (`context:fork`, `allowed-tools`, `argument-hint`) ★ | 🔴 | 2026-07-11 | Session 36 | allowed-tools pre-approve trap nailed cold MCQ3 S15. context:fork correct in teaching. S35 Mock 4 Q35 ✗: a `/trace-dependents` skill's large catalog output pollutes the main session, causing the agent to keep proposing edits to merely-catalogued modules — chose scope-reduction or a smaller model instead of `context: fork` to isolate the skill's output in a subagent context. The exact mechanism taught in S12 wasn't retrieved under a fresh application scenario. |
| D3.4 | Planning mode vs direct + Explore subagent | 🟡 | 2026-07-04 | Session 18 | Planning mode strong; explore subagent needed prompting (had to link back to context:fork). |
| D3.5 | `/compact` and `/memory` | ⚪ | — | — | Taught as quick facts S13, not drilled. Will surface in integration. |
| D3.6 | CI/CD: `-p` / `--bare` / `--output-format json` ★ | 🟡 | 2026-07-04 | Session 18 | --bare correctly identified in MCQ 2 S15 and S14 drill. Context isolation solid. Session context isolation: correct but vocabulary "probabilistic" not used unprompted. |

### Domain 4 — Prompt Engineering & Structured Output (20%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D4.1 | Few-shot prompting (5 types) | 🟡 | 2026-07-04 | Session 17 | S16: correctly identified boundary type as fix for inconsistency (unprompted — good). Vocabulary gaps: said "training" (not "few-shot examples") and "post criteria" (not "positive criteria"). Mechanism clear; exam vocabulary needs one more session. |
| D4.2 | Explicit criteria vs vague instructions | 🟡 | 2026-07-10 | Session 36 | S22 SR flash Q2 ✅ — first clean cold recall. S34 Q6 ✗ (chose A, few-shot) — CORRECTED lineage: this miss should have dropped state to 🔴, which the S34 write-up failed to apply. S35 warm-up Q2 ✅ confident: correctly distinguished explicit-criteria (rule statable → state it directly) from few-shot (rule hard to articulate → demonstrate it) — 🔴→🟡 (one clean recall). One more clean recall in a later session for 🟢. |
| D4.3 | Prompt chaining (attention dilution) | 🟡 | 2026-07-05 | Session 20 | S16: mechanism solid after teaching; "attention dilution" not produced unprompted. S17 SR flash: produced exact term cold. Mechanism strong; one more unprompted production needed for 🟢. |
| D4.4 | The "interview" pattern | 🟡 | 2026-07-05 | Session 22 | S20 first teaching. Q3 ✅ — correctly identified genuine ambiguity ("notification system" = multiple valid approaches) as the interview pattern trigger. Distinguishes from over-asking. |
| D4.5 | `tool_use` + JSON Schema (syntactic vs semantic) | ✅ | 2026-07-09 | Final-week sweep | S21 Q4 ✗. S22 SR flash ✅ (1st clean). S32 MCQ2 ✅ (2nd clean → 🟢). S33 MCQ5 ✅ (3rd clean, 3rd session) → ✅ exam-ready. Rule: enum=one value constrained; array=multiple concurrent values. |
| D4.6 | `tool_choice` (auto / any / forced) | 🔴 | 2026-07-11 | Session 36 | S17 first teaching: auto/any/specific-tool modes taught, never drilled standalone. First genuine test: S35 Mock 4 Q19 ✗ — an agent occasionally replies in prose instead of calling `apply_fix`; the fix is `tool_choice:{"type":"any"}` forcing a tool call. Chose a system-prompt instruction (still permits text under the default `auto` mode) instead. |
| D4.7 | Syntax vs semantic errors | 🔴 | 2026-07-11 | Session 36 | S17: syntactic vs semantic distinction confirmed in Q3 — first clean production, 🟡. S35 Mock 4 Q51 ✗: `--json-schema` output passes validation 100% of the time, yet 6% of severity labels are wrong under the team's own rubric — chose "tighten the schema further" instead of recognizing schema validation only catches syntax, never semantic/business-rule correctness. Same distinction, different application — didn't transfer to a fresh scenario. |
| D4.8 | Validation, retry-with-feedback, self-correction ★ | 🟢 | 2026-07-09 | Session 35 | S18: Q1 ✗ (Type 2 gate missed). S21 Q1 ✅ cold: Type 2 identified, enriched input (first clean). S32 MCQ5 ✅: Type 2 — enrich subagent input with page content, not blind retry (second clean, different session) → 🟢. |
| D4.9 | Message Batches API ★ | 🟢 | 2026-07-09 | Session 36 | S19 3/3 strong first recall. S33 MCQ6 ✅ — 8-hour window = batch eligible (< 24h), no multi-turn loops, 50% saving applies. Second clean different session → 🟢. |
| D4.10 | Multi-instance / multi-pass review ★ | 🟡 | 2026-07-05 | Session 22 | S20 first teaching. Q1 ✅ (reasoning-context bias — structural, not capability failure). Q2 ✅ (parallel per-unit + sequential integration pass). Strong first recall. |

### Domain 2 — Tool Design & MCP Integration (18%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D2.1 | Tool description as the selection mechanism ★ | 🟡 | 2026-07-10 | Session 35 | S22: 3/3 first clean. S33 MCQ3 ✗: lazy-loading misconception resurfaced under compound pressure. S34 Q1 ✅: correctly identified B (always-present) — 2nd clean in isolation post-regression. Needs mock confirmation before promotion. Lock-in phrase: "Always-present = always influencing." |
| D2.2 | MCP fundamentals (tools / resources / prompts) | 🟡 | 2026-07-10 | Session 35 | S23 Q1 ✗ vocab. S24 SR flash miss x2. S26 ✅ resources recovered. S30 SR flash ✅ vocab (first clean). S34 Q3 ✅ vocab (Do/Read/Reuse mnemonic held) + S34 Q4 ✅ resources≠auto-discovery — both sub-topics clean same session. One more clean session for 🟢 on each. Watch for both in mock. |
| D2.3 | MCP server config (.mcp.json vs ~/.claude.json) | 🟡 | 2026-07-07 | Session 26 | S23 Q2 ✅ — correctly identified env var substitution pattern: .mcp.json holds server config (team-shared, VCS), ${GITHUB_TOKEN} substituted from each developer's local env. Project scope = shared; credential = personal. First clean check. |
| D2.4 | `isError` structured errors (+ JSON-RPC vs tool-exec channel) ★ | 🔴 | 2026-07-11 | Session 36 | S24 3/3 comprehension. S26 drill Q2 ✅ — first clean session, 🟡. S35 Mock 4 Q52 ✗: `post_finding` fails two ways — a permission error (never succeeds, any retry count) and a network timeout (succeeds on retry) — both returning an identical generic error, both retried 3x. Correct fix categorizes the permission failure as non-retryable with a named missing scope, and the timeout as transient/retryable. Chose uniform backoff or letting the coordinator guess from error text instead of structured categorization. This is the exact error-category rule taught (transient→retry, permission→escalate) not applied under a fresh two-failure-type scenario. |
| D2.5 | Tool allocation + `tool_choice` (too-many-tools problem) ★ | 🟡 | 2026-07-10 | Session 35 | S24 3/3, S26 ✅. S33 MCQ3 ✗ (chose lazy-loading instead of decompose). S34 Q2 ✅: correctly identified A (domain-scoped subagents, 4–5 tools each) — clean recall post-miss. Distinction clear: content-index patch (B) adds tokens, not clarity; tool merging (D) trades one problem for another. One more for 🟢. |
| D2.7 | Tool description scope/boundary clarity (state what it covers AND excludes, incl. natural-language phrasing, not just ID-type disambiguation) ★ NEW | 🟡 | 2026-07-11 | Session 37 | Discovered as a gap: S35 Mock 4 Q8 ✗ + Q47 ✗ (two independent misses, same corpus section, different scenarios). First taught S36: produced a concrete two-tool disambiguation (order ID vs. customer ID) unprompted after one Socratic follow-up — first clean recall, 🟡. Refinement flagged: cover natural-language intent phrasing too, not just structured-ID cases. One more clean recall, later session, for 🟢. Corpus: Domain-2_v2 §2.2; Key-Distinctions #10. |
| D2.6 | Built-in tool selection + incremental investigation | 🔴 | 2026-07-11 | Session 36 | S25 Q1 ✗ Glob-vs-Grep → S26 Q4 ✅ → S35 warm-up Q3 ✅ (2nd clean, separate session) → promoted to 🟢. PROMOTION WAS TOO NARROW: within the SAME sitting, S35 Mock 4 Q32 ✗ — `Edit`'s anchor `return response` matches 19 locations and fails; engineer suggests shortening the anchor to `return` to be "more specific." Correct fallback is Read the full file, modify programmatically, then Write it back. Chose the shortened-anchor trap (a shorter, more generic anchor is MORE likely non-unique, not less) or a Bash/sed bypass. All 3 evidenced clean recalls (S25/S26/S35-warmup) were specifically Glob-vs-Grep; this miss is a different built-in-tool fact (Edit-anchor-uniqueness) within the same named sub-domain — the 🟢 covered one facet, not the whole sub-domain. Matches the 2026-07-09 insight: corrected concepts regress under compound/fresh-scenario pressure. |

### Domain 5 — Context Management & Reliability (15%)
| Sub-domain | Concept | Mastery | Last checked | Next review due | Evidence / note |
|---|---|---|---|---|---|
| D5.1 | Context window risks (lost-in-the-middle, accumulation) | 🟢 | 2026-07-09 | Session 33 | S27 Q1 ✅ mechanism. S27 Q2 ✗ mitigation miss (placed in middle). S28 Q3 ✅ mitigation cleared (first clean recall). S30 SR flash ✅ mitigation: key findings TOP, action items BOTTOM — second clean separate-session recall → 🟢. |
| D5.2 | Fact extraction + tool-result trimming + position-aware input | ✅ | 2026-07-09 | Final-week sweep | S27 Q3 ✅ (1st clean). S28 Q1 ✅ (2nd clean → 🟢). S33 MCQ7 ✅ — persistent fact block preserves exact numbers across progressive summarization (3rd clean, 3rd session) → ✅ exam-ready. |
| D5.3 | Scratchpad files + structured state persistence ★ | 🟢 | 2026-07-09 | Session 34 | S29 Q1 ✅ scratchpad (first clean). S31 Q1 ✅ + MCQ1 ✅ (second clean session). Two sessions clean → 🟢. Note: S29 Q2 miss on subagent-output-scope ("never return" vs "return structured summary") was not explicitly re-tested in S31; watch for this in integration scenarios. |
| D5.4 | Confidence calibration + stratified sampling ★ | 🟢 | 2026-07-09 | Session 34 | S30 first teaching (Q1/Q2 ✅). S31 comprehension Q2 ✅ + scenario MCQ4 ✅ (second clean session). Two separate sessions clean → 🟢. Key phrase: "stratified random sampling across document types." |
| D5.5 | Provenance preservation + conflicting data ★ | ✅ | 2026-07-09 | Final-week sweep | S30 ✅ (1st clean). S31 ✅ (2nd clean → 🟢). S33 MCQ8 ✅ — claim→source pairs as structured data survive every layer; free-text breaks the chain (3rd clean, 3rd session) → ✅ exam-ready. |

### Mock-Surfaced Gaps — not yet in the tracked ledger (from S35 Mock 4, 2026-07-11)

*Four misses tested real, high-yield facts that don't cleanly map to an existing D-numbered cell. Flagged here rather than force-fitted, so Session 36 covers them explicitly. Consider promoting each to a formal ledger row if a future mock retests the same fact.*

| Concept | Domain | Evidence | Rule |
|---|---|---|---|
| Two-tool token-binding pattern (preview/execute split with a single-use token) | D2 | Mock 4 Q2 ✗ — chose a `dry_run:boolean` variant, a system-prompt sequencing rule, or a post-hoc logging hook instead of the two-tool split. | A single tool with a boolean the model sets itself is never architecturally guaranteed; splitting into `preview_X` (returns a token) + `execute_X` (requires that token) makes skipping the precondition structurally impossible. Corpus: Domain-2_v2 §2.4; Key-Distinctions #11/#12. |
| ~~Tool description must state scope/boundary~~ — PROMOTED to D2.7 below | — | — | — |
| Partial subagent failure → coverage-annotated synthesis (not error-out, not silent-omit) | D1 (related to D1.3, distinct fact from context-isolation evidence) | Mock 4 Q17 ✗ — 2 of 8 files unparseable, other subagents complete fully; chose to fail the whole report or omit mention of the gap. | Synthesize with what's available; explicitly annotate which conclusions are well-supported vs. where a real gap exists. Don't block the whole report on partial failure, and don't hide the gap either. Corpus: Domain-1_v2 §1.10. |
| Stated-assumptions technique for ambiguous automated requests (distinct from the interview-pattern trigger in D4.4) | D4 (related to D4.4) | Mock 4 Q54 ✗ — "/review focus on the risky parts" with "risky" undefined; chose to block and ask, or to silently guess without saying so. | When blocking to ask would stall an automated pipeline, proceed with a stated, reasonable assumption and say so explicitly in the output so it can be corrected — don't block, and don't guess silently either. Corpus: Domain-4_v2 §4.19; Key-Distinctions #19. |

---

## 2. Reinforcement Queue (spaced repetition — read at session start)

> The Spaced-Repetition Flash and any gap-fill drills are drawn from the TOP of this queue.
> Rule: list everything whose **Next review due ≤ the upcoming session**, sorted weakest-first (🔴 → 🟡 → 🟢).

| Priority | Concept | State | Due | Why it's queued |
|---|---|---|---|---|
| 1 | D2.4 — Retryable (transient) vs non-retryable (permission) error categorization | 🔴 | Session 36 | S35 Mock 4 Q52 ✗ — PRIORITY, D2 is the confirmed-weak domain (45%). |
| 2 | D2.6 — Edit anchor uniqueness: shorter anchor ≠ more specific; Read+Write fallback | 🔴 | Session 36 | S35 Mock 4 Q32 ✗ — premature 🟢 promotion same session, corrected. PRIORITY. |
| 3 | D1.2 — `AgentDefinition.allowed_tools` as structural least-privilege enforcement | 🔴 | Session 36 | S35 Mock 4 Q34 ✗ — first genuine test, missed cold. PRIORITY. |
| 4 | D1.6 — Escalation trigger: high-stakes ambiguity even absent explicit prohibition | 🔴 | Session 36 | S35 Mock 4 Q14 ✗ — regressed from 🟢. PRIORITY. |
| 5 | D1.8 — Decomposition-gap diagnosis: coordinator's task list, not subagent execution | 🔴 | Session 36 | S35 Mock 4 Q39 ✗. |
| 6 | D3.1 — `@import` nesting depth (5) + multi-level concatenation, no override | 🔴 | Session 36 | S35 Mock 4 Q22 ✗ AND Q46 ✗ — two independent misses same sitting. |
| 7 | D3.3 — `context: fork` to isolate a skill's large/exploratory output | 🔴 | Session 36 | S35 Mock 4 Q35 ✗ — taught cleanly at S12, not retrieved under fresh scenario. |
| 8 | D4.6 — `tool_choice:{"type":"any"}` forces a tool call over prose | 🔴 | Session 36 | S35 Mock 4 Q19 ✗ — first genuine drill, missed cold. |
| 9 | D4.7 — Schema validation catches syntax only, never semantic/business-rule correctness | 🔴 | Session 36 | S35 Mock 4 Q51 ✗ — regressed from 🟡 first-clean. |
| 10 | NEW — Two-tool token-binding pattern (D2) | 🔴 | Session 36 | S35 Mock 4 Q2 ✗ — see Mock-Surfaced Gaps table above. |
| 11 | NEW — Tool description scope/boundary clarity (D2, related to D2.1) | 🔴 | Session 36 | S35 Mock 4 Q8 ✗ + Q47 ✗ (two independent misses) — see Mock-Surfaced Gaps table. |
| 12 | NEW — Partial-failure synthesis with coverage annotation (D1, related to D1.3) | 🔴 | Session 36 | S35 Mock 4 Q17 ✗ — see Mock-Surfaced Gaps table. |
| 13 | NEW — Stated-assumptions technique for ambiguous automated requests (D4, related to D4.4) | 🔴 | Session 36 | S35 Mock 4 Q54 ✗ — see Mock-Surfaced Gaps table. |
| 14 | D1.1 — stop_reason: primary signal; content blocks derived/secondary | 🟡 | Session 37 | S35 warm-up ✅ confident → 🟡. Held clean through the mock (not retested — no stop_reason item missed). One more clean, later-session recall for 🟢. |
| 15 | D4.2 — Explicit criteria vs few-shot: state the rule when it's statable | 🟡 | Session 37 | S35 warm-up ✅ confident → 🟡. Held clean through the mock. One more clean, later-session recall for 🟢. |
| 16 | D2.2 — Tools/Resources/Prompts official vocabulary | 🟡 | Session 37 | S34 Q3 ✅ (Do/Read/Reuse held), not retested in mock. One more for 🟢. |
| 17 | D2.2 — Resources ≠ auto-discovery | 🟡 | Session 37 | S34 Q4 ✅, not retested in mock. One more clean recall for 🟢. |
| 18 | D2.1 — Tool descriptions always-present, NOT lazy-loaded | 🟡 | Session 37 | S34 Q1 ✅, not retested in mock (Q8/Q47 tested a related but distinct fact — see Mock-Surfaced Gaps). One more for 🟢. |
| 19 | D2.5 — Too-many-tools fix: domain-scoped subagents (4–5 tools each) | 🟡 | Session 37 | S34 Q2 ✅, not retested in mock. One more for 🟢. |
| 20 | D4.3 — Prompt chaining: "attention dilution" exact term | 🟡 | Session 37 | S17 first cold production, not retested in mock. One more for 🟢. |
| 21 | D4.10 — Multi-instance: no generation context → structural finding | 🟡 | Session 37 | S20+S32 solid, not retested in mock. One more for 🟢. |
| 22 | D4.4 — Interview pattern: genuine ambiguity trigger only | 🟡 | Session 37 | S20+S32 solid. Q54 tested the related-but-distinct stated-assumptions fact instead — see Mock-Surfaced Gaps. One more for 🟢. |
| 23 | D2.3 — MCP server config (.mcp.json vs ~/.claude.json) | 🟡 | Session 37 | S23+S26 clean, not retested in mock. One more for 🟢. |
| 24 | D3.2 — paths: conditional loading (file-being-edited trigger) | 🟡 | Session 37 | S33 MCQ4 ✅ first clean post-miss, not retested in mock (Q22/Q46 tested D3.1, not D3.2). One more for 🟢. |
| 25 | D4.8 — Type 1/2 failure gate ★ | 🟢 | Session 36 | S21+S32 two clean, not retested in mock. Sweep before Mock #2. |
| 26 | D4.9 — Message Batches API: 24h window, no multi-turn, custom_id | 🟢 | Session 36 | S19+S33 two clean, not retested in mock. Sweep before Mock #2. |
| 27 | D5.1 / D5.3 / D5.4 — all 🟢 | 🟢 | Session 39 | D5 scored 9/9 (100%) in the mock — no action, final-week sweep only. |
| 28 | D4.5 — enum=one value; array=multiple coexisting | ✅ | Final-week | ✅ exam-ready, not retested in mock (consistent — no D4.5-shaped item appeared). |
| 29 | D5.2 — PostToolUse trimming + persistent fact block | ✅ | Final-week | ✅ exam-ready. |
| 30 | D5.5 — Provenance: claim+source survive every layer as structured data | ✅ | Final-week | ✅ exam-ready. |

---

## 3. Strengths (anchor new teaching to these)

> Concepts Ram reliably nails (🟢 / ✅). Use them as the *known* side of a new analogy — bridge from a strength to a new concept.

- D1.3 — Context isolation / clean context window (🟡 — 1 clean recall S5; 1 more needed)
- D1.4 — Task tool + parallel spawn (🟡 — first check solid)
- D1.5 — Hooks: deterministic vs probabilistic (🟡 — first check solid; key distinction clear)

---

## 4. Concept Interlink Map

> When teaching a new concept, link it to a strong prior one — this is exactly what the exam's cross-domain scenarios test. Add a row whenever a genuine connection surfaces in a session.

| Concept A | ↔ | Concept B | The bridge to say out loud |
|---|---|---|---|
| Hooks — `PreToolUse` (D1.5) | ↔ | Escalation (D1.6) | "A PreToolUse hook that blocks a >$500 refund and an escalation are the two halves of the same decision: stop the unsafe action, hand it to a human." |
| Hooks — `PostToolUse` (D1.5) | ↔ | Tool-result trimming (D5.2) | "Trimming a 40-field order down to 5 is a context technique (D5) *implemented* with a D1 mechanism — same hook, different goal." |
| Determinism: hooks + preconditions (D1.5) | ↔ | Structured Outputs / `tool_use` (D4.5) | "Guarantee at the source, not by asking nicely — hooks for actions, schemas for output. Prompts are probabilistic; both of these are deterministic." |
| Tool descriptions (D2.1) | ↔ | Tool selection reliability + system-prompt associations (D1/D2.5) | "The description is how the model picks; the system prompt can quietly bias that pick. Same failure (wrong tool), two root causes." |
| Coordinator context isolation (D1.3/D1.4) | ↔ | Scratchpad + state persistence (D5.3) | "Subagents don't inherit history, so you pass context explicitly — and a scratchpad is how the coordinator remembers across that boundary." |
| Batch API (D4.9) | ↔ | CI/CD sync-vs-batch (D3.6) + no multi-turn tool calling (D2) | "Batch = 50% off but up to 24h and no mid-request tool loop → great for overnight audits, fatal for a blocking pre-merge check." |
| Lost-in-the-middle (D5.1) | ↔ | Position-aware multi-agent synthesis (D1.3) | "Key findings go at the TOP of the aggregated input — the same lost-in-the-middle rule that bites a single prompt bites the synthesis agent." |
| `isError` structured errors (D2.4) | ↔ | Error propagation to coordinator (D1/D5.3) | "A good `isError` payload (type, retryable, partial results) is what lets the coordinator decide retry vs escalate vs continue-with-gaps." |

---

## 5. Cross-Session Insight Log

> Durable observations about HOW Ram learns — which analogy domains land, recurring confusions, pacing, and where his real Infosys/solution-architect experience can be used as an anchor. Each entry: date · observation · how to apply it next time.

- **2026-06-27 — Systems-first thinker.** Ram's D1 answers described architecture (what talks to what, who persists, who is responsible) before mechanics. He'll absorb "why does this design exist" before "what is the syntax." Lead with design intent, not API detail.
- **2026-06-27 — Self-generated analogies.** He independently reached the USB analogy for MCP — the canonical one. When he reaches for an analogy himself, affirm it and build on it rather than replacing it.
- **2026-06-27 — Clear metacognition on gaps.** Said "I do not know" directly for headless and prompt caching rather than guessing. Trustworthy signal — his 🟡s are genuine partial knowledge, not bluffing.
- **2026-06-27 — Gap pattern: conceptual vs. technical.** Consistently strong on the "what it is and why" layer; consistently missing the "how the API actually signals it" layer (stop_reason, tool_use content blocks, cache_control fields). Bridge from his concept to the API shape. **UPDATE (S2–S4):** Technical layer is absorbing quickly once taught — stop_reason retained cleanly across two sessions same day. Gap pattern may narrow faster than expected.
- **2026-06-27 — Responds well to "what breaks if..."** His best answers came from failure-mode questions (stateless context drop, Analyst with no facts). Use this pattern: teach the mechanism, then ask what breaks if it's missing. He reasons from consequences, not from definitions.
- **Known context to leverage:** Ram is a Solution Architect at Infosys (Claude Partner) with hands-on agent/Claude Code experience. Prefer enterprise-delivery and systems-architecture analogies over consumer ones; he can reason from real production trade-offs.
- **2026-06-30 — Precision gap under exam pressure.** In MCQ format with multiple plausible answers, Ram picks directionally correct options that lack the precise exam term (e.g. "too much context" instead of "attention dilution"; text-content check as valid instead of anti-pattern). Teach the exact vocabulary each session. In MCQ format: when two answers look similar, the exam rewards the one with the precise named concept.
- **2026-06-30 — Dangerous misconception pattern on D1.1.** Anti-pattern 3 (text-content check as completion signal) was not only forgotten but actively selected as the CORRECT answer in a scenario. This is a belief-level error, not a recall error. Re-exposure alone won't fix it — must explicitly contrast: "this sounds reasonable but is exactly the anti-pattern." Use the contrast frame.
- **2026-07-04 — D1.1 belief-level error resolved; precision gap remains.** S10 SR flash: correctly rejected text-content anti-pattern. Progress is real. New gap: API signal vocabulary ("end tool use" instead of "end_turn"). Drill with contrast MCQ — offer both `"tool_use"` and `"end_turn"` as options so the correct one gets locked in precisely.
- **2026-07-04 — MCQ pressure reveals reflex over-application.** In teaching, Ram demonstrates correct reasoning. Under MCQ conditions, he applies the most recently reinforced rule broadly even when the scenario requires distinguishing it (e.g., "project level = correct for teams" → applied to a personal rule question). Needs explicit "same concept, different scope" contrast MCQs to break the reflex. This is a pattern to watch in D4 and D2 drills.
- **2026-07-04 — Vocabulary compression under self-expression.** Ram understands mechanisms correctly but compresses exam vocabulary when answering in his own words: "training" for few-shot prompting, "post criteria" for positive criteria, "loss in the attention" for attention dilution. The concept lands; the precise term does not transfer automatically. Strategy: after teaching a named concept, ask him to use the exact term in a sentence before advancing. One production repetition per session locks it faster than multiple MCQ exposures.
- **2026-07-11 — Mock 4: total score overstates readiness; the domain floor caught what the total hid.** 45/60 (775 scaled) clears the 720 pass line comfortably, but D2 (Tool Design & MCP) landed at 45% (5/11) — a clear floor breach — and the CI scenario block at 67%. This is the exact warning already written into ENGAGEMENT-PROTOCOL.md's mock spec: a raw-proportion score can overstate readiness because the real exam weights scenario/anti-pattern items more heavily than recall. Confirms the floor gate (not the total alone) is the right Go/No-Go instrument for Ram specifically — a strong total was fully capable of masking a real, confirmed domain gap.
- **2026-07-11 — Fresh-scenario transfer is the dominant failure mode across all 15 misses, not raw unfamiliarity.** Nearly every miss was on a concept taught cleanly and even previously drilled clean (D2.6 Edit-fallback, D3.3 context:fork, D3.1 import depth, D1.6 escalation triggers, D2.4 error categorization) — but re-applied in a scenario shaped differently from its teaching/drill instance. This is the same "corrected concepts regress under compound exam pressure" pattern from 2026-07-09, generalized: it's not just compound (two-concepts-in-one-stem) pressure that causes regression — a single concept in an unfamiliar scenario shape is enough. Implication for Session 36: re-teaching should deliberately vary the scenario surface (different tool names, different narrative) from how each concept was originally taught, not just repeat the original framing.
- **2026-07-11 — A 🟢 promotion earned on one facet of a sub-domain does not cover the whole sub-domain.** D2.6 was promoted to 🟢 in this exact session (S35 warm-up, Glob-vs-Grep, two clean separate-session recalls) and then missed within the same sitting on a different built-in-tool fact (Edit-anchor uniqueness) that happens to share the same ledger cell name ("Built-in tool selection"). The ledger cell's evidence trail is now honest about this: three clean recalls all tested the same narrow fact. Going forward, before crediting a 🟢/✅ on a broadly-named sub-domain, check whether the accumulated evidence spans genuinely different facts within it, not just repeated tests of the same one.
- **2026-07-11 — Timing data from Mock 4 is not clean 120-minute-condition data.** Several questions show implausible elapsed times (Q7: 64 min, Q12: 51 min, Q55: ~8.3 hours) — clear evidence of breaks taken mid-exam that the passive per-question timer counts as think-time. Total reported time (~12.3 hours) is not comparable to the real exam's 120-minute window. This doesn't invalidate the domain/scenario accuracy signal, but the pacing data is unusable, and the mock wasn't taken under single-sitting exam-condition fidelity we set up for Session 35. Recommend Mock #2 (Session 37) be attempted in one continuous sitting, or with breaks explicitly excluded from the timing analysis.
- **2026-07-08 — Mechanism-to-application gap in D5.1.** S27: Ram correctly identified positional bias (Q1 ✅ — middle = low attention). But when asked how to mitigate it, chose placing findings in the middle (Q2 ✗). Knowing what the failure IS did not automatically transfer to knowing the fix. Teaching note: pair mechanism and mitigation rule in the same breath; test both separately. Rule follows directly: low attention in middle → key findings TOP, action items BOTTOM.
- **2026-07-08 — D2.2 vocabulary persistent miss across 3 exposures.** Official MCP names (Tools/Resources/Prompts) not locking under SR pressure after S23 Q1, S24 SR flash x2. Conceptual understanding correct; exam-exact terminology drifting. Try a mnemonic at S28: Do/Read/Reuse = Tools/Resources/Prompts. Ask Ram to produce the names in a sentence before advancing — one production beats three MCQ exposures.
- **2026-07-09 — Corrected misconceptions regress under compound exam pressure.** S33 MCQ3 asked about too-many-tools AND the reason descriptions matter — two D2 concepts in one stem. Ram selected B (lazy-loading) — the original misconception from S22 resurfaced when the stem combined D2.1 + D2.5 instead of testing each in isolation. Implication: a concept corrected in a standalone drill may not hold when embedded in a multi-concept scenario that activates the old mental model. Before mocks, test each corrected misconception in a scenario that could plausibly re-activate the original wrong answer.
- **2026-07-10 — Mastery-rule enforcement gap found and fixed.** The S34 write-up left D1.1 and D4.2 at 🟡 despite fresh misses (Q5, Q6) that session — the mastery state machine is explicit that ANY miss drops a concept straight to 🔴, even a prior 🟢, with no carve-out for "it was a trap-resistance failure, not an ignorance failure." Softening the rule for trap-resistance misses defeats its purpose: those are exactly the misses most likely to recur under real exam pressure, so they most need the reset. Corrected both entries in this session (2026-07-10, S35) before promoting either past the corrected 🔴 baseline. Going forward: apply the miss→🔴 rule mechanically, with zero exceptions, regardless of how sympathetic the wrong answer looks.
- **2026-07-10 — Methodology import from cross-project migration audit.** A comparison of this conversational approach against the sibling HTML mock-exam generator (`prep with quiz/`) found the generator superior on domain-quota discipline, generic scenario framing (no invented names — confirmed via a 76-question audit of real exam text), distractor-archetype naming, and scaled-score reporting. Adopted all four into SESSION-PLAN.md's Session 35 entry, plus a fifth item — confidence capture ("confident or guessing?") — into ENGAGEMENT-PROTOCOL.md's mastery state machine, since it tightens the existing honesty rule (a lucky guess should not read as a clean recall). Not adopted: the generator's misconception-reactivation and belief-tracking recommendations were aimed at making it more like this conversational approach — this side already runs those natively (S34 is a live example) and needs no change.
- **2026-07-10 — Trap-resistance failures are the primary mock risk.** S34 Q5 (D1.1): Ram knows end_turn=STOP/tool_use=CONTINUE, but chose D ("content blocks over stop_reason") — a technically-related distractor that sounds authoritative. S34 Q6 (D4.2): chose few-shot (A) over positive criteria (B) — D4.1 bleed under pressure. Both are trap-resistance failures, not recall failures: the concept is present, but a confident-sounding wrong answer overrides it. Pre-mock protocol: one contrast MCQ per vulnerable concept where the distractor is the plausible-sounding wrong answer, not an obvious foil.
- **2026-07-05 — Solution-state blinds recognition of problem-state in MCQs.** S17 Q1: Ram knew the correct schema fix (nullable type → Rule 2) and selected the answer describing CORRECT behavior, when the question was asking what goes WRONG with the broken schema. He was answering "what does the good design do" instead of "what does the bad design do." Watch for this in D2 and D5: when a question describes a flawed setup, wrong answers will describe what the FIXED version does. Always re-read the question stem to confirm whether it's asking about the broken or fixed state.

---

## 6. Domain Confidence Summary (recompute at each sign-off)

> One-line read of where the program stands per domain. Used for Go/No-Go judgement alongside mock scores.

| Domain | Weight | Concepts ✅/🟢 | Concepts 🟡 | Concepts 🔴 | Untested | Read |
|---|---|---|---|---|---|---|
| D1 | 27% | 2 (D1.3/4/5 🟢, treated as one cluster for count purposes → 1 row shown) | 2 (D1.1/7 🟡) | 3 (D1.2/6/8 🔴) | 0 | Mock 4: 12/16 = 75% ✓ floor. But D1.2 (least-privilege whitelist), D1.6 (escalation trigger, regressed from 🟢), D1.8 (decomposition-gap diagnosis) all missed. D1.3/4/5 not retested, still 🟢. Session 36 priority. |
| D2 | 18% | 0 | 2 (D2.1/2/3/5 🟡, D2.3 untested in mock) | 2 (D2.4/6 🔴) | 0 | Mock 4: 5/11 = 45% ✗ CONFIRMED WEAK, floor breach. D2.4 (error categorization) + D2.6 (Edit-anchor, premature 🟢) both missed. Plus 3 new unranked gaps (token-binding, description-boundary ×2). Weakest domain, top priority Session 36. |
| D3 | 20% | 0 | 2 (D3.2/4 🟡) | 2 (D3.1/3 🔴) | 1 (D3.5) | Mock 4: 9/12 = 75% ✓ floor. D3.1 (import mechanics, 2 independent misses) + D3.3 (context:fork) both missed. D3.6 not retested. /compact+/memory untested. |
| D4 | 20% | 2 (D4.5 ✅; D4.8 🟢; D4.9 🟢) | 4 (D4.1/3/4/10 🟡) | 2 (D4.6/7 🔴) | 0 | Mock 4: 10/12 = 83% ✓ floor. D4.6 (tool_choice:any, first drill) + D4.7 (schema=syntax-only) both missed. D4.5/8/9 not retested, still ✅/🟢. Plus 1 new unranked gap (stated-assumptions). |
| D5 | 15% | 5 (D5.1/3/4 🟢; D5.2/5 ✅) | 0 | 0 | 0 | Mock 4: 9/9 = 100% ✓ floor — perfect domain score, zero misses. D5.2 ✅ + D5.5 ✅ (3 clean each). D5.1/3/4 🟢, none retested but no reason to doubt. Strongest domain by a wide margin — no action needed. |
