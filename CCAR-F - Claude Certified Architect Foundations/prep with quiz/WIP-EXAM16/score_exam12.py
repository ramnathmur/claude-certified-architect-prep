"""Score Exam 12 into the ledgers: EXAM-LOG.md header patch + scored analysis + Professor's Note
for Exam 17 + Insights Round 3, and the DASHBOARD-DATA.jsonl row. Append-only apart from the three
pending header lines inside the Exam 12 entry. Refuses to run twice.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOG = os.path.join(ROOT, "EXAM-LOG.md")
JSONL = os.path.join(ROOT, "DASHBOARD-DATA.jsonl")

t = open(LOG, encoding="utf-8").read()
if "## Insights Round 3 —" in t or "## Exam 12 — SCORED" in t:
    raise SystemExit("REFUSING: Exam 12 already scored / Insights Round 3 already written.")

# ---- 1. patch the three pending header lines inside the Exam 12 entry only ----
start = t.index("## Exam 12 — Generated 2026-08-10")
end = t.index("## Exam 13", start)
seg = t[start:end]
old = ("**Attempt date:** Not yet attempted\n"
       "**Score source:** Pending\n"
       "**Total score:** Pending")
new = ("**Attempt date:** 2026-08-11\n"
       "**Score source:** results-json\n"
       "**Total score:** 53 / 60 correct (estimated scaled: 895 / 1000; pass line 720)\n"
       "**Total time:** 42:40 (42.7s/question — 36% of the 120-minute allowance)")
assert seg.count(old) == 1, f"header block not uniquely found in the Exam 12 entry ({seg.count(old)} hits)"
t = t[:start] + seg.replace(old, new) + t[end:]

entry = """

---

## Exam 12 — SCORED 2026-08-11

**Score source:** results-json (full per-question data)
**Total:** 53 / 60 correct · estimated scaled 895 / 1000 · pass line 720
**Time:** 2,560s = 42:40 across 60 questions (42.7s/question). The allowance is 120 minutes; **77 minutes
went unused.**

Note on denominators: Exam 12 ran the confirmed-weakness quota (D1 14 / D2 15 / D3 12 / D4 12 / D5 7),
not the base 16/11/12/12/9. Percentages are comparable across exams; raw counts are not.

### Domain Breakdown

| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 14 | 13 | 93% | no |
| D2 Tool Design & MCP | 15 | 13 | 87% | no |
| D3 Claude Code Config | 12 | 10 | 83% | no |
| D4 Prompt Engineering | 12 | 10 | 83% | no |
| D5 Context Management | 7 | 7 | 100% | no |

### Block Breakdown

| Block | Scenario | Correct |
|---|---|---|
| 1 | Code Generation with Claude Code | 13 / 15 |
| 2 | Multi-Agent Research System | 13 / 15 |
| 3 | Developer Productivity with Claude | 14 / 15 |
| 4 | Claude Code for Continuous Integration | 13 / 15 |

Blocks are flat — 13/13/14/13. No scenario is a weak spot.

### The seven misses

| Q | Dom | § | Picked | Key | Time | What the wrong pick was |
|---|---|---|---|---|---|---|
| 1 | D3 | §3.1 | C `.claude/rules/` | A `/memory` | 26s | a fix, before diagnosing which file loaded |
| 6 | D4 | §4.1 | D post-process output | A few-shot examples | 117s | a repair stage bolted after generation |
| 17 | D1 | §1.2 | C give it a retrieval tool | B coordinator passes findings | 93s | wider privileges instead of passing context it already holds |
| 18 | D2 | §2.1 | A missing user message | D `tool_result` keyed by `tool_use` `id` | 25s | protocol mechanics |
| 33 | D2 | §2.5 | B `auto` + prompt rule | A `{"type": "any"}` | 32s | a probabilistic control where a guarantee exists |
| 56 | D3 | §3.4 | B `.claude/rules/` | C `.claude/commands/` | 30s | wrong config location |
| 57 | D4 | §4.11 | B synchronous fallback | A deadline − 24h | 38s | a workaround instead of the planning rule |

### Observations

**1. Five of the seven misses are one error, not five.** Q1, Q6, Q17, Q33 and Q57 all reach for a
compensating mechanism rather than the root-cause fix or the available deterministic guarantee: build a
rules file rather than diagnose; post-process rather than give examples; grant a tool rather than pass
context; `auto` plus an instruction rather than `any`; a synchronous fallback rather than submitting a day
earlier. Those map onto three of the exam's own stated answer heuristics — *fix the root cause not the
symptom*, *deterministic over probabilistic*, *proportionate first response*. **This is one reusable
decision rule, and drilling it is worth more than drilling five sections.**

**2. `.claude/rules/` was chosen wrongly twice on one paper** (Q1 and Q56). It is operating as a default
answer to "where should this live?". The three-way distinction to hold: **rules** = path-scoped
conventions that auto-load on matching files; **commands/skills** = invocable by name; **CLAUDE.md** =
always-on standards. In Q1 the answer was not a location at all — it was a diagnostic.

**3. Speed is not the constraint; confidence is.** Five of the seven misses took under 40 seconds. The
two slow ones (117s, 93s) were considered at length and still wrong. 42:40 of a 120-minute allowance was
used. There is no time pressure at this pace — the errors live in fast, confident answers to
"which mechanism" questions, which is precisely where the compensating-mechanism reflex fires.

**4. The D2 experiment succeeded and should now end.** D2 was CONFIRMED weak entering this paper, which
is why Exam 12 carried +4 (15 D2 questions, the largest D2 quota ever set). Result: 13/15 = 87% — on the
biggest denominator, against a 78.4% all-time D2 mean. The targeted quota did its job.

### Professor's Note — Intent for Exam 17

Written after Exam 12 (attempted 2026-08-11). Based on results-json. **Numbering: "Intent for Exam 17",
not 13 — Exams 13, 14, 15 and 16 were all generated before this score arrived, mirroring the Exam 9→12
skip precedent. Its targeting function therefore cannot reach the papers already on disk; the actionable
part this week is the revision focus below, not the next paper.**

- Misconceptions revealed:
  1. **Compensating mechanism over root-cause fix** — the dominant shape, five of seven misses, spanning
     D1 §1.2/§1.11, D2 §2.5, D3 §3.1, D4 §4.1 and D4 §4.11. Not a domain gap; a decision-rule gap.
  2. **`.claude/rules/` as a catch-all location** (D3 §3.2 confused with §3.1 and §3.4, twice on one paper).
  3. **The tool-result protocol** (D2 §2.1) — results re-enter as `tool_result` blocks keyed to their
     `tool_use` `id`, not as narrated prose. Missed here after also being a targeted section in Exam 13.
- Weakest this paper: **D3 and D4 tied at 83%** — not confirmed, because Exam 11 (the most recent prior
  scored paper by attempt chronology) was weakest at D5. Base quota therefore applies to Exam 17.
- Intent for next paper: within the fixed quota, build items where the plausible workaround is *present
  and attractive* but the root-cause fix is available — that is the exact geometry of all five misses,
  and a paper that omits the tempting distractor will not test it. Give D3's where-does-this-live family
  (§3.1 / §3.2 / §3.3 / §3.4) a three-way discrimination rather than a single lookup. Re-test D2 §2.1 on
  the `id` correlation specifically.
- Watch next: whether the compensating-mechanism reflex disappears when the paper is unfamiliar in shape
  (Exams 14 and 16 carry no recognisable question archetypes), or whether it survives — which would make
  it a genuine reasoning habit rather than a pattern-matching artefact.

---

## Insights Round 3 — 2026-08-11 (fires at 9 scored exams)

Nine exams are now scored. Ordered by **attempt** date, not generation number.

| # | attempted | raw | scaled | mins | D1 | D2 | D3 | D4 | D5 | weakest |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 2026-07-11 | 45/60 | 775 | 736 | 75% | 45% | 75% | 83% | 100% | D2 |
| 5 | 2026-07-11 | 52/60 | 880 | 32 | 94% | 73% | 92% | 75% | 100% | D2 |
| 6 | 2026-07-12 | 49/60 | 835 | 260 | 93% | 73% | 83% | 83% | 71% | D5 |
| 7 | 2026-07-16 | 55/60 | 925 | 325 | 94% | 100% | 83% | 83% | 100% | D3/D4 |
| 8 | 2026-07-28 | 52/60 | 880 | 35 | 94% | 91% | 75% | 75% | 100% | D3/D4 |
| 10 | 2026-07-29 | 54/60 | 910 | 39 | 94% | 82% | 83% | 92% | 100% | D2 |
| 9 | 2026-08-09 | 49/60 | 835 | 42 | 88% | 64% | 92% | 83% | 78% | D2 |
| 11 | 2026-08-10 | 55/60 | 925 | 40 | 94% | 91% | 92% | 92% | 89% | D5 |
| 12 | 2026-08-11 | 53/60 | 895 | 43 | 93% | 87% | 83% | 83% | 100% | D3/D4 |

**Domain trends (all-time mean / last-3 mean):** D1 90.8 / 91.4 · D2 78.4 / 80.4 · D3 84.3 / 88.9 ·
D4 83.3 / 86.1 · D5 93.1 / 88.9.

**1. The band is stable and comfortably above the line.** The last six attempts run 49–55/60, scaled
835–925, against a 720 pass line. The lowest of the nine (775, Exam 4) still passes. Nothing in this
record suggests the exam is in doubt.

**2. D2 has genuinely recovered — retire the adjustment.** Trajectory 45 → 73 → 73 → 100 → 91 → 82 → 64
→ 91 → 87. The 64% (Exam 9, attempted 2026-08-09) reads as the outlier rather than the trend: that paper
was generated 2026-07-19, and the two attempts on either side of it scored 82% and 91%. The confirmed-
weakness quota fired once, put 15 D2 questions on Exam 12, and D2 returned 87%. **Recommendation: no
further D2 adjustment.**

**3. D3 and D4 are the standing weakness, and have been for nine exams.** They have now tied weakest
three times (Exams 7, 8, 12) and **neither has ever been the strongest domain on any paper.** All-time
means 84.3% and 83.3% — the two lowest apart from D2's recovering 78.4%. The last-3 figures (88.9%,
86.1%) are better, so this is a slow improvement rather than a stall, but it is the only place a
meaningful number of marks is still being left.

**4. D5's Exam 11 flag was a denominator artefact, and the rule that produced it needs a caveat.** Exam
11 named D5 weakest at 88.9% — one wrong answer out of 9. Exam 12 returned 100%. D5's all-time mean of
93.1% is the **highest** of any domain. On a 7–9 question domain a single miss moves the percentage by
11–14 points, which is enough to win a weakest-domain comparison outright. **Standing caveat for future
rounds: treat "weakest" on D5 (and on any domain running fewer than 10 questions) as provisional unless
the margin exceeds one question.** The two-consecutive-exam gate already protects against acting on it,
and it correctly did so here.

**5. The finding this round that is not about domains at all.** Exam 12's seven misses concentrate into
one error shape — preferring a compensating mechanism to the root-cause fix or the deterministic
guarantee — that spans four of the five domains. A domain-weighted quota cannot target it, because it is
not located in a domain. **It is targetable through question geometry instead: items where a plausible
workaround is present and attractive alongside the correct root-cause fix.** That is a generation
instruction, and it is recorded as such in the Intent for Exam 17 above.

**6. Timing has no remaining risk.** Excluding the three papers taken across multiple sittings (Exams 4,
6, 7 at 736/260/325 minutes), the five single-sitting attempts run 32–43 minutes against 120. Exam 12
used 36% of the allowance. There is no scenario in which the clock is the binding constraint, which means
slowing down on the four or five items that feel obvious costs nothing.
"""

# ---- 2. one atomic write: patched header + appended analysis ----
before = len(open(LOG, encoding="utf-8").read())
out = t + entry
assert len(out) > before, "refusing to shrink EXAM-LOG.md"
assert "## Exam 16 —" in out and "## Exam 4 —" in out, "refusing to write a truncated log"
with open(LOG, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"EXAM-LOG.md: {before} -> {len(out)} chars (+{len(out)-before})")

# ---- 3. dashboard row ----
rows = [json.loads(l) for l in open(JSONL, encoding="utf-8") if l.strip()]
hit = [r for r in rows if r["exam_n"] == 12]
assert len(hit) == 1, "expected exactly one exam_n 12 row"
if hit[0].get("total_correct") is not None:
    raise SystemExit("REFUSING: exam_n 12 already scored in DASHBOARD-DATA.jsonl")
hit[0].update({
    "attempted_date": "2026-08-11", "score_source": "results-json",
    "total_correct": 53, "estimated_scaled": 895, "total_seconds": 2560,
    "domain_scores": {"D1": {"correct": 13, "of": 14}, "D2": {"correct": 13, "of": 15},
                      "D3": {"correct": 10, "of": 12}, "D4": {"correct": 10, "of": 12},
                      "D5": {"correct": 7, "of": 7}},
    "weakest_domain": "D3/D4 (tied)", "confirmed_weakness": False, "insight_round_due": True,
})
rows.sort(key=lambda r: r["exam_n"])
with open(JSONL, "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
scored = sum(1 for r in rows if r.get("total_correct") is not None)
print(f"DASHBOARD-DATA.jsonl: {len(rows)} rows, {scored} scored")
