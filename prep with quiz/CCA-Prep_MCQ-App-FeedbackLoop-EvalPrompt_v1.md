# Cross-Project Evaluation Prompt — Results-JSON Feedback Loop for mcq-practice-app

**Purpose:** Copy-paste the single code block below as the first message in a fresh Claude Code session opened at `C:\Claude Cowork\Projects\mcq-practice-app`. It asks that project's AI to independently evaluate whether the results-JSON diagnosis pattern built and used in `prep with quiz` (this project) is worth adopting there.

**Source of the pattern:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz\mock-exams\CCA-Prep_MockTest-4_v1.html` (results-JSON export) and the academy tracking files it feeds (`academy\PROGRESS.md`, `academy\LEARNER-MODEL.md`) plus this project's own `EXAM-LOG.md` and `DASHBOARD-DATA.jsonl`.

**Target of the evaluation:** `C:\Claude Cowork\Projects\mcq-practice-app` (confirmed by Ram as "learning exam mcq").

**Written:** 2026-07-11

---

```text
I'm evaluating a feature pattern for this project (mcq-practice-app) that was just built and used successfully in a sibling exam-prep project. I want you to independently verify my description against this project's actual current state, then decide — on your own judgment, not mine — whether it's worth adopting here, and if so, how.

═══════════════════════════════════════════════════════════════
BACKGROUND — WHY THIS PROMPT EXISTS
═══════════════════════════════════════════════════════════════

Ram (this project's owner) is preparing for the Claude Certified Architect — Foundations (CCA-F) exam. He runs two parallel, independent prep efforts:

1. **"academy"** — a conversational, AI-professor-led program at `C:\Claude Cowork\Projects\Claude Certified Architect Prep\academy\`. A persistent learner model tracks mastery per concept across ~37 sessions.
2. **"prep with quiz"** — a separate sub-project at `C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz\` that generates full 60-question HTML mock exams grounded in a fixed corpus, with per-option rationales.
3. **THIS project (mcq-practice-app)** — a third, independent tool: a Python CLI that calls Claude Code in headless mode (`claude -p`) to generate a *fresh* MCQ set every run (no static bank), rendered as a self-contained offline HTML file or plain text.

These three are unrelated in code but share the same exam target. This prompt is about porting a *pattern*, not code, from #2 into #3.

═══════════════════════════════════════════════════════════════
THE FEATURE PATTERN — WHAT WAS BUILT AND WHY IT WORKED
═══════════════════════════════════════════════════════════════

The "prep with quiz" HTML mock exams already had interactive scoring (right/wrong feedback, per-question rationale, a results screen with domain breakdown). What they were missing — and what got added in the session this prompt is drawn from — is a **feedback loop back to an AI that can diagnose the result**, not just display it. Three parts:

**Part A — Structured results export from the HTML itself.**
After the last question, alongside the visual results screen, the HTML renders a `<pre>` block containing a JSON object plus a "Copy results JSON" button. Schema (adapt field names to whatever this project's question objects look like):
```json
{
  "attempted_date": "YYYY-MM-DD",
  "total_correct": 45, "total_questions": 60, "total_seconds": 44148,
  "estimated_scaled": 775,
  "domains": {
    "D1": {"correct": 12, "of": 16}, "D2": {"correct": 5, "of": 11}, "...": "..."
  },
  "questions": [
    {"q": 1, "domain": "D1", "selected": "C", "correct": true, "seconds": 43},
    "..."
  ]
}
```
Nothing fancy — just: every question, what was picked, whether it was right, how long it took, rolled up by domain. This is a browser-side, offline JSON blob copied by hand; no server round-trip.

**Part B — A human pastes that JSON back into an AI session, and the AI treats it as a diagnostic input, not just a score.** Concretely, on receiving the JSON, the AI:
1. Computes pass/fail against BOTH a total-score threshold AND per-domain/per-category floors — the total alone is explicitly rejected as sufficient. (In the CCA-F case: total ≥ 720/1000 scaled, AND no domain below 70%, even if the total passes. A domain floor breach forces "NO-GO, remediate this segment" regardless of how good the total looks.) This mattered in practice: today's real result was 45/60 = 775 scaled (a clear pass on the total) but one domain scored 45% — a real, actionable weakness the total completely hid.
2. For every MISSED question, goes back to the **source corpus** (not its own memory) — in this case, the exam's grounding documents — and extracts the actual rationale: what the correct answer was, why, and what specific misconception each wrong answer encodes. This produces a precise, cited diagnosis per miss, not a vague "you got D2 wrong."
3. Maps each miss against a **persistent per-concept mastery ledger** the AI maintains across sessions (a markdown file with rows like "concept | mastery state 🔴/🟡/🟢/✅ | last evidence | note"). Critically, the ledger has an honesty rule: ANY miss on a tracked concept drops its state, even if it was previously marked mastered — no exceptions for "it was just a tricky distractor." This session actually caught and corrected a case where I'd been too lenient about this rule two sessions running, and separately caught a concept that had been marked "mastered" 20 minutes earlier in a warm-up drill, only to be missed in the full mock on a different facet of the same concept — the promotion was real but too narrow, and the ledger now says so honestly instead of hiding it.
4. Where a miss doesn't map to any existing tracked concept, it's logged as a new discovered gap rather than silently dropped or force-fitted into the wrong bucket.
5. Writes all of this back to the persistent tracking files (the ledger, a session-progress log, and the generator project's own exam-log/results file), so the NEXT attempt has full continuity — what's weak, what to re-teach, what to re-test.

**Part C — this is a repeatable loop, not a one-off.** Each scored attempt appends to history; nothing is overwritten. The receiving AI is explicitly instructed to distrust its own or the project's documentation if the live files disagree with it (verify current state, don't trust stale claims) — this mattered because in the source project, a tracking file claimed a resource existed that turned out not to be on disk, and had to be caught and corrected before use.

The net effect: the HTML mock exam stopped being just a "score yourself" tool and became a **diagnostic instrument that feeds a standing, corrected-over-time model of what the learner actually knows** — with a stricter pass bar than a naive percentage, because the whole point is that a good total can hide a real gap.

═══════════════════════════════════════════════════════════════
THIS PROJECT'S ACTUAL CURRENT STATE — VERIFY BEFORE TRUSTING
═══════════════════════════════════════════════════════════════

I read the following directly today (2026-07-11) rather than relying on this project's own docs, because the docs are stale — `HANDOFF.md` still says "Application code written" is unchecked and describes the project as un-built, but real, working source files exist. **Do not trust HANDOFF.md's current-state claims without re-checking the actual files yourself first** — that staleness is itself something worth fixing regardless of what you decide about the feature below.

**What actually exists and works**, per direct inspection of `src/`:
- `mcq_launcher.py` — CLI entry point. Collects 4 config choices (scope, difficulty, session size, format), calls `claude -p` headlessly (with chunking for N>30, code-fence stripping, one retry on malformed JSON, a diagnostic-file fallback on repeated failure), then calls `qa_validator.py` (**not in the original requirements doc — built since, filters/flags implausible questions before rendering**), updates a dedup stems log, and renders output.
- `prompt_builder.py`, `html_renderer.py`, `text_renderer.py`, `templates/session_template.html` (Jinja2, ~31KB, all CSS/JS inline) — all present and non-trivial (not stubs).
- `data/stems_log.txt` — the **only** persistence mechanism that survives across runs. It stores question-stem prefixes purely for dedup, nothing else.
- I grepped `session_template.html` for any results/export/localStorage/JSON-output hook: **none exists.** The button after the last question just says "See Results" — a plain client-side reveal of the in-memory score. Nothing is exported, copyable, or saved. Closing the tab loses everything except the dedup stems.

**What the requirements doc (`Claude Certified Architect Prep\mcq-practice\The Requirements for Anthropic Exam MCQ Prep.md`, v1.1 — read it, it's the source of truth this project's own CLAUDE.md points to) explicitly says about this:**
- Domain weights match the academy/prep-with-quiz projects exactly (D1 27%, D2 18%, D3 20%, D4 20%, D5 15%) — same exam, same target.
- §5.5 already specifies a "Final Summary Page" with domain breakdown and a flagged weakest domain — **but this is computed and shown once, in-browser, and discarded.**
- Explicit **non-goal**, stated twice (PRD.md and the parent requirements doc): *"Track cross-session progress (v2 feature)."* The parent project's `mcq-practice/CLAUDE.md` lists "cross-session progress tracking" under **"v2 features (do not build now, do not foreclose architecturally)."**
- Session files are named `session_YYYYMMDD_HHMMSS_<scope>_<difficulty>_<N>q.<ext>` and are explicitly designed to support a *future* aggregator: *"a v2 summary tool can read all `session_*.html` files in `sessions/` and parse scores from their metadata headers"* — the requirements doc already anticipated needing to get score data back OUT of these files, it just never specified how.
- Hard constraints already on record you must respect in any recommendation: no `ANTHROPIC_API_KEY` / no `anthropic` SDK (Claude Code CLI only), no external CDN/network calls from the HTML (must stay fully offline), no database/SQLite, no new third-party Python packages without explicit approval (currently only `jinja2` + stdlib), never overwrite or delete a session file.

**The structural difference from where this pattern came from, which you need to reason about, not ignore:** the source project has an *ongoing conversational AI session* sitting in the same project the whole time — pasting JSON "back to the AI" means pasting it into the same chat that's been building the learner model all along. This project has no equivalent standing session — it's a CLI tool invoked fresh each run (`python mcq_launcher.py`), and the "AI" (`claude -p`) is invoked once per question-generation call, headless, with no memory between calls except what `prompt_builder.py` explicitly re-injects (currently: curriculum context + last 50 stems). Any adoption of this pattern here has to solve that gap somehow — there is no free "just paste it back to the chat that already knows the history" step waiting for you.

═══════════════════════════════════════════════════════════════
YOUR TASK
═══════════════════════════════════════════════════════════════

1. **Independently re-verify the current-state claims above.** Read the actual files (`src/*.py`, `templates/session_template.html`, `data/`, the requirements doc, `memory/decisions.md`). If anything above is now wrong or has moved on since 2026-07-11, trust what you find, not this prompt.

2. **Decide whether this pattern is worth adopting here — your call, not a mandate.** Consider explicitly:
   - Does a fresh-generation, no-static-bank tool even benefit from a persistent mastery ledger the way a fixed-corpus tool does? (A fixed corpus lets the diagnosing AI cite an exact source section for every miss. This project's questions are generated fresh each run with no saved corpus of *why* each answer is right — that grounding step may not have anything to point back to. Is that a blocker, or does the generation prompt already carry enough of a "why" in the `explanation` field per the question schema in the requirements doc §6.4 to make grounded diagnosis possible anyway?)
   - Does this violate or sit awkwardly against the explicit "cross-session tracking is v2, not now" decision already on record? If you think it's time to revisit that non-goal, say so explicitly and why — don't silently override a recorded decision.
   - What would Part B's "AI receives and diagnoses the JSON" step even look like in a CLI tool with no standing session? Options worth weighing on their merits (don't just pick one because it's listed first): a new `src/results_ingest.py` script the user runs manually with a saved JSON/session file, invoked via another `claude -p` call; a follow-up interactive step bolted onto `mcq_launcher.py` itself; simply exporting the JSON and leaving diagnosis to whatever chat session the user happens to paste it into next (the cheapest option, closest to what the source pattern actually does); or something else entirely that fits this codebase better than any of these.
   - Is the results-JSON export (Part A alone, no diagnosis loop) worth doing independently of Parts B/C? It's the cheapest single piece, requires no architecture decision, stays inside existing constraints (still fully offline, no new dependencies), and is a strict improvement on data currently thrown away — it may be worth separating from the harder question of whether a persistent ledger belongs in this project at all.

3. **If you decide to adopt some or all of it**, propose a concrete design that fits this project's actual stack (Python stdlib + Jinja2, offline HTML, `claude -p` headless, no DB) — don't propose a generic solution requiring a framework or dependency this project has explicitly ruled out.

4. **Log your decision** in `memory/decisions.md`, following this project's own existing format (Decision / Why / Alternatives considered) — that file already has 4 entries in exactly this shape, so match it. Whatever you decide — full adoption, partial (e.g. Part A only), or rejection — the reasoning should be on record the same way this project's other architectural calls already are.

5. **Update `HANDOFF.md` and the roadmap** if your decision changes the current phase's scope, and flag the stale "application code written: unchecked" line while you're in there regardless of what you decide about the main question — that's a real, separate accuracy problem worth fixing either way.

Do not implement anything beyond what's needed to record and act on your decision unless the adoption you choose is small enough (e.g., Part A's export button alone) that designing and building it in the same pass is clearly reasonable. For anything larger, a decision + a concrete design written down is the deliverable — not a full build.
```

---

**How to use:** open a fresh Claude Code session with working directory `C:\Claude Cowork\Projects\mcq-practice-app`, paste the fenced block above (everything between the ` ```text ` markers) as your first message. It is fully self-contained — no reference back to any other conversation is needed.
