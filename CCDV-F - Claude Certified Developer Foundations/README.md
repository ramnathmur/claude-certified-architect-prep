# Claude Certified Developer — Foundations (CCDV-F) Prep

Preparation project for Anthropic's **Claude Certified Developer – Foundations** exam, exam code
**CCDV-F**, $125. Started 2026-08-19.

**Status:** ⭐ **ACTIVE — this is Ram's next exam**, decided 2026-08-19.
**Current phase:** **Phase 1.** Phase 0 closed 2026-08-19 — the official guide (v1.0, July 2026) is
filed at `sources/CCDV-F_Official-Exam-Guide_v1.0.pdf` and fully reconciled. **Phases 2–4's build/
corpus/mock-paper work now runs through `Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md` instead
— see `ROADMAP.md` for how the two relate.** Part I of the regenerated material (chapters 1–5) is
delivered and gate-verified as of 2026-08-22.
**Pacing:** no target date. The plan gates on evidence, phase by phase.
**Alongside:** CCAR-P is kept warm — its Integration and Responsible-AI lessons feed this exam and are
front-loaded for that reason.

> **The guide corrected two things this project believed.** The exam tests **judgement, not code
> production** — all three official sample items are scenario-plus-four-options with no code at all —
> and it is **not the hardest of the four**: roughly 47% of the paper has real CCAR-F carry-over and
> another 13.6% is generic software engineering that favours Ram's background. Both corrections are
> recorded in `EXAM-FACTS_v1.md` §4 and `ROADMAP.md`, not quietly overwritten.
>
> It remains a serious exam: closed book, 53 items in 120 minutes, with real new ground in Application
> Design, Security, and the Agent SDK.

## Read these in order

| File | What it holds |
|---|---|
| `EXAM-FACTS_v1.md` | **Start here.** Every exam mechanic, the full 8-domain / 25-skill blueprint with weights, what the sample items reveal about item shape, and §4's record of what the guide corrected |
| `ROADMAP.md` | Five gate-paced phases, the skill-by-skill standing table, and the build order by weight × gap |
| `BACKGROUND-MATERIAL-INDEX_v1.md` | All study material, tiered 0–4, with live URLs |
| `prep with quiz/EXAM-LOG.md` | The single source of truth for scores once papers start |

## Folder layout

```
CCDV-F - Claude Certified Developer Foundations/
├── README.md                          this file
├── CLAUDE.md                          project rules for Claude sessions
├── EXAM-FACTS_v1.md                   verified mechanics + the full blueprint
├── ROADMAP.md                         five-phase plan
├── BACKGROUND-MATERIAL-INDEX_v1.md    tiered study material
├── sources/                           official PDFs — the exam guide goes here
├── notes/                             one file per official lesson, written as decision rules
├── Outputs/                           deliverables (HTML artifacts, trap sheets, reports)
└── prep with quiz/                    the engine
    ├── EXAM-LOG.md                    per-paper scores + Professor's Notes
    ├── DASHBOARD-DATA.jsonl           one line per paper, machine-readable
    ├── DASHBOARD-SCHEMA.md            the jsonl contract
    ├── CCDV-F_Corpus-Index_v1.md      corpus index + reconciliation checklist
    ├── CCDV-F_Domain-Template_v1.md   the shape every domain file must take
    ├── CCDV-F_Domain-1..8_v1.md       domain corpus (not created until Phase 0 closes)
    ├── CCDV-F-Orchestration-Prompt_v1.md   mock-exam generator
    └── mock-exams/                    generated papers
```

## Why the structure mirrors the other exam folders

The CCAR-F run produced a first-attempt pass at 851 because of four specific things, all reproduced
here:

1. **One source of truth for standing.** `prep with quiz/EXAM-LOG.md`. The CCAR-F project had a stale
   `academy/` folder reporting 45/60 and NO-GO for a month after the real figure was 57/60, and it
   corrupted a generated artifact before it was caught.
2. **A domain corpus written as decision rules**, not prose. Questions get generated *only* from those
   files.
3. **A logged miss record.** Every wrong answer traced to a corpus section, so patterns surfaced
   instead of feeling like unrelated mistakes. Four recurring patterns accounted for 21 of 64 misses.
4. **A verification file that outranks community sources.** `EXAM-FACTS_v1.md` here.

One thing is added for this exam: a **build phase**. Reading closed the gap on CCAR-F because that exam
tested judgement about systems. This one tests whether you can produce code from recall with no
assistant in the room, and no amount of reading substitutes for having written it.

## What is not here yet

**Superseded, 2026-08-26 (via `/sync-up`).** This section described the state as of 2026-08-22. Since
then: all 34 course chapters are authored (2026-08-25, each carrying its own self-test items as the
question corpus) and Mock Paper 1 has been generated (2026-08-25, not yet sat) — see `ROADMAP.md` for
the live stage. What's still genuinely missing: chapters 15–34 have not been converted to HTML yet,
and no mock paper has been sat or scored.

Three things the guide settled that change how the corpus gets built:

- **"Applications and Integration" (33.1%) is six named skills**, and 13.6 of its 33.1 points are
  generic software engineering, requirements and life-cycle work — not Claude-specific at all.
- **Eval at 2.6% and Claude Code at 3.1% are correct as published.** Anthropic teaches both at length
  and tests them lightly as standalone domains. Lesson minutes do not predict exam weight.
- **"Accelerators & IP Contribution" is not on the blueprint** — 155 minutes of the official prep path
  is partner enablement. Skipping it cuts the path from 774 to 619 minutes.
