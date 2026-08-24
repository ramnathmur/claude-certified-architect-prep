# Session State

status: COMPLETE
phase: EXAM_20_SCORED
started_at: 2026-08-17
completed_at: 2026-08-17
exam_file: mock-exams/CCA-Prep_MockTest-20_v1.html (SCORED, Exam Mode)
format: FULL60
score: Exam 20 SCORED 2026-08-17 (56/60, 940 — ties Exam 19 for second-highest on record, 15 behind Exam
  13's 955). Exams 15, 16, 18 remain unattempted (verify current list in EXAM-LOG.md — this line is a
  snapshot, not re-derived live). Real exam sitting: 2026-08-18 (tomorrow).
exams_scored: 14 (Insights Round 4 ran retroactively at Exam 20's generation session; next round due at 15
  — one more scored exam away)
weakest_domain: D3/D4 tied nominal at 83.3% each (Exam 20) — confirmed_weakness recorded FALSE (a tie
  fails the unambiguous-weakest bar). A data-quality finding (Q55 domain-mistagged D3, content is 100% D4
  §4.11 — see EXAM-LOG.md Finding 4, PB-30) means the corrected read is D4 ALONE weakest at 76.9%, which
  would satisfy the confirmed-weakness bar against Exam 19's unambiguous D4-weakest at 75% — flagged, not
  applied to the structured field, pending sign-off on correcting a shipped exam's domain tag.
recommendation: do NOT generate Exam 21 before tomorrow's sitting. Highest-value use of remaining time is
  a direct re-read of CCA-Prep_Domain-4_v2.md §4.11 (Batch API tool support — missed twice in Exam 20,
  Q42 and Q55) and §4.6 (tool_choice over-specification — now confirmed twice, Exam 19 Q23 + Exam 20 Q48),
  plus CCA-Prep_Domain-3_v2.md §3.7.4 (feedback-batching axis, resurfaced untargeted at Q58).

## Session 2026-08-17 — Exam 20 scored (56/60, 940), one day before the real sitting

**What was asked:** log Exam 20's results-json paste-back.

**Findings, ranked:** (1) NEW — the Batch API's tool-support fact (`§4.11`) was missed twice in one
sitting, Q42 and Q55, both resting on the same underlying claim (batch requests CAN define tools; the real
limit is no mid-request pause-to-execute). (2) CONFIRMED a second time — D4 §4.6 tool_choice
over-specification (Exam 19 Q23, Exam 20 Q48 — the deliberate clean second test Exam 19's own Professor's
Note asked for, and it came back wrong again). (3) D3 §3.7 feedback-batching axis-confusion (Q58)
resurfaced untargeted, the same section Exam 17 flagged and Exam 19 cleared untargeted — this project's
recurring "section gap that opens and closes without warning" shape. (4) Data-quality: Q55's `domain`
field reads D3 but every citation in the question is D4 §4.11 — logged as **PB-30** in
GENERATION-INTELLIGENCE.md; the fidelity gate's check 4 verifies block-level tallies, not per-question
domain-vs-citation match, so this kind of mistag can ship undetected.

**Also fixed this session:** `DASHBOARD-DATA.jsonl`'s Exam 14 row had never been backfilled after Exam 14
was scored 2026-08-15 (still showed `attempted_date: null`) — corrected from EXAM-LOG.md's existing "Exam
14 — SCORED 2026-08-15 (49/60, 835)" entry, a pure backfill, no new judgment calls.

**Not done, deliberately:** no Exam 21 generated. With the real sitting less than 24 hours out, this
project's own repeated finding (reaffirmed at Exam 20's own generation session) is that reviewing specific
corpus sections beats producing another full paper this close to the exam.

---

## PRIOR STATE (before 2026-08-17)

status: COMPLETE
phase: EXAM_20_GENERATED
started_at: 2026-08-16
completed_at: 2026-08-16
exam_file: mock-exams/CCA-Prep_MockTest-20_v1.html (unattempted, Exam Mode)
format: FULL60
score: Exam 19 SCORED 2026-08-16 (56/60, 940 — highest on record, first sitting under Exam Mode).
  Exam 20 generated same session. Exams 15, 16, 18, 20 unattempted (verify current list in EXAM-LOG.md —
  this line is a snapshot, not re-derived live).
exams_scored: 13 (Insights Round 3 fired at 9; Round 4 was due at 12/missed, run retroactively this
  session — see EXAM-LOG.md and GENERATION-INTELLIGENCE.md PB-28; next round due at 15)
weakest_domain: D4 at 75% (Exam 19) — suspected, NOT confirmed (Exam 14, the true immediate predecessor
  by attempt date, was weakest at D3 67%; different domain). Base quota applied to Exam 20.

## Session 2026-08-16 — Exam 19 scored, full historical review, Exam 20 generated in Exam Mode

**What was asked:** score Exam 19, explain what to focus on before the 2026-08-18 sitting, then "generate
the next exam... do a full review of what was done in the past to see weak areas... stick to the format
of Exam 19, where it is in exam mode."

**Exam 19 scored 56/60 (940/1000)** — highest on record, first paper taken under Exam Mode (no
per-question feedback). Misses: Q23 (D4 §4.6, tool_choice over-specification, new direction), Q58 (D4
§4.5, prevention-vs-repair, a confirmed repeat of Exam 17's pattern), Q35 (D4, select-2, schema-scope
confusion), Q53 (D2, description-vs-examples — later corrected to §2.2, not §2.1).

**Full historical review found two real process gaps, both fixed before Exam 20 was planned** (see
GENERATION-INTELLIGENCE.md PB-28, PB-29 and EXAM-LOG.md "Insights Round 4"):
1. Insights Round 4 was due 2026-08-15 (exams_scored hit 12) and never ran. Run retroactively — window
   Exam 13→17→14. Recovered a real finding: D3 was confirmed weak that window, then recovered cleanly
   (12/12) on Exam 19, untargeted.
2. Exam 19's own confirmed-weakness check had used the wrong comparator (Exam 17 instead of Exam 14, the
   true immediate predecessor by attempt date). Outcome unchanged; reasoning corrected.

**Exam 20 generated** — FULL60, Exam Mode (same variant as Exam 19), 4 parallel block sub-agents (all
four stalled simultaneously on first dispatch, a documented recurring infrastructure issue — resumed, not
restarted, zero rework lost). Draws Multi-Agent Research, Developer Productivity, Structured Data
Extraction, Claude Code CI (rests Customer Support, Code Generation). Base quota, no domain confirmed
weak. Targets, in priority order: D2 §2.8 (5-miss oldest trap, both directions), D4 §4.5 (2 confirmed
instances, 3 fresh facets), D4 §4.6 (1 miss, needs a clean second test), D2 §2.2 (1 miss), D3 §3.1/§3.8
(1 confirmatory item only, per the recovery finding).

**Fidelity gate (`tools/archetype_gate.py`): ALL 7 CHECKS PASS**, including 0 archetype collisions
against 1,133 prior stems — the largest prior-stem set this check has run against. First pass failed 2
checks (2 false-positive invented-name flags, stem median 59 vs the 50-55 band); both fixed by targeted
prose edits, facts/citations unchanged.

**Files updated this session:** EXAM-LOG.md (Exam 19 score, Insights Round 4, Exam 20 skeleton — all
appended, nothing overwritten), GENERATION-INTELLIGENCE.md (header, KD-tracker-gap notice, Scenario Block
Rotation table through Exam 20, 4 new/renumbered Open Findings Ledger rows PB-26/27/28/29, Session 21
reflection), DASHBOARD-DATA.jsonl (Exam 19's real score was never appended at scoring time — fixed here;
Exam 20 skeleton row added), this file.

**Not verified interactively in a browser this session** — see the chat transcript for why (the
available browser tooling couldn't load a local file with working JS in this environment). The shipped
HTML was verified via `node --check` (JS syntax valid) and the mechanised fidelity gate against the
actual shipped file (not just the pre-assembly JSON). Recommend Ram do a quick manual click-through of
Exam 20 before relying on it, same as was flagged for Exam 19.

**Next action:** attempt Exam 20 if there's time before 2026-08-18, or sit whichever unattempted papers
remain — this project's own repeated finding (Session 19) is that sitting existing papers is more
valuable than generating further ones this close to the real exam.

---

## PRIOR STATE (before 2026-08-16)

status: COMPLETE
phase: EXAM_17_SCORED
started_at: 2026-08-14
completed_at: 2026-08-14
exam_file: mock-exams/CCA-Prep_MockTest-17_v1.html (scored), CCA-Prep_MockTest-18_v1.html (unattempted)
format: FULL60
score: Exam 17 SCORED 2026-08-14 (51/60, 865). Exams 14, 15, 16, 18 unattempted.
exams_scored: 11 (Insights Round 3 fired at 9; Round 4 fires on the NEXT scored paper)
weakest_domain: D2 73% and D3 75% — treat as TIED, not ranked. Each concentrates in two sections
  (D2 §2.5 x2 + §2.9; D3 §3.7 x2 + §3.2), so target sections not domains. Base quota for Exam 19.

## Exam 17 — scored 2026-08-14 (51/60, 865), 37:58

**The tool_choice error is closed.** Four items tested it in four directions; three landed. Q21 — the same
"which configuration guarantees a tool call" shape missed twice in fourteen hours on Exams 12 and 13 — was
answered correctly after 138 seconds, the longest question on the paper. Different stem, different
scenario, different tagged domain, so this is not recognition. The item both prior Professor's Notes called
the highest-priority in the corpus is resolved.

**What replaced it is narrower.** Q36 needed a specific named tool because that tool's schema is the
pipeline contract; `any` was chosen — a real guarantee that is weaker than the requirement. New framing for
Exam 19: match guarantee strength to what the requirement specifies. The old "probabilistic control over an
available guarantee" framing is retired.

**Transfer failure worth more than a coverage gap.** Q2 (PostToolUse vs PreToolUse, asked directly) was
right. Q19 (the same prevention-vs-detection distinction dressed as tool design) was wrong — a PostToolUse
hook discarding a response after the internal endpoint had already been called. The rule is known and does
not travel out of the hooks frame.

**Cleanest section gap: D3 §3.7.** Q50 treated "rewrite the prose more precisely" as complementary to
worked examples rather than superseded by them. Q54 split feedback on a mechanical-vs-substantive axis
instead of interacting-vs-independent. Both are wrong-axis errors, not missing facts.

**The .claude/rules/ reflex is now speed-dependent.** Same three-way discrimination twice: Q9 right at 99
seconds, Q41 wrong at 32 seconds. Fourth wrong instance across three papers.

**Timing caveat that revises Insights Round 3.** Round 3 said the clock is never binding, so slowing down
costs nothing. He did slow down (138s, 106s, 91s against a 38s average) and got one of those three right,
while four of nine misses came in under 40 seconds. The fast misses are the recoverable ones; the slow
misses are genuine reasoning errors.

**Multiple-response cost 2 marks for 2 half-right answers** (6/8, both misses partial).

Written to EXAM-LOG.md: the scored entry plus **Professor's Note — Intent for Exam 19**. DASHBOARD-DATA.jsonl
updated (11 scored). Exam 18 row added, insight_round_due true.

**Immediate action available for the first time: import this result into the drill deck.** The mock map was
repaired earlier the same day, and this results JSON boosts 67 distinct cards with zero unmatched questions
— 18 on D1 §1.1, 19 across D2 §2.5/§2.9, 16 across D3 §3.2/§3.7, 14 across D4 §4.6/§4.7. First scored paper
whose misses reach the spaced-repetition layer.

## Exams 17 and 18 — generated 2026-08-14 from an independent trap inventory

**What is new about these two papers.** They are the first generated from a second community source: a
local mirror of `claudecertificationguide.com` at `Outputs/ccg-mirror/` (57 pages, 72,486 words, crawled
2026-08-14), from which **121 "Exam Trap" blocks** were extracted as a seed pool. That site is registered
as source-authority item 4 in `CCA-Prep_Corpus-Index_v2.md` v2.2 — same non-authoritative tier as
`guide_en.md`. The traps supplied **distractor geometry only**; every rationale on both papers cites the
v2 corpus, and the coverage cross-check found the site adds **zero new task statements**.

**Scenario draws.** Both are previously-unused 4-of-6 draws, solved as a constraint problem over all 15
possible draws: Exam 17 is CS+MR+CI+SD, Exam 18 is CG+DP+CI+SD. Together they cover all six official
scenarios. After these two, the only unused draws left are CS+CG+MR+DP (infeasible — no D4-primary block
against a 12-question D4 quota) and CS+CG+CI+SD (one D1-primary block against a 16-question D1 quota).

**Both Professor's Notes for Exam 17 are consumed, and the tool_choice instruction is met in full.** The
note asked for three items in three scenarios with three different keys. Exam 17 carries four:
Q21 `any` correct, Q36 forced-specific correct, Q48 `auto` correct, Q14 forcing `any` is the defect.
Four directions, so no memorised rule answers them. The where-does-this-live family gets three-way
discriminations at Exam 17 Q9/Q41 and six items across Exam 18.

**Compensating-mechanism geometry** — the shape behind five of Exam 12's seven misses, which the Insights
Round 3 note said no domain-weighted quota can target — is built into 13 items on Exam 17 and is the
default distractor shape on both papers.

**A site-vs-corpus conflict was found and handled rather than absorbed.** The mirror's D1 traps
1.30/1.32/1.34 state that `--resume` after file changes is always a trap and a fresh session with summary
injection is always right. Corpus D1 §1.16's worked exam pattern says the opposite for the 3-of-50-files
case. Rather than pick a side, Exam 18 tests all three mechanisms separately — Q11 resume-and-inform,
Q44 fresh-plus-summary, Q4 fork — with the corpus's staleness criterion as the discriminator. The
mirror's claim that MCP transport selection may be tested was rejected outright: the official
out-of-scope list bars server-sent events and MCP hosting, so no transport question appears on either
paper.

**Verification.** Both papers pass all 7 archetype-gate checks. Dedup was run by Jaccard against 886
prior stems (810 from EXAM-LOG Exams 2–16 plus the 76 community stems): Exam 17 max 0.367, mean 0.153;
Exam 18 max 0.196, mean 0.134; zero stems at or above the 0.40 reskin threshold on either. The gate also
checked Exam 18 against Exam 17's stems — 0 collisions.

**Known deviations, reported not hidden.** Exam 17's inline code/config token rate is 27.5% and Exam 18's
is 17.1%; both sit inside the gate's 15–30% pass band, on either side of the 20–25% target. Exam 17's is
driven by its `tool_choice`/MCP/CLI concentration, Exam 18's by subject matter that runs to mechanisms
rather than parameter values.

**Next action for Ram:** sit Exam 14 (the oldest unattempted paper) or go straight to 17 — the two new
papers are the ones targeted at the twice-repeated `tool_choice` miss. Paste the results JSON back to
score it and trigger the Professor's Note for Exam 19.

**RESOLVED 2026-08-14 — the drill deck's mock map now covers all 18 papers.** It previously covered only
Exams 2, 3, 4 and the Exam-2 retrofit, so importing any recent result failed with "No question map for
exam N". Two separate faults, both fixed in `drill/build_deck.py` (the canonical pipeline, not the pack
copy):

  1. **The map was never regenerated.** `extract-mocks` parses every paper correctly and had simply not
     been re-run since Exam 4. Re-running it picked up all 18 papers, 1,080 questions.
  2. **The citation vocabulary did not join.** This was the fault that mattered. Cards carry
     `Domain-2_v2 SECT2.9`; papers cite it three other ways depending on which generation of the
     generator wrote them — `D2 SECT2.9` (Exams 5-10), `CCA-Prep_Domain-2_v2.md SECT2.9` (Exams 11-18),
     and composite `Key Distinction #6` forms. `canonicalize_cite` only understood the first, so even
     after regenerating the map **only 27.7% of questions joined any card** and the import would have
     looked like it worked while boosting almost nothing. The normaliser from
     `Outputs/_packbuild/remap_deck.py` — written to patch the prep-pack copy only — was ported into
     `build_deck.py` and extended: it now folds all four spellings, expands a sub-section cite to its
     parent as well as itself (the old code replaced it, losing any card written at the finer grain),
     and splits the one paper that writes `SECT1.15, SECT1.6` as a comma-separated pair.

  **Coverage after the fix: 1,079 / 1,080 = 99.9%** (was 299/1,080 = 27.7%). Deck re-embedded at
  deckVersion 2; `validate` passes 366 cards with no issues. Verified by simulating the deck's own
  `parseImport` join against the embedded payload: every paper boosts 240-318 distinct cards with zero
  unmatched questions, and **the twice-repeated `tool_choice` miss now lands** — Exam 12 Q33 boosts 9
  cards, Exam 13 Q46 boosts 14, and both include `d4-020`, the shared card. That is the spaced-repetition
  path that was dead at the exact moment it would have paid for itself.

**Two findings left open, both reported rather than silently fixed:**

  - **The deck has no card for Key Distinctions #26-29.** Cards exist for #1-25. The four missing ones
    are the built-in-tools additions from Key-Distinctions v1.1 — Grep vs Glob, Edit vs Read+Write,
    incremental investigation, MCP vs built-in preference. This is the single remaining unmatched
    question (Exam 10 Q18, citing #29) and it is a content gap, not a plumbing one. Exam 17 Q40 and
    Exam 18 Q7/Q13/Q18/Q56 all test this family, so four cards would close it.
  - **The deck's study schedule is stale.** It still reads "Mon 08-11 sit Mock 2", "Wed 08-13 Mock 3",
    "Fri 08-15 Mock 4" — dates now past, pointing at the three oldest papers while five sit unattempted.
    The schedule is the `SCHEDULE` constant in `build_deck.py`. Which papers to sit on which day is
    Ram's call, so it was left alone.

  - `Outputs/_packbuild/remap_deck.py` now duplicates logic that lives in `build_deck.py`. It still
    works and targets the pack copy, so it was not touched, but it is the place to look if the two
    ever disagree.

weakest_domain: none confirmed. Exam 13's nominal weakest (D2 at 91%) was a denominator artefact — D2,
  D3 and D4 each lost exactly one question. Base quota applied to both Exams 17 and 18.

---

## PRIOR STATE (before 2026-08-14)

status: COMPLETE
phase: EXAM_GENERATED
started_at: 2026-08-11
completed_at: 2026-08-11
exam_file: mock-exams/CCA-Prep_MockTest-16_v1.html (Exams 14 and 15 generated earlier the same day)
format: FULL60
score: Exam 12 SCORED 2026-08-11 (53/60, 895); Exam 13 SCORED 2026-08-12 (57/60, 955 — best of ten).
  Exams 14, 15, 16 still unattempted.
exams_scored: 10 (Insights Round 3 fired at 9; next round at 12)

## Exam 13 — scored 2026-08-12 (57/60, 955) — best result across ten attempts

D1 **16/16** (first clean sweep of the heaviest domain), D5 9/9, D2 10/11, D3 11/12, D4 11/12. Blocks
15/14/14/14. Time 35:53 — fastest full sitting on record *and* the highest score, so speed is not costing
accuracy.

**Weakest domain is D2 at 91% — disregard it.** D2, D3 and D4 each lost exactly one question; D2 only
ranks lowest because it has 11 questions to their 12. This is the denominator artefact Insights Round 3
flagged one day earlier, arriving immediately. No confirmed weakness (Exam 12's weakest was D3/D4). Base
quota stands for Exam 17.

**THE FINDING: Exam 13 Q46 repeats Exam 12 Q33 exactly, and the same wrong option was chosen both times.**
Both ask which configuration *guarantees* a tool call; both offer `tool_choice: auto` + a prompt
instruction as the trap and `any` as the key. Picked the trap on 2026-08-11 and again on 2026-08-12,
~14 hours apart, **having read the full rationale in between**. The two stems measure **0.118 Jaccard** —
far under the 0.40 reskin threshold, different scenarios, different tagged domains. So this is **not**
recognition of a repeated question: it is an actively held wrong preference, and it is the single most
valuable diagnostic in ten scored papers.

Secondary: **`.claude/rules/` is now a confirmed reflex** — third wrong pick across two papers (e12 Q1
where the answer was `/memory`; e12 Q56 where it was `.claude/commands/`; e13 Q41 where it was to delete
prose from `CLAUDE.md`). Three different right answers, one recurring wrong instinct.

The compensating-mechanism pattern **persisted but attenuated** — Q46 took a probabilistic control over an
available guarantee, and Q19 changed tool behaviour rather than fixing the description; but the obvious
post-processing workaround in Q19 was correctly rejected.

Written to EXAM-LOG.md: scored entry plus **Professor's Note — Intent for Exam 17 (second note)**, which
promotes `tool_choice` from "a section to cover" to the highest-priority corpus item for this learner.

**Blocker worth naming: the drill deck cannot consume either result.** Its mock map still covers only
Exams 2, 3, 4 and the Exam-2 retrofit, so the mechanism that would turn a twice-repeated miss into spaced
repetition is not running at the exact moment it would pay for itself.
weakest_domain: D3/D4 tied at 83% on Exam 12 — NOT confirmed (Exam 11, the prior scored paper by attempt
  chronology, was weakest D5). Base quota applies to Exam 17. D2 adjustment retired: it was confirmed weak,
  Exam 12 ran the +4 quota at 15 questions, and D2 returned 87% — the experiment worked.

## Exam 12 — scored 2026-08-11 (53/60, 895)

Full results-json. Blocks flat at 13/13/14/13; D5 7/7; D1 93%; D2 87%; D3 83%; D4 83%. Time 42:40 of the
120-minute allowance — **77 minutes unused.**

**The finding that matters: five of the seven misses are one error, not five.** Q1, Q6, Q17, Q33 and Q57
each reach for a compensating mechanism instead of the root-cause fix or an available deterministic
guarantee — build a rules file rather than run `/memory`; post-process output rather than give examples;
grant a retrieval tool rather than pass context the coordinator already holds; `auto` plus a prompt rule
rather than `{"type": "any"}`; a synchronous fallback rather than submitting a day earlier. It spans four
of five domains, so **no domain-weighted quota can target it.** The generation lever is question geometry:
build items where a plausible workaround is present and attractive alongside the correct fix.

Secondary: `.claude/rules/` was picked wrongly **twice on one paper** (Q1, Q56) — it is acting as a default
answer to "where should this live?". And five of seven misses took under 40 seconds: these are fast
confident errors, not time pressure.

Written to EXAM-LOG.md: the scored entry, the **Professor's Note — Intent for Exam 17** (numbered 17, not
13, because Exams 13–16 were all generated before this score arrived — the Exam 9→12 skip precedent), and
**Insights Round 3** (fired at 9 scored exams). DASHBOARD-DATA.jsonl row updated.

## Exam 16 — the even-load paper

Ram asked for one more paper, again because compute was expiring. The concern was stated first — four
papers already unattempted, seven days to the sitting — and the paper was built, since that is his call.
**Five papers are now unattempted: 12, 13, 14, 15 and 16.**

PURPOSE: it is the flattest domain load the scenario bank permits. No block carries more than five
questions of any single domain, against twelve in Exam 15's extraction block. That is the one thing the
other four unattempted papers cannot offer.

DRAW: Customer Support; Multi-Agent Research; Developer Productivity; Claude Code for CI. **This is the
first paper where rotation and the never-used-set rule conflict** — the four least-used scenarios form
`{CS, CG, MARS, CI}`, which Exam 7 already used. Ten of the fifteen 4-of-6 sets are used, one of the
remaining five is infeasible (no D4 carrier), and all four survivors level the rotation identically, so
the tiebreak used was minimum-maximum-cell: only this draw keeps every block at or below 5 of one domain.

ALL SEVEN GATES PASS on the shipped file, computed by `tools/archetype_gate.py`, not hand-tallied:
0 invented names; SA letters A11 B12 C12 D12 matching the pre-plan exactly; stems 43/54/62 with option
max 25; block primacy holds in all four blocks (margin exactly 1 everywhere — what "flattest" costs);
inline token rate 20.6%; 13 well-formed MR items; **0 archetype collisions against 893 prior stems** and
0 intra-paper.

THE GATE EARNED ITS KEEP AGAIN. First pass failed six of seven checks: four invented-name flags
(`Briefings`, `Yesterday`, `Monday` twice — weekday names are not in the allowed-proper list), a stem
median of 46 against the binding 50–55 band, a 14.4% inline-token rate, a select-count phrasing the MR
validity check cannot read ("Select the two named patterns" → reworded to close on "Select two."), and
two questions in one block closing on the identical sentence. All 81 fixes are asserted fragment
replacements in `WIP-EXAM16/patch_gates.py`, so the edit set is auditable. **Archetype collisions were
zero on the first pass** — the opposite of Exam 15, which needed 16 stems rebuilt. The difference is that
no prior exam's stem ledger entered this session's context before authoring.

VERIFIED IN BROWSER through the page's own handlers: single-answer lock-and-reveal both paths, MR toggle
and commit-at-N on select-2 and select-3, the "belongs in the answer" state for unpicked correct options,
all three resume branches, Back/Next disabled states, the 60-chip jump map, the accuracy pill exact at the
620/900 threshold (31/45 = 68.889% green, 30/45 red), the pass boundary exact at 42/60 = 730 and
41/60 = 715, print-all rendering 60 questions then tearing down, and the export schema with `item_formats`
and per-question `type`. Console clean bar a favicon 404. localStorage cleared — ships unstarted.

FOUND, NOT FIXED: Exam 15's four block narratives carry literal `<code>` tags in their DATA payload. The
template escapes HTML before converting backticks, so a reader sees the tags as text. Narrative cards
only — no stem, option or rationale is affected. Left alone because Exam 15 is unattempted and Ram may
still sit it.

## Exam 15 — generated after Exam 14, same session

Ram asked for one more paper because compute was expiring. The concern was raised — three papers already
unattempted, seven days to the sitting — and the paper was built anyway, since that is his call and
generation is cheap against losing the compute. **Four papers are now unattempted: 12, 13, 14 and 15.**

PURPOSE: the companion to Exam 14, not a harder paper. Exam 14 covers the four scenarios it drew; Exam 15
covers the two it rested (Customer Support, Code Generation), so the pair spans the full official scenario
bank. Same difficulty, same ban-list, same base weighting, same 13 multiple-response items.

DRAW: Customer Support; Code Generation; Developer Productivity; Structured Data Extraction. Nearly
forced — requiring both of Exam 14's rested scenarios leaves only two unused 4-of-6 sets, and one of them
is infeasible (Customer Support would be the sole D1-primary block, and D1 needs 16 in a 15-question
block). Exactly one candidate survived.

ACCEPTED TRADE-OFF: any draw with both Customer Support and Code Generation has a single D4 carrier, so
Structured Data Extraction absorbs all twelve D4 questions in fifteen. Ram was shown this and chose the
skew over deviating from official weights or dropping Code Generation for a third consecutive paper. It
also pulls the inline-token rate to 16.0% — passing, but below Exam 14's 21.8% — because code tokens live
in D2/D3 options and that block has almost none. Tokens were not forced in.

ALL SEVEN GATES PASS on the shipped file. Verified in browser: single-answer lock-and-reveal, MR toggle
and commit-at-N on both select-2 and select-3, correct and wrong MR feedback including the
"correct — not picked" state, all three resume branches, pass boundary exact at 42/60 = 730 green and
41/60 = 715 red, export schema with `item_formats` and per-question `type`. localStorage cleared, so it
ships unstarted.

**THE FINDING THAT MATTERS MOST THIS SESSION.** Exam 15's first draft failed the archetype gate with
**16 of 60 stems** at or above 0.40 Jaccard against prior exams — two at 0.841 and 0.821, near-verbatim
reproductions of Exam 13 questions. Authoring had consulted no prior stem. The leak came from reading
Exam 13's full 60-stem header ledger hours earlier, while studying the HTML template to add
multiple-response support. **This disproves PB-23's recommendation (b) — "draft from corpus text alone"
— as a standalone control, because a session cannot govern when the ledger enters its context for
unrelated reasons. The mechanised scan is what holds the line, and it must be run on every exam.** All 16
were rebuilt around genuinely different situations; final state is 0 collisions. Recorded in PB-23 and
Session 19 of GENERATION-INTELLIGENCE.md.

Also caught: Q57's correct answer drifted from its pre-planned letter D to C during option drafting; the
per-block check found it and options were reordered without touching content, per Phase 4.e.5.

## Exam 14 — generated earlier the same session

## READ THIS FIRST — new binding artifact

`QUESTION-ARCHETYPE-BANLIST.md` (new, 2026-08-11) is binding on every exam from 14 onward.
It defines a **seventh Phase 4.e.6 check — ARCHETYPE COLLISION** — and names nine banned
question shapes with their approved re-frames. Read it before authoring any question.

`tools/archetype_gate.py` (new) computes fidelity checks 1–5, the new check 7, and a
multiple-response validity check, directly from a shipped exam HTML or a questions JSON:

    python tools/archetype_gate.py mock-exams/CCA-Prep_MockTest-14_v1.html

Orchestration-prompt v10 still describes these gates as hand-tallied and lists only six
checks. **Editing v10 to reference the ban-list and the script is an open decision for Ram**
— it changes a stated contract, so it was flagged rather than done silently. Until then, this
file is the pointer that makes the ban-list discoverable.

## What this session did

Ram asked for one more mock exam, and asked whether the earlier exams could stop repeating
patterns — specifically the case studies and problem statements — with a "totally refreshingly
new set of scenarios."

An audit of all 720 questions across Exams 2–13 (12 unique papers, parsed from the shipped
HTML) located the repetition precisely:

- **Scenario rotation is healthy.** All six official scenarios sat at exactly 8 draws.
- **Block narratives are healthy.** Same-scenario narratives average 0.12–0.16 Jaccard.
- **The repetition is in the question archetypes.** Nine reskinned families, worst being the
  dry-run/token-binding question appearing in seven exams (4, 5, 6, 7, 10, 11, 13) with only
  the tool name changed, and the paired-tool-calls question in four (6, 8, 10, 11) measuring
  0.717 Jaccard between Exam 10 Q6 and Exam 11 Q9.
- **Closing-line monoculture.** 247 of 720 stems (34.3%) closed on a "most effective"
  construction; 81 closed on the byte-identical sentence "What is the most effective fix?"
- **Item-format gap.** Zero multiple-response items across 720 questions, although the
  official guide §2 states the exam uses them.

Four decisions were taken with Ram via popup:

1. **Fresh worlds, generic framing.** The naming ban (Phase 4.e.6 check 1) wins — it is
   grounded in an audit of 76 real exam texts and confirmed against all 12 official samples.
   Freshness comes from new industry territory instead. Ram's first answer had been "named
   worlds"; that option was written before v10's naming gate had been read, the conflict was
   flagged, and he re-decided.
2. **Multiple-response items, heavy drill** — 13 of 60 (Ram chose the largest option).
3. **Ban-list written into the generation system**, rather than patching old exams.
4. **Adversarial calibration** — re-frame the archetypes he has been getting *right*, past
   recognition, on the theory that part of the recent 54–55/60 may be template recognition.

## Exam 14 specifics

QUOTA: base weights, D1 16 / D2 11 / D3 12 / D4 12 / D5 9. No weakness adjustment (Exam 9
weakest D2, Exam 11 weakest D5 — different domains, so the two-consecutive gate is not met).

SCENARIOS DRAWN: Multi-Agent Research System; Developer Productivity with Claude; Claude Code
for Continuous Integration; Structured Data Extraction. All six scenarios stood at 8 draws, so
the rotation rule could not discriminate; selection fell to the never-used-combination rule.
Of the 15 possible 4-of-6 draws, 8 were already used. Of the 7 unused, 3 are infeasible against
this quota (two cannot carry D1 16 with a single D1-primary block; one has no D4 carrier at
all). This is the only feasible unused draw where every domain has two carrier blocks, and it
rests both of Exam 13's other two scenarios.

ITEM FORMATS: 47 single-answer + 13 multiple-response (9 select-2-of-5, 4 select-3-of-6),
scored all-or-nothing. This is a deliberate, Ram-approved deviation from v10 Phase 4.e's
"exactly 4 options — 1 correct". The exam HTML engine was extended to support it: checkbox
rendering, a "Select N" banner with a live count, toggle-and-commit-at-N behaviour, persisted
in-progress selections so resume works mid-selection, set-based scoring, a by-item-format
results card, and an export schema carrying `type` and comma-joined `selected` letters.

INDUSTRY TERRITORY (all new): clinical-evidence synthesis; hospital patient-flow tooling;
telecom provisioning CI; agricultural commodity trade documents. Generic framing throughout.

AUTHORED CENTRALLY, not delegated — the adversarial-calibration goal requires prior stems in
the drafting context, and Ram's global instructions forbid unrequested subagent use. The
dedup risk that central authoring creates (logged previously as PB-23) was handled by running
the mechanised gate rather than by a by-hand scan.

ALL SEVEN GATES PASS on the shipped file: 0 invented names; SA letters A12 B12 C12 D11; stems
42/50/59 with option max 21; block margins 3/3/3/4; inline token rate 21.8%; 13 well-formed MR
items; 0 archetype collisions against 773 prior stems and 0 intra-paper.

GATE CAUGHT TWO REAL DEFECTS during authoring: Q52 was a 0.431 reskin of Exam 12 Q50 and was
rewritten onto §4.8's other half; and the paper's stem median came in at 41 words against the
50–55 band, so all 60 stems were lengthened with concrete situational detail.

VERIFIED IN BROWSER (localhost:8765, engine exercised through real click handlers): landing
card with the verbatim rotation-disclosure line; single-answer lock-and-reveal; MR toggle on
and off; commit at exactly N; post-commit clicks ignored; correct-path and wrong-path MR
feedback including the "correct — not picked" missed-option state; all three resume branches
(fresh → landing, partial → first unanswered, complete → results); pass boundary exact at
42/60 = 730 green and 41/60 = 715 red; export JSON schema including `item_formats` and
per-question `type`. localStorage was cleared afterwards, so the file ships unstarted.

## Repairs made in passing

- **DASHBOARD-DATA.jsonl was missing its Exam 13 row entirely** — it jumped from 12 to 14.
  Added, and the file is now sorted by `exam_n` with all 14 rows present.
- Validating the new gate against the back catalogue surfaced three defects in Exam 13 that
  the by-hand process shipped: one 0.435 Jaccard collision with Exam 10 Q55, one option at 36
  words against the 35-word cap, and three repeated closing sentences inside a single block.
  **Not fixed** — Exam 13 is unattempted and Ram may still sit it; changing it now would
  invalidate that. Recorded here so a future session can decide.

## Working-directory note

This session opened in `.claude/worktrees/nostalgic-davinci-9a0d97`, which launch-prompt §0
forbids — that worktree is behind master and holds only Exams 2–4. All work targeted the main
checkout via absolute paths. One file was added inside the worktree: `.claude/launch.json`,
a preview-server config used for browser verification. `.claude/` there was already untracked.

## Not committed

The repo is public. Exam 14's questions, answer keys and rationales become publicly readable
if pushed, as would the ban-list's inventory of every prior exam's weak spots. Awaiting Ram's
decision.

**Git state, verified 2026-08-11 after a fresh fetch — master has DIVERGED, so a push would be
rejected as-is:**

    ## master...origin/master [ahead 3, behind 2]

- **Ahead 3** (local, never pushed): `d849f50` Score Exam 11 + drill-deck guide-v1.0 fidelity fix;
  `a8025a5` merge of `claude/nostalgic-davinci-9a0d97`; `2400f6b` drill deck + Launchpad links.
- **Behind 2** (on origin, not pulled): `a60c3a6` Link Mission Control cheat sheet into Launchpad;
  `d27d31a` Add CCA-F Mission Control exam cheat sheet.
- **Uncommitted/untracked:** modified `EXAM-LOG.md`, `SESSION-STATE.md`, `DASHBOARD-DATA.jsonl`,
  `GENERATION-INTELLIGENCE.md`; untracked `QUESTION-ARCHETYPE-BANLIST.md`, `tools/`, `WIP-EXAM14/`,
  `mock-exams/CCA-Prep_MockTest-13_v1.html`, `mock-exams/CCA-Prep_MockTest-14_v1.html`, and several
  files under `Outputs/`. **Exam 13 has been untracked since 2026-08-11 with no decision recorded.**

Reconciling the divergence needs a pull/rebase before any push. Note `a60c3a6` **modifies the
Launchpad**, which is also where the "only Exams 2–4 are linked" gap lives — resolve the incoming
change first, then decide about the missing exam cards, or the two edits will collide.

## DEFECT FOUND IN THE DRILL DECK — affects Ram's own prep this week

While building the colleague distribution pack, the drill deck's mock-results importer was
exercised properly for the first time. **`prep with quiz/drill/CCA-Prep_Drill_v1.html` can only
import results from Exams 2, 3, 4 and the Exam-2 retrofit.** Its embedded `mockMap` — the
per-exam question-to-citation map the importer needs — contains exactly those four keys:

    top-level exam keys: ['2', '3', '4', '2-retrofit']

Pasting Exam 9, 11, 12, 13, 14 or 15 results produces *"No question map for exam N. The deck was
built before that exam existed."* and boosts nothing.

**Cause:** `build_deck.py`'s `extract-mocks` step reads `MOCKS_DIR = prep with quiz/mock-exams`.
The deck was built on 2026-08-10 from a session running in the
`.claude/worktrees/nostalgic-davinci-9a0d97` worktree, which holds **only Exams 2–4**. The map
was therefore generated against three papers instead of thirteen.

**This contradicts a claim in this file's own 2026-08-10 entry** — "dry-run confirmed all 5 missed
questions match at least 2 cards each" for Exam 11. That cannot have exercised the mockMap path,
because Exam 11 has no map. Treat that line as unverified.

**Fix:** re-run the deck build from the **main checkout** (not a worktree) so `extract-mocks` sees
all the papers, then re-embed. A worked reference implementation of the remap exists at
`Outputs/_packbuild/remap_deck.py`, which regenerates the map directly from the shipped exam HTML
and folds the four different citation spellings the generations use onto the deck's card
vocabulary — that normalisation is the non-obvious part and is what takes coverage from 30% to
100%. Until this is fixed, importing exam results into the drill deck does nothing for Ram.

## Next action — stop generating, start sitting

**Four papers now sit unattempted: Exams 13, 14, 15 and 16** (Exam 12 was scored 2026-08-11), with the
real exam on **2026-08-18 — seven days out**. The scarce activity is sitting them, not producing more.
A seventeenth would add coverage there is no evening left to consume.

Suggested order across the four, if only three get sat: **14, then 16, then 15.** Exam 14 is the
calibration read (no recognisable question shape). Exam 16 is the second read on that, and the only paper
whose blocks switch domain the way the real exam's do — a good proxy for whether the score survives
losing the single-domain rhythm. Exam 15 third, for the two scenarios 14 and 16 both rest (Code Generation,
Structured Data Extraction) — between the three papers all six official scenarios are covered. Exams 12
and 13 remain the lower-value pair: 12 predates the ban-list, and 13 carries three known defects left in
place deliberately.

The older two-paper note below is superseded but kept for its per-paper reasoning:

1. **Exam 14 first.** It is the calibration read: if the 54–55/60 band holds on a paper where no
   question shape is recognisable, the score means what Ram wants it to mean. If it drops
   sharply, the gap is real and the drill deck should be re-weighted toward whatever falls.
   Watch **Q26** — D2 §2.8, missed on four separate papers, rebuilt as a select-3-of-6 from the
   opposite end.
2. **Exam 15 second**, for the two scenarios Exam 14 does not touch.

On both, watch the multiple-response items as a group. The results card reports single-answer and
multiple-response accuracy separately, so a format problem stays distinguishable from a knowledge
problem — which matters, because Ram has never sat one before this week.

Exams 12 and 13 remain available but are the lower-value pair now: 12 predates the ban-list, and 13
carries three known defects (a 0.435 collision with Exam 10 Q55, one over-length option, three
repeated closing sentences) that were deliberately left in place rather than edited under him.
