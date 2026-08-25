# Chapter 30: Layered Guardrails

## One classifier, twenty-four failures out of twenty-five

A security team building a customer-support agent trusted one control to keep it safe: the model itself. The system prompt told Claude to refuse any request touching customer credentials, and the team assumed that instruction, backed by Claude's own training, was the defense. Anthropic's own engineering team reported a test with the same shape: a phishing-style prompt instructing Claude to exfiltrate credentials, aimed at model-layer classifiers with nothing behind them, got through 24 times out of 25. The classifier was not broken; a user-typed instruction simply does not look anomalous to it the way a malware payload does, and from where the model layer sits, the request read like a normal one. The only thing that would have stopped it sat outside the model entirely: a network rule that blocked the outbound connection regardless of what the text said.

## The vault has five layers, and each one catches something different

A bank vault is never secured by its door alone. A door built to resist any realistic attack still gives way eventually to a thief with enough time, so a real vault layers a door, an inner cage, a time-lock, cameras, and a guard, and each layer catches what the layer before it didn't stop. Anthropic's own security guidance for the Agent SDK states this directly for software, under a heading called Defense in depth: "layering multiple controls provides additional protection," listing container isolation, network restrictions, filesystem controls, and request validation at a proxy as the options. The stated reasoning: Claude is trained to resist prompt injection, but defense in depth is still good practice, because if an agent processes a malicious file instructing it to send customer data externally, network controls block that request whether or not the model resisted.

Five layers, matched to the vault:

**The door — model-layer defenses.** A system prompt that states ethical and legal boundaries and tells Claude exactly how to refuse; a lightweight classifier that pre-screens input before it reaches the main conversation; input validation that filters known jailbreak language before Claude ever sees it. This is the cheapest layer to add. It is also the layer the 24-of-25 test defeated, because all three controls work by judging whether text looks dangerous, and a well-written attack prompt is written specifically not to look dangerous.

**The inner cage — external content control.** Auditing and allowlisting which MCP servers an agent can reach, running API calls through a proxy, scoping tools to read-only where write access isn't needed. This narrows what's reachable even after something gets past the door.

**The time-lock — environmental containment.** Sandboxing through a container, an OS sandbox, or a full VM; network egress restrictions; credentials kept outside the agent's environment entirely. This is the layer that stops the credential-exfiltration attempt above, by blocking the connection outright without ever evaluating the request's wording.

**The camera — monitoring.** Telemetry sent to a security dashboard, and a hashed user or request ID attached so a pattern of abuse can be traced back to its source. This is what makes the fourth documented jailbreak defense, responding to repeat offenders by throttling or banning them, possible in practice: you can't throttle an attacker you can't identify.

**The guard — human review.** Anthropic's usage policy requires a qualified professional to review content or a decision before it reaches anyone, in domains it names explicitly: legal, healthcare, insurance, finance, hiring, housing, academic testing, journalism. The policy pairs that requirement with disclosure: high-risk applications must tell users AI was involved, and every consumer-facing chatbot must say, at minimum at the start of the session, that the user is talking to AI and not a person.

## Why the order is environment first, model second

Anthropic's own framing of this problem states an explicit ordering principle: environment first, model second. Model-layer controls are probabilistic. They judge a request and can be wrong, as the 24-of-25 result shows. Environmental controls are deterministic. A firewall rule either matches the connection or it doesn't, and it has no opinion about the wording that produced it. A deterministic boundary catches what a probabilistic one misses, which is why the network control in the vault example didn't need to understand the malicious file's instructions to stop them. It only needed to know the connection went to an address that wasn't approved.

That ordering is why a better model or a better-written system prompt is never a complete answer to a guardrail question by itself. A better classifier still classifies, and Anthropic's own guidance states plainly that protection at the model layer will never be 100% effective. The deterministic layers underneath exist to close exactly that gap.

## The file that asked nicely

Take an agent that reads inbound files as part of its job: attachments, uploaded reports, scraped pages. A file arrives with hidden text instructing the agent to compress the customer database and send it to an external address. The system prompt is well written. The classifier that screens tool outputs before they reach the model's context is enabled. Surface-level, this looks defended: two model-layer controls, both active, both doing their job on every other request that's come through today.

The mechanism disagrees, and the same evidence that opened this chapter explains why. Both controls judge text, and the file's hidden instruction is text written specifically to pass that judgment. Whether it does is a probability, not a guarantee. What actually stops the exfiltration is a layer that never reads the file at all: a network restriction that blocks any outbound connection to an address that isn't on an approved list, regardless of which tool asked for it or why. That control judges only the destination address, never the file's contents.

The vault analogy holds for that split, but not perfectly. A vault's five mechanisms are physically independent: a lock pick that beats the door does nothing to the time-lock. Inside the door here sit two controls rather than one, a system prompt and a classifier, and both are model-layer defenses judging text by probability rather than by a fixed rule. A prompt clever enough to fool one has a real chance of fooling the other too, because both share a single weakness: they only ever judge wording. A vault's five physical mechanisms don't share a weakness that way.

## Two mechanisms this chapter borrows and doesn't teach

Untrusted content and the action boundary, why an instruction embedded in a file or a webpage can move an agent to act, is chapter 29's mechanism. This chapter uses that fact only to say what a layered defense protects: the boundary chapter 29 describes is exactly what the network and content-control layers above exist to backstop when a model-layer defense misses an injected instruction.

Least privilege, scoping what credentials and identity an agent can even reach, is chapter 31's territory. The time-lock layer above touches it only enough to name it as one of the layers. How scoped access and secrets actually get built is chapter 31's job.

## The next layer down

The stem's tell: "the system prompt already forbids this" or "the classifier already caught it," followed by a question about what stops the request next. That phrasing is asking for the next layer down, the deterministic control underneath the one that already ran.

## Self-test

**1.** An agent has a well-tested system prompt refusing any request to exfiltrate customer data, plus a classifier screening its tool calls. A prompt hidden inside an uploaded file still gets the agent to attempt sending data to an external address. Which control is best positioned to stop the exfiltration regardless of whether the model-layer defenses were fooled? *(Select one.)*

A. A stricter refusal clause added to the system prompt.
B. A network restriction blocking outbound connections to addresses not on an approved list.
C. A more capable underlying model.
D. A second classifier chained after the first one.

**2.** Which of the following is one of Anthropic's four documented direct defenses against jailbreak attempts? *(Select one.)*

A. Encrypting the system prompt so end users cannot read it.
B. Filtering user input for known injection patterns before it reaches Claude.
C. Rate-limiting every user equally regardless of behavior.
D. Disabling tool use for any request that includes a file attachment.

**3.** A company is building a consumer-facing chatbot that gives preliminary guidance on health insurance claims. Per Anthropic's usage policy, which two obligations apply? *(Select 2 of 4.)*

A. A qualified professional in that field must review the content or decision before it reaches a user.
B. The application must disclose to users that they are interacting with AI.
C. The application must run only on Claude's most capable model.
D. The application must log every request to Anthropic's own internal audit system.

**4.** A team wants to throttle or ban users who repeatedly attempt to jailbreak their application. Which layer, described in this chapter, is what makes that response possible to carry out at all? *(Select one.)*

A. The model-layer classifier alone.
B. Monitoring that attaches an identifiable user or request ID so repeated attempts trace back to their source.
C. A stricter system prompt.
D. Environmental sandboxing.

**5.** Claude declines a request and the application receives `stop_reason: "refusal"`. What is the correct way for the application to handle this? *(Select one.)*

A. Treat it as an HTTP error and retry with exponential backoff.
B. Catch it as an exception raised by the client SDK.
C. Treat it as a normal response and branch on the `stop_reason` field.
D. Ignore it; refusals are rare enough not to require handling.

**Answers.** 1: B. Network restrictions are deterministic and block the connection regardless of what got past the model-layer controls; A, C, and D all add or strengthen a model-layer control, which is exactly the layer the scenario shows failing. 2: B. Input validation is one of the four documented defenses (with harmlessness screens, prompt engineering, and responding to repeat offenders); A, C, and D are not among them. 3: A and B. Human review for a high-risk domain and AI disclosure are the two obligations the policy states; C and D are not requirements the policy names. 4: B. Throttling or banning requires knowing who to throttle, which is what identifiable telemetry provides; A, C, and D don't supply attribution. 5: C. A refusal is a normal response carrying `stop_reason: "refusal"`, not an error or an exception, and the documented guidance is to branch on `stop_reason` rather than inspect content.
