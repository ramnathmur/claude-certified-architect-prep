# Chapter 4: What is actually on the wire

## The letter leaves the building

Seal an envelope, address it, and hand it to a courier. Nothing happens to the paper inside until someone at the other end opens it. Everything in between is the courier's problem: which van, which route, which rules about what may cross which border.

Your code does the same thing every time it calls Claude. An architect building a contract-review assistant writes one call: send the clause under review and an instruction to flag anything that conflicts with the firm's standard terms, get a judgment back. That call reads like a function running inside the same program as everything else.

It isn't.

Somewhere between the keystroke and the answer, the request left the building, in the same physical sense as the letter, and someone else's infrastructure carried it. This chapter follows that one request out and back, then follows what happens when the firm's compliance team insists it travel by a specific courier.

## What a request actually is

Strip away the SDK and here is what your call becomes: an HTTP request, addressed to one endpoint, carrying one JSON body, going out over the same internet connection as everything else your machine does. That connection runs over the same encrypted transport, TLS, as any other sensitive web traffic. There is no special protocol to open a port for and no private network to negotiate. The endpoint names a resource: `/v1/messages` means create a message. The verb is POST, because you are asking the server to create something. That is REST, at the level that matters here: a resource named by an address, an action named by the verb.

The body is the letter. JSON is the language it is written in, because JSON is a format both sides parse the same way regardless of what language wrote it or what language reads it. The body carries the model you want, the conversation so far, and whatever limits you are placing on the answer. None of that content depends on which language your code is written in, and none of it depends, yet, on who is going to carry it.

Around the body sit the headers, and the headers are the envelope. One header names the contract version, because the shape of the JSON body is itself a versioned agreement between you and whoever reads it. That header exists so Anthropic can change the shape of the contract over time without breaking requests already written against an older shape: send an older version marker and the API keeps honoring it. Another header carries your credential, proof that whoever holds it is allowed to hand this specific letter to this specific counter. Change the credential and the letter is unchanged. Only who is allowed to send it has changed.

Send the request and a response comes back the same way: a JSON body describing what Claude produced, wrapped in headers describing what happened to the request itself. An HTTP status code reports that outcome before the body is even worth reading: success, a mistake in how the request was built, or a failure on the server's side. A body that looks like well-formed JSON can still be reporting an error rather than an answer, which is why the status code gets read first.

The whole exchange is one round trip, out and back. Every SDK in every language does the same four things underneath: build the body, attach the headers, send the request, and turn the JSON that comes back into objects your code can use without parsing text by hand.

That is what the SDK is: a convenience layer that does the letter-writing and the counter work for you. It validates the body before it leaves your machine, so a malformed request fails locally instead of over the wire. It retries a request that failed for a reason worth retrying. It hands back a typed object instead of a block of text you would otherwise parse yourself. Every one of those functions could be written directly against the same endpoint, in the same JSON, by someone willing to do it by hand. The SDK saves you the labor of exercising a capability the raw request already had.

Anthropic ships that wrapper across common application languages: Python, TypeScript, Java, Go, C#, PHP, Ruby. Whichever one your application is written in, the method that sends a message does the same four things underneath. The differences between the SDKs are differences of language idiom. What gets sent over the wire does not change with the language that built it.

The reason this matters here is the next step. The letter does not have to go to Anthropic's own counter. Amazon, Google, and Microsoft each host the same Claude models on infrastructure they operate, under rules they each set for their own counter. Same letter. A different counter, a different ID check, different rules about what that counter will carry.

## The same letter, three counters

Look at the three that Anthropic documents by name: Amazon Bedrock, Google Cloud, and Microsoft Foundry. Each runs Claude on its own infrastructure, under a licensing arrangement with Anthropic, and each expects the letter addressed and signed its own way.

On Amazon Bedrock, the address changes to an AWS endpoint, and the ID check changes with it. Instead of an Anthropic API key, the request is signed with AWS credentials: a service role, a temporary session issued by AWS's own identity service, or a short-lived bearer token, depending on how tightly the customer's security team wants to hold it. The model name changes shape too. `claude-opus-5` at Anthropic's own counter becomes `anthropic.claude-opus-5` at Amazon's, because Amazon prefixes every model it hosts with the name of the vendor who built it, the way a shared warehouse labels shelves by supplier.

On Google Cloud, the ID check moves to Google's own credential chain, the kind of authentication many applications already running on that platform use. The address changes in a smaller but real way: the model name moves out of the letter's body and into the address itself, part of the URL the request is sent to, and the version marker moves from a header into a field inside the body. The letter's content is functionally identical. What moves is where two of its details sit.

On Microsoft Foundry, the request is authenticated either with an Azure-issued key or with a Microsoft Entra ID token, and the model is addressed by a deployment name chosen at setup, which defaults to the model's own name but does not have to match it. Foundry offers a further choice: the same model can run on Anthropic's own infrastructure or on Azure's, as two separate deployments of the same catalogue entry, and which one is picked changes which features are available on that specific deployment. Its billing follows the same pattern of borrowed infrastructure: charges run through the customer's existing Azure Marketplace account rather than a separate invoice from Anthropic, which is often the whole reason a firm already committed to Azure chooses this counter at all.

None of the three counters asks you to rewrite the letter itself. All three still accept the same kind of JSON body, describing the same conversation, asking for the same kind of judgment back. What each one insists on is its own proof of identity and its own address, because each counter is operated by a different company, running its own infrastructure, under its own rules for who is allowed to use it.

That is also where the three counters stop being interchangeable. Each one publishes, separately, which parts of what Anthropic ships it actually carries. Fast mode, the higher-throughput setting from the previous chapter, is a working example: it is a Claude-API-only offering, absent from all three partner counters at the time of writing. A feature available at Anthropic's own counter is not guaranteed at every partner counter. The guarantee has to be checked per feature, per platform, regardless of how identical the letter format looks on the surface.

None of this is theoretical plumbing. A firm chooses a counter for reasons that have nothing to do with which one is technically superior. Its cloud spend is already committed to one provider, and routing new charges through the same contract clears procurement faster than opening a new vendor relationship. Its data must stay inside a network boundary its own security team already audits, a boundary drawn around AWS, or Azure, or Google Cloud. The letter's content rarely changes for any of these reasons. Which counter carries it does.

Region control follows a similar logic. Each counter offers a globally-routed request, answered from whichever of its data centers is available, alongside a region-pinned request, answered only from a location the counter guarantees in advance. Anthropic's own direct API does not currently offer that pin for every jurisdiction a regulator might name. A firm that must keep inference inside the European Union gets that guarantee through a partner counter's regional endpoint instead.

## What changes when a different counter takes the letter

Pull the rule out of what the three counters actually do, one step at a time.

Start from what a request needs to arrive anywhere at all: an address, and proof that the sender is allowed to use it. Every one of the three counters supplies both, but neither one is Anthropic's to set once a partner operates the infrastructure. AWS decides what counts as valid proof of identity on AWS. Google decides it on Google Cloud. Microsoft decides it on Azure. Authentication changes with the counter by necessity, because identity is a property of whoever operates the infrastructure the request travels through.

The model's name is a resource identifier, and a resource identifier belongs to whoever publishes the catalogue. Anthropic's own counter names its models one way. A partner republishing those same models into its own catalogue is free to name the shelf however its own system expects, which is why Amazon prefixes it, Google moves it into the address, and Microsoft lets the customer rename it entirely. The catalogue changed hands. The model underneath it did not.

Follow the same logic one step further, to how long a route stays open. A model's retirement date is an operational decision made by whoever runs the infrastructure that model sits on. Where Anthropic operates the infrastructure directly, Anthropic sets that date. Where a partner operates it, the partner does, on its own timeline, because retiring a model is a decision about capacity and support on infrastructure Anthropic no longer directly controls once it has been licensed out. Anything that is a property of who operates the infrastructure is set by that operator, and a model's retirement schedule is exactly that kind of property.

What does not follow that logic is the letter's own content. The Messages API contract, the JSON body describing the conversation, is the product Anthropic licenses to each counter. No counter is free to redesign it. That is why the same request, in the same shape, works at all three, once it is addressed and signed correctly.

One more thing stays fixed across every counter: how a response accounts for what it cost. The usage figures attached to a response are reported the same way regardless of which counter produced them, so a cost model built against the direct API's token accounting carries over to a partner counter without rebuilding it.

The working rule: which counter carries a request is a configuration decision, absorbed by choosing which flavor of the SDK's client to instantiate, for exactly as long as every capability the application depends on is one that counter actually carries. In practice that is a handful of lines: the same language's SDK ships a distinct client class for each counter, one for Bedrock, one for Google Cloud, one for Foundry, each building the same kind of request against a different address with a different credential scheme. The moment the application depends on something a given counter does not carry, the decision stops being configuration and starts being a redesign.

## When the schedule isn't Anthropic's to keep

Here is where the surface reading and the mechanism disagree, and the mechanism wins.

The same architect from the opening case ships two deployments of the contract-review assistant: one calling Claude directly, for the firm's general work, and one routed through Amazon Bedrock, because the litigation team's engagement runs entirely inside an AWS environment their client has already approved. Both deployments call the same model. The architect reasons that a single model, running the same weights, has a single retirement date, and checks Anthropic's own model-deprecation page to confirm it. The page lists the model as active, with no retirement date set. He reports both deployments as safe and moves on.

Weeks later, the Bedrock-routed deployment starts failing. The direct deployment keeps working without incident.

The surface reading treated "active" as a fact about the model. It is a fact about whoever is answering the question, and Anthropic's own page only answers it for the infrastructure Anthropic itself operates. Amazon Bedrock and Google Cloud are documented, explicitly, as partner-operated: each one sets its own retirement schedule for the models it hosts, on its own timeline, and that schedule can fall earlier or later than Anthropic's. The architect checked a real, authoritative page. It was the wrong authority for that specific deployment, because the deployment in question was never running on infrastructure that page describes.

Nothing in the application code pointed at the cause. The request that failed used the same model name in spirit, the same JSON body, the same conversation-handling logic as the one still working on the direct deployment, because that logic was never vendor-specific to begin with. The only difference was which counter had carried the letter, and that difference lived entirely outside the code the architect could see by reading his own repository.

The mechanism from the derivation applies without exception: a retirement date is set by whoever operates the infrastructure a given deployment actually runs on. For a deployment on the direct API, that is Anthropic's own deprecation page. For a deployment on Amazon Bedrock or Google Cloud, it is that platform's own documentation for the model in question, checked separately, because the two schedules are not guaranteed to move together.

The same trap catches feature availability too. A request that depends on a capability the direct API ships first can keep working on Anthropic's own infrastructure for months before a partner counter catches up, if it ever does.

The operational habit that follows is unglamorous: track retirement per deployment. A spreadsheet with one row per model name undercounts a firm running the same model through two counters. A spreadsheet with one row per deployment does not.

## Where the letter analogy stops carrying weight

Two edges to this chapter's picture, and one honest limit on the analogy itself.

The first edge is which SDK is in your hand. Everything above describes the plain Anthropic SDK, a wrapper around one request out and one response back. There is a second, different SDK, the Claude Agent SDK. It runs a whole agent loop inside your own process: many requests, tool execution between them, iteration until the task is done, closer to a standing correspondence than to the single letter this chapter has been following. The wrapper-around-one-request picture here is exactly right for the plain SDK. It stops being the right picture the moment your code is driving that loop instead of a single call. That is why the two ship as separate products rather than as two configurations of one library: a request built for a single round trip is a different kind of thing to design than a loop that keeps a session open across many of them. What the loop provides, and when to reach for it, belongs to a later chapter.

The second edge is shape. Every request in this chapter has been the simplest case: one call out, one response back, nothing streamed, nothing batched, nothing awaited across a longer job. That simplicity was deliberate, to keep the wire mechanism visible. Which shape a given request should take, and what changes when the answer needs to arrive in pieces or overnight, is a separate decision, covered next.

And the honest limit on the analogy itself. A real letter, handed to a different courier, arrives unchanged. That part does not survive contact with what actually happens on the wire. The address has to be rewritten for each counter, sometimes down to which field a single value sits in, and two counters carrying what looks like the identical letter can still be running different clocks on how long they intend to keep accepting it. The analogy earns its keep on the parts that genuinely hold: one letter, several counters, each with its own rules for identity and carriage. It does not stretch to cover a request arriving byte-for-byte identical wherever it is sent.

## Three phrases that route here

A stem naming an existing AWS, Azure, or Google Cloud commitment. A stem requiring data or inference to stay inside a named cloud's boundary. A stem where a request that used to work has started failing with no change to the code, on either the model side or the application side. Any of the three is the signal to check that platform's own documentation, not Anthropic's, before answering.

## Self-test: which carrier, which clock

**1.** A bank's procurement policy requires all new vendor spending to route through its existing AWS Enterprise Agreement, and its security team requires model inference to stay inside AWS's own network boundary. Select 1.

A. Call the Claude API directly, routed through the bank's own API gateway.
B. Call Claude through Amazon Bedrock, authenticated with the bank's existing AWS IAM roles.
C. Add a policy statement to the project's CLAUDE.md instructing that Claude may only be called through AWS.
D. Switch the application to the most capable Claude model, since larger AWS commitments come with better enterprise terms.

**Answer: B.** Bedrock runs on AWS-operated infrastructure and bills through the existing AWS relationship, satisfying both constraints at once. A is a client-side routing change; the request still leaves AWS's boundary to reach Anthropic's own infrastructure. C is an instruction that nothing in the system enforces. D addresses neither procurement nor the network boundary.

**2.** An application calls Claude through Google Cloud. A teammate checks Anthropic's own model-deprecation page, finds the model listed as active, and reports no action needed. Two months later, requests through Google Cloud begin failing, while a separate direct-API deployment of the same model keeps working. Select 1.

A. The model was never deprecated; the failures are unrelated.
B. Google Cloud, as the operator of that delivery route, sets its own retirement schedule for the models it hosts, separately from Anthropic's own schedule; the team should have checked Google Cloud's own documentation for that model.
C. The application's API key expired and needs rotating.
D. Add automatic retry with backoff so failed requests recover on their own.

**Answer: B.** Partner-operated platforms set their own retirement timelines, which can fall earlier or later than Anthropic's. Anthropic's deprecation page only answers the question for infrastructure Anthropic itself operates. C invents a failure mode the scenario does not support. D retries against a route that is failing for a structural reason, which no retry will fix.

**3.** Select the two statements that correctly describe how authentication changes when Claude is invoked through a third-party platform rather than the direct Anthropic API. Select 2.

A. On Amazon Bedrock, requests can be authenticated with AWS credentials, including temporary credentials issued through an assumed IAM role, instead of an Anthropic API key.
B. On Microsoft Foundry, requests can be authenticated with a Microsoft Entra ID token instead of an Anthropic API key.
C. All three third-party platforms accept the same Anthropic-issued API key used by the direct API.
D. No credential is required on any third-party platform, because the cloud account's own network boundary is sufficient.

**Answer: A, B.** Each platform substitutes its own identity system for Anthropic's API key: AWS credentials on Bedrock, Entra ID or an Azure key on Foundry. C and D both describe a credential-free or credential-portable world that none of the three platforms documents.

**4.** A team built a feature around the Claude API's structured outputs, a JSON-schema-constrained response. To consolidate cost under an existing cloud contract, they move the integration to Amazon Bedrock, changing only the SDK client class and the credentials. In testing, the feature stops returning schema-constrained JSON. Select 1.

A. A bug in the SDK silently dropped the schema parameter; retry the request.
B. Structured outputs is a capability the direct API supports that Amazon Bedrock does not carry; the application depended on a feature the new counter does not offer, so the change was not a pure configuration swap.
C. Bedrock requires a higher token ceiling for schema-constrained responses to return correctly.
D. Lower the model's effort level so the response is formatted more carefully.

**Answer: B.** Feature parity is not guaranteed across platforms, and structured outputs is documented as unavailable on Bedrock. A and C invent mechanisms neither platform documents. D reaches for a lever from a different decision entirely and does not restore a missing capability.

**5.** An architect is asked whether moving a Claude integration from the direct API to Google Cloud will require rewriting the application's conversation-handling logic. Select 1.

A. Yes: Google Cloud uses a request format that shares nothing with the Messages API.
B. No. The request is still built against the same Messages API contract. What changes is how it is addressed and authenticated.
C. It depends on whether the application uses a streaming response.
D. Yes: tool calling is only available through the direct API.

**Answer: B.** Google Cloud's integration is documented as using the same Messages API shape, with the model name and version marker moved to different parts of the request. A and D both overstate the difference. C raises a real but separate decision that does not bear on whether the vendor swap itself requires a rewrite.

## What will drift: platform specifics

Everything below is a detail that moves with a product update rather than a rule of judgment. Treat it as a snapshot taken while writing this chapter, worth a glance rather than memorization.

**The platforms named in this chapter, as currently documented:** Amazon Bedrock, Google Cloud (through its Agent Platform integration, commonly called Vertex AI), and Microsoft Foundry. A fourth option, Claude Platform on AWS, is Anthropic-operated despite running on AWS, bills through AWS Marketplace, and is documented separately from the AWS-operated Bedrock.

**Model identifier formats, as currently documented:** Amazon Bedrock prefixes every model with `anthropic.`, for example `anthropic.claude-opus-5`. Google Cloud's integration passes the model in the request URL rather than the JSON body, and its version marker is a body field fixed to the literal value `vertex-2023-10-16`. Microsoft Foundry addresses models by a deployment name that defaults to the model ID but can be renamed at provisioning time.

**Which platforms set their own deprecation schedule, as currently documented:** Amazon Bedrock and Google Cloud are named explicitly as partner-operated, with their own retirement timelines that can differ from Anthropic's. Microsoft Foundry is documented as following the Claude API's own lifecycle schedule, despite running partly on Azure infrastructure. Which company operates a given deployment sets its retirement clock, independent of which cloud that deployment happens to run on.

**Feature parity, as currently documented:** none of the three third-party platforms carries the Batch API, Claude Managed Agents, the Admin or Usage API endpoints, or the newest agent-infrastructure features such as Agent Skills, the MCP connector, and programmatic tool calling. Structured outputs and some server-side tools are available on some platforms and hosting options and not others; check the specific platform's current feature list before an application comes to depend on either.

Re-verify all of the above against each platform's own current documentation before treating any single line of it as settled.
