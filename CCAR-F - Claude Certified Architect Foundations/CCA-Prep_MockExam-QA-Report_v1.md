# QA Evaluation Report: Claude Certified Architect Mock Exam

**Artifact under test:** `practice/CCA-Prep_MockTest-1_v1.html` · 30 questions · static HTML  
**Supporting corpus evaluated:** `practice/` bank (51 Qs), `practice/held-out-mocks/` (Mock A/B), `mcq-practice/` (dynamic generator)  
**Evaluation date:** 2026-06-27  
**Evaluator stance:** senior QA engineer + instructional designer

---

## 1. Corpus Fidelity Evaluation

**Test method:** Spot-checked all 30 question answers against `EXAM-DIGEST.md`, `CURRICULUM.md`, and domain citation files. Verified key API facts independently.

**Findings:**

| Claim in mock | Verified? | Notes |
|---|---|---|
| `tool_use` block fields: `id, name, input` | ✅ | Correct per API docs |
| Context overflow → 400 `context_length_exceeded` | ✅ | Correct |
| Prefilling = last message in array with `assistant` role | ✅ | Correct |
| `prompt caching` via `cache_control: {type: 'ephemeral'}` | ✅ | Correct |
| `stop_reason: 'max_tokens'` when ceiling hit | ✅ | Correct |
| No `json_mode` parameter in Claude API | ✅ | Correct (Anthropic uses Structured Outputs via `output_config.format`, not a `json_mode` flag — but Q21 explanation could be clearer here) |
| Minimal footprint = least permissions + prefer reversible | ✅ | Aligned with Anthropic docs |
| Principal hierarchy: operators via API/system prompt, users in human turn | ✅ | Correct |

**Accuracy flag — Q21 (D4):** The explanation says "there is no universal json_mode parameter in the Claude API" without mentioning that Anthropic *does* have `Structured Outputs` (constrained decoding via `output_config.format`). A candidate who knows about Structured Outputs could misread this as "Anthropic offers no schema-enforced JSON output," which is wrong. Needs a one-sentence clarifier.

**Missing-source flag — Q12 (D1):** "Subagents cannot spawn their own subagents" is stated as a platform constraint. Correct per `EXAM-DIGEST.md`, but the `[VERIFY]` flag on the citation files means this could drift. Confirm against live docs before ship.

**Verdict: PASS with two minor corrections needed.** Corpus fidelity is solid — questions draw from verified material, not Claude's general training knowledge.

---

## 2. Blueprint Alignment Evaluation

**Test method:** Counted domain distribution and question-type mix in `CCA-Prep_MockTest-1_v1.html` against the official blueprint in `mcq-practice/The Requirements for Anthropic Exam MCQ Prep.md`.

**Domain distribution (30 questions):**

| Domain | Blueprint % | Expected Qs | Actual Qs | Delta |
|---|---|---|---|---|
| D1 Agentic Architecture | 27% | 8.1 | 8 | ✅ |
| D2 Tool Design & MCP | 18% | 5.4 | 5 | ✅ |
| D3 Claude Code | 20% | 6.0 | 6 | ✅ |
| D4 Prompt Engineering | 20% | 6.0 | 6 | ✅ |
| D5 Context & Reliability | 15% | 4.5 | 5 | ✅ |

Domain distribution: **PASS.**

**Question type mix — Anthropic-Grade target vs actual:**

| Type | Target (Anthropic-Grade) | Expected in 30 Qs | Actual in Mock #1 |
|---|---|---|---|
| Scenario-based | 40% | 12 | ~3 |
| Anti-pattern recognition | 25% | 8 | ~2 |
| Concept + application | 25% | 8 | ~18 |
| Definition / recall | 10% | 3 | ~7 |

**This is the primary quality defect.** The mock is labeled Anthropic-Grade in spirit but reads at Prep Range difficulty in practice:
- 4× too few scenario-based questions (3 vs 12)
- 4× too few anti-pattern questions (2 vs 8)
- 2× too many concept questions and 2× too many recall questions

The practice bank (D1 file) and held-out mocks do this correctly — both are scenario-heavy and anti-pattern-forward. Mock Test #1 did not carry that pattern through.

**Verdict: FAIL on question type mix.** Domain weights pass; question type distribution does not match the Anthropic-Grade spec that the hero text implies.

---

## 3. User Experience Quality Evaluation

**Test method:** Read-through of the HTML source. Static analysis of structure, interactions, and rendering dependencies.

**What works well:**
- Polished, professional visual design (amber/ink/cream palette, DM Serif Display + JetBrains Mono)
- Progress bar, sticky score pill, per-question domain badge — all functional
- Session resume via `localStorage` — good experience, tested in source
- Per-question explanation on wrong answers — the strongest UX feature, directly serves learning
- Weakest-domain identification on the final summary — correctly implemented in JS
- Domain breakdown grid on final summary — correct
- `✅/❌` symbols (not color alone) — accessibility requirement satisfied
- Mobile responsive layout via `@media(max-width:720px)` — present
- Print stylesheet — bonus

**Blockers:**

**B1 — External font dependency.** The file references `https://fonts.googleapis.com/css2?family=DM+Serif+Display...` at line 40. This breaks the self-contained / offline requirement (Spec §5.1). A user opening this file with no internet gets system fallback fonts and a degraded first impression. Must be inlined as base64 data URI or replaced with a system font stack before ship.

**Medium-priority gaps:**

**I2 — Final screen dead-ends.** "↻ Restart Mock Test 1" re-runs the same 30 questions. No forward link to Mock Test 2 or a study path. For a commercial product, the final summary needs a "what's next" CTA.

**I3 — 30-question length not clearly framed.** The hero says "~60 min" without stating this is a half-length mock. The real exam is 60 questions. Add "Half-length mock" to the hero eyebrow so users know how it maps to the real exam.

**Nice-to-have:** No question-type label per card (the practice bank labels `Type: anti-pattern`, `Type: scenario`). Adding a subtle type badge would help candidates calibrate their preparation.

**Verdict: CONDITIONAL PASS — blocked only by Google Fonts dependency. Dead-end final screen is a UX gap but not a blocker.**

---

## 4. Additional QA Dimensions

### 4a. Content Originality & Provenance

Mock #1 stems and the held-out mock stems are **distinct** — no verbatim overlap detected between the comment block in the HTML and `held-out_D1.md`. The practice bank README documents provenance cleanly: "Authored 2026-06-09 by 5 parallel item-writers, one per domain, each grounded only in EXAM-DIGEST.md and that domain's verified citations."

However, there is **conceptual duplication** between the practice bank and Mock Test #1. The escalation counter anti-pattern appears in D1 practice Q6, held-out A-D1-06, and Mock Test #1 Q8. A candidate who studies D1 practice will recognise the pattern in the mock — fine for learning, but this means Mock Test #1 cannot serve as a blind "cold test" after the practice bank.

**Recommendation:** Explicitly label Mock Test #1 as the "warm mock" (post-practice) and the held-out mocks (Mock A/B) as "cold mocks" (taken only once, never shown during study). This distinction is not currently visible anywhere in the product.

**Verdict: PASS on originality. Needs labelling to clarify warm vs cold use.**

### 4b. Distractor Quality

D1 distractors are excellent — wrong answers require architectural reasoning to eliminate. Example from Q8 (high-stakes task): "Add automatic retry logic so the agent recovers from failures" is a genuine anti-pattern that sounds reasonable and catches the unprepared.

D2 and D3 distractors are weaker. Example from Q14 (CLAUDE.md purpose): "The billing configuration file for Claude Code API usage" is obviously wrong to anyone who has used the tool. Distractors should require domain knowledge to eliminate, not common sense.

**Verdict: PASS for D1. D2/D3 distractor quality needs tightening.**

### 4c. Explanation Quality

All 30 explanations follow the correct pattern — WHY the right answer is right, WHY the wrong answer fails. D5 explanations (context management) are particularly strong.

One gap: Q15 (Claude Code hooks) explanation defines hooks correctly but does not call out why "JavaScript callback" (option A) is wrong. Candidates who conflate Claude hooks with browser/server hooks miss the teaching moment.

**Recommendation:** In each explanation, explicitly name and refute the most tempting distractor.

**Verdict: PASS. Minor improvement opportunity.**

### 4d. The Dynamic MCQ Generator (`mcq-practice/`)

**Critical finding: the dynamic MCQ generator application does not exist.**

`mcq-practice/CLAUDE.md` states explicitly (as of 2026-06-26):

> ⚠️ STATUS: SPEC ONLY — NOT BUILT. The application (`mcq_launcher.py`, `prompt_builder.py`, `html_renderer.py`, etc.) does not exist yet. Until implemented, this generator is NOT part of the exam-readiness path.

If the commercial offer includes dynamic question generation, **it is not shippable in any form**. Only the static mock and the static practice bank are actual deliverables.

**Verdict: BLOCKER if dynamic generator is in scope for v1.**

### 4e. Exam Scenario Vocabulary Coverage

The mock does not reference the 6 official exam scenario names ("Customer Support Resolution Agent", "Multi-Agent Research System", etc.) in question stems. The practice bank and held-out mocks do. Familiarity with the exact scenario vocabulary is a stated goal in the requirements doc (§6.3 and Appendix A).

**Verdict: GAP. D1 scenario-based questions should reference scenario names.**

---

## 5. Launch Readiness Verdict

**Overall: NOT READY — 3 blockers, 3 improvements required.**

### Blockers (must fix before ship)

| # | Issue | Location | Fix |
|---|---|---|---|
| B1 | Google Fonts external CDN dependency | `CCA-Prep_MockTest-1_v1.html` line 40 | Inline fonts as base64 data URI, or swap to system font stack |
| B2 | Question type mix does not match Anthropic-Grade spec | Mock Test #1 (30 Qs) | Rewrite or replace ~9 concept questions and ~4 recall questions with scenario-based and anti-pattern equivalents |
| B3 | Dynamic MCQ generator does not exist | `mcq-practice/` | Either build it, or explicitly scope it out of v1 commercial offer |

### Improvements required before ship (medium priority)

| # | Issue | Fix |
|---|---|---|
| I1 | Q21 (D4) explanation implies Anthropic has no structured output | Add: "Anthropic's Structured Outputs feature (`output_config.format`) enforces schema compliance — it just isn't called `json_mode`." |
| I2 | Final screen dead-ends with no next step | Add a "→ Return to study path" or "→ Attempt Mock Test 2" CTA |
| I3 | Warm vs cold mock distinction not labelled | Add product-level note: "Complete the practice bank before this mock. Hold the held-out mocks (Mock A/B) for your cold-run tests." |

### Conditional path to ship (static mock only, v1)

If B1 and B2 are fixed and B3 is explicitly scoped out (dynamic generator = v2), the product is shippable as:

> **CCA-F Mock Test #1 — half-length warm mock (30 questions, ~60 min)**  
> For use after completing the practice bank. Dynamic generation is a v2 feature.

### What is already strong and should not change

- All 30 explanations — quality is high, teaching mechanism is correct
- Domain breakdown and weakest-domain identification on the final summary
- `localStorage` session resume
- Practice bank provenance and question quality (especially D1)
- Held-out mock bank — exam-quality content, properly isolated
- Overall HTML design and accessibility posture
