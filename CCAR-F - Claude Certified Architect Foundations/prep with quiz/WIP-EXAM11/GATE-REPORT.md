# Exam 11 — Fidelity Verification Gate Report (Phase 4.e.6)

Run 2026-07-29 against the merged 60-question set (`exam11-verified.json`). One real issue was found and fixed before this final run — documented below rather than hidden.

| # | Check | Computed value | Threshold | Pass/Fail | Fix applied |
|---|---|---|---|---|---|
| 1 | No invented names | 0 hits | 0 | **PASS** | — |
| 2 | Correct-letter tally (per block / exam-wide) | B0 4/4/4/3 · B1 4/4/3/4 · B2 4/3/4/4 · B3 3/4/4/4 · Exam-wide 15/15/15/15 | Each block within 1 of 4/4/4/3; exam-wide within 1 of 15/15/15/15 | **PASS** | A transcription error while hand-fixing g29 (below) briefly put `correct` at index 0 instead of the pre-planned index 1 (letter B) — caught by re-running this exact check, fixed by reordering options. |
| 3 | Stem/option word count | Stems 43-54(median)-67; options 8-33 | Stem median 50-55 (cap 95); option cap 35 | **PASS** | — |
| 4 | Block domain tally vs primary | B0 primary-min 3 > nonprimary-max 1; B1 3>0; B2 6>2; B3 4>3; exam-wide D1:16 D2:11 D3:12 D4:12 D5:9 | Every primary domain outnumbers every non-primary in its block | **PASS** | — |
| 5 | Inline code/config token rate | 56/240 options = 23.3% | Target 20-25%; acceptable 15-30% | **PASS** | — |
| 6 | Scenario-rotation disclosure line | Not yet on any artifact | Must appear verbatim on landing card | **PENDING → Slice G** | To be added during HTML build |

## A real content collision was found and fixed — not just a citation issue

The automated citation-collision tally and a 0.30-threshold Jaccard scan both reported clean on the first pass. A manual cross-block content read (reading all four flagged questions' full text side by side, per the standing PB-19 discipline) found something neither automated check could see:

- **§2.3 (g3 vs g21, original draft):** both questions tested the *identical* underlying lesson — a business-rule denial should be `retriable: false` with a customer-friendly explanation — just reskinned with different tool names (warranty claim vs. deploy-freeze exception). This is a real content collision despite passing both automated checks, because the facet-fence instructions given to each block ("use a different tool") were satisfied while the underlying teaching point was not actually different.
- **§2.8 (g9 vs g29, original draft):** same problem, worse — §2.8's actual corpus content (`CCA-Prep_Domain-2_v2.md` §2.8) is genuinely ~4 lines with exactly ONE teachable lesson (prefer prompt-bundling over a composite tool). There is no second facet available in the corpus at all, unlike §2.3 which does support multiple distinct facets on inspection (four error categories, business-rule denial, valid-empty-vs-access-failure, error-handling-at-the-right-level).

**Fix applied (by the coordinating session directly, not a re-dispatch):**
- g21 rewritten from the business-rule-denial facet (already covered by g3) onto §2.3's genuinely distinct "valid empty results vs. access failure" facet (an audit tool returning an ambiguous empty result for both a genuine zero-findings case and an unreachable backend) — confirmed as a different lesson from g3 on read.
- g29 reassigned from §2.8 entirely (since no second facet exists there) to §2.6, using the MCP-primitive-taxonomy facet (tools/resources/prompts) — a facet distinct from g8's community-vs-custom-server facet, confirmed on read. §2.8 now appears exactly once in the exam (g9).
- Re-ran the full gate script after the fix; caught and corrected one further transcription slip (g29's letter) before this final clean run.

This changes the exam's D2 repeat pair from the originally-planned {§2.3, §2.8} to {§2.3, §2.6} — a valid substitution, since the requirement is "2 of D2's 9 sections repeat with genuinely distinct facets," not any specific two sections.

**Structural section-repeat check:** confirmed via script — the ONLY sections used more than once anywhere in the exam are the (now corrected) D2 pair above. D1 uses 16 of its 18 sections, D3 all 12, D4 12 of 20, D5 9 of 14, each exactly once.

**Internal Jaccard near-duplicate scan (stem-level, threshold 0.30):** 0 pairs flagged across all 60 stems, both before and after the fix.

**Mandatory targeted re-tests, freshness confirmed on read:**
- D4 §4.6 (g38, 4th re-test): tests the reverse direction — a scenario where `"any"` is actually correct (a per-language test-writing tool roster where the template type isn't knowable ahead of time) — genuinely distinct mechanism from Exam 7 (outcome-branching), Exam 8 (precondition-gating), and Exam 10 (stale-tool-list).
- D3 §3.11 (g36, 2nd formal re-test): tests a category-mismatch trap (path-scoped content wrongly bundled into a Skill) — distinct from both Exam 8 and Exam 10's "half-split" framing.

**KD budget note:** came in at 8 (targets #4, #12, #15, #19, #20, #21, #25, #27), above the Session 13 tightening target of 4-6 — each block correctly stayed within its own "1-2" instruction, but 4 blocks × 2 sums above the intended exam-wide ceiling. Still well within the hard 15-question cap from the orchestration prompt, and every seed is a genuine natural fit (no forcing reported by any author) — not treated as a fidelity failure requiring rework, but logged honestly rather than claimed as hitting the target.

**Verdict: all 6 gate checks pass. One real content-collision issue was found by the manual cross-block read (not by any automated check) and fixed directly. The exam ships as corrected.**

Next: Slice G (HTML build), then Slice H (logging).
