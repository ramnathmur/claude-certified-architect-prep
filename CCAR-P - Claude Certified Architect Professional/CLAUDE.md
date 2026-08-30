# CCAR-P Prep — Project Instructions

Global rules live in `~/.claude/CLAUDE.md`. This file covers only what is specific to this project.

## What this project is

Preparation for Anthropic's **Claude Certified Architect – Professional** exam (code **CCAR-P**).
Sibling folder: `..\CCAR-F - Claude Certified Architect Foundations\` — the Foundations run, passed
2026-08-18 with 851/720. Its machinery is the template for this one.

## Mock-exam engine — **built 2026-08-29**

`prep with quiz/CCAR-P-Orchestration-Prompt_v2.md` is the authority for how a paper is generated.
Read it before generating, auditing, or changing any paper. It supersedes v1, which ported the
Foundations feedback loop and left the item-fidelity half behind — the reasoning is in
`Outputs/CCAR-P_Mock-Exam-Engine-Audit_v1.md`.

The engine's parts: the orchestration prompt · four ledgers (`CCAR-P_Objective-Map_v1.md`,
`FACET-LEDGER.md`, `STEM-LEDGER.md`, `ARCHETYPE-LEDGER.md`) · `GENERATION-INTELLIGENCE.md` ·
`mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html` · `mock-exams/DASHBOARD.html` · `tools/run-gate.js`.

`..\sop\SOP_Mock-Exam-Engine_v1.md` remains the exam-agnostic methodology behind the engine. Where
the orchestration prompt and the SOP differ, **the orchestration prompt wins for this exam** — it was
written against CCAR-P's own guide and corpus, and two of its rules deliberately invert the SOP's
sibling-derived defaults.

### Two decisions recorded, both Ram's, 2026-08-29/30

1. **Item sourcing is full AUTHOR mode for every paper, including Paper 1.** A hybrid plan (Paper 1
   TRANSCRIBE, Papers 2–10 AUTHOR) was proposed first, but measurement showed the corpus's 79
   ready-made scenarios have the correct answer as the longest option 84% of the time — a verbatim
   Paper 1 would have been answerable by length alone, chance is ~33%. TRANSCRIBE was rejected
   entirely; Paper 1 shipped 2026-08-30 in AUTHOR mode, 0/63 key-longest above chance. This settles
   SOP §3.3 for this project.
2. **The objective map lives outside the corpus.** `CCAR-P_Objective-Map_v1.md` assigns all 78
   sections to the 38 official objectives without editing a single domain file, so corpus section
   numbering and content stay exactly as reviewed.

**The verification rule below still binds.** `EXAM-FACTS_v1.md`'s VERIFIED table now carries the real
weights and item count (promoted 2026-08-25, with the S3-mirror provenance caveat attached), which is
what makes generation legitimate. Nothing may still be generated from the UNVERIFIED table.

## Output folder

All deliverables go to `Outputs/` in this folder. Never to `C:\Claude Cowork\CLAUDE OUTPUTS\` —
this is project-scoped work.

## Source of truth — non-negotiable

| Question | The one file that answers it |
|---|---|
| What are the exam mechanics? | `EXAM-FACTS_v1.md` |
| What is Ram's current standing? | `prep with quiz/EXAM-LOG.md` |
| What study material exists? | `BACKGROUND-MATERIAL-INDEX_v1.md` |
| What happens next? | `ROADMAP.md` |

If any other file starts carrying scores or exam mechanics, delete it. The Foundations project lost a
month to a stale `academy/PROGRESS.md` that reported 45/60 and NO-GO long after the real figure was
57/60, and it produced a materially wrong artifact before anyone noticed.

## The verification rule

`EXAM-FACTS_v1.md` has two tables: VERIFIED and UNVERIFIED.

- **VERIFIED** requires an Anthropic-controlled source — anthropic.com,
  anthropic-partners.skilljar.com, or pearsonvue.com/anthropic.
- **UNVERIFIED** is everything else, including every community certification guide.
- **Never generate a practice question, a domain quota, or a study plan from the UNVERIFIED table.**

Precedent: on the Foundations run, a community guide stated the exam draws 8 scenarios. The real
number is 6. That error reached generated practice material. One community source currently states
CCAR-P has 63 standalone non-scenario items — Anthropic's own FAQ says all four exams use
"scenario-based multiple response questions", which contradicts it directly.

## Corpus conventions (from Phase 2 onward)

- Domain files are named `CCAR-P_Domain-N_v1.md` and are the **only** permitted source for generated
  questions. Never generate from notes, from the web, or from memory.
- Each domain file carries: core-facts table · decision tables · exam scenarios with ✅ correct and
  ❌ wrong options · an explicit "Misconception" block per section.
- Write decision rules, not explanatory prose. The Foundations `_v2` files are the reference shape.
- Section numbering is stable once assigned. Misses are logged by section, so renumbering breaks the
  miss history.

## Exam-log conventions

- One `## Paper N — SCORED YYYY-MM-DD` heading per sitting. Scores are read from `SCORED` headings and
  attempt dates, never from generation-entry status lines.
- **Attempt chronology, never file numbering.** The Foundations log was corrupted twice by assuming
  paper number equalled attempt order.
- Confirmed weakness = the same domain unambiguously weakest on two consecutive papers *by attempt
  date*. A tie fails the bar.
- Insights Round every 3 scored papers.
- `DASHBOARD-DATA.jsonl` gets one line per paper, matching `DASHBOARD-SCHEMA.md`.

## Carry-over weaknesses — keep these visible

Six objectives scored 0% on the real CCAR-F paper. Two had been open in the mock corpus for weeks
(the `.claude/rules/` configuration-mechanism reflex, and plan-mode vs direct execution). All six are
listed at the end of `BACKGROUND-MATERIAL-INDEX_v1.md`. They belong in the first corpus files written.

Behaviour-level habits that carried across all 64 documented Foundations misses, and will carry here:

1. Reaching for a workaround beside a mechanism instead of a narrow adjustment to it.
2. Losing multiple-response items by being majority-right — all-or-nothing scoring.
3. Choosing an option because of how it *sounds* — safer, more architected, more thorough — rather
   than because it matches the requirement the scenario actually states.

## File authoring

Use Write/Edit to author file content. Bash is for running commands.

## HTML artifacts

Paged with sticky top nav and prev/next — never one long scroll. Verify in a browser before calling
any artifact done.
