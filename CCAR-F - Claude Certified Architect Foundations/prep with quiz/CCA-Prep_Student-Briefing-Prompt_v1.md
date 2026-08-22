# CCA-F Student Briefing — HTML Generation Prompt

**Purpose:** Generates `CCA-Prep_Student-Briefing_v1.html` — a plain, student-facing orientation document for the CCA-F prep project. Rerun this prompt whenever the project state changes (e.g. when the MCQ generator ships, when new mock tests are added, when held-out mocks are expanded).

**Last generated:** 2026-06-27  
**Output file:** `CCA-Prep_Student-Briefing_v1.html` (increment version on each regeneration)

---

## When to rerun this prompt

- The MCQ practice app (`mcq-practice/`) is built and functional → remove the "not yet available" notice in Section 1 and replace it with accurate invocation instructions
- A new mock test is added to `practice/` → update the Mock exams row in the resource table and the Step 4 sequence entry
- The held-out mock banks are expanded (Mock B added) → update Step 5 and the tips accordingly
- The course modules change (new extension added, a module removed) → update the course layer description and Step 1

---

## The Prompt

```
Create a self-contained HTML briefing document for students using the CCA-F exam prep project. Save it as CCA-Prep_Student-Briefing_v1.html.

Before writing anything, do a QA pass: read the actual project contents — the course files in courses/, the practice bank files in practice/, the held-out mocks in practice/held-out-mocks/, the CLAUDE.md, and the mcq-practice/CLAUDE.md — and ground every claim in the document to what actually exists. Do not describe features or files that are not present.

The document is a student-facing orientation. Write it for someone opening this project for the first time who wants to know what they are holding, in what order to use it, and how to get the most out of repeated sessions.

Tone and style:
- No marketing language. No hero banners, no taglines, no puffery.
- Do not describe the project as exceptional, comprehensive, or otherwise inflate it.
- Write in the same register you would use for a staff handbook or a product README — factual, direct, and complete.
- Do not include a large hero section at the top. A plain page header with the document title and one orienting sentence is sufficient.

The document must cover exactly these four topics, in this order:

1. What the student can expect from this project
   - List what actually exists: the course modules (name them), the practice bank (state the question count and domain breakdown), the cross-domain integration checkpoints, the mock test(s), and the held-out mock banks.
   - State the format of each resource (HTML, markdown, etc.) and how it is accessed.
   - If any major planned feature is not yet built, state that plainly. Do not omit it and do not soften it.

2. The best way to derive value — the recommended sequence
   - Prescribe a specific order: course modules → domain practice bank (one domain at a time) → cross-domain checkpoints → warm mock → held-out cold mocks.
   - For each step, say what to do, not just what to open. Include the scoring threshold, what to log in GAPS.md, and when to advance to the next step.
   - State which domain to start with and why.

3. How it improves over multiple runs
   - Be honest: the content is static. The improvement mechanism is student-operated.
   - Explain the three things that drive gains across multiple passes: gap tracking in GAPS.md, spaced repetition (return after a gap of at least one day), and score discipline (the 70% threshold per domain).
   - Explain the correct use of held-out mocks: one-shot only, never for repeated practice.

4. Tips and tricks for maximum value
   - Write 7–8 specific, actionable tips. Each tip should teach something a student would not know from reading the materials cold.
   - Required tip topics: answer-before-scrolling discipline, why scenario and anti-pattern questions matter more, D1 priority, the six exam scenario names and how to use them, when to open EXAM-DIGEST (not at the start), how to use wrong-answer explanations in the mock test, the cross-domain checkpoint approach (cold attempt required), the compliance-in-code pattern.

Visual design:
- Use the same design tokens as the rest of the project: --bg:#faf8f5, --ink:#2b2622, --accent:#c96442, system font stack (no external fonts, no CDN).
- Clean, readable layout with a max-width of 760px.
- Use a resource table for the project layers (Layer / What it is / Format).
- Use a two-column card grid for the "multiple runs" section.
- Use a left-border sequence list (label column + content column) for the recommended order.
- Use a simple arrow-prefixed tip list for the tips section.
- The file must be fully self-contained and work offline. No external script, font, or stylesheet references.
```

---

## MCQ generator provision

When `mcq-practice/` is built and the app is functional, replace the "What is not yet available" notice in Section 1 with the following block (adjust details to match what was actually built):

```
Section 1 replacement — MCQ practice app (add as a fourth row in the resource table):

| MCQ practice app | Generates a fresh set of questions on demand by calling Claude in headless mode. Configure scope (full exam or per domain), difficulty (Anthropic-Grade or Prep Range), session size, and output format at launch. Each run is different — no static bank is reused. | Run python mcq_launcher.py from the mcq-practice/ folder |

And add a Step 3.5 to the sequence (between checkpoints and the warm mock):

Step 3.5 — Run targeted MCQ sessions on weak domains. After the cross-domain checkpoints, use the MCQ app in Per Chapter mode on any domain where you scored below 70% in the practice bank. Run Anthropic-Grade, 15–20 questions. Log new misses in GAPS.md. The stems log prevents question repetition across runs.
```

Update the "multiple runs" section to reflect that the MCQ app adds a genuine freshness mechanism (stems deduplication log) on top of the student-operated mechanisms.

---

## Notes on regeneration

- Increment the version number in the filename on each regeneration (`_v2.html`, `_v3.html`, etc.)
- Do not overwrite the prior version — keep it as a reference
- After regenerating, do a spot-check: open the file in a browser, confirm all four sections are present, confirm no external resource is loaded (check Network tab with DevTools), confirm no feature is described that does not exist in the current project state
