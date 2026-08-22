# Chapter 5: Who is waiting?

## The rule the owner gives new staff before anything else

A restaurant owner trains new staff on one distinction before teaching them anything else: know who is standing there waiting, and know who is not. A table ordering à la carte is waiting, seated, watching for the kitchen door to swing open. A counter-service customer is waiting too, but standing where they can watch the order get built rather than sitting until a finished plate arrives. Delivery is not waiting in the same way. The customer has gone back to their desk, and the kitchen fires the ticket the moment it lands, on the same footing as any other order. A catering order booked a week out is not waiting at all. The kitchen chooses which slow Tuesday afternoon to prep it, and charges less for the privilege of choosing.

The owner never says a word about software. The same distinction sorts every request your code will ever send to the Messages API, and it decides which of five request shapes that call should take.

## The four ways this kitchen takes an order, and the one it doesn't

Five patterns cover every way your code can get an answer back out of the Messages API: call it and wait for the whole thing, call it and watch the answer arrive in pieces, call it without blocking your own thread while it runs, hand it a pile of work to complete on its own schedule, or keep a channel open in both directions for as long as the conversation lasts. Four of those five have a service mode in this kitchen already. The fifth doesn't, and the absence is worth understanding too. None of the five is a style choice: each one changes what your code has to do to use the answer, and three of them change what you pay for it.

### À la carte: nothing leaves the kitchen until the plate is finished

At the table, the kitchen is out of sight, and the dish arrives only once it is completely done, with nothing partial reaching you in between. This is the synchronous request: your code sends it and blocks until the complete response comes back in one piece. It is the right default whenever a single caller needs the finished answer and either the wait is short or nobody is watching it happen: a backend job, a short classification call, anything where the finished answer is all that matters. The characteristic misuse is calling it over and over inside a loop and treating the loop as a substitute for volume handling. Each call still blocks, still ties up whatever issued it, and still counts as one request against the same rate limit as every other call. A hundred synchronous calls in a row are a hundred synchronous calls, however you group them on your side before sending them. Two identical calls cost the same whether one is the only request of the day or the ten-thousandth sent in a tight loop; the shape itself carries no volume discount.

### Counter service: you watch the order get built

At the counter, you are still standing there, still waiting, this time in full view of the kitchen. You watch the sandwich get built ingredient by ingredient, and the wait feels shorter even though the kitchen is doing the same work at the same speed. This is streaming: Claude sends the response in pieces as it generates them, over the same connection, and your code reassembles the pieces into the finished message. A response that starts arriving within 300 milliseconds feels faster than the same content delivered whole after two seconds, even though the kitchen spent the same two seconds cooking either way. That is worth the added complexity when a live caller is watching the output arrive, a chat interface being the obvious case, and worth nothing at all when nobody is watching it arrive. Assembling a stream correctly, and recovering when it breaks partway through, is its own discipline with its own failure modes; this chapter only tells you when to reach for the shape.

### Delivery: the order still starts now, you just are not standing there

Order delivery, and the kitchen fires the ticket the instant it arrives, exactly as it would for a table. What's different is what you do with yourself while it cooks. You go back to your desk instead of standing there blocked, watching the kitchen, and something notifies you once the order is ready. This is what async/await buys a program that calls Claude: a client that does not block the thread that issued the request. The call still runs in real time, at the same priority as any other request. Only the calling code's own behaviour changes, freed to do other work until the response lands rather than sitting idle. This is not tied to one language either: any client library that exposes a non-blocking call, awaited rather than blocked on, gives you the same trade. Reach for it when a server is handling many callers at once and cannot afford to freeze a thread for every request in flight. The characteristic misuse is treating it as a cost lever. Freeing a thread and lowering a bill are different problems, solved by different mechanisms, and the fix for one does nothing for the other.

### The catering order: renting out the kitchen's slow afternoon

A catering order placed a week ahead never has anyone standing at the counter for it, and the kitchen does not start it the moment it lands. It starts whenever the kitchen has a stretch of unclaimed capacity, and it charges less because the customer accepted that arrangement. This is the Message Batches API. You submit a large set of requests in one call, and results come back once the whole batch completes, sometimes in minutes and sometimes taking most of a day. The per-token price is lower than the same calls made one at a time. The lower price buys the provider permission to run your work whenever its own capacity allows, rather than the instant your request lands, and that permission is only worth granting when nobody is standing at the counter for any single result in the set. The characteristic misuse is granting it and then treating the result as if it had been ordered à la carte: building a user-facing flow around a batch call, and discovering that a live person is now standing at the counter waiting on a result that was designed to arrive whenever the kitchen got round to it.

### The line this kitchen never offers

None of the four modes above keeps a channel open in both directions the whole time, where the kitchen can speak to the table unprompted and the table can speak back without placing a new order. That fifth mode is what a websocket is: a single connection, held open, over which either side can send at any moment without waiting for the other to ask first. Real systems reach for one when both ends genuinely need to originate messages unpredictably; a live multiplayer session is the clearest case.

Claude's Messages API does not expose one. Every request still begins with your code, the same as every order in this kitchen begins with the customer. The one-directional need, pushing a growing answer to a caller who is already waiting, is fully met by streaming over an ordinary connection: Claude sends the response as a sequence of server-sent events on the same HTTP connection used for the request itself. A websocket would buy two-way traffic that nothing in this relationship uses. Building one to consume Claude's output means operating a second kind of connection for a job the first one already does, complete with its own reconnection and keep-alive handling, machinery the request-per-message pattern never needs since a dropped connection is just a request you send again.

## One question, settled before you write a line of code

Everything above turns on one thing: whether anyone is waiting for this specific answer right now, and if so, what they need while they wait.

Nobody is waiting: hand the work to the Message Batches API and collect it on the provider's schedule. Somebody is waiting but does not need to be blocked personally while the request is in flight: call through a non-blocking client and let async/await free the thread until the response lands. Somebody is waiting and is blocked, wanting only the finished answer: call synchronously. Somebody is waiting, is blocked, and a growing answer serves them better than silence: stream it.

That produces the realtime-versus-batch tradeoff as a consequence rather than a rule to memorise. Streaming spends effort making a response feel faster to someone in the loop. Batching spends nothing on feel and instead lowers what the same work costs, because nobody is in the loop to feel anything. A single request cannot be both at once, because whether a caller is waiting is a fact about the request, fixed before you choose a lever. Given a case this chapter never showed you, the check is the same. No live consumer, and a schedule the provider controls is tolerable: the trade is available and worth taking. Anyone or anything blocked on the specific answer, anywhere in the flow: the trade is off the table, regardless of how much money it would save.

Take a fraud-review queue that scores overnight transactions and a live support chat, both sitting on the same model. Nobody reads a fraud score until the morning shift logs on, so that queue is a batch job regardless of how interesting the model's reasoning is. Someone reads every word of the chat reply as it lands, so it is synchronous or streamed regardless of how simple the question was. The task's difficulty never entered into either decision.

The asynchronous-programming half of this earns its own line, because the word gets reused for something else. Anthropic's own materials describe the Batch API itself as asynchronous processing, and in one sense that is fair: nothing blocks while a batch runs. But async/await, as a client-side pattern, is doing a different job. It frees a thread while a request that is still running in real time completes. Batch defers when the request even begins. A server using async/await to handle many live users at once buys concurrency. The discount that makes batch cheaper never enters into it: the request underneath is still running in real time, at the same priority and the same price, whether or not the calling code chose to block on it. The shared word "asynchronous" is the only thing the two mechanisms share.

## A rate limit that three nights of chunking never touched

A nightly classification job kept hitting rate-limit errors at the same point, three nights running. The developer running it had already tried the obvious fix: split the input list into smaller chunks, on the reasoning that a smaller batch would be gentler on the API. The errors kept firing anyway.

A senior developer asked how the requests were actually being submitted. The answer was a loop, calling the synchronous endpoint once per item, just working through smaller groups than before. That is serial calls against the synchronous endpoint, wearing the vocabulary of batching. Splitting the list into chunks does not change what the API sees. It still sees one request per item, back to back, and the rate limit does not care how the items were grouped on your side before you sent them. Running those same per-item calls in parallel instead of one after another does not change the underlying fact either. It is still one request per item against the synchronous endpoint; only how soon the limit arrives moves.

The surface feature here is genuinely misleading. The job was processing input in batches, in the everyday sense of that word, and everyday usage is exactly what makes this trap easy to fall into. The mechanism cares only whether the request went to the synchronous endpoint or the batch endpoint, and chunking a loop never changes which endpoint the request hits. The fix was to submit the entire set as one Message Batches API call: up to 100,000 requests or 256 MB, whichever limit arrives first, returning a single batch_id that the application polls until the job reports done. The per-token cost dropped below the synchronous rate, and the rate limit stopped firing, because the application was no longer making thousands of individual requests. It was making one.

Three nights of failed runs meant three nights of a job re-triggered, checked, and explained to whoever needed the output by morning, all because the fix that looked obvious, splitting the list into smaller pieces, never touched the actual cause.

One detail catches people on the way out of this fix: batch results do not return in submission order, so match them back to their inputs using the custom_id set on each request going in.

## What's on a different menu

Consuming a stream without corrupting your conversation history is its own discipline: assembling delta events into complete blocks, committing a turn only once the stream actually closes, and recovering when a connection drops partway through. Get any piece of that wrong and a dropped connection can corrupt the very history the next request depends on. None of that is decided by the question this chapter answers. Once "stream it" is the right call, chapter 12 owns everything that happens next.

What the batch discount is actually worth in your own numbers, and how it compounds with prompt caching on a job that reuses the same context across many requests, belongs to chapter 9. This chapter only tells you that the discount exists and what you are trading for it.

Which model answers the request is a separate dial from how the request is shaped. A batch job can run against any model tier, same as a synchronous one, and chapter 3 is where you decide which tier earns its keep for a given task. Sending images or PDFs alongside any of these five shapes adds its own budget question on top, and that question belongs to chapter 25.

Underneath all five shapes sits the same REST API that chapter 4 already laid out. What differs is timing, and for one shape, the form the response itself takes: streaming returns a sequence of events, not one finished body.

## Words the stem uses instead of a stopwatch

A stem never says "use batch." It says "overnight," "nightly," "no user is waiting," "runs on a schedule," or states a volume in the thousands against a deadline measured in hours. It signals synchronous with a single document or a single lookup, or with "the answer is needed right away." It signals streaming with "should appear as it's generated" or "watch the reply build." It signals async/await with "must not block the request thread" while a live caller still waits on the other end. And on the rare stem that mentions a persistent, two-way connection to Claude itself, read it as the wrong-shape distractor: that connection does not exist.

## Self-test

**1. Select ONE.** A compliance team has 40,000 scanned intake forms that must be classified against a fixed taxonomy by Monday morning. Nobody reviews an individual result as it completes; the whole set is loaded into a dashboard once every form is done. The team is watching cost closely this quarter.

A. Submit the whole set as a single Message Batches API call and collect the results once it completes.
B. Fan out parallel synchronous calls across many worker threads to finish faster.
C. Keep the synchronous call, but lower max_tokens on each request to cut cost.
D. Route the job to a smaller model to cut cost per call.

**Answer: A.** Nobody is waiting on any individual result, so the batch discount is available at no latency cost to anyone. B still makes one synchronous call per document at the synchronous rate, and risks the same rate limits at this volume. C and D change what gets sent or which model answers; neither one changes who is waiting, which is the constraint the scenario actually states.

---

**2. Select ONE.** A web application calls Claude to answer a live user's question inline in a chat window. The engineering team is worried that holding a connection open per request will exhaust the server's thread pool under load. The user still expects a reply within a couple of seconds.

A. Move the call to the Message Batches API so the request does not tie up a thread.
B. Call Claude through a non-blocking client so the thread is freed while the request is in flight, and pick up the result when it returns.
C. Reduce max_tokens so each response completes faster.
D. Switch to a smaller model so each response completes faster.

**Answer: B.** The user is waiting live, which rules out batch regardless of the thread-pool concern; batch would trade away the couple of seconds the scenario requires. Async/await solves the concurrency problem without changing that the request runs in real time. C and D address latency; neither touches the thread-exhaustion problem the scenario actually states.

---

**3. Select ONE.** A team is building a live chat interface and wants Claude's answer to appear progressively as it is generated, the same way a human would see someone typing. One engineer proposes opening a websocket connection to Claude so the server can push tokens to the browser as they are produced.

A. Open a websocket connection directly to Claude and consume the push stream.
B. Use the Messages API's streaming mode over the standard connection and forward the events to the browser.
C. Poll the Messages API every few hundred milliseconds for the latest partial output.
D. Submit the request to the Message Batches API and display the result once it completes.

**Answer: B.** Claude's API does not expose a websocket. The one-directional need, pushing a growing answer to a client that is already waiting, is exactly what streaming over the standard connection provides. A names a shape Claude does not offer. C recreates streaming badly with a polling loop, and D removes the progressive-appearance requirement entirely.

---

**4. Select ONE.** A nightly job classifying 60,000 records has hit rate-limit errors for three nights running. The team already split the input list into smaller chunks and loops over each chunk, calling the synchronous endpoint once per record. The errors keep firing at the same point every run.

A. Split the input into even smaller chunks so each loop finishes faster.
B. Add retry-with-backoff around each synchronous call to absorb the rate-limit errors.
C. Submit the records as a single Message Batches API call instead of looping over the synchronous endpoint.
D. Request a rate-limit increase for the account.

**Answer: C.** Chunking a loop over the synchronous endpoint still sends one request per record, so smaller chunks in A do not change what the API sees. B absorbs the symptom without removing the cause, and D raises a ceiling while leaving the workload paying synchronous rates and serializing thousands of calls. C changes the submission model itself, which is what the workload needed.

---

**5. Select TWO.** Which two statements are true of the Message Batches API only?

A. Results can take substantially longer to return than a synchronous call, up to a day.
B. It frees your application thread from blocking while the request is in flight.
C. It costs less per token than the same call made synchronously.
D. It delivers the first tokens of the answer before the rest has finished generating.

**Answer: A and C.** These are the batch trade: a provider-controlled schedule in exchange for a lower unit cost. B describes async/await, which still runs in real time rather than on a schedule. D describes streaming, which changes when output becomes visible rather than its cost or completion time.
