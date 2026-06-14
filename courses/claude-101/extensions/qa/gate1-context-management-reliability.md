# QA Gate 1 — Content Fidelity Report

**Lesson:** `context-management-reliability.html`
**Ground truth:** `context-management-reliability_citations.md`
**Reviewer role:** AI Professor + Senior Research Analyst (independent)
**Date:** 2026-06-05

---

## VERDICT: **PASS**

0 Blockers, 0 Majors. Three Minors (cosmetic/wording) noted below. The lesson is a faithful rendering of the citations file: every major citation section is represented, all concrete numbers/strings/JSON shapes match the source, the single analogy is correctly labeled, every MCQ answer key is sound, and the version-sensitive facts carry visible ⚠ VERIFY notes.

---

## 1. Coverage — all citation sections represented

| Citation section | Lesson location | Status |
|---|---|---|
| 1. Context windows (200K/1M, shared budget) | §2 | Covered (full) |
| 2. Linear accumulation / quadratic bill | §3 | Covered (full) |
| 3. Context rot / attention budget | §4 | Covered (full) |
| 4. Compaction | §5 | Covered (full) |
| 5. Context editing | §6 | Covered (full) |
| 6. Effective context engineering | §7 | Covered (full) |
| 7. Token budgeting | §8 | Covered (full) |
| 8. Reliability patterns | §9 | Covered (full) |
| 9. Prompt-caching intersection | §3, §8, §9 | Covered (brief, as scoped to C-E4) |

No section is missing or thin. The prompt-caching material is intentionally brief per the citations' own scope note ("full treatment belongs to extension C-E4") and the HTML repeats that framing.

---

## 2. Correctness — concrete-fact spot-check (all PASS)

Every number, header string, type string, and JSON shape below was checked HTML-vs-citations and **matches**:

- Compaction trigger **150,000** input tokens, min **50,000** — §5 + both key-takeaway and Quiz Q4. ✓
- Compaction beta header `compact-2026-01-12`; edit type `compact_20260112` — §5 VERIFY note + request JSON. ✓
- Context-editing beta header `context-management-2025-06-27` — §6 VERIFY note. ✓
- Strategy strings `clear_tool_uses_20250919`, `clear_thinking_20251015` — §6 table + config JSON + thinking-clear text. ✓
- Overflow stop reason `model_context_window_exceeded` — §2, §9, Quiz A Q4. ✓
- Earlier-model opt-in header `model-context-window-exceeded-2025-08-26` — §2. ✓
- Cache min prefix **1,024** (Opus 4.8 / Sonnet 4.6 / Sonnet 4.5 / Opus 4.1) vs **4,096** (Opus 4.7 / 4.6 / 4.5 / Haiku 4.5) — §9 VERIFY note. ✓ (matches citations §9/quick-ref)
- Cache pricing multipliers **1.25× / 2× / 0.1×** — §9 VERIFY note. ✓
- Window sizes **200K / 1M** and model IDs `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-haiku-4-5-20251001` — §2 table. ✓
- Compaction request JSON (model, max_tokens 4096, trigger value 150000, `pause_after_compaction: false`, `instructions: null`) — §5, byte-for-byte match with citations. ✓
- Compaction response JSON (`compaction` block, `iterations` array with 180000/3500 and 23000/1000, `stop_reason: end_turn`) — §5, match. ✓
- Tool-result-clearing config JSON (trigger 30000, keep 3, clear_at_least 5000, exclude_tools `["web_search"]`) — §6, match. ✓
- `usage` object fields (`input_tokens` 2048, `output_tokens` 503, `cache_creation_input_tokens` 5120, `cache_read_input_tokens` 1800) — §8, match. ✓
- Total-input formula `cache_read + cache_creation + input_tokens` = 1800+5120+2048 = **8,968** — §8 text + MCQ. ✓ (arithmetic correct)
- `count_tokens` endpoint `POST /v1/messages/count_tokens`; example counts 14 / 403 / 1551 / 2188; RPM tiers 100 / 2,000 / 4,000 / 8,000 — §8. ✓
- Context-aware budget signal `<budget:token_budget>1000000</budget:token_budget>` and `<system_warning>Token usage: 35000/1000000; 965000 remaining</system_warning>` — §8. ✓ (numbers match citations exactly)
- `cache_control` shape `{ "cache_control": { "type": "ephemeral", "ttl": "5m" } }` — §9. ✓
- Per-model thinking-clear defaults table (Opus 4.5+/4.1−; Sonnet 4.6+/4.5−; Haiku all through 4.5) — §6, match. ✓
- Thinking-clear-first ordering rule — §6. ✓
- MRCR v2 8-needle stat **76% vs 18.5%** (Opus 4.6 vs Sonnet 4.5) — §4, match + carries VERIFY. ✓

**Verbatim quotes** spot-checked against the citations' quoted text (context-window definition, "more context isn't automatically better," "attention budget," "n² pairwise relationships," compaction drop-behavior, context-editing definition, server-side property, context-engineering maxim) — all reproduce the source wording accurately.

No numeric, header, type-string, or JSON-shape mismatch was found.

---

## 3. Traceability / anti-hallucination

Every substantive factual claim in the HTML traces to a claim in the citations file. No product fact appears that is absent from the citations. Spot-checks of the riskiest claims (Microsoft Foundry 200K, 1M model set, batch-300K context, auto-compact %, MRCR stat, cache prices) all trace to a corresponding citation line, and the version-sensitive ones are caveated.

**Analogy label — confirmed.** The single author analogy (cutting board / pantry, §1) is explicitly tagged inline: `<span class="analogy">Analogy, not a product fact.</span>` and the blockquote opens "Analogy (clearly labeled):". This is the only non-source illustration in the lesson, and it is labeled exactly as required. The Sources section and footer both restate that this is the one analogy and that it is labeled.

---

## 4. MCQ answer-key soundness — all keys correct

Every inline MCQ and both quizzes were verified key-vs-citations. All keyed answers are correct and no distractor is a true statement mislabeled (or vice-versa).

| Question | Keyed index | Verdict |
|---|---|---|
| §2 "does NOT consume the window" | 3 (training corpus) | ✓ |
| §3 "why cost > linear" | 1 (re-sends history) | ✓ |
| §4 "what budget" | 2 (attention budget) | ✓ |
| §5 "messages before compaction block" | 1 (API drops them) | ✓ |
| §6 "why clear_at_least" | 0 (cache-invalidation worthwhile) | ✓ |
| §8 "total input" | 1 (8,968) | ✓ |
| §9 "model_context_window_exceeded response" | 2 (handle/compact) | ✓ |
| Quiz A Q1 working memory | 2 | ✓ |
| Quiz A Q2 not from window | 3 (weights) | ✓ |
| Quiz A Q3 cumulative cost | 0 (quadratic) | ✓ |
| Quiz A Q4 overflow signal | 1 (stop_reason) | ✓ |
| Final Q1–Q10 | 2,3,1,0,2,3,1,0,2,1 | ✓ all |

Distractors checked for "true-but-marked-wrong": none found. E.g. Final Q4's "min 50,000" is folded into the correct option (not a trap), and the 200,000/output-token distractors are genuinely false per citations.

---

## 5. [VERIFY] preservation — all version-sensitive facts caveated

The citations' 12-item [VERIFY] list is preserved. Version-sensitive facts that appear in the HTML carry a visible ⚠ VERIFY note or inline badge:

| [VERIFY] item | In HTML? | Caveated? |
|---|---|---|
| 1. Model lineup & sizes | Yes (§2 table) | ✓ verifynote + key-takeaway badge |
| 2. 1M beta header | Yes (§2) | ✓ verifynote |
| 3. Opus 4.8 not context-aware | Yes (§8) | ✓ verifynote + badge |
| 4. Compaction header/type | Yes (§5) | ✓ verifynote + key-takeaway badge |
| 5. Context-editing header/strings | Yes (§6) | ✓ verifynote |
| 6. `applied_edits` shape | Yes (§6) | ✓ verifynote (flagged as unconfirmed) |
| 7. Auto-compact % (~83.5%/~167K) | Yes (§5) | ✓ verifynote (marked unverified) |
| 8. MRCR stat | Yes (§4) | ✓ verifynote |
| 9. Cache prices / min-prefix | Yes (§9) | ✓ verifynote |
| 10. Batch 300k header | **Not in HTML** | N/A — fact omitted, so no caveat needed |
| 11. Retries / idempotency | Yes (§9) | ✓ verifynote (marked inferred) |
| 12. Pricing snapshot ($5/$25 etc.) | **Not in HTML** | N/A — prices omitted from §2 table (only sizes/IDs shown), so no flat statement to caveat |

No version-sensitive fact is stated flatly without a caveat. Items 10 and 12 were simply not carried into the HTML (the §2 table deliberately omits price columns and the batch-300K header), so there is nothing to flag — this is a safe omission, not a defect. The Sources section also aggregates a consolidated [VERIFY] list.

---

## Defect tables

### Blockers
*(none)*

### Majors
*(none)*

### Minors (cosmetic / wording — non-blocking)

| # | Location | Issue | Correct per citations | Suggested fix |
|---|---|---|---|---|
| m1 | Consolidated [VERIFY] list, Sources section (§ "📌 [VERIFY] flags preserved") | The aggregated list enumerates 9 flags and omits the batch-300K header (#10) and the pricing snapshot (#12) from the citations' 12-item list. This is internally consistent (those two facts aren't in the lesson body), but a reader comparing to the source's "12-item list" may notice the count differs. | Citations list has 12 items; HTML body legitimately drops items 10 and 12. | Optional: add a parenthetical "(items 10 & 12 — batch-300K header and price snapshot — were not included in this lesson body)" so the count reconciliation is explicit. Purely cosmetic. |
| m2 | §3 cross-reference and §9 | Prompt caching is referenced as "Section 8" in §3 ("prompt caching mitigates the cost … (Section 8)") but the brief caching treatment actually lives in **Section 9**. The §8 budget pie does touch caching, so it is not wrong, but the dedicated caching paragraph is in §9. | Caching brief = §9 per the lesson's own structure. | Optional: change "(Section 8)" to "(Sections 8–9)" or "(Section 9)" for precision. Minor. |
| m3 | §2 VERIFY note wording | Says the 1M set is "Opus 4.8, Mythos Preview, Opus 4.7, Opus 4.6, and Sonnet 4.6." Citations verbatim string is "Claude Opus 4.8, Claude Mythos Preview, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6." Content identical; only the "Claude" prefix is dropped (paraphrase, not a quote). | Same set, same order. | None required — it is not presented as a verbatim quote. Noted only for completeness. |

---

## Reviewer notes

- The HTML is admirably disciplined: JSON shapes are reproduced character-accurate (including the `iterations` 180000/3500 summarization-cost example), the 8,968 arithmetic is correct, and the context-aware budget tag uses the exact 35000/1000000/965000 figures from the source.
- The lesson does not invent a 1M beta header, does not assert Opus is context-aware, and does not state the unverified auto-compact percentage as fact — all three are the most common ways this topic goes wrong, and all three are handled correctly.
- Gate 1 scope (content fidelity) only: build mechanics, interactivity, and accessibility were not assessed here.

**Gate 1 result: PASS** (0 Blockers, 0 Majors).
