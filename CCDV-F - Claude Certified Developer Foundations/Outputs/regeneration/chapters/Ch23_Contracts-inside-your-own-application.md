# Chapter 23: Contracts Inside Your Own Application

## A billing team that will not sign off on "usually"

A support-ticket triage feature hands its output to the billing team's reconciliation system: category, priority, assigned queue, one record per ticket. The billing team does not work on the AI project. They wrote back with one requirement: every record in the nightly batch has to parse into their schema, or the whole batch fails their audit run. "The model usually gets the category right" is not something their pipeline can build a check around. They don't care how the category was decided. They care whether the record that arrives can be checked, mechanically, against a shape they specified in advance.

That is a constraint from outside engineering, and it names the problem this chapter solves. A wrong answer is expensive to catch when the only way to catch it is a person reading the output and deciding whether it looks right. A contract, a defined boundary between instruction, data, and output, plus a schema for what comes back, turns that judgment call into a mechanical check. The response either matches what was promised or it doesn't.

A general contractor extracts the same deal from every subcontractor on a job. The sub gets a written scope of work, the instructions, and the site materials, samples, measurements, existing conditions, the data. What they deliver, the finished work, is only acceptable if it meets acceptance criteria agreed before the first day on site and checkable the moment the work is done. Nobody walks the site afterward asking whether it "seems about right." They check it against the list.

## Three zones, kept apart

An application built on Claude moves three different kinds of content through one conversation: the instructions you wrote, the data Claude is working on, and the output it hands back. Anthropic's guidance is specific about where the middle one is allowed to sit. Untrusted content, a fetched web page, an inbound email, a document a user uploaded, belongs only inside a `tool_result` block. It should not appear inside the system prompt or inside a plain user text block, because Claude is trained to read content inside a `tool_result` with more caution than it reads a direct instruction.

The rule runs the other way too. Your own instructions do not belong inside a `tool_result` block either. Content placed there is treated as data, so an instruction sitting in that slot may be discounted along with everything else in it. If a task needs Claude to act on something once a tool call returns, that instruction belongs in the user turn that follows the tool result, sent as its own turn rather than folded into the result.

This is the job-site rule in miniature: the blueprint stays in its own folder, the site materials stay in their own pile, and nobody staples a change order to a delivery of lumber and expects the crew to read it as an instruction.

Placing content in the wrong slot creates ambiguity. Once an instruction and a fact sit inside the same undifferentiated block of text, nothing in the transcript can mechanically tell you which one was which, and neither can Claude. A wrong answer that comes out of a muddled boundary has no clean line to point to. A wrong answer that comes out of a violated boundary does: the content was in the wrong place, a fact checkable by reading the request structure rather than a judgment reconstructed after it.

Three techniques reinforce the boundary once the placement itself is right. State the policy explicitly, inside the system prompt, that content returned from a tool is untrusted and should not override an instruction. Name the content's nature and source, in the tool's `description` or in the structure of the result, so both Claude and a human reading the transcript later know they are looking at the body of an inbound email from an unknown sender rather than an unlabeled string. And where the content might itself contain characters that look structural, quotes, tags, delimiters, encode it as a JSON string inside the `tool_result` rather than concatenating it into free text. JSON escaping gives the payload unambiguous delimiters, so a stray character in the real data cannot be read as the end of the data and the start of something else. This is the same reason XML tags help any prompt that mixes instructions, context, and input: wrapping each kind of content in its own tag, `<instructions>`, `<context>`, `<input>`, gives the parser, and the person reading the log afterward, an edge to check against instead of a wall of undifferentiated text.

## What the delivered shape has to match

The output side of the contract works the same way, and Anthropic documents it as two separate mechanisms rather than one. Structured Outputs groups both under a single name. They are two: JSON outputs, configured through `output_config.format`, control the shape of Claude's own response, the thing your application receives back. Strict tool use, configured through `strict: true` on a tool definition, validates the parameters Claude sends when it calls one of your functions. These solve different problems and can be used together in the same request. An application's own output contract, the one the billing team's reconciliation pipeline checks against, is the JSON-outputs mechanism. A tool's input contract, which chapter 11 already covers, is the separate strict-tool-use mechanism.

The schema language for either one is JSON Schema, but a bounded subset of it. Supported: the basic types, object, array, string, integer, number, boolean, null; `enum` and `const`; `anyOf` and `allOf`, with limits; `$ref` and `$def` for reuse inside the same document; a fixed list of string formats, including `date-time`, `email`, and `uuid`; `required`; `additionalProperties`, which must be set to `false` on an object; and `minItems` on an array, restricted to 0 or 1. Not supported: recursive schemas, complex types nested inside an `enum`, a `$ref` pointing outside the document, and numeric or string-length constraints such as `minimum`, `maximum`, `minLength`, `maxLength`. A schema that leans on `maxLength` to cap a field will not compile here. The subset is smaller than the full specification, and the acceptance criteria have to be written inside that boundary from the start.

Closing the schema is the specific practice that turns it into a contract rather than a loose suggestion. In JSON Schema generally, unrecognized fields are allowed by default, so a schema without `additionalProperties: false` is a suggestion, not a contract: an extra field passes through unnoticed, because nothing in the check is looking for fields it wasn't told to expect. Closed, the same schema rejects that record the moment an unexpected field shows up. SDKs that generate a schema automatically from a native type, a Pydantic model, a Zod schema, add this flag for you, which signals how load-bearing it is treated.

Three named use cases show what this contract is for: Data Extraction, pulling structured fields out of unstructured text; Classification, assigning a category, a confidence score, a tag; and API Response Formatting, shaping status, data, and error fields for whatever system reads the response next. All three are the same move, stated at the top of this chapter: decide the shape you need before the request goes out, and let the schema do the checking instead of a person reading the response.

## Why a closed acceptance list is the only kind that catches a breach

Derive the closed-schema rule from what "checkable" actually requires. A check that can pass or fail mechanically needs a boundary around what counts, because a boundary is what makes "unexpected" a defined condition rather than a matter of opinion. An acceptance list with no boundary, one that reads "the fields below, and anything else reasonable," cannot fail on an unreasonable extra field, because "reasonable" was never written down as a checkable condition. It has to be judged, and a judged check is exactly the thing a contract exists to remove.

`additionalProperties: false` supplies that boundary on the software side. Once it's set, the schema stops being a list of fields Claude is encouraged to include and becomes a list of fields the response is permitted to contain and no others. A response either matches that closed list, in which case it passes, or it doesn't, in which case it fails, with the failing field named in the validation error. There is no third outcome where a reviewer has to decide whether the extra field is close enough to acceptable.

This is exactly where the subcontract analogy stops mapping cleanly onto the software mechanism, and the gap is worth stating precisely. A general contractor's acceptance criteria are usually written in language that still needs a human on site: "workmanlike manner," "to code," "consistent with the sample." A GC inspecting delivered work applies judgment to those phrases even with a written checklist in hand, because the checklist's own terms are not fully mechanical. The schema check this chapter teaches has no equivalent judgment step. `additionalProperties: false` and a `required` list are evaluated by a validator; no person walks the site to judge them, and the outcome is the same regardless of how the extra field got there. The contract analogy explains why acceptance criteria matter; it does not explain how mechanical this particular check is, because nothing in a construction contract is quite that mechanical.

## A response that reads fine and still breaches the contract

A team building the triage feature tests it by eye for a week: category, priority, queue, each field present, each value plausible, nothing that looks wrong. The schema they wrote has `required` set for all three fields but leaves `additionalProperties` unset, which defaults to permitting extra ones. A prompt change causes Claude to start including a fourth field, a short `reasoning` string explaining the category choice, useful context, correctly typed, harmless to read on its own. Nothing in the eyeball test catches it, because the response still reads as a good answer.

The billing team's reconciliation pipeline breaks two weeks later, because their own parser was written against the original three fields and the extra field pushes a downstream row past a fixed-width limit in a system nobody on the AI team has access to. The failure surfaces far from its cause, in a system that only receives the output, well after the change that caused it. Tracing it back means reading logs across two teams to find a field that was never supposed to be there.

The fix is a closed schema: `additionalProperties: false` on the original three fields. With that flag set, the same prompt change that added the `reasoning` field would have failed the request the moment it happened, in the same system, on the same day, with a validation error naming the exact field that didn't belong. Surface features, a plausible-looking response with reasonable values, said everything was fine. The schema said otherwise, and the schema was checking the thing that actually mattered.

## Two contracts, one for the tool, one for the app

The schema this chapter covers, configured through `output_config.format`, is the contract between your application and whatever reads Claude's final answer: a reconciliation pipeline, a UI, another service. A tool's `input_schema`, validated by `strict: true`, is a different contract, the one between Claude and the function it calls mid-turn. Chapter 11 already covers how to write a tool schema that survives contact with an ambiguous request; this chapter does not repeat that ground. The two mechanisms can run in the same request, one governing what Claude asks a tool for, the other governing what Claude hands back once it's done, and a single stem can test whether both are needed at once rather than assuming one covers the other.

A schema contract has a cost boundary worth knowing before reaching for one on every request. The first time a schema is used, compiling the grammar behind it adds latency. The compiled grammar is cached for 24 hours from last use, but that cache is invalidated the moment the schema's structure changes or the toolset in the request changes. A schema rebuilt fresh on every call, shaped per user rather than reused across a fixed set of request types, forfeits that cache on every single request it runs. A small number of stable, reused schemas is what keeps the contract cheap as well as checkable.

The same instruction/data boundary that makes a wrong answer detectable here also closes off a specific way an adversary could exploit a muddled one; a later chapter covers that framing directly, as a defense rather than as a design choice.

## What the stem sounds like

A stem naming this chapter describes a downstream system, a compliance reviewer, or another team that needs Claude's response to always parse into a fixed shape, or it describes third-party content, an email, a web page, a document, arriving through a tool call. The tell is the word guaranteed, or a downstream system with zero tolerance for a record it cannot parse.

## Self-test

**1.** A feature fetches a customer's support-ticket history from a third-party helpdesk API and needs Claude to summarize it. Where should that fetched content be placed in the request? *(Select one.)*

A. Inside the system prompt, so Claude treats it as authoritative background.
B. Inside a plain user text block, concatenated with the summarization instruction.
C. Inside a `tool_result` block, with the summarization instruction sent in the following user turn.
D. Split evenly between the system prompt and a `tool_result` block, for redundancy.

**2.** A team writes a JSON schema for Claude's response with `required` fields for `status` and `data`, but does not set `additionalProperties`. What is the mechanical consequence? *(Select one.)*

A. The schema fails to compile, because `additionalProperties` is mandatory on every object.
B. A response containing an extra, unexpected field will still pass validation.
C. Claude will refuse to respond until `additionalProperties` is set.
D. The response is capped at exactly two fields regardless of the schema.

**3.** Which two of the following are NOT supported by the JSON Schema subset used for Claude's structured output? *(Select 2 of 4.)*

A. `required`
B. `minLength` on a string field
C. `enum` with string values
D. A recursive schema

**4.** An application needs two guarantees in the same request: Claude's final answer must always parse as `{status, data, errors}` for a downstream billing service, and a tool Claude calls mid-turn must always receive validly typed parameters. Which pairing correctly matches mechanism to guarantee? *(Select one.)*

A. `output_config.format` for the tool's parameters; `strict: true` for the final answer.
B. `strict: true` for both guarantees, since it is the general-purpose validation mechanism.
C. `output_config.format` for the final answer; `strict: true` for the tool's parameters.
D. Neither mechanism applies; both guarantees require a custom validation layer outside the API.

**Answers.** 1: C. Third-party content is untrusted data and belongs only in a `tool_result` block; the instruction to summarize it follows in the next user turn, so A and B place data where it can be read as authoritative instruction, and D splits a single piece of data across two slots for no documented benefit. 2: B. Without `additionalProperties: false`, the schema is open, and an object schema without it does not reject unlisted fields; A and C invent a hard requirement that doesn't exist, and D confuses `required` with a field-count cap. 3: B and D. `minLength` is a string-length constraint and recursive schemas are unsupported; `required` and string-valued `enum` are both part of the documented subset. 4: C. `output_config.format` is the application's own output contract, and `strict: true` validates a tool's input; A reverses the mapping, B collapses two distinct mechanisms into one, and D ignores that both are built-in API mechanisms.
