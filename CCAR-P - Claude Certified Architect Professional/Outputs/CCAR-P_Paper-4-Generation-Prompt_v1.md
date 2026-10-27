# CCAR-P Mock Test Paper 4 — Generation Prompt

**Written:** 2026-08-31, at the end of the session that generated Paper 3. Paper 3 generated cleanly on
the third straight run of the redesigned pipeline (13/13 sub-batches, zero stalls) but surfaced one
finding that changes what Paper 4 can do without a decision from Ram first — see §2 below before
planning anything. This document supersedes `CCAR-P_Paper-3-4-Generation-Prompt_v1.md` for the Paper 4
work that document's own §5 flagged but did not fully resolve.

---

## 0 — Session-continuity rule: save to disk continuously, not at the end

Unchanged from the Paper 3 prompt, and still the load-bearing rule. A generation session runs for
hours and a large token budget; background dispatches can fail outright partway through (documented
twice now, Papers 2 and — differently — nowhere on Paper 3, which went 13-for-13 clean). Design the
session around **cheap, frequent, durable checkpoints**:

1. Compute the central plan once, write it to disk immediately, before dispatching any authoring agent.
   Use `prep with quiz/_PAPER4-STAGING/plan.json` and a rendered `p4-slots.md` — never only the
   session's ephemeral scratchpad. Verify the path resolves inside
   `CCAR-P - Claude Certified Architect Professional/prep with quiz/` before writing anything.
2. Every authoring sub-batch writes its own output file the moment it finishes.
3. Re-save the merged items file after assembly and after every fix pass.
4. If running low on budget or context with the paper unfinished, stop and write a resume prompt in
   the same shape as Paper 2's and Paper 3's sessions used — what's done (exact file paths), what's
   open, the exact next action, decisions locked in, gotchas.
5. Never trust your own account of what shipped over the actual files. Every check in this prompt reads
   from disk, not from memory of what you intended to write.

---

## 1 — Before anything else

Read these, in this order. Paths are relative to `CCAR-P - Claude Certified Architect Professional/`:

1. `CLAUDE.md` (repo root)
2. `CLAUDE.md` (this folder)
3. `prep with quiz/CCAR-P-Orchestration-Prompt_v2.md` — **THE AUTHORITY** for schema, style caps, the
   T1-T4 tests, distractor-family taxonomy, and the phase structure, including §7.2's Papers-4-7
   direction-inversion policy and §7.3's series table. Where this prompt and the orchestration prompt
   disagree, the orchestration prompt wins.
4. `EXAM-FACTS_v1.md`
5. `prep with quiz/EXAM-LOG.md` — every `SCORED` heading, sorted by attempt date. Read the Paper 3
   entry in full — it has the full generation story, the 13-check gate table, and the D2 finding this
   prompt is built around.
6. `prep with quiz/GENERATION-INTELLIGENCE.md` — read **Session 6 in full** (F-21 through F-26, Paper
   3's findings). Earlier sessions for background if needed, but Session 6 is the one with material
   you cannot skip.
7. `FACET-LEDGER.md`, `STEM-LEDGER.md`, `ARCHETYPE-LEDGER.md`, `CCAR-P_Objective-Map_v1.md`. The first
   three were rebuilt from the shipped HTML after Paper 3 (not from a session's own account) and now
   carry Papers 1-3's usage — but see F-21: extract facet freshness from the shipped HTML files
   directly as the ground truth, the same way Paper 3's session did, rather than trusting the ledger's
   "used" column at face value. The three shipped papers to check are
   `mock-exams/CCAR-P_MockTest-1_v1.html`, `..._2_v1.html`, `..._3_v1.html`.

---

## 2 — Read this before planning D2's quota — it is very likely a stop-and-ask trigger

**D2's real decision-table facet supply is now fully exhausted.** All 18 of D2's facets have been used
across Papers 1-3 (8 + 8 + 2), and Paper 3 additionally used 6 of D2's 9 misconception units, leaving
only **3 unused D2 facets of any kind** — `M-2.3`, `M-2.5`, `M-2.9` — against Paper 4's 8-item D2 quota.

The facet-supply note in `FACET-LEDGER.md` lists three ways out, in preference order: direction
doubling, misconception units, corpus expansion. Misconception units are now nearly spent too (3 of 9
left). Direction doubling is the mechanism Paper 4 is structurally built around — §7.2 of the
orchestration prompt makes Papers 4-7 the phase where every shape appears with its direction inverted —
but **do not assume this automatically extends D2's facet supply**. The facet-supply note's own
example of direction doubling in action is a corpus-authored pair (D1's §1.3 tests the normal direction,
§1.4 exists specifically to test the reverse) — a directly, of a fresh section, purpose-written for the
opposite direction. **D2's corpus file has no such paired sections** — a direct check this session ran
found zero matches for "reverse direction" or "inverted" anywhere in `CCAR-P_Domain-2_v1.md`. Whether
re-testing an already-used D2 facet from an inverted stem angle counts as a legitimately fresh slot, or
is just re-testing the same fact with cosmetic phrasing changes, is not something this prompt can settle
from the corpus as it currently stands.

**Do not resolve this unilaterally.** Per the standing rule (`CLAUDE.md` root, and repeated in the
Paper 3/4 prompt's §8), any question that touches how a corpus file's content gets stretched to cover a
quota is Ram's call, not something to improvise past. Concretely, before authoring any D2 item for
Paper 4:

1. Confirm the exact remaining D2 supply against the shipped HTML (facets: 0 fresh of 18; misconception
   units: 3 unused of 9 — `M-2.3`, `M-2.5`, `M-2.9`) using the same extraction method as Paper 3's
   session (`_PAPER3-STAGING/parse-facet-ledger.js` and `analyze-prior-papers.js` are reusable
   templates, not committed tools — copy the pattern into a fresh `_PAPER4-STAGING/` script).
2. **Stop and ask Ram** which of these he wants for D2's remaining 5 items (8 quota − 3 unused
   misconception units): (a) approve direction-inverted reuse of specific already-used D2 facets, and if
   so, confirm the mechanism produces a genuinely different testable decision rather than a cosmetic
   restate; (b) do the D2 corpus expansion now (the ~20 new decision-table rows `FACET-LEDGER.md` has
   flagged as pending since Session 1, `F-01`) rather than waiting for the Paper 4 Insights Round as
   previously planned; (c) temporarily lower D2's quota for this paper only and raise another domain's,
   documented as a one-off, not a standing confirmed-weakness adjustment (which requires two consecutive
   *scored* papers and is a different mechanism); or (d) something else Ram prefers.
3. Whatever Ram decides, record it in the Paper 4 generation entry as a locked-in decision, the same way
   the `deepDive` demotion and the sub-batch dispatch size were recorded as Ram's decisions in Paper 2's
   entry.

This is the single most important thing this document changed from the last one. Everything below
assumes this conversation has already happened before any D2 item is authored.

---

## 3 — Preflight: which paper is actually next, and is it targeted or untargeted

Do not assume Paper 4 without checking, even though it is very likely correct.

1. Check `mock-exams/` for the highest existing `CCAR-P_MockTest-N_v1.html` (as of this writing:
   `..._3_v1.html`) and `DASHBOARD-DATA.jsonl` for the highest `paper_n` (as of this writing: `3`). The
   next paper is one past whichever is higher. Abort and report if this prompt's Paper 4 assumption
   doesn't match what you find.
2. Check `EXAM-LOG.md` for `## Paper N — SCORED <date>` headings. As of this prompt being written
   (2026-08-31), **none of Papers 1, 2, or 3 had been sat.** If that is still true when you run this:
   - Paper 4 is generated the same way Papers 1-3 were — an **explicitly untargeted diagnostic**. Gate
     check 13 = N/A. Do not fabricate targeting triples. §5's Phase-7.1-rule-4 habit-escalation check
     (below) also has nothing to fire on without scored data — say so explicitly rather than guessing.
   - **Stop and ask the user to confirm before generating**, exactly as the Paper 2 and Paper 3 sessions
     did — Ram may want to sit an existing paper first so real targeting and habit-escalation data
     exists, and Paper 4 is a meaningfully bigger structural jump (direction inversion begins) than
     Papers 1-3 were from each other.
   - If this is the situation, skip the targeting-specific instructions in §5 below.
3. If one or more of Papers 1-3 **have** been sat and scored by the time you run this:
   - Read the most recent Professor's Note (written after the most recently *attempted* paper by date)
     and the most recent Insights Round if more recent than that note.
   - Apply Phase 7.1 in full: every targeting triple gets ≥1 item from the opposite facet/direction,
     satisfied inside the fixed domain quota; ≥3 previously-missed triples left deliberately untargeted
     and named.
   - Check whether Phase 7.1 rule 4 (habit escalation) fires: has one distractor family captured ≥3
     items across two consecutive *scored* papers by attempt date? If so, that family's shape becomes
     the **correct** answer on 2-3 items this paper — this is a real, no-longer-hypothetical mechanism
     once two scored papers exist, and Paper 4 is the first paper positioned to actually use it.
   - If the Professor's Note and the latest Insights Round disagree, reconcile explicitly in the
     generation entry and state which won and why.

---

## 4 — What changed after Paper 3 — read this or the paper will cost more than it should

Six findings from Paper 3's session (`GENERATION-INTELLIGENCE.md` F-21 through F-26), condensed to what
changes how you work this paper. Full detail is in Session 6 of that file.

**a. Facet freshness extraction from shipped HTML, not the ledger's "used" column, is now standing
practice — do it again, do not skip it because the ledger looks freshly rebuilt.** `FACET-LEDGER.md`,
`STEM-LEDGER.md`, and `ARCHETYPE-LEDGER.md` were all correctly rebuilt from the shipped HTML after
Paper 3, but the discipline that matters is re-deriving the exclusion list from the three shipped
`mock-exams/CCAR-P_MockTest-{1,2,3}_v1.html` files at the start of *this* session, not trusting any
ledger's bookkeeping — including this one — at face value.

**b. Dispatch granularity (5-6 items per sub-batch) is now settled, not provisional — stop
re-verifying it.** Three consecutive clean runs (13/13, 13/13, 13/13) is enough evidence. Split each
domain's authoring into sub-batches of 5-6 items (D7's 4 items stay as one batch), same as Papers 2-3,
and do not spend session time re-litigating whether this still holds.

**c. Assembly needs BOTH the `lessonKey` collision check AND the stem-Jaccard check — they catch
different failure modes, not the same one.** Paper 3 shipped 0 `lessonKey` collisions but 2 real
content collisions, both caught only by stem-Jaccard (one against Paper 2's own shipped stem, one
within Paper 3 itself). `lessonKey` catches two items resting on the identical underlying corpus answer
text; stem-Jaccard catches two items built from overlapping *numbers and phrasing* even when the
underlying facet differs. Run both at assembly, against all three prior papers' stems for the
cross-paper check and against the paper's own 63 stems for the within-paper check.

**d. The independent grounding audit must also check this session's own assembly-stage fixes, not
just what the sub-batch authors wrote.** Paper 3's session made an assembly-time family-tag relabel to
satisfy the `DETECTIVE-FOR-PREVENTIVE` floor, and that relabel was itself wrong — caught only because
the grounding audit treated it with the same skepticism as authored content. When you fix a
family-cap violation, a dedup collision, or any other assembly-time problem by editing an item, treat
that edit as unverified until the grounding audit (§7 step 6, still run before the generation entry is
written) has checked it — do not assume a fix that makes the numbers work is self-evidently correct.

**e. Open, unresolved: the `t1Alt` IRREDUCIBLE rate varies more than expected across papers (Paper 2:
5/63, Paper 3: 8/63) and is not obviously tied to a domain's overall facet richness — 3 of Paper 3's 8
were in D1, which has 62 facets and no supply pressure.** Watch this rate on Paper 4. If it stays near
8/63 rather than reverting toward 5/63, that's evidence worth raising at whichever Insights Round comes
next (still gated on 3 *scored* papers, so likely not yet due) — the rate may be closer to a real
corpus-wide baseline than a fixable process defect.

**f. A shipped paper needs three separate template fixes, not one — verify all three in a browser, not
by diffing static HTML.** The `TEMPLATE`'s three leftover artifacts are: the landing `<h1>`/banner text
(static HTML), the sticky top-nav `<div class="brand">` text (also static HTML, but easy to miss since
it's outside the landing section), and a JS line —
`document.getElementById("fDemoCount").textContent = ITEMS.length + " demo items";` — that silently
overwrites a stat tile *at runtime* regardless of what the static HTML says. Paper 1 fixed all three
correctly; Paper 2 fixed none (a background task is pending to fix it — check whether it's landed
before this session, since a stale Paper 2 could otherwise mislead a "compare against a working
example" check); Paper 3 initially missed the second and third and only caught them by opening the
shipped file in a browser and clicking "Begin" after the gate already passed. **Do the same for Paper
4: after building the HTML and passing the gate, open it in a browser, confirm the nav bar and landing
page say "Mock Test 4" nowhere say "TEMPLATE" or "demo items", click Begin, answer a single-answer item
and a multi-response item, and confirm both score and show feedback correctly before considering the
paper done.**

---

## 5 — Paper 4 specifics — real structural differences from Papers 1-3

Paper 4 is not "another Paper 3." Per the orchestration prompt's §7.2/§7.3 series table:

**a. Direction inversion begins.** Per `ARCHETYPE-LEDGER.md`'s inversion table (Part 1), **each of the
8 shapes must appear at least twice this paper with its direction inverted** — read that table's
per-shape inversion definition before authoring (e.g. S5-inverted is "under-engineering — a stated
requirement is genuinely non-enumerable and the higher rung is correct," the reverse of S5-normal's
over-engineering trap). This is the mechanism aimed directly at root `CLAUDE.md` habit 3 (choosing the
option that *sounds* safer/more architected). Build this into the central plan (§6) as an explicit
per-item `direction` assignment, the same way letters and facets are pre-assigned — don't leave it to
each sub-batch to decide. **This is also the mechanism §2 above discusses for D2's supply crisis** — if
Ram approves direction-inverted reuse of an already-used D2 facet as one of D2's remaining slots, this
is where that decision gets implemented, with the inverted-direction stem genuinely testing the
opposite trap, not a cosmetic restate.

**b. Habit escalation may fire (Phase 7.1 rule 4).** If a distractor family has captured ≥3 items
across two consecutive *scored* papers by attempt date, that family's shape becomes the **correct**
answer on 2-3 items this paper. This requires real miss data from scored papers — per §3 above, if
Papers 1-3 aren't scored yet by the time Paper 4 is generated, this rule has nothing to fire on; say so
explicitly in the generation entry rather than guessing or skipping the check silently.

**c. Two things are due at Paper 4 that are not paper-content work — surface both, don't silently skip
either:**
- **The fidelity-gate mechanization.** Per `GENERATION-INTELLIGENCE.md`'s pending-decision list and
  orchestration prompt Phase 6's closing note, this is the paper where hand-checking stops being
  reliable. Build into `tools/run-gate.js` (as committed, reusable code, not a one-off script) the
  checks that have now been proven correct as one-off scripts across three papers:
  - Stem-Jaccard against `STEM-LEDGER.md`, threshold 0.30 (recalibrate the threshold if warranted —
    the ledger now holds 48 seeded + 63×3 = 237 generated stems, enough to check whether 0.30 still
    separates independent pairs from duplicates the way it did on 48).
  - The `lessonKey` cross-domain collision check — already mechanized in `validateItems()` since Paper
    1 (F-10), but fold in the minimum-token floor refinement from `GENERATION-INTELLIGENCE.md` F-18
    (an answer text under 3 content words is excluded from the check, not flagged or trusted).
  - The distractor-family-cap check (no family >25%, `EVIDENCE-MISMATCH` ≥8%, `DETECTIVE-FOR-PREVENTIVE`
    ≥5%, `ARCHITECTED` ≤10%) — proven as a one-off assembly-time check on three consecutive papers now
    (F-19), confirmed necessary every single time regardless of dispatch shape.
  - `_PAPER3-STAGING/extra-checks.js` and `_PAPER2-STAGING/assemble.js` are the reference
    implementations to consult, not committed tools themselves — port the logic, not the files.
- **The D2 corpus-expansion decision** — see §2 above. This is no longer a "surface it before Paper 6"
  item; Paper 4's own D2 quota is directly blocked on it. Do not generate any D2 item until this
  conversation has happened.

---

## 6 — Central planning (do this once, in full, before any dispatch)

Exactly as the orchestration prompt §5.1-5.2 and §3 require, and exactly as Papers 1-3 all did:

1. Domain quota — fixed at 11/8/12/10/9/9/4 unless a confirmed-weakness adjustment is in force (needs
   two consecutive *scored* papers unambiguously weakest by attempt date, single-answer items only —
   check fresh, don't assume) or Ram's §2 decision changes D2's quota for this paper specifically.
2. Objective floor pass (38 objectives, one each) + discretionary pass (cap 3/objective) — recomputed
   fresh; no cross-paper cap on objective coverage, only on facet reuse.
3. Format split — 55 single + 8 multi-response, `selectN:2` on all eight, pairs capped at ≤2 repeats
   **within this paper**.
4. **Correct-letter multiset, pre-shuffled: Paper 4's short letter is A** (the P1→P2→P3→P4 rotation is
   D→C→B→A, then repeats). Plan as {A×13, B×14, C×14, D×14} or whatever the exact split works out to —
   recompute from scratch, don't assume Paper 3's exact numbers carry over.
5. Facet freshness — per-domain exclude lists built from all three prior shipped papers' actual facets
   (§4a), plus which sections are still wholly untouched. **D2 needs Ram's §2 decision resolved first.**
6. Distractor-family minimums per domain for `EVIDENCE-MISMATCH` and `DETECTIVE-FOR-PREVENTIVE`,
   summing to the paper-wide floors (≥15 and ≥9 respectively, recompute the exact total once format
   split is fixed).
7. **Direction assignment per item** (new this paper) — at least 2 items per shape (16+ items total)
   marked `direction: "inverted"`, built against the inversion table's per-shape definition, spread
   across domains rather than concentrated in one.

Write the finished plan to disk (§0) before dispatching anything.

---

## 7 — Build, dispatch, assemble, audit, gate, close-out

Follow the orchestration prompt's Phases 5-9 for content rules. Follow §0's checkpointing discipline
and §4's operational lessons for *how* to run the session. In order:

1. Resolve the §2 D2 decision with Ram before anything else touches D2.
2. Compute and save the central plan (§6), including direction assignments.
3. Dispatch sub-batches per domain, each ~5-6 items (D7 as one batch), `deepDive:null`, immediate
   per-batch save. For any inverted-direction item, the sub-batch prompt must state the inversion
   explicitly and quote the inversion table's definition for that shape, not leave it to the author to
   infer from the shape name alone.
4. Assemble: `lessonKey`, cross-domain collision check, stem-Jaccard against all three prior papers'
   ledgers plus within-paper, family-cap check-and-fix (treat any fix as provisional until audited —
   §4d), save the merged file.
5. Build/update the shipped HTML from the template. Const changes: `PAPER_N`, `KEY`, `EXAM_MODE` (stays
   `false` — Paper 4 is not 8 or 10). **Also fix the sticky-nav `.brand` text and the `fDemoCount` JS
   override line (§4f) — do not stop at the landing HTML.**
6. Run `node tools/run-gate.js mock-exams/CCAR-P_MockTest-4_v1.html 63` — if §5c's mechanization
   landed, this should now cover more of the 13 checks than Paper 3's run did. Fix any error to 0.
   Re-run checks 2, 3, 6, 10 after any item swap.
7. Dispatch the independent grounding audit (7 fresh agents, one per domain, blind to the authors' own
   reasoning), same session, before generation-entry write-up. Fix what's fixable (and audit the fixes —
   §4d); document what's IRREDUCIBLE.
8. Manually verify what the mechanized gate still doesn't check: objective codes against the canonical
   38, zero invented names, D1/D5/D6 zero inline tokens.
9. **Open the shipped HTML in a browser** (§4f) — confirm no "TEMPLATE"/"demo items" text anywhere,
   click Begin, answer a single-answer and a multi-response item, confirm both score correctly, check
   the console for errors.
10. Phase 8 close-out: `EXAM-LOG.md` generation entry (mode, targeting consumed or explicitly none, the
    D2 decision and how it was implemented, the full 13-check gate table with computed values, the
    generation story), `DASHBOARD-DATA.jsonl` line with null scores, rebuild all three ledgers from the
    shipped HTML, `GENERATION-INTELLIGENCE.md` Session 7 entry.

---

## 8 — Stop and ask, do not guess

Stop and ask the user if: **§2's D2 decision has not yet been resolved** (this is now a near-certain
trigger, not a contingent one) · §3's preflight finds a different paper number than expected · a scored
Paper 1/2/3 exists with a Professor's Note that conflicts with the latest Insights Round · the corpus
cannot supply a facet a quota needs beyond what §2 already covers · the gate cannot be brought to 0
errors without changing an item's `correct[]` · you would need to edit any `CCAR-P_Domain-N_v1.md`
corpus file · a sub-batch dispatch fails more than once at the same size (this would be new evidence
against F-23's "settled" verdict, worth a decision before continuing rather than a third blind retry).

Report honestly. Quote real command output rather than reconstructing it. If a check did not run, say
so. Do not report a paper as generated until the gate is clean, the grounding audit has run (including
against this session's own assembly-time fixes), the ledgers are rebuilt from disk, and the shipped file
has been opened in a browser and actually clicked through — not just gate-checked.
