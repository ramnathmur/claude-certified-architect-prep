# CCAR-P Corpus Index

**Status:** empty. No domain files exist yet, by design.

Domain files are the only permitted source for generated questions. Creating them now would mean
naming them after domains that currently rest on a community source which states on its own site
that it is not affiliated with Anthropic. That is the exact failure mode this project is structured
to avoid, so the corpus starts after Phase 0 closes.

---

## Phase 0 reconciliation checklist

Run this the moment the official CCAR-P Exam Guide PDF lands in `../sources/`.

- [ ] **Domain list.** Record the real domain names and codes. Community source says seven:
      Integration · Solution Design & Architecture · Evaluation, Testing & Optimisation ·
      Governance, Safety & Risk Management · Stakeholder Communication & Lifecycle Management ·
      Claude Models, Prompting & Context Engineering · Developer Productivity & Operational
      Enablement. The names are corroborated by the official prep path's lesson titles; treat the
      *set* as likely and the *labels* as unconfirmed.
- [ ] **Weightings.** Community source says 19/17/16/14/14/13/7. Nothing official corroborates these.
      Question quotas come from the guide, never from that list.
- [ ] **Item count.** Community source says 63. Unverified.
- [ ] **Item structure.** Community source says standalone, not scenario-based. Anthropic's own FAQ
      says all four exams use "multiple choice and scenario-based multiple response questions."
      **These contradict.** The guide settles it. If scenarios exist, record how many are in the pool
      and how many are drawn per sitting — the Foundations answer was 6 in pool, 4 drawn, and the
      block structure changed how papers had to be generated.
- [ ] **Multiple-response scoring.** All-or-nothing, or partial credit? On Foundations it was
      all-or-nothing and cost eight marks. This single answer changes exam-day tactics more than any
      content fact.
- [ ] **Objective list.** The Foundations score report exposed 37 objectives — the right granularity
      to build against. Capture the published objectives per domain.
- [ ] **Guide version and date.** The Foundations guide moved to v1.0 in July 2026 and dropped a whole
      section. Record version + date here and re-check quarterly.
- [ ] Update `../EXAM-FACTS_v1.md`: move confirmed rows to VERIFIED, delete disproved rows, and note
      anything the guide states that neither source anticipated.

---

## Corpus files

Created in Phase 2, one per confirmed domain, from `CCAR-P_Domain-Template_v1.md`.

| File | Domain | Weight | Sections | Status |
|---|---|---|---|---|
| `CCAR-P_Domain-1_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAR-P_Domain-2_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAR-P_Domain-3_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAR-P_Domain-4_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAR-P_Domain-5_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAR-P_Domain-6_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAR-P_Domain-7_v1.md` | *pending Phase 0* | — | — | not created |

## Head starts — material that already exists

| Target domain | Existing asset | Where |
|---|---|---|
| Claude Models, Prompting & Context Engineering | Foundations `CCA-Prep_Domain-1,4,5_v2.md` | `..\..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\` |
| Evaluation, Testing & Optimisation | Eval Design Blueprint, ~13.5k words | `my blueprints\eval-blueprint\` |
| Solution Design & Architecture | AI-First Design Blueprint + PRD pipeline | `my blueprints\` |
| Developer Productivity & Enablement | Foundations `CCA-Prep_Domain-3_v2.md` (Claude Code config) | Foundations project |
| Governance, Safety & Risk | none — build from Tier 3 of `../BACKGROUND-MATERIAL-INDEX_v1.md` | — |
| Stakeholder Comms & Lifecycle | none written, but this is Ram's professional ground | — |
| Integration | none — the genuine stretch | — |

## Section numbering rule

Once a section number is assigned it never changes. Misses are logged by section, so renumbering
destroys the miss history — which is the asset that made the Foundations mistake-pattern analysis
possible.
