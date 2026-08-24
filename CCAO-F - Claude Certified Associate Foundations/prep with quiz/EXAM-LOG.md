# CCAO-F Exam Log

**The single source of truth for Ram's standing on CCAO-F.** No other file in this project carries
scores. If one starts to, delete it.

**Status:** no papers generated, no papers sat. Blocked on Phase 0 — see `../ROADMAP.md`.

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
4. **Insights Round every 3 scored papers.** On a 4–6 paper plan that means one round, possibly two.
5. **Every miss is logged to a corpus section.** A miss with no section reference cannot become a
   pattern, and patterns are the entire point.
6. **Multiple-response items are recorded separately** from single-answer. On CCAR-F, eight misses were
   majority-right answers scored zero by all-or-nothing grading — a scoring leak that looked like a
   knowledge gap until the formats were split out.
7. **Time per question is recorded.** It distinguishes rushed errors from considered-and-wrong errors.
   On CCAR-F every miss cluster turned out to be considered-and-wrong, which changed the remediation
   entirely.

### One convention specific to this exam

8. **Record whether the miss was an altitude error.** Ram holds CCAR-F; this exam sits a tier below it.
   A miss where the chosen answer was *more technical or more architected than the question asked for*
   is a different failure from not knowing the material, and it needs a different fix. Tag those
   `ALTITUDE` in the miss table. If they cluster, the corpus is pitched too high, not too thin.

---

## Entry template

Copy this block for each paper. Do not abbreviate it — the Professor's Note is what makes the next
paper better than the last.

```markdown
## Paper N — SCORED YYYY-MM-DD (XX/YY, scaled ZZZ)

**File:** `mock-exams/CCAO-F_MockTest-N_v1.html`
**Attempt date:** YYYY-MM-DD | **Score source:** results-json | **Total time:** MM:SS of 120:00
**Total score:** XX / YY correct (estimated scaled ZZZ; pass line 720)
**Item formats:** single-answer A/B (x%) · multiple-response C/D (y%)
**Mode:** Exam Mode (no per-question feedback) / Practice Mode

### Domain Breakdown
| Domain | Questions | Correct | % |
|---|---|---|---|
| ... | | | |

### Misses
| Q | Domain § | Format | Time | Picked | Correct | Why wrong | ALTITUDE? |
|---|---|---|---|---|---|---|---|

### Confirmed-weakness check
Comparator: Paper M, attempted YYYY-MM-DD (the true immediate predecessor by attempt date).
Weakest this paper: ... | Unambiguous? yes/no | confirmed_weakness: true/false

### Findings
Ranked by evidence strength. A finding needs a section reference and a stated direction of error.

### Pace
Average s/question. Were the misses fast or slow? Fast = time pressure. Slow = a real decision error.

### Professor's Note — Intent for Paper N+1
Ranked list of what the next paper must test, and from which direction.
```

---

## Papers

*None yet.*

---

## Insights Rounds

*None yet. First one fires at 3 scored papers.*
