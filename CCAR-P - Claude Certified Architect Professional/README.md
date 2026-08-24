# Claude Certified Architect — Professional (CCAR-P) Prep

Preparation project for Anthropic's **Claude Certified Architect – Professional** exam, exam code
**CCAR-P**. Started 2026-08-18, the day CCAR-F was passed with 851 against a 720 pass line.

**Status:** parallel track — kept warm while **CCDV-F is the active exam** (decided 2026-08-19).
**Current phase:** Phase 0 — blocked on the official exam guide. See `ROADMAP.md`.

> **What "warm" means in practice.** The official video path runs alongside CCDV-F prep, but in a
> deliberate order: **Lesson 2 (Enterprise Integration & Production, 158 min) and Lesson 3
> (Responsible AI, Safety & Risk, 114 min) first**, because they feed CCDV-F's largest domain and its
> Security domain respectively. Lesson 4 (Stakeholder Engagement) feeds nothing in CCDV-F and waits.
> Notes from these lessons live in this folder's `notes/`; anything that becomes a CCDV-F decision
> rule gets copied there with its provenance.

## Read these in order

| File | What it holds |
|---|---|
| `EXAM-FACTS_v1.md` | Every exam mechanic, split into VERIFIED (Anthropic sources) and UNVERIFIED (community). **Start here.** |
| `ROADMAP.md` | The twelve-month plan, six phases, and the honest read on what this takes |
| `BACKGROUND-MATERIAL-INDEX_v1.md` | All study material, tiered 0–4, with live URLs |
| `prep with quiz/EXAM-LOG.md` | The single source of truth for scores once papers start |

## Folder layout

```
CCAR-P - Claude Certified Architect Professional/
├── README.md                          this file
├── CLAUDE.md                          project rules for Claude sessions
├── EXAM-FACTS_v1.md                   verified vs unverified exam mechanics
├── ROADMAP.md                         12-month phased plan
├── BACKGROUND-MATERIAL-INDEX_v1.md    tiered study material
├── sources/                           official PDFs — the exam guide goes here
├── notes/                             one file per official lesson, written as decision rules
├── Outputs/                           deliverables (HTML artifacts, trap sheets, reports)
└── prep with quiz/                    the engine
    ├── EXAM-LOG.md                    per-paper scores + Professor's Notes
    ├── DASHBOARD-DATA.jsonl           one line per paper, machine-readable
    ├── DASHBOARD-SCHEMA.md            the jsonl contract
    ├── CCAR-P_Corpus-Index_v1.md      corpus index + reconciliation checklist
    ├── CCAR-P_Domain-1..7_v1.md       domain corpus (stubs until Phase 0 closes)
    ├── CCAR-P-Orchestration-Prompt_v1.md   mock-exam generator
    └── mock-exams/                    generated papers
```

## Why the structure mirrors the Foundations project

The Foundations run produced a first-attempt pass because of four specific things, all of which are
reproduced here:

1. **One source of truth for standing.** `prep with quiz/EXAM-LOG.md`. The Foundations project had a
   stale `academy/` folder that reported 45/60 and NO-GO for a month after the real figure was 57/60,
   and it corrupted a generated artifact before it was caught.
2. **A domain corpus written as decision rules**, not prose — core facts, decision tables, ✅/❌ exam
   scenarios, explicit misconceptions. Questions get generated *only* from those files.
3. **A logged miss record.** Every wrong answer traced to a corpus section, so patterns surfaced
   instead of feeling like unrelated mistakes. Four recurring patterns accounted for 21 of 64 misses.
4. **A verification file that outranks community sources.** `EXAM-FACTS_v1.md` here; the Foundations
   equivalent caught a community guide claiming 8 scenarios when the real number is 6.

## What is deliberately not here yet

No practice questions, no domain content, no mock papers. Phase 0 has to close first — the domain
list and weightings currently rest on a community source that says on its own site it is not
affiliated with Anthropic. Generating a corpus against unverified quotas is exactly the failure this
project is structured to avoid.
