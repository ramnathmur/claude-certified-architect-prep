# sources/

Official, authoritative documents only. Anything from a community site belongs in `../notes/` with its
provenance recorded, never here.

## Held

| File | Version | Filed |
|---|---|---|
| `CCDV-F_Official-Exam-Guide_v1.0.pdf` | **v1.0, effective July 2026** | 2026-08-19 — reconciled into `../EXAM-FACTS_v1.md` |
| `course-transcripts/` | — | **All four examinable modules captured 2026-08-19** — ~381,000 chars, 83 screens, verified against each module's self-declared screen count. M5 skipped (not on the blueprint). See that folder's README for method and checkpoint-capture gaps |

## Still wanted

| # | File | Where to get it |
|---|---|---|
| 1 | Certification Terms and Conditions (PDF) | Anthropic Academy → CCDV-F certification page → the certifications page it links to. Partner Network sign-in |
| 2 | Anthropic Certification Exam Policy (PDF) | Same page |
| 3 | **Any revision superseding the held v1.0** | **Re-check quarterly.** The guide states it is "subject to change without notice" and v1.0 is the initial publication |

## Naming

`CCDV-F_Official-Exam-Guide_v<version>.pdf` — use the version printed in the document, not a sequence
number of your own. If the document carries no version, use its date:
`CCDV-F_Official-Exam-Guide_2026-08.pdf`.

Never overwrite a previous version. The CCAR-F guide moved from v0.1 to v1.0 and dropped a whole
section; having both files is what made that diff visible.

## What v1.0 settled — reconciled 2026-08-19

The three questions this folder existed to answer are answered. Full detail in `../EXAM-FACTS_v1.md`.

1. **"Applications and Integration" (33.1%)** is six named skills, and 13.6 of its 33.1 points are
   generic software engineering and solution work — REST, JSON, async, version control, SDLC, code
   review, refactoring, requirements, life-cycle frameworks.
2. **Eval at 2.6% and Claude Code at 3.1% are correct as published.** The prep-path lesson minutes
   simply do not track exam weight.
3. **"Accelerators & IP Contribution" is not on the blueprint at all** — 155 minutes of the official
   path is partner enablement, not exam preparation. Skip it.

Also settled: items are **standalone**, each stating its own response count (no scenario blocks), and
**no MCP specification revision is named** — the published MCP scope is conceptual, so spec-version
trivia is out of scope.

## When a new revision lands

Do not overwrite v1.0. File the new version alongside it, diff the two, then re-run the reconciliation
checklist in `../prep with quiz/CCDV-F_Corpus-Index_v1.md` and update `../EXAM-FACTS_v1.md`. Having
both files is what made the CCAR-F v0.1→v1.0 diff visible — that upgrade silently dropped a whole
section mid-prep.
