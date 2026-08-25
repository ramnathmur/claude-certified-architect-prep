# Chapter 19: Where the Human Stands

## A boundary an audit can certify

A compliance reviewer signing off on an agent deployment tests one thing before anything else: whether this agent can be told, in the moment, to write to a path it isn't supposed to touch. The engineering team's answer is that the system prompt says not to, and the agent has followed that instruction in every test run so far. The reviewer doesn't accept it. A rule the constrained party could decline is not something an audit can certify, because there is no way to verify today what a different context window produces tomorrow. What the reviewer is certifying is the boundary's reliability across every run the agent will ever make, and a favorable track record on past runs certifies nothing about the next one.

That question decides two things this chapter covers: where a human checkpoint belongs in an agent's loop, and which of Claude Code's mechanisms actually hold a boundary rather than describe one.

## Four rungs, in order of what survives contact with the model

Four mechanisms can sit between an agent and a consequential action, and they do not hold with equal strength.

The weakest is a prompt-based instruction: a line in CLAUDE.md, a clause in the system prompt, telling the agent what not to do. The model reads it, weighs it against everything else competing for its attention that turn, and decides what to do next. Most of the time the instruction wins that competition. It doesn't have to.

A real instance shows the gap. A team's CLAUDE.md had grown to 847 lines over two months of additions, and line 347 read "Do not modify files in /legacy/tokens/." A user gave the same instruction directly in a prompt on top of it. The agent read both, then edited a file in that directory anyway while updating a related interface, because the other 846 lines had diluted how much weight any single line carried against everything else in the request. The rule was present in context the whole time. Presence and enforcement turned out to be different properties, and closing that gap is what the rest of this chapter is about.

One rung up is a permission mode: Claude Code's setting for whether a tool call must wait on a human's yes before it runs. This holds better than a prompt line, because the wait doesn't depend on the model choosing to comply. But it depends on something else: a human available to answer, and an operator who left the mode set to ask rather than switched to bypass for the afternoon. The approval flow that carries that yes or no back to the model is chapter 11's mechanism. What matters here is that an approval, however the mode is configured, is a single decision made at one point in time, good only for the action it was asked about.

## Where the checkpoint goes before it's a hook

Deciding where that single point should sit is a separate question from how the approval itself is wired. The governing test is which outcome would be worst if this step ran without a human check, and three points in a loop answer that test differently, at three different levels of risk. Before a destructive tool call (a write, a delete, a send) the risk is high: the worst outcome is irreversible, so a checkpoint here buys the most. After a planning step, before the agent starts executing what it planned, the risk is medium: the worst outcome is a coherent plan built on a wrong premise, expensive to unwind once several steps have already run against it. On unexpected output (an error flag, an empty result, a value outside the range the task expects) the risk is variable, and the worst outcome is a retry loop compounding a failure it can't see. That third point is what a checkpoint catches and plain retry logic never does, because retry logic assumes the same call will eventually succeed rather than asking whether it should be attempted again at all. A loop that places its only check somewhere convenient, rather than at one of these three, is answering a different question than the one that matters.

## The rule that outranks the rest of the rungs

Above a permission mode sits a deny rule: a rule that blocks a class of action outright, evaluated by Claude Code's own permission layer rather than consulted by the model. This is where a fact worth stating on its own terms belongs, because it is true of any layered permission system and not a fact about one product. When more than one rule applies to the same action, deny beats ask beats allow. The most restrictive rule that matches wins, in full, regardless of how many looser rules also match the same action. This is a fixed precedence rather than a tiebreak decided by which rule was written most recently or scoped most narrowly, and it holds the same way in a firewall's rule set or a filesystem's access-control list: one denied path stays denied no matter how many broader rules also happen to permit it. Claude Code implements exactly this precedence in its own permission settings; the mechanics of writing that rule, and how a deny entry is actually declared, belong to chapter 20.

## The checkpoint that doesn't ask

Above a deny rule sits a hook: a script Claude Code runs at a fixed point in the agent's lifecycle, independent of what the model decided to do at that point. The same gap that separated the diluted CLAUDE.md line from an enforced rule shows up here one rung further along. A PreToolUse hook doesn't compete with 846 other lines for the model's attention, because the model's attention is not what runs it.

Picture an airport security checkpoint. It runs a physical, independent check against everyone who reaches it, rather than asking a traveler to declare on their own recognizance whether they're carrying something prohibited, and that check runs regardless of what any individual traveler intends or claims at the moment they reach it. A hook occupies the same position relative to a tool call: it runs on its own schedule, outside the agent's judgment, and the tool call either clears it or doesn't.

The picture understates one thing about the real mechanism. A checkpoint is a single gate a traveler passes through once; a hook binds to seven distinct lifecycle events, so a session is checkpointed at several separate points rather than funneled through one gate. The events are PreToolUse, before a tool call executes; PostToolUse, after one completes; UserPromptSubmit, before the model processes a submitted prompt; Stop, when the model finishes responding; Notification, on a permission request or 60 seconds of idle time; SessionStart; and SessionEnd.

## Two hooks, two jobs

PostToolUse runs after the tool call has already executed, so it can't block anything, which makes it the right place for deterministic side effects that must happen every time regardless of what the model was focused on that turn: run a formatter after an edit, run the test suite after a source change, write an audit-log entry for a privileged action. Configure a PostToolUse hook to run a formatter and it runs on every matching edit, in every session, because the hook fires whether or not the model remembered to ask for it.

PreToolUse runs before the call, which means it can stop one. A PreToolUse hook can exit with code 2, which blocks the tool call and writes its reason to stderr, where the agent sees it and can adjust the next step. Pointed at a protected resource, this is the guardrail against a destructive action: a hook checking every write_file call against a single allowed path, say /workspace/output, denies anything the path doesn't start with, and logs both the blocks and the permitted writes as they happen. That log gives a reviewer the record of every privileged action before anyone asks to see one, because the entry was written at the moment the call was evaluated, sourced from the call itself rather than assembled later from memory or a transcript. The guardrail holds at every tool call, in every session, regardless of permission mode, which is what actually separates a guardrail from a convention: a convention is what the model is asked to remember, and a guardrail is what runs whether it remembers or not.

## What still has to sit above a hook

A hook only covers what it explicitly checks. A PreToolUse hook watching write_file says nothing about a network call to an endpoint nobody wrote a rule for, and a hook that's missing, misconfigured, or bypassed enforces nothing at all. The layer that holds in that gap is OS-level sandboxing: filesystem isolation scoped to the working directory and network isolation scoped to a named set of endpoints, both enforced by the operating system rather than by a script. Because that isolation runs beneath the hook layer, it holds even when a specific hook was never written to cover the path or endpoint in question. It is a separate mechanism with its own configuration surface, out of scope for this chapter. What carries forward is the principle the whole ladder has been climbing toward: no single layer, hooks included, is sufficient by itself. A defense built on one control failing closed is one bug away from an incident; a defense built in layers degrades instead of collapsing when any single layer is bypassed.

## What the stem is listening for

A stem describing a rule the model is asked to remember (a CLAUDE.md line, a system-prompt clause, an approval a human might or might not be watching for) is describing a convention, however firmly it's worded. A stem describing something bound to a fixed lifecycle event, that blocks with an exit code before the action completes, or that logs an action nobody had to remember to check, is describing a hook.

## Self-test

**1.** A team wants to guarantee that Claude Code never edits files under `/config/production/`, in every session, regardless of who is running it or what the current permission mode is set to. *(Select one.)*

A. Add a clause to CLAUDE.md instructing the agent not to edit that path.
B. Repeat the instruction in the system prompt as well, for reinforcement.
C. Configure a PreToolUse hook that checks the path on every write and exits with code 2 to block it.
D. Ask the team to set the permission mode to "ask" before working near that directory.

**2.** In Claude Code's permission settings, a deny rule and a looser allow rule both match the same tool call. Which rule applies, and why does that outcome not depend on anything specific to Claude Code? *(Select one.)*

A. The allow rule applies, because allow rules are evaluated last.
B. The deny rule applies; deny outranks ask outranks allow in any layered permission system, not just this one.
C. Whichever rule was configured most recently applies.
D. Whichever rule is scoped to the more specific file pattern applies.

**3.** Of the following four candidate checkpoints in an agent loop, select the two that match a governing test of "what is the worst possible outcome if this step runs unchecked" at high or medium risk. *(Select 2 of 4.)*

A. Before the agent executes a delete operation on a customer record.
B. After every successful tool call, regardless of what the call did.
C. After the agent has produced a plan and before it starts executing it.
D. Before the agent reads a file it has already read once this session.

**4.** Where does the airport-checkpoint analogy for a hook stop matching the real mechanism? *(Select one.)*

A. A checkpoint runs independently of what a traveler intends; a hook does not run independently of what the model decided.
B. A checkpoint is one gate a traveler passes through once; a hook binds to seven distinct lifecycle events spread across a session.
C. A checkpoint can be bypassed with the right documents; a hook cannot be configured incorrectly.
D. A checkpoint only screens people; a hook only screens tool calls, never lifecycle events.

**Answers.** 1: C. A and B are prompt-based instructions the model could still deprioritize under enough competing context, exactly as happened with the diluted CLAUDE.md line; D still depends on a human being present to answer. 2: B. This is the general precedence principle stated on its own terms: the most restrictive applicable rule wins in any layered permission system, and Claude Code implements it rather than inventing it. A, C, and D describe mechanisms (last-write-wins, most-specific-wins) that are not how this precedence works. 3: A and C. A destructive delete is the high-risk case and a completed plan is the medium-risk case from the governing table; B checks everything regardless of risk and adds no signal, and D is a read with no destructive consequence to guard against. 4: B. The seven lifecycle events are the one place the single-gate picture understates the real mechanism; A reverses the chapter's central fact, and C and D are not properties either the checkpoint or the hook were described as having.
