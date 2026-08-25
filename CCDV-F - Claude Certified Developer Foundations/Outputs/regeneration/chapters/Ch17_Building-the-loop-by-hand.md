# Chapter 17: Building the Loop by Hand

## Ten iterations, never used

A developer building a file-editing agent set a cap on its retry loop: ten iterations. The agent could read a config file, propose a fix, write it, validate it, and try again, up to ten times, before giving up. In every test run it converged in two or three iterations. In production it converged in one. The cap was never reached, on any run, before or after deployment. That number was never the problem. The agent went on to break a customer's production environment while behaving exactly as its ten-iteration loop was built to behave. The failure sat somewhere else in the build entirely, and this chapter is about finding where.

Building an agent loop by hand is flat-pack furniture without the instructions. You have every part: the tools, a model that can call them, a rough picture of what the finished thing does. What you don't have is a fixed order to assemble them in, unless you write one yourself. Skip a step, or do two of them out of sequence, and you can still end up with something that stands up and looks like a bookshelf. Whether it holds weight under load is a separate question, and it's usually not one you get an answer to until something is standing on it.

**Where the analogy breaks.** Furniture assembly forgives some reordering: tighten the screws in a different order and the shelf still holds. A loop's exit condition doesn't work that way. It isn't a step you can leave until late in the build; it's a boundary that has to exist before the first write reaches a live environment, and the furniture picture has no equivalent for that.

## Register, scope, iterate, exit

Four steps hold across every way of wiring a loop, whether you write it directly against the API or lean on a framework to carry part of the weight. You still write all four; a framework only changes how much of each you write yourself versus inherit.

**Register the tools.** Every tool the agent can call needs a schema entry: a name, a description, and the parameters it accepts. That entry is what lets the agent know, on any given turn, what's actually available to call. Getting this wrong runs in two directions. A tool named in the system prompt but never registered can't be executed when the model reaches for it. A tool that is registered but described so vaguely it overlaps with a neighbor gets picked inconsistently. The registration list has to be complete and each entry has to be distinguishable from the others.

**Scope the system prompt.** A prompt that says "handle this customer's request" hands the model a wide field to route across. A prompt that names the specific task and the specific tools available for it narrows that field to what the task actually needs. The difference shows up as routing reliability: a broad prompt produces broader, less predictable tool selection, because the model has less in the prompt to anchor a choice to. The prompt should name the task, name the tools that apply to it, and say nothing about tools the agent doesn't have.

**Handle the tool-use loop.** When an assistant turn contains one or more tool-use blocks, your code executes every one of them and returns a tool-result block for each, matched by id, before the next assistant turn can proceed. A turn with three tool calls needs three tool-result blocks back, all in the same round. This step is mechanical rather than a design choice. Miss it and the conversation itself stalls or gets rejected by the API, immediately, rather than degrading quietly the way a scoping problem does.

**Define exit conditions.** The loop runs until it receives a stop condition. Leave that condition undefined and the loop keeps requesting tool calls past the point where the task is actually finished, because nothing in the build has told it "done" already happened. An iteration cap, like the ten in the opening incident, is one kind of exit condition: it stops a loop from running away. It is not the only kind, and the incident below shows exactly what an iteration cap does not catch.

The checklist that verifies this wiring runs to five items, not four: tools registered, prompt scoped, tool-use loop implemented, exit conditions defined, and one more, at least one human checkpoint somewhere in the loop. Where that checkpoint belongs is a separate decision, worked out in chapter 19. What this chapter requires is narrower: that the checklist forces the question before the loop ships, and that the other four items on it are the same four steps just walked through, verified rather than re-taught.

## Why these four and no others

Each step exists to close one specific gap, and no step covers for a gap in another. An unregistered tool produces a call the loop can't execute; nothing about a well-scoped prompt changes that, because the tool still isn't there to call. An unscoped prompt doesn't stop the loop from running; it degrades which tool gets chosen, turn over turn, in a way that shows up as unreliability rather than as a hard failure. An unresolved tool-use block breaks the conversation outright, the moment the next turn is attempted, because the API is waiting on a result that never came back. A missing exit condition breaks nothing visibly either. It just keeps the loop running, spending tool calls, past the point where stopping was the correct move.

Four different ways to fail, one step assigned to each. Mapped onto the flat-pack picture, three of the four are ordinary instruction steps: the parts list, the picture on the box, the fastening sequence. The fourth, the exit condition, is the one the picture doesn't cover at all, which is exactly the gap the caveat above names. That is the whole of what "wiring the loop" means: closing all four gaps, in whichever order you build them, before the loop runs unsupervised.

## The write that passed validation and broke production

The file-editing agent from the opening had three tools: `read_file`, `write_file`, and `validate_config`. After each write it re-ran `validate_config`; if the result still failed, it adjusted the edit and wrote again, up to the ten-iteration cap. Tested against a scratch copy of the target config, it worked on every run, usually settling in two or three iterations.

In production, it found a parameter out of range, proposed a correction, wrote the file, and re-ran `validate_config`. The check passed. The loop exited after one iteration, exactly as built.

The parameter it corrected was a rate limit the customer's application depended on. `validate_config` checked the new value against the schema's allowed range, and the value was inside that range. The check had never been built to ask whether anything downstream still depended on the old one. Within minutes, the customer's application started failing: requests were being throttled at a rate it wasn't built to handle.

The loop did not misfire. It edited, validated, and exited on a pass, which is exactly what an exit condition scoped to "did this file validate" will always do. The gap sat between two states the loop never distinguished: a change proposed, and a change committed to a live environment. Nothing in the build stopped `write_file` from crossing that line unattended, and the ten-iteration cap was never built to catch it, because the cap only watches iteration count. If a tool can take an irreversible action in production, it needs a checkpoint before it runs, and that constraint belongs at the point where the tool surface is scoped.

## Where the tool list itself becomes the problem

Registering tools correctly is necessary, but a correctly-registered list can still be the wrong list. Two failure directions pull opposite ways here. A registry with too many overlapping tools, two entries both described as roughly "update a record," for instance, degrades routing on every turn: the model is choosing between near-duplicates, and picking wrong gets more likely as the overlap grows. A registry with too few tools forces the agent to either hallucinate a path that doesn't exist or return an incomplete result, because the capability it needed was never on offer.

Over-tooling is the shape that shows up after ship. A tool gets added "just in case" it's needed later, and it sits in the registry from then on, weighed against on every subsequent turn whether or not it's ever called again. It isn't a neutral addition. Selection quality degrades as the registered surface grows, so an unused tool is still a cost the loop pays on every decision, even the ones that never touch it.

The corrective is the same discipline applied one layer earlier than the system prompt: start with the minimum set of tools the task actually requires, and add one only once a specific gap in capability is confirmed, not anticipated. A prompt can only be scoped as tightly as the toolset it has to describe.

## Where this chapter's authority stops

This chapter covers the loop itself: registering tools, scoping the prompt, resolving tool-use blocks, and defining an exit condition. What the loop carries forward between turns, and what a subagent is for, is a different problem, covered in chapter 18. A deterministic action tied to a specific loop event is a hook, covered in chapter 19, outside the loop's own control flow. Which path actually runs this loop, a direct implementation, the Agent SDK, or Managed Agents, was decided before this chapter started, in chapter 16; whichever path you picked, all four steps above still apply to it. Where the checklist's human checkpoint belongs inside the loop is also settled elsewhere, in chapter 19.

## What the stem sounds like

A stem naming this chapter describes an agent already built or mid-build, and asks about the loop's own construction: whether a tool called is actually registered, whether the prompt names only the tools the agent has, whether every tool-use block gets a matching result, or whether an exit condition exists and what it fails to catch when it's scoped too narrowly, the way `validate_config` was.

## Self-test

**1.** An agent's system prompt reads: "Assist the user with their account." It has twelve registered tools spanning billing, provisioning, and support ticketing. Routing has become unpredictable. *(Select one.)*

A. Add more tools so the agent has a path for every request.
B. Raise the iteration cap so the agent has more attempts to find the right tool.
C. Narrow the system prompt to name the specific task and the specific tools it requires.
D. Remove the exit condition so the loop doesn't stop before finishing.

**2.** A loop's exit condition is "the tool result matches the expected schema." A tool call that matches the schema but takes an irreversible production action has just been proposed. Which addition closes the actual gap? *(Select one.)*

A. A higher iteration cap, so the loop has more chances to self-correct.
B. A more detailed tool description, so the model chooses more accurately.
C. A checkpoint between the change being proposed and the change being committed.
D. A broader system prompt, so the agent has more context about the task.

**3.** Which two of the following are required by the loop-wiring checklist independently of which path (direct implementation, SDK, or Managed Agents) runs the loop? *(Select two.)*

A. Every tool the agent may call is registered before the loop runs.
B. The loop has a defined exit condition that does not depend on the model volunteering to stop.
C. The agent is limited to a single tool to minimize routing risk.
D. The system prompt describes every tool the underlying framework makes available, whether or not the agent has it.

**4.** A team adds a fourth tool to an agent's registry "in case a future request needs it," though no current task calls for it. What is the most direct cost of that addition? *(Select one.)*

A. The unused tool has no effect until it is called for the first time.
B. It degrades selection quality on every turn, because the model weighs it against the others regardless of whether it's called.
C. It forces the loop's exit condition to be redefined.
D. It requires a human checkpoint to be added before the loop can run.

**Answers.** 1: C. Twelve tools behind a task-agnostic prompt is the over-tooling and unscoped-prompt pattern together; A and B spend complexity in the wrong place, and D removes a control the scenario never questioned. 2: C. A schema-matching result says nothing about whether the action itself is safe to commit, which is exactly the gap the file-editing incident exposed; A, B, and D all improve a part of the loop that was never the problem. 3: A and B. Registration and exit conditions are two of the four steps that hold regardless of path; C invents a rule the chapter never states, and D has the requirement backwards; the prompt should name only tools the agent actually has. 4: B. A tool sitting unused in the registry is still weighed on every routing decision; A treats it as free, and C and D attach consequences the scenario gives no basis for.
