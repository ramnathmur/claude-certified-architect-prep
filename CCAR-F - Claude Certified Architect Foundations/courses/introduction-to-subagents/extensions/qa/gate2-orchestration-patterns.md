# GATE 2 — Build Quality & Usability QA Report

**Artifact:** `courses/introduction-to-subagents/extensions/orchestration-patterns.html`
**Reference:** `extensions/source/orchestration-patterns_citations.md`
**Reviewer role:** Independent Senior QA Lead + AI Student (adversarial; did not build this)
**Date:** 2026-06-05
**File size:** 108,511 bytes · 1,212 lines · single self-contained HTML

---

## Verdict summary

| Severity | Count |
|---|---|
| BLOCKER | 0 |
| MAJOR | 0 |
| MINOR | 3 |

No blockers. The artifact is a valid, fully self-contained, dependency-free HTML lesson. All interactive JS logic traces correctly (no off-by-one in quiz scoring, all `data-correct` indices in range, all nav/scroll targets resolve). Cross-links are present and correct. Content depth fully matches the citations file with no dilution.

---

## 1. Build findings

**Self-contained / no external dependencies — PASS.**
- Single `<style>` block (lines 7–177), single inline `<script>` IIFE (lines 1073–1209). No external `<script src>`, no `<link rel=stylesheet>`, no CDN, no remote images, no `@import`, no web-font loads.
- `grep` for `http | src= | @import | url( | cdn | <link | integrity | crossorigin` returns only benign hits:
  - All `url(#…)` are **internal SVG marker references** (e.g. `marker-end="url(#aw1)"`) — same-document fragment refs, not network requests.
  - All `https://` occurrences are **link text/href inside the Sources `<ol>`** (lines 1049–1053) and inline `code` URLs — these are reference citations the learner may click, not resource loads. Acceptable and expected.
- Fonts are system stacks only (`-apple-system, …, sans-serif` and `"SF Mono", ui-monospace, …, monospace`). No remote fonts.
- No `<img>` tags at all — every diagram is **inline SVG** (8 figures).

**SVG validity — PASS.** All 8 `<svg>` blocks are inline, each with `viewBox`, `role="img"`, and an `aria-label`. `<defs>`/`<marker>`/`<style>` scoped per-SVG; marker IDs are unique per diagram (`aw1/aw2`, `ag`, `ac`, `ar`, `ap`, `ao/ao2`, `ae/ae2`, `al`, `am/am2`, `ab/ab2`) and every `marker-end="url(#…)"` resolves to a defined marker in the same SVG. Tags are balanced.

**HTML structure — PASS.** Well-formed doctype, `lang="en"`, viewport meta, charset. Layout = sticky sidebar + main. Closing comments confirm balanced `/wrap`, `/main`, `/layout`.

---

## 2. JS logic trace (by hand)

**MCQ inventory:** 24 `.mcq[data-mcq]` blocks. 11 are standalone inline checks; 13 carry `data-inquiz` (5 in Quiz A, 8 in the Final Check).

**Quiz denominators — PASS (no off-by-one).**
- `updateQuiz()` (lines 1191–1207) computes `total = quiz.querySelectorAll('.mcq[data-inquiz]').length` **scoped to each `.quizblock`** — so Quiz A → 5, Final → 8, computed dynamically, not hardcoded in logic.
- Actual `data-inquiz` counts: Quiz A = 5 (lines 650, 655, 660, 665, 670); Final = 8 (lines 1001, 1006, 1011, 1016, 1021, 1026, 1031, 1036). Matches the hardcoded display seeds `0 / 5` (line 649) and `0 / 8` (line 999).
- Result box only renders when `answered.length === total` (line 1198) — correct gating.
- Percentage bands: `>=75` pass, `>=50` mid, else mid (re-read). For /5: 4/5=80% pass, 3/5=60% mid, 2/5=40% re-read — sane. For /8: 6/8=75% pass, 4/8=50% mid — sane.

**`data-correct` indices — PASS (all in range, all keyed to correct option).**
- Every MCQ has exactly 4 `.opt` buttons (verified: standalone MCQs list 4 buttons each; quiz MCQs pack 4 buttons per line). All 24 `data-correct` values are in `{0,1,2,3}` — in range.
- Spot-checked correctness vs. option text and source: classify-question→idx1 ("who controls the path"); augmented-LLM→idx2 ("retrieval, tools, memory"); gate→idx0; routing→idx3; 90.2% question→idx2; tokens-15×→idx1; multi-agent-poor-fit→idx3 ("share same context + tight dependencies"). All correct against the citations file.

**Scoring flow — PASS.** Click handler (lines 1168–1186): guards re-answer via `answered` flag; disables all opts; marks the correct option `.correct`+✓; marks a wrong pick `.wrong`+✗; shows feedback with Correct/Not-quite prefix + the `.fbmsg` body. For in-quiz MCQs it writes `mcq.dataset.result` and calls `updateQuiz`. Score counts `dataset.result==='1'`. Correct.

**Progress bar / scroll-spy — PASS.**
- Progress bar width = `scrollTop / (scrollHeight - clientHeight) * 100` (lines 1106–1110) — correct denominator, clamped via `height>0`.
- `progPct` = `doneCount / TOTAL_LESSONS * 100`, `TOTAL_LESSONS = lessonEls.length` = 11 `section.lesson` elements — correct denominator.
- Active-nav: finds the last lesson with `offsetTop <= mid`, sets `.active` on `nav a[data-target="lN"]`. TOC builds targets `l1`–`l11` (line 1089) and `final` (line 1097); sections carry ids `l1`–`l11`; `#final` divider exists. All anchor targets resolve.

**Reveals — PASS.** `doReveal` (1152–1157) shows `.ans`, disables button, updates label. 5 reveal blocks present.

**Collapsibles — PASS (accessible).** `toggleCall` toggles `.collapsed` + `aria-expanded`. Init loop (1142–1149) adds `role="button"`, `tabindex="0"`, initial `aria-expanded`, and Enter/Space/Spacebar keydown handlers with `preventDefault`. All callouts start collapsed with chevron rotation styled.

**Mobile menu — PASS.** `toggleNav` toggles sidebar `.open` + scrim + `menubtn` `aria-expanded`. Nav links auto-close the menu on click below 980px (line 1091). Menu button has `aria-label`.

**MCQ `aria-live` — PASS.** Each feedback `.fb` gets `aria-live="polite"` and `role="status"` (line 1164) so screen readers announce correct/incorrect.

---

## 3. Cross-link check — PASS

| Link | Location | Target | Status |
|---|---|---|---|
| ← Back to the base course | sidebar (191), hero crosslink (211), footer (1066) | `../introduction-to-subagents.html` | Target file EXISTS ✓ |
| Extension banner | hero (201–204) | n/a (descriptive) | Present, correctly framed as Beyond-Academy ✓ |
| What's next | nextbox (1061) | `subagents-as-sdk-primitive.html` | File not yet created — **explicitly labelled "file may not exist yet"** (honest forward-link) — MINOR |
| Sources section | (1045–1055) | 5 Anthropic primary sources | Present; matches citations file exactly ✓ |
| Back to top | footer (1066) | `#top` (hero id, line 200) | Resolves ✓ |

All 5 citation URLs in the Sources `<ol>` match the citations file's source list (incl. the research mirror). Inline `description`-as-router and `Agent` tool references are consistent with the citations.

---

## 4. Usability findings (AI-Student lens)

**Strong — a learner can follow it end to end.**
- Clear "why before how" framing in §1 (the workflow-vs-agent line is taught first as the foundational classifier), matching the project's AI-first methodology.
- Reading order is linear and signposted: 4 section dividers (Foundations → Five patterns → Choosing → In production) + Final check. Sidebar TOC mirrors this with section headers, numbered lessons, per-lesson done-ticks, and a live progress %.
- Each pattern is taught by its **fit signal** with a verbatim source definition, a labelled SVG, a "Maps to subagents" bridge, a predict-first reveal, and a quick-check MCQ — consistent, predictable rhythm.
- Quiz feedback is clear: correct option always highlighted green+✓ even on a wrong pick, wrong pick marked red+✗, explanatory `.fbmsg` shown, and a banded result box with actionable guidance ("skim the misses", "worth a re-read").
- VERIFY flags and the point-in-time note are surfaced prominently (hero + case-study), teaching the learner to treat the numbers as dated — good exam hygiene.

**Where a learner might briefly stumble (all MINOR):**
- The "Final knowledge check" sidebar item never shows an active/done state, because the `final` divider is not a `section.lesson` and `seen[]` is only populated for lesson ids. A learner watching the progress ticks may think they "missed" the final section. Cosmetic only — the link still scrolls correctly.
- The "what's next" link points to a not-yet-created file; the inline "file may not exist yet" caveat mitigates confusion but a click still 404s.
- Section-number labels are slightly mixed (lesson tags say "Section 1/2/6/7", "Pattern 1–5", "Case study", "Implementation") vs. the citations file's "Section 8/9/10/11". Internally consistent within the HTML and arguably friendlier, but a learner cross-referencing the source notes will see different section numbers. Non-blocking.

---

## 5. No-dilution check vs. citations file — PASS

Verified the HTML preserves the full depth of `orchestration-patterns_citations.md`:

- **All 5 named patterns** present with verbatim definitions, when-to-use, and source examples: prompt chaining (§l3, incl. gate), routing (§l4, incl. cost/model-routing example), parallelization sectioning+voting (§l5, both variations + guardrails/evals/code-vuln examples), orchestrator-workers (§l6, the "subtasks aren't pre-defined" distinction), evaluator-optimizer (§l7, literary-translation example). ✓
- **Augmented LLM** building block (retrieval/tools/memory) — §l2. ✓
- **Autonomous agent loop** with ground-truth-at-each-step and cost/compounding-error caution — §l8. ✓
- **Decision framework**: verbatim simplicity-first rule, single-call default, escalation guidance, workflow-vs-agent tradeoff, and the synthesized 7-rung ladder — §l9. ✓
- **Case-study numbers — all present and exact:** 90.2% eval improvement; ~4× (agents) and ~15× (multi-agent) token use; 80% variance from token usage (BrowseComp); up to 90% research-time cut; 40% tool-description figure (with VERIFY flag preserved). Effort-scaling heuristics table verbatim ("1 agent with 3-10 tool calls", "2-4 subagents with 10-15 calls each", "more than 10 subagents"). Economic gate (high-value + heavy parallelization + exceeds context window; not for shared-context/tight-dependency tasks) — §l10. ✓
- **Subagent-implementation detail intact** — §l11: what crosses the context boundary (Agent tool prompt string = only channel in; verbatim final message = only channel out; no parent history/results/system prompt), the no-nesting constraint, Workflow-tool graduation for dozens–hundreds of agents, YAML frontmatter example, `AgentDefinition` fields, built-in subagents (Explore/Plan/General-purpose), `/agents` command, scope precedence, and the Task→Agent rename VERIFY note. ✓

No facts beyond the citations were introduced; the two author analogies (railway/taxi) are explicitly labelled "(Author analogy, not a product fact.)". Both VERIFY flags from the source are carried through verbatim.

---

## MINOR findings (consolidated)

1. **Final-check nav item lacks active/done state.** The `#final` divider isn't a `section.lesson`, so scroll-spy never marks its sidebar link active or done. Cosmetic; scrolling works. (Fix: include `#final` in the scroll-spy/seen set.)
2. **"What's next" link targets a non-existent file** (`subagents-as-sdk-primitive.html`). Mitigated by the inline "file may not exist yet" caveat; still 404s on click.
3. **Section-numbering mismatch** between the HTML's friendly labels and the citations file's Section 8–11 numbering. Internally consistent; only matters if a learner cross-references the source notes.

---

## Build trace summary
- External deps: **0** (verified by grep).
- Inline SVGs: **8**, all valid with resolving internal marker refs and aria-labels.
- MCQs: **24**, all 4-option, all `data-correct` in range and correct.
- Quizzes: **2** (5-q Quiz A, 8-q Final) — denominators dynamic and correct, no off-by-one.
- Accessibility: aria-live feedback, keyboard-operable collapsibles, aria-expanded on menu/callouts — all present.
- Cross-links: base-course back-link valid; sources complete; only forward-link is honestly flagged as not-yet-existing.

---

**GATE 2: PASS**
