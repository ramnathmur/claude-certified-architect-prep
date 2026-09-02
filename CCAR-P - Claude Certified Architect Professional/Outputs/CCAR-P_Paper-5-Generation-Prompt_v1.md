# CCAR-P Mock Test Paper 5 — Generation Prompt

**Written:** 2026-09-01, at the end of the session that generated Paper 4. Paper 4 shipped clean (0
gate errors) but only after the heaviest audit-and-fix cycle any paper in this series has needed —
see §2 and §4 below before planning anything. This document supersedes nothing; it is the first
Paper-5-specific prompt.

---

## 0 — Session-continuity rule: save to disk continuously, not at the end

Unchanged from every prior paper's prompt, and still load-bearing. Design the session around
**cheap, frequent, durable checkpoints**:

1. Compute the central plan once, write it to disk immediately, before dispatching any authoring
   agent. Use `prep with quiz/_PAPER5-STAGING/plan.json` and a rendered `p5-slots.md` — never only
   the session's ephemeral scratchpad. Verify the path resolves inside
   `CCAR-P - Claude Certified Architect Professional/prep with quiz/` before writing anything.
2. Every authoring sub-batch writes its own output file the moment it finishes.
3. Re-save the merged items file after assembly and after every fix pass.
4. If running low on budget or context with the paper unfinished, stop and write a resume prompt in
   the same shape as Papers 2-4's sessions used — what's done (exact file paths), what's open, the
   exact next action, decisions locked in, gotchas.
5. Never trust your own account of what shipped over the actual files. Every check in this prompt
   reads from disk, not from memory of what you intended to write.
6. **Use absolute paths for every shell/file operation, or verify your cwd before each one.**
   Paper 4's session lost real time to a `cd X && node Y` chain in Bash that left the shared working
   directory nested inside `_PAPER4-STAGING/`, which then caused a subsequent Write call (given a
   path that looked absolute-ish but wasn't) to create a duplicated folder tree one level inside
   itself. If you must `cd`, confirm with `pwd`/`Get-Location` immediately after, in the same tool
   call where practical, before trusting any subsequent relative path.

---

## 1 — Before anything else

Read these, in this order. Paths are relative to `CCAR-P - Claude Certified Architect Professional/`:

1. `CLAUDE.md` (repo root)
2. `CLAUDE.md` (this folder)
3. `prep with quiz/CCAR-P-Orchestration-Prompt_v2.md` — **THE AUTHORITY** for schema, style caps,
   the T1-T4 tests, distractor-family taxonomy, and the phase structure, including §7.2's direction-
   inversion policy and §7.3's series table (Paper 5's row: "rolling triples · direction-inverted ·
   Confirmed-weakness adjustment first eligible to fire twice running"). Where this prompt and the
   orchestration prompt disagree, the orchestration prompt wins.
4. `EXAM-FACTS_v1.md`
5. `prep with quiz/EXAM-LOG.md` — every `SCORED` heading, sorted by attempt date. **Read the Paper 4
   entry in full** — it has the fullest generation story of any paper so far: the D2 decision's
   implementation, the two real construction bugs the audit-fix cycle introduced and how they were
   caught, the `cite`-field bug, and the gate-mechanization work.
6. `prep with quiz/GENERATION-INTELLIGENCE.md` — read **Session 7 in full** (F-27 through F-33,
   Paper 4's findings). Earlier sessions for background if needed, but Session 7 is the one with
   material you cannot skip, especially F-01/F-27/F-29/F-31/F-33's pending-decisions list.
7. `FACET-LEDGER.md`, `STEM-LEDGER.md`, `ARCHETYPE-LEDGER.md`, `CCAR-P_Objective-Map_v1.md`. All
   three were rebuilt from the shipped HTML after Paper 4 (not from a session's own account) and now
   carry Papers 1-4's usage — but per standing practice (F-21), **extract facet freshness from the
   shipped HTML files directly as the ground truth**, the same way every paper since Paper 3 has,
   rather than trusting any ledger's "used" column at face value. The four shipped papers to check are
   `mock-exams/CCAR-P_MockTest-{1,2,3,4}_v1.html`.
8. `prep with quiz/_PAPER4-STAGING/` — kept as a historical reference, the same way Papers 2-3's
   staging folders were. `analyze-prior-papers.js`, `parse-facet-ledger.js`, `build-plan.js`,
   `finalize-plan.js`, `assemble.js`, `extra-checks.js`, `apply-audit-fixes.js`, `build-html.js`, and
   the three `rebuild-*-ledger.js` scripts are all reusable templates — port the logic into a fresh
   `_PAPER5-STAGING/`, don't just copy the files verbatim (facet counts, section lists, letter
   pre-plan, and the hard-coded D2 handling all need Paper-5-specific numbers).

---

## 2 — Read this before planning D2's quota — the picture changed again, and it's more subtle than Paper 4's version

**D2's misconception-unit supply is now fully spent.** Paper 3 used 6 of 9 units; Paper 4 used the
remaining 3 (M-2.3, M-2.5, M-2.9). **All 9 of 9 misconception units are used.** That fallback no
longer exists for any future paper.

**D2's decision-table facets were already at 0 fresh before Paper 4 even started**, and Paper 4's
direction-inverted-reuse mechanism (Ram's approved decision) consumed five specific facets as
inversion anchors: `F-2.1-01`, `F-2.2-01`, `F-2.4-01`, `F-2.7-01`, `F-2.8-01` — each of these now
carries **two** real uses in the archetype ledger (a `normal` instance from whichever paper first
authored it, and an `inverted` instance from Paper 4).

**This prompt cannot tell you exactly how much D2 supply is left, because the answer depends on
facet-level bookkeeping this session must do fresh, not section-level bookkeeping like Paper 4 used.**
Here is the reasoning, offered as a strong working hypothesis to verify, not a settled number:

- Sections 2.6, 2.7, 2.8, 2.9 each hold exactly **one** facet. Of these, 2.7's and 2.8's sole facets
  were the ones Paper 4 inverted — each now sits at the archetype ledger's 2-use cap
  (`normal` + `inverted`), and a third attempt at either would need a third *direction* to exist,
  which the shape's inversion table doesn't define. **Treat 2.7 and 2.8 as fully exhausted for D2
  purposes.** 2.9's sole facet was never reuse-inverted (Paper 4 used its misconception unit instead)
  — it has one `normal` use and could in principle support one genuine `inverted` use, if the
  section's content actually supports a real inversion (2.9's own content, per Ram's decision write-
  up in Paper 4, is thin — check this carefully, it may turn out IRREDUCIBLE the way 2.2 almost did).
  2.6 was untouched by any of Paper 4's five reuse-inversion anchors — its sole facet (`F-2.6-01`) has
  only a `normal` use on record and is a **likely fresh reuse-inversion slot**.
- Sections 2.1, 2.2, 2.4 each hold more than one facet, and Paper 4 only inverted *one* facet per
  section (the "01" facet in each case). The *other* facets in those sections (2.1 has two more,
  2.2 has three more, 2.4 has one more) have a `normal` use on record but **no `inverted` use yet** —
  these are also likely fresh reuse-inversion slots, distinct (shape, section, facet, direction)
  triples from what Paper 4 already used.
- Section 2.3's facets are all used `normal` (2.3's misconception unit was used in Paper 4, its
  facets were never reuse-inverted) — same shape as 2.6/2.9: check for fresh reuse-inversion slots.
- **Adding this up naively suggests D2 may still have a handful of genuinely fresh (section, facet,
  inverted) slots left** — enough for Paper 5's 8-item quota, possibly without touching corpus
  expansion yet. But this is exactly the kind of naive count that produced a cosmetic-restate failure
  in Paper 4 (g19, D2 §2.8) — a facet with only one thin decision-table row may simply not support a
  *second*, genuinely different inverted-direction test even if the ledger has technical room for it.
  **Do not assume the arithmetic above means the content problem is solved. It only means the
  bookkeeping doesn't forbid trying.**

**Concretely, before planning any D2 item:**

1. Extract every D2 `(section, facet, direction)` combination actually shipped across Papers 1-4 from
   the HTML directly (extend `_PAPER4-STAGING/parse-facet-ledger.js`'s method), not from
   `FACET-LEDGER.md`'s bookkeeping.
2. For each D2 section, compute which specific facets have a `normal` use but no `inverted` use.
   These are your only candidate slots — there is no fresh-facet or misconception-unit fallback left
   at all.
3. **If the candidate count is ≥8, this is very likely the last paper this works for without Ram's
   corpus-expansion decision** — every one of those candidate slots will be spent after Paper 5, and
   Paper 6's D2 quota will have nothing but re-runs of already-both-directions-used facets, which
   §7.1 rule 1 of the orchestration prompt bans outright ("Same triple, same direction is banned").
   Say this plainly to Ram in the same conversation where you confirm the count.
4. **If the candidate count is <8**, D2 corpus expansion is not just overdue (per `ROADMAP.md`'s own
   escalation after Paper 4) — it is now a **hard blocker for generating Paper 5's D2 quota at all**,
   not a "papers 6-10" problem. Stop and ask before doing anything else.
5. Either way, **stop and ask Ram to confirm the mechanism** exactly as Paper 4's session did,
   updating the menu of options for what's actually still available: (a) proceed with whichever
   fresh reuse-inversion slots the count in step 2 actually supports, explicitly naming which
   sections/facets and accepting some may resolve IRREDUCIBLE on audit (matching 2.2's and 2.8's
   precedent); (b) do the D2 corpus expansion now (the ~20 new decision-table rows
   `FACET-LEDGER.md` has flagged since Session 1, `F-01`) rather than deferring further — this is now
   the option the evidence most strongly points toward; (c) temporarily lower D2's quota for this
   paper only with a compensating raise elsewhere, documented as a one-off; or (d) something else Ram
   prefers.
6. Whatever Ram decides, record it in the Paper 5 generation entry as a locked-in decision, exactly
   as Papers 2 and 4's D2 decisions were recorded.

**This is very likely the single most consequential decision this session needs from Ram, more so
than Paper 4's version of the same question** — Paper 4 could lean on 8 still-untouched pairings
(3 misconception units + 5 fresh reuse-anchor facets); Paper 5 has neither fallback fully intact and
is working from the last remaining scraps of facet-level bookkeeping room.

---

## 3 — Preflight: which paper is actually next, and is it targeted or untargeted

Do not assume Paper 5 without checking, even though it is very likely correct.

1. Check `mock-exams/` for the highest existing `CCAR-P_MockTest-N_v1.html` (as of this writing:
   `..._4_v1.html`) and `DASHBOARD-DATA.jsonl` for the highest `paper_n` (as of this writing: `4`).
   The next paper is one past whichever is higher. Abort and report if this prompt's Paper 5
   assumption doesn't match what you find.
2. Check `EXAM-LOG.md` for `## Paper N — SCORED <date>` headings. As of this prompt being written
   (2026-09-01), **none of Papers 1, 2, 3, or 4 had been sat.** If that is still true when you run
   this:
   - Paper 5 is generated the same way Papers 1-4 were — an **explicitly untargeted diagnostic**.
     Gate check 13 = N/A. Do not fabricate targeting triples.
   - **Stop and ask the user to confirm before generating** — this is now the *fifth* consecutive
     untargeted diagnostic if Ram proceeds. Papers 2-4 each individually made the reasonable call to
     keep generating rather than pause, but the case for actually sitting one before generating a
     sixth-in-a-row is stronger every time it's deferred: no targeting data exists yet, Phase 7.1
     rule 4 (habit escalation) has never fired, and the confirmed-weakness mechanism the orchestration
     prompt's own series table says should be "first eligible to fire twice running" at Paper 5 has
     nothing to work with. Say this plainly when asking, don't just repeat the boilerplate question.
   - If this is the situation, skip the targeting-specific instructions in §5 below.
3. If one or more of Papers 1-4 **have** been sat and scored by the time you run this:
   - Read the most recent Professor's Note (written after the most recently *attempted* paper by
     date) and the most recent Insights Round if more recent than that note.
   - Apply Phase 7.1 in full: every targeting triple gets ≥1 item from the opposite facet/direction,
     satisfied inside the fixed domain quota; ≥3 previously-missed triples left deliberately
     untargeted and named.
   - Check whether Phase 7.1 rule 4 (habit escalation) fires: has one distractor family captured ≥3
     items across two consecutive *scored* papers by attempt date? If so, that family's shape becomes
     the **correct** answer on 2-3 items this paper.
   - Check whether the confirmed-weakness adjustment fires: is the same domain unambiguously weakest
     on two consecutive scored papers by attempt date, on single-answer items only? If so, raise that
     domain's quota by 2-4 and lower the strongest domain by the same, documented and reverted the
     following paper. D7 floors at 3 and caps at 6.
   - If the Professor's Note and the latest Insights Round disagree, reconcile explicitly in the
     generation entry and state which won and why.

---

## 4 — What changed after Paper 4 — read this or the paper will cost more than it should

Seven findings from Paper 4's session (`GENERATION-INTELLIGENCE.md` F-27 through F-33), condensed to
what changes how you work this paper. Full detail is in Session 7 of that file.

**a. The `cite` field is now a hard requirement, and it earned that status the hard way.** Paper 4's
own shared authoring brief omitted `cite: "<domain> <section>"` from the item schema — every item
shipped without it, which showed as literal "undefined" text in the browser's feedback footer on
every single question. `validateItems()` now requires `cite` (fixed in the TEMPLATE). **Include
`cite` explicitly in whatever shared brief you write for Paper 5's sub-batches** — do not rely on
`validateItems()` alone to catch its absence at the sub-batch level; the gate only sees it once
assembled.

**b. Gate mechanization (checks 10 and 11) is done — use it, don't rebuild it.** `tools/run-gate.js`
now runs the distractor-family-cap check and the stem-Jaccard/triple-reuse dedup check as committed
code, not a one-off script. It is also now safe to re-run at any point in the Phase 6→8 sequence,
including after the ledger rebuild (it excludes the paper's own already-appended ledger rows by
parsing the paper number from the filename). **Run it early and often this paper** — after assembly,
after every fix, and once more at the very end — instead of writing a fresh one-off `extra-checks.js`
from scratch. If you do need one-off checks beyond 10/11 (objective cap, multi-pair repeats, t1Alt
presence — checks 5/7/12), port `_PAPER4-STAGING/extra-checks.js`'s remaining logic rather than
reinventing it.

**c. Direction-inverted items need per-instance audit, not just per-mechanism trust.** 16 of Paper
4's 17 inverted items were genuine on first authoring; the 17th (one of D2's reuse-inversion slots)
was a cosmetic restate of an already-shipped lesson, caught only by the independent audit. **Every
inverted item this paper — D2's especially, since they're reusing an already-`normal`-used facet —
needs the grounding audit to explicitly answer "is the correct answer's text genuinely different from
what this facet's normal direction already teaches," not just "does the shape's abstract inversion
definition apply."**

**d. The independent grounding audit can and will overturn an author's own self-assessment — trust
it over the author when they conflict.** Paper 4's D2 §2.2 item was flagged IRREDUCIBLE by its own
author; the independent auditor read it fresh, found it actually resolves, and named the specific
fix. If a sub-batch author flags something IRREDUCIBLE this paper, the grounding audit still checks
it fresh and independently — do not let the author's own flag pre-empt that check.

**e. Any fix — from a sub-batch author, from the audit, or from your own session — is provisional
until it's been run back through the mechanized gate, not just re-read.** Paper 4's session applied
audit-recommended fixes to two items and each fix round introduced a *new* mechanical error (a
letter-position break that violated the pre-planned tally, a duplicate-family violation, a word-cap
overrun) — none caught by inspection, all caught by re-running `tools/run-gate.js`. **Re-run the full
gate after every content edit, not just after the first assembly pass.**

**f. A parallel, smaller-scale version of D2's supply problem may exist in D7's section 7.2.** Paper
4's D7 multi-response item structurally duplicated Paper 1's own item at the same two facets
(`allowed-tools` + `context:fork` — section 7.2 has only two positive mechanism rows to pair for a
genuine 2-of-4 multi-response item). **If Paper 5 draws a 7.2 multi-response item again, check it
against all four prior papers' D7 items for the same structural-pairing duplication, not just a
stem-Jaccard score** — Jaccard didn't catch Paper 4's version either, since the wording differed even
though the underlying mechanism pairing was identical.

**g. `ARCHETYPE-LEDGER.md`'s own shape-budget (hard floor 4, hard ceiling 11) is real and is not one
of the 13 numbered gate checks.** Paper 2 shipped a violation (S8 at 12, S7 at 3) that nothing ever
caught. Paper 4's session caught its own version pre-dispatch by computing the shape tally before
authoring started — **do the same here**: compute and print the shape tally from your central plan
before dispatching any sub-batch, and rebalance if any shape falls outside [4, 11]. Whether this
becomes a formal gate check 14 is still an open decision for Ram (`GENERATION-INTELLIGENCE.md`
Session 7's pending-decisions list) — until it is, this remains something you have to remember to
check, not something the gate will catch for you.

---

## 5 — Paper 5 specifics — what's actually different from Paper 4

Per the orchestration prompt's §7.3 series table, Paper 5 is "rolling triples · direction-inverted ·
Confirmed-weakness adjustment first eligible to fire twice running":

**a. Direction inversion continues exactly as Paper 4 established it** — 17+ items (≥2 per shape,
all 8 shapes) marked `direction: "inverted"`, built against the inversion table's per-shape
definition, spread across domains. Re-verify the exact per-paper minimum item count for each shape
against `ARCHETYPE-LEDGER.md`'s current instance table (it now includes Paper 4's 63 rows) before
assuming any specific facet/shape pairing is still fresh — several of Paper 4's own inverted
instances may now be at or near their own 2-use cap for a future paper, not just D2's.

**b. Confirmed-weakness adjustment is named as "first eligible to fire twice running" at Paper 5** —
but this requires two consecutive *scored* papers, which do not exist yet per §3 above. If Papers 1-4
remain unscored when this paper is generated, this mechanism has nothing to fire on this time either;
say so explicitly rather than skipping the check silently.

**c. Two things are due at Paper 5 that are not paper-content work:**
- **The D2 decision from §2 above** — this is not deferrable to "surface it before Paper 6" anymore;
  it is very plausibly a hard blocker for this paper's own D2 quota.
- **Ram's open decision on whether shape-budget compliance (F-31) becomes a formal, numbered gate
  check.** Raise it again if it hasn't been settled since Paper 4's session ended; keep computing the
  tally pre-dispatch either way.

---

## 6 — Central planning (do this once, in full, before any dispatch)

Exactly as every prior paper's session did:

1. Domain quota — fixed at 11/8/12/10/9/9/4 unless a confirmed-weakness adjustment is in force (needs
   two consecutive *scored* papers unambiguously weakest by attempt date, single-answer items only —
   check fresh, don't assume) or Ram's §2 decision changes D2's quota for this paper specifically.
2. Objective floor pass (38 objectives, one each) + discretionary pass (cap 3/objective) —
   recomputed fresh; no cross-paper cap on objective coverage, only on facet reuse.
3. Format split — 55 single + 8 multi-response, `selectN:2` on all eight, pairs capped at ≤2 repeats
   **within this paper**.
4. **Correct-letter multiset, pre-shuffled: Paper 5's short letter is D again** (the rotation
   D→C→B→A repeats: P1=D, P2=C, P3=B, P4=A, P5=D). Plan as {A×14, B×14, C×14, D×13} or whatever the
   exact split works out to — recompute from scratch, don't assume Paper 4's exact numbers carry
   over (Paper 4's own short-A plan was {A13,B14,C14,D14}; Paper 5's short-D plan mirrors Paper 1's
   shape, not Paper 4's).
5. Facet freshness — per-domain exclude lists built from all four prior shipped papers' actual
   facets (§1.7 above), plus which sections are still wholly untouched. **D2 needs Ram's §2 decision
   resolved first, and the facet-level (not section-level) bookkeeping §2 describes.**
6. Distractor-family minimums per domain for `EVIDENCE-MISMATCH` and `DETECTIVE-FOR-PREVENTIVE`,
   summing to the paper-wide floors (≥15 and ≥9 respectively — these are fixed numbers, not
   percentages of the actual distractor count; Paper 4's session found and fixed a real bug in
   `tools/run-gate.js` from exactly this confusion, see F-32).
7. **Direction assignment per item** — at least 2 items per shape (16+ items total) marked
   `direction: "inverted"`, built against the inversion table's per-shape definition, spread across
   domains rather than concentrated in one. Check the archetype ledger's updated instance table
   (now including Paper 4) before assuming a specific (shape, section, facet) pairing is still under
   its 2-use cap.
8. **Shape-budget check (F-31)** — compute the full 8-shape tally from the plan before dispatching
   anything; rebalance any shape outside [4, 11] the same way Paper 4's session did (move a
   normal-direction item to a better-fitting shape, don't force the direction-inverted assignments
   to absorb the rebalance).

Write the finished plan to disk (§0) before dispatching anything.

---

## 7 — Build, dispatch, assemble, audit, gate, close-out

Follow the orchestration prompt's Phases 5-9 for content rules. Follow §0's checkpointing discipline
and §4's operational lessons for *how* to run the session. In order:

1. Resolve the §2 D2 decision with Ram before anything else touches D2.
2. Compute and save the central plan (§6), including direction assignments and the shape-budget
   check.
3. Dispatch sub-batches per domain, each ~5-6 items (D7 as one batch), `deepDive:null`, immediate
   per-batch save. Give every sub-batch the full item schema **including `cite`** (§4a). For any
   inverted-direction item, state the inversion explicitly and quote the inversion table's definition
   for that shape — don't leave it to the author to infer from the shape name alone.
4. Assemble: `lessonKey` (exclude answers under 3 content words, per F-18), cross-domain collision
   check, stem-Jaccard against all four prior papers' ledgers plus within-paper, family-cap
   check-and-fix (treat any fix as provisional until audited — F-25).
5. Build/update the shipped HTML from the template. Const changes: `PAPER_N`, `KEY`, `EXAM_MODE`
   (stays `false` — Paper 5 is not 8 or 10). Also fix the sticky-nav `.brand` text and the
   `fDemoCount` JS override line, exactly as every prior paper needed.
6. Run `node tools/run-gate.js mock-exams/CCAR-P_MockTest-5_v1.html 63` — checks 1, 10, 11 are now
   mechanized (§4b); fix any error to 0. Re-run after every subsequent edit, not just once.
7. Dispatch the independent grounding audit (7 fresh agents, one per domain, blind to the authors' own
   reasoning), same session, before generation-entry write-up. Every direction-inverted item gets the
   explicit genuineness check from §4c. Fix what's fixable (re-run the gate after each fix — §4e);
   document what's IRREDUCIBLE.
8. Manually verify what the mechanized gate still doesn't check: objective codes against the
   canonical 38, zero invented names, D1/D5/D6 zero inline tokens, the shape-budget tally (§4g).
9. **Open the shipped HTML in a browser** — confirm no "TEMPLATE"/"demo items" text anywhere, confirm
   the `cite` field actually renders (not "undefined") on at least one single-answer and one
   multi-response item, click Begin, answer both, confirm both score correctly, check the console for
   errors.
10. Phase 8 close-out: `EXAM-LOG.md` generation entry (mode, targeting consumed or explicitly none,
    the D2 decision and how it was implemented, the full 13-check gate table with computed values,
    the generation story), `DASHBOARD-DATA.jsonl` line with null scores, rebuild all three ledgers
    from the shipped HTML (using the real per-item `direction` field, not hardcoding "normal" — Paper
    4's session fixed this bug in its own rebuild scripts; carry the fix forward), `GENERATION-
    INTELLIGENCE.md` Session 8 entry.
11. **Run `/sync-up`** (or at minimum grep for the string "Paper 4 generated" / "Papers 1-4 generated"
    across root `CLAUDE.md`, root `README.md`, `CCAR-P/README.md`, `CCAR-P/ROADMAP.md`, and
    `prep with quiz/mock-exams/README.md`) before considering the session done. Paper 4's own
    generation session shipped clean but left five separate hub/status docs stale by three papers'
    worth of drift, caught only by a follow-up `/sync-up` — don't repeat that gap for Paper 5.

---

## 8 — Stop and ask, do not guess

Stop and ask the user if: **§2's D2 decision has not yet been resolved** (this is now a near-certain,
high-stakes trigger — very possibly a hard blocker, not a contingent one) · §3's preflight finds a
different paper number than expected · a scored Paper 1/2/3/4 exists with a Professor's Note that
conflicts with the latest Insights Round · the facet-level count in §2 step 2 comes back lower than
8 · the gate cannot be brought to 0 errors without changing an item's `correct[]` · you would need to
edit any `CCAR-P_Domain-N_v1.md` corpus file without it being the explicit corpus-expansion decision
from §2 · a sub-batch dispatch fails more than once at the same size (F-16/F-17/F-23 call this
settled at 4/4 clean runs — a failure now would be new evidence worth a decision before continuing) ·
an inverted-direction item's own facet is found to already be at its 2-use cap in the archetype
ledger for every direction the shape supports.

Report honestly. Quote real command output rather than reconstructing it. If a check did not run, say
so. Do not report a paper as generated until the gate is clean, the grounding audit has run (including
against this session's own assembly-time fixes, per F-25), the ledgers are rebuilt from disk, the
shipped file has been opened in a browser and actually clicked through — not just gate-checked — and
`/sync-up` (or an equivalent manual check) confirms the hub docs reflect Paper 5, not Paper 4.
