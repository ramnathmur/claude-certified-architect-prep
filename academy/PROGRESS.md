# CCA-F Academy — Session Progress Tracker

**Learner:** Ram
**Program start:** 2026-06-27
**Target exam date:** 2026-08-22 (provisional — reassess after Session 9 drill)

---

## Current Status

```
Current session:  5 (Task Tool + Explicit Context Passing)
Current phase:    1 — Domain 1: Agentic Architecture
Overall progress: 4 / 37 sessions complete
Active gaps:      D3.6 (headless/CI mode), D4.5 (stop_reason cycle), D5.1 (lost-in-middle mechanism), D5 (prompt caching)
Mock exam score:  Not yet taken
Go/No-Go:         Not yet decided
```

---

## Completion Health (update every session — solo-learner dropout is the #1 risk)

```
Exam booking target:   2026-08-22 (provisional)
Last session date:     2026-06-27
Days since last:        0
Sessions this week:     4 (Sessions 1–4 all completed on day 1 — strong start)
Current streak:          1 day
Next session booked:   Session 5 — Task Tool + Explicit Context Passing (next visit)
Cadence target:        ~1 session/weekday → ~8 weeks; compress to ~6 weeks with back-to-back sessions
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

### Held-out mock — ✅ BUILT (2026-06-26)
2×60 fresh, domain-weighted, scenario-tagged questions authored with no overlap with teaching examples or the `practice/` banks. Location: [`../practice/held-out-mocks/`](../practice/held-out-mocks/README.md) (Mock A + Mock B + per-domain files + answer keys). Covers the 6 official scenarios. Sealed — open only at mock time (Sessions 35/37). Note: prefer the official Skilljar practice exam for Mock #1.

---

## Resume Bookmark (read FIRST on resume; written at every sign-off)

```
Last sign-off:     2026-06-27
Resume at:         Session 5 — Task Tool + Explicit Context Passing (D1.4)
Mid-concept?:      No — clean session boundary
Reinforcement due: D1.1 (🟢 — confirm at SR flash), D1.3 (🟡 — explicit context passing + context isolation)
Note to professor: Strong first day. Sessions 1–4 complete. D1.1 confirmed 🟢 (loop mechanics, 
                   stop_reason, anti-patterns). D1.3 at 🟡 (context isolation demonstrated, 
                   confirm at Session 5 flash). Open Session 5 with SR flash on D1.1 + D1.3.
                   Then teach Task tool: spawn mechanics, explicit context format, parallel spawning.
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
| 2 | Agentic Loop Fundamentals | ✅ | stop_reason, stateless model, tool_use/end_turn cycle — D1.1 confirmed 🟢 |
| 3 | The Agentic Loop as a Pattern | ✅ | Anti-patterns nailed: text parsing, iteration cap, content check — all 3 classified correctly |
| 4 | AgentDefinition + Hub-and-Spoke | ✅ | Least privilege instinct correct; explicit context passing demonstrated; D1.3 at 🟡 |
| 5 | Task Tool + Explicit Context Passing | ⬜ | |
| 6 | ★ Hooks: PreToolUse/PostToolUse | ⬜ | Gap concept |
| 7 | ★ Escalation Patterns + Handoffs | ⬜ | Gap concept |
| 8 | ★ Session Mgmt + Task Decomposition | ⬜ | Gap concept |
| 9 | D1 Comprehension Check + Scenario Drill | ⬜ | |

---

### Phase 2 — Domain 3: Claude Code Config (20%)

| # | Session | Status | Notes |
|---|---|---|---|
| 10 | CLAUDE.md Hierarchy + @path | ⬜ | |
| 11 | Path-Specific Rules (.claude/rules/) | ⬜ | |
| 12 | ★ Skills: context:fork, allowed-tools | ⬜ | Gap concept |
| 13 | Planning Mode + /compact + /memory | ⬜ | |
| 14 | ★ CI/CD: -p flag + JSON output | ⬜ | Gap concept |
| 15 | D3 Comprehension Check + Scenario Drill | ⬜ | |

---

### Phase 3 — Domain 4: Prompt Engineering (20%)

| # | Session | Status | Notes |
|---|---|---|---|
| 16 | Few-Shot + Explicit Criteria | ⬜ | |
| 17 | tool_use with JSON Schemas | ⬜ | |
| 18 | ★ Validation + Retry + Self-Correction | ⬜ | Gap concept |
| 19 | ★ Message Batches API | ⬜ | Gap concept |
| 20 | ★ Multi-Instance Review + Interview Pattern | ⬜ | Gap concept |
| 21 | D4 Comprehension Check + Scenario Drill | ⬜ | |

---

### Phase 4 — Domain 2: Tool Design & MCP (18%)

| # | Session | Status | Notes |
|---|---|---|---|
| 22 | ★ Tool Description as Selection Mechanism | ⬜ | Gap concept |
| 23 | MCP Architecture + Server Config | ⬜ | |
| 24 | ★ isError Errors + Tool Allocation | ⬜ | Gap concept |
| 25 | Built-in Tool Selection + Incremental Investigation | ⬜ | |
| 26 | D2 Comprehension Check + Scenario Drill | ⬜ | |

---

### Phase 5 — Domain 5: Context Management (15%)

| # | Session | Status | Notes |
|---|---|---|---|
| 27 | Context Window Risks + Lost-in-Middle | ⬜ | |
| 28 | Trimming + Persistent Fact Blocks | ⬜ | |
| 29 | ★ Scratchpad Files + State Persistence | ⬜ | Gap concept |
| 30 | ★ Confidence Calibration + Provenance | ⬜ | Gap concept |
| 31 | D5 Comprehension Check + Scenario Drill | ⬜ | |

---

### Phase 6 — Integration Scenarios

| # | Session | Status | Notes |
|---|---|---|---|
| 32 | Integration A: Multi-Agent Research | ⬜ | D1+D4+D5 |
| 33 | Integration B: Conversational AI Arch. | ⬜ | All 5 domains |
| 34 | Gap Remediation (conditional) | ⬜ | Skip if integration scores strong |

---

### Phase 7 — Mock Exams

| # | Session | Status | Score | Notes |
|---|---|---|---|---|
| 35 | Mock Exam #1 (60 Q / 120 min) | ⬜ | — | |
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
| Mock #1 | | | | |
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
