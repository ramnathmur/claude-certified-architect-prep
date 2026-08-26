# CCA-F Academy — Session Progress Tracker

**Learner:** Ram
**Program start:** 2026-06-27
**Target exam date:** 2026-08-22 (provisional — reassess after Session 9 drill)

---

> **SUPERSEDED, 2026-08-26 (via `/sync-up`).** This academy track was abandoned mid-program (stopped at
> session 36 of 37) in favor of the `prep with quiz/` mock-exam generator, this project's real source
> of truth. The real exam was sat 2026-08-18 and **PASSED at 851/720** — see
> `../prep with quiz/EXAM-LOG.md`'s closing entry. The "NO-GO, 45/60" status below reflects one early
> mock from this abandoned track, was never the final word, and should not be read as current standing.

## Current Status

```
Current session:  36 (Mock #1 Analysis + Targeted Re-Drill)
Current phase:    7 — Mock Exams
Overall progress: 35 / 37 sessions complete
Active gaps:      D2 domain CONFIRMED WEAK — 5/11 (45%), floor breach. Top priority Session 36.
                  9 concepts regressed to 🔴 from the mock: D1.2, D1.6, D1.8, D2.4, D2.6, D3.1, D3.3, D4.6, D4.7
                  4 new gaps surfaced (not yet ledger cells): two-tool token-binding (D2), tool-description
                  boundary clarity (D2, 2 misses), partial-failure synthesis (D1), stated-assumptions (D4)
                  CI scenario block also breached floor (10/15, 67%) — overlaps significantly with D2 misses
Promotions S35:   None from the mock (15 misses); warm-up promoted D1.1/D4.2 (🔴→🟡) and D2.6 (🟡→🟢,
                  LATER REVERSED same session — see D2.6 note below)
Mock exam score:  Mock #1 (Exam 4): 45/60 correct, estimated scaled 775/1000 — CLEARS total floor (≥720)
                  but FAILS domain floor (D2 45%) and scenario floor (CI block 67%)
Go/No-Go:         NO-GO on booking. Per protocol: "Total ≥ 720 but a domain/scenario floor missed →
                  targeted remediation on that segment, then re-test that segment. Do NOT book on the
                  total alone." Session 36 = targeted re-drill on D2 (primary) + the 9 regressed concepts.
```

---

## Completion Health (update every session — solo-learner dropout is the #1 risk)

```
Exam booking target:   2026-08-22 (provisional)
Last session date:     2026-07-10
Days since last:        0 (today — S34 gap remediation)
Sessions this week:     2 (S33 on 2026-07-09; S34 on 2026-07-10)
Current streak:          active (Jul 9, Jul 10)
Next session booked:   Session 35 — Mock Exam #1
Cadence target:        3 sessions remain (S35–S37); mock readiness dependent on D1.1 + D4.2 trap-resistance
```

### 5-Week Reference Calendar (target dates; adjust to actual start)
| Week | Focus | Sessions |
|---|---|---|
| 1 | Orientation + D1 (Agentic Architecture) | 1–9 |
| 2 | D3 (Claude Code) + D4 start | 10–18 |
| 3 | D4 finish + D2 (Tools & MCP) | 19–26 |
| 4 | D5 (Context) + Integration | 27–33 |
| 5 | Remediation + Mocks + Go/No-Go | 34–37 |

> **Missed-day rule:** a missed session moves the calendar, it does not delete a session. If >10 days lapse, run a re-engagement check and a wider Spaced-Repetition Flash before resuming. The adaptive path (SESSION-PLAN Session 1) can compress known concepts to recover time.

### Held-out mock — CORRECTED (2026-07-10): claimed bank does not exist on disk
The 2026-06-26 claim below was never verified and the folder is absent (`../practice/held-out-mocks/` — checked 2026-07-10, does not exist). Do not trust this claim at mock time without re-verifying the path first — see global VERIFICATION discipline.
**Actual mock source for Session 35:** `../prep with quiz/mock-exams/CCA-Prep_MockTest-4_v1.html` — genuinely unattempted, FULL60 format, exact domain quota (D1 16/D2 11/D3 12/D4 12/D5 9), generated under orchestration-prompt v9's corrected fidelity standard (generic scenario framing, no invented names, pre-planned balanced answer letters, verified end-to-end in a live browser render). Ram takes this exam directly in the HTML file; results-JSON comes back here for scoring and Go/No-Go analysis.
~~2×60 fresh, domain-weighted, scenario-tagged questions authored with no overlap with teaching examples or the `practice/` banks. Location: `../practice/held-out-mocks/` (Mock A + Mock B + per-domain files + answer keys). Sealed — open only at mock time (Sessions 35/37).~~

---

## Resume Bookmark (read FIRST on resume; written at every sign-off)

```
Last sign-off:     2026-07-11 (Session 35 closed; Session 36 begins same sitting)
Resume at:         Session 36 — Mock #1 Analysis + Targeted Re-Drill (Professor re-teaches, Exam Coach drills) — IN PROGRESS, starting with D2 (confirmed weak, gates Go/No-Go)
Mid-concept?:      No — clean session boundary (mock scored and fully logged)
Reinforcement due: D2 domain — PRIORITY, confirmed weak (45%). Re-teach: D2.4 (error categorization),
                     D2.6 (Edit-anchor fallback), plus new gaps (two-tool token-binding, description
                     boundary clarity — 2 misses).
                   D1.2/D1.6/D1.8 🔴 — re-teach allowed_tools whitelisting, escalation trigger conditions,
                     decomposition-gap diagnosis.
                   D3.1/D3.3 🔴 — re-teach @import nesting depth + concatenation, context:fork.
                   D4.6/D4.7 🔴 — re-teach tool_choice:any, schema-validation-is-syntax-only.
                   New gaps (D1 partial-failure synthesis, D4 stated-assumptions) — teach as extensions
                     of D1.3 and D4.4 respectively.
Note to professor: S35 ⚠️ 2026-07-11: Mock Exam #1. Warm-up 3/3 clean confident (D1.1, D4.2 → 🟡;
                   D2.6 → 🟢). Mock taken via Exam 4 HTML (results-JSON scored): 45/60, 775 scaled.
                   NO-GO — D2 domain floor breach (45%) and CI scenario floor breach (67%) despite
                   total clearing 720. 15 misses analyzed against corpus citations; 9 mapped to existing
                   ledger cells (all dropped to 🔴, including D2.6 which had JUST been promoted to 🟢 in
                   this same session's warm-up — see LEARNER-MODEL.md insight log for the "narrow
                   promotion" lesson). 4 new gaps logged in LEARNER-MODEL.md's Mock-Surfaced Gaps table.
                   Timing data unreliable (multi-hour gaps between some questions — breaks, not think
                   time); domain/scenario accuracy signal still valid. Session 36 = targeted re-drill,
                   D2 first. Do NOT proceed to Mock #2 (S37) until D2 clears 70% on re-test.
```

> On resume ("Professor, I'm back"), read this block + `LEARNER-MODEL.md`, open with a Spaced-Repetition Flash drawn from the Reinforcement Queue, then continue at **Resume at**. The sign-off ritual that writes this block is Session Type 6 in `ENGAGEMENT-PROTOCOL.md`.

---

## Session Log

Update this file at the end of every session. Format: `[status] Session N — brief note`

Status codes: `[✅]` = complete · `[🔄]` = in progress · `[⬜]` = not started · `[⚠️]` = completed with gaps

---

### Phase 0 — Orientation

| # | Session | Status | Notes |
|---|---|---|---|
| 1 | Orientation + Baseline Diagnostic | ✅ | 10-Q cold diagnostic complete (2026-06-27). D1 🟡, D2–D5 🔴. Provisional exam: 2026-08-22. |

---

### Phase 1 — Domain 1: Agentic Architecture (27%)

| # | Session | Status | Notes |
|---|---|---|---|
| 2 | Agentic Loop Fundamentals | ✅ | stop_reason, stateless model, tool_use/end_turn cycle — D1.1 strong in-session |
| 3 | The Agentic Loop as a Pattern | ✅ | Anti-patterns nailed in-session; missed on SR flash S5 → D1.1 back to 🔴 |
| 4 | AgentDefinition + Hub-and-Spoke | ✅ | Least privilege instinct correct; context isolation confirmed S5 flash; D1.3 🟡 |
| 5 | Task Tool + Explicit Context Passing | ✅ | Parallel spawning, context discipline, token cost trade-off — D1.4 🟡 |
| 6 | ★ Hooks: PreToolUse/PostToolUse | ✅ | Deterministic vs probabilistic distinction confirmed; discount/financial example correct — D1.5 🟡 |
| 7 | ★ Escalation Patterns + Handoffs | ✅ | 3 patterns taught; structured handoff payload; unreliable triggers. D1.6 🟡 |
| 8 | ★ Session Mgmt + Task Decomposition | ✅ | resume/fork/fresh; fixed vs dynamic; multi-pass + attention dilution. D1.7/D1.8 🟡 |
| 9 | D1 Comprehension Check + Scenario Drill | ✅ | 3/3 comprehension; 4/5 MCQs. D1.1 🔴 persists (text-content anti-pattern selected as correct in Q2) |

---

### Phase 2 — Domain 3: Claude Code Config (20%)

| # | Session | Status | Notes |
|---|---|---|---|
| 10 | CLAUDE.md Hierarchy + @path | ✅ | Both concepts clean. D3.1 🟡 first clean recall. |
| 11 | Path-Specific Rules (.claude/rules/) | ✅ | Conditional loading needed teaching then landed. D3.2 🟡. |
| 12 | ★ Skills: context:fork, allowed-tools | ✅ | allowed-tools pre-approve trap nailed cold. D3.3 🟡. |
| 13 | Planning Mode + /compact + /memory | ⚠️ | Explore subagent needed prompting; /compact+/memory taught but not drilled. D3.4 🟡. |
| 14 | ★ CI/CD: -p flag + JSON output | ✅ | --bare identified correctly; context isolation solid. D3.6 🟡. |
| 15 | D3 Comprehension Check + Scenario Drill | ⚠️ | 3/5 MCQs. MCQ 1 (user vs project) + MCQ 4 (paths: scope) missed. Scenario 2/4. Cross-domain hook correct, "deterministic" vocab missing. |

---

### Phase 3 — Domain 4: Prompt Engineering (20%)

| # | Session | Status | Notes |
|---|---|---|---|
| 16 | Few-Shot + Explicit Criteria | ⚠️ | SR flash 3/3. D4.1 boundary type correct; vocabulary gaps ("training" vs "few-shot examples"). D4.2 🟡 new. D4.3 🟡 after clarification. Comprehension Q1/Q3 🟡, Q2 🟢. |
| 17 | tool_use with JSON Schemas | ⚠️ | SR flash: D1.8 ✅ "attention dilution" cold, D4.2 🟡 (negative space ✅, positive criteria confused with few-shot again). Comprehension 2/3: Q1 ✗ (broken vs fixed schema confusion — selected correct-design answer for broken-schema question). Q2 ✅ enum + "other". Q3 ✅ semantic vs syntactic. D4.5/6/7 🔴→🟡. |
| 18 | ★ Validation + Retry + Self-Correction | ⚠️ | Comprehension 2/3: Q1 ✗ (Type 2 failure not classified before retry — applied retry to info-not-in-source scenario). Q2 ✅ retry-without-3-elements → same output. Q3 ✅ self-correction pattern. D4.8 🟡 new. |
| 19 | ★ Message Batches API | ✅ | 3/3 comprehension: multi-turn constraint (Q1), custom_id targeted re-submission (Q2), SLA math — deadline < 24h → sync (Q3). D4.9 🟡 new. First perfect score on new material. |
| 20 | ★ Multi-Instance Review + Interview Pattern | ✅ | 3/3: reasoning-context bias (Q1), parallel per-unit + sequential integration (Q2), interview pattern trigger = genuine ambiguity (Q3). D4.4/10 🟡 new. Second consecutive 3/3. |
| 21 | D4 Comprehension Check + Scenario Drill | ⚠️ | Comprehension 3/3 ✅. Scenario 4/5: Q4 ✗ (enum+other chosen for multi-value field — array type needed). D4.8 Type 1/2 gate recovered cold. D4 domain: 87% (7/8). |

---

### Phase 4 — Domain 2: Tool Design & MCP (18%)

| # | Session | Status | Notes |
|---|---|---|---|
| 22 | ★ Tool Description as Selection Mechanism | ✅ | 3/3 comprehension. Misconception corrected: descriptions are always-present selection context, not lazy-load gates. D2.1 🔴→🟡. |
| 23 | MCP Architecture + Server Config | ⚠️ | 2/3 comprehension. Q1 miss: vocabulary trap (D vs B — Actions/Context/Templates ≠ Tools/Resources/Prompts). Q3 miss: auto-discovery vs resources conflated. D2.2 🟡, D2.3 🟡 new. |
| 24 | ★ isError Errors + Tool Allocation | ✅ | 3/3 comprehension. Two-channel trap correct. Error categories correct. D2.4/D2.5 ⚪→🟡. SR flash 0/3: D2.2 vocab + resources vs auto-discovery + D1.1 all missed → 🔴. |
| 25 | Built-in Tool Selection + Incremental Investigation | ⚠️ | 2/3. Q1 miss: Glob (file names) vs Grep (file content). Q2/Q3 correct. D2.6 ⚪→🟡. |
| 26 | D2 Comprehension Check + Scenario Drill | ✅ | 3/3 comprehension + 5/5 scenario drill = 8/8. D2 domain gate PASSED. Resources vs auto-discovery recovered in Q3. |

---

### Phase 5 — Domain 5: Context Management (15%)

| # | Session | Status | Notes |
|---|---|---|---|
| 27 | Context Window Risks + Lost-in-Middle | ⚠️ | 2/3. Q1 ✅ positional bias mechanism (D5.1 🔴→🟡). Q2 ✗ mitigation: placed findings in middle — correct is key findings TOP. Q3 ✅ PostToolUse trimming. D5.2 ⚪→🟡. |
| 28 | Trimming + Persistent Fact Blocks | ✅ | 3/3. PostToolUse trimming (Q1), persistent fact block (Q2), position-aware input TOP/BOTTOM (Q3 — S27 mitigation miss cleared). D5.2 🟡→🟢. D5.3 ⚪→🟡. |
| 29 | ★ Scratchpad Files + State Persistence | ⚠️ | 2/3. Q1 ✅ scratchpad pattern. Q2 ✗ over-corrected: chose "never return to coordinator" instead of "return structured summary." Q3 ✅ manifest + per-agent state files. D5.3 🟡 (first session, miss on subagent output scope). |
| 28 | Trimming + Persistent Fact Blocks | ⬜ | |
| 29 | ★ Scratchpad Files + State Persistence | ⬜ | Gap concept |
| 30 | ★ Confidence Calibration + Provenance | ✅ | SR flash 3/3 (D5.1→🟢, D1.1/D2.2 🔴→🟡). Comprehension 3/3. D5.4/D5.5 ⚪→🟡. |
| 31 | D5 Comprehension Check + Scenario Drill | ✅ | Comprehension 3/3 + Scenario 5/5 = 8/8. D5.3/4/5 🟡→🟢. D5 DOMAIN PASSED. |

---

### Phase 6 — Integration Scenarios

| # | Session | Status | Notes |
|---|---|---|---|
| 32 | Integration A: Multi-Agent Research | ✅ | 8/8. D1+D4+D5. D4.5 🟡→🟢, D4.8 🟡→🟢. |
| 33 | Integration B: Conversational AI Arch. | ⚠️ | 7/8. MCQ3 ✗ D2.1 lazy-loading misconception + D2.5 fix. D1.6 🟢, D4.5 ✅, D4.9 🟢, D5.2 ✅, D5.5 ✅. |
| 34 | Gap Remediation (conditional) | ⚠️ | 4/6. D2.1+D2.5+D2.2x2 ✅. D1.1 ✗ (stop_reason trap), D4.2 ✗ (few-shot bleed). D2.6 not drilled. |

---

### Phase 7 — Mock Exams

| # | Session | Status | Score | Notes |
|---|---|---|---|---|
| 35 | Mock Exam #1 (60 Q / 120 min) | ⚠️ | 45/60, 775 scaled | Warm-up 3/3 clean. Mock via Exam 4 (HTML). Total clears 720 but D2 (45%) + CI scenario (67%) breach floor → NO-GO. 15 misses, 9 mapped to existing 🔴 regressions, 4 new gaps surfaced. See LEARNER-MODEL.md for full breakdown. |
| 36 | Mock #1 Analysis + Targeted Re-Drill | ⬜ | — | |
| 37 | Mock Exam #2 + Go/No-Go | ⬜ | — | |

---

## Active Gaps Log

*(Populate this section as comprehension checks reveal persistent weak areas)*

| Gap identified | Domain | Session discovered | Status |
|---|---|---|---|
| *(none yet)* | | | |

---

## Baseline Diagnostic Results (Session 1)

*(Fill in after Session 1 — cold 5-question diagnostic, one question per domain)*

| Domain | Baseline read | Notes |
|---|---|---|
| D1 — Agentic Architecture | 🟡 Developing | Loop and orchestrator/subagent conceptually solid; stop_reason technical layer missing |
| D2 — Tool Design & MCP | 🔴 Weak | USB/MCP analogy right; tool description has lazy-loading misconception; primitives unknown |
| D3 — Claude Code Config | 🔴 Weak | CLAUDE.md surface-level; headless/CI mode unknown |
| D4 — Prompt Engineering | 🔴 Weak | Few-shot partial; stop_reason / tool_use API cycle unknown |
| D5 — Context Management | 🔴 Weak | Lost-in-middle symptom right, mechanism wrong; prompt caching unknown |

---

## Mock Exam Scores

| Attempt | Date | Raw questions correct | Est. scaled score | Go/No-Go |
|---|---|---|---|---|
| Mock #1 (Exam 4) | 2026-07-11 | 45/60 (D1 12/16, D2 5/11, D3 9/12, D4 10/12, D5 9/9) | 775/1000 | NO-GO — total passes but D2 domain (45%) and CI scenario (67%) both breach the 70% floor |
| Mock #2 | | | | |
| Real exam | | | | |

---

## Session Start Protocol (read this every session)

1. Read this file — the **Resume Bookmark** first, then current session number and active gaps
2. Read `LEARNER-MODEL.md` — mastery state, Reinforcement Queue, interlinks, insights
3. Read SESSION-PLAN.md entry for the current session
4. If there are active gaps, flag them for the Exam Coach if the current session is a drill
5. Open with Spaced Repetition Flash (2–3 questions from the TOP of the Reinforcement Queue) — skip only for Session 1
6. Adopt the correct persona (Professor or Exam Coach per SESSION-PLAN.md)

## Session End Protocol (update these files every session)

1. Change session status from ⬜ to ✅ or ⚠️
2. Add a brief note if any concept did not fully land
3. Add any persistent weak areas to the Active Gaps Log
4. Update `LEARNER-MODEL.md`: mastery transitions, Reinforcement Queue, Domain Confidence Summary, any new interlink/insight
5. Update the `Current Status` block and the `Resume Bookmark` at the top

> If the session ends on the learner's signal ("that's it for today"), run the full **Day's-End Ritual** (Session Type 6 in `ENGAGEMENT-PROTOCOL.md`) instead — it covers all of the above plus a spoken close.
