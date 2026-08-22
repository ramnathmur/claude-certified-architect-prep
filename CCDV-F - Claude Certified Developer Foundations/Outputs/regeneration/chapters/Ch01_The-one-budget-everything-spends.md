# Chapter 1: The one budget everything spends

## Twenty-five thousand six hundred of forty thousand

Twenty-five thousand six hundred tokens is what eight turns of tool output cost one agent. The agent processed sales receipts and had been given a 40,000-token context budget, a cap the team set as a cost control rather than a limit the model imposed. In development it ran against twenty test receipts, each tool result around 800 tokens, and the full twenty-turn session stayed comfortably under the cap. In production the receipts arrived with supporting documentation, transaction records and correspondence attached. Average tool output grew to roughly 3,200 tokens per call. Eight turns of that is 25,600 tokens, and once the system prompt, the user messages and the assistant messages were added on top, the running total reached the cap at turn eight.

What the team saw was an agent choosing the wrong tools and returning incomplete analyses. A token usage audit found the cause two days after deployment.

## One container, and everything that rides in it

A shipping container has a fixed internal volume. You can pack it well or pack it badly, and the number of cubic metres does not move. Every carton you load takes volume from the same figure, and when the figure is spent the doors close on whatever is inside.

The context window is the total number of tokens the model can take in for a single request. It holds the system prompt, the full conversation so far, the tool definitions, every tool result, any documents you inject, and the model's own output. All of it at once, measured against one number.

That last item is the one that makes the container image worth keeping. The model's answer is built inside the same volume, while the doors are shut, out of whatever room the loading left.

### The unit on every line of the manifest

Claude reads tokens, not characters or words. The characters-per-token average depends on the tokenizer of the model at hand and differs between model generations, so any rule of thumb you carry from one model is model-dependent and worth confirming at build time.

Tokens are the unit of the input, the unit of the output, and the unit of price. Estimating what a feature costs and estimating whether an input fits are the same arithmetic on the same unit, which is why the habit worth building is to think in tokens rather than in pages or paragraphs.

The volumes themselves are set by the model. Current Claude API models carry at least a 200k-token context window, and the newest flagship models, Fable included, serve 1M tokens by default. The receipt agent's 40,000 was a figure its team chose. The model had far more room.

### Cargo that is already aboard before the first message

Tool definitions load with the container. An MCP server adds its tool definitions to the context window even when none of its tools are called in the current turn, so connecting several servers at once spends budget before the user's first message arrives. The system prompt behaves the same way: it is sent on every request, whether or not the current turn needs anything in it.

This is the part of the manifest that is easiest to forget, because nobody wrote it as part of the conversation. It arrives because the session was configured, and it arrives on every trip.

### The container is emptied and reloaded for every trip

Nothing is kept between requests. A conversation works because your application sends the whole message history again on every API call, so turn nineteen is one request carrying all nineteen turns.

Two consequences follow. The budget is refilled to full at the start of every request, so a session never accumulates a debt it cannot clear. And the budget is re-charged in full on every request, so the tokens you loaded on turn three are paid for again on turn four, and again on turn nineteen.

### The two ways a container fails to ship

These are different failures at different points in the request, and they leave you holding different things.

**The manifest exceeds the volume at the dock.** A request whose input is already larger than the context window is rejected with a validation error before generation begins. Nothing was generated, so there is no partial output to salvage and no stop reason to read.

**The doors close mid-load.** A request that fits on input can still reach the ceiling during generation. Current models stop and return the output generated so far with a `model_context_window_exceeded` stop reason rather than raising an error. What arrives is a successful response holding real, incomplete content.

Neither path silently drops your oldest content.

### Reading the loading plan

The receipt agent's ledger, laid out as a manifest, shows where a real request's budget actually goes.

In development: twenty tool results at roughly 800 tokens each, comfortably inside a 40,000-token cap across the full session. In production: tool results at roughly 3,200 tokens per call, so 25,600 tokens across eight turns, with the system prompt, the user messages and the assistant messages loaded on top of that to reach 40,000.

Read the second column as a proportion. Tool results were the largest line item on the manifest by a wide margin, and they were the only line item nobody had measured. The system prompt was written by hand and reviewed before it shipped. The user messages were short. The tool results were whatever a document happened to contain that day, and the assistant's own replies grew alongside them, because summarising a longer document takes more words than summarising a short one.

A published session trace shows the same shape turn by turn. Four consecutive calls to `fetch_policy_document` returned 2,400 tokens each, so by the end of turn four there were 9,600 tokens of tool results sitting in the window, occupying room that the instructions about which tool to call next were also occupying.

## The rule that falls out of a fixed volume

Three facts are on the table. The volume is fixed for a given model. Every component draws from that one volume. The whole manifest is loaded again on every request. Derive from them in order.

Because every component draws from one volume, the components compete with each other. Room spent on tool results is room the model's own answer cannot use. That is also why raising the cap on output length cannot create room: it raises a ceiling on one line item that is drawn from the same total.

Because the whole manifest is reloaded every request, what decides when the ceiling arrives is the spend per turn. Twenty turns at 800 tokens a tool result left dev comfortably under the cap. Eight turns at 3,200 tokens a tool result reached it in production, on the same agent, the same window and the same code. The tool-result line item changed size by four times; everything else in the request moved only in step with it.

Because the volume is fixed while the spend rate is not, a request that fitted yesterday can fail today with no change to your model, your prompt or your code. In development the window rarely fills, because test inputs are small and sessions are short. In production, tool outputs run longer, drawn from documents nobody sized in advance.

So the rule. Before an agent ships, measure the actual token cost of a tool result against the largest input you can find in your target data, then set that per-turn figure against the ceiling. A fixture set tells you the code works. It tells you nothing about the spend rate: fixtures are authored by whoever wrote them, while production traffic arrives from whatever a real document happens to contain.

## Two truncations that look identical on screen

An agent returns half a JSON object, stopped mid-structure. That single surface feature is produced by three different failures with three different fixes, and the surface feature does not separate them. Read the stop reason.

`stop_reason: max_tokens` means the response hit the output cap and stopped there. The window was never the constraint on that call. Raising `max_tokens` addresses the stated cause.

`stop_reason: model_context_window_exceeded` means the request fitted on input and generation walked into the ceiling. Raising `max_tokens` buys nothing here, because it sets how much Claude can write in a single response, not how much context it can read, and the writing is drawn from the same volume the reading already filled. That confusion is documented: a Module 2 checkpoint offers "increase `max_tokens` in the API call to give Claude more room to respond" as the answer to a session whose window was filling, and marks it wrong for exactly this reason.

A validation error before generation is the third case, and it is the easiest to separate once you look for it, because it carries no stop reason at all. There was no generation to stop.

The receipt agent shows the same disagreement one level up. Its visible symptom was wrong tool selection, which points at the tool schemas. The schemas had not changed. Accumulated tool results had crowded out the system prompt and the early instructions, and the agent was choosing tools from a window that no longer held the guidance it started with. The check follows directly: when tool selection degrades after a fixed number of turns, look at whether the window is filling before you start debugging the schema.

## Where the container stops being the right picture

Keeping a long session under the ceiling is a separate job with its own instruments. Pruning, compaction, clearing and subagent handoff each buy room, and each destroys a specific kind of continuity in exchange. Chapter 8 owns that choice. Paying less for the part of the manifest that never changes between requests is prompt caching, and measuring context pressure before a request goes out belongs beside it; both are chapter 9. Which model you run decides which volume you get, and that decision is chapter 3.

The image itself has a limit worth stating. Cartons in a container do not interact with each other. The contents of a context window do. The model reads everything in the window as one stream of tokens, with no structural marker separating your instructions from a document a tool fetched, so the contents affect how the model behaves as well as how full the window is. The receipt agent is the mild version of that, where crowded-out instructions degraded tool choice. Chapter 28 covers the sharp version, where fetched content carries instructions of its own.

## Phrases that put you in this chapter

A stem naming a turn number, a token figure set against a ceiling, or a session that ran fine in testing and fails in production is asking about this pot. So is any stem carrying "the response stops mid-structure", "rejected before generation", "fits on input", or "tool results accumulate". The give-away is a quantity measured against a limit rather than a quality being judged.

## Self-test

**1. Select TWO.** An agent registers six tools and calls one of them on a given turn. The team is auditing what that request spends against the context window. Which two of the following are counted against the window on that request?

A. The definitions of all six registered tools, including the five not called.
B. The model's own output for that request.
C. The wall-clock latency of the tool call.
D. The number of retries the SDK performed before the call succeeded.

**Answer: A and B.** The window holds the system prompt, the conversation history, the tool definitions, every tool result and the model's own output at once, and definitions occupy budget whether or not a tool is used in the turn. Latency and retry counts are not text in the request, so they cost nothing against the window.

---

**2. Select ONE.** A generation stops mid-structure. The response carries `stop_reason: max_tokens`, and a count of the input shows it used under a tenth of the model's window. The team wants the shortest change that addresses the stated cause.

A. Raise `max_tokens` on the call.
B. Summarise the conversation history before the next request.
C. Add a line to the system prompt instructing the model to always close its JSON.
D. Move the workload to a model with a 1M-token window.

**Answer: A.** The stop reason names the output cap, and the input measurement rules the window out. B and D relieve a ceiling the measurement shows was never approached, and C is an instruction the model can fail to follow, so it does not enforce the structure.

---

**3. Select ONE.** A request comes back as a validation error with no content. The on-call engineer needs to know whether any partial output exists to salvage before retrying.

A. No output exists; the input alone exceeded the window, so the request was rejected before generation began.
B. Partial output exists in the response body under a `model_context_window_exceeded` stop reason.
C. Partial output exists, but the oldest turns were dropped to make room, so early context is missing from it.
D. Output exists and was discarded by the SDK; re-reading the response object recovers it.

**Answer: A.** An oversized input is rejected before generation, so nothing was produced to salvage. B describes the other edge behaviour, which arrives as a successful response carrying truncated content, and C describes silent eviction of old turns, which does not happen.

---

**4. Select ONE.** A team connects four MCP servers to one session so the tools are available if they turn out to be needed. Before the user sends a first message, they want to know what has already been spent from the window.

A. Nothing; definitions cost budget only on the turn a tool is called.
B. The tool definitions of all four servers, plus the system prompt.
C. Only the definitions of the server whose tools the first message will use.
D. Nothing measurable; definitions are compiled server-side and are not part of the request.

**Answer: B.** MCP servers add their tool definitions to the context window whether or not the tools are used in the current turn, and the system prompt is sent on every request. Connecting servers speculatively spends budget before the conversation starts.

---

**5. Select ONE.** An agent's tool selections start going wrong at turn eight in production. It completed twenty-turn sessions cleanly against the test fixtures. The tool schemas, the model and the prompt are unchanged, and average tool output has gone from about 800 tokens per call to about 3,200. The team must name the mechanism before choosing a fix.

A. The tool descriptions became ambiguous as the conversation grew.
B. The per-turn spend rose while the ceiling stayed the same, so accumulated tool results crowded out the system prompt and the early instructions.
C. Sampling drifted over the longer session, so lowering the temperature will stabilise selection.
D. The window is too small for this workload, so the fix is a model with a larger window.

**Answer: B.** The window did not change; what changed is how much each turn spends against it, and instructions crowded out of the window are what degrade tool choice. A reads the symptom as a schema problem, C reaches for a lever the scenario gives no evidence for, and D buys a bigger container for a spend-rate the team has not yet measured.
