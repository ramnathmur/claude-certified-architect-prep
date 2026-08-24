# Exam Mode — Design Spec v1

**Status:** Approved by Ram 2026-08-16, implemented same day on Test 19
**Scope:** Temporary variant for the final pre-exam sittings only (Test 19 now, Test 20 when generated). Does NOT change the blueprint's default design stance ("per-question feedback is deliberate" — `CLAUDE.md`), which remains the default for every exam after the 2026-08-18 sitting.
**Trigger:** Ram's real CCA-F exam is Tuesday 2026-08-18. Every mock exam through Exam 19 reveals correctness + full rationale immediately on selecting an option — useful for learning, but the opposite of exam conditions for a final dress rehearsal.

---

## 1. Problem

Test 19 (and every prior mock exam) is built on the AI Oracle Quiz v2 design system, whose `pick()` → `commit()` flow does three things the instant you click an option:
1. Locks the option (`if(g in state.answers) return;` blocks further clicks)
2. Paints it green/red via `paintAnswered()`
3. Renders a full rationale panel via `renderFeedback()`

This is correct for the project's stated learning-per-question design, but for a dress-rehearsal sitting two days before the real exam, it removes any test of whether Ram can hold uncertainty across a full 60-question block without being told the answer as he goes.

## 2. Interaction model changes

Add `const EXAM_MODE = true;` near the top of the script, alongside `const KEY`.

**Single-answer items — `pick(g,i)`:**
- Remove the lock guard for exam mode: `if(!EXAM_MODE && g in state.answers) return;`
- Every click calls `commit(q,i)` exactly as today (writes `state.answers[q.g]=i`, records timing, re-renders via `renderPage`) — no new commit path needed, since single-answer selection is already a complete, replaceable action.

**Multiple-response items — same `pick(g,i)` toggle mechanic:**
- Toggle logic in `state.pending[g]` is unchanged.
- `commit(q,arr)` fires once exactly `selectN` are chosen, exactly as today.
- New: when a further click drops the pending set back under `selectN` in exam mode, delete `state.answers[g]` again (Next re-disables) — matches "changeable, not append-only."
- New: `commit()` no longer deletes `state.pending[q.g]` when `EXAM_MODE` — instead re-seeds it from `ans` — so a revisit or further toggle continues from the live set instead of a blank one.

**Rendering — `renderPage()`:**
- Branch the existing `if(answered) paintAnswered(q); else {...}` block: in exam mode, call a new `paintExamSelected(q)` instead of `paintAnswered(q)` for single-answer items (multi already goes through `paintPending(q)`, which is already neutral-colored and reusable as-is).
- `paintExamSelected(q)`: highlights the chosen option with the existing `.pending` CSS class (violet, already used for in-progress multi-select — no new CSS needed) and sets its mark text to `"selected"`. No color-by-correctness, no feedback panel render.

**Net effect:** you can click freely, change your mind, revisit any question via Back or the jump-map and change it again, right up until you submit — with zero indication of correctness at any point.

## 3. Sticky nav

- `#scorePill` and `#pctPill`: hidden (`display:none`) and skipped in `updateNav()` when `EXAM_MODE` — showing live right/wrong counts would leak correctness by proxy even without per-question color.
- Timer (`setInterval` callback on `#navTimer`): switches from count-up to a 120:00 countdown when `EXAM_MODE`. `remain = Math.max(0, 7200 - elapsed)`, formatted via the existing `fmtTime()`. Floors at `0:00` — does **not** force-submit. This is a practice tool, not proctoring software; auto-submitting an in-progress answer two days before the real exam risks losing work over a UI decision nobody asked for. If Ram wants a hard stop at zero, that's a follow-up, not part of this change.
- Landing card: one new disclosure line — "⏱ Exam Mode — no per-question feedback; explanations arrive only after you finish, with a 120:00 countdown, matching real exam conditions." Placed alongside the existing "Last scored exam" line.

## 4. After submission — unchanged

`submitExam()`, the results card, per-domain/block/format breakdown, `printAll()` (full rationale review), and the results-JSON export are untouched. The realism constraint applies only during the exam; the debrief stays exactly as rich as it is today. `submitExam()` already reads from `state.answers`, which stays correctly populated under the interaction changes above — no scoring logic changes.

## 5. Reset / resume — unchanged

`resetExam()` and `routeOnLoad()`'s three-way resume routing (`no answers → landing`, `some answered → first unanswered`, `all answered → results`) both key off `state.answers`, which exam mode keeps populated the same way (immediately for single-answer, at exactly-`selectN` for multi). No changes needed to either function.

## 6. Rollout

1. **Test 19** — retrofit directly (it already exists): add `EXAM_MODE`, patch `pick()`/`commit()`/`renderPage()`/`updateNav()`/timer/landing card as above.
2. **Test 20** — doesn't exist yet. When generated via `/cca-exam`, Step 5 of the blueprint should build it with `EXAM_MODE = true` baked in from the start, using Test 19 (post-patch) as the reference implementation, rather than generating in practice mode and retrofitting.
3. **Blueprint documentation** — add a short, explicitly-scoped "Exam Mode (temporary)" note to `prep with quiz/CLAUDE.md`, pointing at this spec, so the design-stance sentence isn't silently contradicted and so future sessions know why 19/20 behave differently from 1–18 and (presumably) 21+.

## 7. Explicitly out of scope

- No practice/exam toggle UI — fixed behavior for these two files only (Ram's choice).
- No change to any exam file other than 19 (now) and 20 (at generation time).
- No change to the default blueprint design stance for exams after the 2026-08-18 sitting.
- No auto-submit at 0:00.
- No changes to `EXAM-LOG.md` scoring format, the results-JSON schema, or DASHBOARD.html.
