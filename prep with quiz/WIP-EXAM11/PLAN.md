# Exam 11 Generation Plan (WIP checkpoint)

**Date:** 2026-07-29 | **Operating prompt:** CCA-Orchestration-Prompt_v10.md | **Format:** FULL-60
**Purpose:** durable checkpoint plan (same discipline as Exam 10's WIP-EXAM10/, which shipped the first zero-fix exam in this project's history). No usage-limit risk flagged this session, so blocks are dispatched in PARALLEL (the standard 4.b.6/4.b.7 pattern), not serially.

## Slice status

| Slice | Work | Artifact | Status |
|---|---|---|---|
| A | This plan + SESSION-STATE checkpoint | WIP-EXAM11/PLAN.md | DONE |
| B | Block 1 Customer Support (g1-15) | WIP-EXAM11/block-1.json | DONE (2026-07-29; §2.3 facet=warranty-claim denial, §2.8 facet=get_customer+fetch_loyalty_tier; KD#12,KD#21 seeded) |
| C | Block 2 Developer Productivity (g16-30) | WIP-EXAM11/block-2.json | DONE (2026-07-29; §2.3 facet=deploy-freeze exception denial, §2.8 facet=dependency-scan+license-check, both confirmed developer-tooling only via grep; KD#27,KD#4 seeded) |
| D | Block 3 Claude Code CI (g31-45) | WIP-EXAM11/block-3.json | DONE (2026-07-29; §4.6 g38 4th-retest via reverse-direction any-is-correct mechanism, genuinely novel vs Exam7/8/10; §3.11 g36 2nd-retest via path-scoped-vs-workflow-scoped category mismatch, novel vs Exam8/10's half-split; KD#15,KD#25 seeded) |
| E | Block 4 Structured Data Extraction (g46-60) | WIP-EXAM11/block-4.json | DONE (2026-07-29; pipeline domain=recruiting/resume-parsing, distinct from Exam10's equipment-inspection; §3.1/§3.6 routine coverage, fresh facets; KD#19,KD#20 seeded) |
| F | Fidelity gate + citation-collision tally + Jaccard scan + cross-block content read | WIP-EXAM11/exam11-verified.json + GATE-REPORT.md | DONE (2026-07-29; found+fixed a REAL content collision the automated checks missed — g21/g29 were reskins of g3/g8's exact lessons; rewrote both onto genuinely distinct facets, D2 repeat pair now {§2.3,§2.6} not {§2.3,§2.8}; KD count 8, above 4-6 target but within 15 cap) |
| G | HTML build | mock-exams/CCA-Prep_MockTest-11_v1.html | DONE (2026-07-29; 174,293 bytes, DATA valid/60 Qs, disclosure line present, PB-20 regression check clean, UTF-8 verified byte-level, JS syntax verified) |
| H | EXAM-LOG skeleton, DASHBOARD-DATA line, GENERATION-INTELLIGENCE Session 14, SESSION-STATE close | logged exam | DONE (2026-07-29; all logs updated, WIP folder kept as audit trail) |

**GENERATION COMPLETE.** Exam 11 shipped at `mock-exams/CCA-Prep_MockTest-11_v1.html`, fully logged. A real D2 content collision was found and fixed by the coordinating session before shipping — see SESSION-STATE.md and GENERATION-INTELLIGENCE.md's PB-19 row for the full story.

## Governing inputs (Phase 1 state)

- **Professor's Note — Intent for Exam 11** (EXAM-LOG.md, written after Exam 10 scored 54/60, 2026-07-29): base quota unchanged (D2's decline is real but only a single exam as sole-weakest so far — needs Exam 11 to also show D2 weakest before the mechanical +4/−2/−2 fires). Bias: (a) a FOURTH re-test of D4 §4.6 (missed Exam 7, 8, 10 — three straight; if missed again this is a confirmed-stubborn corpus-study case, not more exam exposure); (b) a SECOND formal re-test of D3 §3.11 (fresh miss Exam 8, re-test miss Exam 10 — now 2-for-2, D3's new priority now that §3.1/§3.6 both recovered); (c) broader D2 coverage — all 9 sections, not just §2.3/§2.8, per Insights Round 2's explicit "test whether this is domain-wide breadth, the same pattern D3/D4 showed before it became visible."
- **Insights Round 2** (EXAM-LOG.md, fired after Exam 10 — exams_scored hit 6): Primary focus D4 §4.6 (confirmed stubborn, 3/3 exams missed). Secondary focus D2 as a domain (3-exam decline 100%→90.9%→81.8%, plus a §2.8 repeat). D1 and D5 need no attention (rock-solid / perfect, 3 exams running each).
- **exams_scored = 6** (Exam 4-8, Exam 10). Scoring Exam 9 or Exam 11 next brings it to 7 — not a multiple of 3, no Insights Round due at either scoring. (Insights Rounds trigger on scoring, not generation — irrelevant to this generation session directly.)
- **KD tracker clean** — ALL 10 of Exam 10's seeded KDs scored correct; zero weak rows, 6 exams running now. Session 13's explicit guidance: **tighten seeding back to 4-6 deliberate KDs**, not 10 opportunistic ones — no weak-signal KD to chase, seed only for periodic confirmation where a section naturally fits.
- **Corpus fully saturated** (all 71 sections Heavy, unchanged) — spread quota across distinct sections per block where possible (18 D1 / 9 D2 / 12 D3 / 20 D4 / 14 D5 sections available); D2's 11-over-9 still forces exactly 2 repeats.
- Exam 9 (generated 2026-07-19) remains unscored — its 60 stems are still part of the dedup ledger.

## Scenario draw (4 of 6 — first exam with NO rotation tiebreaker, all six tied at count 6 after Exam 10)

Rested: **Code Generation with Claude Code** and **Multi-Agent Research System** — both used in Exam 9 AND Exam 10 (a 2-exam-running streak); drawing either a third consecutive time carries this pool's highest convergence risk (per GENERATION-INTELLIGENCE.md's "Weak Patterns" warning about 4th+/heavy-recent use).

Drawn (each used in Exam 10 but NOT Exam 9, i.e. not on a consecutive streak) plus both scenarios rested since Exam 9:
1. **Customer Support Resolution Agent** (Primary: D1, D2, D5) — g1-15
2. **Developer Productivity with Claude** (Primary: D1, D2, D3) — g16-30 — rested since Exam 9, last used two exams ago
3. **Claude Code for Continuous Integration** (Primary: D3, D4) — g31-45 — rested since Exam 9, last used two exams ago
4. **Structured Data Extraction** (Primary: D4, D5) — g46-60

D4-carrier constraint satisfied (Claude Code CI + Structured Data Extraction — BOTH D4-carriers drawn, a deliberate change from most prior exams' single-carrier pattern, letting D4's 12 questions split 6/6 rather than concentrating ~10 in one block). Structural bonus: every domain now has exactly 2 primary-carrying blocks (D1: CS,DP · D2: CS,DP · D3: DP,CCCI · D4: CCCI,SDE · D5: CS,SDE) — the most balanced draw this project has produced, and it directly serves this exam's two real priorities: D2 breadth (2 D2-primary blocks) and D4/§4.6 (2 D4-primary blocks, so §4.6 doesn't have to carry the whole domain alone).

## Block × domain allocation (gate-verified: every Primary > every non-Primary per block)

| Block | D1 | D2 | D3 | D4 | D5 | Total |
|---|---|---|---|---|---|---|
| B1 Customer Support (P: D1,D2,D5) | 6 | 5 | 1 | 0 | 3 | 15 |
| B2 Developer Productivity (P: D1,D2,D3) | 6 | 6 | 3 | 0 | 0 | 15 |
| B3 Claude Code CI (P: D3,D4) | 1 | 0 | 6 | 6 | 2 | 15 |
| B4 Structured Data Extraction (P: D4,D5) | 3 | 0 | 2 | 6 | 4 | 15 |
| **Totals** | **16** | **11** | **12** | **12** | **9** | **60** |

Margins: B1 min(6,5,3)=3 > max(1,0)=1 ✓ · B2 min(6,6,3)=3 > max(0,0)=0 ✓ · B3 min(6,6)=6 > max(1,2)=2 ✓ · B4 min(6,4)=4 > max(3,2,0)=3 ✓ (tightest, still passes).

## Correct-answer letter pre-plan (4.d.5)

| Block | Multiset | Short letter |
|---|---|---|
| B1 | A4 B4 C4 D3 | D |
| B2 | A4 B4 C3 D4 | C |
| B3 | A4 B3 C4 D4 | B |
| B4 | A3 B4 C4 D4 | A |

Exam-wide: 15/15/15/15.

## Section assignments (grep-verify against live corpus headings before writing, PB-18 discipline)

Corpus is saturated — freshness is informational only per GENERATION-INTELLIGENCE.md (no fresh/moderate tier remains anywhere). Section picks below prioritize: (1) the two mandatory Professor's Note re-tests landing in the right block, (2) D1 breadth toward §1.4/§1.18 (both UNUSED in Exam 10 — the two D1 sections most overdue), (3) D2's full 9-section spread with §2.3/§2.8 deliberately repeated for reinforcement, (4) otherwise even spread, no repeats needed elsewhere since each domain's quota ≤ its section count outside D2.

**B1 Customer Support (15):**
- D1 (6): §1.1 · §1.4 (UNUSED Exam 10 — bring back) · §1.9 · §1.12 · §1.16 · §1.18 (UNUSED Exam 10 — bring back)
- D2 (5): §2.1 · §2.3 **facet A: a DIFFERENT business-error facet than Exam 10's refund-denial (e.g. a different tool's business-rule outcome — not process_refund again)** · §2.4 · §2.6 · §2.8 **facet A: a DIFFERENT tool-bundling facet than Exam 10's lookup_order/check_return_eligibility pairing**
- D3 (1): §3.4
- D5 (3): §5.4 · §5.8 · §5.9

**B2 Developer Productivity (15):**
- D1 (6): §1.2 · §1.5 · §1.10 · §1.11 · §1.14 · §1.17
- D2 (6): §2.2 · §2.3 **facet B: sibling of B1's §2.3 facet A — pre-declare and keep disjoint** · §2.5 · §2.7 · §2.8 **facet B: sibling of B1's §2.8 facet A — pre-declare and keep disjoint** · §2.9
- D3 (3): §3.2 · §3.5 · §3.7

**B3 Claude Code CI (15):**
- D1 (1): §1.15
- D3 (6): §3.3 · §3.8 · §3.9 · §3.10 · **§3.11 — MANDATORY 2nd formal re-test (D3's new priority; Exam 8 fresh miss, Exam 10 re-test miss, 2-for-2 — fresh facet required, different from both prior misses' half-split framing)** · §3.12
- D4 (6): **§4.6 — MANDATORY 4th re-test (missed Exam 7/8/10, three straight — fresh facet required, different mechanism than Exam 10's stale-tool-list framing, Exam 8's precondition-gating framing, and Exam 7's outcome-branching framing)** · §4.1 · §4.3 · §4.4 · §4.12 · §4.13
- D5 (2): §5.1 · §5.7

**B4 Structured Data Extraction (15):**
- D1 (3): §1.3 · §1.6 · §1.8
- D3 (2): §3.1 (periodic confirmation only — recovered Exam 10, no urgency) · §3.6 (periodic confirmation only — recovered Exam 10, no urgency)
- D4 (6): §4.2 · §4.5 · §4.7 · §4.8 · §4.9 · §4.19
- D5 (4): §5.2 · §5.3 · §5.5 · §5.6

Sections deliberately unused this exam (breadth headroom): D1 §1.7, §1.13 · D4 §4.10, §4.11, §4.14, §4.15, §4.16, §4.17, §4.18, §4.20 · D5 §5.10, §5.11, §5.12, §5.13, §5.14.

## KD seeding (TIGHTENED per Session 13 — 4-6 total, not 10)

No weak-signal KD exists (tracker fully clean). Seed opportunistically ONLY where a section naturally embodies a KD, ~1-2 per block, stop at 4-6 exam-wide. Do not force a KD into every question. Reasonable natural fits if they arise: KD#1/#4 (D3 scope/precedence, B2), KD#15 (D3 §3.8 headless, B3), KD#21 (D5 persistent case-facts, B1) — authors should pick opportunistically, not treat this list as mandatory.

## Style + format contract (binding, unchanged from Exam 10)

Stem: generic Situation + one decision question, median 50-55 words exam-wide, hard cap 95. Exactly 4 options, ≤35 words each, 1 correct + 3 documented-misconception distractors. Rationales: whyRight + 3 whyWrong, every one cites `D<n> §<sec>` or `KD#n`. Inline code/config tokens in 20-25% of options exam-wide (acceptable 15-30%). Zero invented company/product/persona names, ever. Out-of-scope 16-item list in Exam-Mechanics_v2 is a hard exclusion. Block narrative: "same-tools-progressing-narrative" continuity across the block's 15 questions.

## Question JSON schema (per block file — identical to Exam 10's)

```json
{"label": "<scenario name>", "narrative": "<block narrative for landing card>",
 "letterPlan": ["A","B",...15 letters...],
 "questions": [{"g": <global#>, "block": <0-3>, "blockLabel": "<scenario>", "domain": "D1",
   "section": "§1.1", "kd": <n or null>,
   "stem": "...", "options": ["...","...","...","..."], "correct": <0-3>,
   "whyRight": {"text": "...", "cite": "D3 §3.1"},
   "whyWrong": [{"option": <i>, "text": "...", "cite": "..."}, ...]}]}
```

## Dedup obligations (each author, before returning)

1. Grep EXAM-LOG.md "Questions Used" for EVERY assigned section — do not reuse/closely-paraphrase any prior stem (Exams 1-10, 540 stems, PLUS Exam 9's 60 unscored stems already logged at generation).
2. Check PRACTICE-TEST-STEMS_v1.md §2 (76 locked stems incl. official 12 samples).
3. B1 (Customer Support) and B4 (Structured Data Extraction) sections are at their 7th use — actively rewrite, don't just check.
4. B2 (Developer Productivity) and B3 (Claude Code CI) are also at their 7th use (rested only 1 exam) — same discipline applies.
5. Facet declarations above (§2.3, §2.8 pairs; §3.11 and §4.6 fresh-mechanism requirements) are HARD constraints.

## Landing card must include (verbatim)

"These 4 were curated to guarantee coverage across your exams — the real exam draws 4 of 6 at random each sitting, with no such guarantee."

## HTML build notes (Slice G)

- File: `mock-exams/CCA-Prep_MockTest-11_v1.html`. Template: MockTest-10 structure (same AI Oracle Quiz v2 design system). **PB-20 CAUTION: verify NO hardcoded `exam_n:10` literal survives anywhere in the build — grep the full output file for the string "11" is unhelpful (too common), instead explicitly grep for `exam_n:` and confirm every occurrence reads `DATA.exam_n`, not a bare number, before shipping.**
- `KEY = "cca-mock-11"`. JS comment block at top listing all 60 stems + the 4 scenarios drawn (Phase 4.g).
