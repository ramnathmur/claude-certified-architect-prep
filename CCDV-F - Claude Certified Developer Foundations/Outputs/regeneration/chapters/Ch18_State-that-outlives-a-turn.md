# Chapter 18: State That Outlives a Turn

## An agent that worked for months, until the fourth day

An agent built to help a support team work escalation cases ran cleanly through development. Every test session was long and continuous, ten to fifteen turns without a break, and the agent held the whole case in view the entire time. Production looked different: engineers opened the agent for twenty minutes, closed it, and came back a day or two later to pick the case back up. By the fourth of these sessions, the agent was spending over forty-five thousand tokens of its budget on history from the three sessions before it, plus the system prompt and tool schemas, before it did a single useful thing that day. It started returning incomplete answers partway through its analysis, and the first read on the failure was a broken tool.

The tool was fine. Nobody had decided what this agent should still know when a session starts, and what it should be allowed to lose.

## What a subagent starts with

Chapter 15 covered why a hierarchy exists at all: it splits one large context and one sequential loop into several smaller ones that can run at the same time. This chapter picks up right after that decision is made. Once the lead agent hands a piece of work to a subagent, what does the subagent actually have in front of it?

Its own context window, and little else. A subagent runs its task in a separate context and returns only its output; the main conversation history, the files accumulated during the session, and the session's current state all stay behind. It starts the way a locum doctor starts a shift on an unfamiliar ward: no memory of this particular patient, a chart written for the case rather than a colleague's memory of every prior visit, and enough on that chart to pick the case up without having been in the room for any of it. So does anything at all cross from parent to subagent automatically?

Two things, and they pull in opposite directions. Skills do not travel automatically: a custom subagent sees a project's Skills only when a Skill is explicitly listed in that subagent's own configuration, and a built-in subagent carries no preloaded skills at all. Permission context travels every time: whatever the parent session was allowed to do, the subagent is allowed to do too, without being re-granted. Conversation and instructions are scoped fresh at each delegation; permission is continuous across it.

Which built-in subagent handles the delegation also changes what's in view. Explore and Plan skip CLAUDE.md and git status entirely, trading that context for speed, so a project rule that lives only in CLAUDE.md is silently absent from either one. The general-purpose subagent loads both. Routing a task through Explore because it happened to be the fast option is how a rule that depends on CLAUDE.md goes unenforced, with nobody having changed the rule at all.

Here is where the chart stops holding up as a model for what's happening. A locum can still turn to the patient and ask a direct question, or lean on general medical judgment the chart never wrote down. A subagent cannot. Once it is dispatched, there is no channel back to whatever the parent session knows beyond what was handed over at the start. Anything left out has to be scoped in again — it cannot be requested later.

## Deciding what a session carries forward

The chart raises a second, harder question: what is worth writing down, so the next person on shift can pick the case up instead of re-learning it from nothing. Memory scope is this same decision, applied to an agent instead of a patient file: what it knows when a new session starts, and what maintaining that knowledge costs.

Four scopes cover the space.

In-context memory keeps state inside the live conversation itself. Retrieval costs nothing, because the state is already sitting in the window; the price shows up instead as every turn resending everything that came before, so the bill grows with the conversation's length, and none of it survives past the session that produced it.

External storage writes state to a database and reads it back at session start. State can survive any number of sessions and move between users or agent instances; the price is a read and a write on every access, plus the engineering work behind both.

Summarized memory compresses prior conversation into a condensed brief, generated once and injected at the next session's start. It costs less per session than replaying full history, and it only holds what the summarizer was told to keep. A prompt that says nothing more specific than "summarize the conversation" drops task-critical detail as readily as it drops small talk: which files changed, what a decision was, how an error got resolved.

Stateless memory keeps nothing. There is no retrieval, because there is nothing to retrieve, which fits a job that runs once, finishes, and closes out. It also leaves the agent with no way to answer a follow-up that depends on anything from before.

## Why the choice has to happen before the first line of code

Return to the escalation agent. In-context memory looked right in development, because development never asked it to survive a restart — one continuous session has nothing to carry forward. Production asked exactly that, many times over, and the same choice kept every prior session's history live and resent it in full at the start of the next one. By the fourth session, that accumulated history alone had passed forty thousand tokens.

The fix was a refactor to external storage: pull the accumulated history out of the live context, persist it, and load back only what the next session actually needs. It took about an hour once someone sat down to write it. The mechanism never changed between development and production. What changed was how many sessions the same state had to survive, and that was already knowable before the agent shipped. Production only made the cost visible.

An hour is cheap when a developer chooses to spend it in advance. It stops being cheap the moment it happens mid-incident, with a deadline already running and every hour of the rewrite borrowed from whatever the agent was supposed to be doing instead. The four scopes above are a menu available at design time, before any of the agent's memory-handling code exists. Deferring the choice doesn't remove it; it only moves the bill to a worse moment to pay it.

## The instinct to over-brief a subagent

The isolation that keeps a subagent's context small looks, at first glance, like something to compensate for: hand it as much of the parent's context as will fit, so it cannot possibly be missing something relevant. The mechanism says otherwise. A subagent is scoped to a task description, the minimum context that task needs, whichever results from prior steps are directly relevant to it, the tools required, and a clear exit condition. Padding that handoff with the parent's full history doesn't buy back the visibility isolation costs; the parent still gets only a summary at the end, now produced against a wider, noisier context than the task ever required.

This is also where delegating to a subagent earns its place as a way of managing what sits in the main session's window, a use separate from why a hierarchy exists at all. Spawning a subagent to explore an unfamiliar part of a codebase and answer one question keeps everything that exploration tried, every file it opened, every dead end, out of the main session entirely. The main session receives the answer; the search that produced it never enters its context. The price is specific: the intermediate steps are discarded along with the subagent's context, so if the returned answer turns out wrong, there is no transcript to walk back through to find where it went astray. That price is what the isolation buys, and a handoff scoped any wider would have paid the same price for a worse answer.

## A state problem and an instructions problem

Everything above answers one question: what an agent knows because of what happened in an earlier turn or session. A second, separate question sits right next to it: what an agent knows how to do, independent of any particular conversation. Skills answer that second question — reusable instructions stored on disk, loaded only when a request matches, so a project's full library of them never has to sit resident in a session that doesn't need it. CLAUDE.md answers the same question a different way, loading every session unconditionally regardless of the task at hand; its own mechanics belong to chapter 21. In-context instructions answer it a third way, present for exactly the session they were typed into and gone once that session ends.

The two questions get answered with the same fix often enough to name as a mistake on its own. State that should have been summarized and stored gets pasted into a system prompt as though it were a standing instruction. Instructions that belong in a Skill get repeated into context every session as though the agent would forget how to do the job otherwise. Carrying state and carrying instructions are different design decisions, made for different reasons, and reaching for the wrong container for either is exactly what fills a window that never needed to be full.

Where a subagent sits inside a hierarchy, rather than what it starts with once dispatched, is chapter 15's question. Which lifecycle events fire a script regardless of what the model decides is chapter 19's. The retry discipline a subagent needs once it can fail independently of the lead agent belongs to chapter 27.

## What the stem sounds like

A stem naming this chapter says "starts with no memory of the conversation" or "a subtask that doesn't need the full session" for the subagent mechanism, and "what should persist between sessions" or "token cost climbing every session" for memory scope.

## Self-test

**1.** A team routes a task to the built-in Explore subagent and expects it to follow a rule written only in the project's CLAUDE.md. The rule is silently ignored. *(Select one.)*

A. Explore and Plan skip CLAUDE.md and git status to stay fast; a rule that lives only in CLAUDE.md needs the general-purpose subagent or a custom subagent instead.
B. Subagents never load CLAUDE.md under any configuration, so no subagent could have followed the rule.
C. The rule was ignored because it wasn't listed in Explore's frontmatter.
D. CLAUDE.md only applies to the top-level session and has no relevance to any subagent, built-in or custom.

**2.** A custom subagent defined in `.claude/agents` needs a project Skill to do its job. The Skill never loads when the subagent runs. *(Select one.)*

A. The Skill must be explicitly listed in the subagent's own configuration; nothing loads automatically on delegation.
B. Skills load automatically for any subagent handling a request that matches the Skill's description.
C. Skills are limited to built-in subagents; a custom subagent can never use one, regardless of configuration.
D. The Skill failed to load because the subagent lacked the parent's permission context.

**3.** An agent receives a single job, completes it, and closes out. Nothing about the task depends on any earlier session. *(Select one.)*

A. In-context memory, since the state fits easily within one session.
B. External storage, to be safe in case a future session needs the result.
C. Stateless memory: there is nothing to retrieve, and no later session to serve.
D. Summarized memory, so a condensed version of the job is available afterward.

**4.** Which two of the following are accurate about what a subagent has available once a task is delegated to it? *(Select 2 of 4.)*

A. It inherits the parent session's permission context.
B. The general-purpose subagent loads both CLAUDE.md and git status.
C. Explore and Plan load git status while skipping CLAUDE.md.
D. A custom subagent automatically sees every Skill the parent session has available.

**5.** A team ships an agent that keeps all conversation state in-context, because early testing ran in one long continuous session. In production the agent runs many short sessions across several days, and by the fourth session its token budget is exhausted before it does any useful work. *(Select one.)*

A. The memory-scope choice should have been made at design time, based on how many sessions the state would actually need to survive rather than on how development happened to run.
B. The fix is to request a larger context window from the model provider.
C. This is a tool-selection failure and has nothing to do with memory scope.
D. Stateless memory would have prevented this, since it discards everything.

**Answers.** 1: A. Explore and Plan trade CLAUDE.md and git status for speed, so a rule that lives only in CLAUDE.md doesn't reach either one; B and D overstate the restriction, and C confuses the CLAUDE.md mechanism with the separate Skills-frontmatter mechanism. 2: A. Skills are not carried across delegation automatically; a custom subagent needs the Skill named in its own configuration. B overstates automatic loading, C is false (built-in subagents carry no preloaded skills either), and D confuses Skills with the separate, automatically-inherited permission context. 3: C. A job with no prior session and no future one pays no retrieval cost and needs none; A leaves the state to vanish with no benefit since nothing follows it, and B and D pay for persistence a one-off job never uses. 4: A and B. Permission context is inherited automatically, and the general-purpose subagent is the one built-in subagent that loads both CLAUDE.md and git status. C misassigns that behavior: Explore and Plan skip both together, rather than trading one for the other, and D overstates Skills as automatically inherited. 5: A. The mechanism didn't change between development and production; the number of sessions the state had to survive did, and that was a design-time question. B treats a scope problem as a capacity problem, C misdiagnoses the failure's source, and D solves the token problem by discarding memory the task actually needed.

## Claude Code Operation: Agent Memory

Everything above is scope-agnostic: it holds whether the agent runs against the raw Messages API, the Agent SDK, or Claude Code. Claude Code's own material for this concern is named Agent Memory, and two things about it are worth stating plainly here rather than leaving implied.

The first is that a Claude Code subagent's clean start is the same rule this chapter has already described, applied consistently regardless of which memory scope governs the rest of the session. A custom subagent defined in `.claude/agents` runs without the parent session's Skills unless a Skill is named explicitly in that subagent's own configuration. Leave a Skill off the list and its instructions simply are not present when the subagent runs. This is the isolation from earlier in the chapter, showing up in Claude Code's own configuration file rather than as a separate mechanism to learn on top of it.

The second is what Claude Code actually supplies automatically, which is narrower than it can look. CLAUDE.md is read in full at the start of every session, regardless of what that session's task turns out to be; chapter 21 covers what belongs in it and how it's scoped. What matters here is the boundary between that mechanism and this chapter's: CLAUDE.md is a fixed set of instructions, read the same way every session. A session's actual working history lives wherever a memory-scope choice puts it, using the same four options taught above. Claude Code doesn't add a fifth option, and it doesn't make the choice for you.

Past the subagent's clean start and CLAUDE.md's fixed, unconditional load, Claude Code leaves memory scope exactly where the rest of this chapter puts it: a decision chosen and built, for the same reasons, using the same four scopes. Running inside the CLI supplies the isolation and the always-on project file. It supplies neither a default answer nor an exemption from the question the escalation agent's team never asked before their agent shipped.
