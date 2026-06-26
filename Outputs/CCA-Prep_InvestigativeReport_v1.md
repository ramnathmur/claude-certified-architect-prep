# CCA-F Exam Readiness — Investigative Report

> **⚠️ Correction (appended 2026-06-26):** The scenario findings in this report were based on a community guide and are **SUPERSEDED**. The official Anthropic exam guide (`academy/CCA-F_Official-Exam-Guide_v0.1.pdf`, retrieved from the logged-in Skilljar site) confirms the exam has **6 scenarios, not 8** — there is no Scenario 7 or 8, so the "Scenario 8 gap" discussed below does **not** apply. The official domain numbering also differs (D2 = Tool Design & MCP 18%, D3 = Claude Code Config 20%, D4 = Prompt Engineering 20%). The academy files have been reconciled to the official guide; treat this report as a historical snapshot.

**Date:** 2026-06-26  
**Auditor:** Claude (senior curriculum auditor persona)  
**Subject:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\`  
**Single objective assessed:** Will this project get Ram exam-ready to pass the CCA-F?  
**Sources:** Academy folder audit · Full project folder audit · Official Anthropic documentation · Internet/community research

---

## 1. Executive Summary

The CCA-F Prep project is one of the most architecturally complete self-study programs I have audited. It has a rigorous curriculum map, a 37-session AI-professor delivery plan, 51 original practice questions, three cross-domain integration checkpoints, 12 QA-gated HTML reference courses, and a Go/No-Go mock exam system. **The design alone merits a 9/10.** However, the program has not started — 0 of 37 sessions have been delivered — and it carries two substantive content gaps that, if uncorrected, create meaningful exam risk: Scenario 8 (Agentic AI Tools) is entirely unaddressed, and several nuanced distinctions surfaced by live documentation audits are absent from the curriculum. The project is well-positioned to achieve its goal, but only once execution begins and the identified gaps are patched.

**Overall Project Rating: 7.5 / 10**

---

## 2. Curriculum Inventory

| Asset | Type | Domains Covered | Depth |
|---|---|---|---|
| `academy/CURRICULUM.md` | Topic map | All 5 (D1–D5) | Deep — sub-domain level, gap-flagged |
| `academy/SESSION-PLAN.md` | Delivery plan | All 5 + integration | Deep — 37 sessions, analogies scripted |
| `academy/ENGAGEMENT-PROTOCOL.md` | Pedagogy protocol | (methodology) | Deep — 4-beat probe, comprehension gates |
| `academy/PROGRESS.md` | Progress tracker | — | Not started (0/37 sessions) |
| `courses/claude-101.html` | HTML course | D1–D5 foundations | Adequate (surface-level intro) |
| `courses/introduction-to-subagents.html` | HTML course | D1 partial, D2 partial | Adequate |
| `courses/tool-use-agent-loop.html` | HTML course | D1+D4 | Deep |
| `courses/context-management-reliability.html` | HTML course | D5 | Deep |
| `courses/mcp-at-a-builder-level.html` | HTML course | D4 | Deep |
| `courses/prompt-caching-economics.html` | HTML course | D5 | Adequate |
| `courses/prompt-engineering-depth.html` | HTML course | D3 | Adequate |
| `courses/claude-code-configuration.html` | HTML course | D2 | Adequate |
| `courses/orchestration-patterns.html` | HTML course | D1 | Deep |
| `courses/subagents-as-sdk-primitive.html` | HTML course | D1+D2 | Deep |
| `courses/orchestrator-worker-at-scale.html` | HTML course | D1+D5 | Deep |
| `courses/orchestrator-worker-at-scale-202.html` | HTML course | D1+D5 | Deep (advanced) |
| `practice/CCA-F_practice_d1-agentic-architecture.md` | Practice questions | D1 | Deep — 14 questions |
| `practice/CCA-F_practice_d2-claude-code.md` | Practice questions | D2 | Deep — 10 questions |
| `practice/CCA-F_practice_d3-prompt-engineering.md` | Practice questions | D3 | Deep — 10 questions |
| `practice/CCA-F_practice_d4-tools-mcp.md` | Practice questions | D4 | Deep — 9 questions |
| `practice/CCA-F_practice_d5-context-reliability.md` | Practice questions | D5 | Deep — 8 questions |
| `practice/CCA-F_checkpoint_A_support-agent_D1xD5.md` | Integration checkpoint | D1×D5 | Deep |
| `practice/CCA-F_checkpoint_B_ci-cd_D2xD3.md` | Integration checkpoint | D2×D3 | Deep |
| `practice/CCA-F_checkpoint_C_multi-agent-research_D1xD4.md` | Integration checkpoint | D1×D4 | Deep |
| `mcq-practice/index.html` | Interactive MCQ drill | Mixed | Adequate |
| `EXAM-DIGEST.md` / `EXAM-DIGEST.html` | Exam digest | All 5 | Deep |
| `GAPS.md` | Gap log | Mixed | In use (synthetic runs flagged) |
| `guide_en.MD` (external) | Official study guide | All 5 + 60 practice Qs | Deep — 3,400+ lines |

---

## 3. Domain Coverage Matrix

| Domain | Exam Weight | Current Coverage | Missing Subtopics |
|---|---|---|---|
| D1 — Agentic Architecture & Orchestration | 27% | **~75%** | Hooks detailed in docs exceed guide (18 hook types; only Pre/PostToolUse in curriculum); `Managed Agents` REST API distinction not in curriculum |
| D2 — Claude Code Configuration & Workflows | 20% | **~70%** | `--bare` flag for headless mode (skips all local config; potential exam trap vs just `-p`); `disallowed-tools` frontmatter; `disable-model-invocation` and `user-invocable: false` skill options |
| D3 — Prompt Engineering & Structured Output | 20% | **~80%** | Structured Outputs (constrained decoding) flagged in GAPS.md as the correct first fix for malformed JSON at scale — curriculum covers `tool_use` but may miss this nuance |
| D4 — Tool Design & MCP Integration | 18% | **~75%** | `isError: true` inside a successful JSON-RPC response (distinct from JSON-RPC protocol errors — exam-trap distinction); `outputSchema` and `structuredContent` MCP fields (newer, may appear); `allowed-tools` pre-approves but does NOT restrict (common misconception not addressed) |
| D5 — Context Management & Reliability | 15% | **~80%** | No significant gaps beyond what CURRICULUM.md identifies |

---

## 4. Scenario Coverage Matrix

The exam draws 4 scenarios from a pool. Community research confirms **8 scenarios** in the pool (not 6 as listed on many third-party prep sites). The extra two are Scenario 7 (Conversational AI Architecture) and Scenario 8 (Agentic AI Tools).

| Scenario | Status | Integration Session | Notes |
|---|---|---|---|
| 1 — Customer Support Agent | **Covered** | Session 9 (drill) + Checkpoint A (D1×D5) | Full scenario drill + integration checkpoint |
| 2 — Code Generation with Claude Code | **Partial** | Session 15 (CI/CD focus) | CI/CD angle covered; code generation / planning-mode scenarios less drilled |
| 3 — Multi-Agent Research System | **Covered** | Session 32 (integration) + Checkpoint C (D1×D4) | Full integration session |
| 4 — Developer Productivity Tools | **Partial** | Session 25 (built-in tools) | No dedicated scenario drill; flagged in GAPS.md synthetic run as the "most missed" scenario name |
| 5 — Claude Code for CI/CD | **Covered** | Session 15 (drill) + Checkpoint B (D2×D3) | Full scenario drill + integration checkpoint |
| 6 — Structured Data Extraction | **Covered** | Session 21 (drill) | Full scenario drill |
| 7 — Conversational AI Architecture | **Covered** | Session 33 (integration) | Cross-domain integration session; all 5 domains |
| 8 — Agentic AI Tools | **NOT COVERED** | None | Zero coverage. See Gap Analysis. |

**Scenario gap risk calculation:** With 4 of 8 scenarios randomly selected, the probability that Scenario 8 appears in Ram's exam is approximately **50%** (4/8). This is not a tail risk — it is a coin flip.

---

## 5. Sequence Assessment

The curriculum sequence is **logically sound and pedagogically justified**. The prerequisite graph in CURRICULUM.md traces a clean dependency chain:

```
API fundamentals → Tool use → Agentic loop → Coordinator/subagent
→ Hooks → Escalation → Session management → Task decomposition
→ Prompt patterns → JSON schemas → Validation/retry → Batch API
→ Context accumulation → Trimming → Scratchpad → Confidence/provenance
→ Integration scenarios → Mock exams
```

**What works well:**
- D1 (27%) is taught first and given the most sessions (8) — proportional to its exam weight.
- Each domain builds on the previous: you cannot reason about hooks without understanding the agentic loop; you cannot reason about context trimming without understanding coordinator-subagent patterns.
- Integration scenarios are placed after all five domains, not interleaved — this is correct.
- Mock exams come last, after gap remediation, not before.

**One sequencing concern:**
- SESSION-PLAN.md's header states "Total sessions: 34" but the document lists **37 sessions** (including the conditional gap remediation Session 34 and the three mock exam sessions 35–37). This is a documentation inconsistency that will confuse progress tracking. PROGRESS.md correctly tracks 37 sessions.

**Verdict on sequence:** No structural sequencing problems. The inconsistency in session count is cosmetic but should be corrected.

---

## 6. Gap Analysis

### CRITICAL (fix before starting the program)

**GAP-C1: Scenario 8 — Agentic AI Tools — Zero Coverage**

This is the most significant finding. The official study guide explicitly marks Scenario 8 as having "no content" and calls for community contributions. Neither the curriculum, the practice bank, nor the HTML courses address it. Internet research confirms it is real and has been reported by actual exam candidates.

The exam has 8 scenarios; 4 are randomly drawn per sitting. If Scenario 8 is one of Ram's 4, there is currently no preparation for any question from it. The probability is ~50%.

*Recommended action:* Check the [github.com/paullarionov/claude-certified-architect](https://github.com/paullarionov/claude-certified-architect) issue tracker for community-submitted Scenario 8 questions. Search claudecertifications.com (already listed as a supplement in the practice README). Add a dedicted Session 34a to the academy covering whatever emerges. Mark it as high-priority.

---

**GAP-C2: Zero Sessions Delivered**

The academy is a delivery system, not a self-teaching resource. The PROGRESS.md tracker is at 0/37 sessions. The GAPS.md contains only "synthetic runs" (Claude-modeled answers, not Ram's real recall) — flagged explicitly in the file as unreliable baselines.

The project has excellent infrastructure but no execution. At 1 session/day, the curriculum takes 5 weeks. At 2 sessions/day, 2.5 weeks. This is the single biggest exam risk.

*Recommended action:* Book Session 1 (Orientation + Baseline Diagnostic) immediately. The cold 5-question diagnostic will establish where time needs to be concentrated.

---

### IMPORTANT (add before mid-program)

**GAP-I1: `--bare` Flag Missing from Curriculum**

The live Claude Code headless documentation explicitly describes `--bare` as a distinct flag from `-p`. `--bare` skips auto-discovery of hooks, skills, plugins, MCP servers, auto-memory, and CLAUDE.md. Plain `-p` does NOT skip these. The docs note `--bare` is "recommended for scripted and SDK calls" and will become the default for `-p` in a future release.

This is an exam-trap distinction: an option like `claude -p "review this PR"` is NOT equivalent to `claude -p --bare "review this PR"` in terms of what config loads.

*The curriculum teaches only `-p` / `--print`.* Session 14 (CI/CD) should include the `--bare` distinction.

---

**GAP-I2: `allowed-tools` Misconception in Skills Frontmatter**

The live Skills documentation states: "`allowed-tools` auto-approves listed tools — it does NOT restrict other tools. All other tools remain callable subject to existing permissions." The curriculum description implies restriction. This is a semantically inverted understanding that exam distractors exploit.

*Add a correction note to Session 12 (Skills frontmatter).* The field name sounds restrictive but it is actually a pre-approval list.

---

**GAP-I3: `isError` vs. JSON-RPC Protocol Error Distinction**

The MCP documentation reveals two distinct error channels: (1) JSON-RPC protocol errors (malformed request, unknown method — the JSON-RPC response itself is an error), and (2) tool execution errors reported with `isError: true` inside a successful JSON-RPC response body. These are architecturally different and the exam may test the distinction.

The curriculum addresses `isError: true` correctly but does not contrast it with the alternative error channel.

*Add one paragraph to Session 24 (isError Structured Errors).* 

---

**GAP-I4: Scenario 4 (Developer Productivity Tools) Is Under-Drilled**

The GAPS.md synthetic run flagged Developer Productivity Tools as the most commonly missed scenario name. The academy has no dedicated scenario drill for it (Session 25 covers built-in tools generally, but not the scenario). With a ~50% chance of it appearing, this deserves a drill.

*Add a 15-minute scenario drill for Scenario 4 to Session 25 or Session 26.*

---

**GAP-I5: Hook Roster Wider Than Curriculum Teaches**

The live Hooks documentation lists 18 hook types. The curriculum teaches only 2 (PreToolUse, PostToolUse). The exam may test awareness of others: `PostToolUseFailure`, `UserPromptSubmit`, `Stop`, `PreCompact`, `SubagentStart`/`SubagentStop`, `PermissionRequest`. The `defer` outcome (ends query for later resumption, distinct from `ask`) is also exam-relevant and not in the curriculum.

*Add a one-page reference table to Session 6 (Hooks).* Do not teach all 18 in depth — but ensure the exam-relevant ones are named.

---

### NICE-TO-HAVE (add if time permits)

**GAP-N1: Structured Outputs (Constrained Decoding) vs. Retry Loops**

GAPS.md synthetic run flagged this: "for malformed JSON at scale, the first lever is Structured Outputs (constrained decoding), not retry/dead-letter." The curriculum's D3 coverage focuses on `tool_use` + JSON Schema + retry-with-feedback but does not explicitly name Structured Outputs as the prior art that makes invalid output impossible at the source.

---

**GAP-N2: `Managed Agents` REST API vs. Agent SDK**

The live Agent SDK overview distinguishes three tiers: Client SDK (you call the API directly), Agent SDK (you run the process locally), and Managed Agents (Anthropic runs the sandbox). The exam may test whether a candidate can choose the right tier. The curriculum does not address Managed Agents.

---

**GAP-N3: Message Batches API — 29-Day Results Retention**

The docs clarify that results are available for 29 days after batch creation, distinct from the 24-hour processing window. The curriculum correctly teaches the 24-hour SLA; the 29-day retention is not mentioned. Unlikely to be tested but worth one sentence in Session 19.

---

**GAP-N4: No Scenario 8 Coverage Anywhere in the Community**

This is worth tracking. The paullarionov GitHub guide requests contributions via Issues. If Ram encounters Scenario 8 questions in third-party practice banks, contributing them back to the community guide benefits everyone. The `cca-f-mock-exam` GitHub repo (1 star) may have Scenario 8 coverage — worth checking before the exam.

---

## 7. Internet Research Findings

### 7.1 Exam Status and Format (Confirmed)

- CCA-F launched March 12, 2026. It is live and fully operational.
- 60 scenario-driven MCQs, 120 minutes, 720/1000 pass, $99 per attempt.
- 4 of **8** scenarios appear per exam (not 4 of 6 as many prep sites state — community research confirms 8).
- The exam is harder to find than expected: it is not on the Skilljar homepage's public course catalog. Access requires the Anthropic Partner Portal (`partnerportal.anthropic.com`) or a direct link from Anthropic.

### 7.2 Infosys Partner Free Access

- Infosys is a confirmed named Claude Partner (alongside Accenture, Deloitte, Cognizant).
- The first 5,000 Partner Network employees took the exam free at launch. That window may be closed.
- Tiered partners receive "discounted rates on their first attempt" as a sustained benefit.
- **Action required:** Verify free/discounted access at `partnerportal.anthropic.com` with your Infosys corporate email before paying $99.

### 7.3 Community Difficulty Reports

- The exam penalizes surface familiarity. Distractors are designed to look correct to candidates who studied in isolation.
- The most commonly cited difficulty: **cross-domain integration**. Candidates who mastered domains separately underperformed on questions that combine two domains in one scenario.
- The project already addresses this with integration scenarios and cross-domain checkpoints — this is a strength.
- One reported top score: 985/1000, suggesting prepared candidates do very well.

### 7.4 Community Resources Worth Using

| Resource | What to use it for |
|---|---|
| `github.com/paullarionov/claude-certified-architect` | Most complete community guide; 8 scenarios documented; Issue tracker for Scenario 8 contributions |
| `claudecertifications.com/claude-certified-architect` | 25 practice questions + 6 scenario walkthroughs (already in practice README as supplement) |
| `cca-f-mock-exam` GitHub repo | 60-question timed mock with analytics — check if Scenario 8 content exists |
| Anthropic Academy (13 free courses on Skilljar) | Official supplemental material; confirms domain weights |
| Tutorials Dojo CCA-F Study Guide | Third-party practice questions for additional volume |

### 7.5 Documentation Gaps vs. Study Guide

The live documentation audit revealed the following details **not present** in the community study guide or this project's curriculum:

| Finding | Exam relevance | Session to patch |
|---|---|---|
| `--bare` flag skips all local config (vs. `-p` which doesn't) | High — likely trap in CI/CD scenario | Session 14 |
| `allowed-tools` pre-approves, does NOT restrict | High — inverted semantics in curriculum | Session 12 |
| `isError: true` is inside a successful JSON-RPC response (≠ JSON-RPC protocol error) | Medium | Session 24 |
| 18 hook types total; `defer` outcome distinct from `ask` | Medium | Session 6 |
| `Managed Agents` REST API vs. Agent SDK | Low-medium | Session 4 |
| `disallowed-tools` / `disable-model-invocation` skill frontmatter fields | Low | Session 12 |

---

## 8. Recommendations (Prioritized)

### Before starting the program

1. **Book Session 1 today.** The program delivers nothing until sessions run. Every week of delay is a week closer to the exam with zero active recall built.
2. **Verify Infosys free exam access** at `partnerportal.anthropic.com` before paying $99.
3. **Fix the session-count inconsistency:** Change "Total sessions: 34" in SESSION-PLAN.md header to "37". Small but will confuse progress tracking.

### Within the first two weeks of study

4. **Research Scenario 8 immediately.** Check `github.com/paullarionov/claude-certified-architect` issues, `cca-f-mock-exam` repo, and `claudecertifications.com` for any Scenario 8 content. Add whatever you find to Session 34a (a new conditional session for Scenario 8) in the SESSION-PLAN.
5. **Patch the `--bare` / `allowed-tools` / `isError` gaps** into Sessions 6, 12, 14, and 24 respectively. These are 1–3 paragraph additions, not full session rewrites.
6. **Add a Scenario 4 (Developer Productivity Tools) drill** to Session 25 or 26. It's the scenario most commonly missed by name, and it has no dedicated drill currently.

### Before mock exams

7. **Run all three integration checkpoints** (A, B, C) before Mock Exam #1. The practice README already mandates this sequence — follow it.
8. **Convert synthetic GAPS.md entries to real ones.** The existing GAPS.md entries are Claude-modeled answers, not Ram's recall. Re-run those diagnostic questions interactively after sessions 2–5 to get real baselines.

### Before booking the real exam

9. **Apply the Go/No-Go criteria strictly.** Only book the exam after Mock Exam #2 produces a scaled score equivalent ≥ 720. If Mock #2 produces 680–719, do one more targeted remediation before booking.
10. **Review the live Hooks documentation** (`code.claude.com/docs/en/agent-sdk/hooks`) once — 15 minutes. The full hook table is richer than any static study guide and may surface one or two exam-relevant distinctions the sessions didn't cover.

---

## 9. Verdict

**PARTIALLY READY — Strong Infrastructure, Execution Pending**

The project is among the most well-designed exam preparation programs I have reviewed. The curriculum is comprehensive, the sequencing is logical, the pedagogy is rigorous (spaced repetition, 4-beat comprehension probes, Go/No-Go gates), and the practice material is weighted to match exam domain proportions.

The project will achieve its goal — passing the CCA-F — if and when it is executed. It is currently a blueprint, not a program. The execution gap is the primary risk, not the content gaps.

The Scenario 8 blind spot is real and materially increases exam risk until it is addressed. The three documentation-level precision gaps (`--bare`, `allowed-tools`, `isError`) are narrower but could each be the deciding factor on a single question near the pass boundary.

**Start Session 1. Patch the three gaps. Research Scenario 8. Follow the Go/No-Go protocol. You will pass.**

---

*Report generated 2026-06-26 · Audit scope: academy folder (5 files) + full project folder (70+ files) + official Anthropic documentation (6 URLs) + internet/community research (15+ sources)*
