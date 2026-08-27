# CCAR-P Corpus Index

**Status:** Phase 0 reconciliation done 2026-08-25. **Phase 2 corpus complete 2026-08-25** — all seven
domain files exist, 78 sections carrying 79 exam scenarios and 158 tagged distractors.

> **Appended 2026-08-27:** §7.8 (Deterministic Enforcement — Hooks and Permission Rules), added after a
> cold review found hooks and `settings.json` absent from both the corpus and the Domain 7 lesson while
> being named explicitly in carry-over weakness #1, which scored 0% on the real CCAR-F paper. Facts are
> sourced from current Claude Code documentation. Numbering is append-only, so no miss history moved.
> The same review corrected `/memory` → `/context` in five places in Domain 7 (including an exam
> scenario's correct answer) and one distractor rationale in §1.5 that rested on "hub-and-spoke", which
> is not Anthropic's vocabulary.

Domain files are the only permitted source for generated questions. The domain list and weightings
are confirmed (see below), and the corpus now satisfies the orchestration prompt's Phase 0 preflight,
which aborts while any domain file is listed as not created.

**Companion teaching material.** Each domain also has a long-form lesson in `../Outputs/lessons/`
(`CCAR-P_Lesson-Domain-N_v1.md`, ~64,150 words total). Those are for learning and revision, written
to teach the mechanism behind each decision rule. **They are not a question source** — questions come
from the domain files in this folder and nowhere else.

---

## Phase 0 reconciliation checklist — closed 2026-08-25

Full detail and sourcing live in `../EXAM-FACTS_v1.md`. Summary:

- [x] **Domain list.** Confirmed — the same seven names the community source used: Solution Design &
      Architecture · Claude Models, Prompting & Context Engineering · Integration · Evaluation,
      Testing & Optimization · Governance, Safety & Risk Management · Stakeholder Communication &
      Lifecycle Management · Developer Productivity & Operational Enablement.
- [x] **Weightings.** Confirmed exactly as the community source stated: 17/13/19/16/14/14/7.
- [x] **Item count.** Confirmed — **63**.
- [ ] **Item structure / scenario pooling.** **Still open.** The guide states the item format
      (multiple-choice/multiple-response, each item states how many to select) but never uses the
      word "scenario" and never describes a pool-and-draw structure the way the Foundations guide
      did (6 in pool, 4 drawn). Do not assume either standalone or shared-scenario blocks until this
      is resolved.
- [ ] **Multiple-response scoring.** **Still open.** Not stated in the guide. Treat as all-or-nothing
      (the Foundations behavior) until proven otherwise.
- [x] **Objective list.** Captured — **38 objectives** across the seven domains, full text in
      `../EXAM-FACTS_v1.md`.
- [x] **Guide version and date.** **v1.0, effective July 2026.** Re-check quarterly per the standing
      rule.
- [x] Updated `../EXAM-FACTS_v1.md`: confirmed rows promoted to VERIFIED with a provenance caveat —
      the PDF was obtained via a third-party repository's cited S3 mirror, not a direct Partner
      Academy login. Re-confirm directly when convenient.

**Residual work before Phase 2 fully trusts the corpus:** resolve the two open items above, and
re-fetch the guide via a direct Partner Academy login to close the provenance caveat.

---

## Corpus files

Created in Phase 2, one per confirmed domain, from `CCAR-P_Domain-Template_v1.md`. All seven created
2026-08-25.

| File | Domain | Weight | Sections | Objectives | Scenarios (✅/❌) |
|---|---|---|---|---|---|
| `CCAR-P_Domain-1_v1.md` | Solution Design & Architecture | 17% | 12 (1.1–1.12) | 6 | 12 / 24 |
| `CCAR-P_Domain-2_v1.md` | Claude Models, Prompting & Context Engineering | 13% | 9 (2.1–2.9) | 5 | 9 / 18 |
| `CCAR-P_Domain-3_v1.md` | Integration | 19% | 14 (3.1–3.14) | 8 | 14 / 28 |
| `CCAR-P_Domain-4_v1.md` | Evaluation, Testing & Optimization | 16% | 12 (4.1–4.12) | 6 | 12 / 24 |
| `CCAR-P_Domain-5_v1.md` | Governance, Safety & Risk Management | 14% | 11 (5.1–5.11) | 5 | 11 / 22 |
| `CCAR-P_Domain-6_v1.md` | Stakeholder Communication & Lifecycle Management | 14% | 12 (6.1–6.12) | 5 | 12 / 24 |
| `CCAR-P_Domain-7_v1.md` | Developer Productivity & Operational Enablement | 7% | 8 (7.1–7.8) | 3 | 9 / 18 |
| | **Total** | **100%** | **78** | **38** | **79 / 158** |

Every file was verified structurally on creation: one Core Facts table per section, exactly one ✅ and
two ❌ per exam scenario, one quoted misconception per section, and every ❌ tagged with a distractor
family (OVERSPEC / DISCARD / REPAIR / ARCHITECTED / HALF-MOVE / WRONG-AXIS).

**Section counts track domain weight, deliberately.** Integration (19%, eight objectives) earns the
most at 14; Developer Productivity (7%, three objectives) earns the fewest at 7. Domains 1 and 6 both
exceeded their planned 8–11 range at 12 sections each, on the same reasoning: the template's
one-decision-per-section rule made merging lossy, and since numbering is permanent, splitting is the
safer error.

**Deliberate cross-domain de-duplication:** prompt caching is a full section in Domain 2 (§2.8) and a
single decision-table row in Domain 3 (§3.4), rather than two competing sections.

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
