# Chapter 7: When asking nicely stops working

## A booking system, and the passenger count that arrived as text

A travel-booking integration asks Claude to return a JSON object after each request, with a plain-language instruction: always return valid JSON matching this shape, including a `passengers` field that is a number. The instruction is followed on almost every call. On some calls, `passengers` arrives as `"2"` instead of `2`, or as the word `"two"`. The receiving function expects an integer, and a string in its place breaks it.

Nothing was misunderstood. Claude read the instruction and produced something a reasonable person would call compliant: a count of passengers, clearly stated. The team asked for a shape and received an answer. Those are two different requests, and the gap between them is what this chapter is about.

## Three rungs, and what each one actually guarantees

A passport application starts as free text: a letter describing who you are and what you need, in your own words. Move to a form, and the facts are pinned to named boxes for the whole document at once, each built so a malformed entry can never be written into it at all, rejected the instant it's typed rather than caught after submission. Move to a form built for a machine to read directly, and that same instant rejection narrows from the whole document to one specific box, a passport number for instance, checked and blocked on its own rather than as part of everything else.

Claude's output guarantees run along the same line. Free text carries no guarantee at all: whatever Claude produces is whatever it judged reasonable at the time. Structured outputs and strict tool use each carry a real guarantee, enforced the same way, by constraining what the model is allowed to sample. What separates those two is scope, not strength: one covers the whole response, the other covers a single field.

**Free text.** A plain instruction asking for JSON is still prose Claude is choosing to produce. Anthropic's own documentation names the failure directly: "Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or omit required fields, breaking your functions and causing runtime errors." Whether the instruction is honoured is, at this rung, a property of the model and the prompt rather than a property of the request itself.

**A form, guaranteed for the whole response.** Structured outputs move the guarantee from the prompt into the API: `output_config.format` set to a JSON schema. Anthropic's routing guidance is explicit about when to reach for it: "If you need Claude to always output valid JSON that conforms to a specific schema, use Structured Outputs instead of the prompt engineering techniques below. Structured outputs provide guaranteed schema compliance and are specifically designed for this use case." The entire response is now typed and complete by construction, independent of how well the model happens to behave.

**One box on the form, rejected as it's being written.** Strict tool use narrows the same kind of guarantee to a single field: the arguments passed to a tool. Setting `strict: true` on a tool definition "guarantees Claude's tool inputs match your JSON Schema by constraining the model's token sampling to schema-valid outputs," a technique Anthropic names grammar-constrained sampling. The booking example is Anthropic's own: "suppose a booking system needs `passengers: int`. Without strict mode, Claude might provide `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response always contains `passengers: 2`." For that one field, the wrong shape is never sampled in the first place.

Two documented levers sit near this ladder without belonging to it, and a stem naming either is asking a different question. `tool_choice` forces *that* a tool is called at all; it says nothing about the shape of the call. Prompting Claude to use tools more readily nudges the same *whether* question. Neither substitutes for `strict: true`, which is the only one of the three that guarantees *what shape* the call takes.

## The rule this chapter is built on

Prose carries no guarantee, however well it is written; the model remains free to satisfy it however it judges reasonable. Moving a requirement out of prose and into a schema, at whichever scope actually fits it, replaces that judgement with a constraint the model cannot sample its way around. The fix for the booking integration is a schema enforced at the point of generation, in place of a clearer instruction requested in prose.

## What no rung on this ladder checks

A completed passport form, every box filled in the correct format, can still state a false birthdate. The form's own check stops at shape; nothing about a well-formed submission confirms its contents are true. Anthropic states the same limit about structured outputs specifically, in one sentence worth taking literally: "Structured outputs guarantee that Claude's response matches your schema, but do NOT guarantee the content is correct or accurate, only that it is schema-valid." The analogy carries the limit but not the mechanism: a passport form is checked by a clerk after it's handed in, while a schema constrains what Claude is allowed to generate as it writes, with no separate check afterward. The same limit holds one rung further up: strict tool use guarantees that `passengers` holds a well-typed integer. It has no way to guarantee that integer is the passenger count this particular booking actually needs. A `passengers` field holding a plausible, well-typed, wrong number passes every check this chapter has built so far, on either rung.

This is where **response validation** and **defensive parsing** stop being one activity wearing two names. Parsing asks whether the response can be read into the shape your code expects, a question the SDKs largely answer for you through typed helpers such as `client.messages.parse(...)` in Python or `zodOutputFormat` in TypeScript. Validation asks whether the content is correct, a question no schema, strict or otherwise, is built to answer, because a schema constrains shape and stays silent on meaning. `minimum`, `maximum`, and `maxLength` are the clearest case: business rules like these are exactly the kind of constraint the current guarantee does not enforce, so range and length checks still belong in your own code even after the shape is trusted completely.

The guarantee can also lapse before content is even the question. A response cut short by `max_tokens` arrives with an incomplete or invalid JSON body, and the field to check is `stop_reason`: a value of `"max_tokens"` means the response was truncated and should not be trusted, whatever it contains. Raising the effort level makes this more likely, because thinking tokens are drawn from the same `max_tokens` budget the JSON needs to complete in. A refusal returns ordinary text in place of structured output entirely, so the response must be checked before it is parsed at all, with a refusal handled by falling back to a different model rather than retrying the same request unchanged.

Confidence and correctness are two different properties here. A schema-valid answer, stated fluently, carries no information about whether it is right; only a check run against the content, separate from the check run against its shape, tells you that.

## What this chapter leaves for later

Everything above assumes a tool is what this chapter needs it to be: a named schema, given as JSON Schema in the tool definition, that the model must fill in correctly. Which tool to define, how many to register, and how to word its `description` field so Claude reaches for the right one on a crowded board of options is a different question, and it belongs to the next chapter that deals with tools directly.

## The tell

A stem asking how to *guarantee* a JSON shape, a field's type, or a field's presence, using the language of `strict: true` or structured outputs, is asking about this chapter's ladder rather than about writing a better instruction. A stem asking whether a schema-valid answer can still be factually *wrong*, or one flagging a `stop_reason` of `"max_tokens"`, is asking about validation, which sits above every rung of that ladder.

## Self-test

**1. Select ONE.** An integration needs every response to be valid JSON with an integer `quantity` field, with zero tolerance for a malformed or wrongly-typed call reaching the downstream function.

A. Rewrite the prompt to state the required shape more precisely and add two examples.
B. Set `strict: true` on the tool definition carrying the `quantity` field.
C. Set `tool_choice` to force the tool to be called on every turn.
D. Lower the effort level so the response completes with less deliberation.

**Answer: B.** Strict tool use constrains sampling so the call cannot be generated outside the schema; it is the only option of the four that guarantees shape. A is still a request written in prose, which the model can decline to satisfy exactly regardless of how detailed it gets. C guarantees that a tool is called; it says nothing about the shape of the call. D affects how much the model deliberates; conformance is untouched either way.

---

**2. Select ONE.** A response using structured outputs returns a schema-valid object. A downstream audit later finds one field's value is factually wrong for that record.

A. The schema failed; strict mode should have been enabled.
B. Structured outputs guarantee shape but leave content accuracy unchecked; the wrong value is a validation gap rather than a schema failure.
C. The `tool_choice` setting was misconfigured.
D. Raise `max_tokens` so the model has room to reconsider the value.

**Answer: B.** Anthropic documents the guarantee as covering schema conformance only, explicitly excluding content correctness. A misapplies a shape-level fix to a content-level problem. C names an unrelated lever. D addresses truncation and does nothing for a value that is complete but wrong.

---

**3. Select ONE.** A structured-output response arrives with `stop_reason: "max_tokens"` and a JSON body that fails to parse.

A. Use the response as-is; a schema-valid shape was requested, so it can be trusted.
B. Treat the response as truncated and unusable; raise `max_tokens` or otherwise let the response complete.
C. Retry the identical request against the same model with no other change.
D. Switch to a stricter schema so truncation cannot occur.

**Answer: B.** A `max_tokens` stop reason means generation was cut off before completion, which the field itself signals, regardless of what schema was requested. A ignores the documented meaning of the stop reason. C does not address why the response was cut short. D confuses a schema constraint with a length constraint; they are independent settings.

---

**4. Select TWO.** Which two statements accurately distinguish parsing from validation in this chapter's sense?

A. Parsing checks whether a response can be read into the expected shape; validation checks whether its content is correct.
B. A schema that enforces required fields and types also guarantees the values in those fields are accurate.
C. Range and length constraints such as `minimum` or `maxLength` are business rules that current schema enforcement does not check.
D. Once strict tool use is enabled, no further content checking is ever necessary.

**Answer: A and C.** These name the actual division of labour: shape is enforced by the schema, and content correctness and business-rule constraints sit entirely outside it. B and D both claim the shape guarantee extends to content, which Anthropic's own documentation states directly that it does not.
