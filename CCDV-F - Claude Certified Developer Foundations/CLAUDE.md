# CCDV-F Prep — Project Instructions

Global rules live in `~/.claude/CLAUDE.md`. Repo-wide rules live in `..\CLAUDE.md`. This file covers
only what is specific to CCDV-F.

## What this project is

Preparation for Anthropic's **Claude Certified Developer – Foundations** exam (code **CCDV-F**, $125).
Sibling folders: `..\CCAR-F - Claude Certified Architect Foundations\` — passed 2026-08-18 with
851/720, and the machinery template for every other folder here — plus
`..\CCAR-P - Claude Certified Architect Professional\` and
`..\CCAO-F - Claude Certified Associate Foundations\`.

## The item-shape rule — the one thing that decides how content is written

The official guide's three sample items — chosen to show "the style and cognitive level of the
exam" — are all the same shape: **a short scenario that states a constraint, then four options, no
code anywhere.** Every wrong option is a legitimate technique that does not match the stated
constraint. The blueprint's 25 skills are written in the language of principles, patterns, tradeoffs
and decision criteria throughout, and the format is multiple-choice / multiple-response — the
candidate selects, never produces.

**So: write for judgement, not syntax.** Every corpus section states a decision and its discriminator.
Code belongs in a section only where the decision is *about* the code — schema shape, defensive
parsing, error-handling strategy — and even there the question is which approach, not what the
parameter is called.

The exam is still **closed book** — no editor, no docs, no assistant — so nothing can be looked up on
the day. That makes coverage matter; it does not make syntax drills the right preparation.

**The assumption is falsifiable, not assumed.** Every mock miss is tagged `RECALL` or `CONCEPT`. If
`RECALL` misses exceed a quarter of all misses across three consecutive papers, this rule is wrong and
`ROADMAP.md` Phase 2 grows back to unassisted reps. Until then, plan for judgement.

**Phase 2 building may be assisted.** The earlier instruction not to help with it was answering a
question this exam does not ask. The point of building is the tradeoff intuitions in Domains 1 and 8,
which come from having shipped the thing — not from having typed it unaided.

## Output folder

All deliverables go to `Outputs/` in this folder. Never to `C:\Claude Cowork\CLAUDE OUTPUTS\` — this is
project-scoped work.

## Source of truth — non-negotiable

| Question | The one file that answers it |
|---|---|
| What are the exam mechanics? | `EXAM-FACTS_v1.md` |
| What is Ram's current standing? | `prep with quiz/EXAM-LOG.md` |
| What study material exists? | `BACKGROUND-MATERIAL-INDEX_v1.md` |
| What happens next? | `ROADMAP.md` |
| What is being taught, in what order, and how far has it got? | `Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md` |
| What did previous generation runs learn the hard way? | `prep with quiz/GENERATION-INTELLIGENCE.md` |

If any other file starts carrying scores or exam mechanics, delete it. The CCAR-F project lost a month
to a stale `academy/PROGRESS.md` that reported 45/60 and NO-GO long after the real figure was 57/60,
and it produced a materially wrong artifact before anyone noticed.

## The verification rule

`EXAM-FACTS_v1.md` has two tables: VERIFIED and UNVERIFIED.

- **VERIFIED** requires an Anthropic-controlled source — anthropic.com, claude.com,
  anthropic-partners.skilljar.com, or pearsonvue.com/anthropic.
- **UNVERIFIED** is everything else, including every community certification guide.
- **Never generate a practice question, a domain quota, or a study plan from the UNVERIFIED table.**

**As of 2026-08-19 this is settled.** The official guide v1.0 is filed at
`sources/CCDV-F_Official-Exam-Guide_v1.0.pdf` and `EXAM-FACTS_v1.md` is fully VERIFIED — 8 domains, 25
skills, all with published weights. The community sources turned out to be transcribing this document
accurately. The discipline stays anyway; being right by luck is not the same as being sourced.

Re-download the guide quarterly. It is v1.0, the initial publication, and states it is "subject to
change without notice." The CCAR-F guide moved to v1.0 mid-prep and silently dropped a section.

## Corpus conventions (from Phase 3 onward)

> **Superseded 2026-08-22 (noted here 2026-08-26 via `/sync-up`).** The 8-domain-file plan below was
> replaced by the regeneration approach: 34 authored chapters, each carrying its own self-test items,
> are now the question corpus — see `Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md` and
> `prep with quiz/mock-exams/README.md`. The domain files below do not exist and are not planned. Left
> here as the historical record of the original plan's reasoning.

- Domain files are named `CCDV-F_Domain-N_v1.md` and are the **only** permitted source for generated
  questions. Never generate from notes, from the web, or from memory.
- Each domain file carries: core-facts table · decision tables · exam scenarios with ✅ correct and ❌
  wrong options · an explicit "Misconception" block per section.
- Write decision rules, not explanatory prose. See `prep with quiz/CCDV-F_Domain-Template_v1.md`.
- **Sections follow the guide's 25 published skills**, numbered `N.M` in the guide's own order. That
  numbering is permanent from day one, which is what makes the miss log durable.
- **Every stem carries a constraint.** All three official samples do. A stem with no constraint has no
  correct answer, only a preferred one.
- Section numbering is stable once assigned. Misses are logged by section, so renumbering breaks the
  miss history.

## Exam-log conventions

- One `## Paper N — SCORED YYYY-MM-DD` heading per sitting. Scores are read from `SCORED` headings and
  attempt dates, never from generation-entry status lines.
- **Attempt chronology, never file numbering.** The CCAR-F log was corrupted twice by assuming paper
  number equalled attempt order.
- Confirmed weakness = the same domain unambiguously weakest on two consecutive papers *by attempt
  date*. A tie fails the bar.
- **Every miss is tagged `RECALL` or `CONCEPT`.** This is the tripwire on the item-shape rule above,
  not the main diagnostic. See `prep with quiz/EXAM-LOG.md` convention 8.
- **D3 (3.1%) and D4 (2.6%) are 1–2 items each** and can never trigger a confirmed-weakness quota bump.
- Insights Round every 3 scored papers.
- `DASHBOARD-DATA.jsonl` gets one line per paper, matching `DASHBOARD-SCHEMA.md`.

## Carry-over weaknesses — keep these visible

Six objectives scored 0% on the real CCAR-F paper, and unlike the CCAO-F case, **all six sit inside
CCDV-F scope**. Two had been open in the mock corpus for weeks (the `.claude/rules/`
configuration-mechanism reflex, and plan-mode vs direct execution). All six are listed at the end of
`BACKGROUND-MATERIAL-INDEX_v1.md`. They belong in the first corpus files written.

Behaviour-level habits that carried across all 64 documented CCAR-F misses, and will carry here:

1. Reaching for a workaround beside a mechanism instead of a narrow adjustment to it.
2. Losing multiple-response items by being majority-right — all-or-nothing scoring.
3. Choosing an option because of how it *sounds* — safer, more architected, more thorough — rather than
   because it matches the requirement the scenario actually states.

## File authoring

Use Write/Edit to author file content. Bash is for running commands.

## HTML artifacts

Paged with sticky top nav and prev/next — never one long scroll. Verify in a browser before calling any
artifact done.
