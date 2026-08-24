# -*- coding: utf-8 -*-
"""Lessons 3, 4 and 5, verbatim as taught."""

L3 = dict(
    slug="prompting",
    nav="Prompt Engineering",
    title="Prompt Engineering and Structured Output",
    weight="20% of the paper, about 12 questions",
    body=r"""
Twenty percent, so about twelve questions. You've sat in the low eighties here on every paper, which is consistent rather than weak, and the marks you drop are scattered rather than clustered.

The objectives cover six things: writing explicit criteria to cut false positives, using few-shot examples, forcing structure through tool use and JSON schemas, building validation and retry loops, deciding when batch processing fits, and designing multi-pass review.

## The form and the blank sheet

Ask ten people to write their details on a blank sheet of paper and you get ten different shapes. One writes the date as the eleventh of March, one writes it the American way round, one writes the month in words. Hand them a form with labelled boxes and you get one shape, ten times.

That's the whole chapter. Everything below is either about writing better instructions on the sheet, or about replacing the sheet with a form.

## Stop telling it to be careful

Take the naive design first, because you've written it yourself. You want an automated review that catches comments lying about what the code does, so you write: check that comments are accurate. It flags a comment for old-fashioned wording. It flags one where the function was renamed. It flags a terse but perfectly correct one.

The instruction that works states the condition: flag a comment only when the behaviour it claims contradicts the actual behaviour of the code. That's a sentence you can write, so write it. General instructions like "be conservative" or "only report high-confidence findings" don't sharpen anything, because they describe a disposition rather than a test.

Now the consequence, which is underpriced. Suppose style findings are wrong about half the time, documentation about the same, performance under one in five, and security about one in twelve. The humans reading the queue do not score you category by category. They learn one thing, which is that this bot is usually wrong, and then they close the security findings unread. **A high false-positive category doesn't cost you that category. It costs you the accurate ones too.**

You dropped a mark on this in Exam 5, and the reason is worth naming. You chose the slow, correct fix over the urgent one. When trust is actively bleeding, you disable the noisy category now and improve its prompt afterwards. Getting the direction right and the urgency wrong is a specific failure mode, and it shows up more than once on this paper.

## When to show it and when to say it

This one has caught you more than once, so slow down here.

Some rules you can state, and some you can only demonstrate. If the rule is statable, state it. Reaching for examples when a clean criterion exists is more work for a weaker result.

Some things resist statement. How to handle a document where the reference sits in a footnote rather than inline. Which of two plausible tools fits an ambiguous request. What "actionably specific" looks like in a review comment. For those, two to four examples aimed at the ambiguous cases will do what another paragraph of prose will not.

There's a third case, and it's where you lost marks in Exam 5 and again in Exam 6. When the task involves a multi-step derivation, an invoice where you apply the discount to the net and then the VAT to the discounted net, what's missing is neither a criterion nor an example. It's the order of operations. That calls for a step-by-step reasoning instruction. Few-shot examples demonstrate format and judgement; they convey an arithmetic procedure only by accident.

So before you answer, ask which of the three the stem is describing. Inconsistent shape wants examples. Vague filtering wants a criterion. Wrong arithmetic wants a reasoning cue.

## Now the form itself

You asked politely for JSON. You wrote "respond only with valid JSON matching this schema" and you meant it. What came back some of the time was a friendly sentence, then a code fence, then JSON with a trailing comma. Somebody bolted a repair library on downstream.

The form is a tool whose input schema is exactly the structure you want, with `tool_choice` set so the model must call it. Now the shape is guaranteed by the mechanism rather than requested in prose.

Three modes and one decision. `auto` permits a text response, which is the behaviour you're trying to eliminate. `any` requires a tool call but lets the model choose which, and that's what you want when several extraction schemas exist and you don't know the document type in advance. Forcing a specific named tool guarantees both the call and the schema, which is right when one particular extraction has to run first.

Then the moment I want you to feel, because you met it in Exam 4 and missed it. You move the pipeline onto the forced tool call and parse failures go to zero and stay there for a month. Then reconciliation reports invoices where the line items don't add up to the stated total, at roughly the rate they always did.

**A strict schema guarantees shape, not meaning.** Line items that don't sum, a value sitting in the wrong valid field, a date that's well-formed and wrong: all of those pass validation cleanly. Tightening the schema cannot reach them, because there is nothing structurally wrong with them.

## Boxes that let it say nothing

Mark a field required only when the information is genuinely always in the source. A required field with nothing to fill it is pressure, and what the model produces under that pressure will look exactly like a purchase order number and appear nowhere in the document. Nullable fields give it a correct way to say the information isn't there.

Enums do the same job on the other axis: a fixed set of allowed values makes a wrong value unsayable, and an "other" value with a detail string keeps the set extensible. An "unclear" value handles genuine ambiguity honestly.

Validation is your code's job, and it happens in two layers. The structural layer checks types and required fields, which is cheap and deterministic. The meaning layer is where the marks are: line items must sum, the start date must precede the end date, the tax must match the rate.

When validation fails, retry with the specific error attached, along with the original document and the failed extraction. That recovers format errors and structural slips. It recovers nothing when the information isn't in the source. Forty documents failing on a purchase order number that only exists in a separate master agreement will fail forty times, however you phrase the retry.

There's an elegant move here worth remembering. Instead of checking the arithmetic afterwards, ask for both numbers in the same response: the total as written, the total re-derived from the line items, and a boolean saying whether they disagree. Now the contradiction is data, and your pipeline routes flagged records to review at extraction time.

## The cheap lane

Short section, nearly free marks, two constraints to hold.

There's a second way to submit work: bundle it and send it off. It costs half. It can take up to a full day, and while it's usually quicker, nothing promises that. Overnight technical-debt reports, weekly audits, nightly test generation, ten thousand documents in bulk: take the discount. Anything a person is sitting and waiting for stays synchronous.

Two more facts. Batch requests cannot execute tools mid-request and feed results back, so an iterative review that fetches related files as it goes cannot be batched at all. And `custom_id` is how you correlate requests with responses, which is what lets you resubmit only the twelve documents that failed rather than reprocessing all three hundred.

## Two passes are not two opinions

When one prompt is doing several jobs at once, the output goes shallow across all of them. You dropped a mark in Exam 5 by reaching for a clearer instruction where the answer was to break the work into a chain: identify the issues, then separately generate fixes for the issues you identified. Each step's output feeds the next.

That's for predictable work where you know the steps. The sharper point is about review. Splitting a fourteen-file review into per-file passes plus a cross-file integration pass fixes attention dilution, and the diagnostic symptom is one reviewer contradicting itself inside a single job. A bigger context window does not fix it, because the problem is attention rather than capacity.
""")


L4 = dict(
    slug="tools",
    nav="Tool Design & MCP",
    title="Tool Design and MCP Integration",
    weight="18% of the paper, about 11 questions",
    body=r"""
Eighteen percent, so about eleven questions. This is your most volatile domain by a distance: forty-five percent on your first paper, a hundred percent on Exam 7, and swinging between seventy and ninety since. It also holds four of your five most-repeated misses. If you only have time to work on one area this week, it's this one.

The objectives cover five things: designing tool interfaces with clear boundaries, returning structured errors, distributing tools across agents and configuring tool choice, integrating MCP servers, and selecting among the built-in tools.

## Two desks with the same word on the door

Two colleagues sit at two desks and the same word is on both doors: Analyst. You have a job in your hand and you've never met either of them. All you have is the word on the door, so you guess, and you're right about half the time. Half your work lands on the wrong desk, gets half done, and comes back late. Nobody did anything wrong.

**When Claude picks a tool, the description is the primary input it uses to decide.** There is no separate routing model, no hidden intent classifier, no lookup table behind the scenes. So a description is not a comment left for the next engineer. It is live production logic written in English.

That has a second consequence people miss under pressure. Descriptions are not fetched when needed. Every tool you give an agent travels with every request: name, description, input schema, all of them, every single turn. So every tool you add taxes every decision the agent makes.

A description has to say four things, and I'd learn this as a list because the exam grades against it almost directly. What the tool does and what comes back. What input it accepts, with formats and example values. When to use it rather than the tool standing next to it. And when not to use it, with the boundary said out loud.

You've lost marks on this twice, Exam 4 and Exam 6, and both times the correct answer was to expand the description. The distractors are consistent: a routing layer that parses the request before the model sees it, a pile of few-shot examples, or merging the two tools into one. The routing layer is over-engineering that also discards the model's language understanding. The examples add tokens without touching the cause. Merging is a defensible architecture change that costs far more than a first step should.

One trap that catches people who've learned all of the above. Production logs show that when a message contains the word "account" the agent calls the customer lookup first, and when the same request is phrased without that word it calls the order lookup. You read the descriptions and they're genuinely good. Go and read the system prompt, because keyword-sensitive wording there can create an association that overrides a well-written description.

And the mirror image, which you'll meet as the MCP question. You stand up a semantic code-search server that's better than the built-in, and the agent keeps using Grep. Nothing is broken. Selection ran on descriptions the way it always does, the built-in has a clear familiar one, and yours says something vague about searching code. The fix is to write what yours uniquely does and what the built-in cannot provide. Removing Grep breaks every legitimate content search, and a blanket "prefer MCP tools" rule is blunt and keyword-sensitive.

## Eighteen tools is the bug

An agent holding eighteen tools calls the wrong one often. A comparable agent holding four or five scoped to its job selects correctly. Same model, same quality of description. The only difference is how large a choice each one is being asked to make.

So scope by role. Where one cross-role need is genuinely high-frequency, give a narrow tool for it rather than the whole toolkit. The canonical case is a synthesis agent that needs to check simple facts eighty-five percent of the time: give it a scoped fact-check tool, and let the complex fifteen percent keep routing through the coordinator.

Parameters are part of the same job description. If a parameter has a known set of values, don't accept free text for it, because a fixed set makes a wrong value unsayable. And what comes back is a design decision too: return the identifiers the next step will need, because the customer lookup returns a verified customer ID precisely so the order lookup has something reliable to use.

## The courier who came back

Now failures, where a large share of your marks in this domain have gone.

One flag does the work here. A tool result carries `isError`, set true when the call failed, and that's the whole mechanism. A failed call and a successful call come back through the same door in the same shape.

There are exactly four kinds of failure, and each demands a different move. Transient, where the service was busy or the call timed out, and the same call made again in a moment has a real chance. Validation, where your request was malformed, and the same call will fail identically forever. Business, where the request was well-formed and policy refused it. Permission, where the caller isn't authorised.

Here's where your marks have been going. Two lines in the log both say the lookup did not return the record. One is a database that was briefly unreachable and will answer next time. The other is a customer ID that does not exist and never will. Hand both to the agent as "lookup failed" and it has one move available, and it will make that move on both.

So a failure has to carry four things: what kind it was, what was attempted, whatever partial results you did get before it broke, and what else could be tried. Give the caller what a decision needs.

And the one that reads as a paradox until you say it out loud. A courier who reaches the right address and finds the house empty has not failed. He has told you something true. **Zero matching results is a successful call, not an error.** Flag it as an error and the agent retries a query that was already answered correctly.

There's also an order to who handles what, and several questions are only asking you to name the lowest level that can deal with the thing. Transient failures are retried inside the tool, with backoff, and the agent never hears about the timeout that cleared on the second attempt. A subagent recovers what it can locally and propagates only what it cannot, along with what it attempted and what it has. Swallowing an error by returning empty success and aborting the whole workflow on one failure are both anti-patterns, and they're opposites.

## The universal socket

You found the right picture for this one yourself, so I built on yours rather than handing you a new one. It's a socket. One agreed shape of plug, and anything built to that shape fits.

A server can offer three kinds of thing. Tools are actions the model can call. Resources are read-only data it can access, which is your content catalogue: issue summaries, documentation hierarchies, database schemas. Prompts are saved templates. Sort them by who decides, and they stop needing to be memorised: the model acts, the application supplies readable data, a person runs a saved workflow.

Now a belief that will cost you a mark. Connecting a server does discover things automatically, and tool definitions from every configured server show up at connection time and are all usable at once. That part is real. The step too far is concluding that your data has arrived. Discovery tells the model what it can ask for. It does not put the contents of your issue tracker into the conversation.

The half that separates passing from nearly passing is what the socket never promised. It gives you one way to describe a capability, one way to call it, and discovery at connect time. It does not give you retries, backoff, what a failure means, which agent gets which tools, or a gate that runs before the call. The plug fits. Nothing about the plug makes it safe.

Which leads to a line worth carrying: a label is not a lock. When a server's own description calls one of its tools read-only or harmless, that's a hint for selection, not a safety boundary you can rely on.

Two files, learned by what they reach rather than by their paths. The project file at the repository root is version controlled and reaches everybody who clones, which makes it the file for team tooling, with `${TOKEN}` style expansion so each developer supplies their own credential. The personal file in your home directory reaches only you, which makes it the file for your own overrides and the server you're trying out this week.

And borrow before you build. For a standard integration use the community server that already exists, and build your own only for a workflow nobody outside your team has.

## The one you've missed four times

Two tools are called back to back in almost every turn, always in the same order, and an engineer proposes collapsing them into one composite tool. You've now got this wrong in Exams 5, 8, 10 and 11.

The corpus favours instructing the model to bundle the two calls into a single turn over hiding them inside a composite tool. The reasoning is that a composite conceals two distinct operations behind one description and one error surface, so when the second half fails the model can no longer tell which half failed or recover selectively. Prompt-level bundling keeps each tool's purpose and failure mode visible.

I want to be straight with you about this one. Four misses on a section that carries a single teachable point is not a comprehension problem. It's that the composite tool genuinely is the better engineering instinct in many real systems, and your instinct is firing correctly against what the paper wants. So don't try to re-derive it in the exam hall. Recognise the shape, which is two habitually-paired calls and a proposal to merge them, and answer against your instinct.

The related one you've missed three times is the preview. A destructive action must not be reachable without its preview, and a `dry_run` boolean is a parameter the model fills in, so the first call of a conversation can set it to false. Two tools bound by a single-use token make the bypass structurally impossible, because the token does not exist until the preview has run.
""")


L5 = dict(
    slug="context",
    nav="Context & Reliability",
    title="Context Management and Reliability",
    weight="15% of the paper, about 9 questions",
    body=r"""
Fifteen percent, so about nine questions. The smallest domain, and the one you're most reliably good at. You've had perfect scores on five of eight papers.

I should correct something the original chapter told you, though. It opened by saying nine out of nine, and that was true when it was written. The two papers you've sat since have each cost you one mark here, so it's very strong rather than untouchable.

The objectives cover six things: preserving critical information across long conversations, escalation and ambiguity, error propagation across agents, managing context in large codebase exploration, human review and confidence calibration, and preserving provenance through synthesis.

## The consultant who forgets

The picture underneath all of it is the sharpest consultant you've ever worked with. Hand her a file and in ninety seconds she finds what everyone else missed. She has one condition: the second she walks out of the room, everything goes. The skill stays, the file goes, your name goes, what you agreed goes.

So there is no server-side memory. The model remembers only because your application resends the prior messages in the array every single time. You lost a mark on this in Exam 6, and the reason is a good one. You've built systems that work the other way, web sessions have identifiers, and long-lived assistants really do sit on top of retrieval. So when a scenario says the assistant forgot something, the instinct is to reach for a session parameter or a vector store. Neither is the mechanism, and any option naming a `session_id` style parameter is describing something that does not exist.

Four things occupy the window on every call: the standing instructions, the tool definitions, the whole message history, and every tool result that has ever come back. Two of those are a fixed cost, the same size on turn fifty as on turn two. The other two only grow.

There's a quieter version of this that you should watch for. A persona in the standing instructions is exactly right for the first few exchanges and generic by the seventh. The standing instructions are not dropped. They're sent again every time. They get outvoted, because accumulated assistant turns dilute their influence. At two or three thousand tokens nothing has overflowed, so an option blaming the window is describing something that cannot have happened.

## Room is not attention

Here is the idea the chapter hangs off. Space on the desk and attention paid to what's on it are two different quantities, and only one of them is fixed by the size of the window. The start of a long input gets read properly, the end gets read properly, and the middle is where things go missing.

That's not a capacity problem, so a bigger window doesn't fix it. Lead with a key-findings summary and organise the detail under explicit section headers, which works with the position effect rather than against it. Rotating which agent's output goes first just moves the disadvantage around, since something is always in the middle.

Then the volume problem. An order lookup can hand back forty fields when five matter, and those forty do not evaporate after the turn that needed them. They sit in the history and get resent on every later call. So cut results down as they arrive, before they enter the record at all.

And compression, which does not degrade evenly. It eats precision before it eats topic. The customer said "the fifteen percent discount I mentioned," and twenty turns later the record says "promotional pricing was discussed." The topic survived and the fact did not.

Which gives you the move that answers half this domain. Pull the transactional facts into their own block: customer ID, order ID, amount, issue, current status. That block lives outside the summarised history, gets updated the moment a new fact appears, and goes into every prompt regardless of what's happening to the rest of the record.

You dropped one mark here in Exam 6, on the hybrid shape. A sliding window that keeps only the last few exchanges works until something said early turns out to matter late. The allergy was mentioned in the first two minutes and the window dropped it hours ago. So the shape you want has three parts: recent exchanges word for word, a running summary behind them, and the facts block that is never compressed. A bigger fixed window delays the same loss.

There's one case where none of that applies. Months of conversation, eighty-five thousand tokens, and somebody asks what you concluded about one thing back in the spring. That's a finding problem rather than a compression problem, and progressive summarisation is precisely wrong for it, because it turns the specific conclusion you want into an abstraction. Semantic retrieval over the stored exchanges is the answer.

## Five reasons to stop

A team worried about giving up too early writes a rule that sounds like discipline: do not escalate until you've made three genuine attempts. Then a customer's first message is "I want to speak to a manager," and the agent obediently offers a replacement, then a store credit, then a partial refund.

Learn the triggers as shapes rather than as a list. Someone asks for a person, and that's the whole test, so hand over now. The action needs authority the agent doesn't have. The policy is silent on the situation. The agent cannot make meaningful progress. And the case involves something the agent has no way to verify.

The policy-silence one is worth sitting with. A customer asks you to match a competitor's advertised price, and your written policy covers price drops on your own site and says nothing about other retailers. Two answers look reasonable to a tired candidate. Applying the own-site rule by analogy invents an entitlement. Refusing because the policy doesn't authorise it invents a prohibition. Both have the agent making policy it was never delegated.

Then the one that looks like an escalation and is not, which cost you a mark in Exam 11. A customer lookup returns several matching records under the same name. That feels like ambiguity, and you've just learned ambiguity is a trigger, so the reflex fires. This ambiguity is one question away from being resolved: ask for the email, the order number, another identifier. Escalating spends a human interaction on something the agent could close itself.

Four proxies fail, and the exam will offer you three of them as options. Sentiment, because mood is not difficulty and a calm paragraph can describe a case needing a policy exception. Self-reported confidence, because an agent already wrong on hard cases is confidently wrong. A trained classifier, because it needs labelled data and infrastructure before prompt work has been tried. An attempt counter, for the reason at the top of this section.

When you do hand over, remember the paramedic. The human receiving your escalation does not have the transcript. That's a design assumption rather than a limitation to route around, so everything they know is what your agent compiled: the verified customer ID, the root cause, the amounts, and a recommended action.

## Finishing what you can

Not every stop is a handoff to a person. In a multi-agent system there's often nobody to hand to, and part of the work genuinely cannot be completed.

Two failure modes here, and they're opposites. Fake success is a subagent catching an access failure and returning an empty result marked successful, which prevents any recovery and quietly ships an incomplete answer. Total abort is one failure killing a workflow where recovery would have worked.

The right behaviour, which you missed in Exam 4, is to complete the synthesis with what exists and annotate the output so a reader can tell which conclusions are well supported and which are affected by missing sources. Uncertainty gets propagated upward rather than hidden.

## The notebook and the claim record

Two last habits, and they're the facts block wearing different clothes.

A long investigation keeps a notebook, in a file rather than in the conversation. Findings get written down as they land, and each continuation reads it back. On the paper this is called a scratchpad file, and that's the wording the option will use. The same idea handles crash recovery: each agent exports its state to a known location, and the coordinator loads the manifest on resume.

And a claim is never stored as a sentence. It's stored as a record carrying the claim, the source name, the link, the publication date and where in the source it came from. Attribution dies during compression for exactly the reason amounts die, because it's detail, and detail is what gets dropped. Publication dates matter more than they look: without them, a genuine change over time reads as two sources contradicting each other.

When two credible sources genuinely disagree, annotate both with their attributions rather than picking one. Averaging them produces a number neither source supports.

Every answer in this domain is the same answer underneath. Decide what must survive, and take it out of whatever is going to be compressed, dropped, buried in the middle, or lost in a crash. The facts block, the trimmed result, the scratchpad, the state manifest and the claim record are five names for one habit.
""")


CLOSING = dict(
    slug="plan",
    nav="Where to spend the days",
    title="Where to spend the six days",
    weight="Reading order and priorities",
    body=r"""
Tool Design first, and by a margin. It holds four of your five repeated misses, it's your most volatile domain, and the composite-tool question alone has cost you four marks across four papers.

After that, the two Claude Code items: the concatenation of memory files, and the two skill frontmatter keys. Those are pure recall rather than judgement, so they are the cheapest marks available to you this week.

Everything else you're already scoring above ninety on, and re-reading it has diminishing returns compared with sitting Exam 13.

## Your record, so the priorities have something behind them

Eight scored papers, every one of them clear of the 720 line.

| Paper | Sat | Score | Scaled |
|---|---|---|---|
| Exam 4 | 11 Jul | 45 / 60 | 775 |
| Exam 5 | 11 Jul | 52 / 60 | 880 |
| Exam 6 | 12 Jul | 49 / 60 | 835 |
| Exam 7 | 16 Jul | 55 / 60 | 925 |
| Exam 8 | 28 Jul | 52 / 60 | 880 |
| Exam 10 | 29 Jul | 54 / 60 | 910 |
| Exam 9 | 9 Aug | 49 / 60 | 835 |
| Exam 11 | 10 Aug | 55 / 60 | 925 |

Domain averages across those eight: Agentic Architecture around ninety percent, Context Management around ninety-two, Claude Code around eighty-four, Prompt Engineering around eighty-three, Tool Design around seventy-seven. That last number is why Tool Design goes first.

## The three concepts that have cost you the most

The composite tool against prompt-level bundling, missed in Exams 5, 8, 10 and 11. Four papers running on a section that carries one teachable point.

Two-tool token binding against a bypassable parameter, missed in Exams 4, 5 and 6.

The CLAUDE.md files concatenating rather than overriding, missed in Exam 4 twice and again in Exam 7.

If nothing else survives this week, let it be those three.

## On the day

Sixty questions, a hundred and twenty minutes, so two minutes each. Four scenarios drawn from the six, and you have no say in which four.

Before you read the options, name the room you are in and name the surface or the mechanism the question is about. Delete any option that names a flag or parameter you have never seen. Delete any option that adds a classifier, a trained model or a routing layer when a description or prompt fix has not been tried. If the stem tells you every component succeeded, the fault is in what they were asked to do. And if money, identity or policy is involved, prefer the deterministic option over the persuasive one.

Mark the genuinely uncertain ones and move on. A question you leave half-solved costs you the two easy ones sitting behind it.
""")
