# Claude Certified Associate — Foundations (CCAO-F) Prep

Preparation project for Anthropic's **Claude Certified Associate – Foundations** exam, exam code
**CCAO-F**, $99. Started 2026-08-19.

**Status:** deferred. CCDV-F is the active exam as of 2026-08-19.
**Current phase:** Phase 0 — blocked on the official exam guide. See `ROADMAP.md`.

> **Read the value note in `ROADMAP.md` first.** CCAO-F sits *below* the CCAR-F credential Ram already
> holds and does not extend it. Whether to sit it at all is an open Phase 0 decision, not an
> assumption — and it is not being made now: CCDV-F is the active exam with CCAR-P warm alongside it.

## Read these in order

| File | What it holds |
|---|---|
| `EXAM-FACTS_v1.md` | Every exam mechanic, split into VERIFIED (Anthropic sources) and UNVERIFIED (community). **Start here.** |
| `ROADMAP.md` | The four-phase plan, the honest read on value and effort, and what carries over from CCAR-F |
| `BACKGROUND-MATERIAL-INDEX_v1.md` | All study material, tiered 0–4, with live URLs |
| `prep with quiz/EXAM-LOG.md` | The single source of truth for scores once papers start |

## Folder layout

```
CCAO-F - Claude Certified Associate Foundations/
├── README.md                          this file
├── CLAUDE.md                          project rules for Claude sessions
├── EXAM-FACTS_v1.md                   verified vs unverified exam mechanics
├── ROADMAP.md                         four-phase plan
├── BACKGROUND-MATERIAL-INDEX_v1.md    tiered study material
├── sources/                           official PDFs — the exam guide goes here
├── notes/                             one file per official lesson, written as decision rules
├── Outputs/                           deliverables (HTML artifacts, trap sheets, reports)
└── prep with quiz/                    the engine
    ├── EXAM-LOG.md                    per-paper scores + Professor's Notes
    ├── DASHBOARD-DATA.jsonl           one line per paper, machine-readable
    ├── DASHBOARD-SCHEMA.md            the jsonl contract
    ├── CCAO-F_Corpus-Index_v1.md      corpus index + reconciliation checklist
    ├── CCAO-F_Domain-Template_v1.md   the shape every domain file must take
    ├── CCAO-F_Domain-1..7_v1.md       domain corpus (not created until Phase 0 closes)
    ├── CCAO-F-Orchestration-Prompt_v1.md   mock-exam generator
    └── mock-exams/                    generated papers
```

## Why the structure mirrors the other exam folders

The CCAR-F run produced a first-attempt pass at 851 because of four specific things, all reproduced
here:

1. **One source of truth for standing.** `prep with quiz/EXAM-LOG.md`. The CCAR-F project had a stale
   `academy/` folder reporting 45/60 and NO-GO for a month after the real figure was 57/60, and it
   corrupted a generated artifact before it was caught.
2. **A domain corpus written as decision rules**, not prose. Questions get generated *only* from
   those files.
3. **A logged miss record.** Every wrong answer traced to a corpus section, so patterns surfaced
   instead of feeling like unrelated mistakes. Four recurring patterns accounted for 21 of 64 misses.
4. **A verification file that outranks community sources.** `EXAM-FACTS_v1.md` here.

## What is deliberately not here yet

No practice questions, no domain content, no mock papers. Phase 0 has to close first.

The evidence for the CCAO-F domain list is genuinely stronger than it was for CCAR-P — six of the
seven community domain names are the official Academy lesson titles verbatim, and the claimed
weightings track the official lesson minutes closely. The arithmetic is laid out in
`EXAM-FACTS_v1.md`. That is good enough to justify reading against those domains. It is not good
enough to set question quotas, because a three-point weighting error is two items on a 60-item paper
and the guide is one sign-in away.
