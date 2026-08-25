# CCAR-P — Twelve-Month Roadmap

**Created:** 2026-08-18, the day CCAR-F was passed (851/720).
**Status:** Phase 0, **parallel track.** CCDV-F became the active exam on 2026-08-19; this project is
kept warm rather than paused. Exam guide obtained and reconciled 2026-08-25 — see the provenance
caveat in `EXAM-FACTS_v1.md`. Only the Path A/B decision below remains open in Phase 0.

> **Revised ordering, 2026-08-19.** Ram is sitting **CCDV-F first**. Phase 1 below still runs, but in
> CCDV-F-serving order: **Lesson 2 (Enterprise Integration & Production), then Lesson 3 (Responsible
> AI, Safety & Risk)**, then the rest. Those two feed CCDV-F's Applications-and-Integration domain
> (its largest) and its Security domain. Phase 3's production work now has a second purpose: it is
> also the exposure CCDV-F assumes and this ordering does not otherwise supply.

## Two dates that anchor everything

| Date | What |
|---|---|
| **2027-08-18** | CCAR-F expires. Free non-proctored renewal if done on time; full price and full exam if it lapses |
| **Target sitting** | Set once Phase 1 completes. See the two options below |

Holding CCAR-F is **not** a prerequisite for CCAR-P and does not upgrade into it — they are separate
exams. But letting F lapse while chasing P means losing a credential already earned, so the renewal
is a hard calendar item regardless of the P timeline.

---

## What this actually takes — honest read

The Foundations run took six weeks, fourteen mock papers, and a purpose-built 155 KB corpus. That
worked because the syllabus was five domains of technical material Ram could learn from documentation.

Professional is a different shape:

- **~13%** (Claude Models, Prompting & Context Engineering) is a direct carry-over from the
  Foundations corpus. Already owned.
- **~33%** (Solution Design 17% + Evaluation 16%) is adjacent — Ram has real assets here, notably the
  Eval Design Blueprint, but the material has to be rebuilt at production-architecture altitude.
- **~19%** (Integration) is the genuine technical stretch: enterprise systems, data connectivity,
  deployment platforms. This is where the "6+ months hands-on Claude in production" recommendation bites.
- **~35%** (Governance/Safety/Risk 14% + Stakeholder/Lifecycle 14% + Enablement 7%) does not exist on
  the Foundations blueprint at all. Of that, the Stakeholder domain is arguably Ram's *strongest*
  ground as a consultant — it just has to be converted from professional instinct into exam-shaped
  recall.

*(Percentages are now VERIFIED against the official exam guide — see `EXAM-FACTS_v1.md`.)*

**The honest bottleneck is not study time. It's production exposure.** The exam is written for people
who have shipped and operated a Claude system. Reading closes the knowledge gap; it does not close
the judgement gap. Phase 3 below exists specifically to build that.

### Two credible paths

| | **Path A — Fast** | **Path B — Grounded** |
|---|---|---|
| Sitting | ~Dec 2026 – Jan 2027 (4–5 months) | ~May – Jul 2027 (9–11 months) |
| Approach | Official path + corpus + mocks, largely book-learned | Same, plus one real Claude system taken to production at Infosys |
| Risk | Integration (19%) and Governance (14%) answered from reading, not experience | Longer runway; F renewal lands mid-flight |
| Fits if | The goal is the credential on the CV this financial year | The goal is the business-consultant→AI-architect transition to be real |

**Recommendation: Path B**, with the Phase 1–2 work started now. The transition Ram is making is the
actual objective; the certificate is evidence of it. Path B also leaves room to renew F on time
without colliding with P revision.

---

## Phases

### Phase 0 — Unblock (this week)
- [x] Download the **CCAR-P Official Exam Guide (PDF)** → `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`
      (2026-08-25, via a third-party repo's cited S3 mirror — not a direct Partner Academy login; see
      the provenance caveat in `EXAM-FACTS_v1.md`)
- [ ] Sign in to Anthropic Partner Academy with the Infosys Claude Partner Network account and
      re-fetch the guide directly, to close the provenance caveat above
- [x] Reconcile every ⚠️ in `EXAM-FACTS_v1.md`; move confirmed rows to VERIFIED (2026-08-25) — two
      items remain genuinely open (scenario pooling, multi-response scoring), not caveat-blocked
- [x] Confirm the real domain list and weightings — all seven names and percentages matched the
      community source exactly; `CCAR-P_Domain-N` stub table in the corpus index now carries the
      confirmed names and weights (files themselves still not created — that's Phase 2)
- [ ] Decide Path A or Path B and write the target date into this file

**Nothing else starts until Phase 0 closes.** This is the lesson from Foundations, where a community
guide's wrong scenario count reached generated practice material.

### Phase 1 — Official syllabus (weeks 2–7)
- [ ] Work the 5-lesson official prep path — 733 min, ~12 h of video, budget 25–30 h with notes
- [ ] One `notes/` file per lesson, written as decision rules, not summaries
- [ ] Close the six carry-over 0% objectives from the CCAR-F score report (listed in
      `BACKGROUND-MATERIAL-INDEX_v1.md`) — these are the only documented weaknesses that already exist
- [ ] Confirm rather than re-sit the six Academy pre-enrolment courses

### Phase 2 — Build the corpus (weeks 6–16, overlapping Phase 1)
- [ ] One `CCAR-P_Domain-N_v1.md` per confirmed domain, built the way the Foundations `_v2` files were:
      core facts, decision tables, exam scenarios with ✅/❌, explicit misconceptions
- [ ] Port the Foundations D1/D4/D5 material into the Models/Prompting/Context domain
- [ ] Build the Evaluation domain from the existing Eval Design Blueprint
- [ ] Tier-3 governance reading → the Governance domain file
- [ ] Corpus index + concept inventory, so coverage can be audited

### Phase 3 — Production exposure (months 3–8, Path B only)
- [ ] Take one Claude system at Infosys from design to production: integration, evals, safety
      controls, cost model, stakeholder sign-off, runbook
- [ ] Keep an architecture decision record — it doubles as Solution Design and Stakeholder revision
- [ ] Everything surprising in production goes into the corpus as a decision rule

### Phase 4 — Mock engine (months 6–10)
- [ ] Port `CCA-Orchestration-Prompt_v10.md` → `CCAR-P-Orchestration-Prompt_v1.md`, re-quota'd to the
      confirmed domains
- [ ] Generate and sit papers on the Foundations cadence. Target ≥10 scored papers
- [ ] `EXAM-LOG.md` per-paper: domain breakdown, per-question misses, Professor's Note
- [ ] Insights Round every 3 scored papers
- [ ] Confirmed-weakness rule: a domain weakest on two consecutive papers gets a quota bump

### Phase 5 — Final approach (final 6 weeks)
- [ ] Miss corpus → mistake-pattern artifact, the way `CCA-Prep_Mistake-Patterns_v1.html` was built
- [ ] Trap sheet, setter's-eye
- [ ] Re-verify `EXAM-FACTS_v1.md` against the guide — check for a version bump
- [ ] Two clean papers in Exam Mode (no per-question feedback) before booking
- [ ] Book Pearson VUE

### Phase 6 — Sitting and after
- [ ] Sit CCAR-P
- [ ] Log the real score report objective-by-objective, as was done for F — that report is the single
      most valuable artifact the whole exercise produces
- [ ] Renew CCAR-F on time (due 2027-08-18)

---

## Standing rules for this project

1. **No practice question is generated from an unverified fact.** Community sources inform reading;
   only the official guide sets quotas.
2. **`EXAM-FACTS_v1.md` is re-verified quarterly.** The Foundations guide silently moved to v1.0 and
   dropped a section mid-prep.
3. **Attempt chronology, not file numbering.** The Foundations log was corrupted twice by assuming
   exam number equalled attempt order.
4. **One source of truth for standing.** `prep with quiz/EXAM-LOG.md`. If a second file starts
   carrying scores, delete it.
5. **Multiple-response items are all-or-nothing until proven otherwise.** Eight of the Foundations
   misses were majority-right answers scored zero.
