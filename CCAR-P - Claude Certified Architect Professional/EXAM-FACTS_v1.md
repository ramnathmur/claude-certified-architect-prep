# CCAR-P — Verified Exam Facts

**Last verified:** 2026-08-18
**Verification rule for this project:** every line below carries a source and a confidence label.
Nothing gets promoted to VERIFIED without an Anthropic-controlled source (anthropic.com,
anthropic-partners.skilljar.com, or pearsonvue.com/anthropic).

> **Why this file exists.** On the Foundations run, a community guide stated the exam draws 8
> scenarios. The real number is 6. That error propagated into generated practice material before it
> was caught. This file is the guard against a repeat: community claims live in the UNVERIFIED table
> and are never used to generate practice content until confirmed against the official guide.

---

## VERIFIED — Anthropic-controlled sources

| Fact | Value | Source |
|---|---|---|
| Exam code | **CCAR-P** | Pearson VUE Anthropic program page |
| Full name | Claude Certified Architect – Professional | Anthropic Partner Academy |
| Price | **$175 USD** | Anthropic Partner Academy certification page |
| Answering time | **120 minutes** | Partner Academy certification FAQ |
| Total seat time | ~135 minutes (incl. check-in + survey) | Partner Academy certification FAQ |
| Scoring | Scaled **100–1000** | Partner Academy certification FAQ |
| Pass mark | **720** (same for all four certifications) | Partner Academy certification FAQ |
| Question types | Multiple choice **and scenario-based multiple response** | Partner Academy certification FAQ |
| Delivery | Pearson VUE — online proctored or test centre | Pearson VUE Anthropic program page |
| Book policy | **Closed book.** No notes, documentation, translation tools, or AI assistants | Partner Academy certification FAQ |
| Validity | **12 months** from date earned | Partner Academy certification FAQ |
| Renewal | Free, **non-proctored** assessment if renewed on time. Lapsed = full exam at full price | Partner Academy certification FAQ |
| Attempts | **Up to 4 per rolling 12 months.** Waits: 14 days after 1st fail, 30 after 2nd, 90 after 3rd. Retakes cost full fee | Partner Academy certification FAQ |
| Prerequisite | **None.** Professional can be taken without holding Foundations | Partner Academy certification FAQ |
| F → P upgrade | **Does not exist.** Separate certifications, separate exams. Foundations never auto-converts | Partner Academy certification FAQ |
| Registration route | Anthropic Partner Academy (tied to Claude Partner Network) | Anthropic Partner Academy |

### Official prep path — VERIFIED
"Claude Certified Architect – Professional Prep Course", Anthropic Partner Academy.
Stated purpose: *design, integrate, and govern production-grade Claude systems end to end.*

| # | Lesson | Minutes |
|---|---|---|
| 1 | Claude Platform & Solution Design | 238 |
| 2 | Enterprise Integration & Production | 158 |
| 3 | Responsible AI, Safety & Risk for Architects | 114 |
| 4 | Stakeholder Engagement, Lifecycle & GTM | 178 |
| 5 | Team Enablement & Operational Productivity | 45 |
| | **Total** | **733 min ≈ 12.2 hours** |

**Stated pre-enrolment courses:** Claude 101 · Claude Code in Action · AI Fluency: Framework &
Foundations · Building with the Claude API · Introduction to Model Context Protocol ·
AI Capabilities and Limitations.

---

## UNVERIFIED — community sources only. DO NOT generate practice material from this table.

Source: `claudecertificationguide.com` — the site itself states it is "an independent community
resource, not affiliated with or endorsed by Anthropic."

| Claim | Stated value | Status |
|---|---|---|
| Question count | 63 items | ⚠️ UNVERIFIED |
| Item structure | Standalone items, **not** scenario-based | ⚠️ **CONTRADICTED** — Anthropic's own FAQ says the exams use "multiple choice and scenario-based multiple response questions." Treat the community claim as wrong until the official guide says otherwise. |
| Domain 1 | Integration — 19% | ⚠️ UNVERIFIED |
| Domain 2 | Solution Design & Architecture — 17% | ⚠️ UNVERIFIED |
| Domain 3 | Evaluation, Testing & Optimisation — 16% | ⚠️ UNVERIFIED |
| Domain 4 | Governance, Safety & Risk Management — 14% | ⚠️ UNVERIFIED |
| Domain 5 | Stakeholder Communication & Lifecycle Management — 14% | ⚠️ UNVERIFIED |
| Domain 6 | Claude Models, Prompting & Context Engineering — 13% | ⚠️ UNVERIFIED |
| Domain 7 | Developer Productivity & Operational Enablement — 7% | ⚠️ UNVERIFIED |
| Recommended experience | 3+ yrs systems architecture / platform engineering; 6+ months hands-on Claude in production; real end-to-end delivery | ⚠️ UNVERIFIED (plausible, echoes Academy audience language) |

**Corroboration note:** the seven domain *names* are independently echoed by the official prep
path's five lesson titles (Solution Design, Enterprise Integration, Responsible AI/Safety/Risk,
Stakeholder & Lifecycle, Team Enablement). The *names* are therefore likely right. The
*percentages* are not corroborated anywhere official and must not be used to set question quotas.

---

## BLOCKING DEPENDENCY — the official exam guide

The Partner Academy certification page carries a downloadable
**"Claude Certified Architect – Professional – Exam Guide (PDF)"**. It sits behind Partner Network
sign-in, which is why it could not be retrieved in this session.

**Action:** sign in to the Anthropic Partner Academy with the Infosys Claude Partner Network
account, download the PDF, and drop it in `sources/`. Then run the reconciliation in
`prep with quiz/CCAR-P_Corpus-Index_v1.md`.

Everything in the UNVERIFIED table gets resolved by that one file. Until it lands, this project
does not generate a single practice question — the same discipline that made the Foundations
corpus trustworthy.

> Foundations precedent: its exam guide moved to **v1.0 in July 2026** and silently dropped the
> Response Types section. Re-check the Professional guide's version and date every quarter.

---

## Open questions for the official guide to answer

1. Exact question count (community says 63 — unconfirmed).
2. Whether items are standalone or grouped into scenarios, and if grouped, how many scenarios
   exist in the pool and how many are drawn per sitting (the Foundations answer was 6 in pool, 4
   drawn).
3. The real domain weightings.
4. Whether multiple-response items are scored all-or-nothing (they were on Foundations — this
   materially changes exam-day tactics).
5. Whether any domain has a minimum floor score.
6. The published objective list per domain — the Foundations score report exposed 37 objectives,
   which is the right granularity to build a corpus against.
