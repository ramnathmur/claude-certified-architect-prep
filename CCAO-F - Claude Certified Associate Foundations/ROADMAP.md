# CCAO-F — Roadmap

**Created:** 2026-08-19
**Status:** **deferred.** CCDV-F became the active exam on 2026-08-19; this one is not being worked.
Phase 0, blocked on the official exam guide, whenever it does start.

## Read this before planning anything

Ram passed **CCAR-F on 2026-08-18 with 851 against a 720 line** — the Architect Foundations exam,
which tested Claude Code, the Agent SDK, the Claude API and MCP. CCAO-F is a **lower tier than the
credential he already holds**. It is aimed, in Anthropic's own words, at *"people already using
AI-powered productivity tools in their work"* — operations, marketing, project management,
communications — and explicitly needs no API or coding experience.

That has two consequences worth stating plainly before any study plan is written.

**On value.** CCAO-F does not upgrade, extend, or deepen CCAR-F. On a CV it sits below it. The
defensible reasons to sit it are: completing the set, partner-program standing (Pearson VUE states
certification "counts toward partner program standing"), or wanting the badge for client-facing work
where "Associate" reads as practitioner rather than architect. If none of those apply, the time is
better spent on the two exams already in flight.

**As of 2026-08-19 this is moot in the near term:** Ram chose CCDV-F as the next exam, with CCAR-P
kept warm alongside it. CCAO-F is deferred. The question below stays on its Phase 0 checklist for
whenever it is picked up. See `../README.md` for the sequencing view.

**On effort.** The prep path is 389 minutes against CCAR-P's 733. Roughly half the syllabus is
already covered by the CCAR-F corpus. This is a **three-to-five week exam**, not a twelve-month one,
and the roadmap below is sized accordingly.

**The actual risk is not difficulty. It is complacency.** The material Ram has *not* covered is
product-surface detail — which Claude product does what, how Projects and knowledge bases behave,
what an admin can configure — and that is exactly the kind of content that feels trivial to read and
then fails under a two-minute clock because it was never drilled. Every documented CCAR-F miss was
considered-and-wrong rather than rushed. An easy exam sat casually is how that becomes a fail.

---

## What carries over, and what does not

| CCAO-F domain (community list, unverified) | Weight | Standing |
|---|---|---|
| Output Evaluation and Validation | 21% | **Partial.** CCAR-F covered evaluation at architecture altitude. This domain wants it at desk altitude: is this output good enough to send, and how would you check |
| Workflow Integration and Solution Design | 16% | **Partial.** Same shape as CCAR-F Solution Design, one tier down |
| Governance, Risk and Responsible Use | 15% | **New-ish.** CCAR-F touched safety; the governance framing here is closer to CCAR-P's Responsible AI lesson |
| Prompting and Task Execution | 14% | **Owned.** CCAR-F `CCA-Prep_Domain-4_v2.md` covers this and more |
| Product and Model Selection | 12% | **The real gap.** Not model architecture — product surface. Which Claude product, which plan, which model, for whom |
| Configuration and Knowledge Management | 12% | **The other real gap.** Projects, knowledge bases, custom instructions, admin settings |
| Troubleshooting and Optimisation | 10% | **Partial.** CCAR-F reliability material maps here loosely |

Roughly **26% of the paper — Product/Model Selection plus Configuration — is genuinely new ground**,
and it is the least intellectually demanding and most easily under-prepared part of the syllabus.
Weight the corpus toward it.

---

## Phases

### Phase 0 — Unblock (week 1)
- [ ] Sign in to Anthropic Partner Academy with the Infosys Claude Partner Network account
- [ ] Download the **CCAO-F Exam Guide (PDF)** → `sources/`
- [ ] Reconcile every ⚠️ in `EXAM-FACTS_v1.md`; move confirmed rows to VERIFIED
- [ ] Confirm the domain list, weightings and item count, then name the `CCAO-F_Domain-N` files
- [ ] Settle the standalone-vs-scenario-block question — it decides how papers are generated
- [ ] Decide whether this exam is worth sitting at all, given the value note above. Write the answer here

**Nothing else starts until Phase 0 closes.** This is the lesson from CCAR-F, where a community
guide's wrong scenario count reached generated practice material.

### Phase 1 — Official path (weeks 1–2)
- [ ] Work the 8-lesson prep path — 389 min of video, budget 10–12 h with notes
- [ ] Confirm rather than re-sit the three prerequisite courses (Claude 101 · AI Fluency ·
      AI Capabilities and Limitations) — all were covered on the CCAR-F run
- [ ] One `notes/` file per lesson, written as decision rules
- [ ] Spend disproportionate time on lessons 1 and 5 — Platform & Model Foundations and
      Configuration & Knowledge Management are the two domains with no CCAR-F carry-over

### Phase 2 — Corpus (weeks 2–3, overlapping Phase 1)
- [ ] Port CCAR-F `CCA-Prep_Domain-4_v2.md` (prompting) into the Prompting domain, dropping anything
      that assumes API or SDK access — this is a no-code exam and the altitude has to come down
- [ ] Write the Product/Model Selection and Configuration domains from scratch. These are the two
      that decide the outcome
- [ ] Governance domain from the official lesson plus the Tier-2 reading in
      `BACKGROUND-MATERIAL-INDEX_v1.md`
- [ ] Corpus index with a concept inventory, so coverage can be audited

### Phase 3 — Mock papers (weeks 3–4)
- [ ] Generate papers with `prep with quiz/CCAO-F-Orchestration-Prompt_v1.md`
- [ ] Target **4–6 scored papers**. CCAR-F needed fourteen; this exam does not
- [ ] Log every miss to a corpus section in `prep with quiz/EXAM-LOG.md`
- [ ] Insights Round after paper 3
- [ ] Do not skip the log because the exam is easy. The miss record is what turns a comfortable 78%
      into a comfortable 90%

### Phase 4 — Sitting (week 4–5)
- [ ] Two clean papers in Exam Mode (no per-question feedback) before booking
- [ ] Re-verify `EXAM-FACTS_v1.md` against the guide — check for a version bump
- [ ] Book Pearson VUE ($99)
- [ ] Log the real score report objective-by-objective, as was done for CCAR-F. That report is the
      single most valuable artifact the exercise produces, and it feeds CCAR-P

---

## Standing rules

1. **No practice question is generated from an unverified fact.** Community sources inform reading;
   only the official guide sets quotas. The corroboration in `EXAM-FACTS_v1.md` is strong but it is
   still an inference.
2. **Attempt chronology, never paper numbering.** The CCAR-F log was corrupted twice by assuming
   paper number equalled attempt order.
3. **One source of truth for standing.** `prep with quiz/EXAM-LOG.md`. If a second file starts
   carrying scores, delete it.
4. **Multiple-response items are all-or-nothing until proven otherwise.** Eight CCAR-F misses were
   majority-right answers scored zero.
5. **Drill the boring domains hardest.** Product surface and configuration detail is where an
   over-qualified candidate loses marks.
