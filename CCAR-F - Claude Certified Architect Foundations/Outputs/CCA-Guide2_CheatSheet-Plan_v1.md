I have read both files in full — file 1 (1,326 lines, the CCA-F Master Recap) and file 2 (2,265 lines, all sections including the four meta-sections). Here is the plan.

---

# Plan: CCA Cheat Sheet #2 — from `exam-preparation-guide.md`

**Source:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\mock exams from repos\repo 2\exam-preparation-guide.md` (2,265 lines: Overview + 15 content sections + 4 meta-sections)
**Reference artifact:** CCA-F Master Recap (file 1)

---

## 1. Inherited Design Grammar (from file 1)

| # | Unit | Anatomy | Pedagogical job |
|---|---|---|---|
| G1 | **Sticky pill nav + scroll-spy** | mono pills, per-domain accent color, active-state highlight, theme toggle | Constant orientation; the reader always knows where they are and how much remains — the primary anti-overwhelm device |
| G2 | **Chapter header** | mono badge (`D1`) + serif-italic title + right-aligned exam weight | Signals priority (weight %) before content; the serif title marks a "breathing" register change from the mono data below |
| G3 | **Narrative connector** (`.narrative`) | left-bordered muted prose between cards / at chapter open | Carries the story spine — *why this concept comes next* — so the sheet reads as one argument, not a list |
| G4 | **Concept card** | `concept-name` (mono uppercase ID) → `concept-desc` (one-sentence *why*) → `.model` (visual) → `.tenets` (chevron recall bullets incl. exam traps) → `.bridge` (italic ↓ line) | The atomic study unit: ID makes it addressable, desc gives the mental model, visual carries recall, tenets carry the exam-precise facts, bridge hands off to the next card |
| G5 | **Bridge line** (`.bridge`) | last line inside the card, `↓`-prefixed italic | Local interconnection: every card explicitly states its relationship to the next concept |
| G6 | **Semantic color tokens** | `--go` green / `--stop` red / `--warn` amber / `--accent` blue + 5 domain hues | Instant valence: correct pattern vs trap is readable before reading |
| G7 | **Visual model library** | signal-bar (binary), hub-diagram (star topology), compare (2-col good/warn), mcp-row (triads), channels (dual-wire), stack (layers), attention-window (gradient continuum), conf-flow (threshold fork), prov-chain (pipeline), type-gate (diamond decision), esc-table / dva-table (mono tables), flag/gg/sess/schema-pair (paired boxes), batch-rule (condition→action grid), pill (inline exam-literal chip) | Each model type matches a concept *shape* — binary choice, hierarchy, continuum, pipeline, contrast — so the spatial form itself is the retrieval cue |
| G8 | **Trap tenets** | tenets phrased as "Exam trap: …" / "Anti-pattern: …" | Converts the source's pitfall lists into recall payload inside the owning concept, not a separate dump |
| G9 | **Card pairing** | one card can carry two sibling concepts ("D1.3 / D1.4") | Compresses tightly coupled concepts without losing either — density control |
| G10 | **Footer provenance** | source + date | Trust anchor |

Everything in the new sheet inherits G1–G10. New model types are added only where file 2 contains concept shapes file 1 never had (see §4).

---

## 2. Concept Inventory (from file 2) — exhaustive, by source section

Notation: `S<n>.<m>` = section n, item m. Line ranges are from the source file.

### S0 — Overview (lines 1–15)
| # | Concept | Lines |
|---|---|---|
| S0.1 | **The responsibility-placement spine**: model = language/judgment; application code = deterministic guarantees (permissions, thresholds, state, retries, idempotency, validation, audit); tool/schema design shapes behavior — "interface failures masquerade as reasoning failures" | 5–11 |
| S0.2 | Exam posture: trade-offs, not rote definitions; "where should responsibility live?" as the master question | 5–7 |

### S1 — API Fundamentals and Output Control (17–122)
| # | Concept | Lines |
|---|---|---|
| S1.1 | Messages API statelessness; app must resend system prompt + history + state + tool results every turn | 21–23 |
| S1.2 | `session_id` is an app-side lookup key, never model memory | 23, 96 |
| S1.3 | Conversation-growth physics: input cost ↑, latency ↑, attention competition ↑ | 25–28, 83–91 |
| S1.4 | API shape: top-level `system` param (not a role); `tool_use` / `tool_result` content blocks | 30 |
| S1.5 | Two structured-output routes: `output_config.format` (response IS JSON) vs tool use / `strict: true` (structured tool call); can combine | 32–41 |
| S1.6 | `tool_choice` four-way: `auto` / `any` / `tool` / `none` + use cases; `any` for guaranteed-but-unchosen extraction; named tool for forced first stage; reordering definitions is unreliable | 43–54 |
| S1.7 | Extraction pipeline recipe (5 steps) ending in the **validation-error feedback loop** — resend source + bad output + exact errors, never blind retry | 56–62, 101–121 |
| S1.8 | Tool/schema definitions cost input tokens; big schema + long doc → degradation near attention boundary (root cause = total context, not model defect) | 64 |
| S1.9 | Structured-output ops facts: first-request grammar-compilation latency, schema caching, complexity limits, refusal/max_tokens can still break conformance — schema ≠ domain validation | 66 |
| S1.10 | **Prefill is legacy**: trailing assistant turn now errors on current models (4.6+); earlier assistant messages (few-shot) still valid; 4-row replacement table (format → structured outputs; label → enum; boilerplate → system instruction; continuation → quoting user turn) | 68–81 |
| S1.11 | Pitfalls: persistent-memory assumption, session_id-as-memory, prompt-forced text JSON, ignoring schema token cost, `auto` ≠ required | 93–99 |

### S2 — Designing Tool Interfaces (124–306)
| # | Concept | Lines |
|---|---|---|
| S2.1 | Tool design = prompt design + API design; description checklist (does / when / when-not / input formats / output / limitations); `input_examples` for nested inputs | 126–139 |
| S2.2 | **Tool execution placement** (4-row table): user-defined client-side / Anthropic-defined client-side / server-side / MCP — who defines schema, who executes, trust boundary + ops burden per row | 141–156 |
| S2.3 | Promote Bash-style opaque actions to dedicated tools when the app must gate/render/audit/parallelize (`send_email` vs `bash -c curl`) | 158 |
| S2.4 | Parameter design: enums for stable closed sets; real-domain parameters, not "bag of strings" | 160–174 |
| S2.5 | **Lookup-then-act** + user disambiguation with differentiating fields; complementary to preview-then-execute (*which entity* vs *what action*) | 176–181 |
| S2.6 | Stable identifiers over derived intermediates; tool resolves mechanical dependencies internally | 183, 239 |
| S2.7 | Split tools when required fields differ per operation (`log_cardio`/`log_strength`; `manage_order` anti-pattern) | 185–187 |
| S2.8 | Output design: structured + IDs for chaining; normalize heterogeneous backends into one schema | 189–215 |
| S2.9 | Empty result = success with empty array, **not** `isError` | 217 |
| S2.10 | Pagination: first page + `total_count` + cursor; never auto-fetch all pages (latency/tokens/context) | 219, 243–249 |
| S2.11 | Tool composition: combine mechanical / always-together / atomic-race-prone (`find_and_book`); never combine across judgment or provenance steps; `hold_slot` caveat | 221–239 |
| S2.12 | **Progressive availability** for large tool sets: discovery tools → ranked shortlist → dynamic registration; vs monolithic `find_and_execute` (hides the decision); SDK tool search; MCP `list_changed` | 251–263 |
| S2.13 | `requires_review` + calibrated thresholds in tool output (not raw confidence); confirmation payloads must show cost/target/scope/irreversibility | 265–282 |
| S2.14 | Safety structure: **preview-then-execute with one-time confirmation token**; `dry_run: boolean` anti-pattern (model can set false) | 284–296 |
| S2.15 | Pitfalls: format-in-parameter-names, free-text-everything, prose-only outputs, combined decision points, annotations-as-security | 298–304 |

### S3 — Error Handling in Agent Tools (308–405)
| # | Concept | Lines |
|---|---|---|
| S3.1 | **Five error categories table**: transient / validation / business rule / permission / uncertain-write → distinct correct handling each | 310–322 |
| S3.2 | Absorb recoverable infrastructure noise inside the tool (model needn't see the first failed attempt) | 324, 382 |
| S3.3 | **Uncertain side effects**: post-submission write timeout → structured uncertain-state result, no `retry_safe: true`, verify via status lookup / idempotency key; inverse of read-side timeouts | 326, 386–396 |
| S3.4 | Structured error results (`isError: true` with categorized JSON payload: category, retryable, code, user explanation, next steps) | 328–357 |
| S3.5 | **MCP two error tiers**: protocol (JSON-RPC — unknown tool, missing required param, malformed request) vs tool-execution (`isError: true` — 404, 503, business, permission); `check_availability` 3-case example; "missing record is data, not protocol failure" | 359–372 |
| S3.6 | **Retry responsibility placement**: tool-level (transient) / model-level (input must change) / human (side-effect or policy); `search_catalog` 8%-vs-4% split example; `retryable` boolean alone is weaker than in-tool retry | 374–384 |
| S3.7 | Pitfalls: exceptions for business errors, retryable uncertain writes, empty-data-for-failure, free-text errors | 398–403 |

### S4 — Structured Data Extraction and Validation (407–613)
| # | Concept | Lines |
|---|---|---|
| S4.1 | Extraction goal ladder: syntactically valid → semantically correct → traceable → safe downstream; schema-backed output for production | 409–413 |
| S4.2 | Schema shapes output but cannot prove source support; **absence-semantics table** (optional/nullable, empty array, `value: null`+reason, `unclear` enum, `other`+detail) | 415–429 |
| S4.3 | Enum escape hatches: `other` + `*_detail` field for evolving category sets | 431–444, 463 |
| S4.4 | Fabrication reduction: extraction-not-inference instructions; required-fields-force-fabrication mechanism → make nullable | 446–455 |
| S4.5 | **Verification-call anti-pattern**: second LLM "verify" pass is inferior to fixing the schema (cost, rationalization, doesn't fix root cause); use only as sampling audit | 457 |
| S4.6 | `null` vs empty array semantics ("didn't address" vs "found none"); grow `unclear` enum for sarcasm/ambiguity | 459 |
| S4.7 | Few-shot for edge cases and format standardization — 2–3 examples beat narrative rules for subtle distinctions | 461 |
| S4.8 | **Provenance fields** (location, quote, effective date); citations-API vs strict-JSON incompatibility → put provenance in the schema; amendments need original+amended+dates, not a scalar; precedence rules in instructions | 465–488 |
| S4.9 | **Semantic validation layer**: totals reconcile, date ranges, ID formats, citation existence, category cross-copying; correction request with source+extraction+errors; `temperature: 0` fallacy | 490–512 |
| S4.10 | Reconciliation fields in-schema (`calculated_total` / `stated_total` / `totals_match`) | 514–525 |
| S4.11 | **When retries can't help**: info absent from provided source (only unfixable case) vs shape/locale/date-format issues (fixable with feedback) | 527–536 |
| S4.12 | Long/scattered docs: chunking (exceeds context; loses cross-section links) vs **pre-extraction summarization** (fits but scattered; preserves both); few-shot ≠ needle-finding | 538–548 |
| S4.13 | Confidence calibration: labeled validation set, per-segment measurement; `requires_review` + reasons beats raw score | 550–565 |
| S4.14 | Human-review routing criteria (low calibrated confidence, ambiguity, high-impact fields, failed validation, error-prone doc types) | 567–573 |
| S4.15 | **Automation-plan validation**: segment accuracy before threshold-setting (97% aggregate can hide 80% segment); post-launch stratified sampling of high-confidence outputs | 575–579 |
| S4.16 | Feedback loops: recurring correction pattern → few-shot fix first (fine-tuning/regex/schema are heavier); dismissed review findings need `detected_pattern`/`rule_id`/`evidence` fields | 581–593 |
| S4.17 | Batch extraction: `custom_id` joining, per-document urgency routing, bulk-deadline strategy (all-in first, resubmit failures with refined prompts) | 595–603 |
| S4.18 | Pitfalls: valid-JSON-as-correct, schema-compliance-as-truth, required-absent-fields, strict-enums, aggregate-only accuracy, single-call long docs | 605–612 |

### S5 — Conversation Context Management (616–773)
| # | Concept | Lines |
|---|---|---|
| S5.1 | Context management = state management; **need→strategy table** (recent flow / narrative / preferences / exact facts / canon / tool-heavy → 6 strategies) | 618–631 |
| S5.2 | Sliding window: when (94%-recent-reference traffic profile), when not; **RAG-results-specific window** (last 2–3 retrievals) separate from conversation policy | 633–639 |
| S5.3 | Progressive summarization: structured (Decisions/Preferences/Open questions/Facts) vs vague prose; hybrid (summaries + verbatim recent); "double the window" anti-fix | 641–662 |
| S5.4 | **Persistent reference sections**: story bibles, user definitions, safety facts (allergies), scaling params — retained verbatim, trimming applies only around them; dinner-party combined-strategy example | 664–675 |
| S5.5 | **Structured state object** as canonical current truth; why alternatives fail (inference, "prefer recent" instruction, pruning, few-shot); surface preference conflicts, never average; multi-issue tracking | 677–701 |
| S5.6 | Retrieval / fact stores for exact values; research-assistant pattern: on-demand source re-injection beats fact-store-everything and high-fidelity summaries | 703–713 |
| S5.7 | Tool-result compression: keep decision-relevant fields, drop the rest; beats accumulation, prose summarizing, vector-DB offloading | 715–719 |
| S5.8 | **API-native management**: compaction (summarize server-side) vs context editing (prune stale tool results); application-level = control/portability, API-native = less plumbing; they compose; `model_context_window_exceeded` stop reason as the trigger | 721–735 |
| S5.9 | **Returning users**: fresh start + structured summary + `fresh_lookup_required`; why resume-with-instruction / filtering tool_results / re-call-everything all fail | 737–753 |
| S5.10 | External mid-session updates: inject fresh state into next request; no unsolicited assistant turns; current state must outrank stale tool results | 755–761 |
| S5.11 | System prompt versioning per conversation; migration strategy for midstream policy changes | 763–765 |
| S5.12 | Pitfalls: capacity ≠ attention, vague summarization of exact facts, RAG-forever, stale-transcript resume | 767–772 |

### S6 — System Prompt Engineering (776–908)
| # | Concept | Lines |
|---|---|---|
| S6.1 | System prompt sent on **every** request; omission diverges immediately, not gradually | 778–782 |
| S6.2 | **Attention weakening despite inclusion**: recent turns compete; fix is structural (reinforce at breakpoints, version, move hard rules to code) | 784, 843–853 |
| S6.3 | XML-sectioned prompts (`<role>/<style>/<safety>/<examples>`); tags aid salience and later referenceability | 786–806 |
| S6.4 | Mid-session external state belongs in the system prompt ("what is currently true") vs tool results (agent-requested) — **but** caching trade-off: rewriting the prefix invalidates cache → inject fast-changing state late | 808–810 |
| S6.5 | **Principles vs conditionals**: principles for judgment, conditionals for safety bright-lines; conditional-explosion anti-pattern (keyword-matching users); 100%-rules go to code | 812–827 |
| S6.6 | Few-shot examples over rule walls: contrasting pairs restore adherence; examples denser than prose for learned (not recited) behavior | 829–841 |
| S6.7 | Prompt dilution mitigations: concise structure, salient sections, behavioral examples, natural-breakpoint reminders (user-role messages), out-of-model enforcement; system-prompt-as-living-config versioning | 843–858 |
| S6.8 | **Clarify vs assume** risk gate: ask when (divergent interpretations / irreversible / conflicting goals / missing info), proceed-with-stated-assumption when low-risk; **one focused question**, not interrogation lists; name preference conflicts, don't average (cheap flight vs 9AM nonstop) | 860–887 |
| S6.9 | Response format control: style instruction + example beats "never say X" lists; repetitive openers = old prefill use case, now system-prompt + examples; structured outputs for machine formats | 889–900 |
| S6.10 | Pitfalls: IMPORTANT/NEVER-as-reliability, endless conditionals, rules buried in prose, workflow checklists in global memory | 902–907 |

### S7 — Model Context Protocol (911–1006)
| # | Concept | Lines |
|---|---|---|
| S7.1 | MCP = open standard; server exposes / client connects / host decides interaction | 913–915 |
| S7.2 | **Three primitives with controllers**: Tools (model-controlled) / Resources (application-controlled) / Prompts (user-controlled) + purposes | 917–929 |
| S7.3 | **Resource vs tool decision rule**: stable reference → resource; dynamic computation → tool; "natural-language aggregator tool" anti-pattern; resources and tools are complements | 931–937 |
| S7.4 | Why MCP: reuse across ≥2 clients; single-app workflows may prefer custom tools; MCP does NOT solve auth/rate-limits/retries/caching | 939–943 |
| S7.5 | Combined tool registry; descriptions compete with built-ins; ignored-MCP-tool fix = better description (when-preferable, IO, examples, capabilities), not removing generic tools | 945–956 |
| S7.6 | **Annotations** (`readOnlyHint`/`destructiveHint`/`idempotentHint`/`openWorldHint`): UI affordances only, **never a security boundary** — choose the prompt, never skip the check | 958–962 |
| S7.7 | MCP error-tier rule restated: before-business-logic → JSON-RPC; reached-target-and-failed → `isError: true`; wrong-tier consequences both directions | 964–973 |
| S7.8 | Tool search / progressive availability at host level; `list_changed` notifications; descriptions must read in isolation for search discovery | 975–982 |
| S7.9 | **Claude Code MCP scopes table**: project (`.mcp.json`, VCS) / local (`~/.claude.json`, project-keyed) / user (`~/.claude.json`, global); precedence **local > project > user**, whole-entry wins (no field merging); credentials never in project scope; local≠user despite same file | 984–996 |
| S7.10 | MCP prompts surface as `mcp__<server>__<prompt>` slash commands; servers should control output size / paginate | 998 |
| S7.11 | Pitfalls: tool-where-resource, MCP-handles-auth assumption, trusting annotations, minimal descriptions | 1000–1005 |

### S8 — Agentic Patterns and Task Decomposition (1009–1138)
| # | Concept | Lines |
|---|---|---|
| S8.1 | The agent loop (observe→reason→act→observe); the architecture question is autonomy + structure | 1011–1015 |
| S8.2 | **Five-pattern table**: prompt chaining / routing / orchestrator-workers / dynamic decomposition / parallel subagents — best-for + avoid-when + examples | 1017–1033 |
| S8.3 | Pattern-to-work-shape matching: billing dispute (fixed chain) vs incident triage (dynamic); dynamic needs termination criteria + step caps | 1035–1039 |
| S8.4 | **When NOT to delegate**: delegation overhead (tool call, fresh context, invocation, result passing); coordinator does small in-context work itself | 1041–1043 |
| S8.5 | **Partition-then-parallel**: N chunks → N subagents → synthesis; balance by expected effort (elapsed = max, not sum); avoid when interdependent / splits logical units / streaming matters | 1045–1051 |
| S8.6 | **Subagent context isolation**: fresh conversation; receives only constructed prompt + own AgentDefinition; no parent turns/tool results/sibling outputs; no default "resume" — parent must persist and re-supply | 1053–1059, (mirrored 1479–1484) |
| S8.7 | Handoff quality: concise task + findings + constraints + output shape; structured claim→source index (IDs, URLs, dates, confidence) when citations required — never prose-only | 1061–1073 |
| S8.8 | Tool distribution by role (search agent ≠ synthesis agent); **Task/Agent tool must be in parent's `allowedTools`** or orchestration silently can't delegate; subagent's own allowedTools separate | 1075–1086 |
| S8.9 | Parallel execution: multiple tool calls per turn / concurrent SDK calls; **serial decompose → parallel execute → serial synthesize** phasing; I/O-bound wins most; balance the slowest slice | 1088–1094 |
| S8.10 | State persistence: structured workflow manifest (completed steps, doc statuses, open gaps); resume by injecting relevant state, not replaying transcripts | 1096–1115 |
| S8.11 | Research provenance: claim + source + date + methodology + uncertainty + established/contested status; dates prevent trend-vs-contradiction confusion; render by content type (tables/prose/lists) | 1117–1130 |
| S8.12 | Pitfalls: full-pipeline-for-simple-facts, strict one-pass research, raw 100K handoffs, over-prescribed subagents | 1132–1137 |

### S9 — Customer Service and Production Workflows (1141–1225)
| # | Concept | Lines |
|---|---|---|
| S9.1 | Escalation triggers (explicit request, missing authority, policy exception, no progress, unsafe state); **not counters** ("after 3 failed tools") — category and impact over count | 1147–1157 |
| S9.2 | Structured escalation handoff payload (id, issue, root cause, records, amount, actions, recommendation); not first-complaint-only, not transcript dumps | 1159–1173 |
| S9.3 | Frustrated users: acknowledge + offer resolution *and* preserve transfer choice; no silent actions, no long intake | 1175–1183 |
| S9.4 | **Programmatic compliance**: threshold read from server-controlled state inside the tool; no model-settable `override`/approval params; structured `requires_approval` result | 1185–1200 |
| S9.5 | Preview-then-execute with **single-use tokens** bound to the previewed payload, short-lived, not constructible by the model | 1201 |
| S9.6 | Server-side authorization on **every** invocation ("the model already checked" is not a defense); defense-in-depth = prompt biases + tool enforces + audit detects | 1202–1204 |
| S9.7 | **Graceful degradation**: report done / pending / next-steps on partial completion; never claim uncompleted side effects; repeated same-input failure → switch strategies, not more retries | 1206–1217 |
| S9.8 | Pitfalls: contextless escalation, prompt-rule high-risk actions, retrying uncertain writes, detail-free confirmations | 1219–1224 |

### S10 — Claude Code and Agent SDK Workflows (1228–1494)
| # | Concept | Lines |
|---|---|---|
| S10.1 | Claude Code vs Claude Agent SDK naming (SDK = current; "Claude Code SDK" = older refs) | 1230–1234 |
| S10.2 | **Built-in tool selection table** (Grep contents / Glob paths / Read / Edit-MultiEdit / Read-then-Write / Bash / Task) | 1236–1250 |
| S10.3 | Exploration workflow: entry points → follow imports → trace representative paths → scratchpad; map-then-read, never read-everything | 1250–1258 |
| S10.4 | Concrete `@file` references beat "follow our usual style" | 1260 |
| S10.5 | **Plan mode vs direct execution**: plan for multi-file/architectural/migrations/approval/read-only; `--permission-mode plan`, `Shift+Tab`; production-bug flow (evidence → narrow fix or escalate to planning) | 1262–1276 |
| S10.6 | **Plan mode ≠ extended thinking**: workflow control vs reasoning quality; composable; diagnose which problem you actually have | 1278–1284 |
| S10.7 | **Session flags table**: `--continue` (latest in cwd) / `--resume` (picker or specific) / `--session-id` (stable UUID) / `--fork-session` (branch from checkpoint); `--continue` wrong-session risk | 1286–1299 |
| S10.8 | Sessions persist conversation, not files: **fork-session + git worktree pairing** for parallel alternatives; changed-codebase resume rules; no concurrent same-session resumes | 1301–1308 |
| S10.9 | Context isolation for self-review: fresh context / review subagent / CI / separate session with diff | 1310–1312 |
| S10.10 | Scratchpads for long explorations (files, data flow, open questions, risks, next steps) | 1314–1325 |
| S10.11 | **Two memory systems**: CLAUDE.md/rules (you write) + auto memory (Claude writes); both context, **not enforcement** — hard rules go to hooks / `permissions.deny` | 1327–1334 |
| S10.12 | **CLAUDE.md hierarchy table**: managed policy / user `~/.claude/` / project / `CLAUDE.local.md`; broad-first concatenation; ancestors load fully at launch, subdirectories lazily | 1336–1347 |
| S10.13 | `@imports` (5 hops, expand at launch — organize but don't save tokens); `claudeMdExcludes` (managed policy immune); `AGENTS.md` interop via import/symlink | 1349–1353 |
| S10.14 | **`.claude/rules/`**: per-file rules, recursive; `paths:` frontmatter = load-on-matching-read; no-frontmatter = unconditional; `~/.claude/rules/` personal; when rules vs CLAUDE.md | 1355–1376 |
| S10.15 | **Auto memory mechanics**: `~/.claude/projects/<project>/memory/`; MEMORY.md first 200 lines / 25KB at start; topic files on demand; machine-local, shared across worktrees; disable paths | 1378–1384 |
| S10.16 | **Four-mechanism decision table**: CLAUDE.md (always-on) / rules (path-scoped) / skills (on-demand procedure) / hooks (deterministic enforcement) | 1386–1397 |
| S10.17 | Debugging memory: `/memory` first (is the file even loaded?); `InstructionsLoaded` hook for lazy/path-scoped loads; "loading scope, not wording" | 1399–1403 |
| S10.18 | **Task-scoped vs path-scoped**: code-review checklist ≠ `paths:` glob (fires outside reviews); slash/skill/subagent for activities, rules for areas | 1405–1419 |
| S10.19 | **Skills**: SKILL.md, description-in-context + body-on-demand (progressive disclosure); skill vs slash command (task-recognition vs deliberate human act) | 1421–1432 |
| S10.20 | Slash commands: reusable prompts, project vs user scope; MCP prompts appear here too | 1434–1442 |
| S10.21 | **Hooks**: `PreToolUse` (deny/allow/ask/defer/inject/modify-input — the canonical hard-rule mechanism) / `PostToolUse` / `UserPromptSubmit` / `SessionStart`; hooks are code with your privileges — vet third-party configs, no secrets through logged args | 1444–1462 |
| S10.22 | Subagents in Claude Code: separate windows, single responsibility, limited tools, output contract; **no inheritance** — CLAUDE.md not auto-loaded, no continuation between invocations | 1464–1484 |
| S10.23 | Pitfalls: plan-mode-for-tiny-edits, direct-execution-for-migrations, unsafe resumes, global-CLAUDE.md checklists, memory-as-enforcement, prompt-gated destructive Bash | 1486–1493 |

### S11 — Iterative Refinement, Testing, Evaluation (1497–1561)
| # | Concept | Lines |
|---|---|---|
| S11.1 | Concrete executable feedback (failing input + expected + actual + assertion); 5-step coding iteration; one failure class at a time | 1499–1517 |
| S11.2 | Recurring same-defect across runs = structural prompt/schema change (example, tool split, new field), not another retry — "prompt fixes generalize; retries don't" | 1519 |
| S11.3 | Test-generation quality: five low-value patterns; document test standards + fixtures with examples | 1521–1531 |
| S11.4 | Code-review agents: explicit report/skip criteria; few-shot beats "be conservative" for false positives; dismissal-capture fields | 1533–1539 |
| S11.5 | **Segment evaluation**: by document type / field / prompt version / model / source quality / confidence band / correction category; aggregate masks segment failures | 1541–1553 |
| S11.6 | Pitfalls: full-rewrite-after-narrow-failure, uncalibrated confidence, dismissals-as-noise, infrastructure-before-examples | 1555–1560 |

### S12 — Model Selection and Inference Controls (1564–1642)
| # | Concept | Lines |
|---|---|---|
| S12.1 | **Tier table**: Haiku (routing/classification) / Sonnet (default workhorse) / Opus (complex agentic); versions/prices change — consult docs/Models API, patterns are stable | 1570–1578 |
| S12.2 | **Five allocation patterns**: tier-per-step, cheap-to-expensive routing, mixed tiers across agents, escalate-on-signal (not anxiety), eval-validated tier changes | 1578–1584 |
| S12.3 | **Adaptive thinking + effort**: model decides when/how much; request-level effort scales reasoning+tools+output; fixed thinking budgets deprecated/legacy; spend reasoning on reasoning-shaped tasks | 1586–1594 |
| S12.4 | Streaming: humans watching (TTFT) or long outputs (timeout risk); skip for batch/M2M; changes delivery, not quality or cost | 1596–1603 |
| S12.5 | **Stop-reason table (7 rows)**: `end_turn` / `tool_use` / `max_tokens` / `stop_sequence` / `pause_turn` (re-send as-is) / `refusal` (no blind retry) / `model_context_window_exceeded` (compact, can't retry); max_tokens vs window-exceeded distinction | 1605–1619 |
| S12.6 | API-level errors: 429 (retry-after, backoff+jitter), 500/529 (retry), 400 (fix, don't retry); **SDKs auto-retry** — don't hand-roll; sustained 429 = capacity planning; limits per model, tokens and requests | 1621–1629 |
| S12.7 | Token-counting endpoint (exact, free, model-specific); third-party tokenizers miscount | 1631–1633 |
| S12.8 | Pitfalls: one-model-everything, anxiety escalation, truncation-as-model-failure, retrying refusals/overflows, hand-rolled retries | 1635–1641 |

### S13 — Prompt Caching (1645–1702)
| # | Concept | Lines |
|---|---|---|
| S13.1 | **Exact-prefix-match invariant**; render order tools → system → messages; one changed byte invalidates everything after; reads ~an order of magnitude cheaper, writes carry premium | 1647–1651 |
| S13.2 | Stability-ordered design (tools, frozen system prompt, stable history, volatile last); **five silent invalidators**: timestamps, non-deterministic serialization, per-user IDs early, flag-toggled sections, mid-conversation tool/model changes | 1653–1668 |
| S13.3 | Cross-section interaction: mid-session system-prompt updates and mode-by-toolset-swap are cache-hostile → inject state late, pass mode as message content | 1670 |
| S13.4 | Breakpoints (≤4), TTL 5 min / 1 hr option, minimum cacheable size (~1–few K tokens, silently uncached below); **verify via usage fields** — zero reads on repeated prefixes = silent invalidator, byte-diff two requests | 1672–1681 |
| S13.5 | Economics: pays off by second hit; steady traffic self-warms; never cache non-repeating content; right-lever matching: repeated prefix→cache, deferrable→batch, over-tiered→smaller model, bloat→trim; caching ≠ capacity, ≠ generation speed | 1678–1693 |
| S13.6 | Pitfalls: timestamp killer, mid-session prompt/tool updates, caching non-repeats, caching-to-fit fallacy, unchecked usage fields | 1695–1701 |

### S14 — Batch Processing, Cost, Latency (1705–1770)
| # | Concept | Lines |
|---|---|---|
| S14.1 | Batch mechanics: independent Messages-shaped requests, background processing, JSONL results, statuses (in progress/canceling/ended; per-result succeed/error/cancel/expire), platform size limits, pre-validate shape | 1707–1739 |
| S14.2 | The two facts: **~50% discount** and **24-hour worst-case window** — design SLAs to worst case | 1712–1714 |
| S14.3 | Fit criteria: good (volume, deferrable, independent) vs poor (interactive, deadlines, dependent steps) | 1716–1729 |
| S14.4 | `custom_id` mandatory: unordered results, join by ID never position; stable unique IDs enable partial re-runs | 1731 |
| S14.5 | **SLA cadence arithmetic**: cadence ≤ deadline − 24h − buffer; 30h→6h, 36h→12h, 26h→2h worked examples; slowest record sets worst case | 1741–1747 |
| S14.6 | Failure handling by type: chunk `context_length_exceeded`, resubmit-with-feedback validation, refine-prompt schema issues, resubmit expired — never rerun whole batch | 1749–1758 |
| S14.7 | Batch + caching stack (best-effort cache hits inside async batches); neither lever fixes the other's limits | 1760–1762 |
| S14.8 | Pitfalls: cost-only choice, assumed ordering, full-batch retries, interactive batching | 1764–1769 |

### S15 — Security and Trust Boundaries (1773–1815)
| # | Concept | Lines |
|---|---|---|
| S15.1 | **Two untrusted flows**: model output → your systems (validate/authorize in code) and external content → the model (prompt injection); prompts influence, code constrains | 1775–1782 |
| S15.2 | Injection rides legitimate content: retrieval, pages, email, tickets, file names, code comments — no malicious user required | 1784–1786 |
| S15.3 | **Four architectural defenses**: least privilege per context, human-gated consequential actions (preview+token), instructions-in-data-are-data, output allowlists | 1788–1793 |
| S15.4 | **Exfiltration triad**: private data + untrusted content + outbound channel — remove or gate one leg | 1795 |
| S15.5 | Supply chain: MCP servers and hooks vetted like dependencies; annotations = unverified claims; hooks = arbitrary code with your privileges | 1797–1799 |
| S15.6 | Secrets & data hygiene: secrets in context = leaked to every storing system; inject at execution layer; data minimization doubles as security; audit logging of tool calls | 1801–1806 |
| S15.7 | Pitfalls: prompt-vs-adversary, every-tool-everywhere, trusted-because-retrieved, "just this session" secrets, MCP-as-plumbing | 1808–1814 |

### Meta-sections — treatment decisions

| Section | Lines | Treatment | Why |
|---|---|---|---|
| **S16 Quick Reference Cheat Sheet** | 1818–1991 | **Not a chapter — a coverage audit instrument.** Every bullet in S16 is a compressed restatement of S1–S15. During authoring, each S16 bullet is checked off against the concept card that carries it; any bullet with no home becomes a new tenet in the owning card (e.g., "3–4 sentence descriptions," "keep `lookup_order` rather than full menu rows" are phrasings that must survive into tenets). | Duplicating it as content would double the sheet and break E4 (calm structure). Its *function* — compression — is what the whole artifact already is. |
| **S17 Study Strategy** | 1994–2043 | Split three ways: (a) Recommended Order (1996–2009) → absorbed into chapter ordering rationale (§3 below); (b) "How to Practice" design-pair list (2011–2029) → each of the 11 duels becomes an inline **xref chip** on the card where that contrast lives (they all map to existing compare panels); (c) **Exam Reasoning Checklist** (2031–2042, 8 questions) → genuinely new content, becomes its own card in the closing "Exam Lens" coda. | (a) and (b) are structure, not concepts; (c) is a real recall asset unique to this source. |
| **S18 Practice Scenarios + Answer Key** | 2046–2215 | **"Scenario Gauntlet" coda chapter** — a 15-row scenario-strip table: scenario name → the trap (why the plausible wrong answers fail, one line) → the winning pattern → chip linking back to the owning chapter. Full scenario prose is NOT reproduced (it's quiz material, not recap); the answer-key *rationales* are the densest recall triggers in the whole guide and are what the strip compresses. | A cheat sheet's job for scenarios is pattern-to-trap mapping, not re-testing. The chip links make the gauntlet double as a self-audit of the 15 chapters. |
| **S19 Recommended Reading** | 2219–2265 | Collapsed appendix: **Source Map** — compact two-column link list grouped by chapter (each chapter's official docs), visually de-emphasized (muted, small mono), placed after the footer-adjacent coda. | The links are reference plumbing, not recall content; grouping by chapter converts a flat list into "where to verify each chapter." |

**Verification (E1 gate):** All top-level sections of file 2 — Overview, S1–S15, and the four meta-sections S16–S19 — appear above with their major concepts itemized: **129 inventory items + 4 meta-treatments.**

---

## 3. Chapter Architecture

### Structure: 4 acts + coda, 15 content chapters

The source's own Study Strategy (S17) prescribes a reading order that is nearly identical to source order; the chapter sequence follows it, with one deliberate move — **Iteration/Eval (S11) stays before Model Selection (S12)** as the source has it, because the "eval-validated tier changes" pattern in S12 depends on S11's segment-evaluation concept.

| Act | Chapter | Source | Cards (est.) | Rationale |
|---|---|---|---|---|
| — | **C0 · The Spine** | S0 Overview | 1 | Concept Zero: the responsibility-placement ledger. Placed alone before Act I because ~10 later cards resolve to it (the sheet's most-referenced node). |
| **Act I — Foundations** | **C1 · The Request** | S1 | 6 | Statelessness is the axiom everything else is derived from — same opening logic as file 1's "the model has amnesia." |
| | **C2 · The Tool Contract** | S2 | 8 | Tools are the first thing built on top of the request. Kept separate from errors: 183 source lines each; merging would breach the chapter budget. |
| | **C3 · The Error Channel** | S3 | 4 | Directly downstream of C2 (a tool's error is part of its contract). Owns the canonical MCP-error-tiers card; C7 chips back to it. |
| | **C4 · The Extraction** | S4 | 8 | The first complete *application* of C1–C3 (schemas + tools + validation loops); ends Act I on a worked system. |
| **Act II — The Conversation** | **C5 · The Context** | S5 | 7 | Shifts from single-request to multi-turn physics. |
| | **C6 · The Prompt** | S6 | 6 | System-prompt behavior presupposes C5's attention model (dilution, competition). Owns the canonical system-prompt-versioning card (S5.11 merges in, chip from C5). |
| **Act III — The System** | **C7 · The Protocol** | S7 | 6 | MCP opens the multi-component world. |
| | **C8 · The Orchestra** | S8 | 7 | Agent patterns; owns the canonical subagent-isolation card (S8.6/S10.22 are the same fact — C10 keeps only the Claude Code-specific configuration angle, chipped). |
| | **C9 · The Front Line** | S9 | 5 | Production customer-service workflows = C8's patterns under compliance pressure; sets up C15's enforcement theme. |
| | **C10 · The Workbench** | S10 | 10, in two labeled sub-groups: *Working* (tools, plan mode, sessions, scratchpads) and *Memory & Config* (hierarchy, rules, skills, hooks, subagents) | Largest source section (267 lines). Sub-grouping inside one chapter keeps nav flat while giving the eye a rest point mid-chapter. |
| **Act IV — Operations** | **C11 · The Feedback Loop** | S11 | 4 | Evaluation precedes the levers it validates. |
| | **C12 · The Dials** | S12 | 6 | Tiers, effort, streaming, stop reasons, rate limits. |
| | **C13 · The Cache** | S13 | 4 | Cost lever #1; heavy cross-links to C6/C12/C14. |
| | **C14 · The Batch** | S14 | 4 | Cost lever #2; the SLA-arithmetic card is this chapter's signature visual. |
| | **C15 · The Perimeter** | S15 | 5 | Security closes the acts: it re-invokes C0's spine ("code enforces"), C2's preview-token, C8's tool restriction — the natural summarizing chapter. |
| **Coda** | **CX · Exam Lens + Scenario Gauntlet** | S17(c), S18 | 2 composite units | The 8-question reasoning checklist + the 15-row gauntlet strip. Ends the document in exam-mode. |
| **Appendix** | **Source Map** | S19 | 1 collapsed list | De-emphasized verification links, grouped by chapter. |

**Merges:** S3.5+S7.7 (MCP error tiers → one card in C3); S8.6+S10.22 (subagent isolation → one card in C8); S5.11+S6.7-versioning (→ one card in C6); S4.17 keeps extraction-routing only, mechanics live in C14. Each merge leaves an xref chip at the vacated location.
**Splits:** none — S10 is sub-grouped, not split, to keep nav ↔ source-section mapping 1:1.

Estimated total: **~60 concept cards** (vs file 1's 20) — proportional to a source ~4× the size of file 1's session notes.

---

## 4. Visual Encoding Plan

**Inherited models reused:** compare (good/warn 2-col), stack, esc-table, dva-table, type-gate diamond, conf-flow, prov-chain, signal-bar, hub-diagram, mcp-row (3-up), channels, flag/schema/sess-pair, batch-rule grid, attention-window gradient, pill.

**New model types required by file 2's concept shapes (7):**

| New model | Shape it serves | Anatomy |
|---|---|---|
| **N1 Ledger** | three-way responsibility split | 3 columns (Model / Code / Interface) with duty chips under each; C0's signature |
| **N2 Precedence cascade** | override hierarchies | stack rows + a "wins ↑" arrow rail and a crossed-out losing entry (MCP scopes, CLAUDE.md levels) |
| **N3 Prefix ruler** | positional cache invariant | horizontal segmented bar `[tools][system][messages…]` with breakpoint flags and a red "byte changed here → everything right of this is void" strike |
| **N4 Time-budget bar** | additive deadline arithmetic | segments `[cadence][24h batch][buffer]` summing against an SLA end-stop (C14) |
| **N5 Triad triangle** | three-legged risk | triangle with legs labeled private data / untrusted content / outbound channel, one leg shown cut (C15) |
| **N6 Spectrum strip** | graded capability/cost | Haiku→Sonnet→Opus gradient bar with role labels (reuses attention-window CSS mechanics) |
| **N7 Gauntlet strip** | scenario→pattern mapping | numbered rows: trap phrase (stop color) → winning pattern (go color) → chapter chip |

### Per-item encoding assignments

*(Encoding + one-line recall rationale. Items sharing a card are grouped.)*

**C0:** S0.1+S0.2 → **N1 Ledger** — the three-column spatial split *is* the exam's master question; every later "code vs prompt" card echoes its geometry.

**C1 · The Request**
| Items | Card | Encoding | Why it aids recall |
|---|---|---|---|
| S1.1, S1.2 | Statelessness | signal-bar ("request contains it → model sees it / not sent → doesn't exist") + pill `session_id` | Binary fact needs binary geometry |
| S1.3, S1.11(p1,p2) | Conversation growth | attention-window-style rising gradient (tokens→cost→latency) | Growth is a continuum; gradient encodes monotonic worsening |
| S1.4 | API shape | stack (system param / messages / content blocks) | Layered request anatomy = layer diagram |
| S1.5, S1.6, S1.11(p5) | Output routes + tool_choice | compare (response-is-JSON vs structured-tool-call) + esc-table for the 4 `tool_choice` rows | The 4-way setting is tabular by nature; the route choice is a contrast |
| S1.7, S1.9, S1.11(p3,p4) | Extraction recipe + ops facts | prov-chain (schema → force tool → validate → feedback loop arrow) | The feedback *loop-back* arrow is the memorable deviation from a straight pipeline |
| S1.10 | Prefill legacy | dva-table (old use → modern replacement, 4 rows) with a struck-through "trailing assistant turn" pill | Replacement mapping is a two-column translation table |

**C2 · The Tool Contract**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S2.1 | Description contract | compare (weak vs strong description) — direct reuse of file 1's D2.1 model | Proven encoding for this exact concept family |
| S2.2, S2.3 | Where tools run | esc-table (4 rows × who-defines / who-executes / trust) + tenet for Bash-vs-send_email | Four execution models = a matrix, not prose |
| S2.4, S2.7, S2.15(p1,p2) | Parameter design + tool splitting | schema-pair (unified `manage_order` warn vs split tools go) | Side-by-side schema fragments make "invalid combinations unrepresentable" visible |
| S2.5, S2.6 | Lookup-then-act | prov-chain (search → IDs+metadata → user picks → act-on-ID) | Disambiguation is a pipeline with a human node |
| S2.8, S2.9, S2.10, S2.15(p3) | Output design + pagination + empty-result | compare (prose blob warn vs structured IDs go) + pill "empty = success" | The empty-result rule is a one-pill exam literal |
| S2.11, S2.15(p4) | Composition | type-gate diamond ("judgment between steps?" → keep separate / combine) | It's a decision gate; the diamond is the gate shape |
| S2.12 | Progressive availability | hub-diagram variant: discovery tool → shortlist → dynamically registered spokes; warn box for `find_and_execute` | Expansion topology; the anti-pattern sits beside it in warn color |
| S2.13, S2.14, S2.15(p5) | requires_review + preview-token | prov-chain (preview → token → user confirms → execute-with-token) + warn pill `dry_run` | The token hand-off chain is the thing to reproduce on the exam |

**C3 · The Error Channel**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S3.1, S3.7(p1,p4) | Five categories | esc-table (category / example / handling — direct source-table lift into mono style) | Multi-row mapping = table |
| S3.2, S3.6 | Retry placement | conf-flow fork (failure → tool retries / model corrects / human approves) with the 8%/4% split as labels | Routing decision = threshold-fork geometry |
| S3.3, S3.7(p2,p3) | Uncertain writes | channels (read timeout: retry-safe / write timeout: state unknown) | Two wires, opposite policies — file 1's channel model fits exactly |
| S3.5 (+S7.7 merged) | MCP error tiers | channels (JSON-RPC: never ran / isError: ran and failed) + the 3-case `check_availability` rows as tenets | Same dual-wire shape as file 1's D2.4 — deliberate visual rhyme aids transfer |

**C4 · The Extraction**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S4.1 | Goal ladder | stack (syntactic → semantic → traceable → safe) | Ascending guarantee levels = layers |
| S4.2, S4.4, S4.6, S4.18(p2,p3) | Absence semantics | esc-table (situation → schema pattern, 5 rows) + pill "required field = fabrication pressure" | The 5-row mapping is the exam's favorite discriminator set |
| S4.3, S4.18(p4) | Enum escape hatch | schema-pair (strict enum warn vs `other`+detail go) | Schema fragments side-by-side |
| S4.5 | Verification-call anti-pattern | compare (verify-pass warn vs fix-the-schema go) | Contrast of interventions |
| S4.7, S4.16 | Few-shot + feedback loop | loop-flow (corrections → recurring pattern → few-shot example → re-measure) | Improvement is a cycle; loop shape encodes it |
| S4.8 | Provenance | prov-chain (value + location + quote + date traveling together) — reuse of file 1's D5.5 chain | Visual rhyme with the sibling sheet's provenance card |
| S4.9, S4.10, S4.11 | Semantic validation + retry gate | type-gate ("why did it fail?" → feedback-fixable / info-absent → enrich, don't retry) + reconciliation-fields snippet | Identical gate to file 1's D4.8 Type 1/2 — same geometry, richer branches |
| S4.12 | Chunk vs summarize | compare-3 (chunk / pre-extraction summarize / raw+few-shot-warn) using mcp-row 3-up layout | Three strategies with distinct failure modes = triad boxes |
| S4.13, S4.14, S4.15, S4.18(p5) | Calibration + automation gates | conf-flow (calibrated threshold → automate / review) + tenet "segment before threshold; stratified sampling after" | Extends file 1's D5.4 with the segment-first gate |
| S4.17, S4.18(p6) | Batch extraction routing | batch-rule grid (urgent → realtime / standard → batch / bulk-deadline → all-in-then-resubmit) | Condition→action grid, file 1's D4.9 shape |

**C5 · The Context**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S5.1 | Need→strategy map | esc-table (6 needs → 6 strategies) | This table is the chapter's master key; keep it tabular |
| S5.2, S5.12(p3) | Sliding window | attention-window variant: timeline bar with recent-turns kept, older faded; RAG sub-window inset | Positional retention is inherently spatial |
| S5.3 | Progressive summarization | compare (vague prose warn vs structured Decisions/Prefs/Questions/Facts go) | The structured-summary format itself is the answer |
| S5.4, S5.5, S5.12(p2) | Reference sections + structured state | stack (retained reference block / state object / summarized middle / verbatim recent) + pill "surface conflicts, never average" | The layered context layout is the design being taught |
| S5.6, S5.7 | Retrieval + compression | compare (accumulate 40-field payloads warn vs compress + on-demand re-injection go) | Contrast of context hygiene |
| S5.8 | API-native vs application-level | channels (compaction: summarize / context editing: prune) + tenet on composition and the stop-reason trigger | Two server-side wires with different verbs |
| S5.9, S5.10, S5.12(p4) | Returning users + external updates | loop-flow (return → structured summary → fresh lookups → answer) with warn fork on "resume stale transcript" | Sequence with a poisoned branch |

**C6 · The Prompt**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S6.1, S6.2, S6.10(p1) | Every-request + attention weakening | signal-bar (omitted → diverges immediately / included → still competes) + attention-window mini | The two distinct failure mechanisms must not blur — two visuals, one card |
| S6.3 | XML sections | stack (`<role>/<style>/<safety>/<examples>`) | Prompt anatomy = layers |
| S6.4 | State placement vs caching | compare (rewrite system prompt warn vs inject state late go) + xref chip → C13 | The trade-off is the concept |
| S6.5, S6.10(p2) | Principles vs conditionals | flag-pair (principle: judgment integration / conditional: safety bright-line) with warn note on conditional explosion | Paired-box dichotomy |
| S6.6, S6.7, S6.10(p3) | Few-shot + reinforcement | dva-table (mechanism: dilution → breakpoint reminders / rule-wall → contrasting examples) — extends file 1's D4.3 table with the fix rows | Mechanism/cause/fix rhythm already proven |
| S6.8 | Clarify vs assume | type-gate ("risk + ambiguity?" → one focused question / proceed with stated assumption) + pill "name the tension, don't average" | Decision gate shape |
| S6.9, S6.10(p4) | Format control | compare ("never say X" list warn vs style instruction + example go) | Contrast |

**C7 · The Protocol**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S7.1, S7.2 | Primitives + controllers | mcp-row 3-up (Tools/model · Resources/application · Prompts/user) — file 1's D2.2 upgraded with the controller row | Direct visual continuity with the sibling sheet |
| S7.3, S7.11(p1) | Resource vs tool rule | type-gate ("stable reference or live computation?") + warn box "NL aggregator tool" | Decision gate |
| S7.4, S7.11(p2) | Why MCP + what it doesn't do | flag-pair (does: reuse across clients / does NOT: auth, retries, rate limits, caching) | Claims/non-claims pairing kills the classic trap |
| S7.5, S7.8, S7.11(p4) | Registry + discovery | hub-diagram (host registry ← servers) + tenets on description competition and `list_changed` | Topology |
| S7.6, S7.11(p3) | Annotations | compare (UI affordance go vs security boundary stop) with the 4 hint pills | The four hint names are exam vocabulary — pills make them literal |
| S7.9, S7.10 | Claude Code scopes | **N2 precedence cascade** (local > project > user, whole-entry-wins strike-through on losers) + file-location labels | Precedence with a visible loser is the fact pattern exams probe |

**C8 · The Orchestra**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S8.1 | The loop | loop-flow (observe → reason → act ↺) — file 1's D1.1 lineage | Continuity |
| S8.2, S8.3, S8.12(p1) | Five patterns | esc-table (pattern / best-for / avoid-when, 5 rows) + tenet contrasting billing-chain vs incident-triage | The avoid-when column is what distinguishes an architect answer |
| S8.4 | When not to delegate | batch-rule grid (small + in-context → coordinator does it / floods context, needs persona, parallelizable → delegate) | Condition→action |
| S8.5, S8.9, S8.12(p3) | Partition-then-parallel | prov-chain (serial decompose → parallel fan → serial synthesize) with "elapsed = max, not sum" pill | The three-phase shape plus the latency formula is the whole answer |
| S8.6 (+S10.22 merged) | Subagent isolation | hub-diagram with an explicit "no memory" barrier on each spoke — extends file 1's D1.3/4 | Same hub, new barrier glyph = incremental schema on an existing memory |
| S8.7, S8.11, S8.12(p2,p4) | Handoffs + provenance | compare (poor "synthesize the findings" warn vs structured claim-source index go) + prov-chain for claim+date pairs | Contrast + chain, both proven |
| S8.8 | Task tool gating | signal-bar (Task in parent allowedTools → can delegate / absent → silent failure) | Binary gate with a silent failure mode — bar makes it loud |
| S8.10 | State manifests | stack (manifest.json / agent-state / structured exports) — file 1's D5.3 lineage | Continuity |

**C9 · The Front Line**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S9.1, S9.2, S9.8(p1) | Escalation | esc-table (trigger rows) + the handoff-payload field list as pills — file 1's D1.6 lineage with "not counters" warn tenet | Continuity |
| S9.3 | Frustrated users | compare (silent action / interrogation warn vs acknowledge + offer choice go) | Behavioral contrast |
| S9.4, S9.6, S9.8(p2) | Threshold in the tool | **N1 Ledger echo**: mini three-column showing the rule living in the code column; struck-through `approved_by_manager` param | Reuses C0's geometry — the spine made concrete |
| S9.5 | Single-use tokens | prov-chain (preview → token bound to payload → confirm → execute consumes token) | Same chain as C2's card, upgraded with token-binding tenets — deliberate rhyme |
| S9.7, S9.8(p3,p4) | Graceful degradation | stack (done / pending / next steps) + pill "repeated same failure → switch strategy" | The three-part progress report is a template to memorize |

**C10 · The Workbench** *(sub-group A: Working)*
| Items | Card | Encoding | Why |
|---|---|---|---|
| S10.1, S10.2 | Tool selection | esc-table (task → tool, 7 rows) + gg-pair Glob/Grep inset — file 1 D2.5 lineage | The Glob/Grep pair is already a proven visual |
| S10.3, S10.4 | Exploration | loop-flow (grep entry → read → follow imports → trace → scratchpad) | Sequence |
| S10.5, S10.6, S10.23(p1,p2) | Plan mode | type-gate ("broad/risky/architectural?" → plan / direct) + flag-pair (plan mode: workflow gate / extended thinking: reasoning depth) | Gate + the exam's favorite false-synonym pair |
| S10.7, S10.8, S10.23(p3) | Sessions | esc-table (4 flags → behavior → best use) + pill "fork-session + worktree" | Flag table is rote-recall material; table it |
| S10.9, S10.10 | Self-review + scratchpads | compare (same-session review warn vs fresh context go) + stack for scratchpad files — file 1 D5.3/D3.6 lineage | Continuity |

*(sub-group B: Memory & Config)*
| Items | Card | Encoding | Why |
|---|---|---|---|
| S10.11, S10.23(p5) | Two memory systems | channels (CLAUDE.md: you write / auto memory: Claude writes) + stop pill "context, not enforcement" | Dual-wire |
| S10.12, S10.13 | CLAUDE.md hierarchy | **N2 precedence cascade** (managed → user → project → local, load-order arrow, lazy-subdir annotation) | Same cascade model as C7's MCP scopes — one geometry for all precedence facts |
| S10.14, S10.18, S10.23(p4) | Rules + scoping | type-gate ("always? / area? / activity? / must-hold?") fanning to CLAUDE.md / rules / skill-slash / hook + warn tenet on the review-checklist misuse | This one gate resolves the exam's whole mechanism-choice family |
| S10.15 | Auto memory | stack (MEMORY.md 200-line/25KB head / topic files on demand) with machine-local pill | Layered loading |
| S10.16, S10.17 | Four mechanisms + debugging | esc-table (mechanism / loaded when / soft-hard / use-for, 4 rows) + pills `/memory`, `InstructionsLoaded` | The source's own table, in the sheet's grammar |
| S10.19, S10.20 | Skills vs slash | flag-pair (skill: task-recognized / slash: human-invoked) + "progressive disclosure" tenet chip → C2's progressive-availability | Dichotomy + family link |
| S10.21, S10.23(p6) | Hooks | esc-table (4 lifecycle events → capabilities) + stop tenet "hooks are code with your privileges" — file 1 D1.5 lineage | Continuity |

**C11 · The Feedback Loop**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S11.1, S11.2, S11.6(p1) | Concrete feedback | compare (vague "handle edge cases" warn vs failing input + expected + actual go) + pill "prompt fixes generalize; retries don't" | Contrast |
| S11.3 | Test quality | tenets-only card with warn pills for the five low-value patterns | List-shaped concept; pills carry the pattern names |
| S11.4, S11.6(p3) | Review agents | compare ("be conservative" warn vs criteria + few-shot pair go) + dismissal-field pills — mirrors C4's S4.16 with xref chip | Deliberate rhyme |
| S11.5, S11.6(p2,p4) | Segment evaluation | conf-flow variant: aggregate 97% bar splitting into per-segment bars, one red | Seeing the hidden failing segment *is* the concept |

**C12 · The Dials**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S12.1, S12.8(p1) | Tiers | **N6 spectrum strip** (Haiku→Sonnet→Opus with role labels) + "consult docs, not memory" tenet | Graded capability = gradient |
| S12.2, S12.8(p2) | Allocation patterns | conf-flow (cheap router → most traffic cheap / signal → escalate) + pill "escalate on signal, not anxiety" | Routing fork |
| S12.3 | Adaptive thinking/effort | dva-table (legacy fixed budget → deprecated / adaptive + effort → current) | Old-vs-new translation |
| S12.4 | Streaming | batch-rule grid (human watching → stream / long output → stream / batch, M2M → skip) | Condition→action |
| S12.5, S12.8(p3,p4) | Stop reasons | esc-table (7 rows) with `max_tokens` vs `model_context_window_exceeded` contrast highlighted — extends file 1's D1.1 signal-bar into the full set | The full table is new territory vs file 1; must be tabular |
| S12.6, S12.7, S12.8(p5) | API errors + token counting | esc-table (429/500-529/400 → handling) + pills "SDK auto-retries", "no third-party tokenizers" | Mapping table |

**C13 · The Cache**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S13.1 | Prefix invariant | **N3 prefix ruler** — the chapter's signature visual | The positional "everything right of the change dies" fact is purely spatial |
| S13.2, S13.3, S13.6(p1,p2) | Invalidators | tenets card with 5 stop-pills (timestamp / unsorted JSON / early IDs / flag sections / tool-model swap) under a mini ruler with strike marks | Five named killers as literal chips = recall list |
| S13.4, S13.6(p5) | Breakpoints + verification | stack (≤4 breakpoints / TTL 5m-1h / minimum size) + go pill "read usage fields; zero reads = invalidator" | Parameter facts |
| S13.5, S13.6(p3,p4) | Right-lever matching | batch-rule grid (repeated prefix→cache / deferrable→batch / over-tiered→smaller model / bloat→trim) + stop pill "caching ≠ capacity" | This quartet grid is the cross-chapter keystone (chipped from C12, C14) |

**C14 · The Batch**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S14.1, S14.2, S14.3 | Mechanics + fit | flag-pair (fits: volume, deferrable, independent / doesn't: interactive, deadline, dependent) + pills "50%", "24h" | The two numbers as pills — exam literals |
| S14.4, S14.8(p2) | custom_id | signal-bar (join by custom_id → correct / join by position → corrupt) | Binary with a corruption consequence |
| S14.5 | SLA arithmetic | **N4 time-budget bar** (cadence + 24h + buffer segments against the SLA end-stop, 30h→6h worked example inline) | The additive-segments-must-fit picture makes the formula derivable, not memorized |
| S14.6, S14.7, S14.8(p1,p3,p4) | Failure handling + stacking | batch-rule grid (failure type → targeted fix) + xref chip → C13 lever grid | Condition→action |

**C15 · The Perimeter**
| Items | Card | Encoding | Why |
|---|---|---|---|
| S15.1 | Two untrusted flows | channels (model output → your systems / external content → the model), both marked untrusted | Dual-wire, both hot |
| S15.2, S15.3, S15.7(p1,p3) | Injection + defenses | compare (prompt-level defense warn vs 4 architectural defenses go, listed as pills) | Contrast at the right altitude |
| S15.4 | Exfiltration triad | **N5 triad triangle** with one leg cut | The three-legs image is the source's own compact heuristic — draw it |
| S15.5, S15.7(p5) | Supply chain | stack (MCP servers / hooks / dependencies — all "code you chose to trust") | Same-treatment layers |
| S15.6, S15.7(p4) | Secrets hygiene | prov-chain showing a secret propagating (context → transcript → logs → cache) with stop coloring; go alternative "inject at execution layer" | The propagation chain is why the rule exists — showing it beats stating it |

**Coda CX:** S17(c) → numbered 8-question checklist card (mono numbered list, each question tagged with its owning chapter chip); S18 → **N7 gauntlet strip** (15 rows). **Appendix:** S19 → muted two-column link list grouped by chapter.

Every inventory item S0.1–S15.7 plus the four meta-treatments has an assignment above. Pitfall items (S*.pitfalls) are distributed as stop-colored trap tenets in the cards indicated — none are dropped, none get standalone cards.

---

## 5. Interconnection Map

Three mechanisms, in increasing locality:
- **Narrative connector** (G3) — inter-card story prose (why next).
- **Bridge line** (G5) — last line of each card (hand-off to the next card). Every card gets one; not itemized here.
- **Xref chip** *(new mechanism)* — a small mono pill inside a tenet, `→ C13 · prefix ruler`, linking non-adjacent cards. New because file 2, unlike file 1's linear session notes, is densely self-cross-referencing across distant sections; bridges alone cannot carry non-adjacent links.
- **Spine echo** *(new mechanism)* — C0's ledger geometry recurs in miniature wherever the "code enforces / prompt influences" law resolves a card (C9 threshold card, C10 hooks, C15). A repeated shape as a motif, not a link.

| # | Relationship | Concepts | Mechanism |
|---|---|---|---|
| R1 | The responsibility spine resolves ~10 cards | S0.1 ↔ S2.14, S6.5, S9.4, S9.6, S10.11, S10.21, S15.1 | Spine echo + xref chip → C0 |
| R2 | Validation-error feedback loop is one pattern at two scales | S1.7 ↔ S4.9 | Xref chips both ways; identical loop-flow geometry |
| R3 | Prefill legacy ↔ format control replacement | S1.10 ↔ S6.9 | Xref chip |
| R4 | Token cost of schemas ↔ context physics ↔ caching economics | S1.8 ↔ S5.1/S5.12 ↔ S13.1 | Narrative connector opening C13 names the thread |
| R5 | Preview-then-execute appears at three altitudes (tool design, compliance, security gate) | S2.14 ↔ S9.5 ↔ S15.3 | Same prov-chain geometry in all three + xref chips; C9 narrative names it "the same chain, now with teeth" |
| R6 | Disambiguation vs preview-execute complementarity (*which entity* vs *what action*) | S2.5 ↔ S2.14 | Bridge line between the two C2 cards |
| R7 | Progressive-disclosure family | S2.12 ↔ S7.8 ↔ S10.19 (skills) | Xref chips; shared tenet phrase "pay tokens only for what you're about to use" |
| R8 | MCP error tiers owned once, referenced twice | S3.5 ↔ S7.7 | Merged card in C3; C7 carries an xref chip instead of a duplicate |
| R9 | Uncertain writes ↔ no-retry policies downstream | S3.3 ↔ S9.7/S9.8 ↔ S14.6 | Xref chips |
| R10 | Calibration family: thresholds ↔ segment eval ↔ escalate-on-signal | S4.13/S4.15 ↔ S11.5 ↔ S12.2 | Narrative connector opening Act IV: "every dial in this act is turned by a measurement, not a feeling" + chips |
| R11 | Batch extraction routing ↔ batch mechanics | S4.17 ↔ S14.1–14.5 | Xref chips both ways |
| R12 | Freshness-vs-cache-stability triangle | S5.10/S5.11 ↔ S6.4 ↔ S13.2/S13.3 | This is the guide's subtlest cross-cut: dedicated narrative connector in C13 + chips in C5/C6 |
| R13 | Capacity ≠ attention | S5.12(p1) ↔ S6.2 ↔ S1.3 | Shared attention-window visual language |
| R14 | Tool-result compression = data minimization (focus rationale vs security rationale) | S5.7 ↔ S15.6 | Xref chip in C15: "same act, second reason" |
| R15 | `model_context_window_exceeded` trigger ↔ stop-reason table | S5.8 ↔ S12.5 | Xref chip |
| R16 | Subagent isolation owned once | S8.6 ↔ S10.22 | Merged in C8; C10 subagent card chips to it and keeps only Claude Code config specifics |
| R17 | Tool restriction: focus rationale ↔ least-privilege rationale | S8.8 ↔ S15.3 | Xref chip in C15 |
| R18 | Hooks: mechanism ↔ compliance use ↔ supply-chain risk | S10.21 ↔ S9.4 ↔ S15.5 | Chips; C15 narrative: "the enforcement layer is itself an attack surface" |
| R19 | Cost-lever quartet is the keystone of Act IV | S13.5 ↔ S12.1 ↔ S14.2 ↔ prompt-trimming | The lever grid lives in C13; C12 and C14 both chip to it |
| R20 | SLA arithmetic ↔ gauntlet Scenario 14 | S14.5 ↔ S18 | Gauntlet row chips back to C14's time-budget bar |
| R21 | Each gauntlet scenario ↔ its owning chapter (15 links) | S18 ↔ C1–C15 | N7 strip's chapter chips — doubles as a whole-sheet self-audit |
| R22 | The 11 design-duel pairs from Study Strategy | S17(b) ↔ their compare panels (S9.4-vs-S6.5 hook/prompt, S4.3 enum/string, S5.2/S5.3 window/summary, S3.6 retry placement, S14/S4.17, S5.9/S10.8 resume/fresh, S2.7 split, S8.7 handoff, S13.5 levers, S6.4 frozen prompt, S12.2 router) | Each hosting card gets a small "⚔ duel" chip marking it as a known exam contrast |
| R23 | Session forking ↔ worktree isolation | S10.7 ↔ S10.8 | Bridge line inside C10 |
| R24 | Empty-result-is-success ↔ error-category table | S2.9 ↔ S3.1/S3.7 | Xref chip |
| R25 | Annotations-not-security ↔ supply chain | S7.6 ↔ S15.5 | Xref chip |

---

## 6. Pacing & Anti-Overwhelm Plan

The core risk: this source is ~4× file 1's density; a naive port would be a 60-card wall. Mitigations:

1. **Two-tier nav.** Sticky nav holds four **act pills** + coda (5 targets — same count as file 1's nav, so the top-level cognitive map stays small). Each act opens with an **act divider**: one serif line stating the act's question + a mini-TOC of its 3–5 chapters. Scroll-spy highlights act, and a slim secondary indicator shows the current chapter. The reader never faces "15 chapters" as a flat list.
2. **Chapter budget: ≤ 8 cards.** Enforced by the merges in §3. C10 (10 cards) is the single exception and gets internal sub-group headers ("Working" / "Memory & Config") as rest points.
3. **Visual-to-text ratio ≥ 1 model per card, tenets ≤ 4 per card.** Anything beyond four tenets means the card must split or a tenet must demote to the gauntlet/appendix. Pitfalls arrive as at most 2 trap tenets per card (they share phrasing with the source's pitfall bullets, so no coverage is lost — several pitfalls per section restate the card's own go-pattern inverted).
4. **Consistent grammar = amortized learning cost.** Every card has identical anatomy (G4); precedence facts always use the cascade (N2), decisions always the diamond, contrasts always compare-cols. After Act I the reader parses cards pre-attentively.
5. **Progressive structure.** Act I is deliberately the most concrete (requests, tools, errors, one worked extraction system); abstraction rises act by act; the coda is pure application. The spine card (C0) is one screen and gives the whole sheet a single organizing question before any detail.
6. **Length dampers at the edges.** The gauntlet is a strip (15 one-line rows), not 15 cards; the Source Map is muted and collapsed-by-styling; the Quick Reference section adds zero length (audit-only).
7. **Rhythm.** Narrative connectors appear at every chapter open and between concept clusters (~every 2–3 cards), matching file 1's cadence — prose valleys between visual peaks.
8. **Estimated total length:** ~3.5× file 1 (~4,500 rendered lines). Acceptable given 4× source scope; the act structure means a study session naturally consumes one act (~12–18 cards), which is a deliberate session-sized chunk.

---

## 7. Eval Self-Score

**E1 — Coverage.**
*How met:* 129-item inventory built section-by-section with line ranges; every item has a card + encoding assignment; the four meta-sections have explicit treatments rather than silent omission; S16 (Quick Reference) is repurposed as a mechanical coverage audit — every one of its ~130 bullets must be traceable to a tenet before the artifact ships, which gives E1 a built-in second check independent of the inventory.
*Biggest risk:* sub-bullet attrition during authoring — an inventory item like S5.5 bundles five "why alternatives fail" sub-points, and the 4-tenet budget pressures silently dropping the fourth and fifth. Mitigation is the S16 audit pass plus a final inventory-to-artifact checklist sweep, but the sweep must actually be run, not assumed.

**E2 — Visual encoding.**
*How met:* every inventory item is assigned a named model matched to its concept shape (binary→bar, precedence→cascade, additive time→budget bar, positional→ruler, triad→triangle, mapping→table, contrast→compare); 7 new model types were created only where file 2 has shapes file 1 lacked; deliberate visual rhymes (same geometry for preview-token at three altitudes, one cascade for both precedence facts) turn repetition into reinforcement.
*Biggest risk:* table overuse — nine cards resolve to esc-table because the source is table-rich, and a run of tables reads as a spreadsheet, not a visual. Mitigation: no two adjacent cards may both be tables (reorder within chapter or convert one to pills/pairs); this constraint is checked at layout time and is the most likely rule to get violated under authoring pressure.

**E3 — Interconnection.**
*How met:* four mechanisms at four ranges (bridge on every card, narrative every 2–3 cards, 25 mapped xref-chip relationships for non-adjacent links, spine-echo motif for the document's one universal law); duplicated source content is merged to a single owner with chips pointing home, so relationships are structural, not just annotated.
*Biggest risk:* chip inflation — 25 relationship families could yield 50+ chips, and past a density threshold chips become noise the eye skips, destroying exactly what E3 wants. Mitigation: hard cap of 2 xref chips per card; relationships beyond the cap ride in narrative connectors instead. The cap forces triage, and the triage judgment (which link matters most for recall) is the residual risk.

**E4 — Structure / calm ingestion.**
*How met:* two-tier nav keeps the top-level map at 5 items; acts are session-sized chunks with question-framed dividers; uniform card grammar amortizes parsing cost; chapter budget ≤ 8 cards; meta-content pushed to a strip and a muted appendix; concrete-to-abstract act ordering with a single opening spine card.
*Biggest risk:* absolute length. Even perfectly structured, ~60 cards is a long scroll, and the "one calm document" impression degrades if a reader lands mid-sheet without the act frame. Mitigation: the act dividers repeat orientation cues (act question + position "Act III of IV"), and the nav is sticky — but if Ram finds the built artifact heavy at review, the fallback lever is demoting C10 sub-group B and the C12 tables to denser multi-item cards (file 1's G9 pairing), cutting ~10 cards at a known, bounded cost to E2 granularity. That trade would be his call, not a silent one.

---

**Pre-finish verification:** all of file 2's top-level sections (Overview, §1–§15, and meta §16–§19) appear in the Concept Inventory with major concepts itemized and line ranges (129 items + 4 meta-treatments) ✓ · every inventory item has an encoding assignment in section 4 (pitfalls explicitly distributed as trap tenets; meta-sections explicitly encoded as checklist card, gauntlet strip, audit pass, and source map) ✓ · no section of this plan contains finished cheat-sheet prose — all card contents are described, not written ✓
agentId: acb914c67051e0366 (use SendMessage with to: 'acb914c67051e0366', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 190882
tool_uses: 5
duration_ms: 979789</usage>