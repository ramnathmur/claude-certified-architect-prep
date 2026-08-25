# Chapter 26: Defining Done Before You Build It

## Three tries and it looked right

A team ships a support-ticket summarizer. Before launch, the person who wrote it tries it on a handful of real tickets, reads the output, and it looks right. Three tries, no misses, ship it. Two weeks later a support lead flags a summary that dropped the customer's actual request and kept only the pleasantries around it. Nobody can say how often that happens: nothing was checked beyond the author's own judgment, on cases the author picked.

That's the gap this chapter closes. "It looked right" is a judgment made once, on a small sample, against no written standard. It cannot be repeated, and it cannot tell you whether tomorrow's change to the prompt made things better or worse. What replaces it is a fixed procedure, run against cases and expectations written down before the feature exists.

## A checklist written before the candidate sits down

A driving test does not grade "did that feel like good driving." It has a fixed, written checklist: signal before every lane change, stop fully at the line, parallel-park within the marked space. The checklist and its pass threshold are set before any candidate gets in the car, so a pass or fail is a checkable outcome against a standard fixed in advance.

An eval is that checklist for a feature. Before you have one, done is a feeling. After, it is a score on a fixed set of cases. You collect a set of input cases, write down the behavior you expect for each one, run the feature on every case, grade the output against what you wrote down, and average the scores.

The pipeline is genuinely small: one function runs a single case and grades it, a second loop runs every case in the set and averages the results.

```
def run_test_case(test_case):
    output = run_prompt(test_case)
    score = grade(test_case, output)
    return {"output": output, "score": score}

def run_eval(dataset):
    results = [run_test_case(c) for c in dataset]
    average = sum(r["score"] for r in results) / len(results)
    return results
```

The score on a first attempt is not inherently good or bad. A two or three out of ten on the first run is normal. What matters is whether the number moves when you change the prompt, the tools, or the model, one of those at a time. Change two at once and a moving score tells you something changed, not what caused it.

## Choosing who grades the answer, and how

The examiner's checklist mixes two kinds of item. Some are mechanical: did the mirror check happen, yes or no. Others take judgment: was the following distance safe for the conditions. An eval faces the same split, and picking the wrong grader for the item wastes the whole exercise.

Exact match is the cheapest grader: check the output character for character against one correct string. It works when there is exactly one correct form, a classifier returning one label. It fails the moment a valid answer can be phrased more than one way.

A code-graded check runs a function against the output instead of a string: does it parse as JSON, is a required field present. This catches format and syntax failures cheaply, and it says nothing about whether the content is good.

The contrast shows up cleanly on a feature that returns a region's three capital cities as a JSON array. One run returns the same three cities in a different order than the reference string. Exact match scores it zero, because the characters don't line up. A code grader that parses the array and checks membership scores it correctly, because all three cities are present and the structure is valid. The grading method has to match the shape of a correct answer, not just the shape of the output.

LLM-as-judge is the third method: a second model call, given the output and a rubric, returns a score. It is the only method that scales an open-ended quality question like "is this summary faithful to the source," because no code rule expresses faithfulness. It is also the most expensive and noisiest of the three, and a judge asked for only a number drifts toward a safe middle score, around six, regardless of quality. Asking it for strengths, weaknesses, and reasoning alongside the score is what anchors that number to something specific.

The driving-test checklist has a limit worth naming here. A driving examiner is one person making a judgment call on every item, mechanical and subjective alike. An eval doesn't get that shortcut. Choosing which grader handles which case, exact match, code check, or judge, is itself a design decision, and getting it wrong is not a minor scoring nuance. It's the difference between a score that means something and one that only looks like it does.

## Trusting the judge's number

Calibration is the step that's easiest to skip, and skipping it is exactly what leaves a judge's score unproven. Start from a set of cases a human has already labeled, twenty or so is enough, and measure how often the judge's score agrees with the human's. Low agreement means the rubric is loose: tighten what each score means, add one example of a good answer and one of a bad one, and measure again.

## Working backward from the checklist to the spec

Reverse the driving-test logic: to write a checklist you can grade against, you first have to decide, in writing, what a pass looks like. "Summarize the thread" cannot be graded, because two defensible summaries can disagree with each other and both still be right. "A two-sentence summary that lists every action item and its owner" can be graded, because a grader, human or code, can check each clause of the output against that sentence.

That is the first of four decisions a short design document states before any production code gets written: what the feature must produce, specific enough to check. Write that decision first and the eval set follows from it directly: one case per representative situation, one stated expectation per case. The other three decisions in the same document set up later chapters of production hardening. This chapter stays with the first one alone.

## When the average lies

A team changes a prompt, reruns the eval, and the average score ticks up. The average says the change helped; ship it. The per-case breakdown says something different: three cases that used to fail now pass, and three that used to pass now fail, on exactly the case type the change was meant to protect. The average across those eight cases barely moves, but a user hitting the three newly broken cases sees a regression the average hid.

The per-case view is what tells you why a case failed, which the average never shows. A formatting failure points at the prompt's output instructions. A factual failure on retrieved content points at the retrieval step. A failure that appears only on long input points at how the feature handles context. Reading only the average and stopping there throws away the information that turns the next change into a targeted fix instead of a guess.

The same mechanism argues for more cases over fewer, cleaner ones. A small hand-picked set tends to cover the cases the author already thought of, and misses the ones a real user actually sends. Twenty cases with messy, irregular input catch a break that three carefully chosen cases never exercise. Claude can generate additional cases from a small labeled starting set, spot-checked afterward, cheaper than hand-writing every case and still catching more.

## What this chapter doesn't decide

The eval answers one question: did this change make the feature better at the thing it's supposed to do. Two decisions sit outside that question. What happens when a call fails, and what a user sees when it can't recover, is failure handling, built from a trace of what actually broke, in chapters 27 and 28. Which inputs are untrusted, and how small the feature's permissions should be, is the trust boundary, chapter 29's territory. The same design document states all four decisions once, before the build starts, so the eval, the error handling, and the security boundary are all checked against one written standard.

## The tell

A stem naming this chapter says "how do you know the change helped," "compare against a baseline," "grade automatically," or "define success before building," often with a grading method mismatch buried in it, like a correct answer in a different order scoring zero. A stem about what a failed call should return, or about which input is untrusted, belongs to chapters 27 through 29 instead.

## Self-test

**1.** A feature must return a boolean flag stating whether a submitted address is deliverable. There is exactly one correct value for every case in the set. *(Select one.)*

A. LLM-as-judge, because deliverability is a judgment call.
B. Exact match, because there is one correct value per case and nothing to paraphrase.
C. Code-graded check, because a boolean needs range validation.
D. Skip grading and read the outputs by hand, since the set is small.

**2.** A feature returns a one-paragraph rationale for a loan recommendation, and no two good rationales are worded the same way. *(Select one.)*

A. Exact match, scored against one reference rationale.
B. A code-graded check confirming the output is a non-empty string.
C. LLM-as-judge, given the rationale and a rubric for what a sound one contains.
D. Skip grading; rationales are too subjective to score.

**3.** A team calibrates a judge against a set of human-labeled cases and finds it agrees with the human score on well under half of them. *(Select one.)*

A. Trust the judge anyway; a second model call is inherently more consistent than a human.
B. Tighten the rubric, add an example of a good and a bad answer, and measure agreement again.
C. Replace the judge with exact match, since judges are unreliable by nature.
D. Raise the pass threshold so more cases score above it.

**4.** Which two of the following does reading an eval's per-case results, rather than only its average score, actually give you? *(Select two of four.)*

A. A category for each failure, formatting, retrieval, context length, that points at what to fix next.
B. A guarantee that the average will rise on the next run.
C. Visibility into a change that fixed some cases while breaking others, which a steady average can hide.
D. Confirmation that exact match is always the correct grading method.

**Answers.** 1: B. One correct value with no paraphrase risk is what exact match is for; A and C reach for a heavier grader the case doesn't need. 2: C. An open-ended rationale needs a rubric-based judge; B only confirms the string exists, which says nothing about quality. 3: B. Weak agreement means the rubric doesn't yet say what each score means; A and C dodge the actual fix, and D moves the threshold instead of fixing the disagreement. 4: A and C. The per-case view supplies a failure category and reveals a mixed result an average can flatten; B and D claim guarantees it doesn't provide.
