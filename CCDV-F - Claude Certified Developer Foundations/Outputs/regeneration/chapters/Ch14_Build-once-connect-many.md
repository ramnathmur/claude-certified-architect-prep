# 14 · Build once, connect many

## The main under the street

A town does not give every house its own well. Before the utility existed, that is what happened: each house sank its own hole, installed its own pump, and maintained it alone. A failed pump was that house's problem to fix, on its own schedule, at its own cost. A town of a hundred houses had a hundred separate systems, none of them coordinated with any other.

The utility replaced all of that with one thing: a main. A single pipe, sunk once, carrying water treated to one standard past every street in town. A house that wants water does not dig anything. It runs its own service line from the wall to the main and draws from a source it had no part in building. The same main serves the house next door, and it will serve a house built five years from now without being redesigned for it.

Software faces the same choice.

## What a server actually is

Wire a capability directly into one application's own code, and the well is dug: it works, and it belongs entirely to that application. If three different applications need the same external service, each one repeats the whole job from its own well: another schema to maintain, another place for a bug to hide. MCP, the Model Context Protocol, replaces the well with a main. It separates a capability from any one application and turns it into its own process, a program that runs independently and exposes what it offers to whoever connects. That program is the **server**.

Anthropic's own documentation for MCP compares this to a familiar piece of hardware: a USB-C port, one standard connector that lets many devices plug into many peripherals without a custom cable for every pair. The comparison states the payoff directly: build once, integrate everywhere.

The application that wants the capability is the **host** — Claude Code, an internal tool, a teammate's application, whatever program is actually doing the work. The host does not reach the server directly. It creates a **client**, a component whose only job is to hold open one connection to one server. A host that needs three separate servers creates three separate clients, one per server, the way a house drawing from both the town main and a private irrigation line keeps two separate service connections rather than merging them into one.

Authoring a server means deciding, once, what it will expose: which actions become tools, which fixed pieces of data become resources, which vetted instructions become prompts. Every host that connects afterward inherits that decision without making it again. This is also what integration comes to mean once a server exists: creating a client and connecting to it, work that costs far less than writing code against someone else's API from scratch. The applications that connect do not have to be alike. Claude Code is one host; a custom internal dashboard built by a different team is another; whatever a teammate builds next year for a problem nobody has thought of yet will be a third. None of them touch the server's own code to get access.

## Three things a server can hand back

A server can do more than answer requests to act. MCP defines three things a server can expose, and each solves a different problem.

A **tool** is a named action the model can call, with a schema describing its inputs, just like a tool wired directly into an application. Nothing about how a tool works changes because it now lives on a server; only where it is defined and who maintains it changes. A GitHub server's tool for opening an issue looks, from the model's side, like any tool an application wrote for itself: a name, a description, and a set of parameters the model fills in before the client sends the call on to the server.

A **resource** is read-only data the server hands the client directly, without the model deciding to call anything. A direct resource sits at a fixed address, such as a list of a company's approved vendors. A templated resource takes a parameter in its address, such as one specific document identified by its ID. Reach for a resource when the client should already have the data in context at the start of a turn, because pulling it in directly is cheaper and more predictable than sending the model to fetch it with a tool call.

A **prompt** is a pre-written instruction template the server exposes by name. A user can already ask for most tasks in plain language, so a prompt earns its place only where carefully built wording produces a materially better result than whatever a given user would type, and where every client connecting to the server should get that same wording rather than reinventing it.

Splitting the capability into three primitives instead of one is itself part of what lets a single server serve many different hosts well. A host that only knows how to call tools still benefits from a server that also offers resources and prompts, because nothing requires it to use all three; it uses whichever ones its own client supports. Resource support in particular varies from one client to the next, so a server built to lean on resources is worth checking against the specific client that will connect to it.

One more piece of the mechanism explains why changing the transport never touches any of this. MCP separates what is exchanged from how it travels: a data layer carries the actual protocol messages, such as listing which tools are available or calling one; a transport layer carries those messages between client and server. A server's tools, resources and prompts are defined once, in the data layer, and stay unchanged whether that server is reached locally or remotely. Only the transport layer changes.

## Two ways to reach it

A client and server still have to talk to each other, and that transport layer comes in two families.

**stdio** runs the server as a subprocess on the same machine as the client. The client launches it directly, and the two talk over standard input and output, just like a program printing to a screen or reading a keystroke. Nothing leaves the machine. This is the direct line run from a single house to a small pump sitting on that same property: fast, simple, and reachable only by the one house it was run for. That directness is stdio's advantage where it fits: no network round-trip, and no separate authentication step to configure. A local script that reads a file and returns its contents pays only the cost of one process talking to another on the same machine.

**Sockets** carry the connection over a network instead. A client and server built for this family can sit on entirely different machines. MCP's current transport in this family is Streamable HTTP: the client sends requests as HTTP POST calls, and the server can stream events back over the same connection. This is the main running under the street, reachable by any house with a valid connection to it, including a house on the far side of town. Because a sockets connection can reach a server on someone else's infrastructure, it typically needs its own authentication on every request: a bearer token, an API key, or a full OAuth sign-in. A stdio server on your own machine needs none of that; it already runs with whatever access your own machine has.

A stdio server is spawned fresh by whichever client starts it, so it typically serves exactly one client. A sockets server is typically hosted somewhere reachable on the network and typically serves many clients that connect to that one running instance. Which one fits is a deployment question: run the capability once, in one place, and let everyone who connects reach that instance, or run it fresh and local, for whoever happens to start it on their own machine. GitHub's own MCP server, which exposes tools for managing pull requests and issues, takes the first path: hosted once by GitHub and reached over sockets, one running instance answering however many houses tap into it.

## When the main earns its cost

Digging a well remains the right answer when only one house needs water and no other house ever will: less to build, and nothing to coordinate with anyone else. The main only pays for itself once a second house wants to connect.

The server decision runs on this arithmetic too. A capability wired directly into one application costs one integration and answers to one team's roadmap. The moment a second application needs the same capability, wiring it twice means maintaining it twice: two schemas to keep in sync with whatever the underlying service changes, two places a bug can diverge from its twin. Say the warehouse API adds a required field to its query endpoint next quarter. With two direct integrations, two different engineers on two different schedules discover this the same way, when a request starts failing. With one server, the fix lands once, in the server's own schema, and both applications inherit it the next time their client calls in.

Building the capability as a server once, and letting every application that needs it create its own client connection, means the underlying service can change in one place and every connected application gets the update the next time it calls in. MCP's own materials name this payoff directly: build once, integrate everywhere. The rule this chapter derives follows from it: reach for a server, over sockets, once more than one application needs the capability, or once the capability must be kept current against something your own team does not control. Below that line, a well is still the right answer.

Building it as a server is not enough by itself: a stdio server built once still runs as separately as the wells it replaced, once more than one machine needs to reach it. The transport has to carry the "many" as well as the "once." The decision can run on a plausible guess about whether a second application will show up, made before either application depends on the answer. Waiting until a second team already depends on the direct integration turns the choice into a migration of a live dependency instead of a decision made in advance.

## What actually runs when three people connect

A team building an internal tool decides three developers should each be able to reach the same data-warehouse capability from their own laptops. Someone writes the MCP server, commits its configuration to the project's repository, and tells the team: clone the repo, and you're connected to the shared server.

The surface of that plan looks like the main: one configuration, checked in once, available to everyone who clones it. The transport underneath works differently. The server was written for stdio, launched as a subprocess by whichever client starts it. When the first developer clones the repository and opens the project, their client reads the committed configuration and spawns its own copy of the server, running locally, on their own machine. The second developer's client spawns a second copy, on their machine. The third spawns a third. Three developers now run three separate server processes, each built from the identical configuration, each a private pump serving only the one house that started it. None of them share one main. Each developer's machine also needs whatever runtime the server requires installed locally, because each machine is running its own copy: if the server is launched with a command like `npx some-warehouse-server`, all three need Node installed and working before their own copy will even start, a requirement that has nothing to do with the warehouse and everything to do with how stdio launches a server.

stdio is doing what a subprocess is supposed to do here: running next to the one client that started it. The mistake is expecting a checked-in stdio configuration to behave like a main when it behaves like a blueprint for three separate pumps. A capability three developers need to reach as one running, centrally maintained instance needs a socket-based server they all connect to. A fresh local copy per developer cannot produce that, no matter how carefully the configuration file is written. Moving the same server to a socket-based transport, hosted on one machine the whole team can reach, turns the three copies back into the one instance the plan assumed from the start: one process, one place a fix has to land.

## The one thing the config file must never hold

A server reached over sockets often needs its own credential to do its job: a data-warehouse server needs a token that proves it may query the warehouse, a code-hosting server needs a token that proves it may act on a repository on your behalf. That credential belongs in an environment variable the configuration file references by name, never written into the file as a literal value.

A configuration file that gets committed to a shared repository, the way project-wide server configuration typically does, carries anything written into it into that repository's history permanently. A later commit that removes the credential removes it only from the current version of the file; the earlier commit where it was still readable stays in history, reachable by anyone who can read the repository. That is the mistake it is tempting to make: edit the credential out of the latest commit and consider it handled. A credential that was ever committed as a literal value has to be treated as compromised and rotated, not edited out. The fix going forward is simple: the configuration file names an environment variable, such as one holding a warehouse token, and the actual value lives wherever environment variables live on that machine, never inside the file MCP reads.

A stdio server rarely raises this problem, since it runs with your own machine's access and is less often checked into a repository everyone else reads. The risk concentrates where sharing does: a sockets server, reached by a team, configured in a file the whole team's clones will hold.

That is where this chapter's authority over secrets ends. Rotating a compromised credential and deciding who is allowed to hold one: that is a separate discipline, and it does not belong here.

## What the stem sounds like

A stem naming this chapter's mechanism says a capability must be reachable from a machine other than the one running it, that several teams need to reach one running instance, or that a credential is about to be written into a file every clone will carry. It does not describe a single developer, alone, on one machine.

## Self-test

**1.** A solo developer builds an MCP server that wraps a script only she runs, only from her own laptop. Nothing else will ever connect to it. Which transport fits? *(Select one.)*

A. stdio, since the client and server are always on the same machine.
B. Sockets, hosted centrally, so the server stays reachable if she later works from a different laptop.
C. Sockets, because that is the transport GitHub's own MCP server uses.
D. Either transport, as long as the team agrees not to commit credentials to the configuration file.

**2.** An internal application needs to reach three separate services (a ticketing system, a deployment pipeline, and a metrics dashboard), each exposed as its own MCP server. How does the host manage these three connections? *(Select one.)*

A. It creates one MCP client for each server: three clients, each maintaining its own connection.
B. It builds one new MCP server that wraps all three services behind a single connection.
C. A single client can reach all three, provided the team documents which tools belong to which service.
D. It caches the tool definitions from all three servers so the context cost stays flat.

**3.** An internal MCP server exposes a fixed, rarely changing list of approved vendors. Every session using this server needs that list in context from the first turn, and fetching it never depends on anything the user says. Which primitive fits, and how should the server expose it? *(Select one.)*

A. A direct resource: a fixed address the client fetches and places into context, no tool call required.
B. A tool the model calls at the start of every session to retrieve the list.
C. A prompt template that instructs the model to always ask the user for the vendor list.
D. A note in the server's documentation that the list rarely changes, so clients can cache it themselves.

**4.** A team commits its MCP server configuration to the project repository so every clone launches the same server automatically. The server needs a bearer token to reach an internal data warehouse. Select the two statements that correctly describe how the token should be handled. *(Select two.)*

A. Reference the token through an environment variable inside the configuration file; never write it as a literal string.
B. Once a token has ever been committed as a literal value, treat it as compromised and rotate it, even after a later commit removes it.
C. Overwrite the configuration file in a new commit with the literal value removed; that clears the exposure.
D. Switch the transport from sockets to stdio so the token never has to leave the local machine.

**Answers.** 1: A. Nothing here needs a network; B and C both spend hosting or transport complexity the scenario never asked for, and D relies on team agreement rather than the mechanism. 2: A. One client per server is the architecture; B is real but unneeded for three existing servers, and C and D each solve a different problem than the one asked. 3: A. Fixed, parameter-free, needed from turn one is exactly a direct resource; B spends a tool call on static data, C misuses a prompt template, and D relies on every client remembering to cache on its own. 4: A and B. Reference the value, and treat any credential that was ever committed inline as compromised regardless of later edits. C is false, since history persists past the edit, and D changes an unrelated design decision without removing the exposure.
