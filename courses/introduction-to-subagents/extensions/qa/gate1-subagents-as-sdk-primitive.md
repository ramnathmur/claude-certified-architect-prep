# QA Gate 1 — Content Fidelity Report
**Lesson:** `subagents-as-sdk-primitive.html`
**Ground truth:** `source/subagents-as-sdk-primitive_citations.md`
**Reviewer:** QA Gate 1 (independent) — AI Professor + Senior Research Analyst
**Date:** 2026-06-05

---

## VERDICT: **PASS**

0 Blockers. 0 Majors. 3 Minors. (PASS requires 0 Blockers AND 0 Majors.)

The lesson is a faithful, traceable rendering of the citations file. Every major
citation section is represented; all 20 answer keys (10 inline MCQs + 10 quiz
questions) are correct; the two author analogies are both labelled "Author
analogy, not a product fact"; and all version-sensitive facts carry visible
VERIFY/⚠ notes. No hallucinated product facts were found.

---

## 1. Coverage — all major sections represented

| Citation section | HTML location | Status |
|---|---|---|
| §1 AgentDefinition fields (TS + Python shapes, field table) | L2 | ✅ Full — both code blocks verbatim, full field table |
| §2 `agents` param + programmatic-vs-filesystem precedence + filesystem ladder | L3 | ✅ Full — type sigs, verbatim Python example, ladder SVG |
| §3 Runtime delegation / Agent tool / Task→Agent rename | L4 | ✅ Full |
| §4 Prompt-string-only channel + receives/does-not-receive table | L5 | ✅ Full + "fresh but not empty" |
| §5 Context isolation + persistence detail | L6 | ✅ Full |
| §6 Guardrails (no-nesting, least-privilege, model, permissionMode, maxTurns) | L7 | ✅ Full |
| §7 Workflow graduation (caps, version gates, who-holds-the-plan table) | L9 | ✅ Full |
| §8 CLI↔SDK mapping (frontmatter, --agents, mapping table, filesystem-only fields) | L8 | ✅ Full |
| §9 Design heuristics (subagent vs longer prompt, one-responsibility, description routing) | L10 | ✅ Full |

No section is missing or thin. Nice-to-note: the verbatim `.claude/agents/code-reviewer.md`
frontmatter example, the never-available-tools list, and the `/btw` heuristic
are all preserved.

## 2. Correctness — spot-checks against citations

All checks **PASS**:

- TS `AgentDefinition` type (L2 code block) — matches citations lines 27-43 field-for-field, including `criticalSystemReminder_EXPERIMENTAL`. ✅
- Python `@dataclass` (L2 code block) — matches citations lines 49-64 field order and types. ✅
- camelCase-in-Python `TypeError` gotcha (L2 callout, Q2) — matches citation line 67 verbatim claim. ✅
- `description` + `prompt` as the only required fields (L2 text, Q1) — matches. ✅
- "omit `tools` → inherits all" (L2 table, L3, L7, Q3) — matches citation line 75. ✅
- Task→Agent rename at **v2.1.63** (L4 verifynote, MCQ) — matches citation line 148. ✅
- "Task" still in `system:init` + `permission_denials[].tool_name` (L4) — matches. ✅
- Programmatic-beats-filesystem precedence (L3, Q8) — verbatim quote matches citation line 138. ✅
- Filesystem ladder: managed > `--agents` > project > user > plugin (L3 SVG) — matches citation line 138. ✅
- No-nesting rule + "don't put Agent in a subagent's tools" (L7, Q6, Q7) — matches citation line 196. ✅
- Workflow caps ≤16 concurrent / 1,000 per run (L9, Q10) — matches citation lines 211/240. ✅
- Workflow version gates: TS SDK v0.3.149+ / Claude Code v2.1.154+ (L9 verifynote) — matches citation line 242. ✅
- Model resolution order: `CLAUDE_CODE_SUBAGENT_MODEL` → invocation `model` → definition `model` → main model (L7) — matches citation line 209. ✅
- Tool allow-list combos table (L7 SVG): Read/Grep/Glob; Bash/Read/Grep; Read/Edit/Write/Grep/Glob; omit tools — matches citation lines 200-205. ✅
- disallowedTools-denylist-applied-first ordering (L7, MCQ) — matches citation line 198. ✅
- Permission-mode precedence (bypassPermissions/acceptEdits override; auto ignores frontmatter) (L7) — matches citation line 215. ✅
- Persistence: separate files, immune to main compaction, `cleanupPeriodDays` default 30, ~95% auto-compaction, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` (L6 callout) — matches citation line 188. ✅
- Never-available tools list: Agent, AskUserQuestion, EnterPlanMode, ExitPlanMode (unless permissionMode: plan), ScheduleWakeup, WaitForMcpServers (L7) — matches citation line 207. ✅
- Filesystem-only fields hooks/isolation/color (L8) — matches citation lines 282/287. ✅
- 8191-char Windows command-line limit workaround (L3 table) — matches citation line 140. ✅

No invented values, no mismatched version strings, no fabricated fields detected.

## 3. Traceability / anti-hallucination

Every substantive claim traces to the citations file. No product fact appears
that is absent from citations. **Both author analogies are correctly labelled:**
- L1 hiring-through-a-form / job-description-in-code analogy → "(Author analogy, not a product fact.)" ✅
- L5 emailing-a-contractor analogy → "(Author analogy, not a product fact.)" ✅

The sources block (7 URLs) and footer both restate the no-external-facts / labelled-analogies / VERIFY-preserved discipline.

## 4. MCQ answer-key soundness

All 20 keys verified correct (0-indexed `data-correct` cross-checked to option text and citations):

| Item | Key | Correct? | Item | Key | Correct? |
|---|---|---|---|---|---|
| L1 | 2 (programmatic) | ✅ | Q1 | 1 (description+prompt) | ✅ |
| L2 | 1 (maxTurns=5) | ✅ | Q2 | 2 (TypeError) | ✅ |
| L3 | 0 (agent name) | ✅ | Q3 | 0 (inherits all) | ✅ |
| L4 | 2 (system:init + denials) | ✅ | Q4 | 1 (prompt string) | ✅ |
| L5 | 3 (restate in prompt) | ✅ | Q5 | 2 (parent history/results) | ✅ |
| L6 | 1 (isolated window) | ✅ | Q6 | 0 (Agent in allowedTools) | ✅ |
| L7 | 0 (denylist first) | ✅ | Q7 | 3 (cannot spawn) | ✅ |
| L8 | 2 (markdown body) | ✅ | Q8 | 2 (programmatic wins) | ✅ |
| L9 | 1 (who holds plan) | ✅ | Q9 | 0 (prompt) | ✅ |
| L10 | 3 (multi-phase shared context) | ✅ | Q10 | 1 (Workflow tool) | ✅ |

No distractor is a true statement mislabelled as wrong, and no keyed-correct
answer is actually false. Distractors are cleanly false per citations (e.g. Q7
distractors about allowed nesting contradict the no-nesting rule; L10/Q5
distractors correctly inverted).

## 5. [VERIFY] preservation

All 11 source [VERIFY] items that surface as version-sensitive facts in the HTML
carry a visible VERIFY/⚠ marker:

| [VERIFY] item | HTML treatment | OK? |
|---|---|---|
| 1. Field roster (TS/Py) | L2 codelabel "VERIFY field roster" + verifynote | ✅ |
| 2. No mode/source field | L2 verifynote (explicit) | ✅ |
| 3. No-nesting rule | Stated firmly (rule, not version-sensitive) — acceptable | ✅ |
| 4. Concurrency caps (per-turn cap unknown) | L9 verifynote explicitly flags this as VERIFY | ✅ |
| 5. maxTurns vs timeout | L7 inline VERIFY on timeout | ✅ |
| 6. Task→Agent rename v2.1.63 | L4 verifynote | ✅ |
| 7. Workflow version gates | L9 verifynote + hero banner | ✅ |
| 8. SDK naming | Implicit (package names used correctly); not stated as a flat version claim | ✅ |
| 9. Host redirects | N/A to lesson body; sources cite live hosts | ✅ |
| 10. Filesystem-only fields | L8 verifynote | ✅ |
| 11. general-purpose built-in | L1 (stated as current); low version risk | ✅ |

The hero `verifynote` banner pre-flags v2.1.63, v0.3.149+, v2.1.154+, and the
caps. **No version-sensitive fact is stated flatly without a caveat.**

---

## Minors (non-blocking)

1. **L2 field table — `model` default wording differs between two sources.**
   The L2 table says model "Defaults to main model" (per citations §1, line 77),
   while L7 says it "defaults to `inherit` if omitted" (per citations §6, line 209).
   Both trace correctly to their respective citation sources and are functionally
   equivalent (`inherit` = main model), but a reader comparing the two sections
   may notice the wording difference. *Fix (optional):* add a one-line note that
   `inherit` resolves to the main model, so the two phrasings read as the same fact.

2. **L9 caption / SVG (g) restates "≤16 concurrent / 1,000 per run" without an
   inline VERIFY marker** (the marker is present in the adjacent verifynote two
   blocks down). Coverage is adequate because the caps are flagged VERIFY nearby,
   but the bare numbers in the SVG text could be read in isolation. *Fix (optional):*
   no change required; the nearby verifynote satisfies Gate 5.

3. **Forward link to S-E3 (`orchestrator-worker-at-scale.html`) is self-flagged as
   possibly 404** ("not built yet; this forward link may 404"). Honest and harmless;
   noting only for completeness. Not a content-fidelity issue.

---

## Summary
The lesson faithfully reproduces the citations with no factual drift, correct
answer keys throughout, properly labelled analogies, and preserved VERIFY flags.
**Gate 1: PASS.**
