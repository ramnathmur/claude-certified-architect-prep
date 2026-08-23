# Chapter 10: The loop your code owns

## The surgeon never touches the tray

A surgeon says a word, "scalpel," and a hand appears holding one. Checking the instrument tray, knowing which blade is sterilized and ready, handing the used one back for cleaning: all of that is the scrub nurse's job, running the whole time, unremarked on, in a different part of the room, while the surgeon only ever names what comes next.

A team building its first tool-integrated agent often assumes the surgeon does both jobs, that once Claude "calls a tool," Claude has, in some sense, run it. Claude's actual part is narrower: it reads the tools your application registered, decides one fits the current step, and tells your application what to call and with what inputs. Whether that call happens at all, and what comes back from it, is entirely your code's responsibility, start to finish.

## One tool call, followed end to end

Trace a single request through the whole loop.

**You define a schema.** A tool has a name, a description, and an input schema stated in JSON Schema. This is what Claude reads to decide whether and when the tool fits.

**You send a message.** The request includes the tools you registered alongside the conversation so far. Nothing about sending it differs from a request with no tools at all, except that the tools are now visible to the model as options.

**Claude returns a `tool_use` block.** If a registered tool fits what the conversation needs next, the response carries a block naming which tool, a unique ID for this specific call, and the input arguments Claude wants passed to it. This is Claude's entire contribution to the loop: a named request, nothing executed.

**Your code executes the tool.** Your application reads the tool name and arguments out of the block, calls the corresponding function, and captures whatever it returns, including any error. The API plays no part in that dispatch; your code carries it out on every call.

**Your code returns the result.** A `tool_result` block goes back in the next turn, carrying the same ID as the `tool_use` block it answers and the content your function produced.

**Claude continues.** With the result now visible, Claude produces its next turn, which might be a final answer or another tool call.

Two more block types appear alongside these two. A **text block** carries Claude's own prose, and it can appear in the same turn as a `tool_use` block, a short comment sitting beside the call rather than replacing it. A **thinking block** carries Claude's internal reasoning and appears only when extended thinking is enabled.

The whole conversation is built from these blocks, and one invariant governs all of it: every `tool_use` block in an assistant turn must be answered by a `tool_result` block carrying the same ID, in the user turn that immediately follows. Miss the pairing, put the result in the wrong turn, or send the wrong ID, and the request fails validation before Claude sees any of it. No prompt wording changes this outcome. Your code either produces the correct sequence on every single request, or the request fails.

Reading the `tool_use` block, dispatching to the right function, and packaging what comes back into a `tool_result` is the harness's actual job, standing in for the scrub nurse. Naming it that way, rather than leaving it as an unlabelled part of "the loop," is what makes the boundary in the next section visible instead of assumed.

## The rule the two roles enforce

Claude owns exactly one decision inside this loop: which tool fits, and with what arguments. Your code owns everything physical: running the tool, handling its failure, returning its result in the shape the API requires. The boundary between those two ownership claims is precisely the `tool_use`/`tool_result` seam: the one place a request can be syntactically perfect and still wrong, a matched ID with the wrong content, a result silently dropped, a turn appended out of order.

## The turn that looked safe to trim

A team's early implementation appends only the `tool_use` block to conversation history when Claude returns a turn containing both a short text comment and a tool call, reasoning that the comment was incidental and only the call matters for continuing the loop. Later turns start behaving oddly: Claude asks about something it appeared to already have addressed, or repeats a caveat it seemingly already stated.

Claude's response, in that turn, was the full content array: the comment and the call together, as one thing Claude actually said. Discarding the comment while keeping the call deletes part of what happened, then asks Claude to reason as though it hadn't. Every follow-up turn depends on the history being a true record, and the fix is appending the entire content array exactly as returned, every time. No part of an assistant turn is safe to discard on the assumption that only the tool call was doing anything.

## What this chapter has not decided

Everything above assumes a tool worth calling was already registered and that Claude reached for the right one. Which tool that should be, how many to register, and how to word a tool's `description` field so the right one gets picked on a crowded board of options is a different problem, with its own failure modes, and it is the next chapter's subject entirely.

## The tell

A stem describing a validation error tied to a missing or mismatched result, a turn appended out of order, or content silently dropped from a turn is asking about this chapter's loop and its pairing invariant. A stem asking why Claude picked one tool over another belongs to the next chapter.

## Self-test

**1. Select ONE.** An assistant turn contains a `tool_use` block. The application's code executes the corresponding function and discards the returned error message rather than sending anything back, because the call "technically" failed and there is nothing to report.

A. This is correct: a failed call has nothing useful to return.
B. The next request will fail validation, because the `tool_use` block has no matching `tool_result` in the following turn.
C. Claude will silently retry the same tool call on its own.
D. The conversation will continue normally, since Claude does not track individual tool calls.

**Answer: B.** Every `tool_use` block requires a matching `tool_result` in the immediately following turn regardless of whether the underlying call succeeded; an error result still has to be returned, typically flagged as such, rather than omitted. C and D both assume behavior the loop does not provide; Claude never acts on a call it was never given a result for.

---

**2. Select ONE.** An assistant turn contains a text block reading "Let me check that for you" followed by a `tool_use` block. The application appends only the `tool_use` block to history, judging the text as filler.

A. This is safe, since only tool calls affect what happens next.
B. This corrupts the history Claude relies on for later turns, because the full content array is what Claude actually produced.
C. This is required, since the API rejects text blocks paired with tool_use blocks.
D. This only matters if extended thinking is enabled.

**Answer: B.** The text and the tool call are both part of the same turn Claude produced, and dropping either one leaves later turns reasoning from an incomplete record. C describes a restriction that does not exist; text and tool_use blocks coexist in one turn freely. D applies a rule specific to thinking blocks where it does not belong.

---

**3. Select ONE.** A developer says: "Claude ran the database query and got the result back, then used it to answer the question." Which correction best states what actually happened?

A. This is accurate; Claude executed the query directly against the database.
B. Claude requested that a specific tool be called with specific arguments; the application executed the query and returned the result in a tool_result block, which Claude then used.
C. The API executed the query on Claude's behalf, transparently to the application.
D. Claude only appears to request tools; in practice the application always runs a fixed, predetermined sequence regardless of what Claude names.

**Answer: B.** Claude's role ends at naming the tool and its arguments; execution and returning the result are entirely the application's responsibility. A and C both assign execution to Claude or the API rather than the application's own code. D denies that Claude's choice of tool and arguments has any effect, which contradicts the loop's actual mechanism.

---

**4. Select ONE.** A single assistant turn contains two `tool_use` blocks with different IDs, because the two calls do not depend on each other's results. Which statement about the following turn is correct?

A. The user turn that follows only needs one `tool_result` block, since both calls came from the same turn.
B. The user turn that follows needs two `tool_result` blocks, each carrying the ID matching its own `tool_use` block.
C. The two tool calls must be split across two separate follow-up turns.
D. Only the first `tool_use` block requires a `tool_result`; the second is optional.

**Answer: B.** Each `tool_use` block needs its own matching `tool_result`, identified by ID rather than by position, which is exactly what lets results arrive in any order when a single turn issues multiple independent calls. A halves a requirement that applies per block. C invents a restriction that does not apply to independent, parallel calls issued in one turn. D leaves one call permanently unanswered, which fails validation on the next request.
