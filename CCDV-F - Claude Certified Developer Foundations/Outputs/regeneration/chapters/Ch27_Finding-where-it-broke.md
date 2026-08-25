# Chapter 27: Finding Where It Broke

## Green all the way down, and a red run anyway

Every test written for a support-ticket agent passes. The parser has a unit test, and it is green. The model call has a functional test, and it is green. Wire the two together and run the full flow the way a user would, and it fails: asked about a refund window, the agent answers from a policy it invented instead of the one it retrieved. Nothing in the test suite predicted this, so there is no obvious place to start looking.

That gap has a specific cause: a seam that unit and functional tests are built to miss. A specific instrument exists to find it, a trace of the run, read one step at a time. A failure lives in exactly one of three places: the input assembled and sent, the output the model returned, or what the code did with that output afterward. Isolating which of the three, before touching a line of code, is this chapter's whole job.

## A plumber does not replace the whole system

When water shows up on a workshop floor, a plumber does not tear out every pipe in the building. They trace the run backward from where the water appeared, checking each joint in turn, until they find the exact point where a good supply of water became a leak. Everything before and after that joint stays untouched, because it was never where the fault was.

A multi-step Claude run behaves in a comparable way. Tracing it backward or forward through each step's input and output, retrieval into prompt, prompt into model call, model call into parser, is the same discipline as checking each joint in turn: find the step where a good input became a bad output, and stop there.

The analogy has one limit worth naming. A plumber can see or feel water directly at the leaking joint; the wet patch is evidence that exists whether or not anyone planned for it. A software trace has no equivalent of looking for the wet spot: if a step was never instrumented to record what it received and what it returned, there is nothing to check at that joint at all, and the gap has to be closed before the run happens rather than after.

## What each green light actually proves

A test only tells you what it was built to check. Four levels exist, and each is blind to everything above and below it.

Symptom: one function looks wrong on its own, a parser returns the wrong type, a formatter drops a field. A unit test isolates exactly one function and checks it with nothing else running. It tells you that piece behaves; it says nothing about whether the pieces around it agree on what to hand each other.

Symptom: a single Claude call looks wrong, the answer is malformed or missing an expected field. A functional test checks that one call returns the expected shape for a given input: the right fields, the right type, a response the calling code can parse. It validates the call on an input already known to be well-formed.

Symptom: everything passes alone, and the full run still fails. This is the symptom that opened the chapter, and it is where most silent production failures hide, because each side can pass its own test while the handoff between them is broken. An integration test exercises exactly that handoff, for instance a retrieval result passed into a model call.

Symptom: the failure only shows up running the whole thing, end to end, the way a user would. An end-to-end test catches this. It is the slowest of the four to run and the hardest to localize, because a failure at the end says the flow broke somewhere, not where.

None of the four levels says where inside a passing-then-failing run the break happened. That is what a trace is for.

## Reading a trace instead of guessing

A trace records each step of a run in order: the prompt sent, every tool call made, the intermediate output at each step, and the timing. A test tells you a failure exists. A trace tells you where it happened.

```
[trace run_id=8f21c]  case: "Where is my refund?"
  step 1  retrieve(query)        ok    42ms   -> 3 chunks
  step 2  build_prompt(chunks)   ok     1ms   -> prompt 1,240 tok
  step 3  model.call(prompt)     ok   980ms   -> answer "..."
  step 4  parse(answer)          FAIL   2ms   -> KeyError: amount
          final score: 0   (failure localized to step 4, the parser)
```

Before this trace existed, the failing eval said only that the case scored zero. After it, the trace says step four, the parser raised a KeyError on a field the model did not return. That is the difference between opening the parser's code directly and rereading the whole flow by hand.

Reading a trace works the same way whichever path assembled the input. A system that routes single-fact lookups to one fetch and multi-step questions to iterative search still produces one linear trace for whichever path a given request took.

## Sent, came back, or done with it

Every step in a trace does one of three things: assembles something to send, receives what came back, or acts on what it received. That maps directly onto the three places a failure can live, and it is worth deriving once so it can be applied without a diagram in front of you.

Take the refund case from the opening. The trace shows `retrieve()` returning a list of chunk dictionaries, `[{"content": "..."}, ...]`, and `build_prompt()` written to expect a plain string. The dictionaries went in raw. `model.call()` ran on that malformed prompt and returned a fluent answer, so step three shows `ok`. Reading only that line makes the fault look like the model reasoned badly. Reading the step before it moves the fault to what was sent: the context the model actually received was a list of dictionaries with no `.content` extracted, never the policy text at all.

That is the isolating move this chapter teaches: before treating a wrong-looking answer as a model-output problem, trace back one step and check whether the input the model received was the input that was intended. A unit test on the parser cannot catch this, because the parser was never in the path that failed. A functional test on the model call cannot catch it either, because the call performed correctly on the malformed input it was given. Only a test that drives `retrieve()` into `build_prompt()` with real data exercises the seam where the fault lives, the integration level from the taxonomy above.

## The fix that looks right and changes nothing

Two fixes look plausible before the trace is read, and both target a component that was never broken.

Adjusting the parser, `dateutil.parse` works, or the schema check passes, feels safe because it already has a passing unit test. That pass is exactly the proof the parser is clear; the case failed upstream of it, so this fix changes nothing about the run that failed.

Rewording the prompt is more tempting, because the answer looks like a language problem: fluent, plausible, and wrong. But the trace shows step three returning `ok`. The model executed correctly against the prompt it was handed, and what it was handed was the defect. Rewording the instructions inside a malformed prompt only asks the model to read the same garbage more carefully; it never touches the line where chunks were inserted without extracting `.content`.

The fix that closes the case aligns the handoff: extract the text from each retrieved chunk before it reaches the prompt, then add an integration test that drives `retrieve()` into `build_prompt()` on real data, so the mismatch fails loudly before a user sees it.

## Where isolation stops

Locating the break tells you which seam failed and why. It does not tell you what to do about it. Once a trace shows the retrieval-to-prompt handoff failed, there is still a decision about whether that class of failure is worth retrying, what a sensible backoff looks like if the retrieval call is flaky, and how the calling code should behave the next time the same shape of malformed chunk arrives. None of that is this chapter's job.

The plumber holds for this boundary too: tracing the pipe run to the leaking joint and deciding how to reseal it are different pieces of work, done with different tools. Deciding how to recover, retriable failures against terminal ones, backoff strategy, tool-error handling, belongs to the next chapter. This one ends at the trace line that says where and why.

## What gives it away in a stem

A stem naming this fork says the pieces "pass in isolation" or "each component works on its own" while the full run fails, or it hands you a trace directly and asks which step, or which test level, would have caught the break. The detail to isolate before picking an option is which step's output changed.

## Self-test

**1.** An order-lookup agent has a passing unit test on its response formatter and a passing functional test on its model call. The end-to-end test fails. The trace shows step 2, `assemble_context(chunks)`, inserting each chunk's raw dictionary into the prompt instead of its `content` field. *(Select one.)*

A. Rewrite the formatter; its unit test may be checking the wrong thing.
B. Reword the system prompt so the model reads context more carefully.
C. Add an integration test on the handoff into `assemble_context`, and fix the extraction there.
D. Rerun the end-to-end test; a single failure may be noise.

**2.** A trace shows `model.call()` returning `ok` with a fluent, coherent, factually wrong answer. Before concluding the model reasoned badly, what should be checked first? *(Select one.)*

A. Whether the step before the model call sent it the input that was actually intended.
B. Whether a different model would answer the same question correctly.
C. Whether the parser downstream handles the wrong answer gracefully.
D. Whether the prompt's wording is polite enough.

**3.** A four-step trace shows steps 1 through 3 marked `ok` and step 4, `parse(answer)`, marked `FAIL` with a KeyError on a field the model did not return. What does the trace establish that the eval's zero score alone does not? *(Select one.)*

A. That the whole flow needs to be rebuilt from scratch.
B. That the failure is step four, the parser, raising on a field the model never returned.
C. That the model is unreliable and should be swapped for a different one.
D. Nothing; a trace and an eval score carry the same information.

**4.** Select two true statements about the four test levels. *(Select 2 of 4.)*

A. A unit test tells you a function behaves on its own; it says nothing about how it fits with the functions around it.
B. An integration test exercises the handoff where one component's output becomes another component's input.
C. An end-to-end test is the fastest of the four and the easiest to localize a failure in.
D. A functional test validates the whole system around a call rather than the call itself.

**5.** The chapter compares tracing a run to a plumber tracing pipe joints back to a leak. Where does the chapter say this analogy stops matching the real mechanism? *(Select one.)*

A. Software failures, like leaks, are always visible without any extra setup.
B. A plumber can see or feel water directly at the leak; a trace only shows where a failure occurred if each step was instrumented and logged before the run happened.
C. Pipes and prompts share no structural similarity, so the comparison never applies.
D. A leaking joint and a broken integration test are repaired using the same procedure.

**Answers.** 1: C. The formatter and the model call both already pass; the trace is what names the actual seam, at step 2. 2: A. `model.call()` returning `ok` means the call executed correctly on whatever it was given; the input assembled the step before is what needs checking first. 3: B. The eval's zero score says only that the case failed; the trace localizes it to a named step and cause. 4: A and B. Unit tests isolate one function, and integration tests exercise the handoff between two; C and D reverse the real properties of end-to-end and functional tests. 5: B. A plumber locates a leak by direct observation. A trace only shows a failing step if that step logged its input and output before the run happened.
