# Chapter 16: Who Runs the Loop

## A word that means four different things

Four engineers at the same company each say they "built an agent" last quarter. One wrote her own loop against the Messages API, deciding in her own code when to call a tool and when to stop. One built his on the Claude Agent SDK, a library running on his own server with Anthropic's loop logic inside it. One fired a request at Claude Managed Agents and let Anthropic run the whole thing on Anthropic's own infrastructure. One made that same Managed Agents call, except his company's security team required the tool calls themselves to execute inside the company's own network.

All four call it "an agent." The four builds share almost nothing: different code owns the loop, different infrastructure hosts it, and a different party is on the hook when something breaks. Choosing among them is an architecture decision, made once per project, and the exam expects it to be made by mechanism rather than by feel.

## Five ways to run a loop

Every option in this chapter answers one question differently: who owns the loop, the code deciding what happens next, and who owns the machine that loop runs on. Employment models sort the five options cleanly, because hiring asks exactly this question about a different kind of work: build it in-house, bring in someone else's process, or hand the whole job to a vendor.

Anthropic's own documentation frames the first four with a placement table:

| If you're... | Use | Why |
|---|---|---|
| Building an agent without implementing the tool loop yourself | Agent SDK | A library that runs the agent loop in your own process |
| Doing interactive development from a terminal | Claude Code CLI | The terminal interface, built for daily interactive use |
| Calling the API directly and implementing the tool loop yourself | Client SDK | Direct API access; you implement the tool loop |
| Running long-running agents without managing your own sandbox | Managed Agents | Anthropic runs the agent and the sandbox |

That table already answers the chapter's own title question for three of its rows. The fifth stop, splitting Managed Agents into a cloud form and a self-hosted form, is Anthropic's next distinction, and it's where this chapter puts most of its weight.

**The raw loop: you as employee.** Write your own loop against the Messages API and you own everything it touches: when to call a tool, when to stop, what state carries between calls. That's the Client SDK row above, and it's the employee model: full control, and every retry policy, every context-window check, every exit condition is a problem you solve, because nobody else owns any part of the loop. Chapter 17 covers how that loop actually gets built; this chapter only places it on the map.

**The Claude Agent SDK: an agency temp who already knows the building.** Hire the Agent SDK and you still run the process, on your own server and your own deployment. What's Anthropic's is the loop logic itself: the code that receives a prompt, calls a tool, evaluates the result, and decides whether to continue, packaged as a library for Python or TypeScript. It ships the same loop that runs Claude Code: receive the prompt with its system prompt, tool definitions, and history; evaluate and respond; execute any tool calls; repeat until a response carries no tool call; return the result. Anthropic calls one full pass through that cycle a turn, and a turn runs without handing control back to your code partway through. Read-only tools can run concurrently inside a turn; tools that modify state run one at a time to avoid stepping on each other. Beyond running that cycle, the SDK does four things a hand-written loop has to build for itself. Automatic compaction summarizes older conversation history once the context window fills, keeping recent exchanges and key decisions intact. One design consequence follows: a persistent rule belongs in CLAUDE.md rather than an early message, because CLAUDE.md content is re-injected on every request while a compacted message might not survive. A `max_turns` or `max_budget_usd` cap stops a loop that would otherwise run until Claude decides it's finished, useful once a task stops being well-scoped, and the budget cap covers any subagents the loop spawns too. Permission evaluation and hooks run inside your application process rather than inside the model's context window, so a hook that fires a hundred times costs no tokens. And sessions persist, resuming or forking with the full prior context restored rather than starting cold. Every one of those four sits on top of the raw loop as a capability the SDK adds; you're still the one deploying and operating the process it runs in.

**Provider-neutral frameworks: temps from other agencies.** Three more options occupy that exact same layer, a library running the loop inside your own process, without being Claude-specific. Each is a different opinion about what matters most once you're the one holding the contract.

Strands, built by AWS and already running production systems inside Amazon Q Developer, AWS Glue, and VPC Reachability Analyzer, bets on the model itself. Its documentation calls this a model-driven approach: the model dynamically directs its own steps and its own tool use, and Strands runs the surrounding loop without you writing orchestration logic or a parser for the model's output. It works with Amazon Bedrock, Anthropic Claude, Llama, Ollama, and other providers through LiteLLM. The project's own phrase for this is "any model, any cloud." It integrates with thousands of published MCP servers to use as tools and publishes its own Strands MCP server besides. It ships built-in multi-agent patterns, Agent-as-Tool and Swarm, for when one agent calls another, and it can run as a local client, behind an API on Lambda or Fargate, or split across separate agent and tool environments.

LangGraph, built by LangChain Inc but usable without LangChain, sits one layer below LangChain rather than beside it. LangChain's own docs describe it as the orchestration runtime handling durable execution, streaming, human-in-the-loop, and persistence. Its central abstraction is a graph of nodes and edges over shared state, and the capability that earns it a place here is that it lets you mix deterministic, hand-coded steps with LLM-driven agentic steps inside the same graph. Reach for it when the requirement is precise control over every part of the agent's behavior, plus durability across a failure and a human-in-the-loop interrupt at a specific point in the graph. LangChain's own docs route a team that just wants a higher-level abstraction, rather than that level of control, toward LangChain's prebuilt agent architectures instead.

PydanticAI, built by the team behind the Pydantic validation library that already underpins the OpenAI SDK, the Anthropic SDK, and FastAPI, bets on the contract rather than the control flow. It runs a typed agent loop where structured output is validated on every single run against a Pydantic model, tools and dependency injection are typed the same way, and swapping the underlying model is a one-line string change; provider support spans OpenAI, Anthropic, Google, Bedrock, Azure, and dozens more, either with individual keys or through a single gateway key with failover built in. Reach for it when what matters most is validated, typed output the downstream code can trust without checking, in a codebase that already speaks Pydantic or FastAPI, rather than fine-grained control over the steps in between.

**Claude Managed Agents, cloud: the managed service.** Managed Agents is a different product from the Agent SDK: a hosted REST API, not a library. Anthropic's own comparison draws the line plainly: the Messages API is for "custom agent loops and fine-grained control," Managed Agents is for "long-running tasks and asynchronous work." Four concepts organize it. An agent is the model, system prompt, tools, MCP servers, and skills. A session is one running instance of that agent. Events are the messages passed between your application and the agent. An environment is where sessions run, and that's where the hosting choice lives. In the cloud form, that's the managed-service hire in full: Anthropic runs the sandbox, the orchestration, and the model, and you consume events and results without operating any infrastructure at all. It suits work running minutes or hours across many tool calls, work needing a persistent filesystem and conversation history across a pause, or work running on a cron schedule.

**Claude Managed Agents, self-hosted: the franchise.** Self-hosting changes exactly one thing. Anthropic's own description of the self-hosted sandbox is precise about the boundary: it "keeps the orchestration on Anthropic's side but moves tool execution into infrastructure you control, so the agent's code, filesystem, and network egress never leave your environment." **The model, the agent loop, and the session state stay with Anthropic in both hosting modes. Only tool execution moves.**

| Aspect | Cloud (Anthropic-hosted) | Self-hosted |
|---|---|---|
| Tool execution | Anthropic's sandboxes | Your infrastructure |
| Agent orchestration | Anthropic | Anthropic |
| Claude model | Anthropic | Anthropic |
| Network egress | Anthropic's controls | Your network policy |

What you provide is a Linux host and an environment worker: a process that polls Anthropic's work queue, claims sessions assigned to your environment, downloads the agent's skills, executes the tool calls locally, and posts the results back. You're also responsible for the containerization, the network and egress policy, and the credentials the worker uses. Push the franchise analogy one step further and it breaks: a real franchisee decides staffing, hours, and day-to-day operating choices inside the franchisor's rules. Self-hosted Managed Agents gives you no equivalent decision-making: you don't decide when a tool runs or what happens after, you only execute the call the loop hands you and report the result back. In this metaphor, Anthropic's loop is the franchisor: it keeps sole authorship of the playbook, deciding which call happens next, while you run the storefront that carries it out.

One boundary catches people out even inside a self-hosted environment. Web search and web fetch always run on Anthropic's servers, whether the sandbox is cloud or self-hosted, and the environment's own networking settings govern only the sandbox's outbound traffic, not those two tools. Restricting what a web tool can reach takes a per-tool allow-list or block-list, separate from the network policy that governs everything else the worker touches.

## Why self-hosted still isn't "running the agent"

Follow the mechanism instead of the label. If orchestration and the model both stay with Anthropic in self-hosted mode, the only thing self-hosting can change is a decision that depends on where tool execution physically happens. That rules out latency: moving one component off-site while the model call itself still crosses the network to Anthropic changes little about round-trip time, and it never appears in Anthropic's own list of reasons to self-host. Cost points the same direction: self-hosting adds infrastructure you now operate, a worker process, a sandbox, an egress policy, all of it overhead you're newly responsible for.

What's left is exactly what depends on where tool execution runs: the data it touches, the services it reaches, and the controls it operates under. Anthropic states the fit condition in one sentence: self-hosting suits an agent that needs to operate on data that cannot leave your network boundary, reach internal services that are not publicly routable from the internet, or run under your organization's own compliance and audit controls. Three discriminators, and only these three. A stem naming any one of them points at self-hosted. A stem about speed or spend is naming something neither hosting mode is documented to change.

Two qualifications keep the picture honest. Tool inputs and outputs still flow to Anthropic's control plane in self-hosted mode too, because the model has to see a tool's result before it can decide what happens next. Isolation covers where the code executes; the round-trip that lets Claude read the answer still crosses to Anthropic either way. And because Managed Agents stores conversation history, sandbox state, and outputs server-side in both hosting modes, it currently qualifies for neither Zero Data Retention nor a HIPAA Business Associate Agreement, in cloud or self-hosted form alike. Self-hosting relocates where code runs; the data path through Anthropic and the compliance eligibility stay exactly where they were.

## The trap the word "self-hosted" sets

A payments team needs an agent that reconciles transactions against a database with no public endpoint, on a network their security team won't open to the internet. "We need this on our own infrastructure" sounds like a vote for the Agent SDK, the option most associated with running things yourself.

The mechanism says otherwise. What the team needs is tool execution reachable from inside their own network, while orchestration, the model, and session handling stay off their plate entirely. That's exactly the non-routable-services discriminator from the section above. Self-hosted Managed Agents gives them that directly: their environment worker runs inside the network the database lives on, and it can serve a custom tool that wraps the database's own internal API, claiming sessions, calling that tool, and posting results back while Anthropic keeps running the loop deciding when to call it. Building the Agent SDK path instead hands the team a second job nobody asked for, writing and operating the orchestration logic itself, to solve a problem that was only ever about where one step of tool execution could physically run.

The surface reading treats "our own infrastructure" as a request to own the whole build. The documented discriminator is narrower: which single layer, tool execution, needs to sit inside a boundary the team controls. Everything else about the agent can stay exactly where Anthropic already runs it.

The trap also runs the other direction. A team weighing cloud against self-hosted Managed Agents purely to shave a few hundred milliseconds off each tool call, or to trim the bill, is optimizing against neither of the documented discriminators, and it's taking on the worker-process overhead from the section above for nothing that overhead is documented to buy. A stem built around either pressure is testing habit against constraint: whether the reader reaches for self-hosted by reflex, or checks the scenario for one of the three discriminators first.

## The boundary of this audit

This chapter decides which of five options runs the loop; how any of them gets built is separate territory. Registering tools, scoping a system prompt, pairing a tool-use block with its result, and writing an exit condition are chapter 17's, once raw loop or Agent SDK has already been chosen as the shape. An earlier chapter named the Agent SDK only to contrast it against other API layers in passing; this is the chapter that actually teaches it.

Two more boundaries are worth naming so a stem doesn't get answered from the wrong place. Choosing between a built-in tool, a custom tool, a Skill, and an MCP server is a four-way comparison this chapter doesn't attempt. That's a decision about what a single tool call is, a different question from who runs the surrounding loop, and it belongs elsewhere in this course. And this chapter doesn't rank the three frameworks against each other on a general "which is best" axis; it places them by what each one optimizes for, and the exam tests the placement rather than a personal preference.

## Reading the stem

"Build your own tool loop" points at the raw loop or the Agent SDK. "Data can't leave our network," "reach an internal service," or "our own compliance controls" points at self-hosted Managed Agents: never latency, never cost. "Validated, typed output" points at PydanticAI. "Mix scripted and model-driven steps" points at LangGraph. "The model should decide its own steps" points at Strands.

## Self-test

**1.** A finance team's agent needs to read files from a server with no public IP address, unreachable from the internet, while everything else about the deployment (session handling, model calls, conversation history) can stay however Anthropic already runs it. *(MC — select one.)*

A. Claude Agent SDK, because the team needs to run the whole agent themselves.
B. Self-hosted Claude Managed Agents, because tool execution needs to reach a non-routable internal service.
C. Cloud (Anthropic-hosted) Managed Agents, because it's the fastest path to production.
D. A raw loop against the Messages API, for the lowest possible latency.

**2.** Which of the following are documented reasons to choose self-hosted Managed Agents over the cloud-hosted form? *(MR — select 2 of 4.)*

A. The agent needs to operate on data that cannot leave the company's network boundary.
B. Self-hosted sessions respond faster because tool calls skip a network hop.
C. The organization's own compliance and audit controls need to govern the session.
D. Self-hosted infrastructure costs less to operate than the cloud-hosted form.

**3.** A team wants an agent whose structured output is validated against a schema on every run, in a codebase already built on FastAPI conventions; orchestration control over each step isn't the priority. *(MC — select one.)*

A. LangGraph, for its graph-based control over every step.
B. Strands, for its model-driven loop.
C. PydanticAI, for its typed, validated output on every run.
D. The Claude Agent SDK, for its built-in permission system.

**4.** A team is comparing Claude Managed Agents' cloud and self-hosted environments. Which two statements correctly describe what stays the same between the two modes? *(MR — select 2 of 4.)*

A. The Claude model that runs the agent.
B. Where tool execution happens.
C. The agent orchestration loop.
D. The network egress policy the sandbox operates under.

**5.** A team wants an agent where the model itself dynamically directs which tool to call next, with no hand-written orchestration graph, and wants the code to stay portable across model providers rather than committing to one vendor. *(MC — select one.)*

A. LangGraph, because it offers precise control over every part of the agent's behavior.
B. Strands, because it runs a model-driven loop and works with multiple model providers.
C. The Claude Agent SDK, because it ships the same loop that runs Claude Code.
D. Cloud Managed Agents, because Anthropic operates the sandbox for you.

**Answers.** 1: B. The stated need, reaching a non-routable internal service, is one of the three documented discriminators for self-hosting; A mistakes "our own infrastructure" for owning the whole loop, and C and D solve a problem the scenario never raised. 2: A and C. Data residency and an organization's own compliance controls are two of the three documented discriminators named in the options; B and D name latency and cost, which the source material never lists as reasons to self-host. 3: C. Validated, typed output on every run in a Pydantic/FastAPI-shaped codebase is PydanticAI's stated fit; A and B optimize for control and model-driven flexibility respectively, and D solves a different problem. 4: A and C. The model and the orchestration loop stay with Anthropic in both modes; B and D name the two things self-hosting actually changes, tool execution and the network egress policy governing it, so they describe what changes between the two modes rather than what stays fixed. 5: B. A model-driven loop with no hand-written orchestration graph, kept portable across providers, is Strands's stated fit; A describes LangGraph's graph-based control, C ties the loop to Claude specifically rather than staying provider-neutral, and D hands the whole loop to Anthropic rather than answering the model-driven requirement at all.
