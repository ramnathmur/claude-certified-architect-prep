# Chapter 31: Identity, Secrets, and the Reviewer's Three Questions

## A word you already think you understand

"Least privilege" has an obvious definition: give an account the fewest permissions it needs, and no more. That definition describes the wrong moment. Anthropic's own guidance states the control's actual purpose plainly: apply least privilege "so that a successful injection can do minimal damage." The control does not stop the injection. It assumes the injection already landed, and it exists for what happens next.

Hold that assumption for the rest of this chapter. An instruction slips past a model, or a developer leaves a shortcut in place a day longer than planned. From that point on, the only thing standing between the agent and real damage is what it can still reach — and what it can reach is set by the credentials it holds, not by the instructions it was given.

## The key that traveled with the file

A developer connecting Claude Code to a data-warehouse MCP server needed the setup working fast. The service-account key went straight into `.mcp.json`, inline, with a plan to move it to an environment variable before sharing the repo. The repo got committed and shared first. Within 48 hours three teammates had cloned it and a CI pipeline had triggered its own fresh clone, so the key existed in four places: the original machine, the teammates' machines, the CI runner, and the repository's own history. Rewriting the file to reference an environment variable afterward removed the key from the current version and left it sitting, readable, in every earlier commit. The service account had to be rotated, and the rotation broke two unrelated external services configured with the same key — three hours of unplanned work to recover from a shortcut meant to save ten minutes.

Nothing in that sequence required a sophisticated attacker. A key typed into a config file gets cloned, indexed, and cached wherever the file travels, the same as any other line of text. The fix that held was two layers together: a CLAUDE.md convention stating that credential values are never written inline to `.mcp.json`, backed by a PreToolUse hook that inspects writes and edits to that file for credential-shaped patterns and blocks the ones it finds. The convention states the intent. The hook runs regardless of whether the model remembered the convention that turn.

## A master key and a floor key

A building run properly issues two kinds of key. A master key exists, held by very few people, and opens every door. Everyone else carries a floor key that opens the one door their job actually requires. If a floor key is lost, whoever finds it can reach one floor. If the master key is lost, whoever finds it can reach the whole building, and no door in it was ever asking to be protected from that particular key in the first place.

The credential the warehouse agent held was a master key. It authenticated as a service account with no directory or resource restriction narrower than "the whole warehouse," so once it existed in four unintended places, all four were master-key incidents rather than floor-key ones. The agent's instructions never changed that. The instructions said what the agent was supposed to do; the credential said what it was actually able to do if something else went wrong — two different facts about the same system.

## Secrets and identity, one term at a time

The platform's documentation groups this territory under **secure-by-design**: privacy, identity and access management, and least privilege, named together as one umbrella rather than three unrelated topics. **IAM**, short for identity and access management, is the discipline that decides who or what an identity is, what it authenticates as, and what it is then authorized to do. **AuthN** answers the first question: is this actually the party it claims to be. **AuthZ** answers the second: given who it is, what is it allowed to touch. A Console admin choosing between the Claude Code role, which can only create Claude Code API keys, and the Developer role, which can create any kind of API key, is drawing a floor-key boundary around who gets to mint keys at all.

Credentials split cleanly along the dev-to-production line. A static API key is the documented fit for local development, prototyping, scripts, and single-tenant servers you already control. It is sent as the `x-api-key` header, or picked up automatically from the `ANTHROPIC_API_KEY` environment variable. Its expiration, if set, is fixed at creation and cannot be changed afterward, and an expired key cannot be reactivated — a new one has to replace it. The platform states the limit of that mechanism directly: "expiration limits the lifetime of a leaked credential, but it is not a substitute for secret hygiene."

Production workloads on a cloud platform, CI/CD pipelines, and Kubernetes get a different pattern. Workload Identity Federation exchanges a short-lived token from an identity provider you already trust for a Claude API access token that the SDK refreshes on its own. That provider can be AWS IAM, Google Cloud, GitHub Actions, or any standards-compliant OIDC issuer. The documentation states the resulting property outright: there is no long-lived key string to mint, distribute, or rotate, because nothing long-lived was issued. Federation still depends on the identity provider behind it, so it pairs with that provider's own controls rather than replacing the need for them.

Anthropic's best-practices guidance for the keys that still exist adds detail worth carrying rather than a fixed number: separate keys per environment so a leaked dev key cannot touch production, `.env` files kept out of source control, and rotation on a schedule — the guidance names 90 days as one example of such a schedule, not a mandated interval. GitHub's secret-scanning partnership with Anthropic catches one common failure automatically: a key detected in a public repository gets deactivated and its owner emailed, without anyone having to notice the leak first.

The pattern that removes the most risk keeps the key away from the agent entirely: a proxy sitting outside the agent's own security boundary injects credentials into outgoing requests, so the agent sends unauthenticated requests and never holds a value that could leak from its own context. The same reasoning covers what an agent may read. Files documented as unsafe to mount even read-only include `.env`, `~/.aws/credentials`, `~/.kube/config`, and any `*.pem` or `*.key` file, because read access to a directory is already enough to expose a credential sitting in it.

## Why the framing at the door still holds

Derive the rule from the master-key picture directly. Claude can only reach what the credential in front of it reaches, so the size of a compromise is bounded by the credential's scope. The platform's own restriction table names four resources to narrow this way: mount only the filesystem directories a task needs, and prefer read-only; restrict network reach to specific endpoints through a proxy; inject credentials through that proxy rather than exposing them directly; and drop system capabilities in a container down to what the task actually uses. Each row cuts the floor a stolen key opens onto down from the whole building.

## The room an injection still lands in

A team that has scoped an agent this way, filesystem read-only, network proxied and allowlisted, credentials injected rather than held, sometimes concludes prompt injection is no longer a risk for it. That conclusion inverts what the control is for. A perfectly scoped agent can still be manipulated into calling every tool it holds; the manipulation itself is chapter 29's mechanism, and narrower credentials do nothing to stop it from being attempted. What narrower credentials change is the outcome once the manipulation succeeds: the size of the room the injection lands in. A scoped agent's worst case is limited to that room. An unscoped agent's worst case is the whole building, reached by the same trick.

## Whose name is on the key, and who is still watching the door

Two more questions sit past scoping. The first is whose identity an action actually runs under. The documented spectrum runs from a system service account, self-contained with no human attached and revoked in one place, to a human-delegated credential, where an employee's own login carries the agent's actions and accountability blurs the moment nobody is watching that session closely. The stated reason to give an agent its own identity is single-point revocation: pulling one identity ends the agent's access everywhere it was used, and every action the agent took already appears in each connected system's own logs, under that identity, rather than buried inside one person's activity history.

The second question is whether the access still deserves to exist, checked on an ongoing basis rather than at the moment of one action. This is a different layer from the ones this course has already covered. Chapter 11's evaluation order and chapter 19's permission-mode checkpoint each decide whether one specific action is allowed to run, at the moment it is attempted. Access approval and authorized-access monitoring, in this chapter's sense, ask a standing question that outlives any single action: does this identity still hold access it should have lost, and would anyone notice if it didn't. The `claude_code.tool_decision` telemetry event, recording which of five sources approved or rejected each call, is one input to that standing question. The Compliance API answers it retrospectively, giving security and legal teams per-event records and retained transcripts to review after the fact. Inference hooks, still in beta, answer it inline, letting an organization's own security server see a governed prompt before inference and deny it in real time. OpenTelemetry streams the same category of signal continuously into a SIEM the organization runs itself. A stem asking to block a request before it reaches the model wants an inline hook's kind of answer; a stem asking how a security team learns, months later, who touched what wants the Compliance API's.

## Where the building analogy stops holding

A floor key that goes missing announces itself: the door it opened is now findable as an open risk, because someone can see the key is gone. A leaked digital credential announces nothing. It keeps authenticating exactly as before, silently, until a scan catches it in a public repository or an audit log shows it used somewhere it shouldn't be. That gap is why authorized-access monitoring earns its place beside scoping and identity: it is the mechanism in this chapter built for a failure that leaves no physical evidence.

Chapter 14 states the one rule that MCP configuration owns and stops there: never write a credential value inline to `.mcp.json`. This chapter owns the rest of the territory that rule sits inside — how a credential is issued, scoped, rotated, attributed to an identity, and watched, across every surface an agent touches.

## Two words in a stem that point here

"Traveled," "committed," or "still had access" in a stem points at scope and identity. "Audited," "after the fact," or "would anyone know" points at monitoring, a different mechanism from the ask-once approval this course covered in chapters 11 and 19.

## Self-test

**1.** A team is deploying an agent to a Kubernetes cluster in production, calling the Claude API as part of a CI/CD pipeline. Per the platform's documented guidance, which authentication method fits this workload best? *(Select one.)*

A. A static API key stored as a `CI_SECRET` environment variable and rotated manually each quarter.
B. Workload Identity Federation, exchanging a token from the cluster's existing identity provider for a short-lived Claude API token.
C. The same API key already used for local development, with an expiration set to `Never`.
D. `apiKeyHelper`, configured to read a static key from a mounted file.

**2.** A security review reports that an agent's tools are scoped to a single read-only directory and its network access runs through an allowlisted proxy, and concludes that prompt injection is no longer a risk for this agent. What is the error in that conclusion? *(Select one.)*

A. Least privilege is documented as a control that limits how much damage a successful injection can do, evaluated after a compromise has already occurred.
B. Read-only filesystem access has no effect on an agent's exposure to prompt injection.
C. Proxy-based network restriction only applies to outbound credentials, never to tool calls.
D. Scoping tools and scoping network access are the same control counted twice.

**3.** A compliance team wants to know, three months after the fact, exactly which files an agent's service-account identity touched across every connected system, with retained transcripts available for review. Which documented capability answers this? *(Select one.)*

A. A PreToolUse hook configured to block writes outside an approved path.
B. The Compliance API.
C. Claude Code's permission-mode ask/allow setting.
D. Workload Identity Federation.

**4.** An engineering lead proposes letting an agent act under a specific employee's own claude.ai login, reasoning that this makes the agent's actions easy to trace back to a person. What does the documented guidance on agent identity say this reasoning gets backwards? *(Select one.)*

A. The stated benefit of a dedicated service-account identity is single-point revocation and attribution in each connected system's own logs, a benefit a shared human login stops providing once the agent runs inside a session nobody is actively watching.
B. Employee logins cannot be used for automated systems under any circumstances.
C. A dedicated service-account identity cannot be revoked without also disabling the employee's own access.
D. Attribution only matters when a human directly performs the action.

**5.** A service-account key was committed to a repository inside a configuration file, then removed from the file in a later commit. What is the correct next step? *(Select 2 of 4.)*

A. Treat the key as compromised and rotate it, because removing it from the current file leaves it intact in commit history.
B. Confirm the fix is complete once the corrected file is committed, since the current version no longer contains the key.
C. Enable a PreToolUse hook, or an equivalent CI check, that blocks future writes of credential-shaped values to that file.
D. Wait for GitHub's secret-scanning partnership to flag the key before taking any action.

**Answers.** 1: B. The documented dev-vs-production split names Workload Identity Federation as the fit for CI/CD and Kubernetes specifically because it removes the long-lived key entirely; A and C keep a static key in production, and D still depends on a static key sitting in a file. 2: A. The guidance's own clause is that least privilege exists "so that a successful injection can do minimal damage" — a blast-radius control, evaluated after a compromise. B, C, and D each misstate what the scoping controls do rather than naming the team's actual error. 3: B. The Compliance API is the documented retrospective audit surface, giving per-event records and retained transcripts for exactly this review. A and C are one-time, per-action controls with no retained record, and D removes a credential rather than producing an audit trail. 4: A. The documented reason to give an agent its own identity is single-point revocation and attribution in downstream systems' native logs, a benefit a shared human login does not provide once the session runs unattended. B overstates the guidance, and C and D are not claims the source makes. 5: A and C. History retention means the key stays leaked regardless of the corrected commit, and a deterministic hook or CI check is what stops the pattern recurring. B repeats the exact mistake the sourced postmortem describes, and D relies on an external scan catching what the team already knows to be exposed.
