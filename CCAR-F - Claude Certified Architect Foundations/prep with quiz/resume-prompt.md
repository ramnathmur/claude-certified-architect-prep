# Resume Prompt — CCA-F MCQ system: exam-realism upgrade + feedback loop
_Generated: 2026-07-06 • Working dir: C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz\ (work committed to master)_

## Context
The CCA-F mock-exam generator was upgraded end to end so its MCQs match the real Claude Certified Architect — Foundations exam, and so each exam learns from the last. Two independent cold-agent audits drove the work: one found the corpus covered only 19/30 official task statements (now remediated to full), the other found the learner-feedback loop had never closed (now built out). All work is committed to `master` in the main checkout; this worktree branch was only a workspace.

## What's done
- **Corpus grounded in the OFFICIAL Exam Guide PDF** (downloaded to `source/CCA-F-Official-Exam-Guide.pdf` + text mirror). The old `guide_en.MD` was a community guide, not official. All 5 domain files upgraded to **v2** (closed 3 missing task statements + 8 partials), Exam-Mechanics v2 (official 60Q/120min/4-of-6 scenarios), Corpus-Index v2, a 76-stem practice-test dedup ledger, and CURRENT-DOCS-DELTA v1.
- **Blueprint v2 + Orchestration v6.** FULL-60 scenario-block format; per-option rationales (whyRight + 3 whyWrong, cited); results-JSON export; passive timing; estimated-data integrity rules.
- **Mock Test 2 generated & QA'd** → `mock-exams/CCA-Prep_MockTest-2_v1.html` (60 Q, exact domain quota 16/11/12/12/9, verified in-browser). QA dedup gate caught 4 near-clones of the practice test and replaced them.
- **Feedback loop built (v6):** "Professor's Note for Next Paper" (Phase 2 f-note writes it every scored exam; Phase 4c.5 reads it to bias section choice within the fixed quota). Learner signal mirrors into GENERATION-INTELLIGENCE.md.
- **Invocation:** `/cca-exam` folder-scoped slash command loads v6.

## What's open
- **The loop has never closed once** — no exam scored yet. This is the single highest-value next action (see below).
- **`/cca-exam` not yet verified in a live menu** — created in a non-interactive session; needs confirmation it registers.
- **Background task in flight:** "Add built-in-tool Key Distinctions" (task_72abe6fe) is editing `CCA-Prep_Key-Distinctions_v1.md` in a SEPARATE session (shows as uncommitted ` M`). Do not touch/commit it here; fold it in once that session finishes.
- **DEFERRED-DECISIONS.md** holds 3 deferred items (difficulty calibration, hard-timed mode, spaced repetition) with reopen triggers.

## Next action (do this first)
Have Ram **take a mock exam** (`prep with quiz/mock-exams/CCA-Prep_MockTest-2_v1.html` or `-3_v1.html` — open in a browser), click **"Copy results JSON"** on the final screen, then open a Claude Code session **in the `prep with quiz` folder** and run **`/cca-exam`**, pasting the JSON when it asks. This closes the feedback loop for the first time and triggers the first Professor's Note. If `/cca-exam` doesn't appear, run `/reload` or restart Claude Code (the command file is `prep with quiz/.claude/commands/cca-exam.md`).

## Decisions locked in
- **Learning tool, not exam simulator:** per-question feedback is deliberate and hardened (per-option rationales); realism lives in style/coverage/structure/difficulty, not in withholding feedback. (Ram's explicit call.)
- **Official Exam Guide PDF is the authority**; community `guide_en.md` is a depth source only. Where they conflict, official framing wins for question authoring (see CURRENT-DOCS-DELTA [CONFLICT-RISK] items).
- **Feedback = attention, not obsession:** weak areas get extra attention via WHICH sections are tested (Professor's Note) and a bounded +4 confirmed-weakness delta — never by collapsing the paper onto the weak domain. Domain quota stays fixed.
- **Professor's Note fires every scored exam; Insights round stays every-3** as the deeper trend layer.
- v-prev files (Domain *_v1, Exam-Mechanics_v1, orchestration v1–v5) preserved as history; generate from v2 corpus + v6 orchestration only.

## Files touched this session (all committed to master)
- `prep with quiz/source/` (official PDF + text + community guide)
- `prep with quiz/CCA-Prep_Domain-1_v2.md` … `Domain-5_v2.md`, `Exam-Mechanics_v2.md`, `Corpus-Index_v2.md`
- `prep with quiz/PRACTICE-TEST-STEMS_v1.md`, `CURRENT-DOCS-DELTA_v1.md`, `DEFERRED-DECISIONS.md`
- `prep with quiz/CLAUDE.md` (blueprint v2), `CCA-Orchestration-Prompt_v6.md`
- `prep with quiz/.claude/commands/cca-exam.md`
- `prep with quiz/EXAM-LOG.md`, `DASHBOARD-DATA.jsonl`, `GENERATION-INTELLIGENCE.md`, `SESSION-STATE.md`
- `prep with quiz/MCQ-Quiz-Builder_Blueprint_v3.md` (scope header only)
- `prep with quiz/mock-exams/CCA-Prep_MockTest-2_v1.html`, `-3_v1.html`

## Gotchas / watch-outs
- **Run sessions from `prep with quiz/`** — the orchestration prompt uses relative paths (`EXAM-LOG.md`, `mock-exams/`) and the slash command lives there. Launching from the project root won't resolve them.
- **Never reuse the 76 practice-test stems** (`PRACTICE-TEST-STEMS_v1.md` §2) — Ram will take that test himself. The v6 self-verification checks this; the QA dedup gate (Jaccard >0.42) already caught 4 misses once.
- The uncommitted `academy/*` and `courses/*` changes are from OTHER sessions, not this one — leave them.

## Git state
_Branch: master (main checkout). This session's work = 6 commits, all landed._
Recent commits (newest first):
- `70bb3aa` Add Professor's Note continuity + /cca-exam command (orchestration v6)
- `cb7a8d0` Phase 4: generate & QA Mock Test 2 (FULL-60, per-option rationales)
- `31a738a` Phase 3: hygiene — scope Quiz-Builder out of CCA pipeline, record deferrals
- `e5dd37e` Phase 2: orchestration prompt v5
- `56c1236` Phase 1: blueprint v2 — per-option rationales, scenario blocks, results JSON
- `dd5c6f3` Phase 0: remediate CCA-F corpus against official exam guide

Uncommitted in main checkout (NOT this session's work — do not commit):
- ` M academy/LEARNER-MODEL.md`, ` M academy/PROGRESS.md` — other sessions
- ` M prep with quiz/CCA-Prep_Key-Distinctions_v1.md` — the in-flight built-in-tool-KD background task (task_72abe6fe)
- `?? courses/introduction-to-subagents/extensions/em_dash_report.txt` — other session
- `resume-prompt.md` (this file) is untracked in `prep with quiz/` — intentional handoff artifact.

No version-bump files (package.json / pyproject.toml / VERSION) in this project — n/a.
