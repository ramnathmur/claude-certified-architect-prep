# CCA-F Concept Atlas — Plan & Concept Inventory (v1)

**Purpose:** Phase-1 checkpoint for the single-file, globally shareable exam refresher. This document is the
contract the authoring and audit phases build against. Regenerate with `prep with quiz/WIP-ATLAS/write_plan.py`.
**Date:** 2026-08-15 · **Exam:** Claude Certified Architect – Foundations (CCAR-F) · **Deliverable:** `Outputs/CCA-F_Concept-Atlas_v1.html`

## 1. Source of truth

- **Official Exam Guide** (`prep with quiz/source/CCA-F-Official-Exam-Guide_text.txt`, v0.2 text; v1.0 is content-identical for domains, task statements, scenarios and scope) — 5 domains → 30 task statements → **240 Knowledge/Skills bullets**, plus Appendix lists: 14 *Technologies and Concepts*, 18 *In-Scope Topics*, 16 *Out-of-Scope Topics*. `extract_bullets.py` parses every one into an ID (`1.1-K1`, `2.5-S5`, `APP-T7`, `APP-I12`, `APP-O3`) — **288 IDs**.
- **Key Distinctions** (`CCA-Prep_Key-Distinctions_v1.md`, 29 traps) — woven into cards as trap callouts.
- **Depth for authoring:** `CCA-Prep_Domain-1…5_v2.md`, `CCA-Prep_Exam-Mechanics_v2.md`, the 12 official sample questions.
- **Deliberately not sourced:** any mock-exam result, `EXAM-LOG.md`, `GAPS.md`, drill progress — the reader is cold.

## 2. Coverage guarantee (verified, not asserted)

`check_coverage.py` result: **127 cards** (122 concept cards + 5 meta cards) · **288/288 IDs mapped, 0 unmapped, 0 unknown references** · **29/29 Key Distinctions covered**. The gate re-runs before authoring and again in the cold audit against the built HTML.

Cards per domain: D1 25, D2 19, D3 24, D4 24, D5 30. Card count follows the guide's bullet count per domain, not the exam weight — D5 has the most bullets.

## 3. Card contract (what every concept card carries)

| Field | Rule |
|---|---|
| **Concept** | One flat sentence. No setup, no invented misconception to negate. |
| **What is tested** | The question shape the exam uses for it, and the distractor it is paired against (from the official samples / Key Distinctions). |
| **Remember** | The rule, at most two lines; inline code for names, flags and paths. |
| **Visual analogy** | Inline SVG, drawn in the domain's metaphor world (below), one idea per picture, no text under 11 px, stroke-based so it prints. |
| **Real-world analogy** | Two or three sentences set in the same world — the same characters recur across a domain so the pictures reinforce each other. |
| **Cite** | `TS x.y` (+ `KD #n` when a trap is woven in). |

Prose rule for every field: a plain, checkable fact gets one flat sentence; say each idea once; no diagnose-negate-reveal tricolons; no dramatic one-liners.

## 4. Metaphor system — one town, five civic buildings (clean sheet)

The document frame is a town map; each domain is a building on it. Every card's picture and text analogy live inside its building, so a reader can locate a concept by *where it happens*.

| Domain | Building | Why it fits |
|---|---|---|
| D1 Agentic Architecture & Orchestration | **The control tower** | Pilots never talk to each other — everything routes through the tower (hub-and-spoke); a plane on the ground has no idea what happened in the air before it (empty subagent context); clearances vs radio requests (code gates vs prompt guidance); flight strips and hand-overs (sessions, resume, fork). |
| D2 Tool Design & MCP Integration | **The library** | The reference librarian picks a database from its blurb (description = interface); look-alike database names misroute (analyze_content vs analyze_document); the catalogue (MCP resources); institutional subscription vs personal card (.mcp.json vs ~/.claude.json); full-text search vs finding by title (Grep vs Glob). |
| D3 Claude Code Configuration & Workflows | **The office** | Company handbook (project CLAUDE.md), your own sticky notes (user-level), floor notices (directory), cross-referenced binders (@import), rules that apply only on the shop floor (path-scoped rules), playbooks pulled off the shelf (skills), an architect's drawing before knocking a wall down (plan mode), the overnight audit robot (CI with -p). |
| D4 Prompt Engineering & Structured Output | **The courthouse** | Elements of an offence vs "be reasonable" (explicit criteria); precedents (few-shot); the clerk's standard form (schema) that can be filled correctly and still be wrong (semantic errors); the appeal sent back with specific grounds (retry with feedback) that cannot rule on evidence not in the record (retry limits); night-court docket (batch); a fresh judge for the appeal (independent review). |
| D5 Context Management & Reliability | **The hospital ward** | Vitals chart at the foot of the bed survives every shift summary (case-facts block); a negative test is not a failed test (empty result vs access failure); call the consultant on written criteria, not on how the patient sounds (escalation); timestamps on every lab value (temporal data); the chart lets the next doctor resume after a crash (manifests). |

Cover / Start page: the town map with the five buildings; exam facts (M-01…M-05) sit on the map, not in a building.

## 5. Document structure (paged, one file)

Sticky top nav + prev/next; pages: **Start** (how to read, exam at a glance, town map) · **The exam** (format, weights, six scenarios, tie-breakers, will-not-appear) · **D1** · **D2** · **D3** · **D4** · **D5** · **Trap index** (all 29 Key Distinctions, each linking to its card) · **Coverage** (the 30 task statements → cards, so a reader can check nothing is missing). Self-contained: inline CSS/SVG, no fonts or scripts fetched, no localStorage, print stylesheet for PDF export.

## 6. Build pipeline

1. `extract_bullets.py` → `bullets.json` (done). 2. `inventory.py` + `check_coverage.py` (done, PASS). 3. Phase 2: `CARD-SPEC.md` + palette validation + `build_atlas.py` renderer skeleton. 4. Phase 3: five authoring subagents write `items_d1…d5.py` against this inventory (card ids fixed; agents may not add or drop cards without flagging); renderer emits the HTML. 5. Phase 4: blind auditors (official guide + built HTML only) check coverage of all 288 IDs, factual fidelity, prose rules, no personal data, both analogies present per card. 6. Phase 5: browser verification, screenshots, delivery.

## 7. Decisions flagged for the checkpoint

- **Four cards come from the practice test, not the official task statements** (Key Distinctions with no guide bullet): D1-19 two-tool token binding vs `dry_run`; D5-06 behavioural drift vs overflow; D5-07 retrieval vs summarisation for months of history; D5-12 state assumptions vs many clarifying questions. Included by default (the official samples are drawn from that practice test); say the word to drop them.
- **Corpus-only depth not carded** (community guide facts outside the official task statements): `tool_result` carrying `tool_use_id`, prefilling the assistant turn, system prompt as the home of persistent behaviour, bundling requests vs composite tools, the `PreToolUse` name (the guide says "tool call interception" without naming the hook — the card uses the guide's wording and mentions the name). Not carded by default to keep the file to what the exam states it tests.
- **KD #4 vs official wording:** the community guide says a same-name personal skill overrides the project skill; the official guide says to create personal variants *with different names*. The card follows the official framing and notes the community claim.

## 8. Concept inventory

### D1 — Agentic Architecture & Orchestration (27%) · The control tower

| Card | Title | Concept (gist) | Guide bullets | KD | Notes |
|---|---|---|---|---|---|
| D1-01 | The agentic loop runs on stop_reason | Send the request, read stop_reason: tool_use means run the tool and go round again; end_turn means the loop is finished. | 1.1-K1, 1.1-S1 · APP-I1, APP-T5, APP-T1 | #5 |  |
| D1-02 | Tool results are appended to the conversation | Each tool result goes back into the message history so the next iteration can reason over it. | 1.1-K2, 1.1-S2 · APP-I1 |  |  |
| D1-03 | Model-driven decisions, not a hard-coded decision tree | Claude decides which tool to call next from context; a pre-configured tool sequence is not an agent. | 1.1-K3 |  |  |
| D1-04 | Loop-termination anti-patterns | Do not end the loop on parsed text, an iteration cap, or the presence of assistant text — only on stop_reason. | 1.1-S3 · APP-I1 | #5 |  |
| D1-05 | Hub-and-spoke: every message goes through the coordinator | Subagents never talk to each other; the coordinator routes all communication, errors and information. | 1.2-K1, 1.2-S4 · APP-I2 | #6 |  |
| D1-06 | Subagents start with an empty context | A subagent inherits nothing; everything it needs must be written into its prompt. | 1.2-K2, 1.3-K2, 1.3-S1 · APP-I3, APP-T13 |  |  |
| D1-07 | The coordinator decomposes, delegates, aggregates — and chooses | The coordinator breaks the task down, picks which subagents to invoke for this query, and merges results; it does not run the full pipeline every time. | 1.2-K3, 1.2-S1 · APP-I2 |  |  |
| D1-08 | Narrow decomposition leaves coverage gaps | When every subagent succeeds and the answer is still incomplete, the coordinator's decomposition was too narrow. | 1.2-K4 | #7 |  |
| D1-09 | Partition scope so subagents do not duplicate work | Give each subagent a distinct subtopic or source type. | 1.2-S2 |  |  |
| D1-10 | Iterative refinement: evaluate, re-delegate, re-synthesise | The coordinator checks the synthesis for gaps, sends targeted queries back to search/analysis, and re-runs synthesis until coverage is sufficient. | 1.2-S3 · APP-I2 |  |  |
| D1-11 | Task tool + allowedTools includes "Task" | Subagents are spawned with the Task tool; a coordinator whose allowedTools omits "Task" cannot delegate. | 1.3-K1 · APP-T1 |  |  |
| D1-12 | AgentDefinition: description, system prompt, tool restrictions | Each subagent type is configured with a description, its own system prompt and the tools it may use. | 1.3-K3 · APP-T1 |  |  |
| D1-13 | Content and metadata travel in separate fields | Pass findings between agents in structured form so source URLs, document names and page numbers survive. | 1.3-S2 |  | also serves TS 5.6 |
| D1-14 | Parallel subagents = multiple Task calls in ONE response | Emit all Task calls in a single coordinator turn; one per turn is sequential. | 1.3-S3 · APP-I2 |  |  |
| D1-15 | Coordinator prompts state goals and quality criteria, not procedures | Give subagents the research goal and what good looks like; a step-by-step script removes their ability to adapt. | 1.3-S4 |  |  |
| D1-16 | Programmatic enforcement vs prompt guidance | When a sequence must hold (identity check before a refund), enforce it in code — hooks or prerequisite gates — because prompt compliance has a non-zero failure rate. | 1.4-K1, 1.4-K2, 1.4-S1, 1.5-K3, 1.5-S3 | #11 |  |
| D1-17 | Structured handoff to a human | An escalation carries customer ID, root cause, amount and recommended action, because the human cannot see the transcript. | 1.4-K3, 1.4-S3 |  |  |
| D1-18 | Multi-concern requests: split, investigate in parallel, synthesise | Decompose a message with several issues into items, work them in parallel with shared context, then answer once. | 1.4-S2 |  |  |
| D1-19 | Two-tool token binding vs a dry_run flag | A mandatory preview is guaranteed only when the execute tool needs a token that the preview tool issues; a boolean can be skipped. | — | #12 | Practice-test distinction adjacent to TS 1.4/1.5 (enforcement in code). |
| D1-20 | PostToolUse hooks normalise tool results | A PostToolUse hook rewrites heterogeneous formats (Unix timestamps, ISO 8601, numeric codes) before the model sees them. | 1.5-K1, 1.5-S1 · APP-T1 |  |  |
| D1-21 | Intercept outgoing tool calls to block and redirect | A hook on the outgoing call blocks a policy violation (refund over $500) and redirects to escalation. | 1.5-K2, 1.5-S2 · APP-T1 |  |  |
| D1-22 | Prompt chaining vs adaptive decomposition | Fixed sequential chains suit predictable multi-aspect reviews; open-ended investigation needs subtasks generated from what each step finds. | 1.6-K1, 1.6-K3, 1.6-S1, 1.6-S3 · APP-T11 |  |  |
| D1-23 | --resume <session-name> continues a named session | Named sessions let you pick up a specific prior investigation across work sessions. | 1.7-K1, 1.7-S1 · APP-T3, APP-T13 |  |  |
| D1-24 | fork_session branches from a shared baseline | Fork one analysed session into independent branches to compare approaches without re-analysing. | 1.7-K2, 1.7-S2, 1.3-K4 · APP-T3, APP-T13 |  |  |
| D1-25 | Resume, or start fresh with a summary — and say what changed | Resume when prior context is still valid; start a new session with a structured summary when tool results are stale; on resume, name the files that changed. | 1.7-K3, 1.7-K4, 1.7-S3, 1.7-S4 · APP-T13 |  |  |

### D2 — Tool Design & MCP Integration (18%) · The library

| Card | Title | Concept (gist) | Guide bullets | KD | Notes |
|---|---|---|---|---|---|
| D2-01 | The description is the interface | Tool selection runs on descriptions; include input formats, example queries, edge cases and when-to-use boundaries. | 2.1-K1, 2.1-K2, 2.1-S1 · APP-I4, APP-I5, APP-T2 | #10 |  |
| D2-02 | Overlapping descriptions misroute — rename and differentiate | Near-identical descriptions (analyze_content vs analyze_document) cause misrouting; fix by renaming and rewriting for a distinct purpose. | 2.1-K3, 2.1-S2 · APP-I4 | #10 |  |
| D2-03 | Split generic tools into purpose-specific ones | One vague analyze_document becomes extract_data_points, summarize_content, verify_claim_against_source, each with a defined contract. | 2.1-S3 · APP-I4 |  |  |
| D2-04 | Keyword-sensitive system-prompt wording overrides good descriptions | A phrase in the system prompt can bind a tool to a keyword; review the prompt when selection goes wrong despite good descriptions. | 2.1-K4, 2.1-S4 |  |  |
| D2-05 | isError plus structured error metadata | Return isError with errorCategory, isRetryable and a readable message; a generic "Operation failed" gives the agent nothing to decide on. | 2.2-K1, 2.2-K3, 2.2-K4, 2.2-S1 · APP-I7, APP-T2 | #8, #9 |  |
| D2-06 | Four error kinds: transient, validation, business, permission | Each kind gets a different move — retry, fix the input, explain the policy (retriable: false), or ask for access. | 2.2-K2, 2.2-S2 · APP-I7 | #9 |  |
| D2-07 | Fewer tools per agent | Eighteen tools instead of four or five degrades selection; decision complexity is the cost. | 2.3-K1 |  |  |
| D2-08 | Scoped tool sets per role, one cross-role tool for the common case | Give each subagent only its role's tools; when one agent frequently needs another's capability, give it a scoped tool (verify_fact) and route the rare complex cases through the coordinator. | 2.3-K2, 2.3-K3, 2.3-S1, 2.3-S3 · APP-T2 |  |  |
| D2-09 | Constrained alternatives to generic tools | Replace fetch_url with load_document that validates document URLs. | 2.3-S2 |  |  |
| D2-10 | .mcp.json (project, shared) vs ~/.claude.json (user, personal) | Team servers live in the repo's .mcp.json; personal or experimental servers in ~/.claude.json. | 2.4-K1, 2.4-S1, 2.4-S2 · APP-I6, APP-T2 | #2 |  |
| D2-11 | ${ENV_VAR} expansion keeps secrets out of the repo | .mcp.json references ${GITHUB_TOKEN}; each developer supplies their own value. | 2.4-K2, 2.4-S1 · APP-I6, APP-T2 | #2 |  |
| D2-12 | All configured servers' tools are discovered at connection and available together | Multiple MCP servers do not take turns; their tools are all on the table at once. | 2.4-K3 · APP-I6 |  |  |
| D2-13 | MCP resources expose content catalogs | Resources give the agent visibility into issue lists, doc hierarchies or schemas without exploratory tool calls; tools act, resources are read. | 2.4-K4, 2.4-S5 · APP-I5, APP-T2 |  |  |
| D2-14 | It keeps choosing Grep over your MCP tool — fix the description | The agent prefers a familiar built-in unless the MCP tool's description spells out what it can do that Grep cannot. | 2.4-S3 · APP-I5 | #29 |  |
| D2-15 | Community server for standard integrations, custom for your own workflows | Use an existing Jira server; write your own only for team-specific behaviour. | 2.4-S4 |  |  |
| D2-16 | Grep searches inside files; Glob matches paths | Callers, error strings and imports are Grep; **/*.test.tsx is Glob. | 2.5-K1, 2.5-K2, 2.5-S1, 2.5-S2 · APP-T9 | #26 |  |
| D2-17 | Edit needs a unique anchor; otherwise Read + Write | Read/Write handle whole files; Edit replaces by unique text match and fails on duplicates, so fall back to Read then Write. | 2.5-K3, 2.5-K4, 2.5-S3 · APP-T9 | #27 |  |
| D2-18 | Grep first, then Read to trace — never read everything up front | Find entry points by content search, then follow imports with targeted reads. | 2.5-S4 · APP-T9 | #28 |  |
| D2-19 | Tracing through wrappers: list the exports, then search each name | Identify every exported name first, then Grep for each across the codebase. | 2.5-S5 |  |  |

### D3 — Claude Code Configuration & Workflows (20%) · The office

| Card | Title | Concept (gist) | Guide bullets | KD | Notes |
|---|---|---|---|---|---|
| D3-01 | CLAUDE.md hierarchy: user, project, directory | ~/.claude/CLAUDE.md, .claude/CLAUDE.md or root CLAUDE.md, and subdirectory files all load — they stack, they do not replace each other. | 3.1-K1 · APP-I9, APP-T3 |  |  |
| D3-02 | User-level is personal — it never reaches teammates | Instructions in ~/.claude/CLAUDE.md are not version-controlled; a new teammate not receiving them is the diagnostic. | 3.1-K2, 3.1-S1 · APP-I9 | #1 |  |
| D3-03 | @import keeps CLAUDE.md modular | Reference external standards files so each package pulls in only what applies to it. | 3.1-K3, 3.1-S2 · APP-I9 |  |  |
| D3-04 | .claude/rules/ splits a monolith into topic files | testing.md, api-conventions.md, deployment.md instead of one long CLAUDE.md. | 3.1-K4, 3.1-S3 · APP-I9, APP-T3 | #3 |  |
| D3-05 | /memory shows what actually loaded | When behaviour differs between sessions, /memory lists the memory files in force. | 3.1-S4 · APP-T3 |  |  |
| D3-06 | Slash commands: .claude/commands/ ships with the repo, ~/.claude/commands/ is yours | Project commands are version-controlled and available to everyone who clones; user commands are personal. | 3.2-K1, 3.2-S1 · APP-I10, APP-T3 |  |  |
| D3-07 | Skills live in .claude/skills/<name>/SKILL.md with frontmatter | SKILL.md frontmatter supports context: fork, allowed-tools and argument-hint. | 3.2-K2 · APP-I10, APP-T3 |  |  |
| D3-08 | context: fork runs the skill in an isolated sub-agent | Verbose or exploratory skill output stays out of the main conversation. | 3.2-K3, 3.2-S2 · APP-I10 | #13 |  |
| D3-09 | allowed-tools restricts what a skill may do | Frontmatter limits tool access during the skill, e.g. no destructive operations. | 3.2-S3 · APP-I10 |  |  |
| D3-10 | argument-hint prompts for missing parameters | When the skill is invoked without arguments, the hint tells the developer what to supply. | 3.2-S4 · APP-I10 |  |  |
| D3-11 | Personal skill variants without touching the team's | Create a personal variant in ~/.claude/skills/ under a different name so teammates are unaffected. | 3.2-K4 | #4 |  |
| D3-12 | Skills are on-demand; CLAUDE.md is always loaded | Universal standards go in CLAUDE.md; task-specific procedures go in skills invoked when needed. | 3.2-S5 | #3 |  |
| D3-13 | Path-scoped rules: paths: globs in YAML frontmatter | A rule with paths: ["terraform/**/*"] loads only while editing matching files, saving tokens. | 3.3-K1, 3.3-K2, 3.3-S1, 3.3-S2 · APP-I9, APP-T3 | #3 |  |
| D3-14 | Glob rules beat subdirectory CLAUDE.md for conventions spread across the tree | Test files everywhere → **/*.test.tsx rule, not a CLAUDE.md in each folder. | 3.3-K3, 3.3-S3 | #3 |  |
| D3-15 | Plan mode for large, ambiguous or architectural work; direct execution for well-scoped fixes | Plan first for multi-file changes, migrations and design choices; go direct for a single-file fix with a clear stack trace; plan then execute for a migration. | 3.4-K1, 3.4-K2, 3.4-K3, 3.4-S1, 3.4-S2, 3.4-S4 · APP-I11, APP-T3 |  |  |
| D3-16 | The Explore subagent keeps discovery noise out of the main context | Verbose discovery runs in Explore and returns a summary, preserving the main window for multi-phase work. | 3.4-K4, 3.4-S3 · APP-T3 | #22 |  |
| D3-17 | Two or three concrete input/output examples beat more prose | When descriptions are read inconsistently, show the transformation. | 3.5-K1, 3.5-S1 · APP-I12 |  |  |
| D3-18 | Test-driven iteration: write the tests, share the failures | Write the suite (behaviour, edge cases, performance) first, then iterate by feeding back failures; fix an edge case with a specific input/expected-output test. | 3.5-K2, 3.5-S2, 3.5-S4 · APP-I12 |  |  |
| D3-19 | The interview pattern | Have Claude ask questions first so it surfaces cache invalidation, failure modes and other considerations you had not anticipated. | 3.5-K3, 3.5-S3 · APP-I12 |  |  |
| D3-20 | Interacting issues in one message; independent issues one at a time | Batch fixes that affect each other; sequence the ones that do not. | 3.5-K4, 3.5-S5 · APP-I12 |  |  |
| D3-21 | -p / --print runs Claude Code non-interactively | In CI, -p processes the prompt, prints to stdout and exits; without it the job waits for input. | 3.6-K1, 3.6-S1 · APP-T4 | #15 |  |
| D3-22 | --output-format json with --json-schema for machine-readable findings | Structured CI output can be posted as inline PR comments. | 3.6-K2, 3.6-S2 · APP-T4 |  |  |
| D3-23 | CLAUDE.md is how CI Claude learns your standards, fixtures and criteria | Document testing standards, valuable-test criteria and available fixtures so generated tests are worth having. | 3.6-K3, 3.6-S5 |  |  |
| D3-24 | Re-reviews see prior findings; test generation sees existing tests | Include last run's findings and ask for new or unaddressed issues only; include existing test files to avoid duplicate scenarios. | 3.6-S3, 3.6-S4 |  |  |

### D4 — Prompt Engineering & Structured Output (20%) · The courthouse

| Card | Title | Concept (gist) | Guide bullets | KD | Notes |
|---|---|---|---|---|---|
| D4-01 | Explicit categorical criteria beat vague instructions | "Flag a comment only when the claimed behaviour contradicts the code" works; "be conservative" and "only high-confidence findings" do not. | 4.1-K1, 4.1-K2, 4.1-S1 |  |  |
| D4-02 | False positives erode trust — switch off the noisy category while you fix it | A high-false-positive category undermines confidence in the accurate ones; disable it temporarily. | 4.1-K3, 4.1-S2 · APP-I14 |  |  |
| D4-03 | Severity levels defined by concrete code examples | Each level gets example code, so classification is consistent. | 4.1-S3 |  |  |
| D4-04 | Few-shot examples for consistent format when instructions fail | Show the exact output shape (location, issue, severity, fix) instead of writing longer instructions. | 4.2-K1, 4.2-S2 · APP-I14, APP-T10 | #16 |  |
| D4-05 | Aim examples at the ambiguous cases, with the reasoning | Two to four targeted examples that show why one action beat the plausible alternative let the model generalise to new patterns. | 4.2-K2, 4.2-K3, 4.2-S1, 4.2-S3 · APP-I14, APP-T10 | #18 |  |
| D4-06 | Few-shot for extraction across varied documents | Examples of inline citations vs bibliographies, methodology sections vs embedded details, reduce hallucination and fix null required fields. | 4.2-K4, 4.2-S4, 4.2-S5 · APP-T10 |  |  |
| D4-07 | tool_use with a JSON schema is the structured-output guarantee | Define an extraction tool whose input schema is the output you want and read it from the tool_use block; syntax errors disappear. | 4.3-K1, 4.3-S1 · APP-I13, APP-T5, APP-T7 |  |  |
| D4-08 | tool_choice: auto may answer in text, any must call some tool, forced must call this tool | any guarantees a tool call when the document type is unknown; {"type": "tool", "name": ...} guarantees a specific extraction runs first. | 4.3-K2, 4.3-S2, 4.3-S3, 2.3-K4, 2.3-S4, 2.3-S5 · APP-I13, APP-T5 |  | also serves TS 2.3 |
| D4-09 | Schema-valid is not the same as correct | Strict schemas remove syntax errors; line items that do not sum and values in the wrong field are semantic errors that survive. | 4.3-K3, 4.4-K4 · APP-T7, APP-T8 |  |  |
| D4-10 | Nullable fields stop fabrication | Mark fields optional when the source may lack them; a required field forces an invented value. | 4.3-K4, 4.3-S4 · APP-I13, APP-T7 |  |  |
| D4-11 | Enums with "unclear" and "other" + detail | Ambiguous cases get an unclear value; extensible categories get other plus a free-text detail field. | 4.3-K4, 4.3-S5 · APP-T7 |  |  |
| D4-12 | Normalisation rules travel with the schema | Tell the prompt how to normalise inconsistent source formats alongside the strict output schema. | 4.3-S6 |  |  |
| D4-13 | Retry with the specific validation error | Send the original document, the failed extraction and the exact error; the model corrects format and structure faults. | 4.4-K1, 4.4-S1 · APP-T8 |  |  |
| D4-14 | Retry cannot create information that is not in the source | Format mismatches retry well; a value that exists only in a document you did not provide will fail every time. | 4.4-K2, 4.4-S2 |  |  |
| D4-15 | detected_pattern turns dismissals into a feedback loop | Record which code construct triggered each finding so dismissed findings can be analysed for false-positive patterns. | 4.4-K3, 4.4-S3 |  |  |
| D4-16 | Self-checking schema: calculated_total beside stated_total, conflict_detected | Extract both numbers so discrepancies flag themselves; add a boolean for inconsistent source data. | 4.4-S4 |  |  |
| D4-17 | Message Batches API: 50% cheaper, up to 24 hours, no latency SLA | Batch fits overnight reports and weekly audits; blocking pre-merge checks stay synchronous. | 4.5-K1, 4.5-K2, 4.5-S1 · APP-I15, APP-T6 | #14 |  |
| D4-18 | A batch request cannot run a tool loop mid-request | Batches are fire-and-forget; anything that needs tool results returned mid-request stays synchronous. | 4.5-K3 · APP-T6 | #14 |  |
| D4-19 | custom_id correlates results and lets you resubmit only the failures | Identify failed documents by custom_id and resubmit them, chunking the ones that exceeded context. | 4.5-K4, 4.5-S3 · APP-I15, APP-T6 |  |  |
| D4-20 | Submission cadence from the SLA arithmetic | A 30-hour SLA with a 24-hour batch window means submitting every 4 hours or so. | 4.5-S2 · APP-I15 |  |  |
| D4-21 | Refine the prompt on a sample before the big batch | Tune on a small set first so first-pass success is high and resubmission cost low. | 4.5-S4 |  |  |
| D4-22 | An independent instance reviews; the author does not | The session that wrote the code keeps its reasoning and will not question it; a second instance without that context catches more than self-review or extended thinking. | 4.6-K1, 4.6-K2, 4.6-S1, 3.6-K4 |  | also serves TS 3.6 |
| D4-23 | Per-file passes plus a cross-file integration pass | A 14-file single pass dilutes attention and contradicts itself; split into local passes and one integration pass — a bigger context window does not fix it. | 4.6-K3, 4.6-S2, 1.6-K2, 1.6-S2 · APP-T11 | #17 | also serves TS 1.6 |
| D4-24 | Confidence beside each finding routes the review | Have the model self-report confidence per finding so low-confidence items get human attention. | 4.6-S3 |  |  |

### D5 — Context Management & Reliability (15%) · The hospital ward

| Card | Title | Concept (gist) | Guide bullets | KD | Notes |
|---|---|---|---|---|---|
| D5-01 | Summaries blur numbers — keep a case-facts block outside the history | Amounts, dates, order numbers and statuses go into a persistent structured block included in every prompt; summarised history loses them. | 5.1-K1, 5.1-S1, 5.1-S2 · APP-I16, APP-T12 | #21 |  |
| D5-02 | Lost in the middle — summary first, explicit section headers | Models read the start and end of long input reliably; put key findings at the top and label the sections. | 5.1-K2, 5.1-S4 · APP-I16, APP-T12 | #20 |  |
| D5-03 | Trim tool output before it lands in context | Forty fields per order lookup when five matter; keep only the relevant fields. | 5.1-K3, 5.1-S3 · APP-I16, APP-T12 |  |  |
| D5-04 | The API is stateless — send the full history every turn | Claude remembers nothing between requests; coherence comes from the messages array you send. | 5.1-K4 | #25 |  |
| D5-05 | Subagents return structured, metadata-rich output — not prose | Key facts, citations, dates, relevance scores instead of verbose reasoning, so downstream agents with small budgets can synthesise accurately. | 5.1-S5, 5.1-S6 |  |  |
| D5-06 | Behavioural drift is diluted instructions, not overflow | At 2,500 tokens the window is not full; the system prompt's influence is being diluted by accumulated responses. | — | #23 | Practice-test distinction adjacent to TS 5.1. |
| D5-07 | Months of history need retrieval, not summarisation | Specific recall over 85K tokens of past conversation calls for semantic retrieval; progressive summarisation compresses conclusions into abstractions. | — | #24 | Practice-test distinction adjacent to TS 5.1. |
| D5-08 | Escalation triggers: human requested, policy gap, no progress | Escalate when the customer asks for a human, when policy is silent or ambiguous, or when the agent cannot progress — not merely when the case is complex. | 5.2-K1, 5.2-S4 · APP-I8 |  |  |
| D5-09 | Explicit criteria plus few-shot; never sentiment or self-confidence | Escalation calibration comes from written criteria with examples; sentiment scores and self-reported confidence do not track case complexity. | 5.2-K3, 5.2-S1 · APP-I8 |  |  |
| D5-10 | Asked for a human: escalate now. Frustrated: acknowledge and offer | An explicit request is honoured immediately without investigation; frustration on a solvable issue gets acknowledgement plus an offer, escalating only if the customer insists. | 5.2-K2, 5.2-S2, 5.2-S3 · APP-I8 |  |  |
| D5-11 | Two customer matches — ask for one more identifier | Never pick a match by heuristic; request an additional identifier. | 5.2-K4, 5.2-S5 |  |  |
| D5-12 | State reasonable assumptions and proceed; do not fire off four questions | For a vague request, proceed with stated assumptions and invite correction; a wall of clarifying questions drives abandonment, and silent defaults confuse. | — | #19 | Practice-test distinction adjacent to TS 5.2 (ambiguity resolution). |
| D5-13 | Structured error context lets the coordinator recover | Failure type, attempted query, partial results and alternatives; a generic "search unavailable", a silent empty success, or killing the whole workflow are all anti-patterns. | 5.3-K1, 5.3-K3, 5.3-K4, 5.3-S1 · APP-I7 | #8 |  |
| D5-14 | Access failure is not an empty result | A timeout needs a retry decision; zero matches is a successful query — report them differently. | 5.3-K2, 5.3-S2, 2.2-S4 | #9 | also serves TS 2.2 |
| D5-15 | Recover locally first; propagate only what you could not fix, with what you tried | Subagents retry transient failures themselves and escalate the rest with partial results and the attempts made. | 5.3-S3, 2.2-S3 · APP-I7 |  | also serves TS 2.2 |
| D5-16 | Coverage annotations in the synthesis | Mark which findings are well supported and which topic areas have gaps because a source was unavailable. | 5.3-S4 · APP-I18 |  |  |
| D5-17 | Context degradation in long sessions | The model starts giving inconsistent answers and citing "typical patterns" instead of the classes it found earlier. | 5.4-K1 |  |  |
| D5-18 | Scratchpad files persist findings across context boundaries | Agents write key findings to a file and read it back for later questions. | 5.4-K2, 5.4-S2 · APP-T12 |  |  |
| D5-19 | Delegate verbose exploration; the main agent keeps the high-level picture | Spawn subagents for "find all test files" or "trace the refund flow" while the main agent coordinates. | 5.4-K3, 5.4-S1 | #22 |  |
| D5-20 | Summarise a phase before spawning the next | Inject the previous phase's key findings into the next phase's initial context. | 5.4-S3 |  |  |
| D5-21 | Crash recovery: state exports plus a manifest | Each agent writes state to a known location; on resume the coordinator loads the manifest and injects it into prompts. | 5.4-K4, 5.4-S4 · APP-I3 |  |  |
| D5-22 | /compact when discovery output fills the window | Reduce context usage mid-session; note that compaction loses precision, so isolate discovery first where you can. | 5.4-S5 · APP-T3 | #22 |  |
| D5-23 | 97% overall can hide a bad segment — measure by document type and field | Aggregate accuracy masks weak document types or fields; verify every segment before automating high-confidence extractions. | 5.5-K1, 5.5-K4, 5.5-S2 · APP-I17 |  |  |
| D5-24 | Stratified random sampling of high-confidence output | Keep sampling the confident extractions to measure error rate and catch novel patterns. | 5.5-K2, 5.5-S1 · APP-I17, APP-T14 |  |  |
| D5-25 | Field-level confidence, calibrated on labeled data, routes to human review | Have the model output confidence per field, calibrate thresholds on a labeled set, and send low-confidence or contradictory cases to reviewers. | 5.5-K3, 5.5-S3, 5.5-S4 · APP-I17, APP-T14 |  |  |
| D5-26 | Claim-source mappings survive synthesis | Subagents output claim, excerpt, source URL/document; the synthesis agent preserves and merges the mapping instead of compressing it away. | 5.6-K1, 5.6-K2, 5.6-S1 · APP-I18 |  |  |
| D5-27 | Conflicting figures: keep both, attribute both, let the coordinator reconcile | Do not pick a value; annotate the conflict with sources. | 5.6-K3, 5.6-S3 · APP-I18 |  |  |
| D5-28 | Well-established vs contested findings in separate sections | Keep the sources' own characterisations and methodological context. | 5.6-S2 |  |  |
| D5-29 | Dates in every structured output | Publication or collection dates stop temporal differences being read as contradictions. | 5.6-K4, 5.6-S4 · APP-I18 |  |  |
| D5-30 | Render each content type in its natural form | Financial data as tables, news as prose, technical findings as lists. | 5.6-S5 |  |  |

### Meta cards (Start / The exam pages)

| Card | Title | Content |
|---|---|---|
| M-01 | The exam at a glance | 60 questions, 120 minutes, single-answer multiple choice (1 correct + 3 distractors), 4 scenarios drawn from a bank of 6, scaled 100–1,000 with 720 to pass, every question must be answered. |
| M-02 | Five domains and their weights | D1 27%, D2 18%, D3 20%, D4 20%, D5 15%. |
| M-03 | The six scenarios and their primary domains | Customer Support (D1 D2 D5), Code Generation (D3 D5), Multi-Agent Research (D1 D2 D5), Developer Productivity (D2 D3 D1), CI (D3 D4), Structured Data Extraction (D4 D5). |
| M-04 | The tie-breakers the sample answers reward | Root cause over symptom; proportionate first response; code for guarantees, prompts for guidance; least privilege; structured over generic; match the API to the latency; independence for review. |
| M-05 | Will not appear | The sixteen out-of-scope topics. |

## Appendix A — Bullet → card matrix (all 288 IDs)

**TS 1.1 — Design and implement agentic loops for autonomous task execution**

| ID | Official bullet | Card(s) |
|---|---|---|
| 1.1-K1 | The agentic loop lifecycle: sending requests to Claude, inspecting stop_reason ("tool_use" vs "end_turn"), executing requested tools, and returning results for the next iteration | D1-01 |
| 1.1-K2 | How tool results are appended to conversation history so the model can reason about the next action | D1-02 |
| 1.1-K3 | The distinction between model-driven decision-making (Claude reasons about which tool to call next based on context) and pre-configured decision trees or tool sequences | D1-03 |
| 1.1-S1 | Implementing agentic loop control flow that continues when stop_reason is "tool_use" and terminates when stop_reason is "end_turn" | D1-01 |
| 1.1-S2 | Adding tool results to conversation context between iterations so the model can incorporate new information into its reasoning | D1-02 |
| 1.1-S3 | Avoiding anti-patterns such as parsing natural language signals to determine loop termination, setting arbitrary iteration caps as the primary stopping mechanism, or checking for assistant text content as a completion indicator | D1-04 |

**TS 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns**

| ID | Official bullet | Card(s) |
|---|---|---|
| 1.2-K1 | Hub-and-spoke architecture where a coordinator agent manages all inter-subagent communication, error handling, and information routing | D1-05 |
| 1.2-K2 | How subagents operate with isolated context—they do not inherit the coordinator's conversation history automatically | D1-06 |
| 1.2-K3 | The role of the coordinator in task decomposition, delegation, result aggregation, and deciding which subagents to invoke based on query complexity | D1-07 |
| 1.2-K4 | Risks of overly narrow task decomposition by the coordinator, leading to incomplete coverage of broad research topics | D1-08 |
| 1.2-S1 | Designing coordinator agents that analyze query requirements and dynamically select which subagents to invoke rather than always routing through the full pipeline | D1-07 |
| 1.2-S2 | Partitioning research scope across subagents to minimize duplication (e.g., assigning distinct subtopics or source types to each agent) | D1-09 |
| 1.2-S3 | Implementing iterative refinement loops where the coordinator evaluates synthesis output for gaps, re-delegates to search and analysis subagents with targeted queries, and re-invokes synthesis until coverage is sufficient | D1-10 |
| 1.2-S4 | Routing all subagent communication through the coordinator for observability, consistent error handling, and controlled information flow | D1-05 |

**TS 1.3 — Configure subagent invocation, context passing, and spawning**

| ID | Official bullet | Card(s) |
|---|---|---|
| 1.3-K1 | The Task tool as the mechanism for spawning subagents, and the requirement that allowedTools must include "Task" for a coordinator to invoke subagents | D1-11 |
| 1.3-K2 | That subagent context must be explicitly provided in the prompt—subagents do not automatically inherit parent context or share memory between invocations | D1-06 |
| 1.3-K3 | The AgentDefinition configuration including descriptions, system prompts, and tool restrictions for each subagent type | D1-12 |
| 1.3-K4 | Fork-based session management for exploring divergent approaches from a shared analysis baseline | D1-24 |
| 1.3-S1 | Including complete findings from prior agents directly in the subagent's prompt (e.g., passing web search results and document analysis outputs to the synthesis subagent) | D1-06 |
| 1.3-S2 | Using structured data formats to separate content from metadata (source URLs, document names, page numbers) when passing context between agents to preserve attribution | D1-13 |
| 1.3-S3 | Spawning parallel subagents by emitting multiple Task tool calls in a single coordinator response rather than across separate turns | D1-14 |
| 1.3-S4 | Designing coordinator prompts that specify research goals and quality criteria rather than step-by-step procedural instructions, to enable subagent adaptability | D1-15 |

**TS 1.4 — Implement multi-step workflows with enforcement and handoff patterns**

| ID | Official bullet | Card(s) |
|---|---|---|
| 1.4-K1 | The difference between programmatic enforcement (hooks, prerequisite gates) and prompt-based guidance for workflow ordering | D1-16 |
| 1.4-K2 | When deterministic compliance is required (e.g., identity verification before financial operations), prompt instructions alone have a non-zero failure rate | D1-16 |
| 1.4-K3 | Structured handoff protocols for mid-process escalation that include customer details, root cause analysis, and recommended actions | D1-17 |
| 1.4-S1 | Implementing programmatic prerequisites that block downstream tool calls until prerequisite steps have completed (e.g., blocking process_refund until get_customer has returned a verified customer ID) | D1-16 |
| 1.4-S2 | Decomposing multi-concern customer requests into distinct items, then investigating each in parallel using shared context before synthesizing a unified resolution | D1-18 |
| 1.4-S3 | Compiling structured handoff summaries (customer ID, root cause, refund amount, recommended action) when escalating to human agents who lack access to the conversation transcript | D1-17 |

**TS 1.5 — Apply Agent SDK hooks for tool call interception and data normalization**

| ID | Official bullet | Card(s) |
|---|---|---|
| 1.5-K1 | Hook patterns (e.g., PostToolUse) that intercept tool results for transformation before the model processes them | D1-20 |
| 1.5-K2 | Hook patterns that intercept outgoing tool calls to enforce compliance rules (e.g., blocking refunds above a threshold) | D1-21 |
| 1.5-K3 | The distinction between using hooks for deterministic guarantees versus relying on prompt instructions for probabilistic compliance | D1-16 |
| 1.5-S1 | Implementing PostToolUse hooks to normalize heterogeneous data formats (Unix timestamps, ISO 8601, numeric status codes) from different MCP tools before the agent processes them | D1-20 |
| 1.5-S2 | Implementing tool call interception hooks that block policy-violating actions (e.g., refunds exceeding $500) and redirect to alternative workflows (e.g., human escalation) | D1-21 |
| 1.5-S3 | Choosing hooks over prompt-based enforcement when business rules require guaranteed compliance | D1-16 |

**TS 1.6 — Design task decomposition strategies for complex workflows**

| ID | Official bullet | Card(s) |
|---|---|---|
| 1.6-K1 | When to use fixed sequential pipelines (prompt chaining) versus dynamic adaptive decomposition based on intermediate findings | D1-22 |
| 1.6-K2 | Prompt chaining patterns that break reviews into sequential steps (e.g., analyze each file individually, then run a cross-file integration pass) | D4-23 |
| 1.6-K3 | The value of adaptive investigation plans that generate subtasks based on what is discovered at each step | D1-22 |
| 1.6-S1 | Selecting task decomposition patterns appropriate to the workflow: prompt chaining for predictable multi-aspect reviews, dynamic decomposition for open-ended investigation tasks | D1-22 |
| 1.6-S2 | Splitting large code reviews into per-file local analysis passes plus a separate cross-file integration pass to avoid attention dilution | D4-23 |
| 1.6-S3 | Decomposing open-ended tasks (e.g., "add comprehensive tests to a legacy codebase") by first mapping structure, identifying high-impact areas, then creating a prioritized plan that adapts as dependencies are discovered | D1-22 |

**TS 1.7 — Manage session state, resumption, and forking**

| ID | Official bullet | Card(s) |
|---|---|---|
| 1.7-K1 | Named session resumption using --resume <session-name> to continue a specific prior conversation | D1-23 |
| 1.7-K2 | fork_session for creating independent branches from a shared analysis baseline to explore divergent approaches | D1-24 |
| 1.7-K3 | The importance of informing the agent about changes to previously analyzed files when resuming sessions after code modifications | D1-25 |
| 1.7-K4 | Why starting a new session with a structured summary is more reliable than resuming with stale tool results | D1-25 |
| 1.7-S1 | Using --resume with session names to continue named investigation sessions across work sessions | D1-23 |
| 1.7-S2 | Using fork_session to create parallel exploration branches (e.g., comparing two testing strategies or refactoring approaches from a shared codebase analysis) | D1-24 |
| 1.7-S3 | Choosing between session resumption (when prior context is mostly valid) and starting fresh with injected summaries (when prior tool results are stale) | D1-25 |
| 1.7-S4 | Informing a resumed session about specific file changes for targeted re-analysis rather than requiring full re-exploration | D1-25 |

**TS 2.1 — Design effective tool interfaces with clear descriptions and boundaries**

| ID | Official bullet | Card(s) |
|---|---|---|
| 2.1-K1 | Tool descriptions as the primary mechanism LLMs use for tool selection; minimal descriptions lead to unreliable selection among similar tools | D2-01 |
| 2.1-K2 | The importance of including input formats, example queries, edge cases, and boundary explanations in tool descriptions | D2-01 |
| 2.1-K3 | How ambiguous or overlapping tool descriptions cause misrouting (e.g., analyze_content vs analyze_document with near-identical descriptions) | D2-02 |
| 2.1-K4 | The impact of system prompt wording on tool selection: keyword-sensitive instructions can create unintended tool associations | D2-04 |
| 2.1-S1 | Writing tool descriptions that clearly differentiate each tool's purpose, expected inputs, outputs, and when to use it versus similar alternatives | D2-01 |
| 2.1-S2 | Renaming tools and updating descriptions to eliminate functional overlap (e.g., renaming analyze_content to extract_web_results with a web-specific description) | D2-02 |
| 2.1-S3 | Splitting generic tools into purpose-specific tools with defined input/output contracts (e.g., splitting a generic analyze_document into extract_data_points, summarize_content, and verify_claim_against_source) | D2-03 |
| 2.1-S4 | Reviewing system prompts for keyword-sensitive instructions that might override well-written tool descriptions | D2-04 |

**TS 2.2 — Implement structured error responses for MCP tools**

| ID | Official bullet | Card(s) |
|---|---|---|
| 2.2-K1 | The MCP isError flag pattern for communicating tool failures back to the agent | D2-05 |
| 2.2-K2 | The distinction between transient errors (timeouts, service unavailability), validation errors (invalid input), business errors (policy violations), and permission errors | D2-06 |
| 2.2-K3 | Why uniform error responses (generic "Operation failed") prevent the agent from making appropriate recovery decisions | D2-05 |
| 2.2-K4 | The difference between retryable and non-retryable errors, and how returning structured metadata prevents wasted retry attempts | D2-05 |
| 2.2-S1 | Returning structured error metadata including errorCategory (transient/validation/permission), isRetryable boolean, and human-readable descriptions | D2-05 |
| 2.2-S2 | Including retriable: false flags and customer-friendly explanations for business rule violations so the agent can communicate appropriately | D2-06 |
| 2.2-S3 | Implementing local error recovery within subagents for transient failures, propagating to the coordinator only errors that cannot be resolved locally along with partial results and what was attempted | D5-15 |
| 2.2-S4 | Distinguishing between access failures (needing retry decisions) and valid empty results (representing successful queries with no matches) | D5-14 |

**TS 2.3 — Distribute tools appropriately across agents and configure tool choice**

| ID | Official bullet | Card(s) |
|---|---|---|
| 2.3-K1 | The principle that giving an agent access to too many tools (e.g., 18 instead of 4-5) degrades tool selection reliability by increasing decision complexity | D2-07 |
| 2.3-K2 | Why agents with tools outside their specialization tend to misuse them (e.g., a synthesis agent attempting web searches) | D2-08 |
| 2.3-K3 | Scoped tool access: giving agents only the tools needed for their role, with limited cross-role tools for specific high-frequency needs | D2-08 |
| 2.3-K4 | tool_choice configuration options: "auto", "any", and forced tool selection ({"type": "tool", "name": "..."}) | D4-08 |
| 2.3-S1 | Restricting each subagent's tool set to those relevant to its role, preventing cross-specialization misuse | D2-08 |
| 2.3-S2 | Replacing generic tools with constrained alternatives (e.g., replacing fetch_url with load_document that validates document URLs) | D2-09 |
| 2.3-S3 | Providing scoped cross-role tools for high-frequency needs (e.g., a verify_fact tool for the synthesis agent) while routing complex cases through the coordinator | D2-08 |
| 2.3-S4 | Using tool_choice forced selection to ensure a specific tool is called first (e.g., forcing extract_metadata before enrichment tools), then processing subsequent steps in follow-up turns | D4-08 |
| 2.3-S5 | Setting tool_choice: "any" to guarantee the model calls a tool rather than returning conversational text | D4-08 |

**TS 2.4 — Integrate MCP servers into Claude Code and agent workflows**

| ID | Official bullet | Card(s) |
|---|---|---|
| 2.4-K1 | MCP server scoping: project-level (.mcp.json) for shared team tooling vs user-level (~/.claude.json) for personal/experimental servers | D2-10 |
| 2.4-K2 | Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) for credential management without committing secrets | D2-11 |
| 2.4-K3 | That tools from all configured MCP servers are discovered at connection time and available simultaneously to the agent | D2-12 |
| 2.4-K4 | MCP resources as a mechanism for exposing content catalogs (e.g., issue summaries, documentation hierarchies, database schemas) to reduce exploratory tool calls | D2-13 |
| 2.4-S1 | Configuring shared MCP servers in project-scoped .mcp.json with environment variable expansion for authentication tokens | D2-10, D2-11 |
| 2.4-S2 | Configuring personal/experimental MCP servers in user-scoped ~/.claude.json | D2-10 |
| 2.4-S3 | Enhancing MCP tool descriptions to explain capabilities and outputs in detail, preventing the agent from preferring built-in tools (like Grep) over more capable MCP tools | D2-14 |
| 2.4-S4 | Choosing existing community MCP servers over custom implementations for standard integrations (e.g., Jira), reserving custom servers for team-specific workflows | D2-15 |
| 2.4-S5 | Exposing content catalogs as MCP resources to give agents visibility into available data without requiring exploratory tool calls | D2-13 |

**TS 2.5 — Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively**

| ID | Official bullet | Card(s) |
|---|---|---|
| 2.5-K1 | Grep for content search (searching file contents for patterns like function names, error messages, or import statements) | D2-16 |
| 2.5-K2 | Glob for file path pattern matching (finding files by name or extension patterns) | D2-16 |
| 2.5-K3 | Read/Write for full file operations; Edit for targeted modifications using unique text matching | D2-17 |
| 2.5-K4 | When Edit fails due to non-unique text matches, using Read + Write as a fallback for reliable file modifications | D2-17 |
| 2.5-S1 | Selecting Grep for searching code content across a codebase (e.g., finding all callers of a function, locating error messages) | D2-16 |
| 2.5-S2 | Selecting Glob for finding files matching naming patterns (e.g., **/*.test.tsx) | D2-16 |
| 2.5-S3 | Using Read to load full file contents followed by Write when Edit cannot find unique anchor text | D2-17 |
| 2.5-S4 | Building codebase understanding incrementally: starting with Grep to find entry points, then using Read to follow imports and trace flows, rather than reading all files upfront | D2-18 |
| 2.5-S5 | Tracing function usage across wrapper modules by first identifying all exported names, then searching for each name across the codebase | D2-19 |

**TS 3.1 — Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization**

| ID | Official bullet | Card(s) |
|---|---|---|
| 3.1-K1 | The CLAUDE.md configuration hierarchy: user-level (~/.claude/CLAUDE.md), project-level (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files) | D3-01 |
| 3.1-K2 | That user-level settings apply only to that user—instructions in ~/.claude/CLAUDE.md are not shared with teammates via version control | D3-02 |
| 3.1-K3 | The @import syntax for referencing external files to keep CLAUDE.md modular (e.g., importing specific standards files relevant to each package) | D3-03 |
| 3.1-K4 | .claude/rules/ directory for organizing topic-specific rule files as an alternative to a monolithic CLAUDE.md | D3-04 |
| 3.1-S1 | Diagnosing configuration hierarchy issues (e.g., a new team member not receiving instructions because they're in user-level rather than project-level configuration) | D3-02 |
| 3.1-S2 | Using @import to selectively include relevant standards files in each package's CLAUDE.md based on maintainer domain knowledge | D3-03 |
| 3.1-S3 | Splitting large CLAUDE.md files into focused topic-specific files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md) | D3-04 |
| 3.1-S4 | Using the /memory command to verify which memory files are loaded and diagnose inconsistent behavior across sessions | D3-05 |

**TS 3.2 — Create and configure custom slash commands and skills**

| ID | Official bullet | Card(s) |
|---|---|---|
| 3.2-K1 | Project-scoped commands in .claude/commands/ (shared via version control) vs user-scoped commands in ~/.claude/commands/ (personal) | D3-06 |
| 3.2-K2 | Skills in .claude/skills/ with SKILL.md files that support frontmatter configuration including context: fork, allowed-tools, and argument-hint | D3-07 |
| 3.2-K3 | The context: fork frontmatter option for running skills in an isolated sub-agent context, preventing skill outputs from polluting the main conversation | D3-08 |
| 3.2-K4 | Personal skill customization: creating personal variants in ~/.claude/skills/ with different names to avoid affecting teammates | D3-11 |
| 3.2-S1 | Creating project-scoped slash commands in .claude/commands/ for team-wide availability via version control | D3-06 |
| 3.2-S2 | Using context: fork to isolate skills that produce verbose output (e.g., codebase analysis) or exploratory context (e.g., brainstorming alternatives) from the main session | D3-08 |
| 3.2-S3 | Configuring allowed-tools in skill frontmatter to restrict tool access during skill execution (e.g., limiting to file write operations to prevent destructive actions) | D3-09 |
| 3.2-S4 | Using argument-hint frontmatter to prompt developers for required parameters when they invoke the skill without arguments | D3-10 |
| 3.2-S5 | Choosing between skills (on-demand invocation for task-specific workflows) and CLAUDE.md (always-loaded universal standards) | D3-12 |

**TS 3.3 — Apply path-specific rules for conditional convention loading**

| ID | Official bullet | Card(s) |
|---|---|---|
| 3.3-K1 | .claude/rules/ files with YAML frontmatter paths fields containing glob patterns for conditional rule activation | D3-13 |
| 3.3-K2 | How path-scoped rules load only when editing matching files, reducing irrelevant context and token usage | D3-13 |
| 3.3-K3 | The advantage of glob-pattern rules over directory-level CLAUDE.md files for conventions that span multiple directories (e.g., test files spread throughout a codebase) | D3-14 |
| 3.3-S1 | Creating .claude/rules/ files with YAML frontmatter path scoping (e.g., paths: ["terraform/**/*"]) so rules load only when editing matching files | D3-13 |
| 3.3-S2 | Using glob patterns in path-specific rules to apply conventions to files by type regardless of directory location (e.g., **/*.test.tsx for all test files) | D3-13 |
| 3.3-S3 | Choosing path-specific rules over subdirectory CLAUDE.md files when conventions must apply to files spread across the codebase | D3-14 |

**TS 3.4 — Determine when to use plan mode vs direct execution**

| ID | Official bullet | Card(s) |
|---|---|---|
| 3.4-K1 | Plan mode is designed for complex tasks involving large-scale changes, multiple valid approaches, architectural decisions, and multi-file modifications | D3-15 |
| 3.4-K2 | Direct execution is appropriate for simple, well-scoped changes (e.g., adding a single validation check to one function) | D3-15 |
| 3.4-K3 | Plan mode enables safe codebase exploration and design before committing to changes, preventing costly rework | D3-15 |
| 3.4-K4 | The Explore subagent for isolating verbose discovery output and returning summaries to preserve main conversation context | D3-16 |
| 3.4-S1 | Selecting plan mode for tasks with architectural implications (e.g., microservice restructuring, library migrations affecting 45+ files, choosing between integration approaches with different infrastructure requirements) | D3-15 |
| 3.4-S2 | Selecting direct execution for well-understood changes with clear scope (e.g., a single-file bug fix with a clear stack trace, adding a date validation conditional) | D3-15 |
| 3.4-S3 | Using the Explore subagent for verbose discovery phases to prevent context window exhaustion during multi-phase tasks | D3-16 |
| 3.4-S4 | Combining plan mode for investigation with direct execution for implementation (e.g., planning a library migration, then executing the planned approach) | D3-15 |

**TS 3.5 — Apply iterative refinement techniques for progressive improvement**

| ID | Official bullet | Card(s) |
|---|---|---|
| 3.5-K1 | Concrete input/output examples as the most effective way to communicate expected transformations when prose descriptions are interpreted inconsistently | D3-17 |
| 3.5-K2 | Test-driven iteration: writing test suites first, then iterating by sharing test failures to guide progressive improvement | D3-18 |
| 3.5-K3 | The interview pattern: having Claude ask questions to surface considerations the developer may not have anticipated before implementing | D3-19 |
| 3.5-K4 | When to provide all issues in a single message (interacting problems) versus fixing them sequentially (independent problems) | D3-20 |
| 3.5-S1 | Providing 2-3 concrete input/output examples to clarify transformation requirements when natural language descriptions produce inconsistent results | D3-17 |
| 3.5-S2 | Writing test suites covering expected behavior, edge cases, and performance requirements before implementation, then iterating by sharing test failures | D3-18 |
| 3.5-S3 | Using the interview pattern to surface design considerations (e.g., cache invalidation strategies, failure modes) before implementing solutions in unfamiliar domains | D3-19 |
| 3.5-S4 | Providing specific test cases with example input and expected output to fix edge case handling (e.g., null values in migration scripts) | D3-18 |
| 3.5-S5 | Addressing multiple interacting issues in a single detailed message when fixes interact, versus sequential iteration for independent issues | D3-20 |

**TS 3.6 — Integrate Claude Code into CI/CD pipelines**

| ID | Official bullet | Card(s) |
|---|---|---|
| 3.6-K1 | The -p (or --print) flag for running Claude Code in non-interactive mode in automated pipelines | D3-21 |
| 3.6-K2 | --output-format json and --json-schema CLI flags for enforcing structured output in CI contexts | D3-22 |
| 3.6-K3 | CLAUDE.md as the mechanism for providing project context (testing standards, fixture conventions, review criteria) to CI-invoked Claude Code | D3-23 |
| 3.6-K4 | Session context isolation: why the same Claude session that generated code is less effective at reviewing its own changes compared to an independent review instance | D4-22 |
| 3.6-S1 | Running Claude Code in CI with the -p flag to prevent interactive input hangs | D3-21 |
| 3.6-S2 | Using --output-format json with --json-schema to produce machine-parseable structured findings for automated posting as inline PR comments | D3-22 |
| 3.6-S3 | Including prior review findings in context when re-running reviews after new commits, instructing Claude to report only new or still-unaddressed issues to avoid duplicate comments | D3-24 |
| 3.6-S4 | Providing existing test files in context so test generation avoids suggesting duplicate scenarios already covered by the test suite | D3-24 |
| 3.6-S5 | Documenting testing standards, valuable test criteria, and available fixtures in CLAUDE.md to improve test generation quality and reduce low-value test output | D3-23 |

**TS 4.1 — Design prompts with explicit criteria to improve precision and reduce false positives**

| ID | Official bullet | Card(s) |
|---|---|---|
| 4.1-K1 | The importance of explicit criteria over vague instructions (e.g., "flag comments only when claimed behavior contradicts actual code behavior" vs "check that comments are accurate") | D4-01 |
| 4.1-K2 | How general instructions like "be conservative" or "only report high-confidence findings" fail to improve precision compared to specific categorical criteria | D4-01 |
| 4.1-K3 | The impact of false positive rates on developer trust: high false positive categories undermine confidence in accurate categories | D4-02 |
| 4.1-S1 | Writing specific review criteria that define which issues to report (bugs, security) versus skip (minor style, local patterns) rather than relying on confidence-based filtering | D4-01 |
| 4.1-S2 | Temporarily disabling high false-positive categories to restore developer trust while improving prompts for those categories | D4-02 |
| 4.1-S3 | Defining explicit severity criteria with concrete code examples for each severity level to achieve consistent classification | D4-03 |

**TS 4.2 — Apply few-shot prompting to improve output consistency and quality**

| ID | Official bullet | Card(s) |
|---|---|---|
| 4.2-K1 | Few-shot examples as the most effective technique for achieving consistently formatted, actionable output when detailed instructions alone produce inconsistent results | D4-04 |
| 4.2-K2 | The role of few-shot examples in demonstrating ambiguous-case handling (e.g., tool selection for ambiguous requests, branch-level test coverage gaps) | D4-05 |
| 4.2-K3 | How few-shot examples enable the model to generalize judgment to novel patterns rather than matching only pre-specified cases | D4-05 |
| 4.2-K4 | The effectiveness of few-shot examples for reducing hallucination in extraction tasks (e.g., handling informal measurements, varied document structures) | D4-06 |
| 4.2-S1 | Creating 2-4 targeted few-shot examples for ambiguous scenarios that show reasoning for why one action was chosen over plausible alternatives | D4-05 |
| 4.2-S2 | Including few-shot examples that demonstrate specific desired output format (location, issue, severity, suggested fix) to achieve consistency | D4-04 |
| 4.2-S3 | Providing few-shot examples distinguishing acceptable code patterns from genuine issues to reduce false positives while enabling generalization | D4-05 |
| 4.2-S4 | Using few-shot examples to demonstrate correct handling of varied document structures (inline citations vs bibliographies, methodology sections vs embedded details) | D4-06 |
| 4.2-S5 | Adding few-shot examples showing correct extraction from documents with varied formats to address empty/null extraction of required fields | D4-06 |

**TS 4.3 — Enforce structured output using tool use and JSON schemas**

| ID | Official bullet | Card(s) |
|---|---|---|
| 4.3-K1 | Tool use (tool_use) with JSON schemas as the most reliable approach for guaranteed schema-compliant structured output, eliminating JSON syntax errors | D4-07 |
| 4.3-K2 | The distinction between tool_choice: "auto" (model may return text instead of calling a tool), "any" (model must call a tool but can choose which), and forced tool selection (model must call a specific named tool) | D4-08 |
| 4.3-K3 | That strict JSON schemas via tool use eliminate syntax errors but do not prevent semantic errors (e.g., line items that don't sum to total, values in wrong fields) | D4-09 |
| 4.3-K4 | Schema design considerations: required vs optional fields, enum fields with "other" + detail string patterns for extensible categories | D4-10, D4-11 |
| 4.3-S1 | Defining extraction tools with JSON schemas as input parameters and extracting structured data from the tool_use response | D4-07 |
| 4.3-S2 | Setting tool_choice: "any" to guarantee structured output when multiple extraction schemas exist and the document type is unknown | D4-08 |
| 4.3-S3 | Forcing a specific tool with tool_choice: {"type": "tool", "name": "extract_metadata"} to ensure a particular extraction runs before enrichment steps | D4-08 |
| 4.3-S4 | Designing schema fields as optional (nullable) when source documents may not contain the information, preventing the model from fabricating values to satisfy required fields | D4-10 |
| 4.3-S5 | Adding enum values like "unclear" for ambiguous cases and "other" + detail fields for extensible categorization | D4-11 |
| 4.3-S6 | Including format normalization rules in prompts alongside strict output schemas to handle inconsistent source formatting | D4-12 |

**TS 4.4 — Implement validation, retry, and feedback loops for extraction quality**

| ID | Official bullet | Card(s) |
|---|---|---|
| 4.4-K1 | Retry-with-error-feedback: appending specific validation errors to the prompt on retry to guide the model toward correction | D4-13 |
| 4.4-K2 | The limits of retry: retries are ineffective when the required information is simply absent from the source document (vs format or structural errors) | D4-14 |
| 4.4-K3 | Feedback loop design: tracking which code constructs trigger findings (detected_pattern field) to enable systematic analysis of dismissal patterns | D4-15 |
| 4.4-K4 | The difference between semantic validation errors (values don't sum, wrong field placement) and schema syntax errors (eliminated by tool use) | D4-09 |
| 4.4-S1 | Implementing follow-up requests that include the original document, the failed extraction, and specific validation errors for model self-correction | D4-13 |
| 4.4-S2 | Identifying when retries will be ineffective (e.g., information exists only in an external document not provided) versus when they will succeed (format mismatches, structural output errors) | D4-14 |
| 4.4-S3 | Adding detected_pattern fields to structured findings to enable analysis of false positive patterns when developers dismiss findings | D4-15 |
| 4.4-S4 | Designing self-correction validation flows: extracting "calculated_total" alongside "stated_total" to flag discrepancies, adding "conflict_detected" booleans for inconsistent source data | D4-16 |

**TS 4.5 — Design efficient batch processing strategies**

| ID | Official bullet | Card(s) |
|---|---|---|
| 4.5-K1 | The Message Batches API: 50% cost savings, up to 24-hour processing window, no guaranteed latency SLA | D4-17 |
| 4.5-K2 | Batch processing is appropriate for non-blocking, latency-tolerant workloads (overnight reports, weekly audits, nightly test generation) and inappropriate for blocking workflows (pre-merge checks) | D4-17 |
| 4.5-K3 | The batch API does not support multi-turn tool calling within a single request (cannot execute tools mid-request and return results) | D4-18 |
| 4.5-K4 | custom_id fields for correlating batch request/response pairs | D4-19 |
| 4.5-S1 | Matching API approach to workflow latency requirements: synchronous API for blocking pre-merge checks, batch API for overnight/weekly analysis | D4-17 |
| 4.5-S2 | Calculating batch submission frequency based on SLA constraints (e.g., 4-hour windows to guarantee 30-hour SLA with 24-hour batch processing) | D4-20 |
| 4.5-S3 | Handling batch failures: resubmitting only failed documents (identified by custom_id) with appropriate modifications (e.g., chunking documents that exceeded context limits) | D4-19 |
| 4.5-S4 | Using prompt refinement on a sample set before batch-processing large volumes to maximize first-pass success rates and reduce iterative resubmission costs | D4-21 |

**TS 4.6 — Design multi-instance and multi-pass review architectures**

| ID | Official bullet | Card(s) |
|---|---|---|
| 4.6-K1 | Self-review limitations: a model retains reasoning context from generation, making it less likely to question its own decisions in the same session | D4-22 |
| 4.6-K2 | Independent review instances (without prior reasoning context) are more effective at catching subtle issues than self-review instructions or extended thinking | D4-22 |
| 4.6-K3 | Multi-pass review: splitting large reviews into per-file local analysis passes plus cross-file integration passes to avoid attention dilution and contradictory findings | D4-23 |
| 4.6-S1 | Using a second independent Claude instance to review generated code without the generator's reasoning context | D4-22 |
| 4.6-S2 | Splitting large multi-file reviews into focused per-file passes for local issues plus separate integration passes for cross-file data flow analysis | D4-23 |
| 4.6-S3 | Running verification passes where the model self-reports confidence alongside each finding to enable calibrated review routing | D4-24 |

**TS 5.1 — Manage conversation context to preserve critical information across long interactions**

| ID | Official bullet | Card(s) |
|---|---|---|
| 5.1-K1 | Progressive summarization risks: condensing numerical values, percentages, dates, and customer-stated expectations into vague summaries | D5-01 |
| 5.1-K2 | The "lost in the middle" effect: models reliably process information at the beginning and end of long inputs but may omit findings from middle sections | D5-02 |
| 5.1-K3 | How tool results accumulate in context and consume tokens disproportionately to their relevance (e.g., 40+ fields per order lookup when only 5 are relevant) | D5-03 |
| 5.1-K4 | The importance of passing complete conversation history in subsequent API requests to maintain conversational coherence | D5-04 |
| 5.1-S1 | Extracting transactional facts (amounts, dates, order numbers, statuses) into a persistent "case facts" block included in each prompt, outside summarized history | D5-01 |
| 5.1-S2 | Extracting and persisting structured issue data (order IDs, amounts, statuses) into a separate context layer for multi-issue sessions | D5-01 |
| 5.1-S3 | Trimming verbose tool outputs to only relevant fields before they accumulate in context (e.g., keeping only return-relevant fields from order lookups) | D5-03 |
| 5.1-S4 | Placing key findings summaries at the beginning of aggregated inputs and organizing detailed results with explicit section headers to mitigate position effects | D5-02 |
| 5.1-S5 | Requiring subagents to include metadata (dates, source locations, methodological context) in structured outputs to support accurate downstream synthesis | D5-05 |
| 5.1-S6 | Modifying upstream agents to return structured data (key facts, citations, relevance scores) instead of verbose content and reasoning chains when downstream agents have limited context budgets | D5-05 |

**TS 5.2 — Design effective escalation and ambiguity resolution patterns**

| ID | Official bullet | Card(s) |
|---|---|---|
| 5.2-K1 | Appropriate escalation triggers: customer requests for a human, policy exceptions/gaps (not just complex cases), and inability to make meaningful progress | D5-08 |
| 5.2-K2 | The distinction between escalating immediately when a customer explicitly demands it versus offering to resolve when the issue is straightforward | D5-10 |
| 5.2-K3 | Why sentiment-based escalation and self-reported confidence scores are unreliable proxies for actual case complexity | D5-09 |
| 5.2-K4 | How multiple customer matches require clarification (requesting additional identifiers) rather than heuristic selection | D5-11 |
| 5.2-S1 | Adding explicit escalation criteria with few-shot examples to the system prompt demonstrating when to escalate versus resolve autonomously | D5-09 |
| 5.2-S2 | Honoring explicit customer requests for human agents immediately without first attempting investigation | D5-10 |
| 5.2-S3 | Acknowledging frustration while offering resolution when the issue is within the agent's capability, escalating only if the customer reiterates their preference | D5-10 |
| 5.2-S4 | Escalating when policy is ambiguous or silent on the customer's specific request (e.g., competitor price matching when policy only addresses own-site adjustments) | D5-08 |
| 5.2-S5 | Instructing the agent to ask for additional identifiers when tool results return multiple matches, rather than selecting based on heuristics | D5-11 |

**TS 5.3 — Implement error propagation strategies across multi-agent systems**

| ID | Official bullet | Card(s) |
|---|---|---|
| 5.3-K1 | Structured error context (failure type, attempted query, partial results, alternative approaches) as enabling intelligent coordinator recovery decisions | D5-13 |
| 5.3-K2 | The distinction between access failures (timeouts needing retry decisions) and valid empty results (successful queries with no matches) | D5-14 |
| 5.3-K3 | Why generic error statuses ("search unavailable") hide valuable context from the coordinator | D5-13 |
| 5.3-K4 | Why silently suppressing errors (returning empty results as success) or terminating entire workflows on single failures are both anti-patterns | D5-13 |
| 5.3-S1 | Returning structured error context including failure type, what was attempted, partial results, and potential alternatives to enable coordinator recovery | D5-13 |
| 5.3-S2 | Distinguishing access failures from valid empty results in error reporting so the coordinator can make appropriate decisions | D5-14 |
| 5.3-S3 | Having subagents implement local recovery for transient failures and only propagate errors they cannot resolve, including what was attempted and partial results | D5-15 |
| 5.3-S4 | Structuring synthesis output with coverage annotations indicating which findings are well-supported versus which topic areas have gaps due to unavailable sources | D5-16 |

**TS 5.4 — Manage context effectively in large codebase exploration**

| ID | Official bullet | Card(s) |
|---|---|---|
| 5.4-K1 | Context degradation in extended sessions: models start giving inconsistent answers and referencing "typical patterns" rather than specific classes discovered earlier | D5-17 |
| 5.4-K2 | The role of scratchpad files for persisting key findings across context boundaries | D5-18 |
| 5.4-K3 | Subagent delegation for isolating verbose exploration output while the main agent coordinates high-level understanding | D5-19 |
| 5.4-K4 | Structured state persistence for crash recovery: each agent exports state to a known location, and the coordinator loads a manifest on resume | D5-21 |
| 5.4-S1 | Spawning subagents to investigate specific questions (e.g., "find all test files," "trace refund flow dependencies") while the main agent preserves high-level coordination | D5-19 |
| 5.4-S2 | Having agents maintain scratchpad files recording key findings, referencing them for subsequent questions to counteract context degradation | D5-18 |
| 5.4-S3 | Summarizing key findings from one exploration phase before spawning sub-agents for the next phase, injecting summaries into initial context | D5-20 |
| 5.4-S4 | Designing crash recovery using structured agent state exports (manifests) that the coordinator loads on resume and injects into agent prompts | D5-21 |
| 5.4-S5 | Using /compact to reduce context usage during extended exploration sessions when context fills with verbose discovery output | D5-22 |

**TS 5.5 — Design human review workflows and confidence calibration**

| ID | Official bullet | Card(s) |
|---|---|---|
| 5.5-K1 | The risk that aggregate accuracy metrics (e.g., 97% overall) may mask poor performance on specific document types or fields | D5-23 |
| 5.5-K2 | Stratified random sampling for measuring error rates in high-confidence extractions and detecting novel error patterns | D5-24 |
| 5.5-K3 | Field-level confidence scores calibrated using labeled validation sets for routing review attention | D5-25 |
| 5.5-K4 | The importance of validating accuracy by document type and field segment before automating high-confidence extractions | D5-23 |
| 5.5-S1 | Implementing stratified random sampling of high-confidence extractions for ongoing error rate measurement and novel pattern detection | D5-24 |
| 5.5-S2 | Analyzing accuracy by document type and field to verify consistent performance across all segments before reducing human review | D5-23 |
| 5.5-S3 | Having models output field-level confidence scores, then calibrating review thresholds using labeled validation sets | D5-25 |
| 5.5-S4 | Routing extractions with low model confidence or ambiguous/contradictory source documents to human review, prioritizing limited reviewer capacity | D5-25 |

**TS 5.6 — Preserve information provenance and handle uncertainty in multi-source synthesis**

| ID | Official bullet | Card(s) |
|---|---|---|
| 5.6-K1 | How source attribution is lost during summarization steps when findings are compressed without preserving claim-source mappings | D5-26 |
| 5.6-K2 | The importance of structured claim-source mappings that the synthesis agent must preserve and merge when combining findings | D5-26 |
| 5.6-K3 | How to handle conflicting statistics from credible sources: annotating conflicts with source attribution rather than arbitrarily selecting one value | D5-27 |
| 5.6-K4 | Temporal data: requiring publication/collection dates in structured outputs to prevent temporal differences from being misinterpreted as contradictions | D5-29 |
| 5.6-S1 | Requiring subagents to output structured claim-source mappings (source URLs, document names, relevant excerpts) that downstream agents preserve through synthesis | D5-26 |
| 5.6-S2 | Structuring reports with explicit sections distinguishing well-established findings from contested ones, preserving original source characterizations and methodological context | D5-28 |
| 5.6-S3 | Completing document analysis with conflicting values included and explicitly annotated, letting the coordinator decide how to reconcile before passing to synthesis | D5-27 |
| 5.6-S4 | Requiring subagents to include publication or data collection dates in structured outputs to enable correct temporal interpretation | D5-29 |
| 5.6-S5 | Rendering different content types appropriately in synthesis outputs—financial data as tables, news as prose, technical findings as structured lists—rather than converting everything to a uniform format | D5-30 |

**Appendix — Technologies and Concepts**

| ID | Official item | Card(s) |
|---|---|---|
| APP-T1 | Claude Agent SDK — Agent definitions, agentic loops, stop_reason handling, hooks (PostToolUse, tool call interception), subagent spawning via Task tool, allowedTools configuration | D1-01, D1-11, D1-12, D1-20, D1-21 |
| APP-T2 | Model Context Protocol (MCP) — MCP servers, MCP tools, MCP resources, isError flag, tool descriptions, tool distribution, .mcp.json configuration, environment variable expansion | D2-01, D2-05, D2-08, D2-10, D2-11, D2-13 |
| APP-T3 | Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ with YAML frontmatter path-scoping, .claude/commands/ for slash commands, .claude/skills/ with SKILL.md frontmatter (context: fork, allowed-tools, argument-hint), plan mode, direct execution, /memory command, /compact, --resume, fork_session, Explore subagent | D1-23, D1-24, D3-01, D3-04, D3-05, D3-06, D3-07, D3-13, D3-15, D3-16, D5-22 |
| APP-T4 | Claude Code CLI — -p / --print flag for non-interactive mode, --output-format json, --json-schema for structured CI output | D3-21, D3-22 |
| APP-T5 | Claude API — tool_use with JSON schemas, tool_choice options ("auto", "any", forced tool selection), stop_reason values ("tool_use", "end_turn"), max_tokens, system prompts | D1-01, D4-07, D4-08 |
| APP-T6 | Message Batches API — 50% cost savings, up to 24-hour processing window, custom_id for request/response correlation, polling for completion, no multi-turn tool calling support | D4-17, D4-18, D4-19 |
| APP-T7 | JSON Schema — Required vs optional fields, enum types, nullable fields, "other" + detail string patterns, strict mode for syntax error elimination | D4-07, D4-09, D4-10, D4-11 |
| APP-T8 | Pydantic — Schema validation, semantic validation errors, validation-retry loops | D4-09, D4-13 |
| APP-T9 | Built-in tools — Read, Write, Edit, Bash, Grep, Glob — their purposes and selection criteria | D2-16, D2-17, D2-18 |
| APP-T10 | Few-shot prompting — Targeted examples for ambiguous scenarios, format demonstration, generalization to novel patterns | D4-04, D4-05, D4-06 |
| APP-T11 | Prompt chaining — Sequential task decomposition into focused passes | D1-22, D4-23 |
| APP-T12 | Context window management — Token budgets, progressive summarization, lost-in-the-middle effects, context extraction, scratchpad files | D5-01, D5-02, D5-03, D5-18 |
| APP-T13 | Session management — Session resumption, fork_session, named sessions, session context isolation | D1-06, D1-23, D1-24, D1-25 |
| APP-T14 | Confidence scoring — Field-level confidence, calibration with labeled validation sets, stratified sampling for error rate measurement | D5-24, D5-25 |

**Appendix — In-Scope Topics**

| ID | Official item | Card(s) |
|---|---|---|
| APP-I1 | Agentic loop implementation: Control flow based on stop_reason, tool result handling, loop termination conditions | D1-01, D1-02, D1-04 |
| APP-I2 | Multi-agent orchestration: Coordinator-subagent patterns, task decomposition, parallel subagent execution, iterative refinement loops | D1-05, D1-07, D1-10, D1-14 |
| APP-I3 | Subagent context management: Explicit context passing, structured state persistence, crash recovery using manifests | D1-06, D5-21 |
| APP-I4 | Tool interface design: Writing effective tool descriptions, splitting vs consolidating tools, tool naming to reduce ambiguity | D2-01, D2-02, D2-03 |
| APP-I5 | MCP tool and resource design: Resources for content catalogs, tools for actions, description quality for adoption | D2-01, D2-13, D2-14 |
| APP-I6 | MCP server configuration: Project vs user scope, environment variable expansion, multi-server simultaneous access | D2-10, D2-11, D2-12 |
| APP-I7 | Error handling and propagation: Structured error responses, transient vs business vs permission errors, local recovery before escalation | D2-05, D2-06, D5-13, D5-15 |
| APP-I8 | Escalation decision-making: Explicit criteria, honoring customer preferences, policy gap identification | D5-08, D5-09, D5-10 |
| APP-I9 | CLAUDE.md configuration: Hierarchy (user/project/directory), @import patterns, .claude/rules/ with glob patterns | D3-01, D3-02, D3-03, D3-04, D3-13 |
| APP-I10 | Custom commands and skills: Project vs user scope, context: fork, allowed-tools, argument-hint frontmatter | D3-06, D3-07, D3-08, D3-09, D3-10 |
| APP-I11 | Plan mode vs direct execution: Complexity assessment, architectural decisions, single-file changes | D3-15 |
| APP-I12 | Iterative refinement: Input/output examples, test-driven iteration, interview pattern, sequential vs parallel issue resolution | D3-17, D3-18, D3-19, D3-20 |
| APP-I13 | Structured output via tool_use: Schema design, tool_choice configuration, nullable fields to prevent hallucination | D4-07, D4-08, D4-10 |
| APP-I14 | Few-shot prompting: Ambiguous scenario targeting, format consistency, false positive reduction | D4-02, D4-04, D4-05 |
| APP-I15 | Batch processing: Message Batches API appropriateness, latency tolerance assessment, failure handling by custom_id | D4-17, D4-19, D4-20 |
| APP-I16 | Context window optimization: Trimming verbose tool outputs, structured fact extraction, position-aware input ordering | D5-01, D5-02, D5-03 |
| APP-I17 | Human review workflows: Confidence calibration, stratified sampling, accuracy segmentation by document type and field | D5-23, D5-24, D5-25 |
| APP-I18 | Information provenance: Claim-source mappings, temporal data handling, conflict annotation, coverage gap reporting | D5-16, D5-26, D5-27, D5-29 |

**Appendix — Out-of-Scope Topics**

| ID | Official item | Card(s) |
|---|---|---|
| APP-O1 | Fine-tuning Claude models or training custom models | M-05 |
| APP-O2 | Claude API authentication, billing, or account management | M-05 |
| APP-O3 | Detailed implementation of specific programming languages or frameworks (beyond what's needed for tool and schema configuration) | M-05 |
| APP-O4 | Deploying or hosting MCP servers (infrastructure, networking, container orchestration) | M-05 |
| APP-O5 | Claude's internal architecture, training process, or model weights | M-05 |
| APP-O6 | Constitutional AI, RLHF, or safety training methodologies | M-05 |
| APP-O7 | Embedding models or vector database implementation details | M-05 |
| APP-O8 | Computer use (browser automation, desktop interaction) | M-05 |
| APP-O9 | Vision/image analysis capabilities | M-05 |
| APP-O10 | Streaming API implementation or server-sent events | M-05 |
| APP-O11 | Rate limiting, quotas, or API pricing calculations | M-05 |
| APP-O12 | OAuth, API key rotation, or authentication protocol details | M-05 |
| APP-O13 | Specific cloud provider configurations (AWS, GCP, Azure) | M-05 |
| APP-O14 | Performance benchmarking or model comparison metrics | M-05 |
| APP-O15 | Prompt caching implementation details (beyond knowing it exists) | M-05 |
| APP-O16 | Token counting algorithms or tokenization specifics | M-05 |
