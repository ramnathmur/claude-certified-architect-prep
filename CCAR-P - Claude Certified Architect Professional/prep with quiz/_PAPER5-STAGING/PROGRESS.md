# Paper 5 Generation — Progress

**COMPLETE — 2026-09-02.** `mock-exams/CCAR-P_MockTest-5_v1.html` shipped, 0 gate errors (checks
1/10/11/14 all PASS), 0 documented IRREDUCIBLE T1 exceptions, browser-verified. EXAM-LOG.md,
DASHBOARD-DATA.jsonl, all 3 ledgers, GENERATION-INTELLIGENCE.md Session 8, and 5 hub docs (root
CLAUDE.md, root README.md, CCAR-P README.md, ROADMAP.md, mock-exams README.md) all updated. This
file is kept as the historical record of the run, per standing practice — not deleted after
completion, but no longer live for a "resume" command (there is nothing left to resume).

**Started:** 2026-09-01. Resume rule: read this file, continue from the first unchecked item. Do not
re-derive state by re-reading outputs; do not restart.

## Decisions locked in (Ram, 2026-09-01)

1. **D2 corpus expansion — DONE.** 21 new decision-table rows added to `CCAR-P_Domain-2_v1.md`
   across all 9 sections (F-2.1-04/05, F-2.2-05, F-2.3-04/05, F-2.4-03/04, F-2.5-03/04,
   F-2.6-02/03/04, F-2.7-02/03/04, F-2.8-02/03/04, F-2.9-02/03/04). `FACET-LEDGER.md` updated to
   match (D2 now 39 facets, corpus total 372). D2 can now draw fresh facets normally for Paper 5 —
   no reuse-inversion or misconception fallback needed this paper.
2. **Generate Paper 5 as a 5th untargeted diagnostic** — proceed without pausing to sit an existing
   paper. No Professor's Note / Insights Round to consume. Phase 7.1 targeting: N/A.
3. **Shape-budget (F-31) becomes formal gate check 14** — add to `tools/run-gate.js` this paper.

## Checklist

- [x] Read CLAUDE.md (root + CCAR-P folder)
- [x] Read orchestration prompt v2, EXAM-FACTS_v1.md, EXAM-LOG.md (all 4 papers), GENERATION-INTELLIGENCE.md Session 7
- [x] Preflight (§3): confirmed Paper 5 is next, confirmed Papers 1-4 all unattempted
- [x] D2 facet/direction ground-truth extraction from shipped HTML (`_PAPER5-STAGING/analyze-prior-papers.js`, `prior-papers-analysis.json`, `d2-facet-direction.json`)
- [x] Ram's 3 decisions confirmed (D2 expansion, proceed untargeted, gate check 14)
- [x] D2 corpus expansion implemented in `CCAR-P_Domain-2_v1.md` + `FACET-LEDGER.md`
- [x] Central plan (§6): `plan-raw.json` → `plan.json` via `build-plan.js`/`finalize-plan.js`. 63 items, quota exact, 38 floor+25 discretionary, 55 single+8 multi (selectN:2, pairs ≤2), letters A14/B14/C14/D13 (short D), 17 direction-inverted (≥2/shape across all 8, spread 7 domains max 4), shapes all in [4,11] after a 4-item rebalance (3.2→S8, 3.5→S6, 1.9→S4, 4.12→S6). Rendered `p5-slots.md`. Two items (D3/3.1, D5/5.8) are exhausted-facet reuse-inverted fallbacks (O3.1/O5.3 had zero fresh facet AND zero misconception left) — standing "direction doubling" mechanism, not a new decision. D2 needed no fallback at all post-expansion.
- [x] Wrote `p5-shared-brief.md` (schema + `cite` fix + inversion rules) and 13 per-batch slot files (`p5-d{N}-batch{k}-slots.json`, D7 single batch)
- [x] Add gate check 14 (shape-budget) to `tools/run-gate.js` — regression-tested clean against Paper 4's shipped HTML (all checks 1/10/11/14 PASS)
- [x] Dispatched all 13 sub-batch authoring agents in background (p5-d1-batch{1,2}, p5-d2-batch{1,2}, p5-d3-batch{1,2}, p5-d4-batch{1,2}, p5-d5-batch{1,2}, p5-d6-batch{1,2}, p5-d7) — each writes `_PAPER5-STAGING/p5-d{N}-batch{k}-items.json` (or `p5-d7-items.json`) the moment it finishes. Waiting on completion notifications.
- [x] Prepared (not yet run — waiting on all 13 batches): `assemble.js`, `build-html.js`, `extra-checks.js`, `rebuild-facet-ledger.js`, `rebuild-stem-ledger.js`, `rebuild-archetype-ledger.js`, all ported from `_PAPER4-STAGING/` and adapted for Paper 5 (paper number, D2-expansion note, check-14 mention).
- Batches completed so far: p5-d2-batch1, p5-d5-batch2, p5-d4-batch1, p5-d1-batch2, p5-d6-batch2, p5-d4-batch2, p5-d2-batch2, p5-d5-batch1, p5-d3-batch1, p5-d1-batch1, p5-d6-batch1 (11 of 13). Remaining: p5-d3-batch2, p5-d7. Do not re-dispatch, wait for notifications.
- g52's own batch confirmed the misconception+inverted resolution (used M-6.4 as anchor for a fresh S7 item, paired with g51) — matches the locked-in decision above exactly.
- New note: g53 (D6 6.10, inverted) flagged by its own author as "not a literal table row, a likely T1 case for audit" — add to the audit's extra-scrutiny list alongside g9/g34/g52.
- Extra note for assembly: g6 (D1 1.12, multi) reports `factAnswerRaw` as a `||`-joined pair of two rows' verbatim text (per the multi-response item's own dispatch instruction to combine two independently-correct sub-actions) — check `computeLessonKey` handles this sanely (it will just tokenize both halves together) rather than erroring.

### Real planning bug found and resolved: g9, g34, g52
`finalize-plan.js`'s DIRECTION_OVERRIDES was written assuming D1/1.4, D4/4.9, and D6/6.4 would
each draw a fresh facet, but `build-plan.js`'s freshness-greedy algorithm actually placed all
three on that section's misconception-unit fallback (kind:"misconception", since those sections'
facets were already exhausted) — confirmed directly against `plan.json`. The shared brief states
misconception items never carry `direction:"inverted"`, so this is a genuine plan/brief conflict,
not authoring error. All three sub-batch agents (D1b2/g9, D4b1/g34, D6b1/g52 — pending) caught
and flagged it themselves rather than silently picking an interpretation, and each authored a
fresh, section-grounded scenario per the `invGuidance` rather than literally rewriting the boxed
Misconception paragraph.

**Resolution (locked in):** keep the authored content and `direction:"inverted"` as-is for all
three — the items are well-grounded, pass T1-T4 on the authors' own checks, and are genuinely
different from their sections' normal-direction lesson. This is a newly-discovered variant, not a
rule violation to force-fix: when a DIRECTION_OVERRIDES target lands on a misconception-fallback
slot, treat the M-<section> id as a scenario anchor and author a fresh inverted item, exactly as
these three did. No mechanized check (validateItems, gate 10/11/14) is affected either way — this
is a construction-quality/documentation matter only. **Flag g9, g34, g52 explicitly for the
independent grounding audit's extra scrutiny** (matching F-27/F-28's precedent for reuse-inverted
items), and record this as a new GENERATION-INTELLIGENCE.md finding for Paper 6 onward: check
plan-raw.json's `kind` field before assigning a DIRECTION_OVERRIDES target, so this interaction is
anticipated rather than caught after dispatch next time.
- [x] Assemble: all 13 batches loaded, 63 items, 0 lessonKey collisions, letters/shapes/directions all match plan exactly. 25 sub-batch transparency notes recorded in `assembly-notes.json`.
- [x] Fixed ARCHITECTED family-cap violation (22→19): g16 opt D→DISCARD, g24 opt B→REPAIR, g47 opt C reverted to ARCHITECTED (my first pass had wrongly created a duplicate family on g47 by moving opt C to DETECTIVE-FOR-PREVENTIVE when opt A already was — fixed).
- [x] Built HTML, ran gate — first pass found 5 check-1 errors (g28/g36 missing literal "select N" phrasing, g37 spread, g47 family dup, g57 word cap) + 7 stem-Jaccard collisions ≥0.30 (g28,g29,g45,g54,g55×2,g62 vs Papers 2-4, including g45 essentially reinventing Paper 4's own g45 scenario). Fixed all by rewording stems/options directly in `items-assembled.json`, **rebuilt HTML, re-ran gate — 0 errors, checks 1/10/11/14 all PASS.** 26 stem-length soft-band warnings remain (guidance not a cap, comparable to Paper 4's 30).
- [x] Dispatched independent grounding audit (7 agents, one per domain, blind to sub-batch notes/plan/brief — each given only the domain corpus file + `audit-input-D{N}.json`, plus domain-specific *structural* facts to check without revealing which items the authors themselves doubted). Waiting on results.
- [x] Applied D1 fixes directly (6 family-tag corrections, g2 stem reword, g6 T1 rebuild, g16 T1 reword) — done in `items-assembled.json`.
- [x] Dispatched 5 parallel fix agents (D3, D4, D5, D6, D7) with the exact audit findings + relevant corpus sections, each writing `fix-output-D{N}.json` with only their domain's corrected item objects. D5 and D6/D7 include real content reworks (g44 cosmetic-restate fix, g45/g53/g63 full rewrites, g49 direction flip, g51 re-citation). Waiting on completion.
- [ ] Merge all fix-output-D{N}.json into items-assembled.json, re-check paper-wide family-cap (ARCHITECTED was at 20/19 after D1 fixes — recheck after D3-D7 fixes land, since several rewrites touch ARCHITECTED-tagged options), re-run build-html.js + gate
### Audit results (7 domains, 6 back so far — only D7 pending)

**D1 (back):** PASS on grounding/T1-T2 for all 11 items, but **6 family-tag mismatches** vs. the
corpus's own established usage (g1-C should be HALF-MOVE not WRONG-AXIS; g2-D should be WRONG-AXIS
not REPAIR; g5-C should be ARCHITECTED not OVERSPEC; g9-C should be ARCHITECTED not OVERSPEC;
g10-B should be WRONG-AXIS or EVIDENCE-MISMATCH not HALF-MOVE; g11-A should be HALF-MOVE not
ARCHITECTED). **g2 stem defect**: closing question asks "what should the panel's output include"
when it means what the panel *receives* — reword. **g6 T1 doesn't hold**: t1Clause (cost) doesn't
actually flip to t1Alt=A when deleted (A's flaw is independently a latency-SLA breach, not a cost
one) — needs a new t1Clause/t1Alt pair, not a patch. All 3 inverted items (g1, g4, g9) confirmed
genuine, not cosmetic.

**D5 (back) — the most serious findings of the audit.** **g44 CONFIRMED cosmetic restate** — the
exact failure mode F-27/F-28 exist to catch: the "inverted" answer teaches the identical
route-by-confidence-and-consequence lesson the anchor's own normal-direction scenario already
teaches, just with fraud/SLA nouns substituted for document/volume nouns. Needs a real rework, not
a patch — anchor on 5.8's OTHER row instead (genuinely-low-volume, uniformly-high-consequence work
where blanket 100% review actually IS correct — test recognizing that, which is the true opposite
of the anchor's lesson). **g45 IRREDUCIBLE as constructed** — two stacked problems: (1) leftover
"EU data-residency" text in whyRight/whyWrong/t1Clause from my own earlier Jaccard-fix stem
rewrite (I changed the stem to PCI/CDE language but never updated the downstream fields — same
class of bug as g29's) — this is now a confirmed pattern, **check every Jaccard-rewritten stem's
whyRight/whyWrong/t1Clause for the same leftover-reference bug**; (2) deeper problem: the "scoped
exception at the infrastructure layer" mechanism I invented in my own invGuidance doesn't exist
anywhere in 5.3's actual decision table (real pattern: classify → de-identify/tokenize → re-
associate locally → audit the crossing). Needs a full content rework grounded in that real
mechanism, not a text patch. **g49 FIXABLE via direction flip** — same invented-mechanism problem
in 5.4: the corpus states FedRAMP absolutism explicitly ("no configuration or added control makes
the deployment compliant," word "exception" appears nowhere in Domain 5) and 5.4's own worked
scenario resolves boundary friction by complying, not carving out an exception. **Resolution:**
flip g49 to `direction:"normal"`, correct answer C (route through the authorized environment or
keep the data out — matching the corpus's real, stated resolution) — this makes g49 test the
absolutism directly rather than a fabricated exception. **Cascading shape-floor check:** with g49
now normal, S8-inverted drops to {g13 (D2), g45-reworked (D5)} = 2, still meets the ≥2 floor —
confirmed safe. Also noted: g42 and g47 are a near-duplicate archetype reskin (both §5.2, same
rule, same 4-option shape) — acceptable per this project's precedent (2 of 9 on one lesson-shape
is not a violation) but flagged for awareness. g43's t1Alt doesn't trace cleanly — needs
re-pairing. g46/g47 have minor family-tag mismatches (HALF-MOVE fits better than EVIDENCE-MISMATCH
resp. the T1 needs re-pairing).

**D2, D3, D4, D6 findings:** see entries above. D7 still pending.

**D6 (back):** 5/9 PASS. **g51 FIXABLE** — cited to 6.2 but its actual lesson (a non-negotiable
compliance mechanism) lives in 6.6, not 6.2 (which is the four-part accuracy-bounding framework
only); recite section/facet to 6.6 (6.6 already has g57, so this stays within the 2-per-section
cap). **g54 FIXABLE** — leftover "latency ceiling" wording in options A/B/D from before the stem
was reworded to a context-window limit (self-inflicted — likely from my own earlier edit pass or
the author's own draft-to-final transition); also t1Clause references "a recorded walkthrough"
but the final stem says "a slide" — align both to the actual final stem. **g55 FIXABLE — real
numeric self-contradiction**: stem says "1 in 350" / "hand-corrected 15%", but correct options
B/C and t1Clause say "1-in-400" / "18%" and whyRight references a "150-case pilot" not in the
stem at all — reconcile to one consistent set of numbers throughout. **g53 needs a rework, not a
patch** — cited to 6.10 but the auditor traced its actual tested skill (ruling out a seasonal
case-mix confound before crediting an intervention) to 6.4's real row instead ("aggregate is a
weighted average over a mix that will change"); 6.10's own decision table (recurring-vs-one-off,
structured capture loop) supports none of it. Chose to rewrite g53's content to genuinely test
6.10's own table in inverted form (keeps section caps clean — 6.4 already has g52) rather than
recite to 6.4 — read 6.10 fresh before rewriting.

**D3 (back):** 10/12 PASS. **g20 FIXABLE** — the reuse-inversion answer (keep 5 role-scoped tools,
don't split) is genuinely correct and non-cosmetic, but `whyRight`/`whyWrong.A`'s stated mechanism
("splitting risks stale eligibility across turns") appears nowhere in §3.1 — reground in §3.1's
actual discriminator (decision-space size / description-quality, not transactional staleness).
**g29 FIXABLE — self-inflicted bug**: my own stem-Jaccard rewrite (turn earlier) changed g29's stem
to "weekly... 2-hour runtime budget" but never updated options A/C or their whyWrong text, which
still say "90-minute SLA"/"nightly" from the pre-rewrite version — align the options/rationale to
the stem's current weekly/2-hour framing. **g28 (§3.3 multi, dedup vs Papers 1/4): judged genuinely
IRREDUCIBLE** — the auditor confirmed §3.3's decision table has only one row-pair that fits an
internal-shared-account multi-response item; rows 2-4 are alternate-scenario conditions, not
layerable requirements. Any 3.3 multi-item at this point is structurally forced onto the same
pairing — a corpus-thinness limitation (matching D2's own pre-expansion problem and D7's F-29),
not an authoring defect. Document as IRREDUCIBLE in the generation entry, do not force a rewrite.

**D2 (back):** 7/8 PASS, all 4 inverted items (g12/13/14/16) confirmed genuine (not cosmetic
restates). **g16 FIXABLE (metadata only)** — `t1Clause` invents a "stays within the cache's
retention window" concept that never appears in the stem; reword to the literal stem phrase
("high-volume") and let the retention-window reasoning live in the explanation, not the clause
text. No stem/option/correct-answer change needed.

**D4 (back):** 8/10 PASS. **g34 FIXABLE** — content genuinely teaches §4.10's diagnosis-attribution
skill (timing-correlated cause vs. evidence-supported cause), not §4.9's release-path skill its
`section`/`facet`/`objective` claim (D4 4.9, M-4.9, O4.3) — a real citation/objective mismatch I
introduced by writing 4.9's invGuidance as an S3 diagnosis-order inversion when 4.9's actual theme
is regression-then-A/B process, not diagnosis order. **Cannot simply retag to 4.10** (would make 3
items from section 4.10 this paper — g35, g40 already there — violating the 2-per-section cap).
**Fix plan:** rewrite g34's stem/whyRight/whyWrong to genuinely test 4.9's own axis in inverted
form — e.g. a prompt change that WAS properly regression-tested/A-B-validated and holds steady,
then a stakeholder wrongly blames it for an unrelated later incident; correct answer is "don't roll
back the validated change, the real cause is elsewhere" (still S3-shaped: recent-change-blamed vs
pinned-variables-point-elsewhere, but content stays inside 4.9's release-path domain). Keep
section/facet/objective as originally assigned (D4 4.9, M-4.9, O4.3) once reworded.
**g35 FIXABLE** — `t1Clause` inversion text ("Recall@k measured low (0.55), leaving retrieval
unverified") is self-contradictory: a MEASURED-low value is verified-and-failing, not unverified,
so it doesn't justify t1Alt A's "should be re-measured" framing. Fix: reword to "Recall@k not yet
measured" (mirroring g41's own construction) — no stem/option changes needed, `t1Clause`/`t1Alt`
text only.
- [ ] Manual checks: objective codes vs canonical 38, no invented names, D1/D5/D6 zero inline tokens, shape-budget tally
- [ ] Open shipped HTML in browser, click through, verify cite renders, both formats score correctly, no console errors
- [ ] EXAM-LOG.md Paper 5 entry (mode, D2 decision + corpus-expansion story, gate table, generation story)
- [ ] DASHBOARD-DATA.jsonl line
- [ ] Rebuild FACET-LEDGER.md, STEM-LEDGER.md, ARCHETYPE-LEDGER.md from shipped HTML
- [ ] GENERATION-INTELLIGENCE.md Session 8 entry
- [ ] /sync-up or manual hub-doc check (root CLAUDE.md, root README.md, CCAR-P/README.md, CCAR-P/ROADMAP.md, mock-exams/README.md)
