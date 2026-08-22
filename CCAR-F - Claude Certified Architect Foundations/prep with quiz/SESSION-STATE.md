# Session State

status: COMPLETE
phase: SCORE_LOGGED
started_at: 2026-08-10
completed_at: 2026-08-10
exam_file: mock-exams/CCA-Prep_MockTest-11_v1.html (scored this session; Exam 12 remains the most recently generated, unattempted)
format: FULL60

## Score-entry note (2026-08-10, this session)

Exam 11 scored: 55/60 (925/1000). Weakest domain D5 (88.9%), not confirmed — the
prior scored exam by attempt chronology (Exam 9, 2026-08-09) was weakest in D2, a
different domain. D2's own confirmed-weakness streak from Exam 9 is broken here:
it recovers to 90.9% on Exam 11's standard (non-adjusted) quota, though this
doesn't yet test whether the recovery holds under Exam 12's larger, weakness-
adjusted D2 allocation, since Exam 12 remains unattempted.

Full breakdown, observations, and cross-referenced misses logged in EXAM-LOG.md
under "## Exam 11". Professor's Note — Intent for Exam 13 appended there (Exam 12
already exists, so per the Exam 9→12 skip precedent this note targets 13, the
next paper that can actually act on it). DASHBOARD-DATA.jsonl's exam_n:11 row
updated to match. exams_scored is now 8 — Insights Round 3 does not fire yet
(needs 9); it will fire the next time any exam is scored, most likely Exam 12.

One finding worth flagging outside the routine pipeline: Q9 (D2 §2.8, composite
tool vs. prompt-bundling for habitually-paired tool calls) was missed on this
exam exactly as it was on Exams 5, 8, and 10 — four separate sittings on a
section the corpus itself says carries exactly one teachable point. The CCA-F
drill deck (prep with quiz/drill/) already carried two cards on this fact
(d2-046, d2-047); both were retagged known-gap/d2.8 this session given the
now-confirmed four-exam pattern, and GAP_MINIMUMS in build_deck.py updated to
track it. Deck re-embedded as deckVersion 4.

Next action: paste the Exam 11 results JSON into the drill deck's Import view
(prep with quiz/drill/CCA-Prep_Drill_v1.html) to boost the matching cards —
dry-run confirmed all 5 missed questions match at least 2 cards each, so
nothing here needs a new card. Then continue toward sitting Exam 12.
score: Pending (generated this session, not yet attempted)
weakest_domain: D2 — CONFIRMED weak (Exam 10 81.8% → Exam 9 63.6%, by attempt chronology)
notes: >
  Exam 12 generated 2026-08-10 from CCA-Prep_Exam-12-Launch-Prompt_v1.md, which
  supplied the routing answer (generate, FULL-60) and four overrides postdating
  orchestration-prompt v10. No score entry this session; no Insights Round due
  (exams_scored stays at 7, not a multiple of 3).

  QUOTA: the confirmed-weakness D2-collision adjustment (+4 D2, −2 D5, −2 D1) —
  D1 14 / D2 15 / D3 12 / D4 12 / D5 7. First weakness-adjusted exam since
  Exam 6.

  SCENARIOS DRAWN: Code Generation with Claude Code; Multi-Agent Research
  System; Developer Productivity with Claude; Claude Code for Continuous
  Integration. Chosen by a computed feasibility check over all 15 possible
  4-of-6 draws. NEW FINDING: the adjusted quota makes THREE draws infeasible,
  not the one the launch prompt anticipated, and the newly binding constraint
  is D5 dropping to 7 (it cannot supply three D5-primary blocks), not the
  familiar D4-carrier rule. Of the twelve legal draws this is the only
  minimum-rotation-sum draw with no scenario on a two-exam streak; it rests
  Customer Support and Structured Data Extraction, both drawn in Exam 10 AND
  Exam 11.

  AUTHORED CENTRALLY, not delegated to four parallel sub-agents. Phase 4.b.6
  makes delegation optional, and PB-19 is caused specifically by blind sibling
  sub-agents. That trade worked on collisions and backfired on dedup — see
  below.

  TWO REAL DEFECTS CAUGHT BY THE GATES:
  1. 20 of 60 stems drifted into close paraphrase of prior exams, one at 0.833
     Jaccard (a reskin of Exam 9 Q48 differing only in a percentage and a field
     name). Root cause is the central-authoring choice: prior stems were in the
     drafting context. All 20 rewritten; final max 0.298, zero pairs above 0.30
     — matching what Exams 9 and 11 shipped. Logged as PB-23.
  2. Q19 (D2 §2.2) and Q37 (D2 §2.6) both reduced to "rewrite the tool
     description" — two different sections, one lesson. Invisible to the
     citation tally and the Jaccard scan; caught only by the mandatory
     side-by-side read of every repeated-section pair. Q37 reassigned to
     §2.6's .mcp.json/${VAR} facet. The corpus itself flags the equivalence
     (KD#29 "mirrors #10"), which is a detector no prior session has used.
  Also fixed: 4 questions whose correct option drifted from its pre-planned
  letter (Q5, Q11, Q26, Q29), caught by the per-block structural gate.

  ALL SIX Phase 4.e.6 gate checks PASS, computed on the shipped file: 0
  invented names; letters exact 15/15/15/15; stems 45/51.5/65 and options
  10/17/27 within caps; every block clears primary-vs-non-primary with margin
  2; inline token rate 26.7% (64/240); rotation disclosure present. Verified
  live in browser incl. the 31/45 = 68.89% pass boundary (green) and 30/45
  (red), all three resume branches, and the export reading "exam_n": 12.

  PB-21 RECONCILIATION CLEAN: every EXAM-LOG "Key Distinction budget" line
  cross-checked against the tracker — 0 unrecorded seeds across Exams 6–11,
  all 29 rows present. Exam 12's own 15 KD seeds written in at generation,
  marked pending.

  NEW: PB-22 (the 4–6 KD target is unreachable on a weakness-adjusted exam —
  D2 alone carries 8 of 29 KDs; Exam 12 hit exactly the 15 cap with one
  deliberate seed) is OPEN and escalated to Ram, NOT resolved by this session.
  PB-23 (central-authoring dedup risk) fixed for this artifact, process fix
  proposed for v11.

  Pending corpus decisions: NONE. All six CORPUS_GAP rows re-verified this
  session by direct read of their actual target files; all six remain FIXED.

  WORKING-DIRECTORY NOTE: this Claude Code session opened in
  .claude/worktrees/nostalgic-davinci-9a0d97, which launch-prompt §0 forbids —
  that worktree is 8 commits behind master, holds only Exams 2–4, and has no
  orchestration-prompt v10. All work targeted the main checkout via absolute
  paths; the worktree was left byte-for-byte as found.

  NOT COMMITTED. The repo is public; Exam 12's questions, answer keys and
  rationales become publicly readable if pushed. Awaiting Ram's decision, and
  six earlier commits remain unpushed on master.

  Next action: attempt Exam 12 and paste the results JSON. The open question
  is whether D2 recovers with 15 questions and full section breadth, or whether
  the 100% → 90.9% → 81.8% → 63.6% slide continues even with more attention.
  Exam 11 also remains unscored; scoring both would bring exams_scored to 9 and
  fire Insights Round 3.
