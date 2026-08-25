# Chapter 24: What an Application Remembers

## Two callers, one conversation

Two customers of the same support product called in on the same afternoon, each reading back lines from a conversation they never had. One quoted a refund policy the other had asked about that morning. Support pulled the record: both customers had, at some point, been dropped into the same application session — the one the assistant had opened for someone else entirely.

The team had built the assistant on the Agent SDK and tested it the straightforward way: one developer, one terminal, one application session running at a time, all week. Every test passed cleanly. In production, dozens of users hit the same deployment inside the same working directory, and a failure that testing could never have produced surfaced within a day.

## What Continue actually does

The application had wired a returning user back into their conversation using the SDK's Continue option. Continue does one thing: it finds the most recent application session written to disk in the current working directory and resumes it automatically. That is documented as the right choice for an app that runs one conversation at a time, because there is only ever one "most recent" session to find. With dozens of users writing application sessions into the same directory inside the same deployment, "most recent" stopped meaning "the one this user started" within the first production day. Whichever request landed last became the application session Continue handed to whoever asked next.

The application's own session, in the SDK's own terms, is the conversation history it accumulates while an agent works: the prompt, every tool call, every tool result, every response, written to disk automatically so the application can come back to it later. It does not cover the filesystem; file edits are tracked separately, through a mechanism called file checkpointing, so restoring a session restores what was said, not what changed on disk.

That disk write lands at a specific path, `~/.claude/projects/<encoded-cwd>/*.jsonl` — the same path, and the same files, the Claude Code CLI uses for its own session. The documentation states this plainly, on the page describing the Agent SDK's own storage. An application built on the SDK and a developer running the CLI in the same working directory read and write the same files by default. The distinction this course draws elsewhere, between the application's own session and the CLI's session, is a framing difference here — building a product around the mechanism versus using it at a terminal, not a separation at the storage layer.

Continue is one of three documented ways back into an application's own session. Resume takes a specific session ID captured earlier, the option the documentation names as required for a multi-user application, because it makes "whose session is this" an input instead of a guess. Fork copies a session's history into a new one and leaves the original untouched, for trying a different direction without losing the ability to go back. A fourth mode writes nothing at all: `persistSession: false` in TypeScript, or the `CLAUDE_CODE_SKIP_PROMPT_HISTORY` environment option in Python, for a task that should leave no application session behind at all.

## The hotel that never checks anyone out

Managed Agents sessions behave differently, and the difference is worth stating plainly: an agent instance in Claude's own hosted environment is a server-side resource with its own conversation history and its own sandbox, entirely separate from anything the SDK or the CLI stores locally.

That resource has four documented statuses. `idle` means it is waiting for input. `running` means it is actively working. `rescheduling` means a transient error is being retried automatically. `terminated` means it has ended, and it only reaches that status one of two ways: an unrecoverable error, or someone deliberately archiving it. A Managed Agents session that finishes its assigned work cleanly returns to `idle` and waits there, rather than terminating.

That single fact carries this chapter's anchor. Picture a hotel that never checks a guest out at the end of a stay: it keeps the room-temperature preference, the complaint about the air conditioner, the note about the extra pillow, indefinitely, because nobody ever told the front desk the stay was over. A Managed Agents session left `idle` behaves the same way: it keeps everything it was holding, history and sandbox alike, until something, a person or a policy, decides to end it.

Ending it is two different operations, and the choice matters. Archiving stops new input and keeps the record; a `running` session cannot be archived directly, it has to be interrupted and settle into `idle` first. Deleting removes the record and its events permanently, and it takes the sandbox with it: every file that session produced is deleted along with it, which the documentation states outright — download anything worth keeping before deleting. A third lever, a hard cost budget, pauses a session at a spending ceiling rather than ending it either way; raising or removing the ceiling resumes whatever paused there automatically.

## The same decision, for a shared plugin set

A team distributing a shared toolset faces a parallel design question: what a fresh clone of the project inherits by default, and who is allowed to add to it. `extraKnownMarketplaces` registers a marketplace automatically once a teammate trusts the project folder, no separate prompt required. `enabledPlugins` then lists which of that marketplace's plugins are on by default, in the form `"plugin-name@marketplace-name": true`. Both are ordinary, committed project settings, so a fresh clone inherits the same marketplace and the same default plugins without anyone configuring it by hand.

`strictKnownMarketplaces` sits one layer above both, in managed settings that a project's own configuration cannot override, and restricts which marketplaces can be added at all — from unrestricted by default, to a full block on every addition, to an allowlist of specific repositories or a wildcard on an organization's own repos, to a hostname pattern for a self-hosted git server. Two marketplaces tracking different refs of the same repository, assigned to different user groups through managed settings, give a team staged "stable" and "latest" rollouts without touching either marketplace's plugin list. And because a plugin's name is its stable install identifier, renaming one would break every existing install if the marketplace file did not carry the change forward: a `renames` entry maps the old name to the new one automatically, kept in place as an append-only record even after most people have migrated, so a rename does not turn into a `plugin-not-found` error for whoever has not updated yet.

## The decision that had to happen upstream

None of this was a bug that testing could have caught, because the choice underneath it was never wrong at small scale. Continue really does find the right application session when there is only one to find. What the support team skipped was deciding, before the integration existed, how a returning user's identity would be captured and handed back to the SDK — a session ID stored against a user record and passed to Resume, rather than inferred from whichever file on disk happens to be newest. A different application, built to process receipts under a fixed token budget, hit a comparable gap from another angle: its budget was sized against short test fixtures, and nobody had decided in advance what should happen to accumulated tool output once it had served its purpose. Both failures share a shape. A resource nobody set a policy for at design time gets discovered the hard way, once, at production scale.

The plugin side asks the same question about governance instead of identity. `extraKnownMarketplaces` and `enabledPlugins` decide what a new teammate inherits without anyone asking twice. `strictKnownMarketplaces` decides who can add to that set at all, and it has to exist before the first unreviewed marketplace ships, because a restriction added later in managed settings does not retroactively undo an addition a project file already made. In every case here, the fix once the failure surfaces is cheap. The decision that would have prevented it was cheaper still, and it had to happen earlier.

## Where the surface reading gets it backwards

A team watching its bill might assume a Managed Agents session sitting `idle` is effectively free, the same intuition that would say an empty hotel room off the books costs nothing while nobody is staying in it. An `idle` session keeps its full conversation history and its sandbox state indefinitely regardless: nothing about that status implies cleanup, and nothing archives it on its own. The room stays reserved, still holding every note anyone left in it, until archive or delete is called deliberately.

The second surface reading runs the other way. A team cleaning up finished work might expect deleting an old session to be the tidy, conservative choice, since "delete" sounds scoped to the session's own record. Deleting a Managed Agents session actually removes its events and its sandbox together: every file that session produced goes with it, and the documentation is explicit that the operation cannot be undone. Archiving preserves the history and stops new input; deleting destroys the history and everything the session wrote to disk. Picking between the two without knowing which the situation calls for is picking blind.

Here is where the hotel stops matching the mechanism. A hotel's front desk loses track of which preferences are current gradually, through neglect; the notes on file do not announce that they have gone stale. A Managed Agents session's status carries no such ambiguity: `idle`, `running`, `terminated` are exact, checkable states, and the platform always knows precisely what it is holding. What sat unresolved in both examples above was a policy nobody set: the platform tracked the status correctly the whole time and simply waited for someone to act on it.

## Where this chapter's authority stops

Compacting an application session that is still active is a separate, sourced mechanism at the Messages API level: it can automatically summarize older context once input tokens cross a trigger threshold and continue the conversation from that summary, and the documentation recommends exactly this for a long-running exchange where the user is still engaged. What the documentation does not state is when to stop compacting and end the conversation instead — that threshold is not published, and this chapter will not invent one. Chapter 8 owns the mechanics of what fills a context window and how compaction works; this chapter places compaction on the map only as a fourth lever alongside archive, delete, and budget-pause. The Claude Code CLI's own session, `/compact`, `/clear`, `/resume` at the terminal, belongs to chapter 20 and stays distinct from everything here except for the storage overlap already named above. Keeping a shared plugin set from breaking on an unreviewed upstream change is a version-pinning problem, semver ranges declared on each dependency, and chapter 21 owns that mechanism in full; this chapter covers only how a plugin set is distributed and governed across a team in the first place.

## The tell

A stem naming this chapter says an application session's identity has to survive concurrent users, or describes a session sitting untouched with nobody deciding whether to archive it, delete it, or keep paying for it, or asks how a team keeps a shared plugin set consistent across every new clone of a project.

## Self-test

**1.** A team builds a customer-support assistant on the Agent SDK. Multiple users will use the deployment concurrently, and each expects to return to their own conversation on a later visit. Which choice correctly captures that requirement? *(Select one.)*

A. Use Continue for every returning user, since it always finds the session that belongs to whoever is asking.
B. Capture a session ID per user at first contact and use Resume with that ID, since Continue only finds the most recent session in the working directory.
C. Use Fork at the start of every conversation, so each user works from an independent copy of the same base session.
D. Use `persistSession: false` so nothing is written to disk and no user can see another user's history.

**2.** A Managed Agents session finishes the task it was given and has nothing left to do. What status does it move to? *(Select one.)*

A. `terminated`, because its assigned work is complete.
B. `idle`, waiting for further input; only an unrecoverable error or an explicit archive moves a session to `terminated`.
C. `rescheduling`, until a new task is assigned to it.
D. It is deleted automatically after a short retention window.

**3.** A team has already downloaded everything it needs from a completed Managed Agents session and now wants to permanently remove it, including any files it produced, so it stops consuming storage. Which operation does that? *(Select one.)*

A. Archive the session; archiving removes the sandbox's files immediately.
B. Delete the session, since deletion permanently removes both the record and the sandbox's files together.
C. Leave the session `idle`; idle sessions are cleaned up automatically after a fixed period.
D. Lower the session's cost budget to zero, which deletes the sandbox once the budget is reached.

**4.** An admin needs to guarantee that engineers can only install plugins from one approved internal marketplace, with no exceptions even if an engineer edits their own project's `.claude/settings.json`. Which mechanism enforces that? *(Select one.)*

A. `enabledPlugins` in the project's `.claude/settings.json`.
B. `extraKnownMarketplaces` in the project's `.claude/settings.json`.
C. `strictKnownMarketplaces` in managed settings, which project configuration and individual users cannot override.
D. A `renames` entry in the marketplace's `marketplace.json`.

**5.** Which two of the following are the only documented ways a Managed Agents session reaches `terminated` status? *(Select two of four.)*

A. An unrecoverable error occurs during the session.
B. The session is explicitly archived.
C. The session finishes the work it was given.
D. The session's cost budget is reached.

---

**Answers.**

1: B. Continue resolves to whichever session was most recently written in the shared directory, which is exactly the mechanism that put two customers in one conversation; a captured session ID passed to Resume makes ownership explicit rather than inferred. Fork starts a new branch from an existing session rather than routing a returning user to their own, and disabling persistence loses every user's history rather than scoping it correctly.

2: B. A session that completes its work returns to `idle` and waits; it does not terminate on its own. Only an unrecoverable error or a deliberate archive moves it to `terminated`, which is the fact behind this chapter's anchor: nothing ends automatically just because the work is done.

3: B. Archiving stops new input while preserving the record — it does not touch the sandbox's files, and in fact cannot be applied to a session that is still `running`. Deletion is the operation that removes both the record and every file the session produced, permanently, which is why the documentation says to download anything worth keeping first. Idle sessions are not cleaned up automatically, and a cost budget pauses a session rather than deleting anything.

4: C. `strictKnownMarketplaces` lives in managed settings, the one layer individual users and project configuration cannot override, which is exactly what "no exceptions" requires. `enabledPlugins` and `extraKnownMarketplaces` are ordinary project settings an engineer could still edit locally, and `renames` only handles a plugin's identity surviving a rename.

5: A and B. An unrecoverable error and an explicit archive are the only two documented paths to `terminated`. Finishing the assigned work returns a session to `idle` instead, and reaching a cost budget pauses a session rather than ending it either way.
