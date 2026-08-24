# CCAO-F Prep — Project Instructions

Global rules live in `~/.claude/CLAUDE.md`. Repo-wide rules live in `..\CLAUDE.md`. This file covers
only what is specific to CCAO-F.

## What this project is

Preparation for Anthropic's **Claude Certified Associate – Foundations** exam (code **CCAO-F**, $99).
Sibling folders: `..\CCAR-F - Claude Certified Architect Foundations\` — passed 2026-08-18 with
851/720, and the machinery template for every other folder here — and
`..\CCAR-P - Claude Certified Architect Professional\`.

## The altitude rule — the one thing that is different about this exam

CCAO-F is a **no-code, business-practitioner exam**. Anthropic's stated audience is operations,
marketing, project management, education and communications staff, and the exam is explicitly written
to need no API or coding experience.

Ram comes to it holding CCAR-F, which tested Claude Code, the Agent SDK, the Claude API and MCP.
**Every piece of ported CCAR-F material must be brought down a tier**, and material that assumes API
or SDK access must be dropped rather than simplified. A question about choosing a model for a
marketing team's summarisation workflow is not a question about model architecture, and answering it
at architect altitude is a way to get it wrong.

When porting or writing content, the test is: could someone who has never opened a terminal answer
this? If not, it is pitched wrong for this exam.

## Output folder

All deliverables go to `Outputs/` in this folder. Never to `C:\Claude Cowork\CLAUDE OUTPUTS\` — this
is project-scoped work.

## Source of truth — non-negotiable

| Question | The one file that answers it |
|---|---|
| What are the exam mechanics? | `EXAM-FACTS_v1.md` |
| What is Ram's current standing? | `prep with quiz/EXAM-LOG.md` |
| What study material exists? | `BACKGROUND-MATERIAL-INDEX_v1.md` |
| What happens next? | `ROADMAP.md` |

If any other file starts carrying scores or exam mechanics, delete it. The CCAR-F project lost a
month to a stale `academy/PROGRESS.md` that reported 45/60 and NO-GO long after the real figure was
57/60, and it produced a materially wrong artifact before anyone noticed.

## The verification rule

`EXAM-FACTS_v1.md` has two tables: VERIFIED and UNVERIFIED.

- **VERIFIED** requires an Anthropic-controlled source — anthropic.com, claude.com,
  anthropic-partners.skilljar.com, or pearsonvue.com/anthropic.
- **UNVERIFIED** is everything else, including every community certification guide.
- **Never generate a practice question, a domain quota, or a study plan from the UNVERIFIED table.**

Note the nuance specific to this exam: the CCAO-F community domain names are corroborated by the
official Academy lesson titles, and the claimed weightings track the official lesson minutes. That
raises confidence in the *domain list*. It does not promote the *percentages*, and quotas come from
percentages. Read against the domains; do not generate against the numbers.

## Corpus conventions (from Phase 2 onward)

- Domain files are named `CCAO-F_Domain-N_v1.md` and are the **only** permitted source for generated
  questions. Never generate from notes, from the web, or from memory.
- Each domain file carries: core-facts table · decision tables · exam scenarios with ✅ correct and
  ❌ wrong options · an explicit "Misconception" block per section.
- Write decision rules, not explanatory prose. The CCAR-F `_v2` files are the reference shape; see
  `prep with quiz/CCAO-F_Domain-Template_v1.md`.
- Section numbering is stable once assigned. Misses are logged by section, so renumbering breaks the
  miss history.

## Exam-log conventions

- One `## Paper N — SCORED YYYY-MM-DD` heading per sitting. Scores are read from `SCORED` headings and
  attempt dates, never from generation-entry status lines.
- **Attempt chronology, never file numbering.** The CCAR-F log was corrupted twice by assuming paper
  number equalled attempt order.
- Confirmed weakness = the same domain unambiguously weakest on two consecutive papers *by attempt
  date*. A tie fails the bar.
- Insights Round every 3 scored papers.
- `DASHBOARD-DATA.jsonl` gets one line per paper, matching `DASHBOARD-SCHEMA.md`.

## Carry-over habits — keep these visible

Behaviour-level habits that carried across all 64 documented CCAR-F misses, and will carry here:

1. Reaching for a workaround beside a mechanism instead of a narrow adjustment to it.
2. Losing multiple-response items by being majority-right — all-or-nothing scoring.
3. Choosing an option because of how it *sounds* — safer, more architected, more thorough — rather
   than because it matches the requirement the scenario actually states.

For this exam add a fourth, specific to sitting a tier below your own: **answering the question you
find interesting rather than the one on the page.** A product-selection item wants the product, not
the architecture behind it.

## File authoring

Use Write/Edit to author file content. Bash is for running commands.

## HTML artifacts

Paged with sticky top nav and prev/next — never one long scroll. Verify in a browser before calling
any artifact done.
