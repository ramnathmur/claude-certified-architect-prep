A firm needs the ability to check a customer's credit before it signs a contract.

It has four ways to get one. It can use the check its accounting package already ships with. It can pay a developer to write one against the credit bureau's API. It can write down the procedure its analysts already follow and put it in the handbook. Or it can subscribe to a credit-checking service that other firms also use, run by someone whose whole business is keeping it current.

Those four are not four flavours of the same thing. They differ on one question: who owns the capability when it changes. The packaged check is owned by the vendor. The developer's script is owned by you. The handbook procedure is owned by whoever wrote it, and it does not do anything — it tells a person what to do. The subscription is owned by the service, and the same service can be used by the sales team, the risk team and both subsidiaries.

Claude has the same four, and they map exactly.

A **built-in tool** is one Anthropic ships and runs. You turn it on. You do not write a schema and you do not run the code. You accept what it does.

A **custom tool** is a schema you write plus a function your application runs. You own the description, the parameters, the execution, and every change to any of them.

A **Skill** is a markdown file with a description. Claude loads it when the description matches the task. A Skill carries instructions — a procedure, a standard, a house style. It does not execute anything itself. It tells Claude how to proceed, and Claude then uses whatever tools it has.

An **MCP server** is a separate process that publishes tools, resources and prompts. Any MCP client can connect to it. You build it once, and Claude Code, your own application and a teammate's application all get the same tools without any of them rebuilding the integration.

Now derive the rule. Two questions, in order.

First: does the capability *do* something, or does it *tell Claude how* to do something? If it tells, it is a Skill, and the other three are wrong however convenient they look. A procedure written as a tool is a tool that returns a paragraph of advice, which is a Skill wearing a costume.

Second, if it does something: how many callers need it, and who keeps it current? One application and you own the logic — custom tool. Anthropic already runs it and its behaviour is acceptable — built-in tool. More than one client needs it, or it must be maintained against somebody else's changing API — MCP server.

Now break it. A team needs Claude to fetch pages from the open web, inside one internal application. The surface features say MCP: it is an integration, it reaches outside the company, integrations are what MCP is for. The mechanism says no. Nobody else needs it. Nothing needs maintaining against a third party's API. Anthropic already ships and runs a web search tool. Turning that on is the answer. Building an MCP server here buys a process to operate and a tool list occupying the context window, in exchange for nothing.

The tell in a scenario stem is the word *reusable*, or any phrase naming a second consumer — "across several applications", "the other teams need it too", "maintained independently". That phrase is what moves the answer from custom tool to MCP server. Without it, MCP is the bigger hammer.
