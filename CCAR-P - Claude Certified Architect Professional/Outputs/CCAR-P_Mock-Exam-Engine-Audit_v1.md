# CCAR-P Mock-Exam Engine — Audit and Engine Specification

**Written:** 2026-08-29
**Scope:** Part A — what the Foundations generator does and what CCAR-P inherited. Part B — what the
real CCAR-P exam looks like, measured from the official guide. Part C — the CCAR-P generation engine.
**Files read in full:** `CCA-Orchestration-Prompt_v10.md` (1107 lines), `QUESTION-ARCHETYPE-BANLIST.md`,
`EXAM-MODE-DESIGN_v1.md`, `PRACTICE-TEST-STEMS_v1.md` §1/§3, `GENERATION-INTELLIGENCE.md` (header,
freshness, distractor notes, pattern library, all 35 Open Findings rows), `tools/archetype_gate.py`
(header + check list), `CCA-Prep_Exam-Mechanics_v2.md` (TOC), `CCA-Prep_Key-Distinctions_v1.md` (TOC),
three generated papers (Exams 2, 14, 20 — embedded `DATA` JSON parsed programmatically),
`CCAR-P-Orchestration-Prompt_v1.md`, `CCAR-P_Corpus-Index_v1.md`, `CCAR-P_Domain-Template_v1.md`,
`CCAR-P_Domain-1..7_v1.md` (structural audit), `EXAM-LOG.md`, `DASHBOARD-SCHEMA.md`,
`mock-exams/README.md`, `CCAR-P_ExternalMock-1/3_v1.html`, `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`
(all 11 pages, text-extracted), `sop/SOP_Mock-Exam-Engine_v1.md`, `EXAM-FACTS_v1.md`, `ROADMAP.md`, and
both governing `CLAUDE.md` files.
**Nothing was written outside this file.** No corpus, exam, log, or dashboard file was modified.

---

## 1. Verdict

The Foundations generation logic is **partially replicated, and the split is not random**: the
learner-feedback half was ported and in three places improved, the item-fidelity half was not ported
at all. Of 66 distinct Foundations mechanisms, 16 are operative in CCAR-P (24%), 15 are specified but
have no file or artifact behind them (23%), 2 were deliberately dropped with the decision recorded
(3%), 31 are missing with no recorded decision (47%), and 2 do not apply. The sharper number is this:
of the 20 mechanisms that control **what a generated question looks like** — locked-stem ledgers,
measured style calibration, word-count budgets, correct-answer-letter pre-planning, inline-token rate,
generic framing, archetype dedup, and the six computed fidelity checks — **zero are operative in
CCAR-P, and only two of the twenty were a recorded decision.** Ram's suspicion is correct about the
generator and wrong about the feedback loop: `EXAM-LOG.md`, the Professor's Note, the confirmed-weakness
rule, the Insights cadence, and the dashboard schema all came across intact, and the CCAR-P versions
of the Note and the corpus item schema are better than the Foundations originals.

---

## 2. Part A findings

### 2.1 The Foundations pipeline, reconstructed as a mechanism list

`CCA-Orchestration-Prompt_v10.md` runs five phases. Its own header comment block (lines 1–125) is a
change log tying most rules to a named defect; those defects are carried in the table's provenance
column and expanded in §2.3.

| Phase | Reads | Decides | Writes | Failure it prevents |
|---|---|---|---|---|
| **1 State Load** (`<state_injection>` Steps 1–5) | `EXAM-LOG.md`, `PRACTICE-TEST-STEMS_v1.md`, `SESSION-STATE.md`, `GENERATION-INTELLIGENCE.md`, `CLAUDE.md`, `CCA-Prep_Exam-Mechanics_v2.md`, `CURRENT-DOCS-DELTA_v1.md` | Which of five mutually-exclusive recovery branches (A–E) applies | `SESSION-STATE.md` status=IN_PROGRESS; a Session Start disclosure block to the user | Generating cold; re-logging an exam already logged; losing an exam generated but never logged (Branch D) |
| **2 Score Entry** (a–h) | Pasted results JSON or a manual report | Which of four score formats was supplied; which domains are estimated; whether a weakness is confirmed | `EXAM-LOG.md` scored entry; `DASHBOARD-DATA.jsonl` line; the **Professor's Note — Intent for Exam N+1** | Estimated per-domain data silently driving quota changes; a single detailed result failing to influence the next paper |
| **3 Insight Extraction** (a–h) | The 3 most recent scored entries | Per-domain trends from non-estimated data only; repeated missed traps; pace | An Insights Round block in `EXAM-LOG.md` | Per-paper noise being read as a trend; a slow domain going unnoticed against the 2 min/question budget |
| **4 Exam Generation** (a–h, with a.5, b.5, b.6, b.7, c.5, d.5, e.5, e.6) | Corpus v2 files, Key Distinctions, style profile, generation intelligence, Professor's Note | Scenario draw, domain quota, section seeds, correct-answer letters, distractor families | 60 or 30 items with per-option rationales; the paper HTML; a JS stem comment block | Every item-fidelity failure listed in §2.3 |
| **5 Close** (a, a.5, b, c, d, e) | This session's own outputs | Which open findings are FIXED vs DEFERRED; which corpus gaps stay pending | `EXAM-LOG.md` skeleton, `DASHBOARD-DATA.jsonl` skeleton line, a full overwrite of `GENERATION-INTELLIGENCE.md`, a ~30-row self-verification table | A generation-quality finding being logged and forgotten; a corpus edit being applied without Ram's sign-off |

### 2.2 The supporting files, one function each

| File | Its single function | What breaks without it |
|---|---|---|
| `GENERATION-INTELLIGENCE.md` | Cross-session generation memory: KD coverage, corpus freshness, weak/effective patterns, scenario rotation, the Open Findings Ledger, Pending Corpus Decisions | Every session starts cold. Section freshness, distractor quality, and the findings ledger have no carrier, so the same weak distractor and the same over-used section recur with nothing to detect it |
| `PRACTICE-TEST-STEMS_v1.md` | Two jobs: §2 is a hard 76-stem exclusion ledger for material Ram sits himself; §3 is the measured style profile (n=76 stems, 304 options) that Phase 4a.5's word budgets and token rates are derived from | Generated items collide with the practice test Ram will take, destroying both. And style calibration becomes assertion — there is no measured target to enforce |
| `QUESTION-ARCHETYPE-BANLIST.md` | Bans *shapes*, not content: 7 content archetypes (BF-1..BF-7) and 2 rhetorical monocultures (BF-8 closing formula ≤20%, BF-9 opening formula ≤15%), plus Fidelity check 7 | Wording-level dedup passes reskins. Its own audit of 720 questions found a reskin pair at 0.717 Jaccard, and D2 §2.8 was missed on four sittings because the same shape was re-tested rather than re-taught |
| `tools/archetype_gate.py` | Mechanises Fidelity checks 1–5 and 7 from the shipped HTML: cross-exam Jaccard against all priors at a 0.40 threshold, letter tally, word counts, block-domain tally, inline-token rate, formula rates. Exit 0/1 | The checks revert to hand-tallying, which the prompt itself says is how a block once shipped 15 questions at the same letter undetected |
| `EXAM-MODE-DESIGN_v1.md` | A narrowly-scoped variant for final dress rehearsals: no per-question feedback, hidden score/accuracy pills, 120:00 countdown, no auto-submit. §7 explicitly fences it to two files | Without the fence, the mechanism gets adopted as the default. The SOP records this happening: CCDV-F's first engine build hardcoded Exam Mode as permanent behaviour, inverting the stated design stance (`sop/SOP_Mock-Exam-Engine_v1.md` §1, citing CCDV-F finding DV-12) |
| `CCA-Prep_Exam-Mechanics_v2.md` | Format facts, the official 6-scenario bank with each scenario's primary domains, answer-pattern heuristics, the in-scope whitelist and the **out-of-scope hard exclusion list** | Items get written on topics the exam does not test, and Fidelity check 4 has no primary-domain reference to compare a block against |
| `CCA-Prep_Key-Distinctions_v1.md` | 29 high-yield trap definitions across 6 groupings — the primary seed bank, with a per-exam cap (≤15) and a coverage cycle | Seeding falls back to unweighted section selection, so the highest-yield traps get tested by accident rather than on a schedule |

### 2.3 Defect provenance — the rules that exist because something broke

Taken from `GENERATION-INTELLIGENCE.md` "Open Findings Ledger" (35 rows) and the v10 header block.
These are the rows a CCAR-P design has to answer to.

| ID | The defect | The rule it produced |
|---|---|---|
| PB-01 | Nested background-agent parent stalled waiting on children, ~250K tokens per stall, recurring | Phase 4.b.7 delegation stall-watch: resume, don't restart |
| PB-02 / PB-09 | A block shipped all 15 questions at option A, undetected by its own QA | Phase 4.d.5 letter pre-plan **before** drafting; 4.e.5 as backstop only |
| PB-03 | A verification script's own regex silently dropped one exam's stems; "zero overlaps" was false | Phase 2.d.5 standing count-mismatch sanity check |
| PB-04 / PB-05 | Sibling sub-agents cannot see each other; one block's QA cannot catch a cross-block collision | Phase 4.b.6 task spec + the coordinating session owning the cross-block check |
| PB-06 | Corpus-freshness tallies were prose self-report | Phase 5a.5: extract `whyRight.cite` from the shipped `DATA` JSON as ground truth |
| PB-07 | Output directory was an unstated convention; Ram could not find Exams 2 and 3 | Phase 4.f names `mock-exams/` explicitly |
| PB-08 | The prompt instructed inventing a per-block company/agent name. A cold audit of 76 real-exam texts found **zero** named fictional companies | Generic framing only; Fidelity check 1, threshold 0 |
| PB-10 | A block's domain tally contradicted its own scenario's primary domains (Exam 3: D2 outnumbered D5) | Fidelity check 4 |
| PB-11 | Inline code/config token rate drifted freely | Target band 20–25%, fail outside 15–30%; Fidelity check 5 |
| PB-15 | Manual assembly of delegated blocks into one HTML `DATA` object introduced a transcription defect that re-reading did not catch | Assembly discipline; later generalised by the SOP's `validateItems()` |
| PB-17 | "Max 1 heavy section per exam" is unsatisfiable once a domain's quota exceeds its own section count | Overflow must be pre-planned and spread, not handled ad hoc |
| PB-19 (four variants) | Cross-item near-duplication that a citation tally cannot see: adjacent-section mis-citation; two citations to one section; **two different sections teaching the same lesson**; pre-declared facet fences satisfied while the lesson stayed identical | The archetype ban-list, and the rule that dedup must run on *shape and lesson*, not wording or citation |
| PB-20 | A template-substitution build script missed a hardcoded `exam_n:9` literal; Exam 10's export reported `"exam_n":9` | Dynamic references, not literals, in export payloads |
| PB-21 / PB-24 | Exam 9's KD seeds were logged but never entered in the tracker; Exam 13's were never written down at all and cannot be recovered | The tracker is a floor, not a record; a condition with no forcing function does not fire |
| PB-23 | Central authoring put prior stems into the drafting context: **20 of 60 stems landed above 0.30 Jaccard, one at 0.833** — a reskin differing by one percentage and one field name. Delegated exams shipped zero above 0.30 | Delegation is a dedup control, not just a speed control |
| PB-28 | Insights Round 4 was due and never ran; no session's own gate caught it | Cadence checks need a cross-session owner |
| PB-29 | A confirmed-weakness check compared against the wrong prior exam — generation-adjacent instead of attempt-adjacent — in the same session that restated the rule | Attempt chronology, mechanically |
| PB-30 (**still OPEN**) | Exam 20 Q55 is tagged `"domain": "D3"` while its stem, all four options, `whyRight`, and all three `whyWrong` cite only `Domain-4_v2.md §4.11`. The block-level check passed because both are primary domains for that block | A **per-question** domain-tag vs citation check. This is the one Foundations defect CCAR-P already fixed — see §2.4 |
| CG-03..CG-06 | The official guide moved v0.2 → v1.0 mid-prep: multiple-response items appeared, the Response Types section was deleted, result reporting changed, and the exam code changed | Quarterly re-verification of `EXAM-FACTS_v1.md` |

### 2.4 What a finished Foundations paper actually contains

Measured by parsing the embedded `const DATA` object out of three shipped papers.

| | Exam 2 (2026-07-06) | Exam 14 (2026-08-11) | Exam 20 (2026-08-16) |
|---|---|---|---|
| Items | 60 | 60 | 60 |
| Quota | 16/11/12/12/9 | 16/11/12/12/9 | 16/11/12/12/9 |
| Item keys | `g, block, blockLabel, domain, stem, options, correct, whyRight, whyWrong` | same + `selectN` on 13 items | same + `selectN` on 8 items |
| Correct-letter tally | **A20 / B17 / D12 / C11** | A12 / B12 / C12 / D11 + 13 multi | **A13 / B13 / C13 / D13 + 8 multi** |
| Stem words min/median/max | 42 / 55.5 / 73 | 42 / 50 / 59 | 40 / 55 / 78 |
| Option words median/max | 17 / 32 | 14 / 21 | 17 / 35 |
| Options per item | 4 (all) | 4×47, 5×9, 6×4 | 4 (all) |
| Multi-response | none | 13 (`selectN` 2 or 3) | 8 (`selectN` 2) |
| Inline code/config in options | **9.6%** | 21.8% | **30.0%** |
| Narrative framing | **named** — "Meridian Retail", agent "Aria" | generic | generic |
| Mode | Practice | Practice | **Exam Mode** (`EXAM_MODE = true`) |

Exam 2 predates PB-08 (named companies), PB-09 (letter pre-plan) and PB-11 (token rate) and fails all
three by the standards later imposed. Exam 20 lands the letter tally exactly on 13/13/13/13 and sits at
30.0% inline tokens — the top of the "acceptable" band and the exact boundary of Fidelity check 5's
FAIL threshold.

Per item, a finished paper carries: a position index `g` (must equal array index + 1), a `domain` tag,
a block index and label, the stem, an options array, a `correct` index (or sorted array for
multi-response), `whyRight: {text, cite}`, and `whyWrong: [{option, text, cite}]` with one entry per
non-correct option. Every rationale carries a corpus citation of the form `CCA-Prep_Domain-N_v2.md §N.M`.

The page itself produces the post-exam analysis: a per-domain **and** per-block results card, an
estimated scaled score `round((totalCorrect/60)*900+100)` shown against the 720 pass line, a
results-JSON export with a copy button, a `printAll()` full-rationale review, `localStorage`
save/resume with three-way routing, passive per-question timing, and — in Practice Mode — a
selection-aware rationale panel that leads with the picked option's `whyWrong` when the pick was wrong.

### 2.5 Mechanism-by-mechanism comparison

Classification key: **PORTED** = present and operative in CCAR-P. **PORTED-INERT** = specified in
CCAR-P's prompt, schema, or the SOP its `CLAUDE.md` binds it to, with no file, data, or tooling behind
it yet. **ABSENT-DELIBERATE** = CCAR-P's own files record the decision not to port.
**ABSENT-UNDECLARED** = missing with no recorded decision. **N/A** = does not apply, with reason.

#### State layer

| # | Foundations mechanism | Class | Justification (file · section) |
|---|---|---|---|
| F-01 | `EXAM-LOG.md` as the single authoritative standing record | PORTED | `CCAR-P .../EXAM-LOG.md` opening line + Conventions 1–7; `CCAR-P/CLAUDE.md` "Source of truth" table |
| F-02 | Cross-paper stem dedup ledger held inside `EXAM-LOG.md` (`dedup_stems`) | PORTED-INERT | `CCAR-P-Orchestration-Prompt_v1.md` Phase 4 check 4 asserts near-duplicate rejection, but the `EXAM-LOG.md` entry template has no stem list to check against — there is nothing to compare a new stem to |
| F-03 | External locked-stem ledger for material Ram sits himself (`PRACTICE-TEST-STEMS_v1.md` §2, 76 stems) | ABSENT-UNDECLARED | No equivalent file. The 45 ExternalMock items and the guide's 3 samples are exactly this category and are named in no exclusion list |
| F-04 | Measured style-calibration profile (§3, n=76 stems / 304 options) | ABSENT-UNDECLARED | No CCAR-P style profile exists. `CCAR-P-Orchestration-Prompt_v1.md` Phase 3 has prose ("the stem should carry a production constraint") with no measured target |
| F-05 | `SESSION-STATE.md` + five-branch recovery (A–E) | ABSENT-UNDECLARED | No `SESSION-STATE.md` in `prep with quiz/`; no branch logic in the CCAR-P prompt |
| F-06 | `GENERATION-INTELLIGENCE.md` as cross-session generation memory | PORTED-INERT | Mandated by `sop/SOP_Mock-Exam-Engine_v1.md` §6 and §7.6, which `CCAR-P/CLAUDE.md` "Mock-exam engine" binds this project to. File does not exist |
| F-07 | Corpus-section freshness tracking (`corpus_heavy` / `corpus_fresh`), tallied by ground-truth citation extraction from the shipped `DATA` JSON | ABSENT-UNDECLARED | Not in the CCAR-P prompt, the corpus index, or the SOP |
| F-08 | `weak_distractors` / `effective_patterns` / `weak_patterns` registries | ABSENT-UNDECLARED | No carrier file |
| F-09 | Out-of-scope hard exclusion list + in-scope whitelist | ABSENT-UNDECLARED | No CCAR-P equivalent of `Exam-Mechanics_v2.md`. Note: the CCAR-P guide v1.0 publishes no out-of-scope appendix, so this would have to be derived rather than transcribed |
| F-10 | `CURRENT-DOCS-DELTA` [CONFLICT-RISK] rule (never let a docs-vs-guide divergence be the scored distinction) | ABSENT-UNDECLARED | No delta file. The risk is live: the CCAR-P corpus index records a `/memory` → `/context` correction across five places in Domain 7, exactly this class |
| F-11 | Session Start disclosure block | ABSENT-UNDECLARED | Not in the CCAR-P prompt |

#### Scoring / learner layer

| # | Foundations mechanism | Class | Justification |
|---|---|---|---|
| F-12 | Multi-format score parsing (FORMAT 0–3) with estimated-domain quarantine | PORTED-INERT | CCAR-P Phase 6.1 names results-json only; `DASHBOARD-SCHEMA.md` `score_source` says "Anything else is lower trust and must be noted", but the fallback formats and the estimated-data exclusion rule are unwritten |
| F-13 | Scaled-score estimator | PORTED-INERT | `DASHBOARD-SCHEMA.md` `estimated_scaled` ("state the formula in the log entry"); `EXAM-LOG.md` template. The formula for N=63 is written nowhere |
| F-14 | Miss → trap cross-reference (Key Distinction matching) | ABSENT-UNDECLARED | No KD file. Functional successor exists: CCAR-P Phase 6.4 classifies each miss by distractor family |
| F-15 | Dedup/extraction count sanity check (PB-03) | ABSENT-UNDECLARED | Not present |
| F-16 | Confirmed-weakness rule — same domain unambiguously weakest on two consecutive papers **by attempt date**, tie fails | PORTED | CCAR-P Phase 2.2 and 6.3; `EXAM-LOG.md` Convention 3; `DASHBOARD-SCHEMA.md` `confirmed_weakness` |
| F-17 | Professor's Note — per-paper setter's brief | PORTED (improved) | CCAR-P Phase 1.2 reads it, Phase 2.3 consumes it, Phase 6.6 writes it, `EXAM-LOG.md` entry template carries it. **Improvement:** Phase 2.3 adds "the direction of the error being retested" — a repeat miss retested from the same direction proves nothing |
| F-18 | Insights Round every 3 scored papers | PORTED | CCAR-P Phase 6.7; `EXAM-LOG.md` Convention 4; `DASHBOARD-SCHEMA.md` `insight_round_due` |
| F-19 | `DASHBOARD-DATA.jsonl` append + schema | PORTED (improved) | `DASHBOARD-SCHEMA.md` exists, file exists (empty). **Improvement:** rule 2 fixes the `[correct, of]` array shape that drifted mid-project on Foundations; rule 4 forbids silent re-tagging of a shipped score |
| F-20 | Timing capture and pace analysis | PORTED (improved) | `EXAM-LOG.md` Convention 7 and the entry template's Pace section; `DASHBOARD-SCHEMA.md` `total_seconds`. **Improvement:** CCAR-P Phase 6.5 states the interpretation rule — slow misses are decision errors, not time pressure |

#### Generation layer

| # | Foundations mechanism | Class | Justification |
|---|---|---|---|
| F-21 | Domain quota derived from published weights | PORTED | CCAR-P Phase 2.1. The computed table for 17/13/19/16/14/14/7 × 63 is not written down in any file — see §4.1 |
| F-22 | Confirmed-weakness quota adjustment | PORTED (changed) | Foundations: fixed +4 to the weak domain, −2 D2, −2 D5, with collision rules. CCAR-P Phase 2.2: +2–4, subtract the same from the *strongest* domain, and **revert on the following paper**. Different mechanism, same purpose |
| F-23 | Professor's-Note section biasing inside a fixed quota | PORTED (improved) | CCAR-P Phase 2.3 adds the retest-direction requirement |
| F-24 | Trap/KD seed bank with a per-paper cap and a coverage cycle | ABSENT-UNDECLARED | No CCAR-P equivalent of `Key-Distinctions_v1.md` |
| F-25 | Fresh-section prioritisation and heavy-section cap | ABSENT-UNDECLARED | Not in the CCAR-P prompt. Acute here: 78 sections against a 63-item paper — see §4.2 |
| F-26 | Scenario bank of 6, 4-of-6 rotation, block × domain allocation table | ABSENT-DELIBERATE | `CCAR-P-Orchestration-Prompt_v1.md` "Deliberately not ported": "The scenario-block architecture… Add this phase back once the guide settles it" |
| F-27 | Generic-framing rule — no invented company, product, or persona name | ABSENT-UNDECLARED | Not mentioned anywhere in CCAR-P. This rule is independent of block structure and applies to standalone items. Its evidence base (zero named entities across 76 real texts) transfers directly: the CCAR-P guide's three samples are also uniformly generic ("A team", "An application", "A RAG system") |
| F-28 | Binding stem/option word-count budget | ABSENT-UNDECLARED | Not present |
| F-29 | Inline code/config token-rate band | ABSENT-UNDECLARED | Not present |
| F-30 | Correct-answer-letter pre-plan before any option text is written | ABSENT-UNDECLARED | Not present, and CCAR-P's Phase 4 six checks contain no letter tally. This is the mechanism whose absence produced PB-09 |
| F-31 | Per-option rationale block: `whyRight` + one `whyWrong` per distractor, each cited | PORTED | CCAR-P Phase 3: "Every question carries: `domain`, `section`, `format`, the correct answer, `whyRight`, and a `whyWrong` for each distractor". Corpus supports it — 158 tagged ❌ options |
| F-32 | Distractors drawn from documented corpus misconceptions; no fabricated flags or behaviours | PORTED | `CCAR-P_Domain-Template_v1.md` rule 4 (misconceptions quoted, not paraphrased) and rule 5; every corpus section carries a quoted misconception block |
| F-33 | Distractor-family variation within an item | PORTED (improved) | Foundations had a 4-archetype taxonomy living only in the style profile's prose. CCAR-P has six named families (OVERSPEC / DISCARD / REPAIR / ARCHITECTED / HALF-MOVE / WRONG-AXIS) **tagged inline on all 158 corpus distractors**, plus Phase 3's "three flavours of the same wrong answer make an item that tests nothing" |
| F-34 | Parallel sub-agent delegation task spec | ABSENT-UNDECLARED | Not present. PB-23 makes this a dedup control, not just a speed control |
| F-35 | Coordinating-session cross-item collision check (same lesson taught twice in one paper) | ABSENT-UNDECLARED | CCAR-P Phase 4.4 covers near-duplication *across papers*, not within one |
| F-36 | Delegation stall-watch | ABSENT-UNDECLARED | Not present |

#### Fidelity gate

| # | Foundations mechanism | Class | Justification |
|---|---|---|---|
| F-37 | A named, blocking pre-ship fidelity gate | PORTED (changed) | CCAR-P Phase 4, six checks, "Reject the paper and regenerate if any check fails". Different check set from Foundations' |
| F-38 | Check 1 — no invented company/product/persona names, threshold 0 | ABSENT-UNDECLARED | Not among CCAR-P's six |
| F-39 | Check 2 — correct-answer letter tally, per block and exam-wide | ABSENT-UNDECLARED | Not among CCAR-P's six |
| F-40 | Check 3 — stem/option word counts against the budget | ABSENT-UNDECLARED | Not among CCAR-P's six |
| F-41 | Check 4 — block domain tally vs scenario primary domains | N/A | No block structure (F-26 deliberately not ported), so there are no primary domains to compare against. Its per-question descendant **is** present as CCAR-P Phase 4.2 — see F-42 |
| F-42 | Per-question `domain` tag vs its own citations | **PORTED — and this is CCAR-P's own addition, not a Foundations port** | CCAR-P Phase 4.2, with the defect quoted: "A Foundations paper shipped with a question tagged D3 whose every citation was D4". That is PB-30, still OPEN in the Foundations ledger. CCAR-P fixed it before its first paper |
| F-43 | Check 5 — inline code/config token rate | ABSENT-UNDECLARED | Not among CCAR-P's six |
| F-44 | Check 6 — scenario-rotation disclosure line on the landing card | N/A | No scenario draw to disclose |
| F-45 | Check 7 — archetype collision against the ban-list and within the paper | ABSENT-UNDECLARED | Not among CCAR-P's six |
| F-46 | `QUESTION-ARCHETYPE-BANLIST.md` as a maintained, append-only artifact | ABSENT-UNDECLARED | No equivalent file |
| F-47 | `tools/archetype_gate.py` mechanised gate | ABSENT-DELIBERATE | `CCAR-P-Orchestration-Prompt_v1.md` "Deliberately not ported": "Rebuild only if paper volume justifies it" |
| F-48 | Per-block letter-distribution self-check against the pre-plan | ABSENT-UNDECLARED | Not present (and has nothing to check, since F-30 is absent) |

#### Build / artifact layer

| # | Foundations mechanism | Class | Justification |
|---|---|---|---|
| F-49 | Item schema | PORTED (improved) | CCAR-P Phase 3 field list + `sop/SOP_Mock-Exam-Engine_v1.md` §2 table. **Improvements over Foundations:** an explicit `section` field (Foundations buried the section inside `whyRight.cite` prose), an explicit `format` field, and `reviewStatus` |
| F-50 | Multiple-response items — `selectN`, sorted-array `correct`, count stated in the stem, all-or-nothing | PORTED-INERT | SOP §2 specifies all four. CCAR-P Phase 2.4 says "Match the confirmed single-answer / multiple-response ratio" — **there is no confirmed ratio anywhere**, so that instruction cannot execute as written |
| F-51 | Paginated one-question-per-page HTML with a selection-aware rationale panel | PORTED-INERT | SOP §2 and §7.2 (copy the CCDV-F reference template's anchors). No CCAR-P template file exists |
| F-52 | Exam Mode as a narrowly-scoped exception | PORTED-INERT | SOP §1 states the design stance and the fence; `EXAM-LOG.md` template carries a `Mode:` line; `DASHBOARD-SCHEMA.md` has `mode`; `ROADMAP.md` Phase 5 wants two Exam Mode papers. No spec file, no implementation |
| F-53 | Sticky nav — elapsed timer, live running-accuracy pill, collapsible jump-map | PORTED-INERT | Via SOP §1's branch list and the CCDV-F reference; nothing CCAR-P-side |
| F-54 | Per-domain results card with a scaled estimate against the pass line | PORTED-INERT | SOP §4 (domain-readiness grid); `DASHBOARD-SCHEMA.md` `domain_scores`. Per-**block** half is N/A |
| F-55 | results-JSON export with a copy button | PORTED-INERT | SOP §4 export shape; CCAR-P Phase 6.1 assumes results-json exists |
| F-56 | `printAll()` full-rationale review | PORTED-INERT | Via the SOP's reference implementation only |
| F-57 | `localStorage` save/resume with three-way routing | PORTED-INERT | Via the SOP's reference implementation only |
| F-58 | JS stem comment block at the top of the file — the dedup seed and audit record | ABSENT-UNDECLARED | Not in the SOP or the CCAR-P prompt. This is the artifact F-02 would read |
| F-59 | Output directory named explicitly | PORTED | `mock-exams/README.md` names the `CCAR-P_MockTest-N_v1.html` convention and reserves the `External` prefix permanently; `EXAM-LOG.md` template carries the path |
| F-60 | Dashboard reading the jsonl | PORTED-INERT | SOP §4 + §7.5; `DASHBOARD-SCHEMA.md` exists. No `DASHBOARD.html` in CCAR-P |

#### Close / self-improvement layer

| # | Foundations mechanism | Class | Justification |
|---|---|---|---|
| F-61 | Generation entry written at generation time with null scores | PORTED (improved) | CCAR-P Phase 5. **Improvement:** it also requires recording "Sections deliberately left untargeted — untargeted recovery is stronger evidence than targeted recovery, and it can only be claimed if the omission was recorded up front." Foundations has no equivalent |
| F-62 | Branch-D double-logging guard | ABSENT-UNDECLARED | Depends on `SESSION-STATE.md` (F-05), which is absent |
| F-63 | Findings ledger with permanent IDs, closed rows retained | PORTED-INERT | SOP §6. No `GENERATION-INTELLIGENCE.md` exists in CCAR-P |
| F-64 | Per-session reconciliation promotion gate — every PROCESS_BUG row FIXED or DEFERRED-with-a-named-reason | ABSENT-UNDECLARED | The SOP mandates the ledger but not the gate. The gate is what stops log-and-forget; PB-21/PB-24/PB-28 are all instances of a condition with no forcing function |
| F-65 | Pending Corpus Decisions gate — never auto-edit a corpus file, route to Ram | ABSENT-UNDECLARED | Partial analogue: `DASHBOARD-SCHEMA.md` rule 4 requires sign-off before re-tagging a shipped score. The unconditional corpus-edit prohibition has no CCAR-P statement |
| F-66 | Session self-verification checklist reported as a table | ABSENT-UNDECLARED | Not present |

#### Tally

| Class | Count | Share |
|---|---|---|
| PORTED | 16 | 24% |
| PORTED-INERT | 15 | 23% |
| ABSENT-DELIBERATE | 2 | 3% |
| ABSENT-UNDECLARED | 31 | 47% |
| N/A | 2 | 3% |
| **Total** | **66** | |

Of the 16 PORTED, six are marked improved over the Foundations original (F-17, F-19, F-20, F-33, F-49,
F-61) and one — F-42 — fixes a Foundations defect that is still OPEN in the Foundations ledger.

### 2.6 Direct verdict on the suspicion

Ram's framing is right in one half and wrong in the other, and the boundary is clean.

**The feedback loop was ported and improved.** All eight mechanisms that turn a sat paper into the next
paper's instruction — `EXAM-LOG.md` authority, attempt chronology, the confirmed-weakness rule, the
Professor's Note, the Insights cadence, timing/pace interpretation, the dashboard schema, and the
generation-entry record — are present, specified in full, and in five cases sharpened. CCAR-P's
Professor's Note requires a retest *direction*; its generation entry requires recording what was
deliberately *not* targeted; its item schema carries an explicit `section` field; and its fidelity gate
already contains the per-question domain-tag check that the Foundations project has open as PB-30.

**The item-fidelity layer was not ported at all.** Take the 20 mechanisms that determine what a
generated question looks like — F-03, F-04, F-24, F-25, F-26, F-27, F-28, F-29, F-30, F-34, F-35, F-38,
F-39, F-40, F-43, F-45, F-46, F-47, F-48, F-58. **Zero are operative.** Two were a recorded decision
(F-26 scenario blocks, F-47 the gate script). Eighteen are missing with nothing written down. Among
those eighteen are the three whose absence produced named, documented Foundations defects: no
correct-answer-letter pre-plan (PB-09 — a block shipped 15 questions at option A), no generic-framing
rule (PB-08 — named fictional companies against a 76-text audit that found zero), and no stem-dedup
ledger of any kind (PB-23 — 20 of 60 stems above 0.30 Jaccard, one at 0.833).

The nuance Ram's framing misses: the ported half is not a copy, and the missing half is not an
oversight of equal weight throughout. Roughly half the missing eighteen are cheap to write (word
budget, letter pre-plan, framing rule, family caps — each a paragraph). The other half needs an
artifact that does not exist yet (a stem ledger, an archetype ledger, a facet-usage tracker), and those
cannot be written before the first paper because they are populated *by* papers. The correct reading is
not "the logic was not carried over" but "the logic that runs on a sat paper was carried over; the logic
that runs on a *drafted* paper was not, and the first paper is where that bill comes due."

### 2.7 Contradictions between files — reported, not resolved

1. **`mock-exams/README.md` vs the filesystem.** The README states "CCAR-P's own corpus
   (`CCAR-P_Domain-N_v1.md` files) **has not been built** — the project is still in Phase 0/1." All seven
   files exist (Domain-1 through Domain-7, 15–39 KB each). The README was written 2026-08-25 09:22; the
   corpus files were created from 18:53 the same day. The README is stale.
2. **`EXAM-LOG.md` vs `CCAR-P_Corpus-Index_v1.md`.** The log's status line reads "Blocked on Phase 0".
   The corpus index reads "Phase 0 reconciliation done 2026-08-25… the corpus now satisfies the
   orchestration prompt's Phase 0 preflight."
3. **`ROADMAP.md` vs `CCAR-P_Corpus-Index_v1.md` — counts.** ROADMAP Phase 2: "77 sections, 77
   scenarios, 154 tagged distractors." Corpus index: "78 sections carrying 79 exam scenarios and 158
   tagged distractors." My own structural count of the seven files gives **78 sections, 79 exam
   scenarios, 79 ✅ options, 158 ❌ options** — the corpus index is right and ROADMAP is stale by the
   §7.8 append of 2026-08-27.
4. **`ROADMAP.md` internal.** Phase 0 states "Nothing else starts until Phase 0 closes" and leaves two
   boxes unticked, while Phase 2 is marked complete and Phase 4's first task ("Port
   `CCA-Orchestration-Prompt_v10.md` → `CCAR-P-Orchestration-Prompt_v1.md`") is unticked despite that
   file existing since 2026-08-25.
5. **Paper count of the reference system.** `CCAR-P-Orchestration-Prompt_v1.md` opening line and
   `ROADMAP.md` both say Foundations generated **fourteen** papers. `EXAM-LOG.md` carries Exam 1
   through Exam 20 and `mock-exams/` holds nineteen paper files (MockTest-2 … MockTest-20) plus a
   retrofit. Both CCAR-P claims are stale.
6. **`sop/SOP_Mock-Exam-Engine_v1.md` §3.3 vs the Foundations method and the CCAR-P corpus shape.**
   The SOP says: "Transcribe items verbatim from the corpus. Never paraphrase, shorten, or invent
   wording — this is a curation task, not an authoring task." The Foundations generator *authored*
   every item from decision tables (its §4.e writes stems, options, and four rationales from scratch),
   and the CCAR-P corpus is built in that same shape — 79 ready-made scenarios for a 63-item paper, not
   a bank of transcribable items. The SOP's rule was extracted from CCDV-F, whose corpus is a chapter
   set. It does not fit CCAR-P's corpus and following it literally would exhaust the corpus on Paper 1.
   This needs Ram's decision; §4.2 assumes the authoring reading.
7. **`CCAR-P/CLAUDE.md` vs `EXAM-FACTS_v1.md` — the engine gate.** `CLAUDE.md` says "Build the engine
   and template with demo items only until `EXAM-FACTS_v1.md` has a real VERIFIED table." That table was
   promoted on 2026-08-25. The gate has cleared and no file says so.

---

## 3. Part B findings

### 3.1 The Professional style profile, measured

**Source:** `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf` §8, pages 6–7, plus the answer key on page 7.
**Sample size: 3 stems, 12 options, 3 rationales.** Every number below is computed from those.

| Dimension | Value |
|---|---|
| Stem word count | 37 / 33 / 29 · min 29, median 33, max 37, mean 33.0 |
| Sentences per stem | 3 / 3 / 2 |
| Option word count | min 5, median 9.5, max 15, mean 9.8 |
| Within-item option spread (max − min) | 3, 6, 4 — every item's four options sit within 6 words of each other |
| Options per item | 4, all three items. Zero multiple-response items are illustrated |
| Point of view | 3/3 third-person indefinite: "A team…", "An application…", "A RAG system…". **Zero** second-person |
| Inline code/config tokens | **0 of 12 options, 0 of 3 stems.** No backticks anywhere in §8 |
| Numbers | 1 of 3 stems ("8,000-token"). Zero percentages |
| Quoted user messages | 0 of 3 |
| Named companies/products/personas | 0 of 3 — uniformly generic, matching the Foundations audit finding |
| Question forms | 2/3 best-approach ("which change best reduces risk?", "Which optimization most directly addresses both?"); 1/3 diagnosis ("What is the most likely first place to investigate?") |
| Rationale length | 41 / 44 / 39 words, mean 41.3 — one sentence justifying the key, then each distractor dismissed by letter in one clause |
| Constraint placement | 3/3 name the deciding constraint **inside the stem**: "Applying least-privilege principles"; "Latency and cost are both concerns"; "while latency and model version are unchanged" |

**Distractor families visible in the published rationales** (this is the extraction `sop/SOP_Mock-Exam-Engine_v1.md`
§3.5 asks for — "the specific families a guide's own samples reject are the strongest available signal
for what that exam actually tests"):

| Family | Instances | Evidence from the guide's own rationale text |
|---|---|---|
| **DETECTIVE-FOR-PREVENTIVE** | S1 A, S1 C (2/12) | "Logging (A) and confirmations (C) are detective/compensating controls, not removal of unnecessary privilege" |
| **EVIDENCE-MISMATCH** | S3 A, C, D (3/12) | "The other options would not be triggered specifically by a document refresh" |
| **LOSSY-SHORTCUT** | S2 A, S2 B (2/12) | "Truncation (A) loses needed policy; downsizing blindly (B) risks quality" |
| **RIGHT-TECHNIQUE-WRONG-MECHANISM** | S2 D (1/12) | "relocating to few-shot (D) does not create a cacheable, reusable prefix" |
| **IRRELEVANT-LEVER** | S1 D (1/12) | "model size (D) is unrelated to authorization scope" |
| — | S1 B, S2 C, S3 B | the three correct answers |

**How much weight this can bear.** Three items cannot support a distribution. What they can support:

- **Upper bounds, yes.** No official Professional stem exceeds 37 words and no option exceeds 15. Those
  are usable as caps because a cap is violated by a single counter-example and none of the three
  approaches it.
- **A median, no.** "Median 33 words" is not a target a generator can be held to on n=3. The Foundations
  median of 51.5 was computed over 76 stems and 304 options and is a genuinely different kind of number.
- **Register and voice, yes.** Third-person indefinite in 3/3, zero inline code in 12/12, and zero
  invented proper nouns in 3/3 are strong signals precisely because they are *absences* — a single
  instance would have broken them, and none appears.
- **Distractor families, yes, as a seed list — no, as weights.** Five families across twelve options is
  a usable taxonomy. "EVIDENCE-MISMATCH is 25% of distractors" is not a usable weight.
- **Multiple-response style, no.** §5 confirms multiple-response items exist. §8 illustrates none. There
  is no official example of what one looks like.

The guide's own framing supports using these as a style reference and no further: §8 says "These
illustrative items show the style and cognitive level of the exam. They are not drawn from the live item
bank," and §7 says "Complete the sample questions in Section 8 to familiarize yourself with item style."

### 3.2 Professional versus Foundations — every dimension that differs

Foundations column from `PRACTICE-TEST-STEMS_v1.md` §3 (n=76 stems / 304 options) and the Foundations
official PDF's 12 samples as cited in `CCA-Orchestration-Prompt_v10.md` Phase 4.a.5.

| Dimension | Foundations | Professional | Size of the difference |
|---|---|---|---|
| Stem length | median 51.5, max 93, mean 53.5; official samples mean ~54 | median 33, max 37, mean 33.0 | **~38% shorter.** The longest Professional stem is shorter than the Foundations median |
| Stem structure | 2–5 sentence paragraph; the question often appears twice (once ending the Situation, once as a bolded restatement) | 2–3 sentences; the question appears once | The Professional item does not restate itself |
| Point of view | 35/76 second-person "You/Your"; 16/76 open on telemetry | 3/3 third-person indefinite | A register change, not a length change |
| Option length | median 16, max 36, mean 15.4 | median 9.5, max 15, mean 9.8 | **~40% shorter.** The longest Professional option is shorter than the Foundations median |
| Option spread within an item | wide — 17 options ≤5 words alongside 4 over 30 | tight — every item within 6 words | Length can be a giveaway on Foundations; on Professional it cannot |
| Inline code/config tokens | 21% of options; 21/76 stems | 0/12 options; 0/3 stems | The token-rate mechanism (F-29) may be **actively wrong** for CCAR-P |
| Evidence density | 41/76 stems carry a number, 19/76 a percentage, 20/76 cite logs/monitoring, 23/76 quote a user | 1/3 carries a number, 0/3 a percentage, 0/3 quote anyone | The Professional stem states a *situation*, not a *telemetry reading* |
| Question form | 67% best-approach, 12% "how should you", 9% diagnosis, 3% placement | 2/3 best-approach, 1/3 diagnosis | Similar mix, smaller sample |
| **What the candidate is asked to do** | pick the change that fixes the observed failure | pick the change that satisfies a **named principle** ("Applying least-privilege principles"), or **two constraints at once** ("Latency and cost are both concerns"), or identify the **first** place to look given what the evidence rules out | The Foundations item asks *what works*. The Professional item asks *what works given a stated governing constraint* |
| **Role of the distractors** | includes fabricated features (a `--batch` flag, `CLAUDE_HEADLESS=true`, `override: true` frontmatter) and over-engineering (preprocessing classifiers, vector DBs, trained models) | **all 9 distractors are real, legitimate techniques.** Logging, confirmation prompts, a larger model, truncation, a smaller model, few-shot blocks, temperature — every one is something a competent architect does somewhere. Wrongness is contextual, never factual | This is the single largest gap. A Foundations distractor can be eliminated by knowing a fact. A Professional distractor can only be eliminated by applying the constraint the stem names |
| **Elimination logic** | root-cause vs symptom; the correct answer "directly addresses the root cause" | the stem **pins variables** so distractors are excluded by evidence: "while latency and model version are unchanged", "Support staff only ever need to read tickets and draft replies" | The exclusions are stated in the stem rather than left to judgement |
| Over-engineering family | 8 of 76 explanations dismiss "infrastructure overkill" | **0 of 12.** No sample distractor is rejected for being too much architecture | The corpus's ARCHITECTED family (20 of 158 distractors) has no support in the official samples |

**What separates a Professional item from a Foundations item with bigger nouns.** Three things, all
observable in the three samples:

1. **The stem names the axis.** A Foundations stem describes a failure and lets the candidate find the
   axis. A Professional stem hands over the axis ("least-privilege", "latency and cost", "unchanged")
   and tests whether the candidate can apply it correctly against options that are all defensible on
   some other axis. Sample 1 is the clearest: without "Applying least-privilege principles", option C
   (a confirmation prompt) is a perfectly good answer.
2. **Every distractor is a real technique in the wrong place.** No fabrication, no straw man. This is
   why the item is harder despite being shorter — you cannot answer it by spotting a flag that does not
   exist.
3. **The stem pins the variables that would otherwise rescue a distractor.** Sample 3 says "latency and
   model version are unchanged", which kills two of the three wrong options before any judgement is
   applied. The remaining work is the *ordering* judgement — what to check **first**.

### 3.3 The two OPEN questions — stance without resolution

Both remain **OPEN** in `EXAM-FACTS_v1.md` and in `CCAR-P_Corpus-Index_v1.md`. Nothing below promotes
either.

#### OPEN 1 — Are the 63 items standalone or grouped into shared-scenario blocks?

**What the guide settles.** §5's item-format line is "Multiple-choice and multiple-response items; each
item states how many responses to select" — the unit named is the *item*. §6 says "The percentages
indicate the approximate proportion of scored **items** drawn from each domain" — the blueprint is
distributed over items, not scenarios. Each of the three §8 samples is fully self-contained: each
carries its own complete situation, and none shares context with another.

**What it does not settle.** The word "scenario" appears in the entire 11-page guide exactly once — on
page 10, inside §13's NDA boilerplate: "all exam content, including questions, answer options, and
scenarios." That is program-wide legal language covering four certifications, not a format statement,
and it is equally consistent with "scenario" meaning "the situation inside an item." The guide neither
confirms nor rules out shared stimuli. Anthropic's certification FAQ language quoted in
`CCAR-P/CLAUDE.md` ("all four exams use scenario-based multiple response questions") has still not been
re-read against this guide's §5, and `EXAM-FACTS_v1.md`'s OPEN row says exactly that.

**Design stance: generate standalone, self-contained items.** Every item carries its own complete
situation and is answerable with no other item on the paper present. The reason is asymmetric cost, not
evidence: a standalone item is a valid item under both hypotheses, while a block-structured paper is
wrong under one of them and burns a fixed share of the paper's 63 items on shared narrative that may
not exist.

**Behaviour if the assumption proves wrong.** What Ram loses is rehearsal of one specific affordance —
carrying a situation across ~15 items and answering later ones faster because the context is already
loaded. Two mitigations, both cheap and neither an assertion:
- **Soft clustering.** Order items so that same-objective items sit adjacent in runs of 3–5. This
  rehearses context-carrying without claiming a structure exists.
- **A dormant schema field.** The item schema keeps `block` and `blockLabel` (Foundations already has
  both) written as `null` on every item. If block structure is later confirmed, papers gain blocks by
  populating two existing fields — no schema migration, no re-tagging of the miss history, and the
  fidelity gate gains checks F-41 and F-44 back unchanged.

**How it would actually get settled.** Only by a direct Partner Academy login re-fetch (already an open
ROADMAP Phase 0 item) confirming the FAQ wording against guide §5, or by a guide version bump. Note
that §13 names "scenarios" as confidential content, so a post-sitting structure note is legally grey —
the score report, which the ROADMAP Phase 6 already plans to log objective-by-objective, is the safe
artifact and it will not answer this question.

#### OPEN 2 — Are multiple-response items scored all-or-nothing or with partial credit?

**What the guide settles.** §5 confirms multiple-response items exist and that "each item states how
many responses to select" — so the count is always given, and a generated item that does not state its
count is wrong regardless of the scoring answer. §9 settles the *exam-level* model: criterion-referenced,
scaled 100–1,000, cut score 720 set by a formal standard-setting study, with percent-correct by domain
reported and explicitly not used for pass/fail.

**What it does not settle.** Item-level partial credit is not mentioned anywhere in the guide. §9's
"percentage of items you answered correctly within each content domain" leans weakly toward binary
item scoring, since a percent-of-items figure reads most naturally over items marked right or wrong —
but a fractional item score could also be aggregated into a percentage, and that inference is too thin
to carry. Do not use it.

**Design stance: score all-or-nothing in the engine, log the raw selection sets, and hold the
multiple-response share at a declared fixed number.** Three parts:
- *All-or-nothing* is the strictly conservative assumption: it can only over-prepare. It matches the
  Foundations precedent that cost eight marks (root `CLAUDE.md` habit 2), and it is already the
  project's standing rule in three places (`ROADMAP.md` standing rule 5, `EXAM-LOG.md` Convention 6,
  `EXAM-FACTS_v1.md` OPEN table).
- *Log the raw sets.* Store `picked: [indexes]` alongside `correct: [indexes]` per item in the
  results-json, not just a boolean. This is the concrete answer to "how the generator behaves if the
  assumption proves wrong": a partial-credit rescore of every paper ever sat becomes a display-time
  function over stored data, computable retroactively with nothing re-sat.
- *Fix the share.* CCAR-P Phase 2.4 currently reads "Match the confirmed single-answer /
  multiple-response ratio" — **there is no confirmed ratio in any file**, so as written that step cannot
  execute. Set it to a declared **8 of 63 (12.7%)**, matching the most recent Foundations paper (Exam 20:
  8 of 60), state the number in every generation entry, and treat it as a one-line correction if the
  ratio is ever confirmed.

**Behaviour if the assumption proves wrong.** If the real exam gives partial credit, Ram's mock scaled
scores read *low* — a safe direction. The unsafe side-effect is that the confirmed-weakness rule
becomes biased against whichever domain carries the most multiple-response items, since an
all-or-nothing miss on a majority-right answer is indistinguishable from a knowledge gap in the domain
tally. Mitigation, already half-built: `DASHBOARD-SCHEMA.md` splits `single_answer` and
`multi_response` as separate `[correct, of]` pairs. Add the rule that **the confirmed-weakness check
runs on single-answer items only**, with the multi-response tally reported beside it. That keeps the
weakness signal clean under either scoring model.

---

## 4. Part C — the CCAR-P generation engine

### 4.0 The constraint that shapes the whole design

Before any mechanism: the CCAR-P corpus is **too small to be transcribed from and exactly the right
size to be authored from**, and the engine has to be built for the second reading.

Measured from the seven files: **78 sections, 79 ready-made exam scenarios, 79 ✅ options, 158 ❌
options.** A 63-item paper with four options each needs 63 correct answers and **189 distractors**. The
corpus holds 158. A single paper drawn one-item-per-scenario would consume 63 of the 79 scenarios —
80% of the corpus — on Paper 1, and Paper 2 would have nothing fresh.

Foundations hit this wall at Exam 8 with 71 sections and spent the remaining twelve papers managing it
(`GENERATION-INTELLIGENCE.md`, "Corpus Section Freshness": "total corpus saturation reached this
session… every future FULL-60 exam's 60 questions will necessarily land entirely on already-Heavy
sections"). CCAR-P saturates at Paper 1 unless the addressable unit is smaller than the section.

**The fix: facets, not sections.** Every corpus section carries a decision table with roughly five
`Situation | Answer | Why` rows, plus a quoted misconception, plus its ready-made scenario. Each of
those rows is an independently testable decision — a *facet*. 78 sections at ~4 usable facets each is
roughly **300 addressable facets**, which supports ten 63-item papers with no facet reused before its
section is exhausted. The ready-made scenario in each section is then reserved for one purpose only:
it is the section's **canonical worked example**, and a generated item must produce a *different*
failure mode from it (Foundations PB-05's instruction, which caught 9 of 15 draft questions in one
block before they reached the coordinator).

Everything below is built on facet-level addressing.

### 4.1 Instruction 10 — the generation logic

#### (a) Domain quota derivation

Published weights × 63 items, rounded:

| Domain | Weight | Exact | Items |
|---|---|---|---|
| D1 Solution Design & Architecture | 17% | 10.71 | **11** |
| D2 Claude Models, Prompting & Context Engineering | 13% | 8.19 | **8** |
| D3 Integration | 19% | 11.97 | **12** |
| D4 Evaluation, Testing & Optimization | 16% | 10.08 | **10** |
| D5 Governance, Safety & Risk Management | 14% | 8.82 | **9** |
| D6 Stakeholder Communication & Lifecycle Management | 14% | 8.82 | **9** |
| D7 Developer Productivity & Operational Enablement | 7% | 4.41 | **4** |
| **Total** | 100% | 63.00 | **63** |

Plain rounding lands exactly on 63; no largest-remainder adjustment is needed. This table does not
currently exist in any project file and should be written into the orchestration prompt so it is not
re-derived per paper.

Confirmed-weakness adjustment stays as CCAR-P Phase 2.2 already defines it (+2–4 to the confirmed
domain, the same subtracted from the strongest, reverted on the following paper), with one addition:
**D7 is floored at 3 and capped at 6.** At 4 items it cannot absorb a −4 without losing objective
coverage (it has 3 objectives), and at 8 it would be over-weighted by 78%.

#### (b) Objective-level coverage — the primary seeding unit

63 items against 38 objectives. Allocate in two passes:

- **Floor pass (38 items).** Every one of the 38 objectives gets exactly one item. This is mechanically
  satisfiable within every domain quota: D1 6 objectives ≤ 11 items, D2 5 ≤ 8, D3 8 ≤ 12, D4 6 ≤ 10,
  D5 5 ≤ 9, D6 5 ≤ 9, D7 3 ≤ 4.
- **Discretionary pass (25 items).** Allocated by the targeting instruction (§4.3), then by facet
  freshness. Per-objective cap of 3 items on any one paper, so no objective can absorb the whole
  discretionary budget.

*Improvement over Foundations, and how I would know it worked:* Foundations seeded on Key Distinctions
and corpus sections and had no objective-level view at all; the CCAR-F score report came back with **six
objectives at 0%**, two of which had been open in the mock corpus for weeks (`CCAR-P/CLAUDE.md`,
"Carry-over weaknesses"). A paper that guarantees one item per objective makes a 0% objective on the
real exam impossible to have gone untested in the mocks. The success measure is direct: after the real
sitting, no objective on the score report should be one the mock series never covered.

**Blocker.** The objective→section map needed for this does not exist in machine-readable form. Only 62
of 78 corpus sections carry an `| Objective |` row in their Core Facts table (D2: 3 of 9; D4: 6 of 12;
D1: 10 of 12), and the strings that are present resolve to **41 distinct values for 38 objectives** —
"Select appropriate architectural patterns" and "Select appropriate architectural patterns (workflow,
agentic, augmented LLM)" are two spellings of one objective. This must be fixed before the floor pass
can run; it is item 2 in the build sequence.

#### (c) Facet freshness and rotation

Maintain `FACET-LEDGER.md` (new). One row per facet: `domain · section · facet-id · facet one-liner ·
papers used · outcome each time · direction tested`.

Rules, in precedence order:
1. No facet appears twice on one paper.
2. No facet is reused until every facet in its section has been used at least once.
3. A facet whose item was **missed** is eligible for immediate reuse — but only from the **opposite
   direction** (`CCAR-P_Domain-Template_v1.md` rule 3: "The `tool_choice` trap on Foundations closed in
   the under-specification direction and immediately reopened in the over-specification direction,
   because only one direction had ever been drilled").
4. A section may contribute at most 2 items to one paper — this is the CCAR-P form of Foundations'
   "max 1 heavy section" rule, loosened because PB-17 proved the strict version unsatisfiable once a
   domain's quota exceeds its section count. D2 (8 items over 9 sections) and D7 (4 over 8) never bind;
   D3 (12 over 14) never binds; D1 (11 over 12) never binds. The rule is a ceiling, not a schedule.

*Carried from Foundations on evidence:* the freshness tracker is why Foundations reached full corpus
coverage by Exam 8 rather than circling five favourite sections. *Changed on evidence:* Foundations
tallied freshness by extracting `whyRight.cite` from the shipped `DATA` JSON (PB-06's standing method,
which exists because prose self-report was drifting). The facet ledger keeps that method — the ledger
is rebuilt from the shipped papers, never from a session's own claim about what it wrote.

#### (d) Single-answer vs multiple-response mix

**55 single-answer + 8 multiple-response (12.7%)**, per §3.3's stance. Rules:
- Every multi-response stem states its count in the stem text ("Select two."), per SOP §2 — "every real
  exam item does this, so every generated one must too", and guide §5 confirms it.
- `selectN` is 2 on all eight for Papers 1–7. Foundations mixed 2 and 3 on Exam 14 and dropped to 2-only
  by Exam 20; there is no evidence for 3 in the CCAR-P guide.
- A multi-response item may only be drawn from a section whose decision table has **≥2 independently
  true rows for the same situation**. Otherwise a 2-of-4 item is a 1-of-4 with a filler, which teaches
  the wrong selection habit.
- Across the eight items, no 2-of-4 correct-pair combination ({A,B}, {A,C}, {A,D}, {B,C}, {B,D}, {C,D})
  appears more than twice. *This is the multi-response analogue of the letter pre-plan, and it exists
  because PB-09's failure mode — position clustering invisible to per-item QA — has no reason to spare
  multi-select items.*

#### (e) Distractor-family variation within an item

Eight families: the corpus's six (OVERSPEC, DISCARD, REPAIR, ARCHITECTED, HALF-MOVE, WRONG-AXIS) plus
two extracted from the official §8 rationales that the corpus does not name —
**EVIDENCE-MISMATCH** (a cause the stated evidence rules out; 3 of 12 official distractors) and
**DETECTIVE-FOR-PREVENTIVE** (a monitoring or confirmation control offered where the requirement is
removal; 2 of 12).

Per-item rule: the three distractors come from three **different** families (CCAR-P Phase 3 already
requires this).

Per-paper caps, which CCAR-P does not currently have:
- No family above **25%** of the paper's 189 distractors (≤47).
- EVIDENCE-MISMATCH ≥ **8%** (≥15 distractors).
- ARCHITECTED ≤ **10%** (≤19).

*Why the caps, with the evidence.* The corpus's own family distribution is skewed and would propagate
into every paper if items were drawn without a cap. Measured across all 158 tagged corpus distractors:
HALF-MOVE **46 (29.1%)**, WRONG-AXIS **36 (22.8%)**, REPAIR **25 (15.8%)**, DISCARD **22 (13.9%)**,
ARCHITECTED **20 (12.7%)**, OVERSPEC **9 (5.7%)**. Two families would supply more than half of every
paper's wrong answers, and Ram would learn the shapes rather than the decisions. Separately, the
ARCHITECTED cap and the EVIDENCE-MISMATCH floor come straight from §3.2: **zero of the nine official
distractors are rejected for being over-architected**, while three of nine are rejected for not
explaining the stated evidence. The corpus over-supplies the family the exam does not use and does not
name the family the exam uses most.

*How I would know the caps worked:* per-paper family capture rates recorded in the miss log. If
ARCHITECTED capture stays high while its share falls, the habit is real and §4.3's habit remedy fires.
If EVIDENCE-MISMATCH capture is high on Papers 1–3, that is a genuine and previously invisible gap.

#### (f) Correct-answer-position planning

Pre-plan the whole 55-item single-answer sequence **before any option text is written**, as a balanced
multiset **{A×14, B×14, C×14, D×13}**, shuffled into a random per-item order, with the short letter
rotating across papers (Paper 1 short D, Paper 2 short C, Paper 3 short B, Paper 4 short A, then repeat).
The correct-answer letter for item *k* is decided here; the drafting step writes the correct option into
that position.

*Carried from Foundations on hard evidence.* This is Phase 4.d.5, added because "one exam block once
shipped all 15 questions at the same option letter, undetected" by its own QA (PB-02/PB-09). The
measured effect is visible in the papers: Exam 2, before the pre-plan, tallied **A20 / B17 / D12 / C11**;
Exam 20, after it, tallied exactly **13 / 13 / 13 / 13**. The prompt is explicit that the post-hoc check
is "a VERIFICATION BACKSTOP… not a substitute for the pre-plan", and CCAR-P currently has neither.

*One change:* the corpus's ready-made scenarios list ✅ first and both ❌ after, in a fixed order. An
authoring agent reading them will drift toward A. The pre-plan is the only defence, and the gate check
(§4.4 check 6) is the proof it held.

#### (g) Near-duplicate and archetype deduplication

Three ledgers, all new, all populated by shipped papers rather than by session self-report:

1. **`STEM-LEDGER.md`** — every stem from every CCAR-P paper, plus the **45 ExternalMock items** (three
   files × 15, which Ram may sit and which `mock-exams/README.md` says stay permanently outside the
   `MockTest-N` sequence), plus the **3 official §8 samples** (which Ram has read). Every new stem is
   Jaccard-compared against all of them. Threshold **0.40** — a stem at or above it is a reskin until
   proven otherwise.
2. **`ARCHETYPE-LEDGER.md`** — one row per `(section, facet, rhetorical shape)` triple. A shape is
   banned within a section after **2 uses**, with two approved re-frames recorded at ban time, in the
   Foundations ban-list's format.
3. **Within-paper lesson check** — no two items on a paper may teach the same lesson, even from
   different sections. This is PB-19 variant (c), "two *different* sections whose content taught the
   same lesson, which a citation tally cannot detect at all", and it is a real risk here: the corpus
   index already records deliberate cross-domain overlap (prompt caching is a full section at D2 §2.8
   and a decision-table row at D3 §3.4), and "lost in the middle" appears in both D2 §2.x and D5 §5.x.

*Carried on evidence.* The Foundations ban-list's own audit of 720 questions found the same teaching
point recurring in the same shape across seven exams while passing a 0.30 wording gate, and found D2
§2.8 missed on four separate sittings because "a wrong mental model was re-tested rather than
re-taught". PB-23 measured the failure directly: a centrally-authored exam shipped 20 of 60 stems above
0.30 Jaccard, one at **0.833**, differing from a prior item by one percentage and one field name.

*Changed from Foundations:* the ledgers are markdown, not a Python gate, until Paper 4. `archetype_gate.py`
was deliberately not ported ("Rebuild only if paper volume justifies it"). That is the right call at
Paper 1 and the wrong call at Paper 4 — see §4.5 step 11.

#### (h) The Professional-tier difficulty floor

Four rejection tests. An item ships only if it passes all four. Each is checkable by reading the item;
none requires judgement about "how it feels."

| Test | Pass condition | Derivation |
|---|---|---|
| **T1 · Constraint sensitivity** | Name one clause in the stem whose deletion or inversion makes a **different** option correct. Record the clause and the option in the item's build note | Validated against all three official samples: delete "Support staff only ever need to read tickets and draft replies" and S1's B becomes wrong; delete "Latency and cost are both concerns" and S2's A or B become defensible; delete "after a document refresh" and S3's B stops being *first*. **All three pass.** A Foundations-tier stem fails, because its correct answer holds regardless of constraints |
| **T2 · Neighbour-correct distractor** | At least one distractor must be an action the **same corpus section's decision table lists as correct in a neighbouring situation** | Directly from §3.2: all nine official distractors are real, legitimate techniques. This test makes that property producible from the corpus rather than left to the author |
| **T3 · No vocabulary answer** | Delete the situation and leave only the question line. If the correct option is still identifiable, reject | Kills the definition question. Every official sample fails identification without its situation |
| **T4 · Production dimension** | The stem carries at least one of: volume/scale, cost, latency budget, a regulator or compliance regime, an SLA, or a named stakeholder who must approve | `CCAR-P_Domain-Template_v1.md`, "Professional-tier specifics": "A Foundations-shaped section that omits all four is likely pitched a tier too low" |

*Why this is a floor and not a style note:* T1 in particular is the mechanical form of the difference
identified in §3.2. It is the only one of the four that a well-written but Foundations-pitched item
reliably fails, and it is cheap to check because the answer is already written down in the corpus
section's own decision table — the row where the *other* option wins.

#### (i) Style targets

| Target | Value | Basis |
|---|---|---|
| Stem hard cap | **45 words** | Official max 37 (n=3), with headroom. Not the Foundations 95 |
| Stem soft band | 28–40 words | The observed 29–37 range, widened by ±3 on n=3 |
| Option hard cap | **20 words** | Official max 15 (n=3), with headroom. Not the Foundations 35 |
| Within-item option spread | ≤ 8 words between longest and shortest | Official max spread 6 |
| Point of view | third-person indefinite; second person permitted on ≤ 15% of stems | 3/3 official are third-person; the Foundations 46% "You/Your" rate has no support here |
| Inline code/config tokens | **≤ 15% of options**, and never in a D1/D5/D6 option | 0/12 official. **This inverts the Foundations mechanism**, which sets a 20–25% *floor*. Applying F-29 unchanged would make every CCAR-P paper less like its own exam |
| Named companies/products/personas | **0** | 3/3 official are generic, matching the Foundations 76-text audit that found zero |
| Rationale length | 35–50 words for `whyRight`; 15–30 per `whyWrong` | Official rationales run 39–44 words covering the key plus all three distractors; CCAR-P splits them per option, so each runs shorter |

*Flagged as the weakest part of this design:* every row above rests on n=3. The caps are safe because a
cap on n=3 is violated by one counter-example and none appeared. The bands are not safe and should be
treated as provisional until either the guide publishes more samples or a paper is sat.

### 4.2 Instruction 11 — evidence for every carried and every new mechanism

**Carried from Foundations, each with the defect it caught or the outcome it produced:**

| Mechanism | Evidence it earned its place |
|---|---|
| Correct-answer-letter pre-plan (§4.1f) | PB-09: a block shipped 15 questions at option A undetected. Measured before/after: Exam 2 A20/B17/D12/C11 → Exam 20 13/13/13/13 |
| Generic framing, threshold 0 (§4.1i) | PB-08: a cold audit of 76 real-exam texts found **zero** named fictional companies; the prompt had been instructing the opposite. Independently confirmed on CCAR-P's own three samples |
| Facet/section freshness ledger (§4.1c) | Foundations reached full 71-section coverage by Exam 8 because of it, and then spent twelve papers managing the overflow the tracker made visible |
| Stem dedup ledger at 0.40 Jaccard (§4.1g) | PB-23: 20 of 60 stems above 0.30, one at 0.833 |
| Archetype/shape ban (§4.1g) | Ban-list §0: D2 §2.8 missed on four sittings because the same shape returned; Exams 7–13 scored 49–55/60 with "an unknown share… template recognition, not knowledge" |
| Within-paper lesson-collision check (§4.1g) | PB-19 variant (c): two different sections teaching the same lesson, undetectable by any citation tally |
| Ground-truth extraction from the shipped artifact, never session self-report (§4.1c, §4.4) | PB-06, and PB-21/PB-24 where seeds were logged in one file and never reached the tracker — one recoverable, one lost forever |
| Attempt-chronology comparison (§4.3) | PB-29: a confirmed-weakness check used the generation-adjacent paper instead of the attempt-adjacent one, in the session that restated the rule |
| Professor's Note as the per-paper setter's brief (§4.3) | The v10 header records it was added specifically to close the "slow to engage" gap — a single detailed result nudging the next paper before the two-exam gate is eligible |
| Practice Mode default, Exam Mode as a fenced exception (§4.3) | SOP §1 / CCDV-F DV-12: a faithful port of the Exam Mode *mechanism* without its *scope* inverted the design stance for every future paper |
| `validateItems()` run in a Node `vm` on the shipped file (§4.4) | SOP §5: "the single highest-value verification step available", and the SOP records the browser preview may not see files written in the current session at all |

**Added, invented, or changed — what each improves and how I would know:**

| Mechanism | What it improves on | How I would know it worked |
|---|---|---|
| **Facet-level addressing** (§4.0) | Section-level freshness saturates at Paper 1 here (78 sections, 63 items). Foundations saturated at Exam 8 and never recovered a freshness signal | The facet ledger still reports unused facets after Paper 5. If it does not, the facet decomposition was too coarse |
| **Objective floor pass** (§4.1b) | Foundations had no objective-level view and the real score report came back with six objectives at 0% | No objective on the real CCAR-P score report is one the mock series never covered |
| **Family caps and floors** (§4.1e) | Foundations had four distractor archetypes living in prose with no enforcement; CCAR-P's corpus is skewed 29% HALF-MOVE / 5.7% OVERSPEC and would propagate that skew | Per-paper family distribution sits inside the caps, and per-family capture rates in the miss log stop being dominated by two families |
| **EVIDENCE-MISMATCH and DETECTIVE-FOR-PREVENTIVE families** (§4.1e) | Extracted from CCAR-P's own official rationales, per SOP §3.5. The corpus names neither, and together they are 5 of 12 official distractors | These two families appear in the miss log at all. On the current corpus they cannot, because no distractor is tagged with them |
| **Inline-token cap replacing the Foundations floor** (§4.1i) | Foundations enforces a 20–25% floor from its own exam's 21% rate. CCAR-P's samples show 0% | Papers stop reading like Claude Code questions. This is the clearest case where copying Foundations would actively reduce fidelity |
| **T1 constraint-sensitivity test** (§4.1h) | Foundations had no difficulty floor at all — its style calibration governed length and register, not cognitive level. "Professional-tier framing" in CCAR-P Phase 3 is prose with no test behind it | Every item has a named clause and a named alternative answer in its build note. An item where the author cannot name one is a Foundations item |
| **Single-answer-only confirmed-weakness check** (§3.3) | Under all-or-nothing scoring, a majority-right multi-response miss is indistinguishable from a domain knowledge gap. Eight Foundations misses were exactly this | The domain weakest on single-answer items and the domain weakest overall stop diverging without explanation |
| **Habit remedy — make the capturing family correct** (§4.3) | Foundations habit 3 ("choosing an option because of how it *sounds*") is unfixable by more testing in the same direction; the ban-list only bans shapes, it never makes a shape the right answer | ARCHITECTED-family capture rate falls across papers **while** accuracy on items where the architected option is correct stays high. If both fall, the remedy taught avoidance instead of discrimination |
| **Phased shape policy across the series** (§4.3) | Foundations banned reskins uniformly from Exam 14 onward — correct for freshness, and it works against the pace advantage Ram names as decisive. Its own audit conceded an unknown share of Exams 7–13's correct answers was template recognition | Mean seconds-per-item falls across Papers 1→7 while accuracy holds. If accuracy falls with the time, recognition was substituting for knowledge |
| **Dormant `block`/`blockLabel` fields** (§3.3) | Makes OPEN 1 reversible at zero cost instead of requiring a schema migration and a re-tag of the miss history | If the guide later confirms blocks, papers gain them by populating two fields |
| **Raw `picked` sets stored per item** (§3.3) | Makes OPEN 2 rescorable retroactively | A partial-credit rescore of every prior paper is computable without re-sitting anything |

**Deliberately not carried, and why** — these exist only because Foundations had them:

- **The 4-of-6 scenario draw and block × domain allocation.** Already ABSENT-DELIBERATE, and correctly:
  it rests on a pool structure the CCAR-P guide never describes.
- **The Key Distinctions seed bank as a separate file.** Foundations needed it because its corpus
  sections were explanatory. CCAR-P's corpus already names a discriminator per section and tags every
  distractor by family — a separate trap file would duplicate the corpus and drift from it, which is
  what CG-02 and PB-21/PB-24 both are.
- **The KD seeding cap (≤15/exam).** PB-22 records that this target became structurally unreachable and
  "needs Ram's decision, not a session-level fix." Do not import an unresolved conflict.
- **The five-branch `SESSION-STATE.md` recovery.** Foundations needed it because generation sessions ran
  long enough to be interrupted mid-paper. Worth adding *if* a CCAR-P generation session is ever
  interrupted — not before.
- **The live running-accuracy pill.** It exists for Practice Mode and is explicitly hidden in Exam Mode.
  Keep it, but note it is a v10 addition with no recorded defect behind it.

### 4.3 Instruction 12 — the post-exam layer

#### What gets logged per miss

One row per missed item in `EXAM-LOG.md`, extending the entry template already in the file:

| Field | Why |
|---|---|
| `q` | position |
| `domain` · `section` · `facet-id` | the addressable unit; a miss with no section reference "cannot become a pattern, and patterns are the entire point" (`EXAM-LOG.md` Convention 5) |
| `objective` | the score-report unit. Six objectives came back at 0% on CCAR-F |
| `format` (single / multi-`selectN`) | Convention 6 — the all-or-nothing leak lives here |
| `picked` (full set) · `correct` (full set) | not a boolean — this is what makes a partial-credit rescore possible (§3.3) |
| `picked_family` | which of the eight families captured him. This is the habit signal |
| `direction` | which side of the section's decision axis the miss fell on. A retest from the same direction proves nothing (CCAR-P Phase 2.3) |
| `seconds` · `paper_mean_seconds` | fast = time pressure, slow = a decision error. On Foundations "every single miss cluster turned out to be considered-and-wrong" (CCAR-P Phase 6.5) |
| `T1_clause` | the constraint clause the item was built around. If the miss came from ignoring that clause, the diagnosis is "did not read the constraint", not "does not know the material" — a different remedy |

#### How misses become the next paper's targeting instruction

Each miss yields a **targeting triple** `(section, facet, direction)`. The Professor's Note ranks them
by evidence strength and the next paper's generation is bound by four rules:

1. Every triple gets **≥1 item** on the next paper, drawn from the **opposite** facet or the opposite
   direction. Same triple, same direction is banned.
2. Triples are satisfied inside the fixed domain quota. The Note never changes quotas — that is the
   confirmed-weakness rule's job, and Foundations' Phase 4.c.5 makes the same separation explicitly.
3. **Untargeted control set.** Every paper leaves at least three previously-missed triples deliberately
   untargeted and records which, because "untargeted recovery is stronger evidence than targeted
   recovery, and it can only be claimed if the omission was recorded up front" (CCAR-P Phase 5 — already
   in the prompt, and better than anything Foundations had).
4. **Habit escalation.** If one distractor family captures ≥3 items across two consecutive papers, it is
   a habit, not a gap. The remedy differs: the next paper places that family's shape as the **correct**
   answer on 2–3 items, so recognising the shape stops being a safe heuristic. This is the only
   mechanism proposed here that directly attacks root `CLAUDE.md` habit 3 — "choosing an option because
   of how it *sounds* — safer, more architected, more thorough — rather than because it matches the
   requirement the scenario actually states."

#### How pattern familiarity is built deliberately

Ram names pattern recognition as one of the two decisive factors, and Foundations built it by accident
then banned it as a defect. Both are wrong. The fix is to make shape-repetition a **phased policy**:

- **Papers 1–3 — build recognition.** Eight canonical item shapes, derived from the official samples and
  the corpus's decision axes: *named-principle application* (S1), *two-constraint optimisation* (S2),
  *post-change diagnosis* (S3), *protocol/mechanism selection*, *retrieval design*, *metric definition*,
  *stakeholder framing*, *configuration scoping*. Each shape appears 6–9 times per paper with entirely
  different content. Within-paper archetype dedup is enforced on `(section, facet)`, **not** on shape.
- **Papers 4–7 — break the reflex.** Same eight shapes, but each appears at least twice with the
  direction inverted (the ban-list's "approved re-frames" method: "make the corpus's own preference the
  distractor and a legitimate composite the answer, or vice versa, so the recalled slogan does not carry
  the item").
- **Papers 8–10 — rehearse under the clock.** Shape and direction randomised, Exam Mode, full 120
  minutes, no per-question feedback.

The measurement that says this is working, and not just producing false mastery: **mean seconds-per-item
falls across Papers 1→7 while accuracy holds or rises.** If accuracy falls as pace rises, recognition is
substituting for knowledge and the ban-list's warning applies.

#### The series, end to end

| Paper | Mode | Targeting | Shape policy | Multi | What changes |
|---|---|---|---|---|---|
| 1 | Practice | none — diagnostic | 8 shapes, content-varied | 8 | Objective floor pass only. Establishes the per-objective baseline |
| 2 | Practice | P1 triples, inverted | same 8 | 8 | First Professor's Note consumed |
| 3 | Practice | P2 triples | same 8 | 8 | **Insights Round 1** after scoring |
| 4 | Practice | P3 triples + first habit check | shapes direction-inverted | 8 | Habit remedy fires if a family qualifies |
| 5 | Practice | rolling triples | direction-inverted | 8 | Confirmed-weakness adjustment first eligible to fire twice in a row |
| 6 | Practice | rolling triples | direction-inverted | 8 | **Insights Round 2** |
| 7 | Practice | **none — deliberate control** | direction-inverted | 8 | The untargeted paper. Recovery here is the real evidence |
| 8 | **Exam** | rolling triples | randomised | 8 | First full-clock dress rehearsal. No per-question feedback |
| 9 | Practice | facets missed ≥1 time across P1–P8 only | randomised | 8 | The remediation paper. **Insights Round 3** |
| 10 | **Exam** | none | randomised | 8 | Final rehearsal, ~2 weeks before the sitting |

Ten papers matches `ROADMAP.md` Phase 4's own target ("Target ≥10 scored papers") and Phase 5's
requirement of two Exam Mode papers before booking.

### 4.4 Instruction 13 — the fidelity gate

Ordered. A paper that has not produced this table has not finished generation and may not be sat.
Checks 1–4 are structural and run first because a structurally broken paper makes every later check
meaningless. Checks 5–9 are fidelity. Checks 10–12 are dedup and difficulty, and run last because their
fixes can reintroduce failures in 5–9.

| # | Check | Pass condition | Failure it prevents |
|---|---|---|---|
| 1 | **`validateItems()` in a Node `vm` on the shipped file** | Exit clean: item count = 63, `g` sequential and unique, every non-correct option has a `whyWrong`, every item has a `whyRight`, every multi-response stem states its count | SOP §5 — "the single highest-value verification step available", and the browser preview may not see files written this session at all. Also PB-15 (manual assembly introduced a transcription defect that re-reading did not catch) and PB-20 (a hardcoded `exam_n` literal survived template substitution) |
| 2 | **Domain quota** | Tallies exactly 11/8/12/10/9/9/4, or the declared weakness-adjusted values | A paper that does not test the published blueprint |
| 3 | **Per-item `domain` tag vs its own citations** | Every item's `domain` matches the domain of every file cited in its `whyRight` and all three `whyWrong` | **PB-30, still OPEN on Foundations.** Exam 20 Q55 is tagged D3 with every citation in D4; the block-level check passed because both were primary domains. Already CCAR-P Phase 4.2 — keep it and keep it early |
| 4 | **Every cited section exists** | Every `§N.M` resolves to a real heading in the file it names | PB-18: a coordinating session cited a section number that did not exist, the assigned author's reasonable correction produced an undetected collision |
| 5 | **Objective coverage** | All 38 objectives have ≥1 item; no objective has >3 | Six objectives at 0% on the real CCAR-F score report, two of which had been open in the mock corpus for weeks |
| 6 | **Correct-answer letter tally** | Single-answer items: no letter below 12 or above 16 across the 55, and the achieved sequence matches the §4.1f pre-plan | PB-09 (15 questions at option A) and PB-02. The pre-plan is the mechanism; this is the proof it held |
| 7 | **Multi-response pair distribution** | No 2-of-4 correct pair appears more than twice across the 8 items; all 8 stems state their count | The same clustering failure as check 6, in the format it would otherwise escape into |
| 8 | **Style budget** | Every stem ≤45 words; every option ≤20 words; within-item option spread ≤8; stem median inside 28–40 | Items drifting to the Foundations register (median 51.5 stems, 36-word options) against an exam whose own samples run 33 and 15 |
| 9 | **Framing and token rate** | 0 invented company/product/persona names, exam-wide. Inline code/config tokens ≤15% of options, none in D1/D5/D6 options | PB-08 (76 real texts, zero named entities) and the §3.1 finding that 0 of 12 official options carry an inline token |
| 10 | **Distractor families** | Three different families per item; no family >25% of the paper's 189 distractors; EVIDENCE-MISMATCH ≥15; ARCHITECTED ≤19 | The corpus's own 29% HALF-MOVE / 5.7% OVERSPEC skew propagating into every paper, and the ARCHITECTED family the official rationales never use |
| 11 | **Dedup** | Every stem <0.40 Jaccard against `STEM-LEDGER.md` (all prior CCAR-P papers + 45 ExternalMock items + 3 official samples). No two items on the paper teach the same lesson. No `(section, facet, shape)` triple used more than twice historically | PB-23 (20 of 60 stems above 0.30, one at 0.833), PB-19(c) (two sections teaching one lesson), ban-list §0 (D2 §2.8 missed four times behind the same shape) |
| 12 | **Professional-tier floor** | Every item passes T1–T4; the T1 clause and its alternative answer are recorded in the build note | An item that would work unchanged on a Foundations paper. Nothing in the Foundations gate tests this — its six checks govern length, register, and balance, never cognitive level |
| 13 | **Targeting satisfied** | Every Professor's Note triple has ≥1 item from the opposite direction; ≥3 triples deliberately untargeted and named | CCAR-P Phase 4.6 already; the untargeted-control half is CCAR-P's own addition and is the only thing that makes recovery evidence trustworthy |

Report all thirteen as a table with computed values, thresholds, and any fix applied. Re-run checks 2,
3, 6, and 10 after **any** fix that swaps or reorders an item — a swapped item carries its own domain,
letter, and family, and can reintroduce exactly what the earlier check cleared. Foundations learned this
in Fidelity check 4's own fix instruction ("re-run check 2 after any swap").

Checks 1, 6, 8, 9, 10, and 11 are mechanisable and should be a script by Paper 4 — see §4.5 step 11.

### 4.5 Instruction 14 — build sequence

Dependency-ordered. State from Part A.

| # | Must exist | State | Notes |
|---|---|---|---|
| 1 | VERIFIED weight table in `EXAM-FACTS_v1.md` | **exists** | Promoted 2026-08-25 with the S3-mirror provenance caveat. The SOP §7.1 gate and `CCAR-P/CLAUDE.md`'s demo-items-only gate have both cleared, and no file records that they have |
| 2 | **Machine-readable objective → section map** | **missing** | The hard blocker for §4.1b. Only 62 of 78 sections carry an `\| Objective \|` row, and the strings present resolve to 41 distinct values for 38 objectives. Needs one canonical objective ID per section, spelling normalised. **Touches corpus files → Ram's sign-off required** |
| 3 | **`FACET-LEDGER.md`** — every section's decision-table rows enumerated as addressable facets | **missing** | The §4.0 constraint. Derivable mechanically from the existing files; no corpus edit needed |
| 4 | Computed domain-quota table written into the orchestration prompt | **missing** | §4.1a. One table |
| 5 | Style targets, family caps, and the T1–T4 floor written into the orchestration prompt | **missing** | §4.1e, §4.1h, §4.1i. Four paragraphs. Note that F-29's Foundations value must be **inverted**, not copied |
| 6 | Correct-answer pre-plan rule + multi-response pair rule | **missing** | §4.1f, §4.1d. Two paragraphs. Highest defect-prevention per line of any item on this list |
| 7 | `STEM-LEDGER.md` seeded with the 45 ExternalMock stems and the 3 official samples | **missing** | Must exist **before** Paper 1, not after — it is the only ledger that can be populated without a paper |
| 8 | `ARCHETYPE-LEDGER.md` with the 8 canonical shapes defined | **missing** | Empty of instances until Paper 1; the shape definitions come first |
| 9 | `GENERATION-INTELLIGENCE.md` (CCAR-P), Session 1 = the engine build | **missing** | Mandated by SOP §6/§7.6. Add the **reconciliation promotion gate** (F-64) the SOP omits — PB-21, PB-24, and PB-28 are all instances of a condition with no forcing function |
| 10 | `CCAR-P_MockTest-TEMPLATE_v1.html` — engine with `EXAM_MODE = false`, `validateItems()`, `selectN`, raw `picked` sets in the export, dormant `block`/`blockLabel` | **partial** | Specified by SOP §2/§7.2, with `CCDV-F_MockTest-TEMPLATE_v1.html` as the reference implementation. Not built for CCAR-P. Ship it with the three official §8 samples as demo content, per SOP §7.2 |
| 11 | `mock-exams/DASHBOARD.html` | **missing** | SOP §4/§7.5. `DASHBOARD-SCHEMA.md` **exists**; `DASHBOARD-DATA.jsonl` **exists** (empty). Domain codes and weights must come from CCAR-P's own `EXAM-FACTS_v1.md`, never a sibling's |
| 12 | Fidelity-gate script covering checks 1, 6, 8, 9, 10, 11 | **missing — and correctly deferred** | ABSENT-DELIBERATE at Paper 1 ("Rebuild only if paper volume justifies it"). Revisit at **Paper 4**: check 11 needs Jaccard against a growing ledger, which is the point where hand-checking stops being reliable |
| 13 | Fix the four stale-status contradictions in §2.7 | **missing** | `mock-exams/README.md` says the corpus does not exist; `EXAM-LOG.md` says "Blocked on Phase 0"; `ROADMAP.md` carries 77/77/154 and "fourteen papers". None blocks generation; all three would mislead the next session |
| 14 | Ram's decision on SOP §3.3 (transcribe vs author) | **missing** | §2.7 item 6. The SOP's transcription rule is exam-agnostic in intent but was extracted from a chapter-shaped corpus. This design assumes authoring. It should be an explicit decision, not an assumption |
| 15 | Paper 1 | **missing** | Everything above is a prerequisite except 11 and 12 |

Items 3–8 are all text, all derivable from files that already exist, and together they close 14 of the
18 undeclared item-fidelity absences. Item 2 is the only one that touches the corpus and therefore the
only one needing sign-off before the rest can proceed.

---

## 5. What I could not determine

| Question | Why the files do not answer it | What would answer it |
|---|---|---|
| Whether the 63 items are standalone or grouped into shared-scenario blocks | The guide uses "scenario" once, in NDA boilerplate, never in §5 or §6. The three samples are self-contained but that is expected of illustrative items either way | A direct Partner Academy login re-fetch confirming the FAQ's "scenario-based" wording against guide §5 — already ROADMAP Phase 0's open item. A guide version bump. Nothing in the current file set |
| Whether multiple-response items score all-or-nothing or with partial credit | §9 describes exam-level scaled scoring only. "Percent-correct by domain" leans weakly toward binary but cannot carry the inference | Anthropic's certification FAQ or a support answer from `certifications-support@anthropic.com`. Not the score report, which reports domain percentages either way |
| The single-answer / multiple-response ratio | Stated nowhere. `CCAR-P-Orchestration-Prompt_v1.md` Phase 2.4 instructs matching "the confirmed" ratio, which does not exist — that step cannot execute as written | Same sources as above |
| Whether the guide's three §8 samples are length-representative or abbreviated for print | §7 and §8 both call them style references, but three items cannot distinguish "the exam is short-stemmed" from "the guide shortened these" | More published samples, or a sat paper. Until then the §4.1i caps are safe and the bands are provisional |
| Whether the exam publishes an out-of-scope topic list | The CCAR-F guide v0.2 carried an Appendix of in-scope technologies that `Exam-Mechanics_v2.md` turned into a hard exclusion list. The CCAR-P guide v1.0 has no equivalent section | A future guide version. Until then a CCAR-P out-of-scope list would have to be derived from the 38 objectives, and a derived list must not be enforced as a hard constraint |
| Whether the corpus's 158 tagged distractors are usable verbatim or are authoring seeds | The corpus files themselves do not say; SOP §3.3 says transcribe, the Foundations method authors, and the CCAR-P corpus is built in the Foundations shape | Ram's decision (build-sequence item 14) |
| Whether the six CCAR-F carry-over 0% objectives map onto CCAR-P objectives | `BACKGROUND-MATERIAL-INDEX_v1.md` lists them; I did not read that file, and the two exams' objective sets are differently worded | Reading `BACKGROUND-MATERIAL-INDEX_v1.md`'s carry-over list against the 38 CCAR-P objectives. This should feed the Paper 1 targeting instruction |
| Whether CCDV-F's `MockTest-TEMPLATE_v1.html` is portable to a 7-domain, 63-item exam without structural change | The SOP says replace only `KEY`, `DOMAIN_NAMES`, `DOMAIN_WEIGHTS`, `SECTIONS`, and landing-card prose. I did not read the template file | Reading `CCDV-F .../mock-exams/CCDV-F_MockTest-TEMPLATE_v1.html`. It exists (85,819 bytes) |
| Whether the Foundations 0.40 Jaccard threshold transfers to shorter Professional stems | Jaccard on a 33-word stem is noisier than on a 51-word stem; the same threshold may fire differently | Calibration against the 45 ExternalMock stems once `STEM-LEDGER.md` exists — measurable before Paper 1 |
| Ram's actual current standing on CCAR-P | `EXAM-LOG.md` records none, correctly — no paper generated, none sat | Nothing. This is the accurate state |
