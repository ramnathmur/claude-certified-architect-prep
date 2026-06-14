# MCP at a Builder Level — CCA-F Domain 4 Research Notes

**Title:** Model Context Protocol (MCP) for Architects — Grounded Research Notes
**Date:** 2026-06-05 · **Re-verified 2026-06-09** (MCP spec `2025-11-25` re-confirmed still latest. Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`)
**Primary CCA-F Domain:** Domain 4 — Tool Design & MCP Integration (18%)
**Secondary overlap flagged inline:** D1 (Claude platform fundamentals — MCP connector on the Messages API), D2 (agentic patterns — the tool-use loop, sampling/agentic workflows).

> Provenance note: This file is a source-of-truth research artifact. **Every substantive claim carries an inline `(source: URL)`.** Quotations are marked with quotation marks and attributed. Version-sensitive or uncertain facts are tagged `[VERIFY]` inline and re-collected in the final `[VERIFY]` list.

## Sources used (every URL fetched for this file)

- https://modelcontextprotocol.io/introduction — "What is the Model Context Protocol (MCP)?" (intro / USB-C framing)
- https://modelcontextprotocol.io/docs/learn/architecture — Architecture overview (participants, layers, data-layer protocol, lifecycle, full JSON-RPC example messages)
- https://modelcontextprotocol.io/docs/learn/server-concepts — Server features (Tools/Resources/Prompts, "who controls it", protocol methods)
- https://modelcontextprotocol.io/docs/learn/client-concepts — Client features (Elicitation/Roots/Sampling)
- https://modelcontextprotocol.io/docs/concepts/transports — Transports (stdio, Streamable HTTP, HTTP+SSE deprecation)
- https://www.anthropic.com/news/model-context-protocol — Original Anthropic announcement (Nov 25, 2024)
- https://platform.claude.com/docs/en/agents-and-tools/mcp-connector — MCP connector on the Claude Messages API
- https://code.claude.com/docs/en/mcp — Claude Code MCP support and `claude mcp add` reference

---

## 1. What MCP Is and Why It Exists  *(CCA-F D4; intro overlaps D1)*

**Definition (verbatim):** "MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems." (source: https://modelcontextprotocol.io/introduction)

**The USB-C framing (verbatim):** "Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems." (source: https://modelcontextprotocol.io/introduction)

**What it connects:** "AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks." (source: https://modelcontextprotocol.io/introduction) — Note the three connectable categories (data sources, tools, workflows) map directly onto the three server primitives in §3.

**Why it exists / the M×N integration problem (verbatim from Anthropic's announcement):** MCP is "a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol." (source: https://www.anthropic.com/news/model-context-protocol) The problem statement: "Even the most sophisticated models are constrained by their isolation from data—trapped behind information silos and legacy systems." (source: https://www.anthropic.com/news/model-context-protocol) Rather than building a separate custom integration for every (AI app × data source) pair — the M×N explosion — MCP collapses it to M+N: each app implements MCP once, each data source implements MCP once.

**Origin facts:** MCP was announced by Anthropic on **November 25, 2024** as "a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments." (source: https://www.anthropic.com/news/model-context-protocol) Anthropic described "open-sourcing the Model Context Protocol" and committed to "building MCP as a collaborative, open-source project and ecosystem." (source: https://www.anthropic.com/news/model-context-protocol)

**Scope boundary (important testable nuance):** "MCP focuses solely on the protocol for context exchange—it does not dictate how AI applications use LLMs or manage the provided context." (source: https://modelcontextprotocol.io/docs/learn/architecture) MCP standardizes the *exchange*, not the model's reasoning.

**Ecosystem breadth:** MCP is "supported across a wide range of clients and servers," including Claude, ChatGPT, Visual Studio Code, Cursor, and others. (source: https://modelcontextprotocol.io/introduction)

---

## 2. Architecture — Host / Client / Server  *(CCA-F D4; the role distinctions are heavily testable)*

MCP "follows a client-server architecture where an MCP host — an AI application like Claude Code or Claude Desktop — establishes connections to one or more MCP servers. The MCP host accomplishes this by creating **one MCP client for each MCP server**. **Each MCP client maintains a dedicated connection with its corresponding MCP server.**" (source: https://modelcontextprotocol.io/docs/learn/architecture) — Emphasis added; the **one-client-per-server** rule is the single most testable architecture fact.

**The three participants (verbatim definitions):** (source: https://modelcontextprotocol.io/docs/learn/architecture)
- **MCP Host:** "The AI application that coordinates and manages one or multiple MCP clients."
- **MCP Client:** "A component that maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use."
- **MCP Server:** "A program that provides context to MCP clients."

**Client-side framing (verbatim):** "the *host* is the application users interact with, while *clients* are the protocol-level components that enable server connections... Each client handles one direct communication with one server." (source: https://modelcontextprotocol.io/docs/learn/client-concepts)

**Worked example (verbatim):** "Visual Studio Code acts as an MCP host. When Visual Studio Code establishes a connection to an MCP server, such as the Sentry MCP server, the Visual Studio Code runtime instantiates an MCP client object that maintains the connection to the Sentry MCP server. When Visual Studio Code subsequently connects to another MCP server... the Visual Studio Code runtime instantiates an additional MCP client object." (source: https://modelcontextprotocol.io/docs/learn/architecture)

**Local vs remote serving model:** "Local MCP servers that use the STDIO transport typically serve a single MCP client, whereas remote MCP servers that use the Streamable HTTP transport will typically serve many MCP clients." (source: https://modelcontextprotocol.io/docs/learn/architecture) Note: a single remote server with two connections from one host is served by **two distinct clients** (per the architecture diagram, Client3 and Client4 both connect to remote Server C). (source: https://modelcontextprotocol.io/docs/learn/architecture)

**"Server" is about role, not location:** "MCP server refers to the program that serves context data, regardless of where it runs. MCP servers can execute locally or remotely." (source: https://modelcontextprotocol.io/docs/learn/architecture)

**Two layers (verbatim):** (source: https://modelcontextprotocol.io/docs/learn/architecture)
- **Data layer (inner):** "Defines the JSON-RPC based protocol for client-server communication, including lifecycle management, and core primitives, such as tools, resources, prompts and notifications."
- **Transport layer (outer):** "Defines the communication mechanisms and channels that enable data exchange between clients and servers, including transport-specific connection establishment, message framing, and authorization."
- "Conceptually the data layer is the inner layer, while the transport layer is the outer layer." (source: https://modelcontextprotocol.io/docs/learn/architecture)

---

## 3. The Three Server Primitives — Tools, Resources, Prompts  *(CCA-F D4; the "who controls it" distinction is the highest-yield exam fact)*

"Servers provide functionality through three building blocks." (source: https://modelcontextprotocol.io/docs/learn/server-concepts) The control model (verbatim from the server-concepts table):

| Primitive | Verbatim explanation | Who controls it |
|---|---|---|
| **Tools** | "Functions that your LLM can actively call, and decides when to use them based on user requests. Tools can write to databases, call external APIs, modify files, or trigger other logic." | **Model** |
| **Resources** | "Passive data sources that provide read-only access to information for context, such as file contents, database schemas, or API documentation." | **Application** |
| **Prompts** | "Pre-built instruction templates that tell the model to work with specific tools and resources." | **User** |

(source: https://modelcontextprotocol.io/docs/learn/server-concepts)

> **Mnemonic for the exam:** Tools = **M**odel-controlled, Resources = **A**pplication-controlled, Prompts = **U**ser-controlled (M-A-U). This three-way control split is the most heavily tested MCP fact.

### 3.1 Tools (model-controlled)
- "Tools enable AI models to perform actions. Each tool defines a specific operation with typed inputs and outputs. The model requests tool execution based on context." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- "Tools are schema-defined interfaces that LLMs can invoke. MCP uses JSON Schema for validation." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- "Tools are model-controlled, meaning AI models can discover and invoke them automatically. However, MCP emphasizes human oversight." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- "Tools may require user consent prior to execution, helping to ensure users maintain control over actions taken by a model." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- **Protocol operations:** `tools/list` ("Discover available tools" -> "Array of tool definitions with schemas") and `tools/call` ("Execute a specific tool" -> "Tool execution result"). (source: https://modelcontextprotocol.io/docs/learn/server-concepts)

### 3.2 Resources (application-controlled)
- "Resources provide structured access to information that the AI application can retrieve and provide to models as context." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- **URI addressing (verbatim):** "Each resource has a unique URI (e.g., `file:///path/to/document.md`) and declares its MIME type for appropriate content handling." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- **Two discovery patterns:** "**Direct Resources** - fixed URIs that point to specific data. Example: `calendar://events/2024`" and "**Resource Templates** - dynamic URIs with parameters for flexible queries. Example: `travel://activities/{city}/{category}`." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- "Resources are application-driven, giving them flexibility in how they retrieve, process, and present available context." (source: https://modelcontextprotocol.io/docs/learn/server-concepts) — i.e., the *application*, not the model, decides whether/how to include a resource.
- **Protocol operations:** `resources/list` ("List available direct resources"), `resources/templates/list` ("Discover resource templates"), `resources/read` ("Retrieve resource contents"), `resources/subscribe` ("Monitor resource changes"). (source: https://modelcontextprotocol.io/docs/learn/server-concepts)

### 3.3 Prompts (user-controlled)
- "Prompts provide reusable templates. They allow MCP server authors to provide parameterized prompts for a domain, or showcase how to best use the MCP server." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- "They are user-controlled, requiring explicit invocation rather than automatic triggering." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- Common UI surfaces: "Slash commands (typing '/' to see available prompts like /plan-vacation), Command palettes... Dedicated UI buttons... Context menus." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- **Protocol operations:** `prompts/list` ("Discover available prompts") and `prompts/get` ("Retrieve prompt details" -> "Full prompt definition with arguments"). (source: https://modelcontextprotocol.io/docs/learn/server-concepts)

---

## 4. Client Primitives — Features the Host Offers Back to Servers  *(CCA-F D4; Sampling overlaps D2 agentic patterns)*

"In addition to making use of context provided by servers, clients may provide several features to servers. These client features allow server authors to build richer interactions." (source: https://modelcontextprotocol.io/docs/learn/client-concepts) Three primary client features (verbatim summaries):

| Feature | Verbatim explanation | Method |
|---|---|---|
| **Elicitation** | "Elicitation enables servers to request specific information from users during interactions, providing a structured way for servers to gather information on demand." | `elicitation/create` |
| **Roots** | "Roots allow clients to specify which directories servers should focus on, communicating intended scope through a coordination mechanism." | `roots/list` (+ `roots/list_changed` notification) |
| **Sampling** | "Sampling allows servers to request LLM completions through the client, enabling an agentic workflow. This approach puts the client in complete control of user permissions and security measures." | `sampling/createMessage` |

(source: https://modelcontextprotocol.io/docs/learn/client-concepts)

### 4.1 Sampling (`sampling/createMessage`)
- "Sampling enables servers to perform AI-dependent tasks without directly integrating with or paying for AI models. Instead, servers can request that the client—which already has AI model access—handle these tasks on their behalf." (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- This is what keeps a server **model-independent** — a server author "want[s] access to a language model, but want[s] to stay model-independent and not include a language model SDK in their MCP server." (source: https://modelcontextprotocol.io/docs/learn/architecture)
- **Human-in-the-loop design (multiple checkpoints):** "Users review and can modify both the initial request and the generated response before it returns to the server." (source: https://modelcontextprotocol.io/docs/learn/client-concepts) The flow includes "Human-in-the-loop review" before forwarding to the LLM and "Response review" before returning to the server. (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- Request params include `messages`, `modelPreferences` (with `hints`, `costPriority`, `speedPriority`, `intelligencePriority`), `systemPrompt`, and `maxTokens`. (source: https://modelcontextprotocol.io/docs/learn/client-concepts)

### 4.2 Roots (`roots/list`)
- "Roots are a mechanism for clients to communicate filesystem access boundaries to servers... While roots communicate intended boundaries, they do not enforce security restrictions. Actual security must be enforced at the operating system level, via file permissions and/or sandboxing." (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- "Roots are exclusively filesystem paths and always use the `file://` URI scheme." (source: https://modelcontextprotocol.io/docs/learn/client-concepts) Structure example: `{"uri": "file:///Users/agent/travel-planning", "name": "Travel Planning Workspace"}`.
- **Advisory, not enforced (verbatim, design philosophy):** "The specification requires that servers 'SHOULD respect root boundaries,' and not that they 'MUST enforce' them, because servers run code the client cannot control." (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- Dynamic updates flow via the `roots/list_changed` notification. (source: https://modelcontextprotocol.io/docs/learn/client-concepts)

### 4.3 Elicitation (`elicitation/create`)
- "Elicitation provides a structured way for servers to gather necessary information on demand. Instead of requiring all information up front or failing when data is missing, servers can pause their operations to request specific inputs from users." (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- The request carries a `message` plus a JSON `schema` defining the fields requested. (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- **Privacy guardrail (verbatim):** "Elicitation never requests passwords or API keys. Clients warn about suspicious requests and let users review data before sending." (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- **Maturity note `[VERIFY]`:** The architecture page labels **Tasks** as "(Experimental)" — "Durable execution wrappers that enable deferred result retrieval and status tracking." (source: https://modelcontextprotocol.io/docs/learn/architecture) Elicitation and Sampling are presented as standard client features in current docs (no "experimental" label observed), but their stability across spec revisions is version-sensitive — `[VERIFY]` against the dated spec at https://modelcontextprotocol.io/specification/latest before asserting GA status in a lesson.

### 4.4 Logging (a fourth client-side utility)
- "Logging: Enables servers to send log messages to clients for debugging and monitoring purposes." (source: https://modelcontextprotocol.io/docs/learn/architecture) Listed among client-facing utility features, distinct from the three primary client primitives above.

---

## 5. Transports — stdio vs Streamable HTTP  *(CCA-F D4; transport naming/status is version-sensitive — `[VERIFY]`)*

"The protocol currently defines two standard transport mechanisms for client-server communication: 1. stdio... 2. Streamable HTTP." (source: https://modelcontextprotocol.io/docs/concepts/transports) "Clients **SHOULD** support stdio whenever possible." (source: https://modelcontextprotocol.io/docs/concepts/transports) "MCP uses JSON-RPC to encode messages. JSON-RPC messages **MUST** be UTF-8 encoded." (source: https://modelcontextprotocol.io/docs/concepts/transports)

### 5.1 stdio (local)
Verbatim mechanics (source: https://modelcontextprotocol.io/docs/concepts/transports):
- "The client launches the MCP server as a subprocess."
- "The server reads JSON-RPC messages from its standard input (`stdin`) and sends messages to its standard output (`stdout`)."
- "Messages are delimited by newlines, and **MUST NOT** contain embedded newlines."
- "The server **MAY** write UTF-8 strings to its standard error (`stderr`) for logging purposes."
- "The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message." (and the symmetric rule for the client writing to the server's `stdin`).

Use stdio for local subprocess servers with "optimal performance with no network overhead." (source: https://modelcontextprotocol.io/docs/learn/architecture)

### 5.2 Streamable HTTP (remote — current standard)
- "In the **Streamable HTTP** transport, the server operates as an independent process that can handle multiple client connections. This transport uses HTTP POST and GET requests. Server can optionally make use of Server-Sent Events (SSE) to stream multiple server messages." (source: https://modelcontextprotocol.io/docs/concepts/transports)
- "The server **MUST** provide a single HTTP endpoint path (hereafter referred to as the **MCP endpoint**) that supports both POST and GET methods. For example... `https://example.com/mcp`." (source: https://modelcontextprotocol.io/docs/concepts/transports)
- Client requirements: "use HTTP POST to send JSON-RPC messages," and "include an `Accept` header, listing both `application/json` and `text/event-stream` as supported content types." (source: https://modelcontextprotocol.io/docs/concepts/transports)
- **Session management:** server "**MAY** assign a session ID at initialization time, by including it in an `Mcp-Session-Id` header." Clients then "**MUST** include it in the `Mcp-Session-Id` header on all of their subsequent HTTP requests." (source: https://modelcontextprotocol.io/docs/concepts/transports)
- **Protocol version header:** "the client **MUST** include the `MCP-Protocol-Version: <protocol-version>` HTTP header on all subsequent requests," e.g. `MCP-Protocol-Version: 2025-06-18`. If absent, "the server **SHOULD** assume protocol version `2025-03-26`." (source: https://modelcontextprotocol.io/docs/concepts/transports)
- Auth: "supports standard HTTP authentication methods including bearer tokens, API keys, and custom headers. MCP recommends using OAuth to obtain authentication tokens." (source: https://modelcontextprotocol.io/docs/learn/architecture)

### 5.3 Deprecation of the standalone HTTP+SSE transport
- Verbatim: "This replaces the HTTP+SSE transport from protocol version 2024-11-05." (source: https://modelcontextprotocol.io/docs/concepts/transports) The deprecated transport is explicitly referred to as "the deprecated HTTP+SSE transport (from protocol version 2024-11-05)." (source: https://modelcontextprotocol.io/docs/concepts/transports)
- **Important nuance:** SSE is **not gone** — it survives *inside* Streamable HTTP as an optional streaming mechanism. What was deprecated is the **standalone HTTP+SSE transport** (the older two-endpoint design with a separate SSE endpoint + `endpoint` event). (source: https://modelcontextprotocol.io/docs/concepts/transports)
- **Product-surface confirmation:** Claude Code's docs state "The SSE (Server-Sent Events) transport is deprecated. Use HTTP servers instead, where available." (source: https://code.claude.com/docs/en/mcp) Claude Code accepts `streamable-http` as an alias for `http` in JSON config: "The MCP specification uses the name `streamable-http` for this transport." (source: https://code.claude.com/docs/en/mcp)

`✓ VERIFIED 2026-06-06` — The current canonical "latest" protocol version is **`2025-11-25`** (confirmed at https://modelcontextprotocol.io/specification/latest). `2025-06-18` and `2025-03-26` are prior revisions; `2025-03-26` remains the documented backwards-compatibility fallback default. Re-verify before exam day — spec dates roll forward.

### 5.4 Security warnings for Streamable HTTP (verbatim MUST/SHOULD)
(source: https://modelcontextprotocol.io/docs/concepts/transports)
1. "Servers **MUST** validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks."
2. "When running locally, servers **SHOULD** bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)."
3. "Servers **SHOULD** implement proper authentication for all connections."
Rationale: "Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites."

### 5.5 Custom transports
"Clients and servers **MAY** implement additional custom transport mechanisms... The protocol is transport-agnostic." Custom transports "**MUST** ensure they preserve the JSON-RPC message format and lifecycle requirements defined by MCP." (source: https://modelcontextprotocol.io/docs/concepts/transports)

---

## 6. Wire Protocol — JSON-RPC 2.0, Messages, Lifecycle  *(CCA-F D4)*

"The data layer implements a JSON-RPC 2.0 based exchange protocol that defines the message structure and semantics." (source: https://modelcontextprotocol.io/docs/learn/architecture) "Client and servers send requests to each other and respond accordingly. **Notifications can be used when no response is required.**" (source: https://modelcontextprotocol.io/docs/learn/architecture)

**Message types:** requests (have `id`), responses (echo the `id`), and notifications (no `id`, no response). "Notifications are sent as JSON-RPC 2.0 notification messages (without expecting a response)." (source: https://modelcontextprotocol.io/docs/learn/architecture)

**Stateful protocol:** "MCP is a stateful protocol that requires lifecycle management. The purpose of lifecycle management is to negotiate the capabilities that both client and server support." (source: https://modelcontextprotocol.io/docs/learn/architecture)

### 6.1 The initialize handshake / capability negotiation
The connection opens with an `initialize` request. Three stated purposes (verbatim): (source: https://modelcontextprotocol.io/docs/learn/architecture)
1. **Protocol Version Negotiation** — "ensures both client and server are using compatible protocol versions... If a mutually compatible version is not negotiated, the connection should be terminated."
2. **Capability Discovery** — "The `capabilities` object allows each party to declare what features they support."
3. **Identity Exchange** — "The `clientInfo` and `serverInfo` objects provide identification and versioning information."

**Initialize request (verbatim example):** (source: https://modelcontextprotocol.io/docs/learn/architecture)
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-11-25",
    "capabilities": { "elicitation": {} },
    "clientInfo": { "name": "example-client", "version": "1.0.0" }
  }
}
```

**Initialize response (verbatim example):** (source: https://modelcontextprotocol.io/docs/learn/architecture)
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "tools": { "listChanged": true },
      "resources": {}
    },
    "serverInfo": { "name": "example-server", "version": "1.0.0" }
  }
}
```

**Capability semantics (verbatim):** `"tools": {"listChanged": true}` means "The server supports the tools primitive AND can send `tools/list_changed` notifications when its tool list changes." `"elicitation": {}` on the client side means "The client declares it can work with user interaction requests (can receive `elicitation/create` method calls)." (source: https://modelcontextprotocol.io/docs/learn/architecture)

**Ready notification (verbatim):** After initialization, "the client sends a notification to indicate it's ready":
```json
{ "jsonrpc": "2.0", "method": "notifications/initialized" }
```
(source: https://modelcontextprotocol.io/docs/learn/architecture)

### 6.2 Notifications in flight
Example tool-list-change notification (verbatim): `{"jsonrpc": "2.0", "method": "notifications/tools/list_changed"}`. "Notice there's no `id` field in the notification. This follows JSON-RPC 2.0 notification semantics where no response is expected or sent." It is "only sent by servers that declared `"listChanged": true`." (source: https://modelcontextprotocol.io/docs/learn/architecture)

### 6.3 Cancellation
"To cancel, the client **SHOULD** explicitly send an MCP `CancelledNotification`." (source: https://modelcontextprotocol.io/docs/concepts/transports)

---

## 7. Discovery and Invocation — The Method Catalog  *(CCA-F D4)*

"Each primitive type has associated methods for discovery (`*/list`), retrieval (`*/get`), and in some cases, execution (`tools/call`). MCP clients will use the `*/list` methods to discover available primitives... This design allows listings to be dynamic." (source: https://modelcontextprotocol.io/docs/learn/architecture)

**Consolidated method table** (names verbatim across the cited pages):

| Method | Type | Purpose | Source |
|---|---|---|---|
| `initialize` | request | Open connection, negotiate version + capabilities | architecture |
| `notifications/initialized` | notification | Client signals readiness | architecture |
| `tools/list` | request | Discover available tools (no params) | architecture, server-concepts |
| `tools/call` | request | Execute a tool (`params`: `name`, `arguments`) | architecture, server-concepts |
| `resources/list` | request | List direct resources | server-concepts |
| `resources/templates/list` | request | Discover resource templates | server-concepts |
| `resources/read` | request | Retrieve resource contents | server-concepts |
| `resources/subscribe` | request | Monitor resource changes | server-concepts |
| `prompts/list` | request | Discover prompts | server-concepts |
| `prompts/get` | request | Retrieve full prompt definition | server-concepts |
| `sampling/createMessage` | request (server->client) | Request an LLM completion | client-concepts |
| `elicitation/create` | request (server->client) | Request user input | client-concepts |
| `roots/list` | request (server->client) | Get filesystem roots | client-concepts / code.claude.com |
| `roots/list_changed` | notification | Roots boundary changed | client-concepts |
| `notifications/tools/list_changed` | notification | Tool list changed | architecture |

(sources: https://modelcontextprotocol.io/docs/learn/architecture ; https://modelcontextprotocol.io/docs/learn/server-concepts ; https://modelcontextprotocol.io/docs/learn/client-concepts ; https://code.claude.com/docs/en/mcp)

**Discovery example — `tools/list` request (verbatim):** `{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}` — "The `tools/list` request is simple, containing no parameters." The response returns a `tools` array where each tool has `name`, `title`, `description`, and `inputSchema` (JSON Schema). (source: https://modelcontextprotocol.io/docs/learn/architecture)

**Invocation example — `tools/call` request (verbatim):** (source: https://modelcontextprotocol.io/docs/learn/architecture)
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "weather_current",
    "arguments": { "location": "San Francisco", "units": "imperial" }
  }
}
```
The response returns a `content` array of typed blocks (e.g., `{"type": "text", "text": "..."}`). "Tool responses return an array of content objects, allowing for rich, multi-format responses (text, images, resources, etc.)." (source: https://modelcontextprotocol.io/docs/learn/architecture)

---

## 8. Using MCP with Claude Specifically  *(CCA-F D4 + D1)*

Keep two surfaces conceptually distinct: **MCP the open standard** (modelcontextprotocol.io) vs **Anthropic's product implementations** that *consume* that standard (the Messages API connector, Claude Code, Claude Desktop, Claude.ai connectors).

### 8.1 MCP connector on the Claude Messages API *(D1 overlap)*
- "Claude's Model Context Protocol (MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API **without a separate MCP client**." (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- **Required beta header (current):** `"anthropic-beta": "mcp-client-2025-11-20"`. "The previous version (`mcp-client-2025-04-04`) is deprecated." (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector) `[VERIFY]` — beta header strings are version-sensitive.
- **Two components:** an `mcp_servers` array (server connection: `type: "url"`, `url` must start with `https://`, `name`, optional `authorization_token`) and a `tools` array containing one `mcp_toolset` per server (`type: "mcp_toolset"`, `mcp_server_name`). (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- **Key limitations (verbatim):** "Of the feature set of the MCP specification, only **tool calls** are currently supported." And: "The server must be publicly exposed through HTTP (supports both Streamable HTTP and SSE transports). **Local STDIO servers cannot be connected directly.**" (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector) The connector is available on the Claude API, Claude Platform on AWS, and Microsoft Foundry, but "not currently available on Amazon Bedrock or Vertex AI." (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- **Tool filtering:** allowlist (set `default_config.enabled: false`, then enable specific tools in `configs`) or denylist (enable all, disable specific tools). "Denylisting write or destructive tools is recommended when building read-only assistants, or when you want a human confirmation step before state changes." (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- **Response content blocks:** `mcp_tool_use` (includes `server_name`) and `mcp_tool_result` (includes `tool_use_id`, `is_error`, `content`). (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- **Data retention caveat:** "This feature is **not** eligible for Zero Data Retention (ZDR)." (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- **Client-side helpers** (TypeScript SDK only) bridge local stdio servers, prompts, and resources into the API: `mcpTools`, `mcpMessages`, `mcpResourceToContent`, `mcpResourceToFile`. "Use the `mcp_servers` API parameter when you have remote servers accessible by URL and only need tool support. Use the client-side helpers when you need local servers, prompts, resources, or more control." (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)

### 8.2 Claude Code as an MCP host
- "Claude Code can connect to hundreds of external tools and data sources through the Model Context Protocol (MCP), an open source standard for AI-tool integrations." (source: https://code.claude.com/docs/en/mcp)
- **`claude mcp add` — three primary transports (verbatim syntax):** (source: https://code.claude.com/docs/en/mcp)
  - Remote HTTP (recommended): `claude mcp add --transport http <name> <url>` — e.g. `claude mcp add --transport http notion https://mcp.notion.com/mcp`
  - Remote SSE (deprecated): `claude mcp add --transport sse <name> <url>`
  - Local stdio: `claude mcp add [options] <name> -- <command> [args...]` — e.g. `claude mcp add --env AIRTABLE_API_KEY=YOUR_KEY --transport stdio airtable -- npx -y airtable-mcp-server`
  - (A fourth, WebSocket `type: "ws"`, is available only via `.mcp.json` / `add-json`, not `--transport`.)
- **The `--` separator (testable detail):** "For stdio servers, the `--` (double dash) separates Claude's own options... from the command and arguments that run the server. Everything after `--` is passed to the server untouched." (source: https://code.claude.com/docs/en/mcp)
- **Three scopes:** (source: https://code.claude.com/docs/en/mcp)
  - **Local** (default): "Available only to you in the current project" — stored in `~/.claude.json`.
  - **Project**: "Shared with everyone in the project via `.mcp.json` file" (checked into version control).
  - **User**: "Available to you across all projects" — stored in `~/.claude.json`.
  - Precedence (highest->lowest): Local -> Project -> User -> Plugin-provided -> claude.ai connectors. "fields are not merged across scopes." (source: https://code.claude.com/docs/en/mcp)
- **Management commands:** `claude mcp list`, `claude mcp get <name>`, `claude mcp remove <name>`, and the in-session `/mcp` panel (also used for OAuth login). (source: https://code.claude.com/docs/en/mcp)
- **Claude Code consumes all three server primitives:** prompts surface as `/mcp__servername__promptname` slash commands; resources are referenced with `@server:protocol://resource/path` (e.g. `@github:issue://123`); elicitation requests pop interactive dialogs automatically. (source: https://code.claude.com/docs/en/mcp)
- **Claude Code can itself be a server:** `claude mcp serve` "Start[s] Claude as a stdio MCP server" that other apps (e.g., Claude Desktop) can connect to. (source: https://code.claude.com/docs/en/mcp)
- **Claude Desktop** is named as a canonical MCP host alongside Claude Code; it launches local stdio servers such as the filesystem server. (source: https://modelcontextprotocol.io/docs/learn/architecture) Servers configured in Claude Desktop can be imported via `claude mcp add-from-claude-desktop` (macOS/WSL only). (source: https://code.claude.com/docs/en/mcp)

---

## 9. Security / Builder Concerns  *(CCA-F D4; trust & permissioning)*

- **Tool permissioning & human oversight (verbatim):** Tools are model-controlled, "However, MCP emphasizes human oversight." Recommended mechanisms: "Displaying available tools in the UI... Approval dialogs for individual tool executions... Permission settings for pre-approving certain safe operations... Activity logs that show all tool executions." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- **Discovery + consent before action:** "Tools may require user consent prior to execution, helping to ensure users maintain control over actions taken by a model." (source: https://modelcontextprotocol.io/docs/learn/server-concepts)
- **Sampling is permission-gated at the client:** sampling "puts the client in complete control of user permissions and security measures," with human-in-the-loop checkpoints before and after the model call. (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- **Roots are advisory, not a security boundary:** "Roots serve as a coordination mechanism between clients and servers, not a security boundary... Actual security must be enforced at the operating system level, via file permissions and/or sandboxing." (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- **Trust the server before connecting (verbatim warning):** "Verify you trust each server before connecting it. Servers that fetch external content can expose you to prompt injection risk." (source: https://code.claude.com/docs/en/mcp) Project-scoped `.mcp.json` servers require explicit approval: "Claude Code prompts for approval before using project-scoped servers from `.mcp.json` files." (source: https://code.claude.com/docs/en/mcp)
- **Transport-level hardening:** Origin-header validation against DNS rebinding, localhost-only binding, and authentication on all connections (§5.4). (source: https://modelcontextprotocol.io/docs/concepts/transports)
- **Elicitation privacy guardrail:** "Elicitation never requests passwords or API keys." (source: https://modelcontextprotocol.io/docs/learn/client-concepts)
- **Self-served Claude Code caveat:** when exposing Claude Code via `claude mcp serve`, "your own client is responsible for implementing user confirmation for individual tool calls." (source: https://code.claude.com/docs/en/mcp)

---

## 10. How MCP Relates to Raw Tool Use  *(CCA-F D4; extends "The Tool-Use Agent Loop," D2)*

**One clean sentence (grounded):** MCP is a standardized packaging-and-transport layer over the same tool-use loop the learner already knows — when Claude decides to call an MCP tool, "the AI application intercepts the tool call, routes it to the appropriate MCP server, executes it, and returns the results back to the LLM as part of the conversation flow," exactly the discover->call->observe cycle of native tool use, but with `tools/list` / `tools/call` standardized across servers. (source: https://modelcontextprotocol.io/docs/learn/architecture)

Supporting detail: the host "fetches available tools from all connected MCP servers and combines them into a unified tool registry that the language model can access," so from the model's perspective MCP tools and natively-defined tools are indistinguishable. (source: https://modelcontextprotocol.io/docs/learn/architecture) On the Messages API, this is literally true — MCP tools flow through the same tool-use machinery, surfacing as `mcp_tool_use` / `mcp_tool_result` blocks parallel to ordinary `tool_use` / `tool_result`. (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)

---

## Final `[VERIFY]` List (version-sensitive / uncertain facts)

1. **Current canonical protocol version string — ✓ VERIFIED 2026-06-06, ✓ RE-CONFIRMED 2026-06-09 = `2025-11-25`** (confirmed at https://modelcontextprotocol.io/specification/latest). `2025-06-18` and `2025-03-26` are prior revisions; `2025-03-26` remains the documented backwards-compatibility fallback default. Re-verify before exam day. (sources: https://modelcontextprotocol.io/specification/latest ; https://modelcontextprotocol.io/docs/concepts/transports ; https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
2. **MCP connector beta header.** Current = `mcp-client-2025-11-20`; previous `mcp-client-2025-04-04` is deprecated. Beta headers rotate — re-verify before publishing. (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
3. **Maturity of client primitives.** "Tasks" is explicitly "(Experimental)." Sampling, Elicitation, and Roots appear as standard features in current docs with no experimental label, but stability across spec revisions is version-sensitive — confirm GA status against the dated spec. (source: https://modelcontextprotocol.io/docs/learn/architecture ; https://modelcontextprotocol.io/docs/learn/client-concepts)
4. **Transport naming/status.** "Streamable HTTP" is the current remote standard; standalone "HTTP+SSE" (protocol version 2024-11-05) is deprecated but SSE persists *within* Streamable HTTP. Re-verify the deprecation has not progressed to removal. (source: https://modelcontextprotocol.io/docs/concepts/transports)
5. **MCP connector platform availability.** "Not currently available on Amazon Bedrock or Vertex AI" — availability matrix is subject to change. (source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
6. **`tools/call` content types & `resources/subscribe`.** Some response/notification shapes (e.g., the full content-type enumeration, `resources/unsubscribe`, completion methods) were not separately fetched from the dated spec; if the lesson asserts the complete method set, cross-check https://modelcontextprotocol.io/specification/latest.
