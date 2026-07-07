# Sub-project: CCA-F Mock Exam Generator

**Owner:** Ram
**Location:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz\`
**Status:** Active
**Blueprint version:** 2.2 | 2026-07-07 (v2.1, v2.0, v1.0 in git history)
**Changelog v2.1→v2.2:** Step 6 now states the output directory explicitly (`mock-exams/`) — closes Open Findings Ledger item PB-07: the directory was never written down anywhere, only followed as an unstated convention (`practice/`, a project-root folder holding unrelated static practice materials), which meant generated exams landed somewhere disconnected from the system that made them and were hard to locate. Exams 2 and 3 were moved from `practice/` to `mock-exams/` accordingly.
**Changelog v2→v2.1:** added a required per-block correct-answer-position self-check to Step 4 — closes Open Findings Ledger item PB-02 (see GENERATION-INTELLIGENCE.md), where a block previously shipped all 15 questions with the correct answer at the same option letter, undetected by its own QA. Part of the session-2 self-improvement mechanism (Open Findings Ledger + Pending Corpus Decisions) that promotes generation-quality findings into binding blueprint/orchestration-prompt rules instead of leaving them as unread prose.
**Changelog v1→v2:** re-grounded on the official Exam Guide PDF; 60-question scenario-block format (matching the real exam) with a 30-question drill option; per-option rationale system (hardened learning feedback — Ram's design decision: this is a learning tool with full per-question feedback, NOT an exam-conditions simulator); passive timing capture; results-JSON export replacing self-reported scores; estimated-flag integrity rules; practice-test dedup ledger.

---

## Purpose

Generate HTML-based MCQ mock exams for the Anthropic Claude Certified Architect — Foundations (CCA-F) exam. Each exam is grounded in the corpus files in this folder, teaches through every single question via per-option rationales, tracks results across sessions, and builds an insight layer that improves future exam generation.

**Design stance (Ram, 2026-07-06):** per-question feedback is deliberate. The tool optimizes learning-per-question, not exam-condition realism. Realism lives in question STYLE, DIFFICULTY, TOPIC COVERAGE, and STRUCTURE — not in withholding feedback.

---

## Corpus (Source of Truth)

All quiz questions must be grounded in these files. Every question must trace to at least one section.

| File | Covers |
|---|---|
| `CCA-Prep_Exam-Mechanics_v2.md` | Format, scoring, official scenario bank (6), answer heuristics, in-scope/out-of-scope lists, style calibration |
| `CCA-Prep_Domain-1_v2.md` | D1: Agentic Architecture & Orchestration (27%) |
| `CCA-Prep_Domain-2_v2.md` | D2: Tool Design & MCP Integration (18%) — incl. built-in tools (§2.9) |
| `CCA-Prep_Domain-3_v2.md` | D3: Claude Code Config & Workflows (20%) — incl. iterative refinement (§3.7) |
| `CCA-Prep_Domain-4_v2.md` | D4: Prompt Engineering & Structured Output (20%) — incl. batch strategies (§4.11) |
| `CCA-Prep_Domain-5_v2.md` | D5: Context Management & Reliability (15%) — incl. confidence calibration (§5.9) |
| `CCA-Prep_Key-Distinctions_v1.md` | 29 high-yield exam traps — always draw from these |
| `CURRENT-DOCS-DELTA_v1.md` | Exam-framing vs current-docs divergences; [CONFLICT-RISK] items must not decide a scored answer against the official framing |
| `PRACTICE-TEST-STEMS_v1.md` | Dedup ledger (never reuse these stems) + style calibration profile |
| `source/CCA-F-Official-Exam-Guide.pdf` (+ `_text.txt`) | Official authority: task statements, scenarios, sample questions |
| `source/guide_en.md` | Community study guide — depth source |

Superseded (do not generate from; kept for history): `CCA-Prep_Domain-*_v1.md`, `CCA-Prep_Exam-Mechanics_v1.md`, `CCA-Prep_Corpus-Index_v1.md`.

---

## Blueprint: How to Generate a Mock Exam

### Step 1 — Read the deduplication ledgers
Read `EXAM-LOG.md` (every stem used in prior mocks) AND `PRACTICE-TEST-STEMS_v1.md` §2 (every community practice-test stem — Ram will take that test himself; the official PDF's 12 samples are drawn from it). No stem from either ledger may be reused or closely paraphrased.

### Step 2 — Choose format and select scenario blocks

**FULL-60 (default):** 60 questions in 4 scenario blocks of ~15, mirroring the real exam. Select 4 of the 6 official scenarios (`CCA-Prep_Exam-Mechanics_v2.md` Scenario Bank) — rotate so all 6 appear across successive exams; state which 4 were drawn. Each block's questions share ONE evolving scenario narrative (same company, same system, progressing situations — not 15 disconnected vignettes).

**DRILL-30 (on request):** 30 standalone questions, no shared blocks. Label the output "Half-Length Drill" — its score is a weaker predictor.

Domain quotas apply ACROSS the whole exam (not per block):

| Domain | Weight | FULL-60 | DRILL-30 |
|---|---|---|---|
| D1 Agentic Architecture | 27% | 16 | 8 |
| D2 Tool Design & MCP | 18% | 11 | 5–6 |
| D3 Claude Code Config | 20% | 12 | 6 |
| D4 Prompt Engineering | 20% | 12 | 6 |
| D5 Context Management | 15% | 9 | 4–5 |

Assign each question a domain tag; verify quota totals before building HTML. Let each block skew toward its scenario's primary domains (per the Scenario Bank) while the exam-level quota holds.

### Step 3 — Seed from Key Distinctions and fresh corpus
Draw from `CCA-Prep_Key-Distinctions_v1.md` first (cycle unused traps across exams, per GENERATION-INTELLIGENCE.md), then fill quota from corpus sections not yet seeded — prioritizing sections marked fresh. Respect `CURRENT-DOCS-DELTA_v1.md`: official exam-guide framing wins wherever a delta is [CONFLICT-RISK].

### Step 4 — Write questions to this standard

Each question must:
- Open with a **Situation** tied to its scenario block's narrative (concrete: log output, metrics like "12% of cases", config snippets, user reports — match the register in `PRACTICE-TEST-STEMS_v1.md` §3 and the official samples)
- Offer **exactly 4 options** — one correct, three distractors that are documented misconceptions (❌ patterns in the corpus), never fabricated flags/parameters, grammatically parallel, no "CORRECT" giveaways
- Carry a **per-option rationale block** (the hardened feedback system):
  - `whyRight` for the correct option — why it is correct, citing corpus file + section (e.g., "D2 §2.9")
  - `whyWrong` for EACH distractor — what misconception it encodes and why it fails here (cite the corpus ❌ pattern where one exists)
  - Writing four rationales is also a quality gate: a distractor whose whyWrong cannot name a real misconception must be replaced before the exam ships
- **Report the correct-answer-index distribution** (count of A/B/C/D) for every scenario block before declaring it done — a required self-check, not an assumed practice. A block whose questions cluster heavily on one letter (e.g., all 15 at option A) must be reshuffled — options only, content and rationales unchanged — before the exam ships. This check is required precisely because it was skipped once and shipped undetected.

### Step 5 — Build the HTML file
Use the **AI Oracle Quiz v2 design system** (reference: `C:\Claude Cowork\Projects\AI Oracle\quizzes\AI-Oracle_Quiz_v2.html`).

Required HTML features:

1. **Landing card** — exam number, date, format (FULL-60 / DRILL-30), the 4 scenarios drawn, prior performance from EXAM-LOG.md (per orchestration prompt rules)
2. **Scenario block headers** (FULL-60) — each block opens with its scenario narrative card; questions within the block reference and evolve it
3. **Sticky nav** — exam title, block progress, question progress
4. **One `q-card` per question** with the four options
5. **Selection-aware feedback panel** — after an option is chosen (choice then locks):
   - Picked RIGHT → green confirm + `whyRight` + a compact "Why the others are wrong" list (all three `whyWrong` entries) — Ram learns the traps even when he dodges them
   - Picked WRONG → red flag + the picked option's `whyWrong` FIRST, then the other two distractors' `whyWrong`, then the correct option highlighted with its `whyRight`
   - Every rationale shows its corpus citation
6. **Passive timing capture** — record per-question elapsed seconds (first render → lock-in) and total elapsed; display an unobtrusive elapsed timer in the nav (no countdown, no pressure); persist in localStorage
7. **Results card** — total, per-domain breakdown, per-block breakdown, estimated scaled score `round((correct/N) × 900 + 100)` with the "approximation — real exam uses psychometric scaling" caveat, pass-line (720) indicator, total time
8. **Results-JSON export** — below the results card, a `<pre>` block + "Copy results JSON" button emitting:
   ```json
   {"exam_n": N, "format": "FULL60", "attempted_date": "YYYY-MM-DD",
    "total_correct": N, "total_questions": 60, "total_seconds": N,
    "domains": {"D1": {"correct": N, "of": 16}, "D2": {"correct": N, "of": 11},
                "D3": {"correct": N, "of": 12}, "D4": {"correct": N, "of": 12},
                "D5": {"correct": N, "of": 9}},
    "blocks": [{"scenario": "...", "correct": N, "of": 15}],
    "questions": [{"q": 1, "domain": "D1", "block": 1, "selected": "B",
                   "correct": true, "seconds": N}]}
   ```
   This JSON is the PRIMARY score-entry input for the orchestration prompt — paste it back in the next session.
9. **`localStorage` save/resume** (key: `cca-mock-N`) — answers, lock states, timing
10. **JS comment block at the top** listing all stems (dedup source for the next exam)

### Step 6 — Name, place, and log the file
- **Directory:** `mock-exams/` (i.e. `prep with quiz/mock-exams/CCA-Prep_MockTest-N_v1.html`) — every generated exam lives here, alongside the system that generates it. Never write to `practice/` (a project-root folder holding unrelated static practice materials — domain question banks, checkpoints — with no connection to this generator).
- File name: `CCA-Prep_MockTest-N_v1.html` (increment N; bump `_vX` only when regenerating the same exam number)
- Immediately update `EXAM-LOG.md` with the skeleton entry

---

## EXAM-LOG.md — Persistent Memory Across Exams

Records per exam: stems used (dedup), scores, domain breakdowns, gap observations, insights rounds.

### Log Entry Format (append after each exam attempt)

```markdown
## Exam N — [Date]

**File:** CCA-Prep_MockTest-N_v1.html
**Format:** FULL60 | DRILL30 | LEGACY30
**Scenarios drawn:** [4 names, FULL60 only]
**Attempt date:** YYYY-MM-DD
**Score source:** results-JSON | self-reported-total (domains estimated)
**Total score:** X / N correct (estimated scaled: XXX / 1000; pass line 720)
**Total time:** MM:SS ([avg s]/question)

### Domain Breakdown
| Domain | Questions | Correct | % | Estimated? |
|---|---|---|---|---|
| D1 Agentic Architecture | 16 | X | X% | no |
| D2 Tool Design & MCP | 11 | X | X% | no |
| D3 Claude Code Config | 12 | X | X% | no |
| D4 Prompt Engineering | 12 | X | X% | no |
| D5 Context Management | 9 | X | X% | no |

### Observations
- Strongest / weakest domain, slowest questions, traps missed (stems)

### Questions Used (for deduplication)
1. [stem 1]
...
```

**Integrity rule:** when only a self-reported total is available, per-domain numbers are proportional estimates — mark `Estimated? yes` on every estimated row and set `Score source: self-reported-total`. Estimated breakdowns are EXCLUDED from confirmed-weakness checks and insights trends (see orchestration prompt Phase 2).

### Professor's Note — per-exam continuity (written every scored exam)

After each scored exam with real per-domain data (results-JSON or a manual breakdown — NOT a total-only report), append a short **Professor's Note — Intent for Exam N+1** block to EXAM-LOG.md, directly under that exam's entry. It is the setter's brief for the next paper: 2–3 misconceptions the wrong answers revealed (named by Key Distinction / corpus §), the weakest domain and whether it is confirmed or merely suspected, one sentence of deliberate next-paper intent, and one thing to watch. It is the mechanism that makes each exam depend on how the student did on the last one.

- It is **learner-centric and append-only** — distinct from `GENERATION-INTELLIGENCE.md`, which is question-centric and overwritten each run.
- It fires on **every** scored exam, not gated to the every-3 insights cadence.
- It states **intent within the fixed domain quota** — it never changes domain weights or breaches the out-of-scope list. The next generation reads it (orchestration prompt Phase 4c.5) and biases WHICH corpus sections it draws from, so a single detailed result nudges the very next paper before the two-exam confirmed-weakness rule is even eligible.

See orchestration prompt v8 Phase 2 f-note (writer) and Phase 4c.5 (reader).

---

## Insight Generation

After every 3 completed exam attempts, generate an insights round (see orchestration prompt Phase 3): domain trends, repeated missed traps, focus recommendation. Only non-estimated domain data feeds trends. (This is the deeper 3-exam trend layer; the per-exam Professor's Note above is its lightweight every-exam complement.)

---

## Operating Rules

- **Read EXAM-LOG.md AND PRACTICE-TEST-STEMS_v1.md first** — no exceptions. Both are dedup ledgers.
- **Generate from v2 corpus files only** — v1 files are superseded history.
- **No out-of-scope topics** — the 16-item exclusion list in `CCA-Prep_Exam-Mechanics_v2.md` is a hard constraint.
- **Every distractor must be a documented misconception** — never fabricate flags, parameters, or behaviors. Real exam distractors trap partial understanding.
- **Every option gets a rationale** — `whyRight` for the key, `whyWrong` for each distractor, all citing corpus file + section.
- **Official framing wins** — on any `CURRENT-DOCS-DELTA_v1.md` [CONFLICT-RISK] item, author per the official Exam Guide; never make the delta itself the scored distinction.
- **Style-match the real exam** — calibrate stems and options against `PRACTICE-TEST-STEMS_v1.md` §3 and the official samples before writing; never copy those stems.
- **Update EXAM-LOG.md immediately** after generating or scoring — append only, never overwrite prior entries.
- **Write a Professor's Note every scored exam** (real per-domain data) and **consume the latest note when generating** — the note biases section choice within the fixed quota, never the quota itself.
- **Invoke via `/cca-exam`** — the folder-scoped slash command loads orchestration prompt v8. Run it from a Claude Code session opened in this `prep with quiz` folder.
