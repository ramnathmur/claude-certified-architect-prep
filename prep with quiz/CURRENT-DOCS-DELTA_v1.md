# Current-Docs Delta — Corpus vs Live Anthropic Documentation

**Version:** 1.0 | 2026-07-06
**Purpose:** The corpus was distilled from a study-guide snapshot. Anthropic's product documentation has moved since. This file records every verified divergence so that (a) Ram studies the current truth, and (b) the mock-exam generator avoids writing questions whose correct answer depends on a fact that changed after the exam was authored.
**Verification:** every entry below was checked against live docs on 2026-07-06 by an independent validation agent (sources cited per entry).

---

## Generator rule (load-bearing)

The real exam was authored against the official Exam Guide's snapshot of product behavior. Where current docs and the exam guide could yield DIFFERENT correct answers, the generator must either (a) avoid making that delta the deciding line of a question, or (b) frame the question at the level both sources agree on. Deltas below marked **[SAFE]** don't change any plausible answer; deltas marked **[CONFLICT-RISK]** must not be the basis of a scored distinction.

---

## D1 — `allowed-tools` semantics **[CONFLICT-RISK — official exam framing wins]**

- **Official Exam Guide framing (task 3.2 skill bullet, verified in the v0.2 PDF):** "Configuring allowed-tools in skill frontmatter to **restrict tool access** during skill execution (e.g., limiting to file write operations to prevent destructive actions)."
- **Current docs:** `allowed-tools` lists tools Claude can use **without asking permission** when the skill is active — a permission grant; `disallowed-tools` is the restricting key.
- **Source:** source/CCA-F-Official-Exam-Guide.pdf p.14 vs https://code.claude.com/docs/en/skills (both retrieved 2026-07-06)
- **Exam posture:** the exam is authored against the official guide, so a question treating allowed-tools as a restriction mechanism is fair game and the generator SHOULD follow the official framing. Ram should additionally know the current-docs semantics for real-world work, but answer exam questions per the official guide.

## D2 — `stop_reason` value set **[SAFE]**

- **Corpus/guide framing:** four values — `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`.
- **Current docs:** seven — adds `pause_turn` (server-tool loop iteration limit), `refusal`, `model_context_window_exceeded`.
- **Source:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons (retrieved 2026-07-06)
- **Exam posture:** the exam's agentic-loop questions turn on `tool_use` vs `end_turn`, which is unchanged. The three new values are safe extra knowledge; the generator may mention them but must not mark a "four values exist" option as correct.

## D3 — MCP configuration scopes **[SAFE]**

- **Corpus/guide framing:** two scopes — project (`.mcp.json`) and user (`~/.claude.json`).
- **Current docs:** three — adds `local` (the default; also stored in `~/.claude.json` but per-project-private).
- **Source:** https://code.claude.com/docs/en/mcp (retrieved 2026-07-06)
- **Exam posture:** the exam guide tests project-vs-user scoping for team-sharing decisions, which is unchanged. Generator should keep questions at project-vs-user level.

## D4 — CLAUDE.md hierarchy semantics **[CONFLICT-RISK]**

- **Corpus framing (v1):** levels form a "highest → lowest precedence" override hierarchy.
- **Current docs:** discovered CLAUDE.md files are **concatenated into context in load order** (filesystem root down to working directory); they do not override each other. Subdirectory files load on demand.
- **Source:** https://code.claude.com/docs/en/memory (retrieved 2026-07-06)
- **Exam posture:** the official guide tests hierarchy LEVELS and sharing scope (user-level not in version control, etc.), not override mechanics. The generator must not write a question whose correct answer requires "lower level overrides higher level."

## D5 — Message Batches API and tool use **[NUANCE — official framing is precise and current]**

- **Official Exam Guide framing (task 4.5 knowledge bullet + Appendix, v0.2 PDF):** "The batch API does not support multi-turn tool calling **within a single request** (cannot execute tools mid-request and return results)."
- **Current docs:** consistent with that precise reading — batch requests can INCLUDE tool definitions and multi-turn message histories ("almost any request you can make to the Messages API"), but each request is self-contained: your client cannot answer a mid-request tool_use and continue that same batch item. 50% discount and 24h window confirmed current.
- **Source:** source/CCA-F-Official-Exam-Guide.pdf pp.19, 34 vs https://platform.claude.com/docs/en/build-with-claude/batch-processing (both retrieved 2026-07-06)
- **Exam posture:** use the official guide's precise wording ("no multi-turn tool calling within a single request"). The generator must never write the sloppy generalization "batches don't support tool use at all" as a correct answer, and must never mark the official precise claim as incorrect.

## D6 — Slash commands and skills convergence **[SAFE]**

- **Corpus/guide framing:** commands in `.claude/commands/`, skills in `.claude/skills/` as distinct mechanisms.
- **Current docs:** both create the same `/name` invocation and "work the same way"; `.claude/commands/` remains supported, skills are the recommended richer form (supporting files, frontmatter, auto-loading). `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N` substitutions all current.
- **Source:** https://code.claude.com/docs/en/skills (retrieved 2026-07-06)

## D7 — `tool_choice` values **[SAFE, one caveat]**

- Confirmed current: `{"type":"auto"}` (default), `{"type":"any"}`, `{"type":"tool","name":"..."}` — exactly the set the official exam guide names in task 2.3.
- A `none` option appears in some docs surfaces but was not confirmed as a defined `tool_choice` value in the tool-use reference; the generator must not build a question around `none`.
- **Source:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview (retrieved 2026-07-06)

## D8 — CLI structured output **[SAFE]**

- Confirmed current: `--json-schema` flag (print mode, `-p`) returns validated JSON matching a schema; `--output-format json` and `--resume` confirmed as framed in the corpus.
- **Source:** https://code.claude.com/docs/en/cli-reference (retrieved 2026-07-06)

---

## Maintenance

Re-verify this file whenever (a) a mock exam is generated more than 30 days after `Last verified`, or (b) any Anthropic docs-changelog announcement touches skills, MCP, memory, batches, or stop reasons. Add new deltas with the same [SAFE]/[CONFLICT-RISK] tag and source line.

**Last verified: 2026-07-06**
