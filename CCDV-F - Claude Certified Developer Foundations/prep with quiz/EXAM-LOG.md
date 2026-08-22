# CCDV-F Exam Log

**The single source of truth for Ram's standing on CCDV-F.** No other file in this project carries
scores. If one starts to, delete it.

**Status:** no papers generated, no papers sat. **Phase 0 closed 2026-08-19** — the official guide is
filed and the blueprint is confirmed. Papers start once the corpus exists (Phase 3). See `../ROADMAP.md`.

**The paper being simulated:** 53 items · 120 minutes · standalone items, each stating how many
responses to select · 720 scaled on 100–1,000 · **no domain floor**, total score only.

---

## Conventions

Carried over from the CCAR-F project, where each of these was learned by getting it wrong.

1. **`SCORED` headings are the record.** Count `## Paper N — SCORED <date>` headings and attempt dates
   together. Never read standing off a generation entry's status line — on the CCAR-F log, two entries
   read "Not yet attempted" for a month after they had been scored.
2. **Attempt chronology, never paper numbering.** Papers are sat out of order. Every comparison —
   confirmed weakness, trend, "the previous paper" — uses attempt date, not paper number.
3. **Confirmed weakness** = the same domain *unambiguously* weakest on two consecutive papers by
   attempt date. A tie fails the bar and is recorded as `false`.
4. **Insights Round every 3 scored papers.**
5. **Every miss is logged to a corpus section.** A miss with no section reference cannot become a
   pattern, and patterns are the entire point.
6. **Multiple-response items are recorded separately** from single-answer. On CCAR-F, eight misses were
   majority-right answers scored zero by all-or-nothing grading — a scoring leak that looked like a
   knowledge gap until the formats were split out.
7. **Time per question is recorded.** It distinguishes rushed errors from considered-and-wrong errors.

### The tripwire convention

8. **Every miss is tagged `RECALL` or `CONCEPT`.**
   - `RECALL` — knew the approach, could not recall a specific. A parameter name, a return shape, an
     argument order.
   - `CONCEPT` — did not know which approach was right for the stated constraint.

   **Why this is cheap insurance rather than the main diagnostic.** The official guide's three sample
   items contain no code and ask the candidate to select an approach, not produce one, and the
   blueprint's 25 skills are written in the language of principles, patterns and tradeoffs. The plan
   assumes a judgement-shaped exam on that basis.

   This tag makes the assumption falsifiable. **If `RECALL` misses exceed a quarter of all misses
   across any three consecutive papers by attempt date, the assumption is wrong** — the exam is more
   syntax-bound than the samples suggested. Say so explicitly in the Insights Round, and escalate to
   `../ROADMAP.md` Phase 2, which grows back to unassisted reps.

   Report the ratio in every Professor's Note. Until the tripwire fires, plan for judgement.

### One convention specific to the blueprint

9. **D3 (Claude Code, 3.1%) and D4 (Eval/Testing/Debugging, 2.6%) are 1–2 items each.** A 0/2 is not a
   trend. Never let them trigger a confirmed-weakness quota bump, and judge them across the whole run
   rather than within a paper. They still matter more than their weight, because four of the six
   CCAR-F 0% objectives live in or beside them — the remedy is corpus coverage and targeted retests
   across many papers, not quota inflation that would make the paper unrepresentative.

---

## Entry template

Copy this block for each paper. Do not abbreviate it — the Professor's Note is what makes the next
paper better than the last.

```markdown
## Paper N — SCORED YYYY-MM-DD (XX/YY, scaled ZZZ)

**File:** `mock-exams/CCDV-F_MockTest-N_v1.html`
**Attempt date:** YYYY-MM-DD | **Score source:** results-json | **Total time:** MM:SS of 120:00
**Total score:** XX / YY correct (estimated scaled ZZZ; pass line 720)
**Item formats:** single-answer (x%) · multiple-response (y%) — all standalone, no blocks
**Miss split:** RECALL n · CONCEPT m
**Mode:** Exam Mode (no per-question feedback) / Practice Mode

### Domain Breakdown
| D | Domain | Quota | Questions | Correct | % |
|---|---|---|---|---|---|
| 1 | Agents and Workflows | 14.7% | | | |
| 2 | Applications and Integration | 33.1% | | | |
| 3 | Claude Code | 3.1% | | | |
| 4 | Eval, Testing, and Debugging | 2.6% | | | |
| 5 | Model Selection and Optimization | 16.8% | | | |
| 6 | Prompt and Context Engineering | 11.0% | | | |
| 7 | Security and Safety | 8.1% | | | |
| 8 | Tools and MCPs | 10.6% | | | |

### Misses
| Q | Domain § | Format | Time | Picked | Correct | Why wrong | RECALL/CONCEPT |
|---|---|---|---|---|---|---|---|

### Confirmed-weakness check
Comparator: Paper M, attempted YYYY-MM-DD (the true immediate predecessor by attempt date).
Weakest this paper: ... | Unambiguous? yes/no | confirmed_weakness: true/false
(D3 and D4 excluded — too few items to be signal. See convention 9.)

### Tripwire check
RECALL share this paper: n/m. Across the last three papers by attempt date: n/m.
Over a quarter? yes/no — if yes, the judgement-shaped assumption is failing. Escalate to ROADMAP Phase 2.

### Findings
Ranked by evidence strength. A finding needs a section reference and a stated direction of error.

### Pace
Average s/question. Were the misses fast or slow? Fast = time pressure. Slow = a real decision error.

### Professor's Note — Intent for Paper N+1
Ranked list of what the next paper must test, and from which direction.
State the RECALL/CONCEPT ratio and what it implies: more corpus work, or more unassisted reps.
```

---

## Papers

*None yet.*

---

## Insights Rounds

*None yet. First one fires at 3 scored papers.*
