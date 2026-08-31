# Paper 2 — Central Plan: Domain Quota, Objective Floor, Letter Pre-Plan, Slot Table

Computed centrally before any authoring, per orchestration prompt §5.1 ("the correct letter for item k
is decided here; drafting writes the correct option into that position"). Read ONLY your own domain's
section below. g-numbers run continuously 1-63 across all seven domains in D1..D7 order, matching
Paper 1's convention.

**Correct-letter multiset for the 55 single-answer items: A14 / B14 / C13 / D14** (Paper 2's short
letter is C, per the P1→P2→P3→P4 D→C→B→A rotation). Multi-response pairs across the 8 items: AB×2,
CD×2, AC×1, AD×1, BC×1, BD×1 — no pair exceeds the cap of 2. Both are pre-planned below; do not deviate
from the letter/pair given for your g-numbers.

---

## D1 — Solution Design & Architecture (11 items: g1-g11, 1 multi)

**Already used in Paper 1 (exclude these exact facet IDs):** F-1.1-01, F-1.2-01, F-1.3-01, F-1.4-01,
F-1.5-01, F-1.6-01, F-1.7-01, F-1.9-01, F-1.10-01, F-1.11-01, F-1.12-01.
**Wholly untouched section (bonus fresh content):** 1.8 (Orchestration Topology — Parallel, Sequential,
Iterative Refinement), objective O1.4.
**Token rule: ZERO inline code/config tokens in any D1 option.**
**Family minimums this domain: EVIDENCE-MISMATCH >= 3, DETECTIVE-FOR-PREVENTIVE >= 2.**

| g | objective | suggested section | format | correct |
|---|---|---|---|---|
| 1 | O1.1 | 1.1 (fresh facet, not -01) | single | B |
| 2 | O1.1 | 1.2 (fresh facet, not -01) | single | D |
| 3 | O1.2 | 1.9 (fresh facet, not -01) | single | A |
| 4 | O1.4 | 1.6 first choice (fresh situation, not -01); if 1.6 has no second independently-multi-qualifying situation, use 1.5 or 1.7 instead | **multi** | **A+B** |
| 5 | O1.2 | 1.10 (fresh facet, not -01) | single | C |
| 6 | O1.3 | 1.3 (fresh facet, not -01) | single | B |
| 7 | O1.3 | 1.4 (fresh facet, not -01) | single | A |
| 8 | O1.4 | 1.7 (fresh facet, not -01) | single | D |
| 9 | O1.4 | **1.8 (wholly fresh section — any facet)** | single | C |
| 10 | O1.5 | 1.11 (fresh facet, not -01) | single | A |
| 11 | O1.6 | 1.12 (fresh facet, not -01) | single | B |

Objective coverage check: O1.1x2, O1.2x2, O1.3x2, O1.4x3, O1.5x1, O1.6x1 = 11. All 6 D1 objectives covered.

---

## D2 — Claude Models, Prompting & Context Engineering (8 items: g12-g19, 1 multi)

**Already used in Paper 1 (exclude these exact facet IDs):** F-2.1-01, F-2.2-01, F-2.3-01, F-2.4-01,
F-2.5-01, F-2.6-01, F-2.7-01, F-2.8-01.
**Sections 2.6, 2.7, 2.8 are now FACET-EXHAUSTED** (each had exactly 1 facet, already used) — do not
draw a decision-table item from them this paper.
**Wholly untouched section:** 2.9 (Modular Prompts & Skills), objective O2.5.
**Family minimums this domain: EVIDENCE-MISMATCH >= 2, DETECTIVE-FOR-PREVENTIVE >= 1.**
D2 is the tightest-supply domain in the whole corpus (18 facets total) — use fresh rows carefully, do
not waste a section's only remaining facet on a weak item.

| g | objective | suggested section | format | correct |
|---|---|---|---|---|
| 12 | O2.1 | 2.1 (fresh facet, not -01) | single | D |
| 13 | O2.1 | 2.1 (a DIFFERENT fresh facet than g12 — section has 3 total) | single | C |
| 14 | O2.2 | 2.2 (fresh facet, not -01) | single | A |
| 15 | O2.2 | 2.2 (a different fresh situation than g14, with 2 independently-true answers) | **multi** | **C+D** |
| 16 | O2.3 | 2.3 or 2.4 (fresh facet, not -01) | single | D |
| 17 | O2.3 | whichever of 2.3/2.4 you did NOT use for g16 (fresh facet, not -01) | single | B |
| 18 | O2.4 | 2.5 (fresh facet, not -01 — section has 2 total) | single | C |
| 19 | O2.5 | **2.9 (wholly fresh section — its only facet)** | single | A |

Objective coverage check: O2.1x2, O2.2x2, O2.3x2, O2.4x1, O2.5x1 = 8. All 5 D2 objectives covered.

---

## D3 — Integration (12 items: g20-g31, 2 multi)

**Already used in Paper 1 (exclude these exact facet IDs):** F-3.1-01, F-3.2-01, F-3.3-01, F-3.4-01,
F-3.5-01, F-3.6-01, F-3.7-01, F-3.8-01, F-3.9-01, F-3.11-01, F-3.13-01, F-3.14-01.
**Wholly untouched sections:** 3.10 (Index Coupling & Post-Refresh Degradation, O3.5), 3.12 (Retrieval
Depth vs Reranking, O3.6).
**Family minimums this domain: EVIDENCE-MISMATCH >= 3, DETECTIVE-FOR-PREVENTIVE >= 2.**

| g | objective | suggested section | format | correct |
|---|---|---|---|---|
| 20 | O3.1 | 3.1 (fresh facet, not -01) | single | C |
| 21 | O3.2 | 3.2 (fresh facet, not -01) | single | B |
| 22 | O3.3 | 3.4 (fresh facet, not -01) | single | D |
| 23 | O3.2 | 3.3 (fresh situation, not -01 — "select two" authorization/identity controls) | **multi** | **A+C** |
| 24 | O3.3 | 3.5 (fresh facet, not -01) | single | A |
| 25 | O3.4 | 3.6 or 3.7 (fresh facet, not -01) | single | C |
| 26 | O3.6 | 3.11 (fresh facet, not -01) | single | B |
| 27 | O3.6 | **3.12 (wholly fresh section)** | single | D |
| 28 | O3.7 | 3.13 (fresh facet, not -01) | single | C |
| 29 | O3.5 | 3.8, 3.9, or **3.10 (wholly fresh)** — "select two" RAG/chunking/indexing practices | **multi** | **B+D** |
| 30 | O3.5 | whichever of 3.8/3.9/3.10 you did NOT use for g29 (fresh facet) | single | A |
| 31 | O3.8 | 3.14 (fresh facet, not -01) | single | B |

Objective coverage check: O3.1x1, O3.2x2, O3.3x2, O3.4x1, O3.5x2, O3.6x2, O3.7x1, O3.8x1 = 12. All 8 D3 objectives covered.

---

## D4 — Evaluation, Testing & Optimization (10 items: g32-g41, 1 multi)

**Already used in Paper 1 (exclude these exact facet IDs):** F-4.1-01, F-4.2-01, F-4.3-01, F-4.4-01,
F-4.5-01, F-4.9-01, F-4.9-02, F-4.10-01, F-4.11-04, F-4.12-01.
**Wholly untouched sections:** 4.6 (Model-Graded Evaluation), 4.7 (Two-Layer Evaluation — RAG and
Agentic), 4.8 (Reliability Aggregation — pass@k vs pass^k) — all three feed objective O4.2 and are
completely fresh content.
**Family minimums this domain: EVIDENCE-MISMATCH >= 2, DETECTIVE-FOR-PREVENTIVE >= 1.**

| g | objective | suggested section | format | correct |
|---|---|---|---|---|
| 32 | O4.1 | 4.1 or 4.2 (fresh facet, not -01) | single | D |
| 33 | O4.2 | **4.6 (wholly fresh section)** | single | B |
| 34 | O4.2 | **4.7 (wholly fresh section)** | single | A |
| 35 | O4.2 | **4.8 (wholly fresh section)** | single | D |
| 36 | O4.3 | 4.9 (fresh facet — not -01 or -02; section has 7 total) — "select two" valid regression/A-B practices | **multi** | **A+D** |
| 37 | O4.4 | 4.10 (fresh facet, not -01) | single | C |
| 38 | O4.5 | 4.11 (fresh facet, not -04) | single | B |
| 39 | O4.5 | 4.11 (a DIFFERENT fresh facet than g38) | single | D |
| 40 | O4.6 | 4.12 (fresh facet, not -01) | single | A |
| 41 | O4.6 | 4.12 (a DIFFERENT fresh facet than g40) | single | C |

Objective coverage check: O4.1x1, O4.2x3, O4.3x1, O4.4x1, O4.5x2, O4.6x2 = 10. All 6 D4 objectives covered.

---

## D5 — Governance, Safety & Risk Management (9 items: g42-g50, 1 multi)

**Already used in Paper 1 (exclude these exact facet IDs):** F-5.1-01, F-5.2-01, F-5.3-01, F-5.4-01,
F-5.5-01, F-5.6-04, F-5.7-01, F-5.8-01, F-5.10-01.
**Wholly untouched sections:** 5.9 (Independent Verification of Confident Output, O5.2), 5.11
(Transparency — Disclosure vs Explainability, O5.5).
**Token rule: ZERO inline code/config tokens in any D5 option.**
**Family minimums this domain: EVIDENCE-MISMATCH >= 2, DETECTIVE-FOR-PREVENTIVE >= 1.**

| g | objective | suggested section | format | correct |
|---|---|---|---|---|
| 42 | O5.1 | 5.1 or 5.2 (fresh facet, not -01) | single | C |
| 43 | O5.2 | **5.9 (wholly fresh section)** | single | A |
| 44 | O5.2 | 5.6 (fresh facet, not -04 — section has 10 total) | single | D |
| 45 | O5.2 | 5.7 (fresh facet, not -01) | single | B |
| 46 | O5.4 | 5.5 (fresh facet, not -01) — "select two" retention/audit practices | **multi** | **B+C** |
| 47 | O5.3 | 5.8 (fresh facet, not -01) | single | A |
| 48 | O5.4 | 5.3 or 5.4 (fresh facet, not -01) | single | C |
| 49 | O5.5 | 5.10 (fresh facet, not -01) | single | B |
| 50 | O5.5 | **5.11 (wholly fresh section)** | single | D |

Objective coverage check: O5.1x1, O5.2x3, O5.3x1, O5.4x2, O5.5x2 = 9. All 5 D5 objectives covered.

---

## D6 — Stakeholder Communication & Lifecycle Management (9 items: g51-g59, 1 multi)

**Already used in Paper 1 (exclude these exact facet IDs):** F-6.1-01, F-6.2-01, F-6.3-01, F-6.4-01,
F-6.6-01, F-6.7-01, F-6.8-01, F-6.9-01, F-6.12-01.
**Wholly untouched sections:** 6.10 (Feedback Loops and Expectation Drift, O6.3), 6.11 (Pilot to Scale
— the Assumption Audit, O6.5).
**Avoid section 6.5** — it has no decision table (0 facets), not needed this paper.
**Token rule: ZERO inline code/config tokens in any D6 option.**
**Family minimums this domain: EVIDENCE-MISMATCH >= 2, DETECTIVE-FOR-PREVENTIVE >= 1.**

| g | objective | suggested section | format | correct |
|---|---|---|---|---|
| 51 | O6.1 | 6.1 (fresh facet, not -01) | single | B |
| 52 | O6.1 | 6.2 (fresh facet, not -01) | single | D |
| 53 | O6.2 | 6.4 (fresh facet, not -01) | single | A |
| 54 | O6.2 | 6.6 (fresh facet, not -01) | single | C |
| 55 | O6.5 | **6.11 (wholly fresh section)** — "select two" pilot-to-scale safeguards | **multi** | **A+B** |
| 56 | O6.3 | 6.9 (fresh facet, not -01) | single | D |
| 57 | O6.3 | **6.10 (wholly fresh section)** | single | B |
| 58 | O6.4 | 6.7 or 6.8 (fresh facet, not -01) | single | C |
| 59 | O6.5 | 6.12 (fresh facet, not -01) | single | A |

Objective coverage check: O6.1x2, O6.2x2, O6.3x2, O6.4x1, O6.5x2 = 9. All 5 D6 objectives covered.

---

## D7 — Developer Productivity & Operational Enablement (4 items: g60-g63, 1 multi)

**Already used in Paper 1 (exclude these exact facet IDs):** F-7.1-01, F-7.2-01, F-7.3-01, F-7.8-01.
**Wholly untouched section:** 7.5 (AI Tooling in the Pipeline, O7.2) — 7 facets, all fresh.
**Avoid sections 7.4, 7.6, 7.7** — no decision table, not needed this paper.
**Note:** section 7.8 is declared-dual O7.1/O7.3 — either objective tag is valid for an item drawn from it.
**Family minimums this domain: EVIDENCE-MISMATCH >= 1, DETECTIVE-FOR-PREVENTIVE >= 1.**

| g | objective | suggested section | format | correct |
|---|---|---|---|---|
| 60 | O7.1 | 7.1 or 7.2 (fresh facet, not -01) | single | B |
| 61 | O7.2 | **7.5 (wholly fresh section)** | single | D |
| 62 | O7.3 | 7.8 (fresh facet, not -01) — "select two" enforcement mechanisms | **multi** | **C+D** |
| 63 | O7.2 | **7.5 (a DIFFERENT fresh facet than g61)** or 7.3 (fresh facet, not -01) | single | A |

Objective coverage check: O7.1x1, O7.2x2, O7.3x1 = 4. All 3 D7 objectives covered.

---

## Grand totals (verify before reporting back)

Domain quota: D1=11, D2=8, D3=12, D4=10, D5=9, D6=9, D7=4 → 63.
Format: 55 single + 8 multi.
Objectives: all 38 covered at least once, none exceeding 3.
Single-answer letters: A14 / B14 / C13 / D14.
Multi pairs: AB, CD, AC, AD, BC, BD, AB, CD (no pair over 2 uses).
Family floors: EVIDENCE-MISMATCH >= 15 total, DETECTIVE-FOR-PREVENTIVE >= 9 total (domain minimums above sum to exactly these).
