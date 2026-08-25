# CCAR-P Corpus Index

**Status:** Phase 0 reconciliation done 2026-08-25. Domain files still not created — that is Phase 2.

Domain files are the only permitted source for generated questions. The domain list and weightings
are now confirmed (see below), so Phase 2 file creation is unblocked, but no domain file exists yet.

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

Created in Phase 2, one per confirmed domain, from `CCAR-P_Domain-Template_v1.md`.

| File | Domain | Weight | Sections | Status |
|---|---|---|---|---|
| `CCAR-P_Domain-1_v1.md` | Solution Design & Architecture | 17% | 6 objectives | not created |
| `CCAR-P_Domain-2_v1.md` | Claude Models, Prompting & Context Engineering | 13% | 5 objectives | not created |
| `CCAR-P_Domain-3_v1.md` | Integration | 19% | 8 objectives | not created |
| `CCAR-P_Domain-4_v1.md` | Evaluation, Testing & Optimization | 16% | 6 objectives | not created |
| `CCAR-P_Domain-5_v1.md` | Governance, Safety & Risk Management | 14% | 5 objectives | not created |
| `CCAR-P_Domain-6_v1.md` | Stakeholder Communication & Lifecycle Management | 14% | 5 objectives | not created |
| `CCAR-P_Domain-7_v1.md` | Developer Productivity & Operational Enablement | 7% | 3 objectives | not created |

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
