# Chapter 8: Keeping a long session inside the budget

## Forty clean turns, then thirty strange ones

A coding agent completes forty turns of a long refactor cleanly. By turn seventy, in the same session, its answers have grown vague, and it re-asks a question the user already answered twenty turns earlier. Every measure chapter 1 established still reads clean here: no rejection before generation, no cutoff mid-generation, the window comfortably under its limit. What the window holds has simply stopped describing the task.

Chapter 1 already established that a session's context window is one fixed pot, refilled in full on every request, and that it fails in exactly two ways: rejected before generation, or cut off mid-generation. This chapter covers a third failure, one that shows up while the pot still fits and is already carrying the wrong thing.

## A pack for a long trek

A hiker planning a multi-day trek does not decide what to carry once, at the trailhead, and stop thinking about it. Weight gets managed the whole way, and different situations call for different moves: doubling back past a wrong turn and dropping the detour that led nowhere, mailing a bulky item home once a condensed note of it is all that is still useful, walking away from the whole pack and starting the next leg with a fresh one, or handing a side-errand to a companion who goes, does it, and reports back only the result.

A long agent session is the same kind of ongoing weight problem. Four instruments manage it, and each trades away a specific kind of continuity for the room it buys back.

**Pruning** rewinds the session to an earlier point and drops everything after it. It is the right move once a path has stopped being useful: Claude went down a debugging tangent that led nowhere, or explored an approach that was abandoned. The turns after the rewind point are gone entirely, so anything Claude worked out during that stretch has to be worked out again if it turns out to matter later.

**Compaction** replaces the accumulated history with a condensed summary that keeps the parts still needed and drops the rest. The summary costs a fraction of the tokens the original turns did, which is the entire point, but only what the summary captures survives. A summarizer told to "summarize the conversation so far" tends to keep the general shape of what happened and lose the specifics. The same instruction told to preserve every file path touched, every decision made at a branch point, and every error and how it was resolved keeps exactly the state a session actually depends on. What the summarizer was told to treat as worth keeping decides what survives, far more than the act of summarizing itself does.

**Clearing** drops everything and starts over with an empty window. Nothing carries forward at all, which is correct the moment the next task has nothing to do with the last one and old context would only bias the new attempt. Clearing keeps nothing, worth keeping or not, so anything that has to survive a clear has to be written somewhere outside the session itself first, a project's own standing instructions file being the standard place.

**Handing a scoped task to a second window** leaves the first three untouched. Instead of carrying an entire exploration inside the running session, a self-contained piece of it is handed to a separate window that has only the task description and what it needs to do the job, and that window works, then returns just its answer. The parent session carries only the conclusion; the exploration itself never enters it. What is lost is visibility into how that conclusion was reached: the intermediate steps live and die inside the second window, and if the reasoning behind the answer matters later, it is not there to inspect.

None of the four is free, and none is a default. A short, single-purpose session that never approaches its own limit does not need any of them; deciding what to prune, compact, or delegate carries its own cost, worth spending only where the budget is genuinely under pressure.

## Two failures with the same symptom and different causes

"The session got worse" describes two different things happening inside the window, and treating them as one problem picks the wrong fix half the time.

**Bloat** is a volume problem. The window is carrying more tokens than it needs to: tool results that were read once and never pruned, an early exploration nobody compacted, documents injected and never removed once their answer was extracted. The fix is as direct as the failure: remove what is no longer needed, on whichever of the first three instruments fits what is being removed.

**Drift** is a different kind of failure, and it can happen in a window that is nowhere near full. Drift is the window quietly ceasing to describe the actual task: the standing instructions have scrolled far enough back, relative to the newer turns, that they carry less weight in what Claude attends to; a decision made at turn twelve is still technically present at turn seventy but no longer functionally visible against everything piled on top of it. A session can drift while comfortably under its token limit, and a session can be bloated while still faithfully, if wastefully, describing the task. Confusing the two means pruning a session that was never too big, when what it actually needed was compaction written to explicitly re-state the standing decisions the later turns have buried.

## Deciding which instrument earns its cost

The choice follows directly from what is actually wrong. A path that turned out to be a dead end calls for pruning: nothing about it needs preserving, condensed or otherwise. A path that produced state worth keeping, in a session too long to keep carrying in full, calls for compaction, written to protect the specific facts later turns will depend on. A session with nothing left to reuse calls for clearing, with anything durable written somewhere outside the session first. A self-contained sub-task that would otherwise clutter the main line of work with exploration nobody needs to see again calls for a handoff to its own window.

A session that has drifted, rather than merely grown, needs compaction aimed specifically at the decisions and facts that have scrolled out of effective reach. A rewind would discard work still needed for the task ahead. A clear would discard everything indiscriminately, including the parts still doing useful work.

## Where the pack stops being the right picture

A hiker's pack holds physical objects that do not interact with each other. A context window holds tokens that the model reads as one continuous stream, so what is carried affects how much room is left and how the model behaves on every turn it is present for: a crowded window can degrade a decision even before it degrades the room available for the next one. This chapter treats the window as a volume to be managed. Which model is doing the managing, and what that model's own thinking or effort setting costs against the same window, is chapter 3's question. What a second window is called, once it has a name and a place in an agent's architecture rather than a mechanism derived from a fixed budget, is a later chapter's territory.

## The tell

A stem describing a session that degrades gradually over many turns, without a hard rejection or a truncated response, is asking about this chapter's instruments. A stem where the session still technically fits but the model's answers have stopped reflecting an earlier instruction or decision is asking specifically about drift, and the fix it wants is a targeted summary rather than a rewind.

## Self-test

**1. Select ONE.** An agent session has run for sixty turns. Total token count is well under the model's context window limit. Starting around turn forty, the agent stops following a formatting instruction given at turn three, though the instruction is technically still present in the transcript.

A. Prune the session back to turn three to restore the original instruction's visibility.
B. Compact the session with a summary that explicitly restates the turn-three instruction alongside anything since that depends on it.
C. Clear the session and start over, since the instruction has clearly been lost.
D. Do nothing, since the total token count is still within budget.

**Answer: B.** The window fits comfortably, so this is drift rather than bloat. The fix is a summary that puts the buried instruction back within effective reach. A rewind would discard forty turns of otherwise-useful work, a token-count check only detects volume problems and would miss this entirely, and clearing discards work still needed.

---

**2. Select ONE.** A session includes an unproductive fifteen-turn debugging detour that led nowhere before the correct fix was found on a fresh approach. The team wants that detour's tokens out of the window without touching anything before or after it.

A. Compaction, with a summary written to omit the detour.
B. Clearing the session entirely.
C. Pruning back to the point before the detour began, then continuing from there.
D. Handing the detour off to a second window after the fact.

**Answer: C.** Pruning rewinds to a specific point and drops what came after, which is exactly what removing a bounded, already-concluded detour calls for. A keeps the detour's tokens present until a summarization pass removes them, at greater cost than a direct rewind. B discards useful turns outside the detour as well. D applies to work still ahead; this detour is already finished.

---

**3. Select ONE.** A task requires exploring several unrelated code paths to find where a bug originates, a process expected to take many tool calls and produce a lot of intermediate, disposable output. The main session is mid-way through an unrelated feature and should not carry that exploration.

A. Prune the main session after the exploration finishes.
B. Hand the exploration to a second window scoped to just that task, and use only the answer it returns.
C. Clear the main session before starting the exploration.
D. Compact the main session preemptively to make room.

**Answer: B.** A self-contained, disposable exploration is exactly what a second, separately scoped window is for; the parent session never carries the intermediate steps at all. A and D both let the exploration's tokens enter the main session first. C discards the unrelated feature work already in progress, which the scenario does not call for.

---

**4. Select ONE.** Two sessions are compared. Session one is carrying twice the tokens of session two but is still answering every question correctly and referencing the standing instructions given at the start. Session two is well under its token limit but has stopped applying an instruction given early on.

A. Both sessions have the same problem, since both are long-running.
B. Session one is bloated but not drifted; session two is drifted but not bloated.
C. Session one is drifted; session two is bloated.
D. Neither session has a real problem, since neither has hit its context window limit.

**Answer: B.** Volume and functional accuracy are independent. Session one carries more tokens but still faithfully reflects its instructions, which is bloat without drift. Session two carries few tokens but has lost track of an instruction, which is drift without bloat. C reverses the definitions. A and D both collapse a distinction the scenario is built to test.
