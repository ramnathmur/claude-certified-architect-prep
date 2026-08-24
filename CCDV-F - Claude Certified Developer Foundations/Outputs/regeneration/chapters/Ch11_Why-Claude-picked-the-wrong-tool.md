# Chapter 11 · Why Claude picked the wrong tool

## Two tools, one order number

A support-ticket agent has two tools registered. `lookup_order` is described as "Retrieves information about a customer order." `check_order_status` is described as "Retrieves the status of a customer order." Different engineers built them on different sprints, and each tool passed its own tests: given a clean, isolated prompt naming the right intent, the agent called the right tool every time.

In production, a customer writes "where's my order," and the agent calls `lookup_order`, the heavier tool, which returns the full order record: line items, billing address, shipping carrier, and, three fields down, the status. Another customer writes almost the same sentence, and the agent calls `check_order_status` instead. Nothing about the two requests explains the split. Both tools work. Both schemas validate. The bug report says "wrong tool." What's actually true is narrower: two tools describe the same thing to the one reader who has to choose between them.

## The label is the only thing Claude can read

Picture a hardware shop's shelf. Two bins sit side by side, and both are labelled "screws." A customer needs 3/4-inch wood screws for a stud wall, and hands the request to a clerk who has never opened either bin. All the clerk has is the two labels and the customer's sentence, and the choice between the bins has to come from matching one against the other.

A hardware shop that wanted a reliable clerk would not solve this by hiring someone smarter. It would rewrite the labels: "Wood screws, coarse thread, for framing and stud walls." "Machine screws, fine thread, for metal fittings; not for wood." The second label states what's inside, states what the bin is for, and closes with what it is not for, which is the clause that lets a customer asking about wood rule out the second bin without ever touching it.

Anthropic's API assembles every registered tool's `description` into a system prompt behind the scenes, so by the time Claude reads it, the description is ordinary instruction text, sitting in the same window as everything else and reasoned over the same way. At the moment Claude decides between `lookup_order` and `check_order_status`, neither tool has run yet, and what it has is the customer's sentence and two blocks of description text. Picking a tool is an act of the same kind as picking the next word: weighing the request against each candidate's words and generating whichever name comes out most likely. There is no separate index mapping "asking about order status" to a tool id. The name Claude emits is a prediction made from text, generated the same way every other token it produces is.

Anthropic's own guidance for writing tool definitions doesn't hedge: "Provide extremely detailed descriptions. This is by far the most important factor in tool performance." The same guidance names four things a complete description has to carry: what the tool does, when it should and shouldn't be used, what each parameter means, and what important limitations it carries, including what it does not return. Two tools whose descriptions both amount to "find information about the order" are the two bins both labelled "screws." Nothing about the schema, the parameter names, or the tool's own correctness changes that.

## Who actually walks to the shelf

A second question sits next to the label: once a tool is chosen, who fetches it.

In the shop, most items come from the shop's own back room. A staff member walks over, gets it, and hands it across the counter, whether they're following a procedure they wrote themselves or one printed by the manufacturer and taped to the shelf. A smaller set of items work differently: the shop calls a supplier, and the supplier's own warehouse pulls the item and ships it straight to the customer. The shop's own staff never touch it.

Claude's tools fall into three buckets along one axis: which infrastructure runs the call. In the first, you write the schema and your own application executes the code; this covers most tool-use traffic in practice. In the second, Anthropic publishes the schema, and your application still executes the code: memory, Bash, the text editor, computer use, and browser use all sit here. In the third, Anthropic runs the code on its own infrastructure and your application only reads the result: web search, web fetch, and code execution sit here, along with a few others.

Bash belongs to the second bucket, and it's worth sitting with why. Bash is an Anthropic-authored tool: Anthropic wrote its schema and documents it on its own site. When Claude calls it, your harness is still the process that opens a shell, runs the command, and sends the output back. Anthropic's own servers never touch that shell. Authorship of the schema and location of execution are two separate facts, and only the second one decides which bucket a tool sits in. That's why "client tool" and "server tool" are named for where execution happens: Bash counts as a client tool despite carrying Anthropic's name on the schema, for the same reason the shop's staff count as fetching an item in-house even when they're working from a checklist the manufacturer wrote.

The reason to prefer Bash's own schema over writing an equivalent custom tool is reliability. Claude has trained on a very large number of successful trajectories using that exact signature, so it calls the tool correctly more often, and recovers from a bad call more gracefully, than it does with a freshly written custom tool built to do the same job.

The billing difference tracks the same split. A client-side call, whichever bucket it's authored in, is priced the same as any other request. Server-side tools can carry their own charges on top: a web search costs per search, independent of the request that triggered it.

## Wiring the tool to something outside the shop

A custom client tool that does something real, rather than compute an answer from its own inputs, almost always ends in a call to an external system: an internal REST API or a third-party service. Registering the tool with Claude is the smaller half of the job. Wiring it to the system it actually touches is the larger half, and that needs the same four things any integration needs, whether or not an agent is involved.

An endpoint. The handler needs an address to call, and that address is not the same in every environment: a sandbox account and the production host are two different values for the same field, and the tool's own description never carries this information, because Claude has no use for it.

A way to authenticate. The call has to prove who it's acting as, with a credential that lives in your application and gets attached to the request at the moment the call actually goes out. Claude never sees it: not in the prompt, and not in the schema.

A timeout. External systems hang, and a call with no time limit leaves the whole turn blocked on a system that may never answer. The handler needs a bound on how long it will wait before it gives up and treats the call as failed.

An error surface. When the external system errors, times out, or returns something unexpected, the handler still has to return a `tool_result`, worded so Claude can act on it: which order failed, and why. A failed call is a normal outcome of talking to a system outside your control, and the tool's job is to hand that outcome back in a shape Claude can reason about and route around, rather than let an unhandled exception stop the loop.

The shelf doesn't decide any of this. It has to be built regardless of how good the label is.

## Writing a label that survives contact with a real question

The rule follows directly from the mechanism above: a description earns a reliable selection only when its words are the words that separate it from every other tool sitting in the same window. The test is whether someone outside the project could tell two tools apart on a first read.

Anthropic's engineering guidance frames it the same way: write the description you would give a new hire, someone who has never seen the codebase, joining the project this week. A new hire told "this retrieves information about the order" is left to guess the same thing Claude is: information from where, and how it differs from the other tool that also retrieves information about the order. A new hire told "retrieves the order's line items, billing address, and carrier from the orders database; does not return the current shipment status; use `check_order_status` for that" has nothing left to guess.

That last clause, the exclusion, is the one most descriptions skip, and it's the one that actually resolves an overlap. Fixing `lookup_order` alone is not enough, because `check_order_status`'s description still reads as "retrieves the status of a customer order," which is still true of `lookup_order` too. Both descriptions need the boundary. Fixing just one leaves the other's description exactly as ambiguous as it was. `check_order_status` gets its own added clause, naming exactly when to call it and, in the same sentence, when the request belongs to the other tool instead.

The fix is two added sentences, one per tool, each naming the case where its own tool should stay silent. Neither a longer schema nor a stricter conformance check touches this problem, because both operate after a tool has already been picked; they confirm that the input matches the declared shape, but they have no say in which tool gets picked in the first place. Parameter names carry the same weight at a smaller scale. A parameter called `id` forces Claude to infer, from context alone, whether it means an order id, a customer id, or a ticket id. A parameter called `order_id` removes the inference.

## Four hundred bins, and the instinct that makes it worse

The same shop that survives two mislabelled bins does not survive four hundred bins, no matter how carefully each one is worded on its own. Selection is a comparison across everything currently on the shelf, and a shelf with hundreds of entries gives Claude hundreds of candidates to weigh on every single call, regardless of how many are actually relevant.

The instinct, when a team wants Claude to reach a large system, is to register one tool per operation: one per REST endpoint, one per database table. Coverage looks complete, and every individual tool can be well described. Anthropic's own engineering guidance rejects this directly: "more tools don't always lead to better outcomes." Selection accuracy is reported to fall once a registered tool-set grows into the tens of entries, well before it reaches the hundreds a wrap-every-endpoint plan produces. A crowded shelf does more than slow the clerk down. It gives two or three tools, out of hundreds, enough surface similarity that the same overlap problem from the two-tool case reappears. No amount of rewriting one description at a time fixes an overlap at that scale.

The documented fix moves in the opposite direction from "add more tools." Consolidate related operations behind fewer tools that take a shared `action` parameter, so `create_pr`, `review_pr`, and `merge_pr` become one `pr_tool` with an `action` field instead of three separate entries competing for the same slice of the shelf. Namespace what's left, so a tool pulled from the GitHub integration reads `github_list_prs` instead of `list_prs`; a name collision with Slack's or Jira's own `list_` tool never gets the chance to happen. Both moves shrink the shelf. That's the opposite of what a "give Claude full coverage" brief usually produces.

Response design belongs to the same job: a tool that returns every field on an internal record, when a request only needs a handful, spends the same context budget a bad description would, for a different reason.

## A label doesn't decide who's allowed to act on it

Everything above governs which tool gets picked and how well. None of it governs a separate question: once a tool call has been picked, correctly, is it actually allowed to run.

That question is answered by a different mechanism, evaluated after selection and in a fixed order. Hooks are checked first, and a hook that denies a call blocks it outright, even in a mode that otherwise skips every other prompt. Deny rules are checked next, and a matching deny rule blocks the call regardless of anything that follows. Only after both of those come ask rules, the general permission mode, and allow rules, in that order: deny beats ask, and ask beats allow, every time.

The word "block" covers two different acts. Removing a tool from the request entirely means Claude never sees it and cannot attempt it, and it also means that tool's description stops occupying context. Denying a pattern within a tool that stays available is a narrower act. The tool is still visible and callable, but a specific shape of call inside it (`rm *`, say, inside a general-purpose shell tool) is refused every time it's tried. Scoping a tool out of the request and denying a pattern inside an available tool solve different problems, and only one of them also saves the context the tool's description would have spent.

Claude Managed Agents draws a related distinction: who owns the toolset. Its own pre-built agent toolset defaults to running without a confirmation step, and toolsets that come from a connected MCP server default to waiting for one. The reason given for the difference is direct: a third party controls what an MCP server's tools actually do, and that server's owner can change a tool's behaviour after your session already trusts it. The built-in toolset can't change out from under you the same way, because Anthropic ships and controls all of it. The default follows the same question the client-and-server split answered earlier in this chapter: who can change what actually happens when the call runs.

A denied call still returns a result. Claude typically tries a different approach or reports that it couldn't proceed, the same way it handles any other outcome it didn't expect.

None of this is enforced by wording. An instruction telling Claude never to touch a given path is a request sitting in the same window as everything else, read and weighed the same way a tool description is. Anthropic's own hook documentation names the distinction plainly: an instruction like this is "a request, not a guarantee." A rule that has to hold regardless of what gets requested belongs in a hook, which runs on every matching call independent of anything Claude decided.

## What the stem sounds like

Two tools with descriptions that both reduce to the same three or four words is the plainest version of this chapter's stem. So is a scenario that proposes a bigger model, a longer schema, or a stricter tool-choice setting as the fix for a wrong-tool pick; each of those is a real lever pointed at a different problem. A stem describing dozens of near-identical operations, or asking how to keep Claude choosing correctly as a toolset grows, is the same mechanism at a different scale. And a stem that needs a rule to hold "regardless of mode" or "even without a human present" is asking about the enforcement layer underneath selection: hooks, deny rules, and the evaluation order that runs before any description gets read.

---

## Self-test

**1.** An agent has two tools, `get_weather_forecast` and `get_current_conditions`. Claude sometimes calls the forecast tool when a user is asking about right-now weather. Both tool schemas validate correctly, and both pass their unit tests individually. Which change most directly fixes the mix-up, without changing what either tool does? *(Select one.)*

A) Require the request to go through a longer input schema with more required fields.
B) Add one sentence to each tool's description stating the case where that tool should not be called.
C) Rewrite both descriptions to be twice as long, adding more general detail about the weather domain.
D) Move the agent to a larger, more capable model.

**2.** A team enables Anthropic's built-in Bash tool so their code-review agent can run shell commands. Which two statements about this tool are correct? *(Select two.)*

A) Because Anthropic wrote the tool's schema, Anthropic's infrastructure executes every command.
B) The team's own application must still run each command and return the result; nothing executes on Anthropic's servers.
C) It is a client-side tool: the schema is Anthropic's, but execution is the calling application's responsibility.
D) Because Bash is a client tool, the team must still write and register their own schema for it before Claude can call it.

**3.** An internal platform team wants Claude to reach "every operation our internal API exposes" and proposes registering one tool per REST endpoint, about 140 tools total. A reviewer objects to the plan before it ships. Which option is the strongest documented reason the reviewer is right? *(Select one.)*

A) Selection accuracy falls once a tool-set grows into the tens of tools; consolidating related endpoints behind fewer tools that take a shared action parameter keeps the set navigable.
B) Add a code comment in each tool's handler function noting which endpoint takes priority when two could apply.
C) Add several worked examples of valid input directly into each tool's own description, so Claude can distinguish the tools by their sample inputs.
D) None of the descriptions need to change; moving to a larger model will resolve any ambiguity Claude runs into.

**4.** A CLAUDE.md instruction tells Claude "never modify files in /config." An engineer wants this to hold even when the agent is running in a mode that otherwise skips every other prompt. Which control actually guarantees it? *(Select one.)*

A) Strengthen the CLAUDE.md wording to "NEVER, under any circumstances, modify /config."
B) Configure a `PreToolUse` hook that denies any file-edit call targeting `/config`; hook denials run before every other permission check and hold even in a mode that otherwise skips every other prompt.
C) Set the tool-choice setting so Claude cannot call any tool for the rest of the session.
D) Switch the session to a larger, more capable model, on the reasoning that it is less likely to make the edit.

**5.** A developer builds a custom tool that calls a third-party invoicing API. In testing, the call occasionally hangs for over a minute before completing. Which addition most directly prevents this from stalling the whole agent loop? *(Select one.)*

A) A longer, more detailed tool description explaining what the invoicing API returns.
B) A stricter schema check that guarantees the input is always well-formed before the call is made.
C) A timeout on the outbound call, with a defined error result returned to Claude if it's exceeded.
D) A bigger, more capable model that is less likely to call the tool in a way that triggers the hang.

**Answers.**
1. B — negative scope in the description is the documented fix for two tools that resolve to the same intent; schema length, general elaboration, and model size don't touch selection.
2. B and C — Anthropic authoring the schema does not move execution onto Anthropic's servers, and the application does not need to write its own schema for a tool Anthropic already publishes.
3. A — this is the documented anti-pattern: full endpoint coverage grows the tool-set past the point where descriptions stay distinguishable; a code comment is never seen by Claude, examples address input shape rather than selection, and a bigger model doesn't change how many near-identical tools are on the shelf.
4. B — hooks are evaluated before every other permission check, including modes that skip prompting entirely; prompt wording alone doesn't enforce anything.
5. C — a timeout with a defined failure result is what stops a hanging external call from blocking the turn; the other three options address selection quality or input shape rather than latency.

---

## Volatile specifics (reference only)

The figures, field names, and mode names below sit behind the mechanisms taught above. The official guide is v1.0 and states it is subject to change without notice, so none of these anchors a self-test item; treat the list as a recognition aid rather than a study target.

- Anthropic's own length guidance for a tool description: at least 3–4 sentences, more for a complex tool.
- `input_examples` is a separate field for clarifying complex or format-sensitive input shapes; it is not supported on server tools or on the computer-use and browser-use client toolsets.
- `tool_choice` takes the values `auto` (the default when tools are provided), `any`, `tool`, and `none` (the default when no tools are provided); `strict: true` on a custom tool's schema guarantees the input matches the declared shape.
- Missing-parameter behaviour differs by model: larger models are more likely to ask for a missing value, smaller ones more likely to infer one.
- Dated `type` identifiers (for example `web_search_20260318`, `code_execution_20260521`, `memory_20250818`) version each tool's wire format; the bucket a tool belongs to (client or server) is stable even as these version strings change.
- Agent SDK permission modes, by name: `default`, `dontAsk`, `acceptEdits`, `bypassPermissions`, `plan`, `auto`.
- An MCP tool whose server sets the `_meta["anthropic/requiresUserInteraction"]` key always falls through to a confirmation callback, regardless of allow rules.
- Claude Managed Agents policy names: `always_allow` and `always_ask`.
- Selection accuracy is reported to degrade once a tool-set passes roughly 30–50 available tools; a typical multi-server setup can carry upward of 55,000 tokens of tool definitions before any work is done.
- Tool results are truncated to 25,000 tokens by default unless a tool's response is designed otherwise.
