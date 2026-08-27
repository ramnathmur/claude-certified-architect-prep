# CCDV-F — Roadmap

**Status:** ⭐ **ACTIVE — this is the next exam.** **Phase 0 closed 2026-08-19** — the official guide
(v1.0, July 2026) is filed and reconciled.
**Now in:** the regeneration plan's Stage 9 (see the superseded-note further down this file) — all 34
chapters authored 2026-08-25 (Stage 6 complete); Mock Paper 1 generated 2026-08-25, not yet sat.
*(Corrected 2026-08-26 via `/sync-up` — this line previously still said "Phase 1," three days after
this same file's own body recorded Phases 2–4 as superseded.)*
**Target date:** none. This plan gates on evidence, not calendar.
**Running alongside:** CCAR-P, kept warm — see "The parallel track".
**Teaching plan:** `Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md` — 34 chapters across all 25
published skills. Part I (chapters 1–5) delivered and gate-verified 2026-08-22, converted to HTML the
same day and approved by Ram (`Outputs/regeneration/html/`, committed `718da8f`, pushed). Chapters
6–10 authored 2026-08-22, gate-verification finished 2026-08-23: **all five confirmed PASS** — 6, 8, 9
clean; 10 clean after resolving a disguised negation-tricolon recurrence; 7 clean after five rounds
resolving two analogy-fidelity defects, with one final C14 finding (an unhedged transition sentence,
substance independently confirmed sound) closed as a Ram-approved documented exception rather than a
sixth round — see the exception note in `CCDV-F_Prose-Gate_v1.md` §3.3 and
`Outputs/regeneration/CCDV-F_Resume-Prompt_v2.md` for the full history. **Converted to HTML, verified,
and committed 2026-08-23** (`Outputs/regeneration/html/Ch06..10_*.html`, commit `e5142c7`, not pushed).
A same-day cycle-time audit found gate re-review costing more than HTML production; two fixes were
approved as standing process — see `CCDV-F_Prose-Gate_v1.md` §3.5 (checksum-gated calibration log) and
`CCDV-F_Regeneration-Plan_v1.md` §7 (Stage 6 authors now receive the gate document itself). **Chapter 11
authored and gate-verified 2026-08-23** — PASS with two Ram-approved documented exceptions (C5, C7,
round 2; not read by Ram himself, waived to keep the chapter moving — see
`CCDV-F_Regeneration-Plan_v1.md` Part III and the exception notes in `CCDV-F_Prose-Gate_v1.md` §3.3), not
yet converted to HTML. **A second cost audit ran 2026-08-23** (Ram-commissioned, independent agent) specifically on chapter
11's ~996k-token cost across 4 dispatches, and found and directly fixed two real waste sources: fix
rounds were being resumed from the full original drafting conversation instead of dispatched fresh
(286k tokens for 3 tool calls — new standing rule added), and the calibration control was reading the
full old Class-01.html every round (replaced with a ~77%-smaller fixture,
`CCDV-F_Calibration-Fixture_v1.md`). **The calibration-checksum bug is now fixed** — narrowed to hash
only §3.1–§3.3 — reversing the "leave it for now" call above; the audit applied it under a broader fix
mandate, the conflict was flagged, and Ram chose to keep it. C5/C7 were flagged as possibly
over-triggering on defensible prose (a real quality tradeoff, reported only, left unchanged). **Chapter 12 gate-verified 2026-08-23 — clean PASS, zero exceptions, 686,648 tokens total (−31% vs.
chapter 11's 995,986)** — the fixed process's first full validated run. **Chapter 13 hit a real process
overrun the same day** — round 2 returned FIX, not PASS, and a second fix plus a third full blind
review were dispatched anyway instead of stopping per the gate's own 2-round cap; running total reached
~820,000 tokens (near chapter 11's unoptimized cost) before Ram interrupted directly. **Fixed:**
`CCDV-F_Prose-Gate_v1.md` §3.5's Rounds rule now makes the 2-round cap unconditional — FIX or FAIL on
round 2 both stop, no discretion to extend, and any round beyond 2 is Ram's call, not another agent
dispatch. See `CCDV-F_Regeneration-Plan_v1.md` Part III for the full account. **Chapter 13 closed out
2026-08-23** — Ram trusted the self-verified fix rather than commission a third review. **Chapter 14 hit
its own round cap the same day** — round 2 came back FAIL (a zero-tolerance C14 hit, notably inside the
self-test itself rather than the teaching prose, plus a C7+C13 bucket FAIL). Per the corrected rule, no
third round was dispatched. **Closed out 2026-08-24** — shown the exact contradiction verbatim, Ram
waived both round-2 findings without a fix, the same waiver pattern as chapters 11 and 13, explicitly
accepting that the self-test's contradictory "launches the same server automatically" phrasing stays
live against the chapter's own launch/spawn vs. host/reach split. **Chapters 11–14 converted to HTML
2026-08-24** — four parallel agents, one plan specified in full first, byte-identical CSS/JS to the
chapters 6–10 template, full prev/next chain verified Ch10 through Ch14 (not committed). One real gap
found in the process: chapter 13's self-test markdown had no answer key at all; a key was derived from
the chapter's own stated decision rule and flagged for Ram to spot-check, not silently invented.
**Chapter 15 ("Workflow or agent") authored and gate-verified 2026-08-24** — round 1 FAIL on three
non-zero-tolerance checks (C7 unsourced superlative, C9 rhetorical question, C13 fact-free screen),
fixed by a fresh agent, round 2 clean PASS with all 14 checks clear including all four zero-tolerance
ones. **Chapter 16 ("Who runs the loop") authored 2026-08-24** — round 1 FIX on one C5 finding, fixed by
a fresh agent; **round 2 review was skipped at Ram's explicit request** ("skip the reviews and just
finish generating the chapters"), so chapter 16 carries one applied fix but is not independently
gate-confirmed. **Chapters 17–20 authored 2026-08-24 with no gate review at all**, per a further explicit
instruction ("complete 17 to 20 without the reviews") — Ch17 "Building the loop by hand" (2,215 words),
Ch18 "State that outlives a turn" (2,705 words), Ch19 "Where the human stands" (2,206 words), Ch20
"Claude Code as a governed agent" (2,900 words). Each author agent received the full prose gate and
pedagogy design and self-audited its own draft (contrast-pair counts, em-dash density, analogy-fidelity
tables checked against self-tests) before finishing, but none of chapters 16–20 has been independently
blind-reviewed. Chapter 20's streaming-mode sub-topic has confirmed zero corpus content across every
module transcript and source pack — the chapter states this honestly rather than inventing mechanics.
**Chapters 21–25 authored 2026-08-24, same no-review instruction** — Ch21 "Three places a durable
instruction can live" (3,763 words, 9 sub-topics, the widest chapter in the course), Ch22 "The same
model, five front doors" (3,070 words, the thinnest-corpus chapter — "Claude Desktop" appears once in
381k characters of transcript, sourced almost entirely from live-fetched docs), Ch23 "Contracts inside
your own application" (2,623 words, deliberately reframed away from chapter 29's future security
argument onto a reliability/detectability argument, verified by the author), Ch24 "What an application
remembers" (2,589 words, honestly states that Agent SDK sessions and the Claude Code CLI session share
the same file-based storage by default rather than forcing a clean boundary the source doesn't support),
Ch25 "Sending Claude things that are not text" (2,120 words, delivers two full worked token-arithmetic
walkthroughs per the brief's explicit must-land instruction). **Chapters 26–30 authored 2026-08-24, same
no-review instruction, opening "Part VI — Proving it holds, and defending it"** — Ch26 "Defining done
before you build it" (1,868 words, held tight per its own explicit "zero owned sub-topics, first thing
to cut" warning), Ch27 "Finding where it broke" (2,094 words, stops cleanly at isolation), Ch28
"Failures you can wait out, failures you cannot" (1,551 words, refusals taught as fail-fast and never
retried, distinct from the retriable/terminal fork), Ch29 "Untrusted content and the action boundary"
(3,401 words, discloses the confidentiality/integrity vocabulary gap explicitly rather than attributing
CIA-triad language to Anthropic, and caught+fixed a real self-test bug — an item with 3 true options
against a stated "select 2" count), Ch30 "Layered guardrails" (1,756 words, hedges its Tier-B evidence —
a reported 24-of-25 exfiltration-success figure — rather than presenting it as a fixed spec number).
**Chapters 31–34 authored 2026-08-25, same author-only instruction, completing the course** — Ch31
"Identity, secrets, and the reviewer's three questions" (2,602 words, densest chapter at 9 must-land
sub-topics), Ch32 "From business requirement to functional and infrastructure requirement" (1,800
words + 8–10-item self-test, tripled per the Domain-2-substitution rule — resolves both must-land
open questions: solution architecture is the guide's named second input source alongside business
requirements, and "infrastructure requirement" is the narrower practitioner term inside the broader
"non-functional requirement" umbrella), Ch33 "Reading and reviewing code you did not write" (1,887
words, one owned sub-topic at full depth), Ch34 "Changing a live system without breaking it" (2,279
words + 10-item self-test, tripled — **the final chapter of the course**, all four life-cycle phases
explicit, model-drift/eval-regression as its stated novel contribution). **All 34 chapters of the
CCDV-F course are now authored — course-completion milestone reached 2026-08-25.**

**Chapters 15–18 converted to HTML 2026-08-25, on request.** Ch17 and Ch18 had never been reviewed at
all, so Ram had them gate-reviewed first: Ch17 round 1 FAILed (zero-tolerance C3 + C1 over-budget),
fixed and round 2 clean PASS; Ch18 round 1 returned FIX (one C13 gap), fixed and round 2 clean PASS —
both now gate-verified, same standing as chapters 1–15. Four parallel agents then built the HTML,
copying Ch14's `<style>`/`<script>` byte-for-byte and adding one new SVG diagram each (Ch15 a
workflow/agent/hierarchy decision tree, Ch16 a model/loop/tool-execution ownership grid, Ch17 a
register/scope/iterate/exit pipeline, Ch18 a four-panel memory-scope comparison). Ch14's forward nav
link was updated from a disabled placeholder to a live link to Ch15, and the full Ch14→18 chain was
verified live in a browser (served over localhost, not `file://`) — all links resolve, no console
errors, self-tests including the multi-select items work correctly.

None of chapters 19–34 are converted to HTML, and none of 15–34 are committed; that and any further
review pass over 19–34 is Ram's call. `resume-prompt.md` now describes a superseded checkpoint
(chapters 31–34 pending) rather than the current state. Supersedes the 29-class syllabus this file
pointed to before 2026-08-22 — see the
superseded note ahead of Phase 2.

---

## Two things the guide changed

This roadmap was written before the exam guide arrived. Two of its premises were wrong, and both
corrections make the exam **more approachable**, not less. Recorded rather than quietly overwritten,
because they drove a day of planning.

### 1. The exam tests judgement, not code production

The earlier plan was built on "closed book means producing API code from recall." The guide's three
sample items — chosen to show "the style and cognitive level of the exam" — contain **no code at all**.
Each is a short scenario with four options, testing which approach fits a stated constraint. The
blueprint's own language runs on *principles, patterns, tradeoffs, decision criteria* across all 25
skills, and the format is multiple-choice / multiple-response: you select, you do not produce.

**This is much closer in shape to CCAR-F than to a coding test.** The consequence is Phase 2 below,
which shrinks from five artifacts and an unassisted-recall gate to what Anthropic actually
recommends — one application exercising several areas.

Closed book still matters, and three samples is thin evidence. So the assumption is made falsifiable
rather than just reversed: see the tripwire in Phase 4.

### 2. This is not the hardest of the four

The earlier read — "harder for Ram than the Professional-tier CCAR-P" — does not survive the
blueprint. Roughly **47% of the paper has real CCAR-F carry-over**, and another **13.6% is general
software engineering and solution work** that is not Claude-specific at all. See the table below.

What remains true: it is an engineer's exam, sat closed book, with real new ground in Security,
Application Design, and the Agent SDK. It is a serious exam requiring months of work. It is not the
wall the first draft described.

---

## The blueprint, and where Ram actually stands

Weights and skills are now **verified** from `sources/CCDV-F_Official-Exam-Guide_v1.0.pdf`. Item counts
are the weight applied to 53 items — arithmetic, not stated in the guide.

| Skill | % | ≈items | Standing |
|---|---|---|---|
| **Claude Application Design** | 8.6 | 4.6 | 🔴 **New.** Cross-interface instruction interpretation, content boundaries, schema design, session hygiene, plugins |
| **Software Engineering Foundations** | 7.4 | 3.9 | 🟢 **Professional ground.** REST, JSON, async, version control, SDLC, code review, refactoring. Needs exam-shaping, not learning |
| **Claude API Mechanics** | 6.8 | 3.6 | 🟠 **Mostly new.** Vision, thinking, third-party vendors, data access patterns. Batch-vs-sync already scored 100% on CCAR-F |
| **Technical Fundamentals** | 6.1 | 3.2 | 🔴 **New.** SDKs wrapping REST APIs, websockets |
| **Agent Construction with Claude** | 5.3 | 2.8 | 🔴 **New.** Agent SDK, custom loops and harnesses, **managed deployment self-hosted vs Anthropic-hosted**, hooks |
| **LLM Fundamentals** | 5.2 | 2.8 | 🟢 **Owned.** Plus newer surface: fast mode, adaptive thinking, effort levels |
| **Agent Patterns and Frameworks** | 4.9 | 2.6 | 🟠 **Partial.** Patterns owned; **Strands, LangGraph, PydanticAI are new** |
| **Prompt Engineering** | 4.6 | 2.4 | 🟢 **Owned.** CCAR-F `Domain-4_v2` |
| **Agent Architecture** | 4.5 | 2.4 | 🟢 **Owned.** Workflow-vs-agent, supervisor hierarchies, subagents — core CCAR-F |
| **Tool Implementation** | 4.4 | 2.3 | 🟢 **Owned.** CCAR-F `Domain-2_v2` |
| **Agentic Customization** | 4.1 | 2.2 | 🟠 **Partial.** Built-in vs custom vs Skills vs MCP tradeoffs |
| **Configuration Management** | 4.1 | 2.2 | 🟠 **Partial, and a documented weakness.** CLAUDE.md and settings.json overlap CCAR-F D3 — which he scored **0%** on. Model pinning, prompt versioning, plugin deps are new |
| **Context Engineering** | 3.8 | 2.0 | 🟢 **Owned.** CCAR-F `Domain-5_v2` |
| **Understanding Requirements** | 3.4 | 1.8 | 🟢 **Professional ground** |
| **AI Application Security** | 3.2 | 1.7 | 🔴 **New.** Prompt injection, jailbreak defence, PII, data leakage |
| **Claude Code Operation** | 3.1 | 1.6 | 🟠 **Partial, and a documented weakness.** The CLAUDE.md hierarchy is exactly the 0% objective |
| **Systems Life Cycle** | 2.8 | 1.5 | 🟢 **Professional ground** |
| **Cost and Token Management** | 2.8 | 1.5 | 🟠 **Partial.** Caching owned; cost modelling and check-pointing thinner |
| **Model Selection and Tradeoffs** | 2.7 | 1.4 | 🟢 **Owned** |
| **Debugging and Error Handling** | 2.6 | 1.4 | 🟠 **Partial.** Trace analysis and integration-vs-model isolation are new framing |
| **Output Handling** | 2.6 | 1.4 | 🟢 **Owned.** Extraction schemas scored 100% on CCAR-F |
| **Guardrails and Safe Deployment** | 2.3 | 1.2 | 🔴 **New** |
| **Identity, Secrets, and Key Management** | 1.6 | 0.8 | 🔴 **New** |
| **Claude Hooks** | 1.0 | 0.5 | 🔴 **New**, and it appears again under Agent Construction |

**Rough split:** 🟢 owned or professional ground ≈ 39% · 🟠 partial ≈ 22% · 🔴 new ≈ 39%.

### Build order — weight × gap, not weight alone

1. **Claude Application Design (8.6)** — biggest skill on the paper and entirely new
2. **Claude API Mechanics (6.8)** + **Technical Fundamentals (6.1)** — 12.9 points, mostly new
3. **Security and Safety, all four skills (8.1)** — no prior material at any depth
4. **Agent Construction with Claude (5.3)** — the Agent SDK specifics
5. **Configuration Management (4.1) + Claude Code Operation (3.1)** — only 7.2 points, but **this is
   the documented 0%**, and the CLAUDE.md-hierarchy question that cost marks on CCAR-F is named
   explicitly in both skill descriptions
6. **Software Engineering Foundations / Requirements / Life Cycle (13.6)** — cheapest points on the
   paper. Ram knows this material professionally; it needs shaping into exam form, not learning
7. Everything 🟢 — port and verify, do not rebuild

### The six CCAR-F 0% objectives, now placed against real skills

| CCAR-F 0% objective | Lands in | Weight |
|---|---|---|
| Claude Code configuration mechanism (CLAUDE.md / rules / Skills / hooks / settings) | Configuration Management + Claude Code Operation | 7.2% |
| Agentic review architecture — plan vs direct vs multi-phase | Agent Architecture | 4.5% |
| Misconfigured subagent spawning | Agent Architecture + Agent Construction | — |
| Dynamic subtask decomposition | Agent Patterns and Frameworks | 4.9% |
| Claude Code review configurations | Claude Code Operation | 3.1% |
| Context window optimisation | Context Engineering | 3.8% |

Between them they touch roughly **17% of the paper**. They stay first in the corpus queue.

---

## How this plan is paced

No target date. Each phase has an **exit gate** — a checkable condition, not a week number. A phase is
done when its gate passes and not before.

**One hard calendar item exists regardless:** CCAR-F expires **2027-08-18**. Free non-proctored renewal
if done on time, full exam at full price if it lapses.

---

## The parallel track — CCAR-P

CCAR-P stays warm, and the overlap holds up against the real blueprint:

| CCAR-P lesson | Min | Feeds CCDV-F |
|---|---|---|
| **Enterprise Integration & Production** | 158 | **Applications and Integration (33.1%)** — the largest domain. Front-load |
| **Responsible AI, Safety & Risk for Architects** | 114 | **Security and Safety (8.1%)** — all-new ground. Front-load |
| Claude Platform & Solution Design | 238 | Model Selection, Agent Architecture, Understanding Requirements |
| Team Enablement & Operational Productivity | 45 | Claude Code Operation |
| Stakeholder Engagement, Lifecycle & GTM | 178 | Systems Life Cycle only, loosely. Leave for last |

Notes from those lessons go in the **CCAR-P folder's** `notes/`. Anything that becomes a CCDV-F
decision rule is copied here with its provenance.

---

## The teaching track

Runs across Phases 1 and 3. Started 2026-08-20, ahead of the self-assessment, because Ram asked to be
taught rather than tested first.

**`Outputs/CCDV-F_Syllabus_v1.md`** is the plan: **29 classes covering all 25 published skills**,
sequenced by dependency rather than by weight, with a skill→class map and a status box per class. It
also records how classes run — concepts taught first, mock papers only after, one understanding check
per class answered in the student's own words.

**How it relates to the phases:**

- It **feeds Phase 1.** A taught class produces the same understanding the self-assessment is meant to
  locate, and turns the standing column above from inference into evidence.
- It **feeds Phase 3.** Each class covers exactly one published skill, so a taught class converts
  directly into that skill's corpus section. Teaching and corpus-writing are one pass, not two.
- It **does not replace Phase 4.** Mock papers stay gated behind the corpus, not behind the classes.

**Teaching voice is a standing instruction, given 2026-08-20.** Classes are taught as a professor
teaches: no section numbers, no weights, no source or transcript citations inside the teaching itself.
Those live in the syllabus. The first attempt showed the plumbing and was rejected for it.

**Status is tracked in the syllabus, not here.** One file carries class progress, the same way one file
carries scores.

---

## Phases

### ✅ Phase 0 — Unblock · **CLOSED 2026-08-19**

- [x] Official guide downloaded → `sources/CCDV-F_Official-Exam-Guide_v1.0.pdf` (v1.0, July 2026)
- [x] `EXAM-FACTS_v1.md` fully reconciled — mechanics, 8 domains, 25 skills with weights
- [x] "Applications and Integration" resolved — six named skills, 13.6 of its 33.1 points generic SE
- [x] Eval at 2.6% and Claude Code at 3.1% **confirmed correct as published**
- [x] "Accelerators & IP Contribution" confirmed **not on the blueprint** — 155 min of the prep path is
      partner enablement, not exam prep
- [x] Item structure confirmed **standalone**, each stating its own response count. No scenario blocks
- [x] Guide version and date recorded, quarterly re-check noted

**Two questions the guide does not answer** and that stay open: whether multiple-response items are
all-or-nothing (assume yes), and whether the score report goes below domain level.

### Phase 1 — Official path and self-assessment

The guide's own first prep instruction is to self-assess against every objective. That comes first —
it turns the standing column above from my inference into his evidence.

- [ ] **Self-assess against all 25 published skills**, one line each: confident / shaky / cold. Record
      in `notes/SELF-ASSESSMENT_v1.md`. This re-prioritises the build order above
- [ ] Work the prep path — **but skip "Accelerators & IP Contribution" (155 min)**, which is not on the
      blueprint. That cuts the path from 774 to 619 minutes
- [ ] Sit the three uncovered prerequisite courses: **Claude Code 101 · Claude Platform 101 · MCP:
      Advanced Topics.** All are recommended, none required — but MCP: Advanced Topics feeds a 10.6%
      domain and Claude Code 101 feeds the documented 0%
- [ ] One `notes/` file per lesson, written as decision rules
- [ ] Write a decision rule for each of the six carry-over 0% objectives

> **Gate 1.** The 25-skill self-assessment exists. Every blueprint lesson has a `notes/` file. Each of
> the six carry-over objectives has a written decision rule stating its discriminator.

> ⚠️ **Phases 2–4 superseded 2026-08-22.** The build-an-application, corpus, and mock-paper work below
> is now executed through `Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md`'s 10-stage process
> instead — its Stage 6 (author 34 chapters) replaces Phase 3's domain files, and its Stage 9
> (diagnostic pre-test, three weighted mocks, RECALL/CONCEPT miss log) replaces Phase 4. Phase 2's own
> reasoning (assisted building, one application not a portfolio) still holds and is unaffected. Left
> below as the historical record of that reasoning — the checkboxes are not being tracked as the
> active plan.

### Phase 2 — Build one application

**Right-sized to what the guide actually recommends**, which is one application, not a portfolio:

> *"Build and operate at least one Claude application that exercises the API, integrates one or more
> tools, applies basic prompt and context engineering, and includes simple security and evaluation
> practices."*

- [ ] **One Claude application** covering all five: the API (streaming, error handling, token
      accounting) · at least one tool · prompt and context engineering · a security control ·
      a simple eval
- [ ] Extend it with **one MCP server plus a client** — MCP Server Development is 2.1% and Agentic
      Customization another 4.1%, and the built-in-vs-custom-vs-Skill-vs-MCP tradeoff is far easier to
      answer once you have written one
- [ ] Try the **Agent SDK** on it, including a hook — Agent Construction is 5.3% and entirely new
- [ ] Everything surprising goes into the corpus as a decision rule, immediately

**Why this is smaller than the first draft.** The exam asks which approach fits a constraint, not what
the parameter is called. Building still matters — the tradeoff questions in Domains 1 and 8 are much
easier to answer from experience than from reading — but it is preparation, not the whole plan.
Assisted building is fine. The earlier unassisted-recall gate was answering a question this exam does
not ask.

> **Gate 2.** One application exists and runs, exercising API + tools + prompt/context + a security
> control + an eval. One MCP server and client exist. One Agent SDK agent with a hook exists.
> Every surprise encountered is written into the corpus.

### Phase 3 — Corpus

Runs alongside Phases 1–2. Quotas are now real, so this can start immediately.

- [ ] Eight `CCDV-F_Domain-N_v1.md` files, from `CCDV-F_Domain-Template_v1.md`, **one section per
      published skill** — the guide's 25 skills are the section structure, so numbering can be fixed
      permanently on day one
- [ ] Build in the order above: Application Design → API Mechanics + Technical Fundamentals →
      Security → Agent Construction → Config/Claude Code (the 0%) → generic SE → port the 🟢 skills
- [ ] Port CCAR-F `Domain-1,2,3,4,5_v2` into the skills that map, verifying rather than rebuilding
- [ ] Corpus index with a concept inventory, so coverage can be audited against the 25 skills

> **Gate 3.** Eight domain files, 25 skill sections, none marked `not created`. Every one of the six
> carry-over objectives has a section. Concept inventory complete.

### Phase 4 — Mock papers

- [ ] Generate with `prep with quiz/CCDV-F-Orchestration-Prompt_v1.md`, now quota'd to the real
      blueprint: 53 items at 14.7 / 33.1 / 3.1 / 2.6 / 16.8 / 11.0 / 8.1 / 10.6
- [ ] Target **≥8 scored papers**
- [ ] Log every miss to a skill section
- [ ] Insights Round every 3 scored papers
- [ ] Confirmed-weakness rule: a domain unambiguously weakest on two consecutive papers *by attempt
      date* gets a quota bump

> **Gate 4.** Eight or more scored papers, with the last three trending at or above the booking bar.

**The tripwire.** Every miss still gets tagged `RECALL` (knew the approach, could not recall a
specific) or `CONCEPT` (did not know which approach was right). It costs nothing and it makes the
judgement-shaped assumption falsifiable: **if `RECALL` misses exceed a quarter of all misses across
any three consecutive papers, the assumption was wrong** — the exam is more syntax-bound than the
samples suggest, and Phase 2 grows back to unassisted reps. Until that fires, plan for judgement.

### Phase 5 — Book and sit

- [ ] Re-verify `EXAM-FACTS_v1.md` against a fresh download of the guide — check for a version bump
      past v1.0. The guide states it may change without notice
- [ ] Miss corpus → mistake-pattern artifact, the way `CCA-Prep_Mistake-Patterns_v1.html` was built
- [ ] Trap sheet, setter's-eye
- [ ] Work the guide's three sample questions cold, late, as a style check
- [ ] Book Pearson VUE ($125) — cancel or reschedule up to 24 h before, inside that the fee is forfeit
- [ ] Log the real score report domain-by-domain. It feeds CCAR-P directly

> **Gate 5 — the booking gate.** Two **consecutive** papers in Exam Mode (no per-question feedback),
> both clean.
>
> ⚠️ **"Clean" still needs a number, and Ram has not set one.** Proposal, for sign-off: both papers at
> **≥800 estimated scaled** against the 720 line. Basis — on CCAR-F his mocks ran 835–955 scaled and
> the real sitting came in at 851, so mocks were roughly predictive rather than inflated.
> **Note the guide removes the domain-floor half of my earlier proposal:** section percentages "are
> not used to determine your pass or fail result," so a per-domain minimum would be a constraint the
> exam does not impose. Total scaled score only. **Confirm or replace the 800 before Phase 4 ends.**

---

## Standing rules

1. **Generate only from the corpus, and quota only from the guide.** Both are now available. The
   community sources turned out to be accurate, which is luck rather than vindication — the discipline
   stays.
2. **Attempt chronology, never paper numbering.** The CCAR-F log was corrupted twice by assuming paper
   number equalled attempt order.
3. **One source of truth for standing.** `prep with quiz/EXAM-LOG.md`.
4. **Multiple-response items are all-or-nothing until proven otherwise.** The guide does not say, and
   eight CCAR-F misses were majority-right answers scored zero. Note the one relief the guide does
   give: each item states how many responses to select.
5. **Effort follows weight.** There is no domain floor — a weak 2.6% domain cannot fail you on its own.
6. **Gates are pass/fail, not aspirational.** A gate that gets waived once stops being a gate.
7. **Re-download the guide quarterly.** v1.0 is the initial publication and it is explicitly subject to
   change.
