# CCA-F Practice — Domain 2: Tool Design & MCP Integration (18%)
_9 questions · original, exam-style · grounded in EXAM-DIGEST + D2 citations_

## Questions

**Q1.** Your team is building an MCP server for an internal travel-booking system. You expose the company's *list of approved hotel chains* and the *expense-policy document* so Claude can ground its recommendations. A junior engineer implements both as MCP **tools** named `get_approved_hotels` and `get_expense_policy` that Claude must call before every recommendation. The architect flags this as a primitive mismatch. Why is it wrong, and what is the correct primitive?
- A) It's correct as-is — anything Claude reads must be a tool, because only tools have JSON Schemas.
- B) The approved-hotel list and policy doc are stable, read-only context the application can supply directly; they belong as **resources** (application-controlled passive context), not tools the model must invoke.
- C) Both should be **prompts**, because the model uses them to shape its workflow.
- D) Both should stay tools but be marked with `readOnlyHint: true`, which converts them into resources at runtime.

**Q2.** A vendor pitches their MCP integration as "production-ready out of the box — because it's MCP, you get authentication, automatic retries, rate-limiting, and caching for free." As the reviewing architect, what is the most accurate response?
- A) Correct — MCP's data layer implements OAuth, exponential-backoff retries, and an LRU cache by spec, so those concerns are handled.
- B) MCP standardizes the *protocol for context exchange* (discovery, invocation, transport framing); it does **not** auto-solve auth, retries, rate-limiting, caching, or authorization — the server author must build those.
- C) Correct for remote (Streamable HTTP) servers only; stdio servers must implement it themselves.
- D) Half-correct — MCP provides retries and caching but leaves auth and rate-limiting to the host.

**Q3.** A security reviewer is auditing an MCP server. One tool, `delete_customer_records`, carries the annotations `{"destructiveHint": true, "idempotentHint": false}`. The reviewer wants to "rely on `destructiveHint` so the host automatically blocks the call unless an admin is logged in." What is the correct architectural judgment?
- A) Sound — `destructiveHint: true` is a hard security boundary the host enforces, so relying on it for admin gating is appropriate.
- B) Tool annotations are **untrusted UI hints**, not security boundaries; authority must be re-verified in code (server-side, on every call). Annotations can guide the UI but must never be the access-control mechanism.
- C) Sound, but only if `idempotentHint` is also `true`, since idempotency is what enforces the security check.
- D) Annotations are server-signed and tamper-proof, so trusting them is safe as long as the transport is TLS.

**Q4.** Claude calls your `transfer_funds` MCP tool. The tool sends the request to the payments backend, but the connection drops *after* the request is submitted and *before* a confirmation comes back — the tool cannot tell whether the transfer actually went through. How should the tool surface this, and what should happen next?
- A) Automatically retry the transfer up to 3 times inside the tool until it gets a clear success or failure.
- B) Return an empty/null result so Claude treats it as "nothing happened" and moves on.
- C) Return a structured error reporting the **uncertain write state** (e.g. `category: "uncertain", retryable: false`) and do **not** auto-retry — blind retry of an uncertain write risks a duplicate transfer; recovery is escalated, not silently retried.
- D) Throw an uncaught exception so the protocol layer records a JSON-RPC error and the host shows a generic failure.

**Q5.** Match the failure to the correct MCP error tier. The client sends `tools/call` with a tool name that the server never registered. Separately, a *different, correctly-named* tool runs but the upstream API returns HTTP 503. How are these two classified?
- A) Both are tool **execution** errors returned with `isError: true`, because both ultimately failed.
- B) Both are **protocol** errors, because both involve the `tools/call` method.
- C) The unknown tool name is a **protocol error** (JSON-RPC, pre-execution — the call never reaches a valid tool); the 503 is a **tool execution error** (`isError: true` — the tool ran but failed).
- D) The unknown tool name is an execution error; the 503 is a protocol error, because network failures are protocol-level.

**Q6.** You're designing a `book_meeting_room` tool. Its parameters interact: if `recurring` is `true`, then `recurrence_rule` and `end_date` become required and `single_date` must be omitted; if `recurring` is `false`, only `single_date` is allowed. The first draft crams all of this into one tool with a free-text `notes` field instructing Claude which fields to fill. What is the better design?
- A) Keep one tool but move the rules into the `description` as prose — descriptions are where conditional logic belongs.
- B) **Split into two tools** (e.g. `book_one_time_room` and `book_recurring_room`) so each has a clean, non-interdependent parameter set; interdependent-constraint parameters are a signal to split.
- C) Keep one tool and make every field `required` so the model can never omit one.
- D) Replace the typed fields with a single free-text `request` string and let Claude write the booking instruction naturally.

**Q7.** A reviewer rejects this tool description: `"description": "Searches records."` — and asks for a rewrite. Which description best follows tool-design guidance?
- A) `"Search."` — shorter is better because it saves tokens in the auto-injected tool-use system prompt.
- B) `"Searches the customer-orders database by email, order ID, or date range and returns matching orders (order ID, status, total, line items). Use when the user asks to find or look up an existing order. Do NOT use to create or modify orders, or to look up products — use product_search for that. Returns an empty array (not an error) when no orders match."`
- C) `"Searches records. Takes a query_string_v2 parameter (format the date as YYYYMMDD inside the name)."` — encode the format hint in the parameter name so Claude can't miss it.
- D) `"A powerful, enterprise-grade, AI-optimized record search tool."` — marketing-style adjectives signal capability to the model.

**Q8.** Your `cancel_subscription` tool is destructive and irreversible. A teammate proposes a boolean `dry_run` parameter: when `true` the tool only previews the cancellation; the model is instructed to "always call with `dry_run: true` first, show the user, then call again with `dry_run: false`." What's the architecturally sound pattern instead?
- A) The `dry_run` flag is the recommended pattern — a boolean preview switch is exactly how destructive ops should be gated.
- B) Preview-then-execute with a **one-time confirmation token bound to the previewed payload**: the preview call returns a token tied to the exact change, and execution requires that token (re-verifying authority server-side). A `dry_run` flag the model can simply skip is not a real safeguard.
- C) Mark the tool `destructiveHint: true` and let the host's UI handle confirmation; no token needed.
- D) Make the tool idempotent so repeated calls are harmless, removing the need for any confirmation step.

**Q9.** A platform exposes ~400 MCP tools across dozens of connected servers. Loading all 400 schemas into context every turn bloats the prompt and degrades tool selection. Which approach best fits the recommended pattern for large tool sets?
- A) Load all 400 tools every turn — context windows are large, so capacity makes selection a non-issue.
- B) Use **progressive availability**: a discovery/search tool returns a relevant shortlist for the task, then the matching tools are dynamically registered for use — rather than pre-loading everything.
- C) Manually delete tools from servers until fewer than 20 remain.
- D) Merge all 400 into one composite `do_anything(action, params)` god-tool so only one schema loads.

---

## Answer Key

**Q1 — B.** Resources are application-controlled passive context (schemas, docs, catalogs) read like context with no tool call needed; tools are model-controlled *actions*. A stable approved-hotel list and a policy doc are "what is true and stable," the canonical resource case. (A) is false — resources also use typed addressing; (C) prompts are user-invoked workflows; (D) `readOnlyHint` is an untrusted annotation and does not change a tool into a resource. _Sub-topic: MCP three primitives (tool-where-resource-fits) · Difficulty: med_

**Q2 — B.** MCP "focuses solely on the protocol for context exchange" — it standardizes discovery/invocation/transport, and explicitly does NOT auto-solve auth, rate-limiting, retries, caching, authorization, or performance; the builder owns those. (A)/(C)/(D) all wrongly attribute built-in reliability/security machinery to the protocol. _Sub-topic: MCP does-NOT-auto-solve auth/retries · Difficulty: easy_

**Q3 — B.** The four annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) are untrusted UI hints, not security boundaries — security belongs in code, with authority re-verified server-side on every call. (A)/(C)/(D) all treat a self-reported, untrusted hint as an enforcement mechanism; (D)'s "server-signed/tamper-proof" claim is fabricated. _Sub-topic: annotations are untrusted hints, not security · Difficulty: med_

**Q4 — C.** Uncertain write state is the textbook "report uncertainty, do NOT auto-retry" case — blind retry of a write whose outcome is unknown risks duplicates. Return a structured error (`category`, `retryable`, `message`) and escalate; recoverable-vs-escalate is an architecture decision encoded in the error surface. (A) causes duplicate transfers; (B) "fake success / nothing happened" is the graceful-degradation anti-pattern; (D) you don't throw exceptions for expected operational failures. _Sub-topic: error handling by category (uncertain write) · Difficulty: hard_

**Q5 — C.** Two error tiers: protocol errors are JSON-RPC and pre-execution (unknown tool, malformed JSON, missing param — the call never reaches a valid tool); tool execution errors mean the tool ran but failed (404/503/business-rule/permission/rate-limit), surfaced with `isError: true`. (A)/(B) collapse the tiers; (D) inverts them. _Sub-topic: two MCP error tiers (protocol vs execution) · Difficulty: med_

**Q6 — B.** When parameters carry interdependent constraints (one field's validity depends on another's value), that's the signal to split into separate tools, each with a clean parameter set — far more reliable than encoding a conditional matrix in prose or making everything required. (A) descriptions guide but don't enforce interdependent shape; (C) forcing all-required breaks the mutually-exclusive cases; (D) free-text strings sacrifice the schema guarantees tools exist to provide. _Sub-topic: split-tools-on-interdependent-params · Difficulty: med_

**Q7 — B.** A strong description states what the tool does, when to use it, when NOT to use it, its inputs/outputs/limits, and behavior on edge cases (here, empty-array ≠ error). (A) minimal descriptions ("Searches records.") are the named anti-pattern; (C) format hints belong in the parameter *description*, never the parameter *name*; (D) marketing adjectives convey no usage signal. _Sub-topic: tool description quality (+ empty-array≠error) · Difficulty: easy_

**Q8 — B.** Destructive ops should use preview-then-execute with a one-time confirmation token bound to the previewed payload, re-verifying authority server-side on each call — not a `dry_run` flag the model can silently skip. (A) is the exact anti-pattern; (C) annotations/UI alone aren't an enforcement boundary; (D) idempotency prevents duplicates but does not provide informed confirmation of an irreversible action. _Sub-topic: destructive ops preview-then-execute-with-bound-token · Difficulty: hard_

**Q9 — B.** Large tool sets call for progressive availability: a discovery tool returns a task-relevant shortlist, then those tools are dynamically registered — keeping context lean and selection accurate. (A) confuses capacity with attention/selection quality; (C) deleting capability is not a design strategy; (D) a composite god-tool is itself an anti-pattern that hides distinct operations behind one opaque schema. _Sub-topic: progressive availability for large tool sets · Difficulty: med_
