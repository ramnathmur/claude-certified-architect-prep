# CCA-F Academy — Project Overview

**One-line purpose:** Get Ram exam-ready to pass the Claude Certified Architect — Foundations (CCA-F) exam, through an interactive AI-professor-led program rather than passive reading.

**Audience:** Non-human / AI systems. This is the read-FIRST document. An AI picking up this project cold should read this file before touching any other, then drop into the operational files named in §6. It is a stable **map** of the project — live, changing state lives in `PROGRESS.md` and `LEARNER-MODEL.md` (see §6).

> All exam facts below are attributed to the official CCA-F study guide (`C:\Users\ramna\Downloads\guide_en.MD`) and the exam platform `anthropic.skilljar.com`. Do not assert exam details from model memory; cite these sources.

---

## 1. What This Project Is

The **CCA-F Academy** is a structured, multi-session exam-preparation program for one learner — **Ram, a Solution Architect at Infosys (an Anthropic Claude Partner)** with hands-on Claude/agent experience. It is **not** a documentation library and **not** a passive reading course. Every concept is taught interactively, in dialogue, by an AI acting as a `professor`, and then drilled by an AI acting as an `exam_coach`.

**The single unifying goal:** pass the CCA-F exam. Every file, session, and design choice in this project serves that one objective. The program does not end at "content covered" — it ends at "exam-ready," confirmed by a timed mock-exam Go/No-Go decision (§5).

The program spans **37 sessions / ~29 hours**, delivered across 7 phases, at the learner's pace (the learner controls when each day ends — see §4).

---

## 2. The Exam at a Glance

*(Source: study guide + anthropic.skilljar.com. Verify partner exam access before booking.)*

| Parameter | Value |
|---|---|
| Exam | Claude Certified Architect — Foundations (CCA-F) |
| Platform | anthropic.skilljar.com |
| Questions | 60 scenario-driven multiple-choice (1 correct of 4) |
| Duration | 120 minutes, closed-book, no AI assistance |
| Passing score | **720 / 1000** scaled |
| Guessing penalty | None — answer every question |
| Cost | $99 per attempt (free/discounted for Claude Partner / Infosys employees — verify at `partnerportal.anthropic.com` first) |
| Scenarios | **4 of 6** drawn at random per sitting (official exam guide) |

### Five domains (weights drive session allocation)

| Code | Domain | Weight |
|---|---|---|
| D1 | Agentic Architecture & Orchestration | **27%** |
| D2 | Tool Design & MCP Integration | **18%** |
| D3 | Claude Code Configuration & Workflows | **20%** |
| D4 | Prompt Engineering & Structured Output | **20%** |
| D5 | Context Management & Reliability | **15%** |

> **Official domain numbering (authoritative, per `CCA-F_Official-Exam-Guide_v0.1.pdf`):** D1 Agentic (27%) · D2 Tool Design & MCP (18%) · D3 Claude Code Config (20%) · D4 Prompt Engineering (20%) · D5 Context (15%). **All academy + practice files now use this scheme**, so a real exam score report ("Domain 2: …") lines up. The reference-only `courses/` HTMLs and the historical `Outputs/` report retain the earlier internal numbering and sit outside the active study path.

### Six scenarios (4 appear per exam) — per the official exam guide
1. Customer Support Resolution Agent · 2. Code Generation with Claude Code · 3. Multi-Agent Research System · 4. Developer Productivity with Claude · 5. Claude Code for Continuous Integration · 6. Structured Data Extraction. *(There is no Scenario 7 or 8 — the earlier community guide listing 8 was incorrect.)*

---

## 3. How It Was Constructed

The curriculum was assembled from five sources, then gap-analysed against the exam, then sequenced by prerequisite.

### 3.1 Source material
| Source | Role in construction |
|---|---|
| Official CCA-F study guide (`guide_en.MD`) | Primary curriculum: domain weights, 5-domain/8-scenario structure, theory Chapters 1–13, domain notes, sample questions (incl. a 60-question practice test) |
| anthropic.skilljar.com verification | Confirmed format: 60 MCQs, 120 min, 720/1000, domain weights |
| 12 QA-gated HTML courses (`courses\`) | Existing assets audited for coverage; used as factual reference only — **NOT** assigned as reading to the learner |
| AI-First Learning Blueprint (`my blueprints\AgentFoundry_AI-First-Learning-Blueprint_v1.md`) | Pedagogical framework (O-R-A loop, four-beat probe, persona protocols) — shapes HOW the professor teaches, not what is covered |
| Persona Library (`AI agents personas\`) | Supplies the `professor` and `exam_coach` personas (routed via ROUTER.md, read before activation) |

### 3.2 Methodology (how exhaustiveness was ensured)
1. **Topic extraction** — every sub-domain in the study guide became a discrete teachable concept; session count per domain is proportional to exam weight (D1 = 27% → most sessions).
2. **Coverage gap analysis** — each existing HTML course was rated per domain as **Full** (architect-depth), **Partial** (introduced, not exam-depth), or **Gap** (absent). Gap-flagged concepts (marked ★ in `SESSION-PLAN.md` / `CURRICULUM.md`) received dedicated from-scratch Professor sessions — e.g. Hooks, escalation/handoff, `fork_session`, Skills frontmatter, CI/CD `-p`/`--bare`, Batch API, `isError` structured errors, scratchpad/state persistence, confidence calibration, provenance.
3. **Prerequisite sequencing** — a dependency graph (in `CURRICULUM.md`) ensures no concept is taught before its prerequisite (e.g. agentic loop before coordinator/subagent).
4. **Integration scenarios** — cross-domain scenarios force synthesis after single-domain teaching, mirroring the exam.
5. **Mock-exam verification** — two timed mocks gate a Go/No-Go decision.

### 3.3 The resulting file system
*(See §6 for the full operational file map.)* The build produced an instruction file (`CLAUDE.md`), a topic map (`CURRICULUM.md`), a delivery plan (`SESSION-PLAN.md`), a conduct protocol (`ENGAGEMENT-PROTOCOL.md`), a live tracker (`PROGRESS.md`), and a persistent learner model (`LEARNER-MODEL.md`), supported by `courses\`, `practice\`, `mcq-practice\`, and `EXAM-DIGEST.md`.

---

## 4. How It Is Delivered

Delivery is interactive dialogue, not reading. The mechanics below are specified in full in `ENGAGEMENT-PROTOCOL.md`; this is the summary an AI needs to operate.

### 4.1 Two personas
- **`professor`** — teaches each concept with the mandatory four-beat probe: **Hook (analogy) → Why it matters → Evidence line → Open question**. Never opens with a definition; never advances past a concept while understanding reads "surface" or "absent" (switches to a different-domain analogy instead). Advances only when the learner explains the concept back, unprompted, in their own words.
- **`exam_coach`** — runs comprehension checks, scenario drills, integration scenarios, and timed mock exams. Retrieval, time pressure, structured feedback, gap targeting.

### 4.2 Session flow (37 sessions, 7 phases)
| Phase | Sessions | What happens |
|---|---|---|
| 0 — Orientation | 1 | Logistics + cold baseline diagnostic (5 Qs, one per domain) |
| 1 — D1 | 2–9 | Agentic Architecture (7 teach + 1 drill) |
| 2 — D2 | 10–15 | Claude Code Config (5 teach + 1 drill) |
| 3 — D3 | 16–21 | Prompt Engineering (5 teach + 1 drill) |
| 4 — D4 | 22–26 | Tool Design & MCP (4 teach + 1 drill) |
| 5 — D5 | 27–31 | Context Management (4 teach + 1 drill) |
| 6 — Integration | 32–34 | Cross-domain scenarios + conditional gap remediation |
| 7 — Mocks | 35–37 | Two timed mocks + Go/No-Go decision |

Each teaching session opens (except Session 1) with a **Spaced-Repetition Flash** — 2–3 questions drawn from the top of the learner model's Reinforcement Queue.

### 4.3 Sign-off and resume (the learner controls the day's end)
The course cannot finish in one session, so the learner ends each day deliberately:
- **Sign-off trigger** — the learner says **"Professor, that's it for today"** (or any clear equivalent: "I'm done for now", "let's continue later", "signing off", "pause here"). This fires the **Day's-End Ritual** (Session Type 6 in `ENGAGEMENT-PROTOCOL.md`): acknowledge in persona → bookmark the exact resume point (session #, concept #, mid-check flag) → update `GAPS.md`, `LEARNER-MODEL.md`, and the `PROGRESS.md` Resume Bookmark → give a 3-line spoken close → confirm sign-off. This is a deliberate checkpoint, **not** a generic context dump.
- **Resume trigger** — the learner says **"Professor, I'm back"** (or "let's resume", "start session N"). The AI reads the Resume Bookmark + `LEARNER-MODEL.md`, opens with a Spaced-Repetition Flash from the weakest queued concepts, then continues at the exact bookmark.

### 4.4 Cross-session memory (how the professor "remembers" the learner)
`LEARNER-MODEL.md` is the professor's persistent memory across the whole program. It answers, at any moment: where the learner is **weak** (🔴), **strong** (🟢/✅), what needs **reinforcement now** (a spaced-repetition queue), which concepts are **interlinked** (bridges to speak aloud — exactly what the exam's cross-domain scenarios test), and durable **insights** about how the learner learns. A **mastery state machine** governs transitions (⚪ Untested → 🔴 Weak → 🟡 Developing → 🟢 Strong → ✅ Exam-ready); promotion requires spaced recalls across different sessions; any miss drops a concept straight to 🔴. **Synthetic / self-driven runs never count toward mastery.**

---

## 5. Its Purpose

**The one objective: pass the CCA-F exam (≥ 720/1000).** Nothing in this project exists for any other reason. Concretely, "done" is defined by the Go/No-Go gate in `ENGAGEMENT-PROTOCOL.md`:
- Mock Exam #2 scaled-equivalent **≥ 720** → recommend booking the real exam.
- **680–719** → one more targeted remediation cycle, then re-assess.
- **< 680** → full re-drill of the two weakest domains before the next mock.

The program is judgment-first by design: the exam scores on a scaled basis and over-weights "what's wrong with this design?" scenario reasoning, so the program optimises for applied judgment and cross-domain synthesis, not definition recall.

---

## 6. Operational Sources of Truth

An AI conducting a session reads these in this order. This overview is the map; the files below are authoritative for mechanics and live state.

| File | Role | Updated by |
|---|---|---|
| `PROGRESS.md` | **Read FIRST.** Live session tracker + Resume Bookmark (where to start now) | After every session and at sign-off |
| `LEARNER-MODEL.md` | Persistent mastery model — weak/strong, reinforcement queue, interlink map, insight log | At every comprehension check and at sign-off |
| `CLAUDE.md` | AI system instructions — how to conduct sessions, persona switching, sign-off/resume, quality rules | Static (update only if methodology changes) |
| `SESSION-PLAN.md` | The 37-session ordered delivery plan, with scripted topics/analogies per session | Static reference |
| `CURRICULUM.md` | Full 5-domain topic map with sub-domains, prerequisite graph, and gap analysis | Static reference |
| `ENGAGEMENT-PROTOCOL.md` | Exact conduct of each session type; Day's-End Ritual; resume; memory mechanics | Static reference |
| `GAPS.md` | Running log of genuine misses (synthetic runs flagged, excluded from mastery) | When a real miss occurs |

**Supporting assets** (reference/practice, not session instructions): `courses\` (12 HTML courses — AI factual reference only, not learner reading), `practice\` (51 questions + 3 integration checkpoints), `mcq-practice\`, `EXAM-DIGEST.md`.

**State vs map:** if this overview and a live file disagree on current status, the live file (`PROGRESS.md` / `LEARNER-MODEL.md`) wins.

---

## 7. Known Open Items

*(Honest status as of this document. Re-check against `PROGRESS.md` for live status.)*

Open items are tracked as a risk register — each with probability, impact, mitigation, owner, trigger/due, and a pass/block rule.

| # | Risk | Prob | Impact | Mitigation | Owner | Trigger / Due | Block rule |
|---|---|---|---|---|---|---|---|
| R2 | Solo-learner motivation / dropout (no cohort, demanding job) — highest-probability failure mode | High | High | 5-week calendar + Completion Health metric + weekly checkpoint + provisional booking date | Ram | Tracked every session in PROGRESS.md | >10 days since last session → re-engagement check |
| R3 | Readiness over-stated by non-held-out / generated mocks | Med | High | Held-out, scenario-balanced Mock #2; Go/No-Go domain + scenario floors, not raw total | Exam Coach | Before Sessions 35/37 | No booking on total-score alone |
| R4 | Volatile facts drift (model IDs, hooks, MCP terms, scenario list) | Med | Med | Pre-mock + pre-booking verification vs live Anthropic docs / Skilljar | Ram + AI | Before each mock + booking | Verify before booking |
| R5 | Mastery untrusted — only synthetic baselines exist; program at 0/37 | High (now) | Med | Genuine 10-question Session 1 diagnostic before any mastery is trusted | Exam Coach | Session 1 | No "ready" claim from synthetic data |
| R6 | Memory updates skipped (manual discipline) → stale learner model | Med | Med | Mandatory Session-End Update Checklist (ENGAGEMENT-PROTOCOL.md) every session | AI | Every session end | — |
| R7 | `mcq-practice` app referenced but NOT built (spec only) | Low | Med | Marked spec-only; excluded from the readiness path until implemented | Ram | — | Not a readiness component until built |
| R8 | Partner free-attempt access unconfirmed | Low | Low | Verify at `partnerportal.anthropic.com` with Infosys email before paying | Ram | Before booking | — |

**Verified against the official exam guide (2026-06-26):** the exam has **6 scenarios** (not 8 — community guide was wrong) and the official domain numbering is D1 Agentic (27%) · D2 Tool Design & MCP (18%) · D3 Claude Code Config (20%) · D4 Prompt Engineering (20%) · D5 Context (15%). An official **practice exam** exists on Skilljar (prefer it for Mock #1). Question count/time are not stated in the guide — treat "60 Q / 120 min" as third-party until the practice exam confirms.

**Already applied:** documentation-precision patches (`--bare` vs `-p`; `allowed-tools`; `isError` channel; Task tool note) across the relevant sessions and `CURRICULUM.md`; Go/No-Go floors, adaptive path, session-end checklist, and Completion Health added. **Built:** held-out 2×60 mock bank (`practice/held-out-mocks/`); 35 per-concept comprehension rubrics (`COMPREHENSION-RUBRICS.md`). `SCENARIO-8_Agentic-AI-Tools.md` retained as optional Agent-SDK practice only (NOT an exam scenario).
