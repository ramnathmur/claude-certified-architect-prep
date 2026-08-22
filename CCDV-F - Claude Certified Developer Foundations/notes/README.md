# notes/

Working notes. One file per official lesson, one per new prerequisite course, plus one per Tier-2
reading block.

## Naming

`L1_MSO-Foundations.md` … `L4_Production-Engineering-Evals-Security.md` for the four **examinable**
official lessons. **Lesson 5, "Accelerators & IP Contribution", is not on the blueprint** — no note
needed, and no need to watch it.
`SELF-ASSESSMENT_v1.md` for the 25-skill self-assessment, which the guide names as the first prep step.
`P1_Claude-Code-101.md`, `P2_Claude-Platform-101.md`, `P3_MCP-Advanced-Topics.md` for the three
prerequisite courses the CCAR-F run did not cover.
`T2A_Messages-API.md`, `T2B_Agent-SDK.md`, `T2C_MCP-Spec.md`, and so on for the reading.

## How to write them

Notes are raw material for the corpus, so write them in the shape the corpus needs. A note that
summarises a lesson is close to useless; a note that captures a decision is directly convertible.

For every idea worth keeping, record:

- **The decision it governs** — "given X, do Y rather than Z"
- **The discriminator** — the one factor that decides between Y and Z
- **The cost, failure mode, or constraint** that makes it a production answer rather than a tutorial one
- **The wrong belief it corrects**, written the way someone would actually say it

## Write for the decision, not the syntax

The official guide's sample items are scenarios with four options and no code. What is scored is
whether you match a technique to a stated constraint — *cost is the primary concern*, *results are not
needed until morning*, *reusable across several applications*.

So a useful note records **the constraint that selects this approach over its neighbours**, not the
call signature.

- Good: "Batch API when the workload is latency-tolerant and cost-primary; sync when a user is
  waiting. Parallelising sync calls does not reduce per-token cost."
- Less useful: the exact shape of the batch request body.

Record what breaks when the approach is wrong, not just what is correct. Failure modes are examinable
and they stick better than signatures.

**Where code still earns a note:** when the decision is *about* the code — schema shape, defensive
parsing, error-handling and recovery strategy, streaming versus not. Even there, note which approach
and why, not what the parameter is called.

## Provenance

Every note states its source at the top — lesson name and timestamp, or URL and retrieval date.
Community sources are labelled as such. A note without provenance cannot feed the corpus, because the
corpus can only be generated from verified material.

MCP notes do **not** need a specification revision recorded. The guide names no revision, and the
published MCP scope is conceptual — resources, tools and prompts; stdio vs sockets; client vs server.
Learn those; leave spec-version trivia alone.
