# CCAR-P Mock Test Papers 3 & 4 — Generation Prompt

**Written:** 2026-08-31, at the end of the session that generated Paper 2. This prompt exists because
Paper 2's own generation needed two attempts (the first failed 6-of-7 dispatches outright) before an
independent audit found the real cost/reliability drivers. This document bakes those findings in as
starting assumptions, not things the next session has to rediscover.

**Use this prompt to generate whichever of Paper 3 or Paper 4 is actually next** — do not assume which
one without checking (§2). Run it once per paper; Paper 4 has real structural differences from Paper 3
(direction inversion, gate mechanization, a corpus decision to surface) called out in §5.

---

## 0 — Session-continuity rule: save to disk continuously, not at the end

**This is the one rule that changed most since Paper 2, and it is not optional.** A generation session
can run for hours and consumes a large token budget; it can also be paused, interrupted, or simply run
out of room mid-task. Papers 1 and 2 both proved that background dispatches can also fail outright
partway through. Design the whole session around **cheap, frequent, durable checkpoints**, not one big
effort held in working memory until a single save at the end.

Concretely:

1. **Compute the central plan once, then write it to disk immediately**, before dispatching any
   authoring agent. Use a durable path inside the actual project tree — e.g.
   `prep with quiz/_PAPER<N>-STAGING/p<N>-slots.md` and `p<N>-shared-brief.md` — **never only the
   session's ephemeral scratchpad**. The scratchpad is tied to one session; a fresh session gets a
   different one and cannot find anything left only there. (This was a real bug in the Paper 2 session:
   an early `mkdir -p` from the wrong working directory created files at the wrong path entirely,
   caught only by chance. Verify the target path resolves inside
   `CCAR-P - Claude Certified Architect Professional/prep with quiz/` before writing anything, every
   time — `pwd` first if there is any doubt.)
2. **Every authoring dispatch writes its own output file the moment it finishes** — this is not new,
   it is §1's sub-batch rule (below), restated for the continuity point: small, immediately-persisted
   units of work are what make a mid-task interruption cheap to recover from. Losing one 5-6 item batch
   costs minutes to redo. Losing an entire domain's un-persisted output costs the whole domain.
3. **After assembly and after every fix pass, re-save the merged items file** (e.g.
   `_PAPER<N>-STAGING/items-assembled.json`) before moving to the next step. Do not hold the "current
   best version" only in conversation context.
4. **If the session is running low on budget or context and the paper is not finished, stop and write
   a resume prompt** — the same shape as `resume-prompt.md` from the Paper 2 session: what's done
   (with exact file paths), what's open, the exact next action, decisions already locked in, and
   gotchas. Do this *before* running out, not as a last gasp. A clean, honest handoff that a fresh
   session can pick up from a known-good disk state is far better than pushing further and risking an
   inconsistent one.
5. **Never trust your own account of what shipped over the actual files.** Every ledger rebuild, every
   gate run, every check in this prompt reads from disk, not from memory of what you intended to write.
   This was true before and remains the single most repeated lesson across both prior papers.

If you are resuming a session that left a `resume-prompt.md` or equivalent checkpoint, read it first,
verify the files it claims exist actually do (a `ls` on the staging folder is cheap), and continue from
there — do not restart planning from scratch.

---

## 1 — Before anything else

Read these four files, in this order, before planning anything. Paths are relative to
`CCAR-P - Claude Certified Architect Professional/`:

1. `CLAUDE.md` (repo root)
2. `CLAUDE.md` (this folder)
3. `prep with quiz/CCAR-P-Orchestration-Prompt_v2.md` — **THE AUTHORITY** for schema, style caps, the
   T1-T4 tests, distractor-family taxonomy, and the phase structure. This prompt does not repeat that
   content; it only adds what changed operationally after Paper 2. Where the two disagree, the
   orchestration prompt wins.
4. `EXAM-FACTS_v1.md`

Then read, in this order:

5. `prep with quiz/EXAM-LOG.md` — every `SCORED` heading, **sorted by attempt date, not paper number**.
   This determines everything in §2 below.
6. `prep with quiz/GENERATION-INTELLIGENCE.md` — read Sessions 4 and 5 in full at minimum (the Paper 2
   pipeline redesign and its outcome — F-15 through F-20). Earlier sessions for background.
7. `FACET-LEDGER.md`, `STEM-LEDGER.md`, `ARCHETYPE-LEDGER.md`, `CCAR-P_Objective-Map_v1.md`.

---

## 2 — Preflight: which paper is actually next, and is it targeted or untargeted

**Do not assume "Paper 3" or "Paper 4" — verify.**

1. Check `mock-exams/` for the highest existing `CCAR-P_MockTest-N_v1.html`, and check
   `DASHBOARD-DATA.jsonl` for the highest `paper_n` already present. The next paper is one past
   whichever is higher. Abort and report if this prompt's assumption (Paper 3 or 4) doesn't match what
   you find.
2. Check `EXAM-LOG.md` for `## Paper N — SCORED <date>` headings. **As of this prompt being written
   (2026-08-31), neither Paper 1 nor Paper 2 had been sat.** If that is still true when you run this:
   - The next paper is generated the same way Papers 1 and 2 were — an **explicitly untargeted
     diagnostic**. Gate check 13 = N/A. Do not fabricate targeting triples.
   - **Stop and ask the user to confirm** before generating, exactly as the Paper 2 session did — they
     may want to sit an existing paper first so real targeting data exists.
   - If this is the situation, §4/§5's targeting-specific instructions below don't apply yet; skip to
     the untargeted-diagnostic path in each.
3. If Paper 1 and/or Paper 2 **have** been sat and scored by the time you run this:
   - Read the most recent Professor's Note (written after the most recently *attempted* paper by
     date, which may not be the highest-numbered one) and the most recent Insights Round if it's more
     recent than that note.
   - Apply Phase 7.1 in full: every targeting triple gets ≥1 item from the opposite facet/direction,
     satisfied inside the fixed domain quota; ≥3 previously-missed triples are left deliberately
     untargeted and named.
   - If the Professor's Note and the latest Insights Round disagree, reconcile explicitly in the
     generation entry and state which won and why.

---

## 3 — What changed after Paper 2 — read this or the paper will cost far more than it should

Paper 2 needed two generation attempts. The first — 7 parallel agents, one per full domain, `deepDive`
authored inline — failed 6 of 7 dispatches outright with a stream-watchdog stall and zero output,
including on retry. An independent cost/failure audit
(`Outputs/CCAR-P_Mock-Exam-Generation-Cost-Audit_v1.md`) found the drivers and both fixes are now
**standing practice, not paper-2-specific workarounds**:

**a. `deepDive` is a deferred, miss-driven Phase 9 addition — this is already the operative rule in the
orchestration prompt (§5.5's 2026-08-30 correction).** Every item ships `deepDive: null` at generation
time. Do not author it during Papers 3/4 generation. It gets populated later, only for items actually
missed, after the paper is scored. This alone roughly halves to thirds the per-item authoring and
grounding burden versus what Paper 1 originally cost.

**b. Authoring dispatch unit is a 5-6 item sub-batch, never a full domain in one turn.** This is the
fix that took Paper 2's redesigned attempt from a demonstrated 1-of-7 success rate to 13-of-13, zero
failures. Concretely: split each domain's item slots into groups of 5-6 (a domain with 4 or fewer items,
like D7, does not need splitting), dispatch each sub-batch as its own agent call, and have each one
write its own output file the instant it's done (§0). Do not dispatch "one agent per domain" the way
Paper 1 and Paper 2's first attempt did — that shape is now a known failure mode, not a design to
default back to.

**c. The central plan is computed once, centrally, before any dispatch — this already worked cleanly
across two papers and should not be revisited.** Domain quota, objective floor pass, the correct-letter
multiset (pre-shuffled, not left to chance), multi-response pairs (cap ≤2 repeats), and per-domain
distractor-family minimums (EVIDENCE-MISMATCH and DETECTIVE-FOR-PREVENTIVE specifically — these are the
two families the corpus under-supplies) all get worked out by the orchestrating session itself, in one
pass, and handed to each sub-batch as fixed slots. This is what produces a clean letter tally and
family distribution without needing a repair pass for *those* two things — see §6.

**d. Facet exclusion lists must be computed from what actually shipped, not trusted from the ledger's
own bookkeeping.** `FACET-LEDGER.md`'s "used" column has at least one known gap (documented in Paper 2's
generation entry). Extract the real facet list per prior paper directly from its shipped HTML — grep
for `facet:"F-` lines, the same way the Paper 2 session did — and treat that as ground truth for which
facets are already spent.

**e. Assembly is its own stage with its own real work, budget time for it.** Centrally compute
`lessonKey` for every item from each item's raw corpus answer text (agents should report
`factAnswerRaw`, not self-compute the key), then run the cross-domain collision check **before**
shipping, not after. Two refinements from Paper 2, both worth carrying forward:
  - A corpus answer that normalises to fewer than 3 content-word tokens (e.g. a bare "Reject" or
    "Synchronous") is not a reliable duplicate-decision signal on its own — exclude these from the
    collision check rather than risk a false positive across unrelated sections. A genuine collision
    with a longer, specific answer text is a real finding and needs a real fix (repoint one item to a
    different facet within the same section, preserving its quota/objective/letter/family
    assignments).
  - **The distractor-family cap (no family above 25%) has been violated on first assembly in multiple
    papers now** — independently-dispatched authoring units default toward the same "safe" families
    (WRONG-AXIS especially) with no visibility into the paper-wide total. Budget an explicit
    family-tally check right after assembly, before the gate run. When it's violated, look for
    distractors whose own `whyWrong` reasoning already better fits a different family — most fixes are
    a relabel, not a rewrite (Paper 2 fixed 10 of these without touching a single sentence of prose).

**f. Run the independent grounding audit in the SAME session, BEFORE the generation entry is written —
not as an optional follow-up.** Dispatch one fresh agent per domain (never the original author), give
it only the corpus file and that domain's shipped items, and have it check `whyRight`/`whyWrong`/
`t1Alt` cold. **`t1Alt` is the priority check**: it must resolve to a real, nameable row in the cited
section's decision table (F-12's original failure was 13 of 63 Paper 1 items shipping a `t1Alt` that
didn't). Paper 2's same-session audit found the resolution rate at 92% before shipping, versus Paper
1's 79% discovered only after. Classify every finding FIXABLE (state the exact fix; re-read the cited
section fresh before writing it — never from memory of what a section "probably" says) or IRREDUCIBLE
(the corpus genuinely doesn't support what's claimed — this happens, especially in D2's thin sections;
document it, don't force a fabricated resolution). Fix what's fixable; a handful of documented
IRREDUCIBLE exceptions is normal and expected, not a failure (Paper 2 shipped 5, down from Paper 1's
13).

**g. Retry protocol for a stalled dispatch.** If an authoring or audit dispatch fails with a stall,
check the target output path first — a genuine stall (Agent tool, not Workflow) produces **zero**
partial output, so a fresh retry is safe and costs nothing extra in duplicate work (this is a different
failure mode from Paper 1's Workflow `resumeFromRunId` bug, which re-ran already-succeeded work — that
risk does not apply here). Do not mass-retry blindly if several dispatches fail at once; retry
individually and watch whether the failure recurs at the same size — if even 5-6 item sub-batches start
stalling, that's new information worth a line in the generation entry, not something to paper over.

---

## 4 — Paper 3 specifics (only if Paper 3 is confirmed next, per §2)

- **Mode:** AUTHOR, same as every paper.
- **Shape policy:** same 8 shapes as Papers 1-2, content-varied, **all `direction: "normal"`**.
  Direction inversion doesn't start until Paper 4 (orchestration prompt §7.2).
- **Correct-letter rotation:** Paper 3's short letter is **B** (the P1→P2→P3→P4 rotation is
  D→C→B→A). Pre-plan the 55 single-answer letters as {A×14, B×13, C×14, D×14} (or whatever exact
  distribution the domain/multi-response split works out to that paper — recompute from scratch per
  §6, don't assume Paper 2's exact numbers carry over).
- **Targeting:** per §2 — if Papers 1/2 are still unscored, this is another untargeted diagnostic. If
  scored, this is the first paper that actually consumes a Professor's Note (per orchestration prompt
  §7.3: "First Professor's Note consumed").
- **If this scoring brings a paper count to 3 scored papers, an Insights Round is due** — that's a
  Phase 9 (post-sitting) activity, not something this generation session does, but worth knowing if
  you're also asked to help with scoring/logging around the same time.

---

## 5 — Paper 4 specifics (only if Paper 4 is confirmed next, per §2) — real structural differences

Paper 4 is not "another Paper 3." Three things change:

**a. Direction inversion begins.** Per `ARCHETYPE-LEDGER.md`'s inversion table (Part 1), **each of the
8 shapes must appear at least twice this paper with its direction inverted** — read that table's
per-shape inversion definition before authoring (e.g. S5-inverted is "under-engineering — a stated
requirement is genuinely non-enumerable and the higher rung is correct," the reverse of S5-normal's
over-engineering trap). This is the mechanism aimed directly at root `CLAUDE.md` habit 3 (choosing the
option that *sounds* safer/more architected). Build this into the central plan (§6) as an explicit
per-item `direction` assignment, the same way letters and facets are pre-assigned — don't leave it to
each sub-batch to decide.

**b. Habit escalation may fire (Phase 7.1 rule 4).** If a distractor family has captured ≥3 items across
two consecutive *scored* papers by attempt date, that family's shape becomes the **correct** answer on
2-3 items this paper, specifically to stop shape-recognition from substituting for real discrimination.
This requires real miss data from scored papers to evaluate — if Papers 1-3 aren't scored yet by the
time Paper 4 is generated, this rule has nothing to fire on; say so explicitly rather than guessing.

**c. Two things are due at Paper 4 that are not paper-content work — surface both, don't silently skip
either:**
  - **The fidelity-gate mechanization** (`GENERATION-INTELLIGENCE.md` pending decision 2,
    orchestration prompt Phase 6's closing note): build the stem-Jaccard-vs-`STEM-LEDGER.md` check and
    the cross-domain `lessonKey` collision check into `tools/run-gate.js` as committed, reusable code
    — Papers 1-3 handled both as one-off scripts (Paper 2's is at
    `prep with quiz/_PAPER2-STAGING/assemble.js` for reference), and hand-checking was explicitly
    deferred only through Paper 3. Do this as part of the same session, before or after the paper
    itself.
  - **The D2 corpus-expansion decision** (F-01, reinforced by F-12 and by 3 of Paper 2's 5 IRREDUCIBLE
    exceptions landing in D2's thinnest sections): this is Ram's decision, not something to resolve
    unilaterally — it touches a corpus file. **Surface it clearly and ask**, don't generate Paper 4's D2
    items and then discover mid-generation that supply is the problem. D2 facet supply is measured to
    hold through Paper 5, so this doesn't block Paper 4 itself, but the decision needs to land before
    Paper 6 is attempted.

---

## 6 — Central planning (both papers — do this once, in full, before any dispatch)

Exactly as the orchestration prompt §5.1-5.2 and §3 require, and exactly as both Papers 1 and 2 did
successfully:

1. Domain quota — fixed at 11/8/12/10/9/9/4 unless a confirmed-weakness adjustment is in force (needs
   two consecutive *scored* papers unambiguously weakest by attempt date on single-answer items only —
   check this fresh, don't assume it applies).
2. Objective floor pass (38 objectives, one each) + discretionary pass (cap 3/objective) — recomputed
   fresh each paper; there is no cross-paper cap on objective coverage, only on facet reuse.
3. Format split — 55 single + 8 multi-response, `selectN:2` on all eight, pairs capped at ≤2 repeats
   **within this paper** (not cumulative across papers).
4. Correct-letter multiset, pre-shuffled, per §4/§5's rotation for whichever paper this is.
5. Facet freshness — per-domain exclude lists built from every prior shipped paper's actual facets
   (§3d), plus which sections are still wholly untouched (best fresh material).
6. Distractor-family minimums per domain for EVIDENCE-MISMATCH and DETECTIVE-FOR-PREVENTIVE, summing
   to the paper-wide floors (≥15 and ≥9 respectively, out of ~181 total distractors for a 63-item
   paper — recompute the exact total once format split is fixed, since multi-response items carry only
   2 distractors each versus 3 for single-answer).

Write the finished plan to disk (§0) before dispatching anything.

---

## 7 — Build, dispatch, assemble, audit, gate, close-out

Follow the orchestration prompt's Phases 5-9 for content rules (schema, T1-T4, style caps, deepDive's
Phase-9-only timing). Follow §0's checkpointing discipline and §3's operational lessons for *how* to
run the session. In order:

1. Compute and save the central plan (§6).
2. Dispatch sub-batches per domain (§3b), each ~5-6 items, `deepDive:null`, immediate per-batch save.
3. Assemble: `lessonKey`, collision check, family-cap check-and-fix, save the merged file (§3e, §0).
4. Build/update the shipped HTML from the template (3 const changes: `PAPER_N`, `KEY`, `EXAM_MODE` —
   stays `false` unless this is Paper 8 or 10, neither of which is in scope here).
5. Run `node tools/run-gate.js mock-exams/CCAR-P_MockTest-N_v1.html 63`. Fix any error to 0. Re-run
   checks 2, 3, 6, 10 after any item swap.
6. Dispatch the independent grounding audit (§3f), same session, before step 8. Fix what's fixable;
   document what's IRREDUCIBLE.
7. Manually verify what the mechanized gate doesn't check (or does, if you built §5c's mechanization
   for Paper 4): objective codes against the canonical 38, zero invented names, D1/D5/D6 zero inline
   tokens, stem-Jaccard dedup.
8. Phase 8 close-out: `EXAM-LOG.md` generation entry (mode, targeting consumed or explicitly none, full
   13-check gate table with computed values, the generation story if anything went sideways),
   `DASHBOARD-DATA.jsonl` line with null scores, rebuild all three ledgers **from the shipped HTML
   file**, `GENERATION-INTELLIGENCE.md` session entry with any new findings.

---

## 8 — Stop and ask, do not guess

Stop and ask the user if: §2's preflight finds a different paper number than expected · a scored Paper
1/2/3 exists with a Professor's Note that conflicts with the latest Insights Round · the corpus cannot
supply a facet a quota needs · the gate cannot be brought to 0 errors without changing an item's
`correct[]` · you would need to edit any `CCAR-P_Domain-N_v1.md` corpus file, including for the D2
expansion decision (§5c) · a sub-batch dispatch fails more than once at the same size, which would be
new evidence worth a decision before continuing rather than a third blind retry.

Report honestly. Quote real command output rather than reconstructing it. If a check did not run, say
so. Do not report a paper as generated until the gate is clean, the grounding audit has run, and the
ledgers are rebuilt from disk — not from memory of the session's own work.
