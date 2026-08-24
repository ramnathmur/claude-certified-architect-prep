# CCAO-F Corpus Index

**Status:** empty. No domain files exist yet, by design.

Domain files are the only permitted source for generated questions. The domain *names* here rest on
strong evidence — six of the seven match the official Academy lesson titles near-verbatim — but the
*weightings* rest on a community source that states on its own site that it is not affiliated with
Anthropic. Quotas come from weightings. So the corpus starts after Phase 0 closes.

---

## Phase 0 reconciliation checklist

Run this the moment the official CCAO-F Exam Guide PDF lands in `../sources/`.

- [ ] **Domain list.** Record the real domain names and codes. Community source says seven:
      Prompting and Task Execution · Output Evaluation and Validation · Product and Model Selection ·
      Workflow Integration and Solution Design · Configuration and Knowledge Management · Governance,
      Risk and Responsible Use · Troubleshooting and Optimisation. Six of these are the official
      lesson titles; the seventh (Product and Model Selection ← "Claude Platform & Model Foundations")
      is the one loose mapping. Confirm it.
- [ ] **Weightings.** Community source says 14 / 21 / 12 / 16 / 12 / 15 / 10. These track the official
      lesson minutes closely (arithmetic in `../EXAM-FACTS_v1.md`) but nothing official states them.
      Question quotas come from the guide, never from that list.
- [ ] **Item count.** Community source says 60 in 120 minutes. Unverified. CCAR-F was also 60/120,
      which makes it plausible and therefore easy to accept without checking.
- [ ] **Item structure.** Community source says standalone items, *"each item states how many responses
      to select"*, with no mention of scenario blocks. CCAR-F drew 4 blocks of 15 items from a pool of
      6. **These are different exam shapes.** The guide settles it. If blocks exist, record how many
      are in the pool and how many are drawn — it changes how every paper is generated.
- [ ] **Multiple-response scoring.** All-or-nothing, or partial credit? On CCAR-F it was all-or-nothing
      and cost eight marks. This single answer changes exam-day tactics more than any content fact.
- [ ] **Objective list.** The CCAR-F score report exposed 37 objectives — the right granularity to
      build against. Capture the published objectives per domain.
- [ ] **Guide version and date.** The CCAR-F guide moved to v1.0 in July 2026 and dropped a whole
      section. Record version + date here and re-check quarterly.
- [ ] **Confirm the program-wide facts apply.** Pass mark 720, scale 100–1000, 12-month validity,
      closed book. These were read from the Partner Academy FAQ as program-wide on 2026-08-18, not
      from a CCAO-F source. Confirm there is no per-exam variation.
- [ ] Update `../EXAM-FACTS_v1.md`: move confirmed rows to VERIFIED, delete disproved rows, and note
      anything the guide states that neither source anticipated.

---

## Corpus files

Created in Phase 2, one per confirmed domain, from `CCAO-F_Domain-Template_v1.md`.

| File | Domain | Weight | Sections | Status |
|---|---|---|---|---|
| `CCAO-F_Domain-1_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAO-F_Domain-2_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAO-F_Domain-3_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAO-F_Domain-4_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAO-F_Domain-5_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAO-F_Domain-6_v1.md` | *pending Phase 0* | — | — | not created |
| `CCAO-F_Domain-7_v1.md` | *pending Phase 0* | — | — | not created |

## Head starts — material that already exists

| Target domain | Existing asset | Where |
|---|---|---|
| Prompting and Task Execution | CCAR-F `CCA-Prep_Domain-4_v2.md` | `..\..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\` |
| Troubleshooting and Optimisation | CCAR-F `CCA-Prep_Domain-5_v2.md` (context/reliability), partial | Same folder |
| Output Evaluation and Validation | Eval Design Blueprint, ~13.5k words | `my blueprints\eval-blueprint\` — written at architect altitude, needs heavy simplification |
| Workflow Integration and Solution Design | AI-First Design Blueprint | `my blueprints\` — same altitude caveat |
| Governance, Risk and Responsible Use | none — build from Tier 3 of `../BACKGROUND-MATERIAL-INDEX_v1.md` | — |
| **Product and Model Selection** | **none** | The real gap. Build from the Help Centre, Tier 2 |
| **Configuration and Knowledge Management** | **none** | The other real gap. Build from the Help Centre, Tier 2 |

**Build order: the two gaps first.** They are 24% of the paper between them, they carry no existing
material, and they are the least interesting to write — which is exactly why they get skipped and then
lost on exam day.

## The altitude audit

Every ported section gets one extra check before it enters the corpus: **could someone who has never
opened a terminal answer this?** If not, it is pitched for CCAR-F, not CCAO-F. Rewrite or drop it.
Record ported-then-dropped sections here so the same material is not re-imported later:

*None yet.*
