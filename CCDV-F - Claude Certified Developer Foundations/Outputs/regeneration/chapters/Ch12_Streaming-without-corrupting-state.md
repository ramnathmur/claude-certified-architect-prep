# Chapter 12 · Streaming without corrupting state

## The handler that couldn't tell an ending from a completion

A team building an operator-facing agent added streaming so staff could watch each response arrive instead of staring at a blank screen while the model worked. The handler was simple: listen for events, accumulate them, and once the loop reading the stream exits, save the assembled turn to conversation history. In testing, on a fast local connection, the loop only ever exited one way. The stream ran to completion every time.

In production, a connection dropped partway through a response. The read loop ended exactly the way it always had. The handler saved the turn, because nothing in its code distinguished one kind of ending from the other. Conversation history now held an assistant turn with a truncated tool call inside it. The corrupted turn sat there quietly. The failure showed up one request later, when the API validated the next turn and rejected it.

## What arrives while a message is still open

Streaming exists for one reason: it lets an application start showing output before the model has finished generating all of it, which is what the team above built it for. In exchange, streaming sends a response as a sequence of small events instead of one finished object. Nothing on the other end holds a message open for you to poll or inspect. Each event describes a single change: a block opening, a fragment of content or input being added to it, a block closing, and eventually the whole message closing. Your handler applies each event to the partial state it's building, one piece at a time.

A live radio broadcast works the same way, and it's worth sitting with the comparison, because the failure above is exactly the mistake it rules out. A song on the radio arrives as continuous sound, in real time, from a transmitter with no obligation to keep playing. If the signal drops, a tunnel, interference, whatever the cause, what you're left holding is a fragment. The only way to know the song is genuinely finished is to hear the outro, or the announcer naming the next track. Silence by itself doesn't tell you which happened, a clean ending or a dropped signal.

A recorded track you already hold in full works differently. The whole recording exists before playback starts, so there's only one way for the audio to stop: you reached the end. A non-streamed API call avoids this gap entirely. The API holds the response until every block is finished, then hands it to you complete, so there's no moment where the response having arrived and the response being whole could come apart.

A tool_use block announces its name and id the moment it opens. Its input arrives afterward, fragment by fragment, as a JSON string that only becomes valid once the block's own closing event fires. The tool being called and the arguments it's being called with become known at two different moments, and only the second one requires waiting.

## The one event that means whole

The gap the radio makes audible is the same kind of gap that sits inside a stream. A block's accumulated input isn't safe to parse until the specific event marking that block finished, content_block_stop, arrives for it. The message as a whole isn't safe to treat as finished until its own closing event, message_stop, arrives. Neither is optional. A block can open, receive fragments for a while, and pause, without any of that counting as a signal either way.

Streaming divides the work between two sides, and each side has exactly one job. The stream's job is to fire message_stop when, and only when, the message is whole. Your handler's job is to treat everything before that event as provisional: readable for display, but unsafe to act on and unsafe to commit anywhere durable. The postmortem's handler broke its side of that arrangement. It treated the read loop exiting, a fact about the connection, as though it were equivalent to message_stop arriving, a fact about the message. A stream ending is not a message completing, and the gap between those two events is exactly where that production incident lived.

Not every partial block carries the same weight of risk. A partial text block that reaches the screen before a connection drops is a cosmetic problem: the user sees a sentence cut off mid-word, and a retry produces a clean one. A partial tool_use block is different in kind: its JSON is either complete or it's unusable, and a stream that stops between the two leaves nothing usable behind. If one reaches conversation history, every later request built on that history inherits the problem.

When a stream runs to completion without interruption, assembling its events gives you back every block a non-streamed call would have returned, fully formed. Streaming changes how many pieces the response arrives in, and how much responsibility your handler carries for knowing when the last piece has arrived.

## Why the rule has to be this strict

The rule follows from where an interruption actually happens. A dropped connection is a transport-layer event. It has no obligation to announce itself to your application in any particular way, and it can occur between any two events in the sequence, including between a block's last fragment and that block's own content_block_stop. Once that's true, a stopped event loop stops being evidence of anything on its own. A completed stream and an interrupted one look no different from each other at the moment the events stop arriving: nothing more comes in, either way. The only fact that tells them apart is whether message_stop was among the events that did arrive before they stopped.

That leaves one workable policy, applied at two levels. At the block level: don't parse or run a tool_use block's input until content_block_stop closes that specific block. At the message level: don't commit a turn to history until message_stop closes the message. Anything short of those two events stays provisional, and there's no partial credit available for what's accumulated so far. A tool_use block cut off mid-argument can't be completed by guessing the rest, because the model was still generating when the connection dropped, and nothing on your handler's side knows what it would have said next. On any other kind of stream ending, discard whatever accumulated, and retry the request from the last turn that did reach message_stop.

## The schema bug that was never a schema bug

Return to the postmortem. The validation error appeared on the retry request, and it named a malformed tool_use block inside that request's history. Read from the error message alone, this looks like an ordinary schema bug: a mismatched id, a missing required field, a tool description that invited the wrong call. An engineer debugging it reasonably starts where the error points, at the retry request and the schema the API is validating it against.

That reading loses. The retry request's tools were defined the way they had always been defined, and the id on the malformed block matched a real, correctly issued tool_use from the assistant. What made the block invalid was its content: a JSON string cut off mid-object, because the stream that produced it dropped before content_block_stop ever fired for it, and the handler saved the turn anyway. The defect sits one turn earlier than the error, inside a stream that had already ended by the time anyone went looking at a schema.

The postmortem team spent an afternoon on the schema and the retry logic before finding this. The mechanism gives a shortcut for next time: when a tool-use validation error shows up on a retry, check first whether the turn immediately before it was assembled from a stream, and whether that stream reached message_stop. Look at the schema only once that's ruled out.

## Where this rule stops

This chapter's rule governs one decision: when a streamed turn is safe to treat as finished. The choice to stream at all, instead of making a single blocking call, belongs to the chapter on request shapes, and this chapter takes that choice as already made. A validation error that turns out to be genuinely about the schema, a wrong type, a missing field, once a stream is ruled out as the cause, is a tool-design problem covered elsewhere. How many times a failed request gets retried, and with what backoff, is a separate policy decided after this one. What belongs here is narrower and comes first: confirming the turn in front of you is actually whole before you act on it or save it.

## The words that flag it

A stem naming this chapter pairs a stream with a failure that surfaces on a later turn than the one that caused it, most often a tool-use or validation error following a turn built from streamed output. "Dropped connection," "interrupted stream," and "read loop" sitting next to a validation error one request downstream mean the same thing: check message_stop before touching the schema.

## Self-test

**1.** An agent streams responses and appends the assistant turn to history as soon as the loop reading the stream exits. In production, a request occasionally fails with a tool-use validation error on the turn after an ordinary user message, even though the tool's schema hasn't changed. Select the one change that fixes the actual defect. *(Select one.)*

A. Add a required array to the tool's input_schema so the model cannot omit an argument.
B. Switch every call this agent makes from streaming to a single blocking request.
C. Add an instruction to the system prompt telling the model to finish its tool call before a connection can drop.
D. Append the assistant turn to history only after message_stop has been received; on any earlier exit, discard the turn and retry.

**2.** A handler is accumulating content_block_delta events for a tool_use block. Select the one true statement about when the accumulated input is safe to parse as JSON. *(Select one.)*

A. As soon as the block's type and id are known, since those are set when the block opens and never change.
B. Once the handler has gone three seconds without receiving a new delta for that block.
C. Only once content_block_stop has fired for that block's index.
D. Never while streaming; disable streaming for any tool that takes structured input.

**3.** A stream is interrupted by a dropped connection after two content blocks have already closed cleanly and a third is still open. Select the one correct next step. *(Select one.)*

A. Keep the two closed blocks, discard the third, and append the assistant turn to history with just the two complete blocks.
B. Discard the entire partial turn, and retry the request from the last turn that reached message_stop.
C. In the next request, ask the model to acknowledge that its previous turn was cut off.
D. Wrap the whole agent loop in a general retry-with-backoff policy, independent of where in the turn the drop happened.

**4.** A tool-use validation error appears on a request, and the immediately preceding assistant turn was produced by a streamed call. Select the two checks to run before touching the tool's schema. *(Select two.)*

A. Confirm whether that preceding turn was committed after message_stop, or committed simply because the read loop exited.
B. Check whether that preceding turn contains a tool_use block with truncated or non-JSON input.
C. Rewrite the tool's description field to add an exclusion condition.
D. Increase max_tokens so the model has more room to finish its response.
E. Wrap the whole agent loop in a broad try/except so any error is silently retried.

**Answers**

1. **D.** A and C don't touch the mechanism: the schema was never wrong, and no prompt instruction can prevent a network interruption. B removes streaming's benefit entirely to fix a defect that has nothing to do with streaming itself, only with when a turn gets committed.
2. **C.** A confuses knowing the tool with knowing its arguments. B substitutes a timer for the actual signal; deltas can legitimately pause without the block being done. D discards streaming for a whole category of tools over a timing issue with one fix.
3. **B.** A keeps output that was never confirmed as the model's complete turn, on the theory that partial credit is better than none. C can't repair state that's already corrupted. D is a real, useful pattern for a different problem, and doesn't address why the corrupted turn got saved in the first place.
4. **A and B.** C solves chapter 11's bug, the wrong tool getting selected. Here the right tool was selected; its block is just malformed. D doesn't address a connection dropping mid-stream. E hides the error instead of finding it, and risks retrying into the same corrupted turn repeatedly.

## Lookup only

The event names below are for reference. The self-test above does not depend on any of them, and the exam is unlikely to test these exact strings.

| Event | What it marks |
|---|---|
| message_start | A new message beginning. An empty shell to start assembling blocks into. |
| content_block_start | A new content block opening, with its type and, for a tool call, its name and id. |
| content_block_delta | One incremental fragment of a block's text, input, or thinking content. |
| content_block_stop | The block at this index is complete. |
| message_delta | Top-level changes to the message as the response nears its end. |
| message_stop | The message is complete. |
