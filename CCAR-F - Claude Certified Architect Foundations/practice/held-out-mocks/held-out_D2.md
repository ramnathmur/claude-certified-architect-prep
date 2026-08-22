# Held-Out Mock Bank — Domain 2: Tool Design & MCP Integration (18%)

> HELD-OUT INTEGRITY: original questions only; no reuse of practice-bank/checkpoint/guide-sample/teaching stems. For Mock A / Mock B only. Scenario 8 excluded.

## Mock A — Domain 2 (11 questions)

### A-D2-01 · Scenario: Developer Productivity Tools · Type: Scenario/anti-pattern · Difficulty: Medium
A code-exploration agent has both a built-in `Grep` tool and a custom MCP tool `code_index_search` that queries a pre-built semantic index of the monorepo (it understands symbol references across language boundaries and resolves call graphs the agent cannot reconstruct from raw text matches). Telemetry shows the agent almost always reaches for `Grep` and rarely calls `code_index_search`, even on cross-language "find every caller of this function" tasks where the index is far superior. The MCP tool's description currently reads: `"Searches the codebase index."` What is the most effective fix?

A. Remove `Grep` from the agent's allowed tools so it is forced to use `code_index_search`.
B. Rewrite `code_index_search`'s description to spell out the unique capability built-in tools lack (cross-language call-graph resolution, symbol references the index resolves that text search misses) and state explicitly when to prefer it over `Grep`.
C. Rename `code_index_search` to `Grep2` so the model treats it as an upgraded version of the tool it already trusts.
D. Add a system-prompt rule: "Always call `code_index_search` before any other search tool."

### A-D2-02 · Scenario: — · Type: Concept/application · Difficulty: Medium
An MCP server exposes a `submit_expense_report` operation and also exposes the *company expense-policy categories and per-category spending caps* — a stable reference table that changes maybe twice a year. The team must decide how to expose the policy table. Which MCP primitive fits the policy table, and why?

A. A **tool** named `get_expense_policy`, because any structured data the model consumes must be reachable through a callable function with an input schema.
B. A **resource**, because the policy table is stable, read-only context the application can supply directly; modeling it as a resource means the model does not spend a tool call to "discover" what is true and unchanging.
C. A **prompt**, because the policy defines the workflow the model should follow when submitting an expense.
D. It should not be exposed at all; the model should infer the categories and caps from `submit_expense_report`'s error messages.

### A-D2-03 · Scenario: Multi-Agent Research System · Type: Scenario/anti-pattern · Difficulty: Hard
A market-data subagent calls an MCP tool `get_quarterly_revenue(ticker)`. For one ticker the upstream data provider is up and answers normally; for a second ticker the provider returns HTTP 503 (overloaded). The tool author wants the agent to be able to retry the 503 case but not retry a different situation where the *agent passed a ticker symbol that the provider's API does not recognize as a valid security*. How should the tool surface these two outcomes so the agent recovers correctly?

A. Return `isError: true` with `{"errorCategory": "transient", "isRetryable": true, ...}` for the 503, and `isError: true` with `{"errorCategory": "validation", "isRetryable": false, ...}` for the unrecognized ticker.
B. Return `isError: true` with identical `{"content": "lookup failed"}` for both, and let the agent decide based on the ticker.
C. Return the 503 as a JSON-RPC protocol error and the unrecognized ticker as `isError: true`.
D. Retry both internally up to five times, then return an empty result so the synthesis stage treats both as "no data found."

### A-D2-04 · Scenario: Conversational AI Architecture · Type: Scenario/anti-pattern · Difficulty: Medium
A travel-assistant chatbot has a single agent loaded with 19 tools: flight search, hotel search, car rental, weather, currency conversion, visa-rule lookup, loyalty-points balance, seat maps, baggage rules, airport-transfer booking, and more. Users report the assistant frequently calls the wrong tool — pulling a seat map when asked about baggage allowance, or checking weather when asked about currency. The architecture is otherwise sound. What is the most likely root cause and the best remedy?

A. The context window is too small; upgrade to a model with a larger window so all 19 tool schemas fit comfortably.
B. Too many tools in one agent degrades selection reliability; partition the tools by role into specialized agents (or scope each phase to a small, relevant subset) so each loop sees ~4–6 well-differentiated tools.
C. The temperature is too high; lower it so the model is more deterministic in tool selection.
D. Set `tool_choice` to `{"type": "any"}` so the model is always forced to call a tool, which will fix the misrouting.

### A-D2-05 · Scenario: — · Type: Concept/application · Difficulty: Hard
Distinguish the two error channels MCP exposes. In which scenario does the failure arrive as a **JSON-RPC protocol error** (the response itself is an error object), versus as a **tool-execution error carried inside a successful JSON-RPC response** (`isError: true`)?

A. Protocol error: a weather tool runs but the weather API times out. Execution error (`isError: true`): the client calls a tool name the server never registered.
B. Protocol error: the client calls `tools/call` for a tool the server does not expose / with a malformed arguments object. Execution error (`isError: true`): a registered `lookup_order` tool runs successfully but the orders backend returns a 500.
C. Both are protocol errors, because every failure is ultimately a violation of the JSON-RPC contract.
D. Both are `isError: true` execution errors, because the request reached the server in each case.

### A-D2-06 · Scenario: Developer Productivity Tools · Type: Recall · Difficulty: Easy
A teammate wants to commit the project's MCP server configuration so every engineer who clones the repo gets the same `github` and `jira` servers, but without leaking API tokens into version control. Which configuration approach is correct?

A. Put the servers in `~/.claude.json` and hard-code the tokens, since that file is per-user and safe.
B. Put the servers in a project-root `.mcp.json` committed to VCS, and reference secrets via environment-variable substitution (e.g., `"GITHUB_TOKEN": "${GITHUB_TOKEN}"`) so tokens are resolved at runtime, not committed.
C. Put the servers in `.mcp.json` with the literal token strings inline, and add `.mcp.json` to `.gitignore`.
D. Put the servers in the project `CLAUDE.md` so the configuration loads as context on every session.

### A-D2-07 · Scenario: Developer Productivity Tools · Type: Scenario/anti-pattern · Difficulty: Medium
An agent is asked to trace how a `RateLimiter` class is used across an unfamiliar Node.js service before proposing a change. The agent's first action is to `Read` all 60 files in `src/` into context, then reason about them. The lead architect flags this as wasteful and unreliable. What is the recommended built-in-tool investigation strategy instead?

A. `Glob` for `**/*.js`, then `Read` every matched file — globbing first guarantees nothing is missed.
B. Use `Bash` to `cat` the entire `src/` directory into one buffer so the model sees everything at once.
C. Incremental investigation: `Grep` for the `RateLimiter` definition/export to find entry points, `Read` those files, `Grep` for its imports/usages, `Read` the consumer files, and repeat until the picture is complete.
D. `Read` only the `README.md` and infer the rest of the usage from documentation.

### A-D2-08 · Scenario: Conversational AI Architecture · Type: Concept/application · Difficulty: Medium
A scheduling assistant exposes a reusable, user-invoked "set up a recurring 1:1" workflow — a templated multi-step procedure (ask for attendee, cadence, duration, then create the events) that the user triggers deliberately, surfaced to the user like a slash command. Which MCP primitive is this, and how is it controlled?

A. A **tool** — model-controlled; the model calls it autonomously whenever it judges a 1:1 is needed.
B. A **resource** — application-controlled passive context the model reads to understand scheduling preferences.
C. A **prompt** — a predefined template surfaced to the user and invoked explicitly, rather than triggered automatically by the model.
D. A **hook** — a deterministic interception point in the agent lifecycle.

### A-D2-09 · Scenario: Multi-Agent Research System · Type: Scenario/anti-pattern · Difficulty: Hard
A document-analysis subagent calls an MCP tool `fetch_filing(doc_id)`. The tool experiences a brief transient network blip on the upstream filings store. The tool author makes the subagent retry indefinitely inside the tool until the call succeeds. In production, when the filings store has a longer outage, the whole research run stalls for minutes per failing call and burns budget. What is the correct error-recovery design at the subagent/tool boundary?

A. Keep the infinite in-tool retry; transient failures always resolve eventually, so waiting is the safest choice.
B. Attempt 1–2 local retries with backoff for the transient failure, and if still unresolved, return a structured error (category `transient`, with any partial results) and propagate it to the coordinator to decide recovery — rather than blocking indefinitely.
C. On the first network blip, abort the entire research workflow so no partial work is wasted.
D. Catch the failure silently and return an empty filings list so the run continues smoothly.

### A-D2-10 · Scenario: — · Type: Concept/application · Difficulty: Medium
You are designing the structured payload an MCP tool returns when it fails. Which return body best supports autonomous agent recovery, and why does the alternative fail?

A. `{"isError": true, "content": "Something went wrong."}` — concise messages keep the context window small, which helps the agent recover.
B. `{"isError": true, "content": {"errorCategory": "business", "isRetryable": false, "message": "Refund exceeds the $200 self-service limit.", "attempted_query": "order=4471, amount=350"}}` — the category, retryability, human-readable reason, and attempted parameters give the agent enough to explain the situation and propose an alternative rather than blindly retrying.
C. `{"isError": false, "content": []}` — returning success with empty content lets the agent move on without being distracted by an error.
D. Throw an uncaught exception so the JSON-RPC layer records a protocol error and the host shows a generic failure dialog.

### A-D2-11 · Scenario: Developer Productivity Tools · Type: Scenario/anti-pattern · Difficulty: Medium
An agent needs to change a single, known line in `config/settings.py`. It calls `Edit` with the target text, but `Edit` fails because that exact text string appears in three places in the file (the match is not unique). What is the correct recovery, consistent with built-in-tool guidance?

A. Re-run the same `Edit` repeatedly until it happens to apply — non-determinism will eventually pick the right occurrence.
B. Provide a larger, uniquely-identifying surrounding context for the `Edit` match (or fall back to `Read` the file, modify the intended occurrence programmatically, then `Write`), so the change targets exactly one location.
C. Use `Bash` with `sed -i 's/old/new/'` to replace the first occurrence and accept whichever line it hits.
D. `Write` a brand-new `settings.py` from memory containing only the corrected line, discarding the rest of the file.

## Mock B — Domain 2 (11 questions)

### B-D2-01 · Scenario: Conversational AI Architecture · Type: Scenario/anti-pattern · Difficulty: Medium
A support assistant has two MCP tools: `find_account(query)` (locate an account by email, phone, or account number) and `get_account_summary(account_id)` (return balance, plan tier, and recent activity for a known account ID). Both descriptions currently say only `"Returns account information."` Agents frequently call `find_account` when they already hold an `account_id` and just need the summary, wasting a turn. What single change best resolves the confusion?

A. Merge the two tools into one `account(action, params)` tool so there is only one schema to choose from.
B. Differentiate the descriptions so each states what it does, its required input, and when to use it vs the other (`find_account`: "use when you have a lookup string but no ID"; `get_account_summary`: "use when you already hold an account_id").
C. Add few-shot examples in the user-facing chat history showing correct tool order.
D. Set `tool_choice` to `{"type": "tool", "name": "get_account_summary"}` for the whole conversation.

### B-D2-02 · Scenario: — · Type: Recall · Difficulty: Easy
In the Claude API, which `tool_choice` setting *guarantees* the model will emit a call to one specific named tool as its next action (e.g., to force a fixed first step in a pipeline)?

A. `{"type": "auto"}`
B. `{"type": "any"}`
C. `{"type": "tool", "name": "extract_metadata"}`
D. `{"type": "none"}`

### B-D2-03 · Scenario: Multi-Agent Research System · Type: Scenario/anti-pattern · Difficulty: Hard
A research coordinator exposes, through one MCP server: (1) a live `search_news(query)` action against a news API, (2) the *internal taxonomy of research topics and the schema of each stored report* (stable, read-only), and (3) a reusable "compile-a-literature-review" templated workflow that an analyst kicks off by hand. A junior engineer modeled all three as MCP **tools**. Which re-mapping to the correct primitives is right?

A. All three are correctly tools, since the model interacts with all of them.
B. `search_news` → tool; the taxonomy/report schema → resource; the literature-review workflow → prompt.
C. `search_news` → resource; the taxonomy/report schema → tool; the literature-review workflow → tool.
D. `search_news` → prompt; the taxonomy/report schema → prompt; the literature-review workflow → resource.

### B-D2-04 · Scenario: — · Type: Concept/application · Difficulty: Hard
Two failures occur against the same MCP server within one minute. (i) The client issues `tools/call` for `geocode_address`, but `geocode_address` was never registered on this server. (ii) A correctly-registered `geocode_address` is later called and runs, but the geocoding backend returns a 429 rate-limit. How does each failure travel back to the client?

A. (i) is a tool-execution error (`isError: true`) because the tool "failed to run"; (ii) is a JSON-RPC protocol error because rate limits are a transport concern.
B. (i) is a JSON-RPC protocol error (the request never reaches a valid tool — pre-execution); (ii) is a tool-execution error surfaced as `isError: true` inside an otherwise successful JSON-RPC response.
C. Both arrive as JSON-RPC protocol errors.
D. Both arrive as `isError: true` tool-execution errors.

### B-D2-05 · Scenario: Developer Productivity Tools · Type: Scenario/anti-pattern · Difficulty: Medium
A team's MCP integration vendor proposes one mega-tool, `repo_op(action, payload)`, where `action` is a free-text string like `"create_branch"`, `"open_pr"`, or `"merge"` and `payload` is an untyped JSON blob whose required fields depend entirely on `action`. The reviewing architect pushes back. What is the strongest tool-design objection and the better approach?

A. No objection — a single composite tool minimizes the number of schemas loaded into context, which is always optimal.
B. A composite "god-tool" with interdependent, action-dependent parameters hides distinct operations behind one opaque schema and weakens selection and validation; split it into discrete, well-described tools (`create_branch`, `open_pr`, `merge_pr`) each with its own typed parameter set.
C. The objection is only the tool's name; renaming it to `repository_operations` resolves the concern.
D. Keep the mega-tool but mark it `readOnlyHint: true` so the host validates the payload automatically.

### B-D2-06 · Scenario: Conversational AI Architecture · Type: Concept/application · Difficulty: Medium
A retail support agent has a system prompt that opens with: "Before responding to ANY message, ALWAYS confirm the customer's loyalty status." Engineers notice the agent now calls `get_loyalty_status` on nearly every turn — even for "what are your store hours?" — bloating latency and context. What does this illustrate, and what is the fix?

A. A protocol error in the loyalty tool; add retry logic to `get_loyalty_status`.
B. System-prompt wording can create unintended tool associations; the blanket "ALWAYS confirm loyalty" instruction over-triggers the tool. Scope the instruction to when loyalty actually matters (pricing, points redemption) so the model calls the tool only when relevant.
C. The agent has too few tools; add more so loyalty is not the default reach.
D. `tool_choice` is set to `{"type": "any"}`; switch it to `{"type": "tool", "name": "get_loyalty_status"}`.

### B-D2-07 · Scenario: Multi-Agent Research System · Type: Scenario/anti-pattern · Difficulty: Medium
A synthesis subagent calls an MCP tool that records a finalized brief to a shared store. The call sends the write request, then the connection drops before any acknowledgment returns — the tool cannot determine whether the brief was actually persisted. How should the tool report this, and what should happen next?

A. Silently retry the write up to three times until it returns success, to guarantee the brief is saved.
B. Return a structured error describing the **uncertain write state** (e.g., not retryable) and escalate/report rather than auto-retry, because blindly retrying a write whose outcome is unknown risks creating a duplicate brief.
C. Return `isError: false` with an empty body so the coordinator assumes the save succeeded and continues.
D. Treat it identically to a read timeout and retry immediately with exponential backoff.

### B-D2-08 · Scenario: — · Type: Recall · Difficulty: Easy
Match each MCP primitive to its control model and purpose. Which row is correct?

A. Tools = passive read-only context the application supplies; Resources = actions the model invokes; Prompts = error templates.
B. Tools = functions/actions the model can call (CRUD, API calls, commands); Resources = read-only data the agent reads for context (schemas, docs, catalogs); Prompts = predefined templates for common tasks, typically user-invoked.
C. Tools = user-invoked slash commands; Resources = lifecycle interception points; Prompts = functions the model calls.
D. Tools, Resources, and Prompts are interchangeable names for the same callable function abstraction.

### B-D2-09 · Scenario: Developer Productivity Tools · Type: Scenario/anti-pattern · Difficulty: Medium
An agent must locate every place a `LEGACY_FLAG` constant is referenced across a large repo, then open and edit the relevant files. A developer wired the agent to use `Glob` to find files by name patterns and to `Read` candidates one by one looking for the constant. The agent is slow and misses references in files whose names give no hint. Which built-in tool is the right primary instrument for the *search* step, and why?

A. `Glob`, because filename patterns are the most reliable way to find where a constant is used.
B. `Grep`, because it searches *within file contents* for the literal `LEGACY_FLAG` text across the repo, which is exactly the "find references inside files" job (`Glob` finds files by name/path, not by content).
C. `Bash` running `ls -R`, because listing every file is the only way to be exhaustive.
D. `Read` on the entire repo, because only loading every file guarantees no reference is missed.

### B-D2-10 · Scenario: Conversational AI Architecture · Type: Concept/application · Difficulty: Hard
An MCP tool `cancel_order(order_id)` returns this on a failed call: `{"isError": true, "content": {"errorCategory": "permission", "isRetryable": false, "message": "Caller lacks the cancel_order scope for this account."}}`. Given the four standard error categories and their prescribed agent responses, what should the agent do?

A. Treat it as transient and retry with exponential backoff until the scope is granted.
B. Treat it as validation and re-prompt itself to reformat the `order_id` argument.
C. Treat it as a permission error: do not retry; escalate to a human / an authorized path rather than attempting the action again.
D. Treat it as a business error and silently propose a partial refund instead.

### B-D2-11 · Scenario: Developer Productivity Tools · Type: Scenario/anti-pattern · Difficulty: Medium
A team adds a custom MCP tool `run_test_suite` to their dev agent. It currently has the description `"Runs tests."`, and engineers complain the agent sometimes calls it with no arguments (running the entire 40-minute suite) when they only wanted the unit tests for one module. Following tool-description best practice, which rewrite is strongest?

A. `"Runs tests."` is fine; the model should infer scope from the conversation.
B. `"Runs the project's automated tests. Accepts an optional `scope` (e.g., a module path or `unit`/`integration`/`all`; defaults to `all` — a 40-min full run). Use a narrow `scope` for fast feedback on a single module; reserve `all` for pre-merge or release checks. Returns per-suite pass/fail counts; an empty failure list means all selected tests passed."
C. `"A fast, powerful, enterprise-grade automated testing tool."`
D. `"Runs tests. Put the scope in the tool name like run_test_suite_unit so the model can't miss it."`

## Answer Key — Domain 2

### Mock A
- **A-D2-01** — Correct: B. The tool description is the primary selection mechanism; agents prefer built-in tools over MCP tools with vague, overlapping descriptions, and the fix is to strengthen the MCP description to highlight the unique data/capability built-ins lack and say when to prefer it. Why others fail: A (removing `Grep`) cripples the agent for the many cases where text search is correct and least-privilege/usefulness suffers; C (renaming to `Grep2`) is a name hack — names are not the selection mechanism and this invites worse confusion; D (a blanket "always call it first" system rule) over-triggers the tool and creates unintended associations, the wrong instrument for a description problem. Sub-domain: D2.1.
- **A-D2-02** — Correct: B. A stable, read-only reference table is "what is true and unchanging" — the canonical resource case (application-controlled passive context the model reads without spending a tool call). Why others fail: A wrongly asserts all consumable data must be a callable tool (resources exist precisely for this); C confuses a data table with a user-invoked workflow template (prompt); D forgoes grounding entirely and invites the model to infer policy from errors. Sub-domain: D2.2.
- **A-D2-03** — Correct: A. Both failures are tool-execution errors carried inside successful responses (`isError: true`), and they belong to different categories — transient/retryable for the 503, validation/non-retryable for the bad ticker — so the agent retries one and fixes-or-drops the other. Why others fail: B gives identical generic errors with no category, leaving the agent unable to decide; C mis-routes channels — a 503 from a tool that ran is not a JSON-RPC protocol error, and a bad-argument value handled by the tool is an execution/validation error, not necessarily a protocol error; D's infinite retry plus empty-as-success masks real failure and wastes budget. Sub-domain: D2.4.
- **A-D2-04** — Correct: B. Too many tools in one agent degrades selection reliability; the fix is scoped tool access — partition by role/phase so each loop sees a small, well-differentiated set. Why others fail: A confuses context *capacity* with selection *quality* — fitting 19 schemas does not make the model pick correctly; C (temperature) does not address tool ambiguity; D (`any`) forces a call but does nothing to make it the *right* call — it can worsen misrouting. Sub-domain: D2.5.
- **A-D2-05** — Correct: B. A protocol error is a JSON-RPC-level failure that occurs before/instead of valid execution (unknown tool, malformed arguments) — the response itself is an error; an execution error is a tool that ran inside a successful JSON-RPC response but failed at runtime (the 500), surfaced as `isError: true`. Why others fail: A inverts the two channels; C wrongly collapses runtime tool failures into protocol errors; D wrongly treats an unregistered-tool call (which never reaches a valid tool) as an execution error. Sub-domain: D2.4.
- **A-D2-06** — Correct: B. Project `.mcp.json` at the repo root is the VCS-shared, team configuration, and env-var substitution keeps secrets out of the commit while resolving them at runtime. Why others fail: A uses the user-scoped `~/.claude.json` (not shared) and hard-codes tokens; C commits literal secrets and only gitignores afterward (the secret may already be exposed and teammates lose the shared config); D puts server config in `CLAUDE.md`, which is instruction context, not MCP server definitions. Sub-domain: D2.3.
- **A-D2-07** — Correct: C. Incremental investigation (Grep entry points → Read → Grep usages → Read consumers → repeat) builds the picture without loading the whole tree, conserving context and improving reliability. Why others fail: A and B both bulk-load everything (glob-then-read-all / cat the directory), the exact waste being flagged; D under-reads by trusting docs and will miss real usages. Sub-domain: D2.6.
- **A-D2-08** — Correct: C. A reusable, user-invoked, templated multi-step procedure surfaced like a slash command is an MCP *prompt* (user/app-controlled, explicitly invoked, not auto-triggered). Why others fail: A makes it a model-controlled tool (wrong control model — it is deliberately user-triggered); B calls a procedural template passive context (resource); D confuses an MCP primitive with an Agent-SDK lifecycle hook. Sub-domain: D2.2.
- **A-D2-09** — Correct: B. Correct pattern is bounded local recovery (1–2 retries with backoff) for transient failures, then a structured error with any partial results propagated to the coordinator to decide — never blocking the run indefinitely. Why others fail: A's infinite in-tool retry is the named latency/resource anti-pattern; C aborts the whole workflow on one failure, discarding partial work; D silently suppresses the error as an empty result, hiding a real failure. Sub-domain: D2.4.
- **A-D2-10** — Correct: B. A structured body with category, retryability, a human-readable reason, and the attempted parameters lets the agent reason about recovery (here: explain the business limit and propose an alternative) instead of blind retry. Why others fail: A's generic "Something went wrong" strips all decision signal; C disguises a failure as empty success (silent suppression); D throws an exception for an expected business outcome and degrades it to a generic protocol-level failure. Sub-domain: D2.4.
- **A-D2-11** — Correct: B. When `Edit` fails on a non-unique match, supply more uniquely-identifying surrounding context, or fall back to Read → modify → Write, so exactly one location changes. Why others fail: A relies on non-determinism to land the right occurrence (unsafe); C's `sed` first-match replacement may edit the wrong line; D discards the entire file by rewriting it from memory. Sub-domain: D2.6.

### Mock B
- **B-D2-01** — Correct: B. The tools overlap only because both descriptions are vague; differentiating them by purpose, required input, and when-to-use-vs-the-other (the description is the selection mechanism) resolves the misrouting at lowest cost. Why others fail: A merges two clean operations into a composite tool — more opaque, not less; C puts examples in chat history rather than the tool definitions the model actually selects from; D forces one tool for the whole conversation, breaking the legitimate lookup case. Sub-domain: D2.1.
- **B-D2-02** — Correct: C. `{"type": "tool", "name": ...}` forces a call to that specific tool, guaranteeing a fixed first action. Why others fail: A (`auto`) leaves the choice to the model (may answer in text); B (`any`) guarantees *some* tool call but not *which* one; D (`none`) disables tool calls entirely. Sub-domain: D2.5.
- **B-D2-03** — Correct: B. The live news action is a model-controlled tool; the stable taxonomy/report schema is read-only application context (resource); the analyst-triggered templated workflow is a user-invoked prompt — the textbook three-primitive split. Why others fail: A leaves passive context and a user workflow miscast as tools; C and D scramble the mapping (e.g., making a live action a resource, or stable context a prompt). Sub-domain: D2.2.
- **B-D2-04** — Correct: B. An unregistered-tool call never reaches a valid tool — it fails at the JSON-RPC protocol layer (pre-execution), so the response itself is an error; a registered tool that runs but hits a 429 returns `isError: true` inside an otherwise successful JSON-RPC response. Why others fail: A inverts the channels; C wrongly makes the runtime 429 a protocol error; D wrongly makes the unregistered-tool call an execution error. Sub-domain: D2.4.
- **B-D2-05** — Correct: B. A composite god-tool with action-dependent, interdependent parameters hides distinct operations behind one opaque schema and weakens both selection and validation; splitting into discrete, well-described, typed tools is the sound design. Why others fail: A treats schema-count minimization as the only goal (it isn't — clarity and validation matter more); C reduces the problem to a naming issue; D misuses an untrusted annotation as if it provided host-side validation. Sub-domain: D2.1.
- **B-D2-06** — Correct: B. This is the classic "system-prompt wording creates unintended tool associations" effect — a blanket "ALWAYS confirm loyalty" over-triggers `get_loyalty_status`; the fix is to scope the instruction to situations where loyalty is actually relevant. Why others fail: A misdiagnoses it as a protocol/retry problem; C adds tools, which does nothing about the over-triggering rule; D blames `tool_choice`, but no forced-call setting is implied and forcing the tool would make it worse. Sub-domain: D2.1.
- **B-D2-07** — Correct: B. A write whose outcome is unknown (acknowledgment lost) is an uncertain-write state: report it as a structured, non-retryable error and escalate, because auto-retrying could duplicate the brief. Why others fail: A's silent triple-retry is exactly what risks duplicates; C disguises an unknown outcome as success (silent suppression); D treats an uncertain write like a safe-to-retry read, the core error. Sub-domain: D2.4.
- **B-D2-08** — Correct: B. Tools = model-callable functions/actions; Resources = read-only context the agent reads (schemas, docs, catalogs); Prompts = predefined templates for common tasks, typically user-invoked — the standard MCP primitive definitions. Why others fail: A swaps tools and resources; C scrambles all three (and conflates prompts/hooks); D wrongly claims they are interchangeable. Sub-domain: D2.2.
- **B-D2-09** — Correct: B. `Grep` searches *within file contents* for the literal text across the repo — the right instrument for "find every reference," whereas `Glob` finds files by name/path and misses content-only references. Why others fail: A uses filename patterns for a content-search job; C lists files but does not search their contents; D bulk-reads everything, the wasteful approach `Grep` exists to avoid. Sub-domain: D2.6.
- **B-D2-10** — Correct: C. A permission-category error is non-retryable; the prescribed response is to escalate to a human/authorized path rather than retry. Why others fail: A treats it as transient and retries (wrong category, never resolves); B treats it as validation and reformats the argument (the argument was fine); D fabricates a business-category remedy (a silent partial refund) the error does not warrant. Sub-domain: D2.4.
- **B-D2-11** — Correct: B. A strong description states what the tool does, its inputs and defaults, when to use a narrow vs full scope, its outputs, and edge-case behavior (empty failure list = all passed) — directly preventing the accidental full-suite run. Why others fail: A leaves the model to guess scope (the cause of the problem); C is marketing adjectives with no usage signal; D encodes the parameter in the tool name, a named anti-pattern (format/scope hints belong in the description, not the name). Sub-domain: D2.1.
