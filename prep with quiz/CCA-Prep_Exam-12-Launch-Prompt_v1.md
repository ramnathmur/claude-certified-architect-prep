# Launch Prompt — Generate CCA-F Mock Exam 12

**Written:** 2026-08-09, at the end of the docs-currency audit session that re-grounded the corpus on Exam Guide v1.0.
**For:** a clean session with no memory of that work. Everything you need is below or cited by path.
**Paste this whole file, or point a session at it and say "follow this."**

---

## 0. Where to work

Open the session **in this folder**:

```
C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz\
```

That is the main checkout on branch `master`. Do **not** work in `.claude/worktrees/*` — those are separate checkouts and are gitignored.

Then invoke the generator:

```
/cca-exam
```

That folder-scoped command loads `CCA-Orchestration-Prompt_v10.md`, which is the real pipeline: dedup ledgers, scenario draw, per-block delegation, the Phase 4.e.6 Fidelity Verification Gate, HTML build, logging. **Follow it as written.** This file does not replace it — it supplies the Exam-12-specific context and the four overrides below, which v10 cannot know about because they postdate it.

If `/cca-exam` does not appear, read `.claude/commands/cca-exam.md` and load the orchestration prompt it names.

---

## 1. Four things that are NOT negotiable

### 1.1 The exam is still 4 options, exactly one correct. Do not build multiple-response items.

You are going to read `CCA-Prep_Exam-Mechanics_v2.md` and its Format table will say:

> **Item format** — Multiple-choice AND multiple-response items; each item states how many responses to select.

That is a true statement about the **real** exam, added on 2026-08-09 from official Exam Guide v1.0. **It is not an instruction to you.** Ram made an explicit, recorded decision the same day: generated exams keep **4 options, exactly one correct answer**, every question. Reasons, so you don't relitigate them:

- The v1.0 guide says "multiple-response" **exactly once**, never elaborates, and gives no worked example.
- All **12 official sample questions** in that same guide are single-answer, 4-option.
- This project's whole feedback system — one `whyRight` plus three `whyWrong`, each naming a documented misconception — and the HTML scorer both assume single-answer.

Rebuilding both on one unelaborated sentence is a bad trade. The decision is recorded in `GENERATION-INTELLIGENCE.md` → Pending Corpus Decisions. **Revisit only if** a future guide revision elaborates the format, an official sample demonstrates one, or Ram reports meeting one in a real sitting. Otherwise: single-answer, no exceptions, and do not add a "select all that apply" item as a nod to realism.

### 1.2 Exam 12 uses an ADJUSTED domain quota. It is not the standard 16/11/12/12/9.

D2 is **CONFIRMED weak** — unambiguously weakest in the two most recent scored exams by attempt chronology (Exam 10 at 81.8%, Exam 9 at 63.6%). That fires the orchestration-prompt v10 Phase 4c confirmed-weakness adjustment. Because the confirmed domain is D2 itself, the D2-collision rule applies (+4 D2, −2 D5, −2 D1 — D2 cannot donate to itself):

| Domain | Standard FULL-60 | **Exam 12** | Δ |
|---|---|---|---|
| D1 Agentic Architecture & Orchestration | 16 | **14** | −2 |
| D2 Tool Design & MCP Integration | 11 | **15** | +4 |
| D3 Claude Code Configuration & Workflows | 12 | **12** | — |
| D4 Prompt Engineering & Structured Output | 12 | **12** | — |
| D5 Context Management & Reliability | 9 | **7** | −2 |
| **Total** | 60 | **60** | |

This is the most lopsided quota since Exam 6 and it changes the block×domain allocation math materially. **Verify the total is 60 before you write a single question.** Source: Professor's Note — Intent for Exam 12, at the top of `EXAM-LOG.md`.

### 1.3 Numbering is Exam 12, not Exam 10 or 11 — both already exist

Exams 10 and 11 were generated before Exam 9's score arrived (Exam 9 sat unattempted for three weeks). The score re-arms targeting at the first *ungenerated* paper, which is 12. Output file: `mock-exams/CCA-Prep_MockTest-12_v1.html`. Confirm that name is free before writing.

### 1.4 Official framing beats current docs, and D1's trap just got sharper

`CURRENT-DOCS-DELTA_v1.md` (now v1.1) marks divergences `[SAFE]` or `[CONFLICT-RISK]`. On any `[CONFLICT-RISK]` item, **author to the official Exam Guide**, and never make the divergence itself the scored distinction. Two updated on 2026-08-09:

- **D1 `allowed-tools` — escalated.** The guide's task 3.2 says `allowed-tools` **restricts** tool access. Live docs now *explicitly negate* that ("It does not restrict which tools are available: every tool remains callable"); `disallowed-tools` is the restricting key. **Write to the guide's framing.** This is the highest-value trap in the corpus.
- **D7 `tool_choice` — caveat resolved, prohibition unchanged.** `{"type":"none"}` *is* now documented. Still do not build a scored question on it — but the reason has changed. It is no longer "it may not exist"; it is "the guide's task 2.3 names only auto / any / forced, so `none` is outside the tested set."

---

## 2. What changed since Exam 11 was generated

A docs-currency audit on 2026-08-09 found Anthropic had **republished the exam guide as v1.0** (Effective July 2026, exam code **CCAR-F**), superseding the cached v0.2 everything was built from. The new PDF was created 2026-07-08, two days after the original download, and went unnoticed for a month because prior re-verification only re-read live docs, never re-downloaded the guide.

**The reassuring half — measured, not assumed.** A word-level diff of v0.2 → v1.0 found:

- domain weights (27/18/20/20/15) — identical
- all 6 scenarios and their primary-domain mappings — **100.0% word-for-word identical**
- all 30 task statements, titles and knowledge/skills bullets — **0 differences**
- in-scope list and the 16-item out-of-scope list — identical
- the 12 sample questions — content identical, only `A)` → `A.` formatting

**So: no domain corpus file changed, no exam is retroactively wrong, and every dedup/saturation/Key-Distinction state from Exam 11 still holds.** Anthropic's own changelog calls v1.0 "formatting and layout updates," which undersells three exam-mechanics facts, but none of them touch what a question tests.

Current authoritative source, top of the precedence chain:

```
source/CCA-F-Official-Exam-Guide_v1.0.pdf   (+ _v1.0_text.txt mirror)
```

`source/CCA-F-Official-Exam-Guide.pdf` is the retained v0.2 snapshot Exams 1–11 were authored against. `source/guide_en.md` remains a community depth/style source and is **never** authoritative.

File versions you will be reading: `CCA-Prep_Exam-Mechanics_v2.md` **v2.1**, `CCA-Prep_Corpus-Index_v2.md` **v2.1**, `CURRENT-DOCS-DELTA_v1.md` **v1.1**. Next docs re-verification is due **2026-09-08** — if you are generating after that date, re-run the currency check first, and re-download the guide PDF itself, not just the docs.

---

## 3. The single biggest risk in this exam: D2 has 15 questions and only 9 sections

This is the thing most likely to go wrong. Do the arithmetic before dispatching anything.

| Domain | Corpus sections | Exam 12 quota | Pressure |
|---|---|---|---|
| D1 | 18 | 14 | comfortable |
| **D2** | **9** | **15** | **6 forced repeats** |
| D3 | 12 | 12 | exactly 1:1 |
| D4 | 20 | 12 | comfortable |
| D5 | 14 | 7 | comfortable |

*(Section counts are from `CCA-Prep_Corpus-Index_v2.md`; verify against the actual domain files.)*

Cover all 9 D2 sections once and you still have **6 questions to place**, into a corpus already at full saturation. That is precisely the failure family logged as **PB-19**, which has now recurred in **four distinct variants** across Exams 7, 8, 9 and 11 — most recently in a form the preventive pattern did not anticipate: pre-declared facet fences ("use a different tool") were *satisfied* while the underlying **lesson** stayed identical.

**What to do, concretely:**

1. Before dispatch, **read the actual section text** for every D2 section you plan to use more than once — not its citation, the content — and confirm it genuinely supports two *distinct teachable lessons*. A different tool name in a different scenario is **not** a different lesson.
2. **§2.8 gets exactly one question.** Exam 11 established it is roughly four lines carrying a single lesson, with no second facet. It is also where the Professor's Note wants a dedicated, unambiguous test (see §4), so spend that one question well and put your repeats elsewhere.
3. Prefer the larger D2 sections for the doubles. If a section will not carry a genuine second lesson, do not force it — move the repeat.
4. After assembly, re-verify by reading the **full question texts** of every repeated-section pair side by side. A citation tally cannot detect the Exam 9 variant, where two *different* sections taught the same lesson.

---

## 4. What the Professor's Note asks for

Read it in full at the top of `EXAM-LOG.md` ("Professor's Note — Intent for Exam 12"). In brief:

- **The D2 gap is breadth, not depth** — four different sections missed (§2.3, §2.6, §2.8, §2.9). Spread the enlarged 15 across all 9 sections rather than drilling one.
- **Guarantee coverage** of those four missed sections.
- **§2.8's composite-tool-over-prompt-bundling misconception** has now been missed in three consecutive scored exams (8, 10, 9). Give it one dedicated, unambiguous test.
- **Re-test KD#27** (Edit vs Read+Write fallback) once more — correct on its Exam 6 debut, missed on its Exam 9 second appearance. Is that a one-off or a real reversal?
- **Watch:** does D2 recover with the bigger quota, or does the 100% → 90.9% → 81.8% → 63.6% slide continue even with more attention? The latter would mean a real deepening gap, not small-sample section luck.

Section-bias operates **within** the fixed quota. It never changes the quota and never breaches the out-of-scope list.

---

## 5. Scenario draw

Counts after Exam 11, computed from every `Scenarios drawn:` line in `EXAM-LOG.md` (10 exams × 4 = 40 slots, verified):

| Scenario | Times used | Primary domains |
|---|---|---|
| Code Generation with Claude Code | **6** | D3, D5 |
| Multi-Agent Research System | **6** | D1, D2, D5 |
| Claude Code for Continuous Integration | 7 | D3, D4 |
| Customer Support Resolution Agent | 7 | D1, D2, D5 |
| Developer Productivity with Claude | 7 | D2, D3, D1 |
| Structured Data Extraction | 7 | D4, D5 |

Rotation favours the two at 6. Two hard constraints on top of that:

- **D4 feasibility (learned the hard way in Exam 4):** D4 is a primary domain in only **Claude Code for Continuous Integration** and **Structured Data Extraction**. D4 still carries 12 questions, and every domain must be primary-dominant in at least one block it appears in. **The draw must include at least one of those two.** An ILP check across all 15 possible 4-of-6 draws found exactly one infeasible combination, and it is the one naive least-used rotation would pick.
- **D2 needs somewhere to live.** With 15 questions, weight the draw toward D2-primary scenarios — Customer Support, Multi-Agent Research, Developer Productivity.

Derive the final four yourself per the orchestration prompt, then state which four you drew and why. Keep the landing-card disclosure that the draw is curated for coverage, whereas the real exam draws 4 of 6 at random with no such guarantee.

---

## 6. Standing process items (not yet codified — apply as practice)

Five findings are logged in `GENERATION-INTELLIGENCE.md` as candidates for a future orchestration-prompt **v11**. None is binding yet; all are live guidance. **If this run produces further findings needing a prompt edit, fold them into that same future v11 — do not create a v10.5.**

- **PB-19** *(highest priority — regressed in Exam 11 after two clean exams)* — cross-block facet collision. See §3 above; it is the dominant risk this exam.
- **PB-21** *(second)* — the Key Distinctions tracker silently lost Exam 9's three KD seeds for three weeks, so a "zero weak rows" claim was wrong the whole time. **Before finalising this file's session rewrite, check every EXAM-LOG entry's "Key Distinction budget" line and confirm each named KD appears in the tracker with that exam listed — an unscored seed shows `Exam N (QX) — pending`, never absent.**
- **PB-17** — overflow-spreading rule.
- **PB-18** — section-assignment verification.
- **PB-20** — after any template-substitution HTML build, grep the whole file for bare occurrences of the *previous* exam's number, not just the `"Mock Test N"` text. Exam 10 shipped a hardcoded `exam_n:9` in its results-export function that the `DATA`-object substitution missed.

Also worth knowing: **serial block dispatch** (write each block's JSON to disk before dispatching the next) proved its worth in Exam 10 when a usage limit interrupted generation mid-Block-2 and zero completed work was lost. Use it if usage headroom is tight.

---

## 7. Definition of done

- [ ] `mock-exams/CCA-Prep_MockTest-12_v1.html` exists, 60 questions, 4 scenario blocks of 15
- [ ] Every question has exactly 4 options, exactly one correct — **no multiple-response items**
- [ ] Exam-wide domain tally is exactly **D1 14 / D2 15 / D3 12 / D4 12 / D5 7**
- [ ] All six Phase 4.e.6 Fidelity Verification Gate checks computed and reported (not asserted)
- [ ] Correct-answer letters pre-planned per block and verified against the pre-plan after drafting
- [ ] Every repeated corpus section verified for genuinely distinct lessons by reading full question texts side by side
- [ ] Zero stems reused or closely paraphrased from `EXAM-LOG.md` (11 exams) or `PRACTICE-TEST-STEMS_v1.md` (76 stems)
- [ ] Every option carries a rationale citing corpus file + section
- [ ] `EXAM-LOG.md` skeleton entry appended; `DASHBOARD-DATA.jsonl` skeleton row appended
- [ ] `GENERATION-INTELLIGENCE.md` rewritten, including the PB-21 KD-tracker reconciliation
- [ ] Ram told which 4 scenarios were drawn and why

---

## 8. Git state as of writing

Branch `master`, working tree clean. `6eb1301` (the audit merge) is pushed. Six later commits — gitignore hygiene, orchestration v10 + Key-Distinctions #26–29, Exams 5–11 and their scores, Exam 10/11 intermediates, `Outputs/`, and the academy/roadmap refresh — were **not yet pushed** when this file was written. Check `git -C "<repo>" status` and `git log origin/master..master` before assuming.

**The repo is public** (`github.com/ramnathmur/claude-certified-architect-prep`). Exam 12's questions, answer keys and rationales become publicly readable if pushed. Ram has accepted that for prior exams; do not push without asking.
