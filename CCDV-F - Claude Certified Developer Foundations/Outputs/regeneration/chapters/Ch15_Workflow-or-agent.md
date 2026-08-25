# Chapter 15: Workflow or Agent

## Five tools and no map

A team building an enterprise onboarding pipeline wired it as an agent. Every new account needs five things done: create the account record, verify the domain, provision seats, send the welcome email, notify the sales rep who closed the deal. The team registered all five as tools, wrote a system prompt describing the goal, "onboard this new account," and let Claude work out which tool to call and when.

For a few weeks it worked. Then the tickets started: an account provisioned before its domain was verified, a welcome email sent twice, a sales rep never notified because Claude judged the notification redundant on a run where the first four steps had gone smoothly. Every individual tool call succeeded. The sequence itself was the defect, and it was a different sequence almost every run, which made the failures hard to reproduce and harder to trust a fix for.

The five steps never varied: every new account needed the same order, every time, a fact that could have gone straight into code before a single system-prompt line was drafted.

## The enumerate-the-steps test

The onboarding pipeline is a workflow wearing an agent's clothes. The question that decides which one a task needs comes before any other design choice: whether you can enumerate the exact steps in code. If the steps can be enumerated, build a workflow, fixed logic, in an order you wrote. If the path itself has to be discovered at run time, from a goal and a toolset rather than a script, build an agent.

That one question forks into five more specific ones, and a mismatch on any of them is a signal the wrong pattern was picked.

| Choose a workflow when… | Choose an agent when… |
|---|---|
| You can enumerate the exact steps in code. | You can specify the goal and the tools, leaving the exact path unspecified. |
| Error cost is real and step-level guardrails matter. | The path cannot be enumerated in advance. |
| Observability with standard tooling is required. | Non-determinism is acceptable, and the agent's actions are bounded by its registered toolset. |
| Inputs are constrained to a known set. | Inputs vary unpredictably in content and structure. |
| Every execution follows the same sequence. | The task requires creative sequencing of the available tools. |

One variable does all the work across those five rows: how much of the path can be known in advance. Error cost, observability, and input shape are downstream of that one fact. A workflow is a script you commit to before the first request arrives. An agent is a decision you defer to Claude, request by request, constrained only by the tools you handed it.

That deferral is the whole trade this chapter is about. You buy an agent when you cannot enumerate the steps in advance, and what you pay for that flexibility is determinism: the same input can take a different route through the same toolset on two different runs, which is exactly what happened to the onboarding pipeline.

## Start simple, and earn the next step

The guidance for picking a pattern is a ladder, climbed one rung at a time: start with the simplest pattern that solves the problem, a single API call, then a workflow, then an agent, and move up only when the simpler pattern cannot handle the variability the task requires. An agent is the rung you reach for last, only once the simpler patterns have proven insufficient.

Two workflow properties make the case concrete. Error cost: a workflow's guardrails sit at the step where they're needed, so a bad output at step three is caught at step three, before step four ever runs on it. An agent's guardrails are harder to place, because there may be no fixed step three to place one at. Observability: a workflow produces the same shape of log entry on every run, so a dashboard built for a fixed sequence works unmodified. Reading an agent's log to find out why one run skipped the sales notification means reading a transcript rather than checking a line count.

Choosing agent carries one more cost worth naming, because it compounds with everything else: every tool you register adds to what the model has to choose between on every step, and a wide toolset degrades routing quality even when each individual tool is well described. Registering every tool a task might conceivably need, "just in case," carries that cost directly: each extra entry in the toolset is one more option the model has to weigh at every step, so a toolset padded past what the task requires degrades the very routing it was meant to protect. Start with the minimum set the task actually requires and add a tool only once a specific gap is confirmed. A workflow does not carry this cost the same way, because a workflow's steps call exactly the tools they were written to call, and nothing else is ever on the table.

## An assembly line against a repair shop

The clearest real-world version of this fork is the difference between an assembly line and a repair shop.

An assembly line is built once, for one product, in one order: weld the frame, mount the engine, fit the doors, run the paint booth, inspect. Every unit gets the same steps in the same sequence, and a guard or a sensor sits at each station because the station, and what can go wrong there, is known in advance. That is a workflow: enumerable steps, a fixed path, guardrails placed exactly where the risk is.

A repair shop knows its goal, fix the car, and its toolset, the bay's full set of diagnostics and tools, but not the path. A technician who hears a rattling noise does not run a fixed script; she listens, tests a hypothesis, checks a different part if the first one turns out fine, and assembles a sequence that fits the specific fault in front of her. That is an agent: a goal, a bounded toolset, and a path built at run time from what the situation turns out to need.

Where the analogy breaks: a technician can walk to a shelf you never labelled and grab a tool you forgot existed. Claude cannot. Whatever an agent does at run time, it does with the tools you registered and no others, the fifth row of the table above, non-determinism bounded by a fixed toolset. The improvisation is real, but it is a search over a space you defined in advance, rather than an open-ended one.

## Why a hierarchy exists at all

Everything so far describes a single agent: one loop, one context window, one set of registered tools. Some tasks outgrow that shape before they outgrow the workflow-or-agent question. A single agent's context window is one shared pot; every source it reads, every tool result, every intermediate note it keeps sits in the same window competing for the same space. A research task reading forty independent sources fills that window with the first several and starves the rest, and it reads them one at a time, because one loop can only do one thing at once.

A manager/supervisor hierarchy exists to solve exactly that problem: it splits one large context and one sequential loop into several smaller ones that run at the same time. A lead agent, the manager, decomposes the task and hands pieces to subagents, the workers, each with its own context window, working its own piece independently of the others. The lead is not doing the reading itself; it decides how to split the work and, once the pieces come back, compiles them into one answer.

That split is what a subagent is for, stated plainly: a subagent buys an isolated context window, so one source's worth of reading does not crowd out another's, and it buys parallel work, several pieces explored at the same time instead of one after another. Neither is available to a single agent's one-loop, one-window shape, however well the prompt is written.

## What the fifteen-times number is buying

Orchestrator-worker is the concrete pattern a hierarchy takes in practice: a lead agent plans, several subagents run in parallel against their own context, and the lead synthesizes what comes back. Anthropic's own multi-agent research system runs on this pattern. Against a single-agent baseline, the multi-agent version showed a substantial accuracy improvement on Anthropic's internal research evals, and it did so at roughly fifteen times the token cost of a normal chat interaction, because every subagent spends its own tokens against its own context.

Derive what that multiplier is paying for. A single agent answering a research question might spend on the order of ten thousand tokens. Splitting that into a lead plus four subagents means five separate contexts, each reading and reasoning independently, plus a synthesis pass over what they return. At roughly fifteen times the single-agent cost, a question that cost ten thousand tokens alone costs on the order of a hundred and fifty thousand tokens split across the hierarchy. The multiplier buys parallel exploration across independent sources. On a task that never needed splitting, it buys nothing.

The token cost is not the only thing a hierarchy multiplies. Every subagent is another place a call can fail, so the same retry and fallback discipline a single agent needs has to run independently inside each one. A subagent that hits a rate limit with no backoff can leave the lead waiting on a return that never arrives, holding up the whole compilation step. Spreading work across agents multiplies the surface area a failure can occur on at the same rate it multiplies the tokens spent.

That is exactly what happened to a real customer: an orchestrator-worker setup where the bill tripled and the answers barely improved, because the task was a sequence of dependent steps, each waiting on the last rather than a fan-out across independent sources. Moved back to a single agent with the same context, the bill dropped and the answer quality held. The lesson is not that orchestration is bad, but that the multiplier only pays off when the work actually splits into independent parts.

## Two questions, in order

Put the two decisions in sequence rather than making them at once. First: workflow or agent, decided by whether the steps can be enumerated in advance. Second, only once the answer is agent: does the task decompose into independent parts that can be explored at the same time, or is it a single chain where each step depends on the last?

Answer no to the second question and a single agent is the right shape; a hierarchy would spend the token multiplier on a parallelism the task cannot use. Answer yes, and the multiplier buys something real: research across many sources, a broad sweep where the pieces genuinely do not depend on each other's answers. Tightly coupled work, coding tasks among them, fails that second test even when it clearly needed an agent for the first: each step's output shapes the next step's input, so there is nothing to run in parallel, and a hierarchy here spends the multiplier on subagents that are, in effect, waiting on each other anyway.

Return to the onboarding pipeline the chapter opened with. The first question alone settles it: five steps, always the same order, so the whole thing is a workflow, with the tool calls written into code in the sequence they always run. If provisioning genuinely needed judgment somewhere inside that sequence, deciding which of a dozen seat configurations fit an account nobody had described in a fixed field, that one step could be an agent call embedded inside the workflow, invoked at the single place the path actually branches. The two questions apply per step, separately at each point in the task, and a pipeline can mix both patterns and still get the right answer at each point in it.

## When the input looks unpredictable and the path still isn't

A support-ticket system reads an incoming ticket, decides whether it belongs to billing, technical, security, or sales, and hands it to that team's queue with a summary attached. Every ticket's wording is different: different products, different tone, different length. A surface reading of the decision table says agent, the fourth row, inputs vary unpredictably, looks satisfied on the first pass.

The mechanism disagrees. What varies is the ticket's content, not the number of things the system can do with it. There are four categories and one action per category: classify, then route, then summarize. The step count and the step order never change; only which of four fixed branches gets taken changes, and that is exactly what a workflow's branching logic is for. Building this as an agent buys nothing, because there is no path to discover: the classification step decides the branch, and the branch was always going to be one of four.

The distinguishing question is whether unpredictable input still resolves into a fixed number of known next actions. A ticket classifier answers yes, four branches, and belongs in a workflow with a classification step. A research agent answers no, because which source it reads next depends on what the last one said, and that dependency is exactly what a workflow cannot express without hand-coding every branch in advance.

## Where this chapter's authority stops

Deciding workflow or agent, and if agent, single agent or hierarchy, is a design decision made before any code exists. Several things sit immediately on the other side of that decision and belong to other chapters.

Which wiring path actually runs the loop, writing it directly against the Messages API, using the Agent SDK, or handing the whole loop to Claude Managed Agents, is a separate choice that does not change which pattern you picked; chapter 16 covers it. Building the loop's own moving parts, registering tools, scoping the system prompt, handling the tool-use-and-result pairing, defining an exit condition, is chapter 17's job once workflow-or-agent has already been decided in the agent's favor. How a subagent is actually spawned, scoped, and handed a slice of the task, the mechanics behind "each with its own context window" above, belongs to chapter 18, along with the broader question of what state a hierarchy carries across a session. Deciding where a human checkpoint goes in an agent's loop is its own decision, made on the worst-case outcome of the step it guards, and it belongs to chapter 19. The retry and backoff discipline each subagent needs once it can fail independently is chapter 27's territory; this chapter only flags that a hierarchy multiplies how many places that discipline has to run.

This chapter's job ends at the fork itself: enumerable or not, and if not, parallel or not.

## What the stem sounds like

A stem naming this chapter's fork says "the exact steps are known" or "every case follows the same sequence" for a workflow, and "the path can't be predetermined" or "inputs vary in ways you can't enumerate" for an agent. A second consumer of parallel, independent subtasks, research across many sources, is the tell for a hierarchy; a chain of dependent steps is the tell against one, the same distinction that decides whether an orchestrator-worker setup's roughly fifteen-times token cost is buying parallel exploration across separate context windows or is being spent on subagents that end up waiting on each other's output anyway.

## Self-test

**1.** A team needs to process incoming invoices: extract the vendor name and amount, check it against a fixed approval-threshold table, and route it to one of three fixed approval queues. Every invoice goes through the same three steps in the same order. *(Select one.)*

A. Build this as an agent; invoice text varies too much for a workflow to enumerate.
B. Build this as a workflow; the steps and their order never change, only the values inside them do.
C. Build this as an orchestrator-worker hierarchy, so each invoice is processed in its own context.
D. Build this as an agent with a wide toolset, so it can improvise the path invoices most often need.

**2.** A team's task reads a single long contract and answers a chain of follow-up questions where each answer depends on the previous one. They configure it as a five-subagent orchestrator-worker setup to speed it up. *(Select one.)*

A. Justified: more agents finish work faster regardless of how the steps depend on each other.
B. Not justified: the steps are sequentially dependent, so the subagents mostly wait on each other while still paying the token multiplier.
C. Justified: a hierarchy always improves accuracy over a single agent on Anthropic's own reported evals.
D. Not justified: contracts should always be handled by a workflow, never an agent.

**3.** Which two of the following does delegating work to subagents in a manager/supervisor hierarchy actually buy, that a single agent's one loop and one context window cannot? *(Select two.)*

A. An isolated context window per subagent, so one source's reading does not crowd out another's.
B. A guarantee that the combined answer will always be more accurate than a single agent's.
C. Parallel exploration of independent pieces of the task at the same time.
D. A lower total token cost than running the task as a single agent.

**4.** A helpdesk system reads a free-text employee request and decides whether it needs IT, facilities, or HR, then opens a ticket in that team's queue with a one-line summary. Every request produces exactly one of those three outcomes. *(Select one.)*

A. Agent — the free text varies too widely for any script to handle.
B. Workflow with a classification step — three fixed branches chosen from varying input is still an enumerable path.
C. Orchestrator-worker — split the classification and the summary into two parallel subagents.
D. Managed Agents — offload the classification to Anthropic's hosted loop.

**Answers.** 1: B. The steps and their order are fixed; only the values differ, which is a workflow by the first row of the decision table, and A, C, and D each spend agent or hierarchy complexity the scenario never asked for. 2: B. Dependent steps cannot be explored in parallel, so the hierarchy pays roughly fifteen times the token cost for no parallel benefit; A and C overstate what the pattern guarantees, and D overcorrects into a rule the chapter never states. 3: A and C. Isolation and parallelism are what a hierarchy adds that a single loop cannot; B and D overstate the trade, since a hierarchy buys parallel reach without guaranteeing either automatic accuracy or savings. 4: B. Three fixed branches chosen from varying free text is still an enumerable path with a classification step; A mistakes input variety for path variety, and C and D spend complexity the three-branch, low-volume task never needed.
