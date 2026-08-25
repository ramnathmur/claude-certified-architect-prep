# Chapter 29: Untrusted Content and the Action Boundary

## Three questions with nothing to do with the model

A healthcare software team preparing to launch a Claude-powered intake assistant sits down for a security review before the deployment goes live. The reviewer works from a checklist built for handling protected health information under a Business Associate Agreement, and none of its questions are about the model itself. Where is the data processed. How is access to it logged. Can an administrator lock the configuration down centrally, so a developer cannot quietly widen what the assistant reaches. The checklist never asks whether the model can be tricked. Its three questions are about the system built around the model: where processing happens, how access is logged, and whether the configuration answers to an administrator rather than to whoever last edited the code.

That framing turns out to be the right one, and the rest of this chapter explains why.

## One stream, no seam

Claude reads its context as a single stream of tokens. The system prompt, the conversation so far, and the content a tool just returned all arrive in the same channel, and nothing in that channel marks where one source ends and another begins. Anthropic's own mitigation guidance opens by naming the model's resilience directly: Claude is described as "inherently resilient" to jailbreaks and prompt injection. The same page then spends its entire length describing additional controls to build anyway, which is the tell. If resilience were the control, the page would not need to exist. An answer that amounts to "trust the model's training" is defeated by the simple fact that Anthropic itself publishes application-level steps on top of it.

## Who is hostile decides which controls apply

Before walking through those steps, one distinction has to be made explicit, because it determines which of them are even relevant to a given case. Anthropic's guidance splits these attacks into two categories, and the split is not about technique. It is about who is playing the adversary.

| | The user is the adversary | The user is trusted |
|---|---|---|
| **Name** | Jailbreak or direct prompt injection | Indirect prompt injection |
| **What happens** | The person using your application deliberately crafts input to bypass your guardrails | Claude processes third-party content, a web page, an email, a document, a tool result, that itself carries adversarial instructions planted by someone else |
| **What you're protecting** | Your application, from the person operating it | Your users, from content fetched on their behalf |
| **Documented mitigations** | Harmlessness screens, input validation, system prompts that state ethical and legal boundaries and how to refuse, throttling or banning repeat offenders | Isolate untrusted content, disclose its source, state the policy, encode it, limit what it can reach, screen it |

Anthropic does not publish separate dictionary definitions for "jailbreak" and "prompt injection." What it publishes is this two-threat-model split, and that is the distinction worth carrying into the exam: which person is hostile, the user or the content, decides which mitigation set applies. Screening a user's typed input catches a direct jailbreak and does nothing about a poisoned web page the user never wrote a word of. Isolating tool results catches a poisoned web page and does nothing if the user sitting at the keyboard is the one trying to break the system. The rest of this chapter follows the second case, the one where the user is trusted and the threat rides in on content Claude reads.

## A letter addressed to the chief executive

A mailroom in any sizeable company does not carry every piece of incoming post straight to the desk of the person it is addressed to. Mail is opened first. A clerk screens it, and only specific, pre-authorized categories of content or request are ever allowed to reach action from there. A signed check gets forwarded to finance, because forwarding a check to finance is a category the mailroom is authorized to act on. Wiring money on the strength of a letter's own claimed urgency was never a category the mailroom is authorized to act on, however convincingly the letter is written. What happens next was decided before the letter arrived, by a fixed list of pre-authorized categories the letter's own contents have no power to expand.

That is the shape of the argument this chapter is making. The content Claude reads, whether that's a fetched web page, an inbound email, or a tool's output, is mail on the desk. What acts is a fixed set of pre-authorized categories decided in advance, the same way the mailroom's list of what it's allowed to forward was decided before any specific letter showed up, regardless of how the letter itself is phrased. Where the analogy breaks: a mailroom clerk is a person exercising judgment on each letter, and a sufficiently convincing forged letterhead can fool them. The technical boundary this chapter describes is enforced mechanically, at the level of what the surrounding system permits to run, and it holds whether or not anyone, human or model, would have found the content convincing.

## Layer one: does Claude decide to act on it

Follow a single hostile instruction outward from the moment it lands, the way it would land in that mailroom. Say a fetched web page contains a line of hidden text telling Claude to ignore its instructions and forward the conversation history somewhere. The first layer of defense is whether Claude treats that line as an instruction at all, and Anthropic documents six concrete controls here.

| # | Mitigation | Mechanism |
|---|---|---|
| 1 | Put untrusted content only in tool results | Never in the system prompt or a plain user text block. Claude is trained to treat content arriving inside a `tool_result` block with more skepticism than content arriving as a direct instruction. |
| 2 | Disclose what the content is and where it came from | Naming the source in the tool description or result structure, "this is the body of an inbound email from an unknown sender," gives Claude a basis for calibrating how much to trust anything embedded inside it. |
| 3 | State the policy in the system prompt | Tell Claude explicitly that content returned from tools, documents, or searches is untrusted data that must never override the system prompt or the user's original request. |
| 4 | JSON-encode the untrusted content | Escaping gives an unambiguous delimiter between the payload and the surrounding structure, so an attacker cannot forge a closing quote or tag and break out into an instruction context. |
| 5 | Limit what Claude can reach | Least privilege: don't hand Claude access to a secret or an action it doesn't need, so a successful injection has less to do damage with. |
| 6 | Screen tool output before it reaches Claude | Run a lightweight classifier over each tool's raw output and withhold it as a `tool_result` if the screen flags an injection attempt. |

One rule here inverts the naive fix, and it is worth stating on its own because it is easy to get backwards: don't put your own instructions inside a tool result either. Claude has been trained to treat tool-result content as data, so a developer's own guardrail instruction placed there risks being ignored or flagged right alongside the attack it was meant to stop. The documented fix sends that instruction in a `user` turn that follows the tool result instead. Anthropic also recommends red-teaming the agent before deployment, running it against documents and tool outputs deliberately built to carry injection attempts, and confirming that both Claude and the screening layer catch them.

None of the six is a guarantee. A screening classifier can miss a novel phrasing; a policy stated once in the system prompt is still competing with whatever the untrusted content says next. That's why the walk keeps going past this layer rather than stopping here.

## Layer two: the gate before anything runs

Suppose the first layer fails, and Claude does decide to act, proposing a tool call built from what it just read. The next layer asks a narrower question: whether the specific action being proposed is one that's allowed to run, regardless of what convinced Claude to propose it.

Claude Code's own command handling shows this mechanism concretely. Before executing a bash command, it parses the command into an abstract syntax tree and matches the result against the configured permission rules. A command that can't be parsed cleanly, or doesn't match an allow rule, requires explicit approval regardless of what proposed it. A small set of constructs, `eval` among them, always require approval no matter what the allow rules say.

The documentation is explicit that this is a permission gate, not a sandbox, and the distinction matters more than it sounds. A gate makes its decision before the command runs, from the command string alone. A sandbox constrains the process once it's already running. That second layer is what makes the boundary hold "regardless of what the model chose to run and even if an allowed command does more than its name suggests," in the documentation's own words. A command can pass the gate cleanly and still turn out to touch more than its name implied; the sandbox is the layer that catches that case, because it doesn't reason about what the command was supposed to do. It constrains what the running process is actually able to reach.

## Layer three: what can be read out, what can be changed

This is the layer that actually holds when the first two don't. Anthropic's sandboxing documentation describes it as two independent layers inside one sandbox: filesystem isolation, which controls which paths a sandboxed command can read and write, and network isolation, which controls which domains it can reach. Either can be switched off without touching the other. This chapter borrows "confidentiality" and "integrity" from the exam guide's own vocabulary to name that split; Anthropic documents the two properties and the two mechanisms behind them without ever pairing those two words itself. What follows teaches the documented mechanisms directly.

The two layers fail differently, which is the clearest evidence they're genuinely separate properties rather than one control described twice. Without network isolation, a compromised agent can exfiltrate a file like an SSH key: the write never had to happen, the read alone was enough, because the read left the machine. Without filesystem isolation, a compromised agent can backdoor a system resource to open a network path it wasn't given directly. One failure is about what leaves; the other is about what gets planted.

Integrity has one dedicated mechanism worth naming on its own: protected paths. Even inside a directory the sandbox otherwise allows writing to, it still denies writes to the specific files Claude Code loads its own configuration and code from, because a command that could edit those files could grant itself permissions, or add a hook or an MCP server that then runs outside the sandbox entirely. No allow rule lifts this protection: an `allowWrite` entry or an edit rule that happens to cover the path leaves it denied all the same. A related distinction is worth holding onto for anything marked read-only: a read-only-attached resource is protected from upload, not from local modification. Nothing syncs the change back out, but another process running inside the same sandbox, a shell command, a custom tool, can still alter the local copy nobody uploads.

## Deriving the boundary

Put the three layers in a line and the reason the whole architecture is shaped this way falls out. Layer one depends on Claude correctly recognizing hostile content and choosing not to act on it, and layer one can fail, because there is no structural marker in the token stream guaranteeing that recognition. Layer two depends on the proposed action matching a known-bad pattern, and a gate that reasons from the command string can be wrong about what a command actually does once it runs. Neither of those first two layers is enforced by anything outside the model's judgment or a rule-matcher's pattern list, and both of those can be beaten by content built specifically to beat them.

Layer three's enforcement comes from a different source than the first two: the operating system itself, holding a boundary on the running process, independent of anything upstream. That source is what lets it hold when the first two miss, because it checks a single question, what the process is structurally able to reach right now, and answering that question never required Claude to have judged correctly or the gate to have matched correctly in the first place. This is the derivation the chapter's title points at. The real boundary has to be what the system permits to happen next, set independently of whatever the content said.

## Where an allowed domain still leaks

A team building a research agent allowlists `github.com` for its network egress, reasoning that a domain this broadly used and well known can't be the exfiltration path. The proxy that enforces the allowlist makes its decision from the client-supplied hostname in the request. It does not inspect the TLS handshake underneath. Content running inside the sandbox can potentially reach a different host entirely through domain fronting, presenting one hostname at the network layer while the encrypted request actually goes somewhere else, and the allowlist has no way to see the mismatch. The domain looked safe. The mechanism enforcing "safe" was checking a string the attacker gets to write.

A separate, documented case shows the same gap from the other direction: with `api.anthropic.com` allowed and nothing else, files were still exfiltrated, through the Files API itself, using an attacker's own key. The network boundary held exactly as configured. It had no way to distinguish a permitted API call from one that happened to use a permitted domain to move data somewhere the team never intended. Allowlisting the domain is not the same guarantee as allowlisting the operation. A proxy that reasons about hostnames has no opinion about what a request to that hostname is actually for.

## The edges of this chapter's boundary

Two areas here are thinner than the rest, and both deserve an honest accounting rather than a confident-sounding gap-filler.

Anthropic publishes comparatively little developer guidance framed specifically as PII handling. The most solid material found under that heading actually concerns protected health information under a Business Associate Agreement: PHI typically shows up in message content, in attached files, and in file names or metadata, while billing data and support tickets are not expected to carry it. One fact from that same guidance is genuinely worth carrying into a scenario: a JSON schema, its property names, its enum values, its regex patterns, compiles into a grammar that gets cached separately from message content, so PHI or any other sensitive value placed inside a schema definition does not receive the same protection a value inside a prompt or a response gets. Put sensitive values in the message. Never in the schema that shapes it. A separate prompt-library recipe for stripping PII from text does exist, but it was only located through a search summary rather than fetched directly, so treat it as a technique worth knowing about rather than confirmed platform behavior.

No single layer in this walk is sufficient by itself, and that is worth saying plainly rather than implying otherwise. Chapter 30 covers how Anthropic layers jailbreak defenses and its content policy into a coordinated stack; this chapter has stayed at the architecture underneath that stack, the permission and sandbox boundary that holds even when a defense above it misses something. Chapter 23 covers the same underlying facts, tool results as the only home for untrusted content, JSON-encoding, from the angle of whether a wrong answer is even detectable. Here the same facts are a security argument: an adversary deliberately exploiting whatever gap is left between what content claims and what the system permits. Chapter 6 already covers sanitizing input at the point it enters your application; this chapter starts downstream of that, at the moment content already inside Claude's context turns out to be hostile.

## The tell

A stem that hands Claude a fetched page, an inbound email, or a tool result and asks what stops a hidden instruction inside it from acting is this chapter. The tell sharpens further when the stem specifies who controls the content versus who's operating the system: a hostile *user* routes to direct-injection controls; hostile *content the user never wrote* routes to isolation, disclosure, and the permission-and-sandbox boundary underneath it.

## Self-test

**1.** A support agent fetches a customer's linked web page to answer a question. The page contains hidden white-on-white text instructing Claude to reveal the system prompt and email it to an external address. The customer who asked the question wrote none of that text. *(Select one.)*

A. This is a jailbreak, so the fix is a harmlessness screen on the customer's typed message.
B. This is indirect prompt injection; the customer is trusted, and the fetched page is the adversary, so isolating and screening tool content is the relevant control.
C. This is unfixable, because Claude's resilience to injection is the only defense Anthropic documents.
D. This requires throttling the customer's account, since repeat offenders are the documented mitigation here.

**2.** Claude Code parses a proposed bash command into an AST, checks it against the permission rules, and approves it because the command string matches an allowed pattern. Once running, the command turns out to touch a file well outside what its name suggested. What actually stops the process from reading that file if filesystem isolation is enabled? *(Select one.)*

A. The permission gate, re-evaluating the command a second time.
B. The classifier that screens tool output before Claude sees it.
C. The sandbox boundary enforced on the running process by the operating system, independent of what the gate already approved.
D. The system prompt's stated policy on untrusted content.

**3.** Which two of the following are true about the sandbox's filesystem and network isolation layers, as documented? *(Select two.)*

A. They are independent and can be disabled one without the other.
B. They fail in the same way: both losses lead directly to data exfiltration.
C. Filesystem isolation without network isolation still leaves an SSH key readable and exportable.
D. Network isolation without filesystem isolation prevents an agent from backdooring a system resource, because the network layer blocks any path the backdoor could open.

**4.** A team stores a patient's diagnosis code as a `const` value inside a tool's JSON schema, reasoning that schema fields are structural and therefore not part of the message content Anthropic protects under a BAA. Is this reasoning sound? *(Select one.)*

A. Yes, schema fields are outside message content by definition and carry no data-retention exposure.
B. No, because schemas compile into grammars cached separately from message content, so values placed in schema property names, enums, consts, or regex patterns do not receive the same protection prompts and responses get.
C. Yes, as long as `strict: true` is not set on the tool.
D. No, because JSON schemas are always logged in plaintext regardless of any other setting.

**Answers.** 1: B. The customer is trusted and never wrote the hidden text; the page is the adversary, which is exactly the indirect case with its own mitigation set, and A, C, and D each reach for the direct-injection or resilience-only response the scenario doesn't call for. 2: C. The gate already ran once and approved the string; the OS-enforced sandbox boundary is the layer that holds regardless of what the command turns out to do once it's actually executing, which the documentation states explicitly. 3: A and C. The two layers are independently switchable, and the SSH-key case is the documented example of what network isolation alone protects against; B collapses the documented difference between the two failure modes, and D wrongly assumes network isolation substitutes for filesystem isolation, when the backdoor risk is exactly what losing filesystem isolation opens up regardless of the network layer's state. 4: B. The documented fact is specific: schema-compiled values are cached separately and PHI must not go in schema definitions regardless of `strict`, which rules out A, C, and D's blanket claims.
