# Claude Certification Prep

Preparation projects for Anthropic's four Claude certifications. One folder per exam, each
self-contained with its own exam facts, roadmap, corpus and mock-exam engine.

| Folder | Exam | Price | Status |
|---|---|---|---|
| [`CCAR-F - Claude Certified Architect Foundations`](CCAR-F%20-%20Claude%20Certified%20Architect%20Foundations/) | Claude Certified Architect – Foundations | $125 | ✅ **Passed 2026-08-18, 851/720**, first attempt. Renewal due 2027-08-18 |
| [`CCAR-P - Claude Certified Architect Professional`](CCAR-P%20-%20Claude%20Certified%20Architect%20Professional/) | Claude Certified Architect – Professional | $175 | Parallel track — kept warm, Integration + Safety lessons front-loaded |
| [`CCAO-F - Claude Certified Associate Foundations`](CCAO-F%20-%20Claude%20Certified%20Associate%20Foundations/) | Claude Certified Associate – Foundations | $99 | Deferred — whether to sit it at all is still open |
| [`CCDV-F - Claude Certified Developer Foundations`](CCDV-F%20-%20Claude%20Certified%20Developer%20Foundations/) | Claude Certified Developer – Foundations | $125 | ⭐ **ACTIVE — next exam.** **Phase 0 closed 2026-08-19**, guide v1.0 filed and reconciled. All 34 course chapters authored 2026-08-25 — see its own `ROADMAP.md` for the live stage |

Every folder opens with `README.md`, then `EXAM-FACTS_v1.md`, then `ROADMAP.md`.

---

## Exam guides — two held, one outstanding

*Updated 2026-08-26 via `/sync-up` — this section previously said "one held, two outstanding" and had
not caught up to CCAR-P obtaining its guide on 2026-08-25.*

**✅ CCDV-F:** the official guide (**v1.0, July 2026**) is filed at
`CCDV-F .../sources/CCDV-F_Official-Exam-Guide_v1.0.pdf` and fully reconciled. 8 domains, 25 skills,
all with published weights. That folder is no longer guessing.

**✅ CCAR-P:** the official guide (**v1.0, July 2026**) is filed at
`CCAR-P .../sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`, obtained 2026-08-25 via a third-party
repository's cited mirror of a real Anthropic S3 asset — not a direct Partner Academy login, but
independently verified byte-identical and internally consistent with a genuine Anthropic guide. 7
domains, 38 objectives, all with published weights, promoted to VERIFIED with that provenance caveat
attached. Full detail in that folder's `EXAM-FACTS_v1.md`. Re-confirming directly via Partner Academy
sign-in remains open but no longer blocking.

**⏸ CCAO-F:** still behind Claude Partner Network sign-in. Its `sources/README.md` names the exact
file. Not being worked right now, so not urgent — but the same sign-in that produced the other two
guides will produce this one too.

Until a guide lands for CCAO-F, that folder's domain list and weightings come from community sources
and are labelled UNVERIFIED. The CCAR-F run is why that labelling exists: a community guide stated the
exam drew 8 scenarios when the real number was 6, and the error reached generated practice material
before it was caught.

> **Worth recording:** for CCDV-F the community figures turned out to be **exactly right** — every
> domain weight, the item count, the fee, the pass mark. The sources were transcribing the real
> document. That is luck, not vindication: they were unverifiable at the time, and holding quotas until
> the guide arrived was still the right call.

---

## Sequencing — decided 2026-08-19

**⭐ CCDV-F — Developer Foundations is the next exam.** Ram's call, made 2026-08-19, overriding the
earlier CCAR-P-first recommendation. The plan is in
[`CCDV-F .../ROADMAP.md`](CCDV-F%20-%20Claude%20Certified%20Developer%20Foundations/ROADMAP.md).

Three things follow from it.

**No target date.** That roadmap paces on evidence, not calendar: every phase has an exit gate that is
a checkable condition rather than a week number, and Pearson VUE gets booked only when the final gate
passes. Rough shape if nothing stalls — Phases 0–1 are a few weeks, Phase 2 runs months, Phases 3–4
overlap its back half.

**The guide corrected two premises, both favourably.** The exam tests **judgement, not code
production** — all three official sample items are scenario-plus-four-options with no code — and it is
**not the hardest of the four**: roughly 47% of the paper has real CCAR-F carry-over and another 13.6%
is generic software engineering that favours Ram's background. The build phase is right-sized
accordingly, to the one application the guide itself recommends. Corrections are recorded in
`CCDV-F .../EXAM-FACTS_v1.md` §4, not quietly overwritten.

**CCAR-P runs in parallel, warm.** Two of its lessons pay for themselves twice and are front-loaded
for that reason: *Enterprise Integration & Production* (158 min) feeds CCDV-F's largest domain, and
*Responsible AI, Safety & Risk* (114 min) feeds its Security domain. The Stakeholder lesson feeds
nothing here and waits.

**CCAO-F is deferred**, and whether to sit it at all remains open — it is a tier below the CCAR-F
credential already held and does not extend it. See its roadmap.

**Also on the calendar regardless:** CCAR-F expires **2027-08-18**. Renewal is free and non-proctored
if done on time; lapsed means the full exam at full price.

---

## Repeatable procedures

[`sop/SOP_Academy-Course-Extraction_v1.md`](sop/SOP_Academy-Course-Extraction_v1.md) — pulling an
Anthropic Partner Academy prep path into local text. Established and verified on the CCDV-F path,
2026-08-19: four modules, 83 screens, ~381,000 characters, about six minutes once one Chrome
permission was set.

The finding that makes it work: **Academy modules are self-contained HTML, not video**, so a whole
module extracts in a single pass rather than being watched. Applies to CCAR-P and CCAO-F when their
turn comes.

## Why every folder has the same shape

The CCAR-F run produced a first-attempt pass at 851 against a 720 line. Four things did that, and each
new folder reproduces all four:

1. **One source of truth for standing** — `prep with quiz/EXAM-LOG.md`, and nothing else carries scores.
   The CCAR-F project had a stale `academy/` folder reporting 45/60 and NO-GO for a month after the real
   figure was 57/60, and it corrupted a generated artifact before anyone noticed.
2. **A domain corpus written as decision rules**, not prose. Practice questions are generated *only*
   from those files — never from notes, the web, or memory.
3. **A logged miss record**, every wrong answer traced to a corpus section. Four recurring patterns
   accounted for 21 of 64 documented misses; none of them were visible one miss at a time.
4. **A verification file that outranks community sources** — `EXAM-FACTS_v1.md`, split into VERIFIED and
   UNVERIFIED with a source on every line.

## Deployment

The CCAR-F Launchpad and course material are served from this repo.

- **GitHub:** https://github.com/ramnathmur/claude-certified-architect-prep
- **Vercel:** https://claude-certified-architect-prep.vercel.app

Root `index.html` is a hub linking into each exam folder. The CCAR-F Launchpad moved with its content
to `CCAR-F - Claude Certified Architect Foundations/index.html`, where all its relative links still
resolve. `Launch CCA Prep.bat` moved with it and still works from that folder.

---

**Part of:** [NEURAL HUB](https://course-landing-hub.vercel.app) — Educational Intelligence for
Practitioners
**Last updated:** 2026-08-19
