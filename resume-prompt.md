# Resume Prompt — CCAR-P Mock Test Paper 2 generation
_Generated: 2026-08-30 22:20 • Working dir: C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCAR-P - Claude Certified Architect Professional\.claude\worktrees\evaluate-certifications-repo-cdf916_

> **SUPERSEDED 2026-08-31 — Paper 2 generation is COMPLETE, not a checkpoint anymore.** Everything below
> was written mid-task and is kept for historical/provenance detail only (the failure story, the audit,
> the fixes). For current status, read `EXAM-LOG.md`'s "## Paper 2" entry — 63/63 items authored,
> assembled, independently grounding-audited, 0 fidelity-gate errors, 5 documented IRREDUCIBLE T1
> exceptions (down from Paper 1's 13). `GENERATION-INTELLIGENCE.md` Session 5 has the engine-level
> findings (F-17 through F-20). Nothing in the "Next action" section below needs doing — it was already
> done. Do not re-dispatch anything based on this file.

**This overwrites an earlier version of this file from earlier today.** Do not use anything from
memory of that earlier version — a great deal changed since (an independent audit ran, a spec decision
was made and implemented, and generation is now 54/63 items complete). This file is the only current
account.

## Context

Generating "CCAR-P Mock Test Paper 2" (63-item AUTHOR-mode exam) per
`CCAR-P - Claude Certified Architect Professional/prep with quiz/CCAR-P-Orchestration-Prompt_v2.md`.
Confirmed with Ram as an untargeted second diagnostic (Paper 1 not yet scored).

**The full arc of today's session, in order:**
1. First generation attempt: 7 parallel full-domain agents (with `deepDive` inline). 6 of 7 failed
   outright (stream-watchdog stalls, zero output, including on retry). Only D7 (4 items) succeeded.
2. Ram paused, asked for a snapshot — handled, then all 6 pending agents reported back as failed while
   he was away. Confirmed: every dispatch above 4 items failed, every time, no exceptions.
3. Ram returned and said the time being spent was "ridiculous," called the system "over-engineered,"
   and — critically — said a prior attempt at a cost fix had "already failed once." He asked for an
   independent agent, forked fresh with no memory of this session's reasoning, to audit the system cold.
4. That audit (`Outputs/CCAR-P_Mock-Exam-Generation-Cost-Audit_v1.md`) found: the core spec (quotas,
   letter pre-plan, T1-T4) is well-evidenced and NOT the problem. `deepDive` — added in a prior session
   with zero cited evidence of need, roughly tripling per-item cost — IS the problem; the project's own
   prior grounding record already showed it overreaches the corpus in 44% of Paper 1's items. Separately,
   today's specific outright failure correlated cleanly with dispatch size (item count per turn), not
   corpus size — the only success (D7) was also the smallest by far.
5. Ram approved the audit's recommendation in full: demote `deepDive` to a deferred, miss-driven Phase 9
   addition, and split each domain's authoring into 5-6-item sub-batches instead of one mega-turn.
6. Both fixes were implemented (see "Decisions locked in" below) and 12 replacement sub-batches were
   dispatched. **10 of 12 succeeded quickly (11.5-17 min each).** Ram then asked to pause for the day
   with 2 sub-batches still in flight.

## What's done

- All the Phase-1 reading, the central 63-item plan (letters, objectives, facets, family minimums), and
  the D7 batch from earlier today — see the "Files touched" section below, nothing there needs redoing.
- **The audit and the decision it produced** — read `Outputs/CCAR-P_Mock-Exam-Generation-Cost-Audit_v1.md`
  if you want the full reasoning; the operative decision is already implemented, described next.
- **`deepDive` demoted to deferred Phase 9, implemented in three places:**
  - `CCAR-P - Claude Certified Architect Professional/prep with quiz/CCAR-P-Orchestration-Prompt_v2.md`
    — §5.5's `deepDive` entry now opens with a dated correction explaining the new rule (item ships
    `deepDive: null`; Phase 9 populates it later, only for missed items). Phase 6's gate note updated to
    match. Phase 9's step list gained a new step 3 describing the miss-driven generation+audit process.
    Paper 1 is explicitly NOT touched — it keeps its already-shipped `deepDive` layer.
  - `mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html` and `mock-exams/CCAR-P_MockTest-2_v1.html` —
    `validateItems()`'s `deepDive` block changed: `null`/`undefined` is no longer an error unless the
    caller passes `opts.requireDeepDive`; a *present* `deepDive` is still checked for being well-formed.
    Verified with a live `node tools/run-gate.js` run (0 errors) before proceeding.
  - `GENERATION-INTELLIGENCE.md` gained a full Session 4 entry — findings F-15 (`deepDive` demoted,
    promoted via Ram's explicit decision) and F-16 (dispatch granularity, not corpus size, predicted
    today's failures) — plus an updated open-findings ledger and a session reflection on why the
    independent-audit approach worked where a second self-directed patch had already failed once.
- **The authoring brief was rewritten** to match: `deepDive` section removed entirely, schema comment
  changed to `deepDive: null` literal, output-format instructions shortened. Now at:
  `CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER2-STAGING/p2-shared-brief.md`
- **12 replacement sub-batches dispatched** (5-6 items each, no `deepDive`, immediate per-batch file
  write) to cover D1-D6 (D7 untouched, already valid from before). **10 of 12 are DONE and on disk:**

| File | Domain | Items | Status |
|---|---|---|---|
| `p2-d1-batch1.json` | D1 | g1-g6 | done |
| `p2-d1-batch2.json` | D1 | g7-g11 | done |
| `p2-d2-batch1.json` | D2 | g12-g15 (incl. D2's multi item g15) | done (took ~38 min — slow but succeeded, did not stall) |
| `p2-d2-batch2.json` | D2 | g16-g19 | done |
| `p2-d3-batch1.json` | D3 | g20-g25 (incl. D3 multi item g23) | done |
| `p2-d3-batch2.json` | D3 | g26-g31 (incl. D3 multi item g29) | done |
| `p2-d4-batch1.json` | D4 | g32-g36 (incl. D4's multi item g36) | done (took ~39 min — slow but succeeded, did not stall) |
| `p2-d4-batch2.json` | D4 | g37-g41 | done |
| `p2-d5-batch1.json` | D5 | g42-g46 (incl. D5 multi item g46) | done |
| `p2-d5-batch2.json` | D5 | g47-g50 | done |
| `p2-d6-batch1.json` | D6 | g51-g55 (incl. D6 multi item g55) | done |
| `p2-d6-batch2.json` | D6 | g56-g59 | done |
| `p2-d7.json` | D7 | g60-g63 (incl. D7 multi item g62) | done (from earlier today, untouched) |

**ALL 63 OF 63 ITEMS ARE NOW AUTHORED AND ON DISK.** D4-batch1 (the last one) landed successfully at
~39 minutes — slow, like D2-batch1, but a genuine success, not a stall. **Every one of the 13 dispatches
on the redesigned pipeline (12 sub-batches + D7) succeeded — 13 for 13, zero failures**, a complete
reversal from attempt 1's 1-of-7. This news arrived after Ram had already asked to pause for the day;
generation work stopped here deliberately, out of respect for that, even though the next step
(assembly) is now fully unblocked. All paths above are relative to
`CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER2-STAGING/`.

## What's open

- **Nothing is pending from any background agent — this is now purely a "pick up the next step" resume,
  not a "check on stalled work" one.** The next action is assembly, and it's entirely this session's own
  work (no more agent dispatch needed until the grounding-audit stage).
- Nothing has been assembled into `mock-exams/CCAR-P_MockTest-2_v1.html` yet — it still has only the
  const changes needed (none done yet either — `PAPER_N`, `KEY`, `EXAM_MODE`) and template/demo `ITEMS`.
- `lessonKey` has not been computed for any item yet (every batch shipped `factAnswerRaw` instead, per
  design — see "Next action" step 2).
- The cross-domain lesson-collision check has not been run.
- The independent grounding audit (separate agents, checking `whyRight`/`whyWrong`/`t1Alt` cold — NOT
  `deepDive`, which no longer exists at this stage) has not been dispatched.
- The fidelity gate (`node tools/run-gate.js ... 63`) has not been run against real content.
- Phase 8 close-out (EXAM-LOG entry, DASHBOARD-DATA line, ledger rebuilds) has not started.
- **One flagged item for the grounding pass:** D5 g46 (section 5.5, the D5 multi-response item)'s own
  author reported that section 5.5's decision table may not cleanly supply a genuine T2
  neighbour-correct distractor — it has only 2 accept-rows (which became the correct pair) and 2
  reject-rows that are never correct anywhere. The author flagged this honestly rather than fabricating
  a false T2 justification. Check this item specifically; it may need a different t1Clause/t1Alt pair or
  an accepted, documented T2 exception (Paper 1 precedent: D2 had 4 documented, unfixable T2 exceptions
  for single-facet sections — see `EXAM-LOG.md` Paper 1 entry, finding 5).

## Next action (do this first)

1. ~~Check pending batches~~ — **done, not needed.** All 13 files exist (verify with a quick
   `ls "CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER2-STAGING/"` if you want
   to double-check nothing evaporated between sessions, but this should just confirm 13 `p2-d*.json`
   files plus the brief/slots files).
2. **Start here: assemble.** All 13 JSON files exist (12 batches + `p2-d7.json`):
   a. For every item, compute `lessonKey` from its `factAnswerRaw` field: lowercase, strip punctuation,
      remove stopwords, dedupe tokens, sort alphabetically, join with spaces (matches
      `STEM-LEDGER.md`'s own normalisation). Leave `""` if `factAnswerRaw` is empty (e.g. D3 g23, which
      is genuinely built from two rows, not one — its author left `factAnswerRaw` empty deliberately).
   b. Run the cross-domain lesson-collision check: group all 63 items by their computed `lessonKey`,
      flag any non-empty key shared by more than one item (this is the F-10 mechanism, done centrally
      before shipping — Paper 1 needed it done by hand after the fact, this time it should happen before
      assembly). If a collision is found, repoint one of the colliding items at a different facet within
      the same section, same pattern as Paper 1's fix (see `EXAM-LOG.md` Paper 1 entry, finding 6).
   c. Strip the `factAnswerRaw` field from every item (it's not part of the shipped schema) after using
      it for `lessonKey`.
   d. Edit `mock-exams/CCAR-P_MockTest-2_v1.html`: set `const PAPER_N = 2;`, `const KEY =
      "ccarp-mocktest-2-v1";`, leave `EXAM_MODE = false`, replace the demo `ITEMS` array with the
      assembled 63 items in g-order, update the top-of-file HTML comment and the `ITEMS` schema-comment
      header so neither describes template/demo content (the schema comment should also now note
      `deepDive` ships `null` — see the template's own already-updated `validateItems()` comment for
      the exact wording to mirror).
3. **Dispatch the independent grounding audit** — separate fresh agents (not the original authors),
   one per domain, each given ONLY that domain's corpus file + that domain's shipped items in the
   assembled file, checking `whyRight`/`whyWrong`/`t1Alt` (NOT `deepDive` — it's null this paper) cold
   against the corpus. This is smaller-scope than Paper 1's deep-dive audit (no `deepDive` to check), so
   it should be fast. Classify findings FIXABLE vs IRREDUCIBLE (F-14 pattern) — fix FIXABLE ones
   directly or via `SendMessage` continuation to the original batch author; for IRREDUCIBLE ones (a
   `t1Alt` that doesn't actually resolve, per F-12), change the `t1Clause`/`t1Alt` pair rather than
   force a claim the corpus can't support.
4. **Run the gate**: `node tools/run-gate.js mock-exams/CCAR-P_MockTest-2_v1.html 63`, work through all
   13 checks from Phase 6 of the orchestration prompt, re-run checks 2/3/6/10 after any item swap.
   Manually verify what the mechanized gate does NOT check: objective codes are exactly the canonical 38
   (not just 38 distinct strings), no D1/D5/D6 option has an inline code token, no invented company/
   product/persona names anywhere, and the stem-Jaccard dedup against `STEM-LEDGER.md` (write a small
   throwaway script for this — do NOT add it to the committed `tools/run-gate.js`, that mechanization is
   deliberately deferred to Paper 4 per the orchestration prompt and `GENERATION-INTELLIGENCE.md`'s own
   pending-decision list).
5. **Phase 8 close-out**: append the Paper 2 generation entry to `EXAM-LOG.md` (mode AUTHOR, untargeted
   diagnostic, the quota table, the full 13-check gate table with computed values, AND a clear account
   of today's generation-process story — the failed first attempt, the audit, the fix, since that's
   exactly the kind of "what actually happened" detail Paper 1's own entry models); append the
   `DASHBOARD-DATA.jsonl` line with null scores; rebuild `STEM-LEDGER.md`, `FACET-LEDGER.md`, and
   `ARCHETYPE-LEDGER.md` from the shipped HTML file (never from this session's own account); append a
   Session 5 entry to `GENERATION-INTELLIGENCE.md` reporting the final outcome: **the sub-batch fix held
   completely — 13 of 13 dispatches succeeded, zero failures**, though 2 of them (D2-batch1, D4-batch1)
   took ~38-39 minutes each versus 11.5-17 minutes for the other 10 — worth noting as a real but
   non-fatal cost of the redesign, and comparing the measured total token cost of this whole generation
   against Paper 1's ~7.7-8M and today's failed first attempt.

## Decisions locked in

- **Paper 2 = untargeted second diagnostic** (Ram-confirmed earlier today).
- **Central pre-plan computed once, before authoring, not delegated** — letters, multi-pairs, objective
  floor, facet freshness all fixed centrally first. This part worked cleanly both times today and
  should not be revisited.
- **`deepDive` demoted to deferred, miss-driven Phase 9 addition** (Ram-approved, implemented — see
  "What's done"). This is now the standing rule for Paper 2 onward, not a one-off workaround. Paper 1
  keeps its existing `deepDive` layer; nothing retroactive.
- **Authoring dispatch unit is now a 5-6 item sub-batch, not a full domain.** Also now the standing
  approach — the redesign was validated today (10/12 succeeded fast; the previous full-domain approach
  succeeded on only 1/7). If the last 2 batches also turn out fine, treat this as confirmed; if they
  stall too, note that even sub-batches aren't fully immune and the next investigation should look at
  whether ~4 items (D7's exact original size) is the real safe ceiling, not ~5-6.
- **`lessonKey` computed centrally by the orchestrator**, not per-agent — every batch author reports raw
  `factAnswerRaw` instead.
- **Gate-script mechanization (Jaccard-vs-ledger, cross-domain collision) still NOT added to
  `tools/run-gate.js`** — deliberately deferred to Paper 4 per the orchestration prompt itself.
- **Agent tool over Workflow tool** — no `ultracode` opt-in was present; also avoids Paper 1's
  Workflow-`resumeFromRunId` duplication bug (a different failure mode from today's stalls).

## Files touched this session (full list, both sub-sessions of today)

- `CCAR-P - Claude Certified Architect Professional/prep with quiz/CCAR-P-Orchestration-Prompt_v2.md` —
  edited (deepDive correction, 3 spots)
- `CCAR-P - Claude Certified Architect Professional/prep with quiz/GENERATION-INTELLIGENCE.md` — edited
  (Session 4 entry appended)
- `CCAR-P - Claude Certified Architect Professional/prep with quiz/mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html`
  — edited (`validateItems()` deepDive block)
- `CCAR-P - Claude Certified Architect Professional/prep with quiz/mock-exams/CCAR-P_MockTest-2_v1.html`
  — created (copy of template) + edited (same `validateItems()` fix); `ITEMS` array NOT yet replaced
- `CCAR-P - Claude Certified Architect Professional/ROADMAP.md` — edited (status note)
- `CCAR-P - Claude Certified Architect Professional/Outputs/CCAR-P_Mock-Exam-Generation-Cost-Audit_v1.md`
  — created by the independent audit agent
- `CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER2-STAGING/` — durable staging
  folder (corrected location after a path bug fix); contains `p2-shared-brief.md`, `p2-slots.md`, and
  12-13 `p2-d*.json` item files (see table above)
- `resume-prompt.md` (this file, worktree root) — overwritten with current state
- Memory file `ccarp-paper2-generation-pipeline.md` — being updated now, see next section

## Gotchas / watch-outs

- **`_PAPER2-STAGING/` lives inside the actual project folder now** —
  `CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER2-STAGING/`, NOT directly under
  the worktree root. An earlier `mkdir -p "prep with quiz/_PAPER2-STAGING"` run from the worktree root
  silently created a stray, wrongly-located folder there instead of using the real nested one — this
  was caught and fixed, but double-check any path you're about to write to actually resolves inside the
  project folder, not the worktree root, before trusting it.
- **The session-specific scratchpad is NOT where anything durable lives anymore** — everything needed
  to resume is inside the actual project tree now (`_PAPER2-STAGING/`), not a temp folder.
- **D2 and D4's slow-but-successful batches (~38-39 min each) both eventually landed cleanly** — no
  action needed, just don't be alarmed if you see their long durations in agent logs; they finished
  fine. D2 remains the tightest-facet domain in the corpus generally (worth remembering for Paper 3+,
  not an issue for the already-shipped Paper 2 content).
- **Do not re-dispatch anything for authoring — all 13 files are done.** If you're re-reading this and
  tempted to regenerate a domain "to be safe," don't; verify the file exists and looks well-formed
  first (step 2a below reads every file anyway, which will surface a real problem immediately).
- **`p2-d3-batch1.json`'s g23 has `factAnswerRaw: ""` deliberately** — it's a multi-response item
  genuinely built from two separate decision-table rows, not one, so no single verbatim Answer-column
  string applies. Its `lessonKey` should also compute to `""` when you run step 2a — do not treat this
  as a missing-data bug.

## Git state

Branch: `claude/evaluate-certifications-repo-cdf916`

```
 M "CCAR-P - Claude Certified Architect Professional/ROADMAP.md"
 M "CCAR-P - Claude Certified Architect Professional/prep with quiz/CCAR-P-Orchestration-Prompt_v2.md"
 M "CCAR-P - Claude Certified Architect Professional/prep with quiz/GENERATION-INTELLIGENCE.md"
 M "CCAR-P - Claude Certified Architect Professional/prep with quiz/mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html"
?? "CCAR-P - Claude Certified Architect Professional/Outputs/CCAR-P_Mock-Exam-Generation-Cost-Audit_v1.md"
?? "CCAR-P - Claude Certified Architect Professional/Outputs/CCAR-P_Paper-2-Generation-Prompt_v1.md"
?? "CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER2-STAGING/"
?? "CCAR-P - Claude Certified Architect Professional/prep with quiz/mock-exams/CCAR-P_MockTest-2_v1.html"
?? resume-prompt.md
```

`Outputs/CCAR-P_Paper-2-Generation-Prompt_v1.md` pre-dates this whole session (it was untracked before
either sub-session started) — not something to clean up as this session's own mess. Everything else
above is this session's work. No commits made, nothing pushed, nothing staged. Recent commits (all
pre-date this session, unrelated):
```
20e0004 Fix Paper 1's stale "four demo items" schema-comment header
bd0facd /sync-up: record the deep-dive session in the docs that lag it
1564316 Mark F-07's Paper 1 conclusion superseded, keep the finding
```
No version-bump markers in this repo.
