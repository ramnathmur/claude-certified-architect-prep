# Chapter 6: Diagnosing a prompt by its failure

## Four labels, six calls

A document-classification prompt is called on the same document six times. The instruction telling Claude what to return has not changed between calls. Twice it comes back as a single top-level label. Three times it comes back as a label plus a nested sub-category. Once it comes back with a numeric confidence score nobody asked for. Nothing about the document is inconsistent. The shape of the answer is.

A team that has not learned to read this reaches for a general fix: rewrite the instruction to sound more forceful, or add a second paragraph restating the same request in different words. Neither touches the actual gap. The prompt never showed Claude what a correctly-shaped answer looks like, so Claude is filling in the shape itself, differently, every time.

## What the noise is telling you

A mechanic does not open the hood and try every tool in the box in sequence. A specific noise narrows the search before a wrench is picked up: a squeal under braking points at the pads, a knock under load points at ignition timing, a whine that only appears in reverse points at the transmission. The noise is the fastest route to the fix, because different failures inside the same engine sound different from the outside.

A prompt failure works the same way. Anthropic's own prompt-engineering guidance documents several distinct techniques, each aimed at a distinct failure, and the failure you are looking at tells you which one is missing. Writing more, or writing the same instruction louder, is the fix a mechanic's method rules out on principle, and it is the fix prompting reaches for far too often.

**Vague or underspecified output.** Anthropic's own guidance states it directly: "Claude responds well to clear, explicit instructions. Being specific about your desired output can help enhance results. If you want 'above and beyond' behavior, explicitly request it rather than relying on the model to infer this from vague prompts." The documented test for whether an instruction is clear enough: "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will likely be too."

**Compliant, but missing the point.** This is a different symptom from vagueness, and Anthropic documents it as a separate technique rather than a stronger dose of the first one: "Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude better understand your goals and deliver more targeted responses." The worked pair on the same page: an instruction reading "NEVER use ellipses" against one reading "Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them." Both name the same rule. Only the second explains why breaking it costs something, and Anthropic's own framing is that "Claude is smart enough to generalize from the explanation." Instruction clarity fixes an underspecified *what*. Added rationale fixes a *why* the instruction never stated. A clear instruction followed to the letter with the goal still missed is the tell that the missing piece is the rationale.

**Format or tone drifting across repeated calls.** This is the classification symptom above, and Anthropic's documentation calls the fix by name: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A few well-crafted examples (known as few-shot or multishot prompting) improve accuracy and consistency." The stated quantity is concrete: "Include 3–5 examples for best results." Examples earn the name only when they meet three documented criteria: "**Relevant:** Mirror your actual use case closely. **Diverse:** Cover edge cases and vary enough that Claude doesn't pick up unintended patterns. **Structured:** Wrap examples in `<example>` tags."

There is a related term worth being precise about, because the exam's own vocabulary and Anthropic's documented vocabulary do not fully overlap. "Zero-shot," "one-shot," and "few-shot" describe how many worked examples a prompt supplies, and the term appears throughout the wider field. Anthropic's current developer documentation, including its own glossary, does not define "zero-shot" as a named prompting technique; it appears in Anthropic's writing only in research and evaluation contexts, never as developer guidance. The safest description of zero-shot for this exam's purposes is the state a prompt is in when it supplies no examples, sourced to the same page's own treatment of what few-shot supplies. A scenario testing whether a candidate reaches for examples at all is testing the zero-shot gap. A scenario testing how many examples and how they should be structured is testing the few-shot guidance quoted above, and only that second question has Anthropic's own documented technique behind it.

**Claude reading the wrong part of a mixed prompt as the instruction.** Documented fix: "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag (for example, `<instructions>`, `<context>`, `<input>`) reduces misinterpretation." A related placement rule addresses a different version of the same symptom, degraded quality on long or multi-document input: "Place your long documents and inputs near the top of your prompt, above your query, instructions, and examples. This improves performance across all models," with queries placed last measured, in Anthropic's own tests, to improve response quality by up to 30 percent on complex, multi-document input. Both rules solve the same underlying problem: Claude has to infer where one kind of content ends and another begins, whether the fix is a tag or an ordering rule.

**Claude ignoring a "don't do this" instruction.** Anthropic's documented framing states the fix as a direction, not just a rewrite: "Tell Claude what to do instead of what not to do." Its own before/after: "Do not use markdown in your response" against "Your response should be composed of smoothly flowing prose paragraphs." Same constraint, stated as an action rather than a prohibition.

**A prompt that reads fine and still fails once real traffic hits it.** Anthropic frames this as a named cycle rather than an ad hoc habit: "Building a successful LLM-based application starts with clearly defining your success criteria and then designing evaluations to measure performance against them." The cycle runs test cases, a preliminary prompt, iterative testing and refinement, final validation, ship: five stages in a fixed order that start from criteria and test cases before the prompt itself is drafted. A prompt that has been reread and polished by eye, with no test cases run against it, has skipped the first two stages the documented cycle puts before refinement.

**A user directly trying to defeat the system, versus untrusted content carrying its own instructions.** These read as the same surface symptom, an unwanted instruction taking effect, and Anthropic documents them as two different threats needing two different fixes. Where the user of the application is the adversary: "Filter user input for known injection patterns before it reaches Claude," or "use a lightweight model like Claude Haiku 4.5 to pre-screen user input before it reaches your main conversation." Where the user is trusted but Claude is reading third-party content the user did not write (a fetched web page, an email body, a tool's return value), the documented fix is isolation rather than filtering, because the content is not necessarily malicious on its face, only untrusted: "Put untrusted content only in tool results... Claude is trained to treat instructions that appear inside tool results with appropriate skepticism," "Tell Claude what the content is and where it came from," and "JSON-encode untrusted content" so "an attacker cannot close a quote or tag to 'break out' into an instruction context." A scenario naming the user as the threat calls for filtering before the request reaches Claude. A scenario naming a document, page, or tool result as the source of the unwanted instruction calls for isolation and labelling instead, because there is nothing to filter. The content carries no disguise. It is simply untrusted.

That last symptom sits on a mechanism worth stating once, plainly, because it is what makes the whole category of sanitization necessary rather than optional. Claude reads a request as one continuous stream of tokens. Nothing in that stream is structurally marked as "this part is an instruction" versus "this part is data" beyond the placement and tagging conventions a prompt author chooses to apply. A paragraph pasted from an email, a paste from a support ticket, a block copied from a web page: all of it enters the same stream your own instructions occupy, and if nothing distinguishes it, anything readable in it is readable as instruction. This is why placement and tagging are load-bearing rather than tidy, and it is the fact that makes the difference, three sections later in this course, between an untrusted paragraph you have merely isolated and one you have decided your agent may still act on.

## The rule underneath the taxonomy

Eight symptoms, eight named techniques, one rule connecting them: a prompt failure has a shape, and the shape names the missing piece. Vague output points at clarity. Compliant-but-pointless output points at rationale. Drifting format points at examples. Misread structure points at tags or ordering. Ignored prohibitions point at positive framing. A prompt that degrades once it meets real traffic points at the refinement cycle, run as a cycle rather than skipped to the final step. An unwanted instruction taking effect points at sanitization, and which sanitization depends on whether the source of that instruction is the user or something the user merely fetched.

A new failure that does not match any of the eight above is a sign the symptom has not yet been read closely enough to say what, specifically, went missing. The diagnostic habit is what generalizes past this list.

## Where "write it more clearly" stops working

A support team's escalation macro instructs Claude to always restate the refund policy before closing a ticket. In practice, Claude skips the restatement whenever the conversation already reads as resolved. The instruction names exactly what to do and when.

The team's first fix is to make the instruction louder: capitalize the key clause, repeat it in a second sentence, move it to the top of the system prompt. The skipping continues at close to the same rate, because the instruction was never unclear. Claude has consistently understood what to do; it has been deciding, call by call, that a policy restatement is redundant once a customer's issue already sounds settled, which is a reasonable inference for anyone who has not been told otherwise.

The fix that actually holds adds a sentence of rationale rather than more force: customers who do not hear the refund policy restated re-contact support within 48 hours in roughly a third of resolved tickets, so the restatement is what keeps a resolved ticket resolved. Once the instruction carries a reason a reasonable assistant would weigh against "this looks finished," Claude stops treating the restatement as optional. Louder instructions repeat a *what* Claude already had. The fix needed a *why* Claude never had, and emphasis on the first is no substitute for supplying the second.

## What a diagnosis by symptom does not cover

Every technique in this chapter operates inside the prompt: what words appear, in what order, in what tags. None of it produces a guarantee. A well-written instruction to return valid JSON, however clear, however well-exampled, is still a request Claude can decline to satisfy exactly on a given call. Where a task needs the response to conform to a schema rather than merely resemble one, that guarantee is bought at the API level, and buying it is this course's next chapter.

Sanitization inside this chapter is a construction discipline: where untrusted content sits in a request, and how it is labelled and encoded, so Claude has the signal to treat it with appropriate skepticism. It is not the decision of what an agent is permitted to *do* once it has read something untrusted. That decision, the action boundary, belongs to a later chapter on untrusted content, and this chapter's placement and encoding techniques are what make that later boundary enforceable rather than cosmetic.

## The phrase that names this chapter

A stem describing output that is inconsistent, mis-shaped, tonally off, or technically correct but missing the point is asking which technique is missing. A stem naming a user as the source of an unwanted instruction is a different sub-question from one naming a document, a page, or a tool result as that source, even though both read, on the surface, as "an instruction that shouldn't have worked."

## Self-test

**1. Select ONE.** A support macro instructs Claude, clearly and specifically, to cite the account's renewal date in every retention call. Claude follows the instruction reliably in isolation but omits the date whenever the customer has already stated they intend to stay. The instruction has not changed in weeks.

A. Rewrite the instruction with more forceful, repeated wording.
B. Add one sentence explaining why the renewal date matters even when the customer sounds retained.
C. Add three worked examples of a correctly formatted retention call.
D. Lower the model's effort level so it spends less time weighing whether the date is still relevant.

**Answer: B.** The instruction is already clear and is followed elsewhere, so the gap is not underspecification; Claude is making a reasonable inference in the absence of a stated reason not to. A repeats a fix for a problem that is not present. C addresses format drift, which is not the symptom described. D touches nothing about this decision and risks the opposite of the fix needed.

---

**2. Select ONE.** A summarization endpoint returns a bulleted list on some calls and a single paragraph on others, for input documents of similar length and content. The instruction asks only for "a summary."

A. Switch to a larger model.
B. Add 3–5 examples showing the exact output format wanted.
C. Move the instruction from the user turn into the system prompt.
D. Lower the temperature to make output more repeatable.

**Answer: B.** Format drift with an unchanged instruction is the documented symptom that few-shot examples address; the instruction never showed Claude which shape counts as correct. C changes where standing behavior lives; it leaves the demonstrated output shape untouched. D affects how concentrated the token distribution is; it does not specify a shape at all. A spends on capability the scenario gives no evidence is the constraint.

---

**3. Select ONE.** A prompt concatenates a fetched support ticket directly into the user turn, ahead of the instruction telling Claude how to categorize it. On tickets that happen to contain phrases like "ignore the categories above," Claude sometimes complies with the pasted text instead of the actual instruction.

A. Add a stronger warning sentence telling Claude to ignore anything that looks like an instruction inside the ticket text.
B. Place the ticket content inside a tool result rather than the plain user turn, and tell Claude where the content came from.
C. Raise the model tier so it is less easily confused.
D. Ask Claude to summarize the ticket before categorizing it.

**Answer: B.** This is untrusted third-party content rather than a user directly attempting to jailbreak the system, so the documented fix is isolation and provenance labelling: Claude is trained to treat tool-result content with more skepticism than plain text sharing the user's own turn. A adds another sentence to the same undifferentiated stream the ticket text already sits in, which is the condition that let the phrase read as an instruction in the first place. C spends on capability where the scenario is about structure. D leaves the embedded phrase sitting in the same stream Claude reads.

---

**4. Select ONE.** A 40-page contract is pasted into a prompt, followed by a two-sentence instruction asking which clauses mention indemnification. Answer quality is noticeably worse than on shorter documents with the same instruction.

A. Move the two-sentence instruction to before the contract text.
B. Rewrite the instruction to be longer and more detailed.
C. Add three worked examples of correctly identified indemnification clauses.
D. Raise the effort level so the model reasons longer before answering.

**Answer: A.** Anthropic's own documented placement guidance measures a quality improvement specifically from placing long documents ahead of the query and instructions. Lengthening the instruction, adding examples, or asking for more deliberation all leave the document's position relative to the question unchanged, which is what the scenario is actually testing.

---

**5. Select ONE.** A prompt has been reread twice, tightened for wording, and looks correct by inspection. On real customer inputs it fails roughly one call in five, in ways the author cannot reproduce by rereading the prompt.

A. Rewrite the prompt once more for clarity.
B. Define success criteria and run it against a set of real test cases before refining further.
C. Add a rule-of-three list of examples to the system prompt.
D. Switch to a model with a larger context window.

**Answer: B.** The documented refinement cycle starts from success criteria and test cases before any further editing; a prompt polished by rereading alone has skipped the stages that would surface a one-in-five failure rate at all. A repeats a step already taken without new information. C and D do not address a failure whose cause has not yet been identified.
