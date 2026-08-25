# Chapter 28: Failures You Can Wait Out, Failures You Cannot

## The retry that made it worse

A developer built a customer-facing feature that called the Anthropic API in a loop, once per item in a batch. Development traffic never came close to a rate limit, so the code shipped with no error handling. At the first real production traffic peak, the API returned a 429. The unhandled exception took down the whole request, and the feature looked simply broken.

The developer's first instinct was to add immediate retries in a tight loop. Each instant retry counted as another request against the same rate limit, deepening the exact shortage that had caused the failure. The fix that worked: classify the error as retriable, then back off — capped attempts, exponential delay, honoring the `retry-after` value the response carried.

Getting that classification right, before anything else, decides everything that follows.

## The one question that decides everything

The deciding question, asked before any other design choice: would waiting and trying the exact same request again plausibly work. A yes makes the failure retriable; a no makes it terminal, and no amount of waiting changes the outcome, since the cause sits inside the request itself.

On the Anthropic API, the status code usually names the bucket directly.

| | Retriable | Terminal |
|---|---|---|
| Triggers | 429 (rate limit), 529 (overloaded), 5xx server faults (500, 502, 503, 504) | 400 (bad request), 401 (auth failure), 403 (permissions) |
| Cause | Transient: momentary capacity, a dropped connection, a limit that clears with time | Structural: a malformed body, an expired key, a permission no retry can grant |
| Recovery | Exponential backoff with jitter, capped attempts, honor `retry-after` when present | Fix or reject the input; surface the error to the caller |
| After exhaustion | Raise a clean error, or fall back to a cached or simpler result | There was never a retry to exhaust |

A timeout is usually retriable, since the work may simply have taken longer than the client waited. A repeated timeout on the same expensive request is a different signal: fix the request instead of resending it. A 403 is terminal, since retrying grants no new permission. When the status code doesn't settle it, default to terminal and raise loudly. A failure wrongly called terminal fails loudly and gets fixed; a failure wrongly called retriable hammers the service and buries the real problem under a wall of retries.

Two more mechanisms decide where retry logic should live. The Anthropic client libraries already retry transient failures automatically, with progressive delays, up to a configurable attempt count. Check that first: two loops around the same call multiply attempts against the same limit instead of capping them. Either let the SDK own the transient cases and reserve custom code for application-specific fallbacks, or turn its retries down and own the whole path yourself. A 429 or 529 response often carries a `retry-after` value naming exactly how long to wait; treat it as authoritative when present, and fall back to exponential backoff only when absent.

Tool calls carry a third, distinct mechanism. When a tool call fails, the result returned to Claude must set `is_error` to true explicitly, never a silent empty result. A dropped error lets the model treat the empty result as valid data and reason confidently on top of information that was never there.

## Where surface signals lie

The classification test maps onto a courier delivering two packages marked "undelivered." One has an unreadable address label: the recipient still lives there, and delivery may succeed once the label is re-printed or clarified. The other's recipient has emigrated: no re-attempt, however many times repeated, will ever find them at that address, because the address itself is permanently wrong.

| Courier case | API concept |
|---|---|
| Unreadable label, recipient present | Rate limit, overload, transient server fault |
| Retry after clarification plausibly succeeds | Backoff and retry plausibly succeeds |
| Recipient has emigrated | Malformed request, expired key, denied permission |
| No retry ever finds them | No retry changes the outcome |
| Telling the two apart takes field investigation | The status code names the bucket directly |

That last row is where the analogy stops carrying. A courier separating a smudged-but-legible label from a genuinely vacated address does real investigative work in the field; the API skips most of that ambiguity, since the status code is a mechanical lookup a courier never gets.

Mechanical lookup still has one blind spot worth watching for. A refusal returns an ordinary 200: no error status, nothing a status-code classifier would flag. Its `stop_reason` field reads `"refusal"` in place of the model's usual output, so a status-only classifier sails past it as a success. The model made a content decision; repeating the request changes nothing about what it decided. A refusal belongs on the terminal side: raise it to the caller and log it, never retry it, even though it arrives wearing an ordinary success's 200.

## Why the fork is worth getting right

Every retry attempt spends two things: elapsed time and a slot against whatever attempt cap is set. Spend that slot on a terminal error and nothing comes back, since the identical request fails identically each time; five attempts just confirm what the first response already said. Spend it well and the budget stays available for a failure elsewhere in the same flow that genuinely could resolve with a moment's wait.

The cost runs in both directions. Classifying a 400 as retriable burns attempts and latency reconfirming a known fact. Classifying a 429 as terminal gives up on a request a brief backoff would have carried through, surfacing a failure patience would have avoided. Correct classification decides whether the retry budget lands on failures that can actually use it.

## Where this chapter's authority stops

This chapter classifies a failure once it has happened and picks its recovery strategy. Building the loop the failure occurs inside (registering tools, scoping a system prompt, defining an exit condition) belongs to chapter 17. Inside a hierarchy the same classify-then-route discipline runs independently at each subagent, but how many subagents to run is that chapter's decision. This chapter's job ends at the fork and the two recovery paths hanging off it.

## What the stem sounds like

A stem naming this chapter says "would likely succeed on a second attempt" or "returned a rate-limit response" for the retriable side, and "the same malformed request" or "an expired credential" for the terminal side. "The response came back 200 but the model declined" is terminal wearing a success's clothing. The tell is never the word "error" on its own; it's whether repeating the identical request could plausibly change what comes back.

## Self-test

**1.** A request returns a 529 during a traffic spike. *(Select one.)*

A. Treat it as terminal; the request itself is invalid.
B. Treat it as retriable; back off and honor `retry-after` if the response includes one.
C. Retry immediately in a tight loop to recover as fast as possible.
D. Treat it the same as a 400, since both come from the Anthropic API.

**2.** A response returns HTTP 200 with `stop_reason: "refusal"`. *(Select one.)*

A. Retry it; a 200 status means the request is safe to resend.
B. Treat it as retriable, since only 4xx and 5xx responses are terminal.
C. Raise it to the caller and log it; the model made a content decision, and retrying changes nothing about that.
D. Silently drop it and continue the loop, since no exception was raised.

**3.** Which two of the following describe correct handling of a failed tool call? *(Select two of four.)*

A. Return the result to Claude with `is_error` set to true.
B. Return an empty result so the model isn't distracted by error details.
C. Retry the tool only if the underlying cause is transient.
D. Always retry a tool error immediately, regardless of cause.

**4.** A team's code already uses the Anthropic SDK's default client, then adds its own exponential-backoff wrapper around every call, unaware the SDK retries transient failures on its own. *(Select one.)*

A. Safe; more retry logic can only help reliability.
B. Risky; both layers may retry the same failure independently, multiplying attempts against a rate limit.
C. Required, since the SDK never retries anything on its own.
D. Only matters for 4xx errors; 5xx errors are unaffected.

**Answers.** 1: B. 529 is Anthropic-side load and transient, so backoff and `retry-after` apply; A and D misclassify it as terminal, and C repeats the tight-loop mistake that deepened the original outage. 2: C. A refusal carries a content decision inside an ordinary 200; A, B, and D all treat a terminal case as if waiting might help. 3: A and C. The error must reach Claude explicitly, and a tool error is worth retrying only when the cause is transient; B hides the failure as valid data, and D retries even terminal tool failures. 4: B. The SDK already runs its own progressive retries, so an unaware second layer multiplies attempts against the same limit; A and C get the SDK's behavior backwards, and D wrongly limits the risk to one status family.
