# Sub-project: CCA-F Mock Exam Generator

**Owner:** Ram  
**Location:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz\`  
**Status:** Active

---

## Purpose

Generate HTML-based MCQ mock exams for the Anthropic Claude Certified Architect — Foundations (CCA-F) exam. Each exam is grounded in the corpus files in this folder, tracks results across sessions, and builds an insight layer that improves future exam generation.

---

## Corpus (Source of Truth)

All quiz questions must be grounded in these files. Every question should trace to at least one section.

| File | Covers |
|---|---|
| `CCA-Prep_Exam-Mechanics_v1.md` | Format, scoring, scenarios, out-of-scope |
| `CCA-Prep_Domain-1_v1.md` | D1: Agentic Architecture & Orchestration (27%) |
| `CCA-Prep_Domain-2_v1.md` | D2: Tool Design & MCP Integration (18%) |
| `CCA-Prep_Domain-3_v1.md` | D3: Claude Code Config & Workflows (20%) |
| `CCA-Prep_Domain-4_v1.md` | D4: Prompt Engineering & Structured Output (20%) |
| `CCA-Prep_Domain-5_v1.md` | D5: Context Management & Reliability (15%) |
| `CCA-Prep_Key-Distinctions_v1.md` | 25 high-yield exam traps — always draw from these |

---

## Blueprint: How to Generate a Mock Exam

### Step 1 — Read the deduplication log
Read `EXAM-LOG.md` before writing a single question. The log lists every question stem used in prior exams. No stem may repeat across exams.

### Step 2 — Select question distribution
Per 30-question exam, the domain-weighted quota is:

| Domain | Weight | Questions |
|---|---|---|
| D1 Agentic Architecture | 27% | 8 |
| D2 Tool Design & MCP | 18% | 5–6 |
| D3 Claude Code Config | 20% | 6 |
| D4 Prompt Engineering | 20% | 6 |
| D5 Context Management | 15% | 4–5 |

### Step 3 — Draw from Key Distinctions first
`CCA-Prep_Key-Distinctions_v1.md` contains 25 exam traps. Prioritise these — they are the highest-yield question seeds. Cycle through unused traps across successive exams.

### Step 4 — Write questions to this standard
Each question must:
- Open with a **Situation** (a realistic scenario — log output, user report, architectural decision)
- Offer **exactly 4 options** — one clearly correct, three plausible distractors grounded in common misconceptions
- Include a **Why** explanation citing the corpus section it comes from
- Never contain the answer in the option phrasing (avoid "CORRECT" labels in the options themselves)

### Step 5 — Build the HTML file
Use the **AI Oracle Quiz v2 design system** (reference: `C:\Claude Cowork\Projects\AI Oracle\quizzes\AI-Oracle_Quiz_v2.html`).

Required HTML features:
- Sticky nav bar with exam title and domain progress indicator
- One question card per question (`q-card` layout)
- Per-domain score breakdown in the final results card
- `localStorage` save/resume (key: `cca-mock-N` where N is the exam number)
- A JS comment block at the top listing all question stems used (for deduplication in next exam)

### Step 6 — Name and log the file
- File name: `CCA-Prep_MockTest-N_v1.html` (increment N)
- Immediately update `EXAM-LOG.md` with the new exam entry

---

## EXAM-LOG.md — Persistent Memory Across Exams

`EXAM-LOG.md` is the cross-exam memory. It records:

1. **Questions used** — stem text per exam (deduplication source)
2. **Score results** — domain scores, total score, pass/fail threshold (720)
3. **Gap observations** — which domains Ram got wrong most often
4. **Insights** — patterns surfaced across multiple exam attempts

### Log Entry Format (append after each exam attempt)

```markdown
## Exam N — [Date]

**File:** CCA-Prep_MockTest-N_v1.html
**Attempt date:** YYYY-MM-DD
**Total score (self-reported):** X / 30 correct (estimated scaled: XXX / 1000)
**Pass threshold:** 720 / 1000

### Domain Breakdown
| Domain | Questions | Correct | % |
|---|---|---|---|
| D1 Agentic Architecture | 8 | X | X% |
| D2 Tool Design & MCP | 5 | X | X% |
| D3 Claude Code Config | 6 | X | X% |
| D4 Prompt Engineering | 6 | X | X% |
| D5 Context Management | 5 | X | X% |

### Observations
- Strongest domain: [domain]
- Weakest domain: [domain]
- Specific traps missed: [list question stems]

### Questions Used (for deduplication)
1. [stem 1]
2. [stem 2]
...
```

---

## Insight Generation

After every 3 completed exam attempts, generate a `INSIGHTS-vN.md` report:

- Which domains show a consistent gap (< 70% correct across attempts)
- Which Key Distinctions are repeatedly missed
- Trend: is the score improving, plateauing, or regressing?
- Recommended focus for next study session before the next mock

---

## Operating Rules

- **Read EXAM-LOG.md first** — no exceptions. Generating without it risks question repetition.
- **No out-of-scope topics** — see `CCA-Prep_Exam-Mechanics_v1.md` for the excluded list. Never write questions on fine-tuning, infrastructure deployment, streaming API, or model weights.
- **Every distractor must be a real misconception** — not a clearly wrong option. Real exam distractors are designed to trap people who partially understand the concept.
- **Cite corpus section in Why** — every explanation names which domain file and section the answer comes from.
- **Update EXAM-LOG.md immediately** after each exam is generated or a score is reported — do not defer.
- **Never overwrite prior log entries** — append only.
