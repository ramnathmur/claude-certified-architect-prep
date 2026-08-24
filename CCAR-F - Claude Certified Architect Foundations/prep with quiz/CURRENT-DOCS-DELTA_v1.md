# Current-Docs Delta — Corpus vs Live Anthropic Documentation

**Version:** 1.2 | 2026-08-14 (v1.1: 2026-08-09; v1.0: 2026-07-06)
**Purpose:** The corpus was distilled from a study-guide snapshot. Anthropic's product documentation has moved since. This file records every verified divergence so that (a) Ram studies the current truth, and (b) the mock-exam generator avoids writing questions whose correct answer depends on a fact that changed after the exam was authored.
**Verification:** D1–D8 were checked against live docs on 2026-07-06 by an independent validation agent, and **re-verified 2026-08-09** (sources cited per entry). D9 is new in v1.2 and was verified against live docs on **2026-08-14**. The E-entries are new in v1.1 and come from a direct diff of the official Exam Guide PDF.
**Changelog v1.1→v1.2:** added **D9** — the subagent-spawning tool was renamed `Task` → `Agent` in Claude Code v2.1.63, tagged [CONFLICT-RISK] because the exam guide and the current product now use different names for the same tool. Found by cross-checking the community study site `claudecertificationguide.com` (mirrored 2026-08-14 at `Outputs/ccg-mirror/`) against this file, then verified against Anthropic's own SDK subagents documentation. **No D1–D8 entry was re-verified in this pass** — the 2026-09-08 re-verification deadline below still stands unchanged.
**Changelog v1.0→v1.1:** the *primary source itself changed*. Anthropic republished the official Exam Guide as **v1.0 (Effective July 2026, exam code CCAR-F)**, superseding the cached v0.2. New section "Exam-Guide Version Delta" (E1–E6) records what changed in the guide. All eight D-entries re-verified against live docs; D1 escalated in severity, D7's open caveat resolved, D2–D6 and D8 unchanged. **Filename deliberately kept at `_v1`** — six files reference this path (Corpus-Index, Exam-Mechanics, CLAUDE.md, orchestration prompts); a rename to `_v2` is a follow-up that must update all inbound references together.

---

## Generator rule (load-bearing)

The real exam was authored against the official Exam Guide's snapshot of product behavior. Where current docs and the exam guide could yield DIFFERENT correct answers, the generator must either (a) avoid making that delta the deciding line of a question, or (b) frame the question at the level both sources agree on. Deltas below marked **[SAFE]** don't change any plausible answer; deltas marked **[CONFLICT-RISK]** must not be the basis of a scored distinction.

---

# Part 1 — Exam-Guide Version Delta (NEW in v1.1)

The cached guide (`source/CCA-F-Official-Exam-Guide.pdf`, v0.2, Last Updated June 30 2026, downloaded 2026-07-06) has been superseded. The currently-published guide is **Version 1.0 — Effective July 2026 — Exam code: CCAR-F**, saved alongside it as `source/CCA-F-Official-Exam-Guide_v1.0.pdf` (+ text mirror). PDF metadata creation date: **2026-07-08** — two days after the cached copy was downloaded.

**Retrieved 2026-08-09** from the official Anthropic Partner Academy certification page (`anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification` → the "Exam Guide" PDF asset). Both files are retained; nothing was overwritten.

**Anthropic's own Document Control table describes v1.0 as "Formatting and layout updates."** That description understates it — E1 and E2 below are substantive changes to load-bearing facts, not layout. Weigh the diff, not the changelog line.

## Verified UNCHANGED between v0.2 and v1.0 (measured, not assumed)

| Element | Method | Result |
|---|---|---|
| 5 domains + weights (27/18/20/20/15) | table read | identical |
| All 6 scenarios + primary-domain mappings | word-level diff of the scenarios region | **100.0% identical** |
| All 30 task statements — titles | normalized title comparison, all 30 | **0 differences** |
| Task statements — knowledge/skills bullets | word-level diff of the objectives region | identical (only difference was the Content Outline block relocating to its own numbered section) |
| Appendix: Technologies and Concepts, In-Scope, Out-of-Scope (16 items) | word-level diff of the appendix region | **99.5% identical** — the only inserts were revision-history dates bleeding into the two-column layout |
| 12 sample questions | word-level diff | content identical; only `A)` → `A.` option-label formatting |
| 60 items, 120 min, $125, 100–1000 scaled, 720 pass, 12-month validity, 4-of-6 scenarios | table read | identical |

**Bottom line: no domain weight, scenario, task statement, in-scope topic, or out-of-scope topic changed.** The corpus's subject-matter content is not invalidated by v1.0.

## E1 — Item format now includes MULTIPLE-RESPONSE items **[CONFLICT-RISK — corpus is now wrong]**

- **Cached v0.2 framing:** "Response format — Multiple choice; one correct answer and three incorrect options," plus a whole **Response Types** section: "All questions on the exam are multiple choice format. Each question has one correct response and three incorrect responses. Select the single response that best completes the statement…"
- **Current v1.0 framing:** "Item format — **Multiple-choice and multiple-response items; each item states how many responses to select**." The entire v0.2 "Response Types" section was **deleted**.
- **Independent corroboration:** the official Certification FAQ on the same Partner Academy site states the format as "Multiple choice and scenario-based multiple response questions" (retrieved 2026-08-09).
- **Source:** `source/CCA-F-Official-Exam-Guide_v1.0.pdf` §3 vs `source/CCA-F-Official-Exam-Guide.pdf` p.2 + "Response Types"; `anthropic-partners.skilljar.com/page/faq-certifications`
- **Nuance worth keeping:** the phrase "multiple-response" appears **exactly once** in the whole v1.0 guide, with no elaboration, and **all 12 sample questions remain single-answer, 4-option**. So the guide asserts the format exists but demonstrates only single-answer items.
- **Exam posture:** this is the one finding that makes a corpus statement affirmatively false. `CCA-Prep_Exam-Mechanics_v2.md` currently states "Multiple choice — 1 correct + 3 incorrect options, single answer" as an official fact. **Proposed corpus edit — awaiting Ram's sign-off (see GENERATION-INTELLIGENCE.md → Pending Corpus Decisions, CG-03).** Note the generator's own 4-option single-answer format is a separate, deliberate product decision and is NOT automatically implicated.

## E2 — Score report now includes per-domain percent-correct **[SAFE — corpus understates]**

- **Cached v0.2 framing:** "Result reporting — Pass or fail." Corpus repeats this as "pass/fail reporting only."
- **Current v1.0 framing:** "Result reporting — Pass/fail with scaled score (100–1,000), **plus percent-correct by domain on the score report**." New §10 adds: "Your score report also shows the percentage of items you answered correctly within each content domain. Section-level percentages are provided to help you understand your performance and are **not** used to determine your pass or fail result, which is based on your total scaled score."
- **Source:** `CCA-F-Official-Exam-Guide_v1.0.pdf` §3 and §10
- **Exam posture:** [SAFE] — no scored question turns on this. It is a **study-planning fact** Ram should know (the real exam returns a per-domain breakdown, which is exactly the shape this project's mock-exam results JSON already produces). Proposed as CG-04.

## E3 — "The platform requires an answer to every question" is GONE **[CONFLICT-RISK — corpus asserts a deleted fact]**

- **Cached v0.2:** "The exam platform requires an answer to every question before you can advance, so no question is left unanswered."
- **Current v1.0:** the sentence does not appear anywhere in the document (verified: 1 occurrence in v0.2, **0 in v1.0**).
- **Source:** grep of both text mirrors
- **Exam posture:** [CONFLICT-RISK] for corpus accuracy, not for question authoring. `CCA-Prep_Exam-Mechanics_v2.md` carries a whole Format-table row asserting this ("no skip, no penalty for wrong answers, so an unsure answer is always submitted") and repeats it under Scoring Context. Its removal does not mean the opposite is now true — it means the guide no longer states it either way, so the corpus is asserting something no longer supported by the primary source. Proposed as CG-05.

## E4 — Exam code CCAR-F introduced **[SAFE]**

- v1.0 introduces an explicit exam code, **CCAR-F**, printed on the title page and in the details table. The cached v0.2 has no exam code, and this project has always called it "CCA-F".
- Community sources use **CCA-F and CCAR-F interchangeably**; the official code is CCAR-F.
- **Exam posture:** [SAFE] — cosmetic for question authoring. Affects naming only. Renaming the whole corpus is a large, low-value change; proposed as a one-line note instead (CG-06).

## E5 — Guide restructured + 9 new administrative sections **[SAFE]**

v1.0 renumbers everything into 18 sections and adds material with no v0.2 equivalent: **§10 How the Exam Is Scored** (criterion-referenced; passing score set by a formal standard-setting study of minimally-qualified-candidate performance), **§11 Registration and Scheduling**, **§12 Exam Policies** (ID requirements; accommodations via Pearson VUE; retake waits of **14 / 30 / 90 days**, max **4 attempts per rolling 12 months**; no-show forfeits fee), **§13 Exam-Day Rules of Conduct**, **§14 Confidentiality/NDA**, **§15 Credential Maintenance and Recertification**, **§16 Support, Appeals, and Privacy**, **§17 Appendix**, **§18 Document Control**.

Note the retake policy is now **guide-official** — Exam-Mechanics v2 currently sources it from "Pearson VUE policy pages," which can be upgraded to the primary source. [SAFE], no question impact.

## E6 — Recertification path is new and materially useful **[SAFE — study-planning fact]**

v1.0 §15: the credential is valid 12 months; to renew **on time** you review what changed and complete a **free, non-proctored assessment** on the Anthropic Partner Academy — no fee. If the credential **lapses**, you must retake the full exam at full price. Anthropic may also require a full retake instead of the renewal assessment if exam content changes significantly.

Not in v0.2 at all. No question impact — but it changes the cost calculus of letting the credential lapse, which is worth Ram knowing before he sits the exam.

## E7 — Program context: four certifications now exist **[SAFE — not a corpus fact]**

Anthropic's certification program expanded from one exam to four (announced on Anthropic's own blog and the Partner Academy FAQ): Claude Certified **Associate** – Foundations (CCAO-F, $99), Claude Certified **Developer** – Foundations (CCDV-F, $125), Claude Certified **Architect** – Foundations (**CCAR-F, $125 — Ram's target, unchanged**), and Claude Certified **Architect – Professional** (CCAR-P, $175).

**Practical gate worth flagging:** the Partner Academy FAQ states registration requires "a partner email address on a recognized company domain — personal email addresses will not work," and candidates must work at a Claude Partner Network organization. This is an eligibility precondition, not an exam-content fact — but it is the kind of thing that blocks a sitting on the day.

- **Source:** `claude.com/blog/four-role-based-claude-certifications`; `anthropic-partners.skilljar.com/page/faq-certifications` (both retrieved 2026-08-09)

---

# Part 2 — Live-Docs Deltas (D1–D8 re-verified 2026-08-09; D9 added 2026-08-14)

## D1 — `allowed-tools` semantics **[CONFLICT-RISK — official exam framing wins] — SEVERITY ESCALATED**

- **Official Exam Guide framing (task 3.2 skill bullet — verified present and *word-for-word unchanged* in the v1.0 PDF):** "Configuring allowed-tools in skill frontmatter to **restrict tool access** during skill execution (e.g., limiting to file write operations to prevent destructive actions)."
- **Current docs (re-verified 2026-08-09):** `allowed-tools` = "Tools Claude can use **without asking permission** during the turn that invokes this skill… **It does not restrict which tools are available: every tool remains callable**, and your permission settings still govern tools that are not listed." The restricting key is `disallowed-tools` = "Tools **removed from Claude's available pool** while this skill is active."
- **Why escalated:** at v1.0 of this file the divergence was *implicit* (docs described a grant; the guide described a restriction). Live docs now **explicitly negate** the exam guide's framing in a dedicated sentence. The contradiction is head-on.
- **Source:** `source/CCA-F-Official-Exam-Guide_v1.0.pdf` (Domain 3, task 3.2) vs https://code.claude.com/docs/en/skills (retrieved 2026-08-09)
- **Exam posture: UNCHANGED.** The exam is authored against the official guide, so a question treating allowed-tools as a restriction mechanism is fair game and the generator SHOULD follow the official framing. Ram should additionally know the current-docs semantics for real-world work, but answer exam questions per the official guide. This remains the single highest-value trap in the corpus.

## D2 — `stop_reason` value set **[SAFE]** — re-verified, unchanged

- **Corpus/guide framing:** four values — `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`.
- **Current docs:** still a superset — adds `pause_turn`, `refusal`, `model_context_window_exceeded`. Newer models also return a structured `stop_details` object when `stop_reason == "refusal"`.
- **Source:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons; Anthropic `claude-api` reference (retrieved 2026-08-09)
- **Exam posture:** unchanged. The exam's agentic-loop questions turn on `tool_use` vs `end_turn`, which is unchanged. The generator may mention the extra values but must not mark a "four values exist" option as correct.

## D3 — MCP configuration scopes **[SAFE]** — re-verified, unchanged

- **Corpus/guide framing:** two scopes — project (`.mcp.json`) and user (`~/.claude.json`).
- **Current docs:** still three — **Local** (the default; stored in `~/.claude.json` but per-project-private), **Project** (`.mcp.json` in project root, shared via version control), **User** (`~/.claude.json`, all projects). Enterprise/managed configuration exists as a fourth admin-deployed layer. Env-var expansion in `.mcp.json` confirmed current (`${VAR}` and `${VAR:-default}`, expandable in `command`, `args`, `env`, `url`, `headers`).
- **Source:** https://code.claude.com/docs/en/mcp (retrieved 2026-08-09)
- **Exam posture:** unchanged. The exam guide tests project-vs-user scoping for team-sharing decisions. Generator should keep questions at project-vs-user level.

## D4 — CLAUDE.md hierarchy semantics **[CONFLICT-RISK]** — re-verified, unchanged

- **Corpus framing (v1):** levels form a "highest → lowest precedence" override hierarchy.
- **Current docs (verbatim, 2026-08-09):** "All discovered files are **concatenated into context rather than overriding each other**." Ordering runs filesystem-root-down to the working directory; `CLAUDE.local.md` is appended after `CLAUDE.md` at each level; subdirectory files load on demand.
- **Also current:** the hierarchy now has four documented levels — **Managed policy** (enterprise), User, Project, Local (`CLAUDE.local.md`) — vs the guide's "user/project/directory". `@import` confirmed current (max depth 4 hops); `.claude/rules/` with `paths:` YAML frontmatter confirmed current; `/memory` confirmed current.
- **Source:** https://code.claude.com/docs/en/memory (retrieved 2026-08-09)
- **Exam posture:** unchanged. The official guide tests hierarchy LEVELS and sharing scope, not override mechanics. The generator must not write a question whose correct answer requires "lower level overrides higher level."

## D5 — Message Batches API and tool use **[NUANCE — official framing is precise and current]** — re-verified, unchanged

- **Official Exam Guide framing (task 4.5 + Appendix, unchanged in v1.0):** "The batch API does not support multi-turn tool calling **within a single request**."
- **Current docs:** consistent with that precise reading. 50% discount and 24h window confirmed current; batch requests can include tool definitions and multi-turn histories, but each request is self-contained. Results arrive in **any order** — key by `custom_id`, never by position (matches the guide's `custom_id` emphasis).
- **Source:** `CCA-F-Official-Exam-Guide_v1.0.pdf` §6/§17 vs https://platform.claude.com/docs/en/build-with-claude/batch-processing (retrieved 2026-08-09)
- **Exam posture:** unchanged. Use the official guide's precise wording. Never write "batches don't support tool use at all" as a correct answer, and never mark the official precise claim incorrect.

## D6 — Slash commands and skills convergence **[SAFE]** — re-verified, now stronger

- **Corpus/guide framing:** commands in `.claude/commands/`, skills in `.claude/skills/` as distinct mechanisms.
- **Current docs (2026-08-09), stronger than at v1.0 of this file:** "**Custom commands have been merged into skills.** A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way. Your existing `.claude/commands/` files keep working." Skills add supporting files, frontmatter, and auto-loading.
- **Frontmatter note:** `context: fork`, `allowed-tools`, `disallowed-tools`, `disable-model-invocation`, `agent`, `model` are current Claude Code fields. `argument-hint` still works in Claude Code but is **rejected** by the claude.ai / Skills API six-field spec (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`). The exam guide names `argument-hint`, which remains correct for Claude Code.
- **Source:** https://code.claude.com/docs/en/skills (retrieved 2026-08-09)

## D7 — `tool_choice` values **[SAFE] — OPEN CAVEAT NOW RESOLVED**

- Confirmed current: `{"type":"auto"}` (default), `{"type":"any"}`, `{"type":"tool","name":"..."}` — exactly the set the official exam guide names in task 2.3.
- **Resolved:** v1.0 of this file said a `none` option "appears in some docs surfaces but was **not confirmed** as a defined `tool_choice` value in the tool-use reference." It is now **confirmed**: `{"type":"none"}` ("Claude cannot use tools") is documented in the tool-use reference, and `none` appears as a first-class tool-choice value in the official per-model token-cost table on the tool-use overview page.
- **Generator rule — keep the prohibition, replace its justification:** still do not build a scored question around `none`. The reason is no longer "it may not exist" but "**the official exam guide's task 2.3 names only auto/any/forced**, so `none` is outside the tested set." Also current: `disable_parallel_tool_use` can be combined with any `tool_choice` value.
- **Source:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview (retrieved 2026-08-09)

## D8 — CLI structured output **[SAFE]** — re-verified, unchanged

- Confirmed current: `-p` / `--print`; `--output-format` (`text` | `json` | `stream-json`); `--json-schema` (print mode only, returns validated JSON matching a schema); `--resume` / `-r`; `--continue` / `-c`; `--fork-session` (new session ID when resuming — matches the guide's `fork_session` mention).
- **Source:** https://code.claude.com/docs/en/cli-reference (retrieved 2026-08-09)

## D9 — The subagent-spawning tool is renamed `Task` → `Agent` **[CONFLICT-RISK — official exam framing wins]** — NEW in v1.2

- **Corpus/guide framing:** subagents are spawned by including `"Task"` in the coordinator's `allowedTools`. `CCA-Prep_Domain-1_v2.md` §1.2 ("Spawning Subagents: The `Task` Tool") names `Task` four times and never mentions `Agent`. The official Exam Guide task statement 1.3 uses the same name.
- **Current docs:** the tool is now `Agent`. Anthropic's SDK subagents page states it directly: *"The tool name was renamed from `Task` to `Agent` in Claude Code v2.1.63. Current SDK releases emit `Agent` in `tool_use` blocks but still use `Task` in the `system:init` tools list and in `result.permission_denials[].tool_name`. Checking both values in `block.name` ensures compatibility across SDK versions."* The same page's worked examples all pass `"Agent"` in `allowedTools`: *"Claude invokes subagents through the `Agent` tool, so include `Agent` in `allowedTools` to auto-approve subagent invocations without a permission prompt."*
- **Precision worth keeping:** this is **not** a clean alias. The name that appears depends on the surface — `Agent` in `tool_use` blocks, `Task` still in `system:init` and in permission-denial records. "Task still works as an alias" is the community shorthand; the docs describe a split, and the corpus should carry the split, not the shorthand.
- **Source:** https://code.claude.com/docs/en/agent-sdk/subagents (retrieved 2026-08-14). Independently surfaced by the community study site `claudecertificationguide.com` lesson 1.3, which reported the rename and the v2.1.63 version but not the `system:init` / `permission_denials` nuance — the delta was found via that site and then verified against the official docs, which are the citation of record here.
- **Exam posture:** **[CONFLICT-RISK].** The architectural fact the exam tests is unchanged and remains the scored point: the coordinator's `allowedTools` must include the subagent-spawning tool, or it physically cannot spawn subagents — a binary gate, not a soft preference. But the *name* now differs between the exam guide and current product, so a question whose key turns on `Task` versus `Agent` could be decided by which source the candidate read. **Never make the tool's name the deciding line of a scored question.** Where a stem or option must name it, use the official guide's `Task`, consistent with the D1 and D4 precedent that official framing wins.
- **Corpus edit status:** not applied to `CCA-Prep_Domain-1_v2.md`. Under the generator rule this delta is recorded here and consumed at generation time; rewriting §1.2 to say `Agent` would move the corpus away from the exam guide it is authored against. Flag for Ram only if a future guide revision adopts the new name.

---

## Maintenance

Re-verify this file whenever (a) a mock exam is generated more than 30 days after the `Last full verification pass` date below, or (b) any Anthropic docs-changelog announcement touches skills, MCP, memory, batches, or stop reasons. Add new deltas with the same [SAFE]/[CONFLICT-RISK] tag and source line.

**Additional trigger added in v1.1:** re-check the **Exam Guide PDF asset itself** on the Partner Academy certification page, not just the docs. The v0.2 → v1.0 republication happened two days after the cached download and would have been invisible to a docs-only check. Compare the printed version marker and the §18 Document Control table.

**Last full verification pass: 2026-08-09** (D1–D8 + E1–E7). D9 was added and verified 2026-08-14, but that was a single-entry addition, not a pass over the file — **the deadline below is deliberately NOT extended by it.**
**Next re-verification due:** before any exam generated after **2026-09-08** (30-day docs-currency rule).
