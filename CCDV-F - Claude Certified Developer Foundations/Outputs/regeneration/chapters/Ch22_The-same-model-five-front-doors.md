# Chapter 22: The Same Model, Five Front Doors

## The instruction that stopped traveling

A developer spends a week tuning a project's CLAUDE.md: a house style for commit messages, a rule about which test suite to run before committing, a note about which package manager the repo uses. In Claude Code, every session obeys it without being told twice. Confident the hard part is done, she pastes the same text into her company's claude.ai project, expecting the chat there to pick up the same habits. Nothing changes, because claude.ai was never reading a CLAUDE.md file in the first place. It keeps its own, separate place for standing instructions, and nobody wired the two together. A colleague hits the same wall from a different angle: he calls the Messages API directly from a Python script and gets generic answers, because the request he built never set a `system` field to anything. Same model, three different programs standing in front of it, three separate places an instruction has to be told to live.

## Five doors on one bank

Think of Claude the way you already think of a bank you hold an account with: one system underneath, one set of capabilities, one set of policies, reachable through several different doors that each understand an instruction differently. A teller at the branch reads a paragraph you hand over and acts on the specific details in it. An ATM understands only a fixed protocol: insert a card, fill in the exact fields it was built to accept, and it does precisely that and nothing else. A phone rep works from a script the bank wrote in advance, holds a real conversation, but has no hands on the machinery beyond what that script allows. The bank's own mobile app has several structured sections for different jobs, and one of those sections can quietly hand a customer to a different backend than the rest of the app uses. Behind all four sits a fifth thing that isn't a customer door at all: a toolkit the bank licenses out so another company can build its own product on the bank's own machinery.

Claude has an equivalent five. Claude Code is the branch, Claude Desktop is the app, claude.ai is the phone, the API is the ATM, and the SDKs are the toolkit a developer uses to build a door of their own. Which one a developer is using decides how an instruction actually gets in, and the rest of this chapter works through what a developer needs, one need at a time.

The analogy holds up to one point. A bank builds separate software for its branch and its app, maintained by separate teams. Claude Code's terminal, VS Code extension, and Desktop's own Code tab run the identical engine instead, invoked from three different places, something no real bank has ever done across two different doors.

### "I need it to read my codebase, run my tests, and edit files": Claude Code

Claude Code is the branch: the door with the most reach, the one your files, your terminal, and your git history are actually visible through. It runs on five surfaces of its own: the terminal (CLI), a VS Code extension, a JetBrains plugin, the Code tab inside Claude Desktop, and a web version at claude.ai/code. All five connect to the same underlying engine. A CLAUDE.md file, a settings.json entry, or an MCP server configured once works the same way no matter which of those five you're sitting in front of.

Instructions live in the same four places regardless of which surface you reach Claude Code through: a CLAUDE.md hierarchy (managed, user, project, and local versions, all additive), path-scoped rules under `.claude/rules/`, subagent system prompts under `.claude/agents/`, and enforced settings in `settings.json`. This door is built for developers working directly in a codebase, interactively at a terminal or IDE, or unattended through `-p` headless mode and CI. That last point is worth holding onto: if the requirement is "run this overnight, with nobody watching a screen," Claude Code's headless mode, or the Agent SDK covered further down, is the door built for it. Claude Desktop's Code tab, despite sharing most of this configuration, is not; the next section explains why.

### "I need a graphical app for diff review and parallel sessions": Claude Desktop

Claude Desktop is the app: a separate application with three tabs, Chat for plain conversation, Cowork for Dispatch and longer agentic work, and Code for software development. Only the Code tab runs the Claude Code engine described above, and it adds things the CLI has no equivalent for: visual diff review, drag-and-drop panes for chat, diff, browser, terminal, and file editor, parallel sessions with automatic git-worktree isolation, computer use with three access tiers (view-only for a browser, click-only for a terminal or IDE, full control elsewhere), an iOS Simulator pane, SSH sessions through a dialog, Dispatch-spawned sessions, PR CI-status monitoring, and scheduled tasks.

The Code tab shares its configuration with the CLI: the same CLAUDE.md and CLAUDE.local.md files, the same MCP servers from `~/.claude.json` and `.mcp.json`, the same hooks and skills, the same settings.json permission rules, the same models. What it drops is scripting. `--print` and the Agent SDK have no Desktop equivalent; neither does agent teams (a lead agent assigning work to teammates from a shared task list, CLI-only), `dontAsk` mode, inline autocomplete, or the `--allowedTools`/`--disallowedTools` flags. A bare `/permissions` reply that opens a terminal dialog in the CLI has nowhere to render inside the Code tab. If the requirement is "unattended, nobody watching a UI," this remains the wrong door however much of the CLI's own configuration it otherwise shares.

### "I need the same persona in every conversation, or documents this project can draw on": claude.ai

claude.ai is the phone: a live, natural-language conversation, guided by whatever standing script the organization set in advance, with no hands on a filesystem beyond what the conversation allows. It carries three separate, differently scoped mechanisms for standing instructions:

| Mechanism | Scope | Set where |
|---|---|---|
| "Instructions for Claude" | every conversation on the account | Account Settings |
| Project instructions | chats inside one specific project only | Inside that project |
| Project knowledge base | documents the project can draw on; not instructions | Uploaded to that project |

A support engineer who wants Claude to answer in the company's tone in every chat she opens sets the account-wide instructions once. A team running a single migration project wants Claude to know that project's schema and nothing else: project instructions, plus a knowledge base holding the actual schema files, which paid plans expand with a larger retrieval mode. One detail is worth being precise about: claude.ai/code is Claude Code's own web surface, not part of the Projects and chat product this section describes. It shares a domain with claude.ai and nothing else, running the coding engine from the previous section on the CLAUDE.md hierarchy instead of this section's three mechanisms. A stem that says "claude.ai" without the word "code" means this section; "claude.ai/code" or "the web version of Claude Code" means the previous one.

### "I need to call Claude from my own backend": the API

The API is the ATM: no rep to interpret the request, just a fixed protocol that does exactly what the form says and nothing else. The Messages API's `system` parameter is where a standing instruction lives for a raw API integration. It sits at the top level of the request, alongside `model`, `messages`, and `max_tokens`: there is no `"system"` role inside the `messages` array itself. Set it once in the code that builds the request, and the calling application includes it on every call, so the persona or the rules it states apply to every turn without being retyped into a user message.

This door is for developers building their own application, who write and own the tool-use loop themselves: deciding when a tool result comes back, what happens next, and when the exchange ends. That ownership is exactly what separates it from the SDKs below. If the requirement is "give Claude a standing role for this whole integration," the answer is the `system` parameter, set once in code and applied automatically to every request that follows.

### "I need to build my own agent, or call the API with less boilerplate": the SDKs

The SDKs are the toolkit behind all four doors rather than a fifth one: access to the bank's actual machinery for a developer who wants to build a product of their own. "SDK" is not one product. Anthropic's own comparison names four:

| If you're... | Use | Why |
|---|---|---|
| Building an agent without writing the tool loop yourself | Agent SDK | runs the agent loop in your own process, in Python or TypeScript |
| Doing interactive work from a terminal | Claude Code CLI | the terminal interface, built for daily interactive use |
| Calling the API directly and writing the tool loop yourself | Client SDK | direct access to the API; you implement the loop |
| Running a long-lived agent without hosting your own sandbox | Managed Agents | a hosted REST API; Anthropic runs the agent and the sandbox |

The Agent SDK is Claude Code packaged as a library: the same tools, agent loop, and context management, callable from a developer's own Python or TypeScript process. Its instructions load the same way Claude Code's do: skills, commands, and memory load automatically from a project's `.claude/` and from `~/.claude/`. One thing is layered on top: a programmatic surface for appending to or replacing the system prompt at the point where the agent is constructed in code, rather than in a file on disk.

The Client SDK is a different product: a thinner wrapper around the same Messages API described above, for a developer who wants the HTTP handling done for them but still intends to write the tool loop. Managed Agents is a fourth, separate product again: a hosted REST API where Anthropic runs both the agent and its sandbox, so a developer sends a task and gets a result without operating any infrastructure of their own. A scenario offering a custom Python agent with no hosting to manage, an API call with hand-rolled retries, a long-lived hosted agent with no sandbox to babysit, and one-off terminal help is drawing its four options from exactly this table.

## Why the same instruction needs five different homes

No general instruction system sits underneath the five doors above. Every request to Claude, from any door, is the same thing at the model level: text goes in, text comes back, and the model carries nothing forward from one call to the next. The differences in this chapter come from five separate pieces of software, each deciding, on the developer's behalf, what to attach to a request before it leaves and what to do with what comes back.

Claude Code's harness is a program that watches the filesystem, finds CLAUDE.md and settings.json and the files under `.claude/`, and folds their contents into the request before it reaches Claude. claude.ai runs a different program: it looks up the account's stored "Instructions for Claude" and the current project's stored instructions from its own database, and folds those in instead. The raw Messages API has no harness between the developer and the model at all, so nothing is added to a request automatically; whatever ends up in the `system` field is there because the developer's own code put it there, which is exactly why the API is the door for someone writing their own loop.

That is also why the boundary between the surfaces isn't arbitrary. Claude Code's five sub-surfaces share configuration for the reason given above: one engine, five entry points. claude.ai, the API, and the SDKs each read from their own separate storage instead, because each is a distinct piece of software with its own idea of where an instruction lives: a database record for claude.ai, a request field for the API, a constructor argument for the Client SDK. The Agent SDK is the deliberate exception, built to reuse Claude Code's own file-reading behavior inside a different product, reading `.claude/` and `~/.claude/` for the same reason Claude Code's other surfaces do: it was written to.

## Where the same-app assumption breaks

Desktop's three tabs live in the same window, on the same machine, opened with the same login. Every surface feature says they must share one configuration. They do not. The Code tab reads `~/.claude.json`, `~/.claude/settings.json`, and the project's CLAUDE.md, the same files the CLI reads. The Cowork tab, one click away in the same application, reads none of that. It sources its skills, plugins, and connectors from the "Customize" configuration synced through the user's claude.ai account, a different storage location reached through a different sync path than the tab sitting right next to it.

A second case sits further from what the surface implies. A Claude Code session started from claude.ai/code, or from Desktop's Cloud environment, still looks like Claude Code end to end: same CLAUDE.md hierarchy, same rules, same command set. It does not read everything the terminal reads. `~/.claude/settings.json` and `.claude/settings.local.json` both stay on the machine that created them; a cloud session only sees whatever got committed into the repository itself plus whatever the server manages centrally. A rule kept only in a personal, uncommitted settings file applies every time the same task runs from a developer's own laptop, and stops applying the moment the identical task runs in the cloud.

Even inside one Desktop session, cross-session messaging follows the same pattern. Desktop can message only its own local, SSH, and WSL sessions in the Code tab. A cloud session, a session started from the terminal CLI, or one started from the VS Code extension stays invisible to it, even when all three sit in worktrees of the exact same project. Two windows open on the same repository imply whatever the specific surface that started each one was built to see, nothing more.

## Where the map hands off

This chapter answers one question: which of the five doors reads an instruction, and from where. It does not answer what belongs inside that instruction once it has arrived: keeping an instruction separated from the data Claude is meant to act on, or shaping a tool's schema so its output can't be mistaken for a new command. That is chapter 23's territory: the internal contract of what gets built behind any of these doors.

It also doesn't answer what a session remembers once a conversation is under way. claude.ai's project knowledge base, Claude Code's context window, and a Desktop session's own history each scope and drop that history on their own terms, named here only in passing. What is retained, for how long, and at what scope belongs to chapter 24.

This chapter's whole job is everything in between: five doors, five different ways an instruction gets attached to a request before Claude ever sees it. It stops exactly there.

## The phrase that picks the door

A stem naming this chapter states what a developer needs and where. "Runs unattended, nobody watching a screen" picks Claude Code's headless mode or the Agent SDK. "Every conversation, regardless of project" picks claude.ai's account-wide instructions. "I manage my own retries" picks the raw API. "Same loop as Claude Code, in my own process" picks the Agent SDK.

## Self-test

**1.** A team wants a Python service that runs its own Claude-powered agent, using the same tools-and-loop behavior Claude Code uses, without asking anyone to operate a terminal. *(Select one.)*

A. Claude Code CLI in `-p` headless mode, invoked from a shell script.
B. The Agent SDK, built into their own Python process.
C. Claude Desktop's Cowork tab, configured through the Customize panel.
D. The Client SDK, with a hand-written tool loop.

**2.** A backend engineer is integrating Claude into a service she already owns. She writes and manages her own tool-use loop, and every request in the integration needs to carry the same fixed persona. *(Select one.)*

A. Set the persona once, in the Messages API's top-level `system` parameter.
B. Paste the persona into the start of every user message the service sends.
C. Set the persona as a claude.ai account-wide "Instructions for Claude" entry.
D. Hand the persona to Managed Agents and let Anthropic run the loop.

**3.** Which two of the following are accurate about Claude Desktop? *(Select two of four.)*

A. The Code tab and the Cowork tab read their skills and plugins from the same `~/.claude` directory.
B. The Cowork tab sources its skills, plugins, and connectors through the user's claude.ai account instead of `~/.claude`.
C. Scripting and automation through `--print` or the Agent SDK have no equivalent inside Desktop.
D. Desktop supports `dontAsk` permission mode in the Code tab, the same as the CLI.

**4.** A support team wants Claude to answer every conversation in the same company tone, regardless of which project or chat the conversation happens in. *(Select one.)*

A. A CLAUDE.md file, since it applies wherever Claude is running.
B. Per-project instructions inside the relevant claude.ai project.
C. Account-wide "Instructions for Claude," set once in Account Settings.
D. A skill invoked at the start of each conversation.

**Answers.** 1: B. The Agent SDK runs Claude Code's own tools, loop, and context management inside a developer's own process; A still needs a terminal-launched process, C reads a different configuration source and isn't scriptable, and D leaves the developer writing the loop by hand. 2: A. The `system` parameter is the top-level field built for this: set once, applied to every request, by code that owns its own loop; B repeats the persona instead of setting it once, C has no reading path into a raw API call, and D hands the loop to Managed Agents when the scenario says she keeps it herself. 3: B and C. The Cowork tab syncs through the claude.ai account rather than `~/.claude`, and Desktop's Code tab has no scripting equivalent to `--print` or the Agent SDK; A reverses the actual split between the two tabs, and D names a CLI-only permission mode. 4: C. Account-wide instructions apply regardless of project; A reaches for a Claude-Code-specific mechanism with no reading path into claude.ai, B is scoped to one project only, and D only fires when explicitly invoked.
