# -*- coding: utf-8 -*-
"""Exam 13 - blocks 1 and 2. Correct-answer letters follow the pre-planned sequence."""
S = "§"

BLOCK1 = dict(label="Customer Support Resolution Agent", narrative=(
 "You run a customer-support resolution agent built on the Agent SDK. It reaches the backend through MCP tools "
 "(<code>get_customer</code>, <code>lookup_order</code>, <code>process_refund</code>, <code>escalate_to_human</code>) and is measured on "
 "first-contact resolution against an 80% target. Across this block the situation moves from raw loop mechanics, "
 "through tool and policy design, to the judgement calls about when the agent should stop and hand over."))

BLOCK2 = dict(label="Multi-Agent Research System", narrative=(
 "A coordinator agent delegates to specialised subagents - one searches the web, one analyses documents, one "
 "synthesises findings, one drafts the report - producing cited research briefs. Across this block the system is "
 "already running and mostly working; what follows are the failures that only appear once several agents are "
 "operating together."))

Q = []
def q(g, block, label, domain, stem, options, correct, right, wrong):
    Q.append(dict(g=g, block=block, blockLabel=label, domain=domain, stem=stem, options=options,
                  correct=correct, whyRight=dict(text=right[0], cite=right[1]),
                  whyWrong=[dict(option=o, text=t, cite=c) for o, t, c in wrong]))

B, L = 0, BLOCK1["label"]

q(1, B, L, "D1",
 "Your harness treats a response as finished whenever `stop_reason` is absent from its checks: it inspects the response for a `tool_use` block, and if none is present it returns the text. A recent change added a tool that occasionally returns nothing useful, and the agent now sometimes replies with a partial sentence and stops. What should the harness key its loop control on?",
 ["Whether the last tool call returned a non-empty result, continuing the loop when the result is empty so the model can try another approach.",
  "Whether the response text ends in terminal punctuation, treating an incomplete sentence as a signal to continue the loop.",
  "The `stop_reason` field: continue the loop while it reads `tool_use`, and terminate only when it reads `end_turn`.",
  "A maximum-iteration counter, returning whatever text is present once the counter is reached."],
 2,
 ("`stop_reason` is the structured signal the loop is meant to run on. `\"tool_use\"` means execute the requested tools, append the results, and send again; `\"end_turn\"` means the model has finished. Inferring completion from the shape of the content is the anti-pattern this field exists to remove.", "D1 " + S + "1.1"),
 [(0, "Emptiness of a tool result says nothing about whether the model intends to act again. A valid empty result is a legitimate outcome, not a reason to keep looping.", "D1 " + S + "1.1; D2 " + S + "2.3"),
  (1, "This is parsing natural language to determine termination - the named anti-pattern. Punctuation is not a control signal.", "D1 " + S + "1.1"),
  (3, "An iteration cap is a safety backstop, never the primary stopping mechanism. Using it as the control condition truncates work that was still progressing.", "D1 " + S + "1.1")])

q(2, B, L, "D1",
 "Production logs show that in 9% of refund conversations the agent calls `process_refund` after identifying the customer only from a name and an order number the customer supplied, without `get_customer` returning a verified customer ID. Three refunds went to the wrong account last month. What change most effectively addresses this?",
 ["Add a programmatic prerequisite that blocks `process_refund` until `get_customer` has returned a verified customer ID for the session.",
  "Strengthen the system prompt to state that identity verification through `get_customer` is mandatory before any refund is issued.",
  "Add few-shot examples showing the agent calling `get_customer` first even when the customer volunteers an order number.",
  "Have the agent restate the customer's identity back to them for confirmation before calling `process_refund`."],
 0,
 ("Where a sequence is required for correctness and money is involved, enforcement must be deterministic. A programmatic prerequisite blocks the downstream call until the prerequisite has actually completed - code, not compliance.", "D1 " + S + "1.14"),
 [(1, "Prompt instructions carry a non-zero failure rate. The agent is already ignoring an instruction of this kind 9% of the time; restating it more firmly does not change the category of guarantee.", "D1 " + S + "1.14"),
  (2, "Few-shot examples raise the probability of compliance without making non-compliance impossible. That is insufficient when the failure has financial consequences.", "D1 " + S + "1.14"),
  (3, "Asking the customer to confirm their own identity verifies nothing - the caller is the party whose identity is in question. It also leaves the tool sequence unenforced.", "D1 " + S + "1.14")])

q(3, B, L, "D2",
 "Telemetry shows `get_customer` and `lookup_order` are called back-to-back in 94% of turns that touch an order, always in that order, and never usefully apart. An engineer proposes replacing them with a single `get_customer_with_orders` tool that performs both lookups internally and returns a merged payload. What should you recommend?",
 ["Adopt the composite tool, since collapsing a habitually-paired sequence into one call removes a round-trip and eliminates the ordering risk entirely.",
  "Adopt the composite tool but keep the originals registered as well, so the agent can choose the granular path when it needs only one of the two.",
  "Reject the proposal and instead add a routing layer that detects order-related requests and issues both calls automatically before the model runs.",
  "Keep the two tools and add a prompt instruction to request them together in a single turn when a request touches an order."],
 3,
 ("The corpus favours instructing the model to bundle the two calls into one turn over hiding them inside a composite tool. Prompt-level bundling keeps each tool's purpose, inputs and failure modes visible to the model; a composite tool conceals two distinct operations behind one description and one error surface.", "D2 " + S + "2.8"),
 [(0, "A composite tool hides two operations behind a single description and a single error path - when the order lookup fails, the model can no longer tell which half failed or recover selectively.", "D2 " + S + "2.8"),
  (1, "Registering both the composite and its two components adds overlapping tools with near-identical purposes, which is precisely the condition that degrades selection reliability.", "D2 " + S + "2.8; D2 " + S + "2.5"),
  (2, "A pre-model routing layer bypasses the model's own tool selection and adds infrastructure to solve an ordering habit that a prompt instruction already covers.", "D2 " + S + "2.8; D2 " + S + "2.2")])

q(4, B, L, "D1",
 "When the agent escalates, the receiving human agent opens a ticket containing the customer's last message and a one-line reason ('customer dissatisfied with resolution'). Human agents report spending the first several minutes of every escalated call re-establishing facts the agent already had. What should the escalation payload carry?",
 ["The full conversation transcript, so the human can read exactly what was said in the order it was said.",
  "A structured summary: the verified customer ID, the root cause as diagnosed, the amounts and order references involved, and a recommended action.",
  "The customer's sentiment trajectory across the conversation, so the human knows what tone to open with.",
  "A confidence score from the agent indicating how certain it was that escalation was warranted."],
 1,
 ("A structured handoff carries the facts the human needs to act: customer ID, root cause, the figures involved, and a recommended action. The human has no access to the conversation, so the payload must stand alone.", "D1 " + S + "1.13"),
 [(0, "A raw transcript re-creates the reading work rather than removing it, and buries the transactional facts the human actually needs inside conversational text.", "D1 " + S + "1.13"),
  (2, "Sentiment is not an actionable fact about the case. It does not tell the human what happened, what was verified, or what to do.", "D1 " + S + "1.13; D5 " + S + "5.8"),
  (3, "A self-reported confidence score is a poorly calibrated signal and, in any event, describes the agent's state rather than the customer's case.", "D5 " + S + "5.8")])

q(5, B, L, "D5",
 "A customer gives a phone number to identify themselves. `get_customer` returns two active accounts sharing that number - a personal account and a small-business account, each with recent orders. The agent immediately escalates to a human, citing ambiguous identity. Reviewers flag this as a wasted escalation. What should the agent do instead?",
 ["Ask the customer for one additional identifier - an order number, an email, or the billing postcode - and proceed once a single account is identified.",
  "Select the account with the most recent order activity, since that is the one the customer is most likely calling about.",
  "Proceed with the personal account by default and switch if the customer's details do not match what it reads back.",
  "Escalate, but attach both account records so the human can disambiguate without re-asking."],
 0,
 ("Multiple matches call for a clarifying question, not a heuristic and not a handover. Asking for one more identifier resolves the ambiguity inside the conversation; this is a resolvable ambiguity, not a policy gap or a customer request for a human.", "D5 " + S + "5.8"),
 [(1, "Selecting on recency is exactly the heuristic the corpus warns against - it silently guesses at identity in a workflow where misidentification has already caused wrong-account actions.", "D5 " + S + "5.8"),
  (2, "Defaulting to one account and correcting later is the same guess with a slower failure mode, and it exposes one customer's details to another.", "D5 " + S + "5.8"),
  (3, "Escalating a question the agent could have asked itself burns a human interaction on a resolvable ambiguity. Escalation triggers are an explicit request, a policy gap, or an inability to progress - none apply here.", "D5 " + S + "5.8; D1 " + S + "1.12")])

q(6, B, L, "D2",
 "`process_refund` is irreversible once it runs. It currently accepts a `preview: boolean` parameter so the agent can inspect the calculated amount, restocking fee and account impact before committing. Audit logs show the agent has called it with `preview: false` as its first and only call on 40 occasions. Which redesign makes skipping the preview architecturally impossible?",
 ["Change `preview` to default to `true` so an explicit override is required to commit.",
  "Add a system-prompt rule that a preview call must always precede a commit call, with few-shot examples of the pattern.",
  "Split it into `preview_refund`, which returns the impact plus a single-use token, and `execute_refund`, which will not run without that token.",
  "Add a `confirmation_phrase` parameter that the agent must populate with the exact refund amount before the call executes."],
 2,
 ("Two-tool token binding makes the bypass structurally impossible: the token `execute_refund` requires does not exist until `preview_refund` has run. Nothing is left to the model's discretion.", "D2 " + S + "2.4; Key Distinctions #12"),
 [(0, "A default is still a parameter the model can set. `preview: false` on the first call remains reachable, which is the behaviour already observed.", "D2 " + S + "2.4"),
  (1, "This is prompt-level enforcement of a rule that must hold every time. It raises compliance without guaranteeing it.", "D2 " + S + "2.4; D1 " + S + "1.14"),
  (3, "A confirmation string is a value the model can synthesise from the request without ever having run a preview. It looks like a gate and is not one.", "D2 " + S + "2.4; Key Distinctions #12")])

q(7, B, L, "D1",
 "A customer asks the agent to match a competitor's lower price on an item they have already received. The published policy covers price adjustments for the retailer's own listed price within 14 days and is silent on competitor matching. The agent declines the request, citing policy. What should it have done?",
 ["Decline as it did - the policy does not authorise the adjustment, so refusing is the correct application of the written rule.",
  "Escalate to a human, because the policy is silent on this specific request rather than prohibiting it.",
  "Apply the own-price adjustment rule by analogy, since a competitor's price serves the same purpose as a listed price.",
  "Ask the customer to submit the request in writing so it can be reviewed after the 14-day window closes."],
 1,
 ("A policy that is silent on the customer's specific request is a policy gap, and policy gaps are an escalation trigger. Silence is not prohibition, and the agent has no authority to decide the case either way.", "D1 " + S + "1.12; D5 " + S + "5.8"),
 [(0, "Treating silence as refusal has the agent making a policy decision it was never delegated. The written rule addresses a different situation entirely.", "D1 " + S + "1.12"),
  (2, "Reasoning by analogy into an unwritten entitlement is the same error in the opposite direction - the agent is still inventing policy.", "D1 " + S + "1.12"),
  (3, "This defers the request without resolving it and attaches an irrelevant deadline. The gap remains unaddressed and the customer is left waiting.", "D1 " + S + "1.12")])

q(8, B, L, "D2",
 "`process_refund` rejects requests above the agent's authorised limit. It currently returns `isError: true` with the message 'Operation failed'. Production shows the agent retrying these calls two or three times before giving up and telling the customer that the system is unavailable. How should the tool represent this outcome?",
 ["Return a success response with a zero-value refund, so the agent treats the limit as a business outcome rather than a failure.",
  "Return `isError: true` with the same message but add an internal retry-suppression window so repeated calls are rejected quickly.",
  "Return `isError: true` with the message 'Refund exceeds authorised limit' and leave retry behaviour to the agent's judgement.",
  "Return `isError: true` with `errorCategory: \"business\"`, `retriable: false`, and a customer-friendly explanation of the limit."],
 3,
 ("A business-rule violation is a distinct error category. Structured metadata - the category, an explicit non-retryable flag, and language the agent can relay to the customer - lets the agent stop retrying and explain the outcome accurately.", "D2 " + S + "2.3"),
 [(0, "Reporting a policy rejection as a success suppresses the error. The agent loses the ability to explain what happened, and the refusal becomes invisible downstream.", "D2 " + S + "2.3; D1 " + S + "1.9"),
  (1, "Suppressing retries at the transport layer treats the symptom. The agent still does not know why the call failed or what to tell the customer.", "D2 " + S + "2.3"),
  (2, "A clearer sentence helps a human reader but leaves the agent guessing whether this is transient. Without a structured non-retryable flag, the retry loop is still a reasonable inference.", "D2 " + S + "2.3")])

q(9, B, L, "D1",
 "A single message reads: the delivered item is damaged, a duplicate charge appeared on the card, and the customer wants a future order redirected to a new address. The agent resolves the damaged item, replies, and waits. Two of the three matters go unaddressed until the customer writes again. How should the agent handle a message like this?",
 ["Decompose the message into three distinct items, investigate them in parallel against the shared customer context, then synthesise one unified resolution.",
  "Handle the highest-value matter first and tell the customer the remaining items will be addressed in a follow-up.",
  "Ask the customer which of the three they would like resolved first, to avoid making an assumption about priority.",
  "Escalate the message to a human, since a request touching three separate systems exceeds the agent's single-turn scope."],
 0,
 ("Multi-concern requests are decomposed into distinct items, investigated in parallel over shared context, and answered once. Serialising them turns one contact into three and defeats the first-contact resolution target.", "D1 " + S + "1.15"),
 [(1, "Ranking by value still leaves the customer to chase the remainder. The concerns are independent and can be investigated at the same time.", "D1 " + S + "1.15"),
  (2, "Asking the customer to sequence work the agent could simply do in parallel adds a turn and produces no information the agent needs.", "D1 " + S + "1.15; D4 " + S + "4.19"),
  (3, "Multiple concerns are not by themselves an escalation trigger. Nothing here is ambiguous, policy-silent, or beyond the agent's tools.", "D1 " + S + "1.12")])

q(10, B, L, "D2",
 "`lookup_order` returns a normal payload with an empty `orders` array when a verified customer genuinely has no orders in the queried window, and it returns the same empty payload when the order service times out. The agent tells customers 'I could not find any orders' in both cases. What is the most important correction?",
 ["Have the tool retry internally on timeout so the empty payload always means a genuine absence of orders.",
  "Distinguish the two outcomes in the response: a successful query with zero matches, versus an access failure carrying a retryable transient error.",
  "Have the agent always follow an empty result with a second `lookup_order` call to confirm the absence before telling the customer.",
  "Extend the queried window automatically when the result is empty, so genuine absences are rarer and the ambiguity matters less."],
 1,
 ("An access failure and a valid empty result demand opposite responses, so they must be distinguishable in the response itself. Zero matches is a successful query; a timeout is a failure needing a retry decision.", "D2 " + S + "2.3; Key Distinctions #9"),
 [(0, "Internal retries help with transience but do not remove the case where retries are exhausted - at which point the tool still reports an indistinguishable empty payload.", "D2 " + S + "2.3"),
  (2, "A blind second call doubles the cost of every genuine zero-result query and still cannot tell the two outcomes apart.", "D2 " + S + "2.3"),
  (3, "Widening the window changes what is queried, not whether the agent can tell success from failure. The ambiguity is unchanged.", "D2 " + S + "2.3")])

q(11, B, L, "D1",
 "The support agent delegates complex billing reconstructions to a specialist subagent. The subagent's `AgentDefinition` grants it the full tool set, and its system prompt says it should confine itself to read-only analysis. Logs show it has called `process_refund` twice during analysis runs. What is the correct fix?",
 ["Add a stronger prohibition to the subagent's system prompt, naming `process_refund` explicitly as out of bounds.",
  "Add a PostToolUse hook that reverses any refund the subagent issues during an analysis run.",
  "Restrict the subagent's `allowed_tools` in its `AgentDefinition` to the read-only tools its role requires.",
  "Have the coordinator review the subagent's planned tool calls and approve them before execution."],
 2,
 ("Tool restriction in the `AgentDefinition` is the structural enforcement of least privilege. If a tool is not in `allowed_tools`, the subagent cannot call it - no prompt compliance is involved.", "D1 " + S + "1.3; D1 " + S + "1.11"),
 [(0, "The prohibition already exists in the prompt and is already being violated. Restating it does not change the guarantee it offers.", "D1 " + S + "1.3"),
  (1, "PostToolUse runs after the tool has executed. A reversal is a compensating transaction for an action that should never have been possible.", "D2 " + S + "2.7"),
  (3, "Coordinator approval inserts a manual gate where a configuration field already provides an absolute one, and it does not scale across delegations.", "D1 " + S + "1.3")])

q(12, B, L, "D1",
 "A specialist subagent handles disputed charges. It currently receives the prompt 'resolve this dispute' and the customer's original message. Its outputs vary widely in quality and it frequently asks the coordinator for facts the coordinator already holds. What is the most effective change to the delegation?",
 ["Include the findings the coordinator already has - the verified customer record, the order details, and the transaction history - directly in the subagent's prompt.",
  "Give the subagent its own `get_customer` and `lookup_order` tools so it can fetch whatever it needs without asking.",
  "Have the coordinator and the subagent share a session so the subagent inherits the conversation automatically.",
  "Increase the subagent's iteration limit so it has room to gather the facts it needs before answering."],
 0,
 ("Subagents do not inherit the coordinator's conversation history and share no memory between invocations. Context must be passed explicitly in the prompt, which is also why the subagent keeps asking for facts that already exist upstream.", "D1 " + S + "1.5; D1 " + S + "1.2"),
 [(1, "Re-fetching data the coordinator already holds duplicates work and widens the subagent's tool surface against least privilege.", "D1 " + S + "1.11"),
  (2, "There is no automatic context inheritance between a coordinator and its subagents; a shared session is not the mechanism on offer here.", "D1 " + S + "1.2"),
  (3, "More iterations lets it spend longer rediscovering known facts. The missing input is context, not time.", "D1 " + S + "1.5")])

q(13, B, L, "D2",
 "The agent has grown from five tools to nineteen as new backend integrations were added. Selection accuracy has fallen: it now routinely calls a shipment-tracking tool for billing questions. An engineer proposes writing longer descriptions for all nineteen. What is the more effective response?",
 ["Rewrite all nineteen descriptions with explicit boundary statements, since description quality is the primary driver of selection.",
  "Scope the tool set by role, giving the agent only the tools its workflow needs and routing the rest through specialised subagents.",
  "Add a `tool_choice` forced selection for billing requests so the correct tool is guaranteed on that path.",
  "Order the tool list so the most frequently used tools appear first and are considered before the others."],
 1,
 ("Selection reliability degrades as the decision space grows - the corpus contrasts an agent holding 18 tools with one holding four or five. Descriptions matter, but at nineteen tools the volume itself is the problem, and scoping by role is the fix.", "D2 " + S + "2.5; D1 " + S + "1.11"),
 [(0, "Better descriptions help within a sensible tool count. They do not undo the decision complexity of nineteen candidates, and the failure here is volume rather than ambiguity between two similar tools.", "D2 " + S + "2.5"),
  (2, "Forcing a specific tool presupposes the request has already been correctly classified, which is the very step that is failing.", "D2 " + S + "2.1"),
  (3, "Tool ordering is not a documented selection mechanism. Selection runs on descriptions and the model's reasoning, not list position.", "D2 " + S + "2.5")])

q(14, B, L, "D5",
 "In a long billing conversation the customer states at turn 3 that they were promised a 15% loyalty adjustment on a $412.60 order. At turn 26, after two rounds of summarisation, the agent quotes a $41.26 adjustment and the customer disputes it. What is the most effective fix?",
 ["Raise the summarisation threshold so compression happens later in the conversation.",
  "Revise the summarisation prompt to instruct the model to preserve all numeric values verbatim.",
  "Extract transactional facts - amounts, percentages, order references, stated commitments - into a persistent case-facts block included in every prompt, outside the summarised history.",
  "Re-fetch the order record before every response so the authoritative figures are always present."],
 2,
 ("Precise values survive by being kept outside the stream that gets compressed. A case-facts block is included in every prompt and is never summarised, so the figure at turn 3 is as exact at turn 26 as it was when stated.", "D5 " + S + "5.4; D5 " + S + "5.3"),
 [(0, "A later threshold delays the loss without preventing it. The conversation continues and the same compression eventually runs.", "D5 " + S + "5.4"),
  (1, "This still depends on flawless execution of a summarisation instruction on every pass. The corpus rejects it for exactly that reason.", "D5 " + S + "5.4"),
  (3, "The order record does not contain what the customer was promised in conversation. Re-fetching restores the order total and loses the commitment.", "D5 " + S + "5.4")])

q(15, B, L, "D1",
 "An account-takeover report needs investigating: the steps required depend entirely on what each check reveals - whether the email was changed, whether shipping addresses were altered, whether new payment methods were added, whether recent orders were placed. Engineers propose a fixed five-step pipeline run identically on every report. Which decomposition suits this work, and why?",
 ["A fixed pipeline, because a security-sensitive workflow benefits most from a repeatable, auditable sequence of identical steps.",
  "A fixed pipeline with conditional skipping, because the five steps cover the space and skipping the irrelevant ones keeps it adaptive enough.",
  "Parallel execution of all five steps at once, because they are independent and running them together minimises investigation latency.",
  "Dynamic adaptive decomposition, because each finding determines which checks are worth running next and what new checks the evidence calls for."],
 3,
 ("Open-ended investigation, where each step's findings determine the next subtasks, is the case for dynamic adaptive decomposition. A fixed chain suits predictable multi-aspect work; this is not that.", "D1 " + S + "1.7"),
 [(0, "Auditability is satisfied by logging what was done, not by doing the same five things regardless of evidence. A fixed sequence cannot pursue a lead it was not written to anticipate.", "D1 " + S + "1.7"),
  (1, "Skipping steps prunes a fixed list; it cannot add the check that the evidence actually calls for. The set of possible steps stays frozen at design time.", "D1 " + S + "1.7"),
  (2, "The steps are not independent - what the email-change check finds determines whether the payment-method check matters and how it should be scoped.", "D1 " + S + "1.7; D1 " + S + "1.15")])

# ---------------------------------------------------------------- BLOCK 2
B, L = 1, BLOCK2["label"]

q(16, B, L, "D1",
 "A brief on 'the effect of automation on regional employment' returns a report covering only manufacturing. The web-search subagent returned relevant sources, the analysis subagent summarised them correctly, and synthesis produced coherent prose. The coordinator's log shows it created three subtasks: 'automation in factory assembly', 'robotics in warehousing', and 'automated quality inspection'. What is the most likely root cause?",
 ["The web-search subagent's queries were too narrow and returned only manufacturing sources.",
  "The coordinator's task decomposition was too narrow, so entire sectors were never assigned to any subagent.",
  "The synthesis subagent lacked instructions to detect and report coverage gaps in what it received.",
  "The analysis subagent's relevance criteria filtered out sources from non-manufacturing sectors."],
 1,
 ("The log states the fault outright: all three subtasks sit inside manufacturing, so services, agriculture, logistics and public sector were never assigned to anyone. Each subagent executed its assignment correctly - the assignment was the defect.", "D1 " + S + "1.6; Key Distinctions #7"),
 [(0, "The search subagent returned relevant results for the subtasks it was given. It cannot search for a sector nobody asked it about.", "D1 " + S + "1.6"),
  (2, "Gap detection in synthesis would surface the problem later; it would not cause it. The sectors are absent because they were never researched.", "D1 " + S + "1.10"),
  (3, "The stem states the analysis subagent summarised its sources correctly. No non-manufacturing sources reached it to be filtered.", "D1 " + S + "1.6")])

q(17, B, L, "D2",
 "The coordinator receives a response with `stop_reason: \"tool_use\"` containing a `tool_use` block for `search_web`. The harness reads the query, runs the search, and appends a new user message containing the results as plain text before calling the model again. The model frequently re-requests the same search. What is the harness doing wrong?",
 ["It should append the results as an assistant message rather than a user message so the model attributes them to itself.",
  "It should set `tool_choice` to `\"any\"` on the follow-up call so the model is forced to move on to the next tool.",
  "It should summarise the results before appending them, since raw search output is too verbose for the model to use.",
  "It should return a `tool_result` block referencing the originating `tool_use` block's `id`, rather than free text."],
 3,
 ("A tool result must be returned as a `tool_result` block carrying the `id` of the `tool_use` block it answers. Without that correlation the model has no record that its requested call was satisfied, so it asks again.", "D2 " + S + "2.1"),
 [(0, "Attribution to assistant or user is not the mechanism. The missing element is the structured correlation between request and result.", "D2 " + S + "2.1"),
  (1, "Forcing a tool call papers over the repetition by compelling a different action; the original result is still unlinked and effectively invisible.", "D2 " + S + "2.1"),
  (2, "Verbosity is a context-budget concern, not the reason a satisfied call is re-requested.", "D5 " + S + "5.5")])

q(18, B, L, "D1",
 "The coordinator evaluates each synthesis draft for gaps and re-delegates to the search and analysis subagents when it finds any. On broad topics it has run eleven refinement cycles on a single brief, each adding progressively less. An engineer proposes capping the loop at three cycles. What is the better design?",
 ["Define an explicit sufficiency criterion - the coverage conditions a draft must satisfy - and stop when the criterion is met.",
  "Cap the loop at three cycles, since diminishing returns after the third are consistent across observed runs.",
  "Have the synthesis subagent decide when its own draft is complete, since it has the fullest view of the findings.",
  "Run a fixed two cycles on every brief so that behaviour is predictable and latency is bounded."],
 0,
 ("A refinement loop needs a defined sufficiency criterion - the conditions under which coverage counts as adequate. An arbitrary cap stops on a count rather than on the state of the work.", "D1 " + S + "1.8"),
 [(1, "A cap is a backstop, not a stopping criterion. It halts a brief that still has real gaps and keeps running one that was already complete.", "D1 " + S + "1.8"),
  (2, "Self-assessment by the agent that produced the draft carries the same blind spot as self-review generally; the coordinator holds the evaluation role.", "D1 " + S + "1.17"),
  (3, "A fixed count is the arbitrary cap with the added flaw of being insensitive to topic breadth in both directions.", "D1 " + S + "1.8")])

q(19, B, L, "D2",
 "The document-analysis subagent has a `fetch_source` tool described as 'Retrieves a source document.' It handles PDFs and HTML pages by URL, silently returns the first 40 pages of longer PDFs, and cannot read anything behind authentication. Analysts have begun citing truncated documents as complete. What is the most effective fix?",
 ["Split it into `fetch_pdf` and `fetch_html` so each tool handles one format with its own description.",
  "Add a post-processing check that flags any returned document whose page count equals the truncation limit.",
  "Expand the description to state the accepted input formats, the 40-page truncation behaviour, and that authenticated sources are out of scope.",
  "Return an error instead of a partial document whenever the source exceeds the page limit."],
 2,
 ("The description is the model's only view of a tool's scope and boundaries. Stating the accepted formats, the truncation behaviour and what the tool cannot reach is what allows the agent to interpret the output correctly and choose a different route when needed.", "D2 " + S + "2.2"),
 [(0, "Splitting by format addresses a distinction that was not causing trouble. Truncation and authentication limits would go undocumented in both new tools.", "D2 " + S + "2.2"),
  (1, "A downstream flag catches one of the three undocumented behaviours, after the fact, and leaves the agent as uninformed as before at selection time.", "D2 " + S + "2.2"),
  (3, "Erroring on long documents discards a partial result that is often useful, and still tells the agent nothing about the limit in advance.", "D2 " + S + "2.2; D2 " + S + "2.3")])

q(20, B, L, "D1",
 "You want to reduce factual errors in the final brief. The proposal is to add a second agent that receives the completed draft with no access to the drafting agent's reasoning, checks each claim against the cited sources, and returns a list of corrections that the drafting agent then applies. Which named pattern is this?",
 ["Context isolation, since the second agent is deliberately scoped to a limited input.",
  "Prompt chaining, since the draft passes through a fixed sequence of processing steps.",
  "Orchestrator-worker, since one agent assigns work that another performs and returns.",
  "Evaluator-optimizer, since one agent produces work and an independent agent critiques it for revision."],
 3,
 ("Evaluator-optimizer names a generate-then-critique loop where an independent evaluator returns corrections that the producer applies. The independence is what makes the critique useful.", "D1 " + S + "1.18; D1 " + S + "1.17"),
 [(0, "Context isolation describes scoping a subagent's input to keep verbose or irrelevant material out of a context window. Both patterns involve limited context; only this one is about critique.", "D1 " + S + "1.18; D5 " + S + "5.6"),
  (1, "Prompt chaining is a decomposition of one task into sequential focused steps. It does not describe a critic returning corrections to a producer.", "D4 " + S + "4.14"),
  (2, "Orchestrator-worker describes delegation and aggregation by a coordinator. Here the second agent evaluates finished work rather than performing assigned work.", "D1 " + S + "1.18")])

q(21, B, L, "D1",
 "A newly deployed coordinator returns a plan describing which subagents it intends to invoke, then answers the research question itself from its own knowledge. It never delegates. Its `AgentDefinition` lists `allowedTools: [\"WebSearch\", \"Read\", \"Write\"]`. What is preventing delegation?",
 ["`\"Task\"` is absent from `allowedTools`, so the coordinator has no mechanism to spawn subagents.",
  "The coordinator's system prompt describes delegation as optional rather than mandatory.",
  "The subagents' own definitions must list the coordinator as a permitted caller before they can be invoked.",
  "`WebSearch` in the coordinator's own tool list makes answering directly the lower-cost path."],
 0,
 ("Subagents are spawned through the Task tool. A coordinator whose `allowedTools` omits `\"Task\"` cannot delegate at all, whatever its prompt says - so it does the next best thing and answers itself.", "D1 " + S + "1.3"),
 [(1, "Prompt wording cannot explain a capability that is absent. Even a mandatory instruction cannot invoke a tool the definition does not grant.", "D1 " + S + "1.3"),
  (2, "There is no reverse permission list on subagent definitions. Delegation is gated by the caller's tool access.", "D1 " + S + "1.3"),
  (3, "Holding `WebSearch` may make self-answering attractive, but the coordinator is not choosing between paths - one of them does not exist.", "D1 " + S + "1.3")])

q(22, B, L, "D2",
 "While combining findings, the synthesis subagent needs to confirm individual facts - a date, a figure, an author's affiliation. It currently returns control to the coordinator, which invokes the web-search subagent and re-invokes synthesis, adding two to three round-trips per brief. Review shows 85% of these checks are single-fact confirmations; the remainder need real investigation. What is the most effective change?",
 ["Have the search subagent pre-fetch additional context around every source so synthesis rarely needs to verify anything.",
  "Give the synthesis subagent a scoped `verify_fact` tool for single-fact confirmations, leaving deeper investigation to route through the coordinator.",
  "Give the synthesis subagent the full web-search tool set so it can resolve any verification need without a round-trip.",
  "Have the synthesis subagent batch all its verification needs and send them to the coordinator once at the end of its pass."],
 1,
 ("A narrowly scoped cross-role tool covers the high-frequency simple case while the coordinator keeps control of anything complex. Least privilege is preserved because the tool does one small thing.", "D2 " + S + "2.5; D1 " + S + "1.11"),
 [(0, "Speculative pre-fetching cannot predict which facts synthesis will question, and it inflates every source payload to serve a minority of cases.", "D2 " + S + "2.5"),
  (2, "Handing synthesis the full search toolkit over-provisions an agent outside its specialisation - the documented condition under which agents misuse tools.", "D2 " + S + "2.5; D1 " + S + "1.11"),
  (3, "Batching to the end creates a blocking dependency: later synthesis steps often rest on facts that needed confirming earlier.", "D2 " + S + "2.5")])

q(23, B, L, "D1",
 "Two of five source repositories were unreachable throughout a research run. The coordinator proceeded with the three that responded, and the delivered brief reads as a complete survey with no indication that anything was missing. A reviewer only discovered the gap by checking the logs. What should the synthesis output have done?",
 ["Withheld the brief until all five repositories were reachable, since a partial survey misrepresents the evidence base.",
  "Reported an error to the requester and returned no brief, since two of five sources is a material shortfall.",
  "Annotated coverage explicitly: which findings are well supported, and which topic areas are thin because sources were unavailable.",
  "Weighted the findings from the three reachable repositories upward to compensate for the missing coverage."],
 2,
 ("Graceful degradation means shipping what was found and stating what was not. Coverage annotations distinguish well-supported findings from areas left thin by unavailable sources, so the reader can judge the evidence.", "D1 " + S + "1.10"),
 [(0, "Blocking on full availability converts a recoverable partial result into no result, which the corpus treats as an over-correction.", "D1 " + S + "1.10"),
  (1, "Erroring out discards three repositories of genuine findings. Partial results with honest annotation are more useful than nothing.", "D1 " + S + "1.10; D1 " + S + "1.9"),
  (3, "Re-weighting fabricates confidence. It makes a thin evidence base look robust, which is the opposite of what the reader needs.", "D5 " + S + "5.11")])

q(24, B, L, "D1",
 "A brief requires three independent lines of enquiry - published literature, regulatory filings, and news coverage - with no dependency between them. The coordinator currently issues one Task call, waits for the result, issues the next, and so on. Total wall-clock time is roughly the sum of the three. How should the coordinator invoke them?",
 ["Emit all three Task calls within a single coordinator response so the subagents run concurrently.",
  "Issue the three Task calls across three consecutive turns without waiting for each result before issuing the next.",
  "Combine the three enquiries into one subagent prompt so a single agent covers all three source types in one pass.",
  "Raise the coordinator's concurrency setting so that sequentially issued Task calls overlap automatically."],
 0,
 ("Parallel execution means emitting multiple Task tool calls in a single response. Issuing them one per turn is sequential by construction, whatever the intent.", "D1 " + S + "1.15"),
 [(1, "Separate turns are still separate round-trips through the model. The calls do not overlap merely because the coordinator does not pause to read each result.", "D1 " + S + "1.15"),
  (2, "Collapsing three distinct source types into one agent removes the specialisation and reintroduces the attention-dilution problem partitioning was meant to avoid.", "D1 " + S + "1.6"),
  (3, "No such setting turns sequential calls into concurrent ones. Concurrency comes from how the calls are emitted.", "D1 " + S + "1.15")])

q(25, B, L, "D2",
 "The web-search subagent times out on a complex query. You are designing what it returns to the coordinator. Which approach best enables recovery?",
 ["Retry internally with exponential backoff and, once retries are exhausted, return a generic 'search unavailable' status.",
  "Catch the timeout and return an empty result set marked successful, so the pipeline continues without special handling.",
  "Propagate the timeout exception to a top-level handler that ends the research workflow and reports the failure.",
  "Return structured error context: the failure type, the query attempted, any partial results already gathered, and alternative approaches worth trying."],
 3,
 ("Structured error context is what lets the coordinator choose intelligently - retry with a narrower query, try another source type, or proceed with partial results and annotate the gap.", "D1 " + S + "1.9; Key Distinctions #8"),
 [(0, "Local retries are correct; collapsing the outcome into a generic status afterwards is not. The coordinator loses the query, the partial results, and every basis for choosing a recovery.", "D1 " + S + "1.9"),
  (1, "Marking a failure as an empty success suppresses the error entirely and silently ships an incomplete brief.", "D1 " + S + "1.9"),
  (2, "Terminating the whole workflow on one subagent's timeout discards work that succeeded and forecloses recovery that would likely have worked.", "D1 " + S + "1.9")])

q(26, B, L, "D1",
 "The synthesis subagent receives from document analysis a prose paragraph per source: 'The study found a 12% reduction, though the sample was small and the authors note the period was unusual.' Attribution is routinely lost by the time the brief is written, and reviewers cannot trace claims back to sources. What should the analysis subagent output instead?",
 ["A shorter prose summary per source, so less material is lost when synthesis compresses it further.",
  "Structured findings that separate content from metadata: the claim, the supporting excerpt, the source name or URL, and the publication date.",
  "The full source text, so synthesis can quote directly and attribution follows naturally from the quotation.",
  "A relevance-ranked list of sources, letting synthesis fetch and read the highest-ranked ones itself."],
 1,
 ("Structured claim-source mappings are what survive synthesis. Separating the claim from its metadata - excerpt, source, date - means attribution is carried as data rather than reconstructed from prose.", "D1 " + S + "1.5; D5 " + S + "5.11"),
 [(0, "Shortening prose loses attribution faster, not slower. The problem is the format, not the length.", "D5 " + S + "5.11"),
  (2, "Passing full texts pushes the whole analysis burden into the synthesis agent's context and defeats the point of the analysis step.", "D5 " + S + "5.5"),
  (3, "A ranked list defers the reading work rather than delivering findings, and duplicates the analysis subagent's role in the synthesis agent.", "D1 " + S + "1.5")])

q(27, B, L, "D1",
 "To cut latency, an engineer proposes that the document-analysis subagent send its findings straight to the synthesis subagent, bypassing the coordinator, and that synthesis request follow-up analysis directly when it needs more. What should you recommend?",
 ["Keep all inter-agent communication routed through the coordinator, which preserves observability, uniform error handling, and control over what each agent sees.",
  "Adopt the direct path but require both agents to copy the coordinator on every exchange for logging.",
  "Adopt the direct path only for the analysis-to-synthesis direction, keeping follow-up requests routed through the coordinator.",
  "Adopt the direct path and move error handling into each subagent, since each is closest to its own failures."],
 0,
 ("Hub-and-spoke exists for observability, consistent error handling and controlled information flow. Direct agent-to-agent exchange blinds the coordinator to what passed between them.", "D1 " + S + "1.2; Key Distinctions #6"),
 [(1, "Copying the coordinator restores a log but not control - it can no longer shape or intercept what each agent receives, only read about it afterwards.", "D1 " + S + "1.2"),
  (2, "A half-open path still breaks the pattern in the direction that matters, and the coordinator no longer knows what synthesis was working from.", "D1 " + S + "1.2"),
  (3, "Distributing error handling into every spoke is the duplication hub-and-spoke removes, and it produces inconsistent recovery behaviour across agents.", "D1 " + S + "1.2; D1 " + S + "1.9")])

q(28, B, L, "D2",
 "Subagents repeatedly issue exploratory tool calls to discover what exists in the internal research archive - listing collections, probing for date ranges, testing whether a topic is covered - before doing any real retrieval. These discovery calls are a third of all tool traffic. Which MCP capability addresses this directly?",
 ["A single `list_archive_contents` tool that returns the full catalogue when called.",
  "Prompt instructions describing the archive's structure so agents know what exists without probing.",
  "MCP resources exposing the archive's catalogue - collections, coverage windows, document hierarchies - so agents can see what is available without exploratory calls.",
  "A caching layer that stores the results of discovery calls so repeated probes are cheap."],
 2,
 ("Resources are the MCP primitive for exposing content catalogues. Tools take actions; resources make available data visible, which is precisely what removes the need for exploratory calls.", "D2 " + S + "2.6"),
 [(0, "This is the right information delivered through the wrong primitive - it is still a call the agent must decide to make, and it competes for selection with every other tool.", "D2 " + S + "2.6"),
  (1, "A prose description in the prompt goes stale as the archive changes and cannot convey coverage windows reliably.", "D2 " + S + "2.6"),
  (3, "Caching makes a wasteful pattern cheaper without removing it. The agent still spends turns discovering what a resource could simply present.", "D2 " + S + "2.6")])

q(29, B, L, "D5",
 "Two credible sources give different figures for the same metric: an industry association reports 34% adoption, a government survey reports 21%. The synthesis subagent currently picks the higher-quality source and reports one number. How should conflicting values be handled?",
 ["Report the midpoint of the two figures with a note that sources vary, which avoids privileging either methodology.",
  "Report both values with their source attributions and the methodological context, structuring the brief to distinguish contested findings from well-established ones.",
  "Report the government figure, since official statistics take precedence over industry association data.",
  "Omit the metric entirely, since a contested figure cannot support a defensible conclusion."],
 1,
 ("Conflicts are annotated with attribution rather than resolved by fiat. Preserving both values, their sources and their methodological framing lets the reader see that the disagreement is real.", "D5 " + S + "5.10; D5 " + S + "5.11"),
 [(0, "Averaging two incompatible methodologies produces a number neither source supports and hides the disagreement behind false precision.", "D5 " + S + "5.10"),
  (2, "A blanket source-precedence rule is still an arbitrary selection. It suppresses a real conflict the reader should be able to see.", "D5 " + S + "5.10"),
  (3, "Dropping the metric loses information. A contested figure, clearly labelled as contested, is more useful than silence.", "D5 " + S + "5.10")])

q(30, B, L, "D5",
 "The final synthesis call receives all subagent outputs concatenated into one long input, ordered by the sequence in which the subagents completed. Reviewers find that findings from the first and last subagents appear reliably in the brief, while a significant finding from a subagent in the middle is repeatedly omitted - even though its output is present and correct. What is the most effective fix?",
 ["Rotate the concatenation order each run so no single subagent is consistently disadvantaged.",
  "Compress every subagent output to under 2,000 tokens so the whole input fits in a range the model handles evenly.",
  "Re-run the synthesis call twice and merge the two briefs, so a finding missed once is likely captured on the second pass.",
  "Place a key-findings summary at the start of the input and organise the detailed outputs under explicit section headers."],
 3,
 ("This is the lost-in-the-middle effect. Leading with a key-findings summary and structuring the detail under explicit headers works with the model's position sensitivity instead of against it.", "D5 " + S + "5.2; Key Distinctions #20"),
 [(0, "Rotation moves the disadvantage from one subagent to another. Something is always in the middle.", "D5 " + S + "5.2"),
  (1, "Aggressive compression risks discarding the very finding that is being lost, and position effects persist within the compressed input.", "D5 " + S + "5.2"),
  (2, "Two passes doubles cost for a probabilistic improvement and leaves the underlying position effect untouched.", "D5 " + S + "5.2")])
