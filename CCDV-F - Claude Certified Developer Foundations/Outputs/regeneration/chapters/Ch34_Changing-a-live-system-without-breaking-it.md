# Chapter 34: Changing a live system without breaking it

## One lane closed, five open

A six-lane bridge needs a new deck, and the road beneath it carries forty thousand cars a day that cannot be told to wait. The crew never closes the bridge. They close one lane, build a section of the new deck on falsework beside the old one, tie it in, load-test that section alone, and reopen it before moving to the next lane. At every point in the project, five lanes are carrying live traffic and the one under work can be reopened to its old state in the time it takes to pull the barriers back. No stage risks the whole crossing at once, and no stage depends on the next stage having gone well.

That is the entire discipline this chapter teaches, applied to software instead of concrete: a change to a system already serving traffic is safe in proportion to how small a piece of the whole it touches at once, and how quickly that piece can be put back the way it was. Everything below is a variation on that one constraint.

## Four names for four kinds of change

A system's life divides into four kinds of work, and a scenario stem naming one of them is asking about the specific risks and controls that stage carries.

**Developing** is writing the change before anyone downstream depends on it: requirements, design, the code itself, on a branch nobody else is running in production.

**Implementing** is landing that change where it starts to matter: merging it, deploying it, promoting it through the environments between a laptop and production traffic.

**Operating** is running the system as it serves real requests: the thing is live, traffic is flowing across it, and nothing about today's work started as a planned change.

**Maintaining** is correcting or evolving the system after it is already live, in response to a defect, a new requirement, or something that shifted underneath it without anyone touching the code at all.

No single named industry framework uses exactly these four words as one list. The closest real match is ISO/IEC/IEEE 12207's technical processes, which separately name Implementation, Operation, and Maintenance, with the pre-implementation work (requirements, architecture, design) folded under one heading the standard's own earlier edition called Development. Other frameworks split the same territory differently: ITIL's current edition merges operate and maintain into one activity called Deliver & Support, and the DevOps loop distributes maintenance across its whole eight-phase cycle rather than naming it once. Four distinct names for four distinct sets of risk is a teaching compression of real, if variously labeled, territory; no single framework checked spells it out in exactly this wording.

## What keeps a small change small

Two mechanisms do the work of the bridge's one-lane-at-a-time discipline for software, and they operate at develop and implement.

The first is version control. It is not a backup system; it is, in the words of Google's own DevOps research program, "our safety net. It allows us to revert AI-generated mistakes instantly and gives us a history we can audit." That safety net covers more than application code: database schema scripts, environment-creation tooling, deployment scripts, and even AI artifacts such as prompts and agent configuration files belong in it too, because any of them can be the thing that has to be reverted. The practice that keeps this safety net small enough to trust is trunk-based development: each engineer merges a small batch of work into the shared line at least once a day rather than accumulating a large branch, which keeps every individual, committed change small enough to reason about and revert cleanly.

The second is refactoring, in its precise sense. Martin Fowler's definition: "a controlled technique for improving the design of an existing code base," applying "a series of small behavior-preserving transformations, each of which is 'too small to be worth doing.'" The discriminator is in that phrase: behavior-preserving. A change that fixes a bug or adds a capability is not a refactoring under this definition, however minor the edit looks, because refactoring's whole safety case rests on the observable behavior never moving. A team that calls every code change a "refactor" is using the word loosely; the technique itself only applies to the subset of changes where nothing external can tell the difference before and after.

Both mechanisms assume the same thing the bridge crew assumes: the piece of work in front of you is small enough to commit, test, and revert as one atomic unit.

## When small stops being available

That assumption breaks at scale, and the organization that documented where is Google, in its own engineering practices for what it calls Large-Scale Changes: any set of logically related edits that cannot be submitted as one atomic commit, either because they touch more files than the version-control system can commit together or because merge conflicts become unavoidable if the team tries. The chapter's own finding on why this is a different problem rather than a bigger version of the same one: as a codebase and its engineering population grow, "the maximum size of atomic changes actually decreases," so the ordinary small-step discipline becomes least available exactly where a change is most sweeping.

The documented response is not "be extra careful this time." It is a different set of practices: automate the change instead of hand-editing each call site; shard the one logical change into many small, independently testable pieces, so each shard is small in Fowler's sense even though the aggregate is not; run transitive test coverage on every shard; put a centralized team in charge rather than leaving the migration as an unfunded mandate on every downstream team; and add a prevention check that blocks the old pattern from creeping back in once the migration lands.

## The bridge that skipped its stages

Now assume a team's ordinary safety net has already failed. A financial-services company needs to modernize a legacy codebase: old framework, undocumented dependencies, code nobody currently on the team wrote. Under time pressure, an engineer points an AI coding agent at the whole repository with a single broad instruction and lets it run without plan review, without a hook restricting which paths it can touch, and without pausing between stages of the change. The surface feature says this is routine maintenance: it is a framework upgrade, the kind of change that ships every quarter. The mechanism disagrees. A change of unknown scope, applied to code with unknown dependencies, by an agent with no boundary on what it can edit, is the bridge crew closing all six lanes at once and hoping the falsework holds.

The documented response to exactly this situation ties the tools from earlier in the course to the blast-radius discipline above: hold the agent in a read-only explore phase with plan mode while the team builds confidence in its proposed edits, review the plan before a single file changes, enforce which paths cannot be touched during the sensitive phases with a hook, and carry the target conventions in a file the agent reads on every turn so it does not drift back to the legacy patterns sitting in the surrounding code. Before the session starts, three questions get answered: "What is the blast radius if something goes wrong: which systems depend on the code being changed, and what breaks downstream if an edit is wrong? How are changes audited: is there a PostToolUse hook logging every tool call, and does that log satisfy whoever needs to review what the agent touched? Who approves each phase before the next one begins?" None of the three questions is specific to legacy modernization. They are the same three questions the bridge crew answers before closing a lane, asked of a codebase instead of a road deck.

## SDLC integration: the same mechanism, run continuously

Read together, develop-and-implement and operate-and-maintain are not two different disciplines; they are the same one, applied to different situations. At develop and implement, small-scale refactoring and trunk-based version control are the documented safety mechanism: each change is small enough to be one atomic, revertible, reviewable unit. At operate and maintain, a correction to something already live has to be made either as another small, version-controlled, reviewed change (the same mechanism, run again) or, if the correction cannot be made atomic, as a Large-Scale Change, because the ordinary safety net stops covering a change of that size. A scenario that treats "the developer's safety practice" and "the operations team's change control" as two separate mechanisms is describing a division the same research specifically found unsupported: it is one mechanism, running continuously, promoted through environments with increasing control and reversible at every stage.

## Deriving why lateness costs more

Put the mechanism and the SDLC-integration picture together and a rule falls out. A decision caught in develop, before anyone downstream depends on it, costs one small, revertible commit to fix: nobody else's work has to move. A decision that survives into implement costs slightly more: it has to be pulled back out of a promotion pipeline rather than off a branch, but it is still one commit. A decision that survives all the way into operate or maintain costs the most, for two compounding reasons. First, the correction now has to be made against live traffic rather than an empty branch, so every safeguard from the bridge's staged-lane discipline has to hold under live traffic as well as it held in a test environment. Second, the longer a wrong decision goes uncorrected, the more other code and other teams build on top of it, which is exactly the condition under which Google's own research shows the maximum size of an atomic change shrinking. The fix that would have been one small commit at develop time can, by the time anyone notices at operate time, only be made safely as a sharded Large-Scale Change. Life-cycle frameworks exist to pull decisions as early as possible in that sequence, because the same decision, made at develop instead of discovered at maintain, is cheaper by construction, not by discipline applied harder after the fact.

## The change nobody committed

The bridge analogy holds for every mechanism above, but it assumes an inspector can see the whole structure before deciding whether a lane is safe to reopen. That assumption is where the analogy stops carrying weight, and where the maintain phase holds a risk none of the frameworks above name: a live system's behavior can shift without a single commit, a merge, or a deploy touching it, because the model underneath it changed instead of the code.

Claude is a family of models spanning several capability tiers, and the family evolves: model identifiers change, older ones are superseded, and the course material itself carries an explicit instruction to confirm the current lineup and model identifiers at build time rather than assume the ones learned once stay current. An application that references a model by a floating alias rather than a pinned identifier can serve different behavior on Tuesday than it served on Monday, with the codebase, the deployment history, and the audit log all showing no change at all. Version control cannot revert what it never recorded, and the staged-rollout discipline above cannot stage an event it was never told was coming.

The corrective mechanism is the same discipline, extended one step further. Pin the model identifier explicitly rather than trailing a "latest" alias, so a version change becomes a deliberate, committed edit to that identifier instead of a silent substitution. Treat a change to that pin exactly the way the course already treats a deliberate step up or down in model tier: gated on a measured score against your own hardest cases, promoted only when an eval confirms the new version holds the existing quality bar, and rolled back to the previous pinned identifier the moment it does not: one line, one commit, fully reversible. The eval is what makes the regression visible in the first place; without one, a model-version change and a quiet quality drift look identical, because both present the same way: the code is unchanged, and the answers are worse. This is the one part of "maintaining" a live system that has no equivalent in bridge maintenance, because a bridge's steel does not get replaced by the supplier while the deck is still open to traffic.

## What the neighboring chapters already cover

Two boundaries keep this chapter from sprawling into territory that belongs elsewhere. Least privilege and credential scoping is chapter 31's territory: the blast radius there comes from what an agent can authenticate as, a separate axis from the code-and-configuration blast radius this chapter has been walking. And the human gate this chapter's implement phase relies on is chapter 33's mechanism in full: a required review before a change merges, what an automated reviewer can establish, what it is only guessing at, and where the human sign-off sits. This chapter places that gate in the sequence above; chapter 33 teaches how it works.

## The phrase that flags this chapter

A stem naming "already in production," "cannot take the system offline," a fix that "touches every call site," or a system that "behaves differently and nothing in the deploy log changed" is asking which stage owns the risk and which mechanism matches the size of what actually has to move: a small revertible commit, a sharded large-scale change, or a pinned and eval-gated model version.

## Self-test

**1.** A team wants to know which stage of a live system's lifecycle is responsible for correcting a defect discovered after the system is already serving traffic. Which stage is that? *(Select one.)*

A. Developing.
B. Implementing.
C. Maintaining.
D. Requirements analysis.

**2.** An engineer changes a function's internal structure without altering any of its observable outputs, in order to make a later change easier. By Martin Fowler's definition, what is this? *(Select one.)*

A. A refactoring, because it preserves behavior while changing the code's internal design.
B. A bug fix, because any code change carries some risk.
C. A Large-Scale Change, because it touches more than one file.
D. Not a real engineering activity, since nothing observable changed.

**3.** A single logically-related edit needs to reach thousands of call sites across a large codebase, and the version-control system cannot commit it as one atomic unit. Which two practices does the documented discipline for this situation call for? *(Select 2 of 4.)*

A. Automating the change rather than hand-editing each call site.
B. Sharding the change into many small, independently testable pieces.
C. Committing the entire change as a single large pull request to preserve atomicity.
D. Skipping test coverage on the individual pieces since the aggregate change is what matters.

**4.** According to the DORA research cited in this chapter, what is version control's documented function beyond storing code? *(Select one.)*

A. It is a safety net that allows a team to revert mistakes instantly and provides an auditable history.
B. It replaces the need for automated testing before a change is promoted.
C. It is primarily a compliance requirement with no measured effect on delivery.
D. It applies only to application source code, and excludes infrastructure or configuration files.

**5.** Which practice keeps a version-controlled change small enough to revert cleanly, according to the trunk-based development research cited in this chapter? *(Select one.)*

A. Each developer merges a small batch of work into the shared trunk at least once a day.
B. Each developer maintains a long-lived branch until the full feature is complete.
C. Merges happen only at the end of each quarter, in one coordinated event.
D. Each team maintains its own separate trunk to avoid merge conflicts.

**6.** A team modernizing a legacy codebase with an AI coding agent asks three scoping questions before the session starts: what breaks downstream if an edit is wrong, whether changes are logged for audit, and who approves each phase. What is this chapter's term for the risk these three questions are managing? *(Select one.)*

A. Blast radius.
B. Latency budget.
C. Context window pressure.
D. Prompt injection.

**7.** An application references its underlying model by a floating "latest" alias rather than a pinned model identifier. Anthropic ships a new default version, and the application's answers change even though no commit, merge, or deploy touched the codebase. What does this chapter identify as the corrective mechanism? *(Select one.)*

A. Pin the model identifier explicitly, and gate any change to that pin on an eval confirming the new version holds the existing quality bar.
B. Disable version control for the model configuration, since it cannot track a change outside the codebase.
C. Wait for the next scheduled deployment window before investigating.
D. Treat the behavior change as a prompting problem and rewrite the system prompt.

**8.** Which two of the following are named as belonging in version control, per the DORA capability this chapter cites, beyond application source code? *(Select 2 of 4.)*
 
A. Database schema scripts and reference data.
B. Environment-creation tooling such as infrastructure-as-code files.
C. The contents of a production database's live customer records.
D. The private keys used to sign production releases.

**9.** A decision about how a system should behave is made and corrected while still on a development branch, before anything downstream depends on it. According to this chapter's derivation, why is this the cheapest point at which to correct it? *(Select one.)*

A. Because the correction is one small, revertible commit, and nothing else has yet been built on top of the decision.
B. Because code on a branch is not subject to any review process.
C. Because branches are automatically deleted after thirty days, forcing early correction.
D. Because the exam guide states development-phase changes carry no cost.

**10.** A scenario states that a large legacy system has been maintained for years using only small, trunk-based commits, each reviewed and revertible. It asks what risk this discipline, applied faithfully, still does not cover. Which answer matches this chapter's argument? *(Select one.)*

A. A behavior change caused by the underlying model version shifting without any commit to the system's own code.
B. A merge conflict between two feature branches.
C. A bug introduced by a single developer's typo.
D. A missing unit test for a new function.

**Answers.** 1: C. Maintaining is defined in this chapter as correcting or evolving a system already live; developing and implementing both precede the system carrying real traffic, and requirements analysis is upstream of all four stages. 2: A. Fowler's definition requires behavior preservation; B describes something that is not a refactoring by that definition regardless of size, C describes a different discipline entirely, and D contradicts the definition given. 3: A and B. Automation and sharding are the two documented practices quoted in this chapter; C is the opposite of the discipline (a single atomic commit is exactly what the situation rules out), and D drops the transitive test coverage the discipline specifically calls for. 4: A. The DORA material quoted names version control as a safety net enabling instant reversion and an auditable history; B, C, and D all contradict details the chapter states directly, including that the safety net's scope extends beyond application code. 5: A. Trunk-based development is defined as small, frequent merges into the shared line; B, C, and D each describe a practice this chapter's cited research associates with weaker delivery outcomes. 6: A. Blast radius is this chapter's term for how far a bad change reaches before it is caught, which is what all three scoping questions are managing. 7: A. Pinning the identifier and gating any change behind an eval is the corrective mechanism this chapter describes; B removes the wrong safeguard, C is not a documented response, and D misdiagnoses a model-version issue as a prompting issue. 8: A and B. Both are named explicitly in the version-control capability's own list; C and D are not, since live customer data and signing keys are not source-controlled artifacts under this definition. 9: A. The derivation in this chapter rests on nothing else having been built on the decision yet, making the correction cheap by construction; B, C, and D are not claims this chapter makes. 10: A. This is the chapter's stated gap: the discipline described governs commits, and a model-version change is not a commit, so the existing safety net does not see it; B, C, and D are all ordinary risks the described discipline already covers.
