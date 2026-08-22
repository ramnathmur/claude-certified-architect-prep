# Chapter 2: Why the same prompt answers twice differently

## Five calls, two wordings

A support-ticket triage endpoint reads an incoming ticket and returns a category with a reason. An engineer sends the same test ticket to it five times in a row before release, nothing else running against the system between calls. Four replies read close to: "This is a billing issue: the customer was charged twice for the same order." The fifth reads: "The customer reports a duplicate charge, which places this under billing." Same ticket, same code, five minutes apart.

The engineer files a defect. An unchanged input returning changed output is what a bug looks like: a stale cache, a race condition, a load balancer sending the fifth call somewhere the first four never reached. One mechanism, working exactly as built, produced all five replies and produced the difference between them.

## Fifty forecasts from one atmosphere

National weather services run their forecast model several dozen times, back to back, for the same forecast date, using the same model each time: the same equations describing how pressure, temperature and moisture move through the atmosphere. What changes between runs is the starting point. Today's atmosphere can never be measured everywhere at once, so each run begins from a slightly different snapshot, nudged within the range the measurement gaps allow. Run the same physics forward from several dozen slightly different starting points and the result is several dozen different forecasts for Tuesday. Some agree closely. Some do not.

Claude generates a response through a comparable two-step process, run once for every position in the reply. First, it scores every token in its vocabulary, the same unit Chapter 1 measured the budget in, against the full window Chapter 1 measured: the system prompt, the conversation history, and every token this response has already produced. Those scores become a probability distribution, a weight attached to each candidate token, produced by the same trained network every time. Second, it draws one token from that distribution rather than always taking the highest-scoring candidate. The model then moves to the next position and scores again, now conditioning on a sequence that includes the token it just drew.

Two things stay fixed at each of these steps. The vocabulary being scored is the same finite set of candidate tokens every time, and the sequence the scores are conditioned on is the prompt plus every token generated in this response so far. What varies is which candidate the draw lands on. The distribution is over tokens: one small piece of text chosen at a time, weighted by how likely the network judges each candidate to be a good continuation of exactly this sequence. A high weight makes a candidate likely to be drawn. It does not make that candidate the only one the draw can land on.

The forecast ensemble and the model diverge on where the nudge sits. A weather ensemble branches at the start, from a handful of different snapshots, and each branch then runs forward from that one nudge through the same governing equations. Token generation branches at every position: dozens or hundreds of times inside one reply, with each draw becoming part of what the next draw is conditioned on. A response of two hundred tokens is two hundred of these score-and-draw steps, run one after another.

A setting called `temperature` changes how concentrated the distribution is at each of those steps. Pulled low, it sharpens the scores toward the highest-probability tokens, so the same candidate wins most of the time. Pushed higher, it flattens the scores, so a wider set of candidates has a real chance of being drawn. The vocabulary being scored stays the same size either way. Only the shape of the weights across it changes. Either setting runs the identical two-step process: score the vocabulary against everything generated so far, then draw.

Send the same prompt to Claude twice and two independent runs of that process start from the same place. Nothing requires the draw at position one, or position twelve, or position forty, to land on the same token both times. Two runs can diverge in wording while both are legitimate draws from the same distribution, the same way two ensemble members can describe Tuesday's rainfall differently while both are legitimate runs of the same forecast model.

## Fifty tracks, and no single correct one

Derive the rule from the two-step process directly. Each response is one sampled path through a space of continuations the model judged plausible, so two responses to an identical prompt are two independent draws from the same distribution. Whether a given draw is acceptable depends on whether it has the property the task actually needs: the right category, the required fact, a number inside the range that makes sense, valid structure. It does not depend on whether its exact wording matches some reference string, because the distribution was never a distribution over strings to match.

A forecast ensemble that returns several dozen slightly different tracks for Tuesday has run several dozen times and produced several dozen legitimate outputs. The correct read is the shape of all of them together against what actually needs to be true, rain or no rain, not any single track held up against a fixed reference track. Two wordings of "this is a billing issue" from one ticket are the same case: neither is the reference, and what matters is whether each one lands on the category the ticket actually belongs in.

That is the mechanism working as designed, not the system failing. The engineer's defect ticket named the symptom correctly and diagnosed the cause wrong: nothing raced and nothing went stale. The two replies disagree in wording for the same reason two ensemble members disagree on Tuesday's rainfall total.

## The day the ensemble splits in two

Not every ensemble run agrees closely. Some forecast dates split the members into two distinct groups: half send a storm out to sea, half bring it ashore two hundred miles apart. Read from outside, a two-cluster result looks worse than a tight one, as if the model had failed on half its runs. Read against the mechanism, the split is information: it means today's atmosphere sits at a genuine branch point, close enough to a threshold that a small difference in the starting snapshot decides which side the storm lands on. A single run could never report that. Several dozen runs, spread into two clusters, do.

The triage endpoint has the same kind of day. Feed it a ticket that mentions both a duplicate charge and a failed login, and repeated calls stop varying only in wording. The category itself starts to flip, BILLING on some calls, ESCALATION on others. Read from outside, that looks like a worse bug than four slightly different sentences about the same category, evidence of something more broken underneath. Read against the mechanism, it is the identical process as the wording case: at the token position where the category gets decided, the distribution split its probability close to evenly between two candidates instead of favouring one heavily, so the draw lands on one side about as often as the other. The size of the difference between two replies, a synonym traded for another synonym against a whole category changing, reads out how peaked or how split the distribution was at the position that mattered. It says nothing about whether the mechanism itself changed between the two cases, because it did not. Both cases take the same fix already derived above: judge the reply by whether it has the property it needs, regardless of how far its wording drifted from another run.

## The dial some models do not have

Sampling controls exist at the API level on some models: `temperature`, `top_p`, and `top_k`, each reshaping the distribution before the draw. They are not universal. On the newest Claude models, setting a non-default value for any of the three is rejected outright, returned as a 400 error, and steering the output runs entirely through what the prompt asks for instead. Where the parameters are accepted, `temperature` set to zero makes output more repeatable. It does not make two calls identical: the guarantee the number seems to promise is a stronger claim than the API makes. Which models accept which parameters changes release to release, so a specific list is worth confirming against the API reference at build time rather than carried from memory.

No dial, on any current model, switches the draw off, and that is the edge of what configuration buys here. The consequence lands on testing: a feature built on the call has to be tested against whatever property a correct answer must carry, however the words land. Chapter 26 is where that becomes a build.

## Reading a stem for repeated calls

The words that flag this chapter compare across calls rather than describing one output alone: "the same prompt returns different wording," "results vary from run to run," "a test asserting exact text is flaky," "the response text changed between identical requests," "two calls, two different answers, both rated correct." Each names a change measured between two responses, which is where this mechanism shows up.

## Self-test

**1. Select ONE.** A unit test checks a summarization endpoint by comparing its output against one fixed reference string. The test passes most runs and fails roughly one run in five, and a human reviewer rates every failing output as correct. What is the most accurate diagnosis and fix?

A. The model is unreliable for this task; move the workload to a larger model.
B. Set `temperature` to 0 on every call so the endpoint returns identical text on every run.
C. The test asserts exact text against a task with more than one correct wording; rewrite it to check the property a correct summary must have, such as required facts being present.
D. Add retry logic that resubmits the request until the output matches the reference string exactly.

**Answer: C.** The failures are draws from the same distribution as the passes rather than a quality regression, so the fix belongs in what the test checks rather than in what the model runs. B does not deliver what it promises: `temperature` 0 makes output more repeatable, it does not make output identical, and current models are not required to accept the parameter at all. A spends more on a model that was never the problem, and D burns calls chasing a string match the task's own correctness never depended on.

---

**2. Select ONE.** A colleague says Claude keeps a large set of complete responses from training and, for any new prompt, retrieves and returns the closest match verbatim. Which statement corrects this?

A. Correct: Claude retrieves the nearest stored response and returns it unchanged.
B. Claude generates the entire reply in one step, then edits it for fluency before sending it.
C. At every position in the reply, Claude scores its vocabulary of candidate tokens against the prompt and everything generated so far, and draws one token from that distribution; the reply is built one draw at a time, never retrieved whole.
D. Claude only scores and draws tokens when a non-default `temperature` is set; otherwise it returns one fixed, precomputed reply.

**Answer: C.** Generation is a sequence of scored draws, each conditioned on the full sequence so far, and that is true on every call regardless of any sampling parameter. A and B both describe a single retrieval or single-shot step that does not exist. D ties the scoring-and-drawing step to one parameter, but the two-step process runs on every call, including the ones where `temperature` is left at its default.

---

**3. Select TWO.** A dashboard shows a Claude-backed endpoint returning different exact response text on back-to-back calls with the same input, while downstream consumers report every answer as usable. Which two statements are accurate?

A. The variation is expected: generation draws from a probability distribution at each token position, so wording can differ across calls without either output being wrong.
B. The deployment should be rolled back until the difference in output text is eliminated.
C. A test that checks this endpoint for exact string equality will register failures unrelated to any regression in the feature itself.
D. The variation confirms that a sampling parameter was left unset and must be pinned to a fixed value before the endpoint can be trusted.
E. The variation will stop once the conversation history grows large enough to fill the context window.

**Answer: A and C.** Wording variance with no change in usability is the sampling mechanism operating normally, and an exact-text test cannot tell that apart from a real regression, which is why it needs to check a property instead. B reaches for a bigger fix than the evidence supports. D assumes a parameter guarantees identical output, which no current model promises even when the parameter is accepted. E reaches for context-window pressure, a different mechanism with no support in what the dashboard shows.

---

**4. Select ONE.** A developer wants a Claude call to return byte-identical output on every run with the same input, and plans to set `temperature` to 0 and pin `top_p` to a fixed value to guarantee it. What is the most accurate assessment of this plan?

A. It works as planned on every current model: `temperature` 0 with a fixed `top_p` guarantees identical output across calls.
B. Sampling parameters do not guarantee determinism, and the newest Claude models reject non-default values for `temperature`, `top_p`, and `top_k` outright; where the parameters are accepted, `temperature` 0 only makes output more repeatable.
C. Determinism is achieved by disabling streaming, which forces the full response to be computed before any token is sampled.
D. Determinism follows automatically once `max_tokens` is set low enough that only one continuation is plausible.

**Answer: B.** No current parameter combination is documented to guarantee identical output, and the newest models do not accept these parameters at all. C invokes a real API setting that has no bearing on sampling. D assumes a short response has only one plausible continuation, which the draw does not require.
