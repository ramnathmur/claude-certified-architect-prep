"""Rewrite the 16 stems the archetype gate flagged at/above 0.40 Jaccard against prior
exams, plus two repeated in-block closing sentences and two name-detector hits.

Root cause is PB-23 exactly: this session read Exam 13's full 60-stem header ledger while
studying the HTML template, so prior framings were in the drafting context. The corpus
point of each question is kept; the situation is rebuilt from scratch.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

REPLACEMENTS = {
9: {
 "stem": "The orchestrator returns to the caller as soon as a response contains any text block. On requests needing two lookups, callers get the agent's narration of what it intends to do, and the second tool never runs. `stop_reason` on those responses reads `tool_use`. What is the defect?",
 "options": [
  "The agent should be prompted not to narrate its intentions before calling a tool.",
  "Text and `tool_use` blocks should never share a response; the request needs adjusting.",
  "Termination is being decided on content rather than on `stop_reason`, where `tool_use` means continue.",
  "The second lookup depends on the first, so the pair should be declared as one composite tool."],
 "correct": 2,
 "whyRight": {"text": "The orchestrator inspects `stop_reason` after each call to decide whether to continue: `tool_use` means execute the tools, append the results and call again; `end_turn` means stop. Deciding on text content instead ends the loop while Claude is still mid-task.", "cite": "CCA-Prep_Domain-1_v2.md §1.1"},
 "whyWrong": [
  {"option": 0, "text": "Narration alongside a tool call is normal and harmless. The defect is that the orchestrator treats its presence as a completion signal.", "cite": "CCA-Prep_Domain-1_v2.md §1.1"},
  {"option": 1, "text": "A response may legitimately contain both. Suppressing text would mask the symptom while leaving loop control keyed to the wrong field.", "cite": "CCA-Prep_Domain-1_v2.md §1.1"},
  {"option": 3, "text": "Nothing indicates the lookups are coupled, and a composite would not help — the loop would still exit on the first response containing text.", "cite": "CCA-Prep_Domain-2_v2.md §2.8"}]},

14: {
 "stem": "One engineer wants to trial an experimental demand-forecast MCP server for a fortnight without changing anyone else's setup, while the team's four production servers must stay byte-identical for all forty operators and visible in code review. Which two statements are correct? Select two.",
 "options": [
  "The experimental server belongs in that engineer's `~/.claude.json`, which is not shared through version control.",
  "The four production servers stay in the project's `.mcp.json`, which is version-controlled and shared.",
  "Adding the experimental server to `.mcp.json` and gitignoring that file keeps the trial private.",
  "Project and user scope cannot both be active, so the trial requires removing the shared configuration first.",
  "An experimental server must be declared in both scopes for tool discovery to resolve it."],
 "correct": [0, 1],
 "whyRight": {"text": "`.mcp.json` at the project root is the shared, version-controlled configuration; `~/.claude.json` in the user's home is for personal overrides, personal auth and experimental servers. The two scopes exist precisely so a private trial and a shared baseline can coexist.", "cite": "CCA-Prep_Domain-2_v2.md §2.6"},
 "whyWrong": [
  {"option": 2, "text": "Gitignoring `.mcp.json` un-shares the four production servers too, which is the opposite of the stated requirement that they stay identical and reviewable.", "cite": "CCA-Prep_Domain-2_v2.md §2.6"},
  {"option": 3, "text": "Both scopes are active together — that is the design. Tools from all configured servers are discovered at connection time.", "cite": "CCA-Prep_Domain-2_v2.md §2.6"},
  {"option": 4, "text": "A single declaration in the appropriate scope is sufficient. Duplicating it across both invites exactly the drift the split is meant to prevent.", "cite": "CCA-Prep_Domain-2_v2.md §2.6"}]},

18: {
 "stem": "A single-file fix arrives with a stack trace pointing at the exact line and a one-line reproduction. The team's rule, written after a costly migration went wrong, is to use plan mode for everything. The fix takes twenty minutes; producing and reviewing its plan takes forty. What does the rule get wrong?",
 "options": [
  "Nothing — a uniform rule is worth the overhead because it removes a judgement call from every task.",
  "Plan mode should apply to any change crossing a package boundary, whatever its size.",
  "The rule is sound but plans for small changes should be correspondingly shorter.",
  "Mode follows scope and design ambiguity; a defined fix with a known approach calls for direct execution."],
 "correct": 3,
 "whyRight": {"text": "Planning mode is for large scope, architectural decisions and situations where several approaches are viable. A single-file fix with a clear stack trace has defined scope and a known approach — the corpus's own example of direct execution.", "cite": "CCA-Prep_Domain-3_v2.md §3.6"},
 "whyWrong": [
  {"option": 0, "text": "The judgement being removed is the one that determines whether the overhead is worth paying. A rule that doubles the cost of every small fix is not free.", "cite": "CCA-Prep_Domain-3_v2.md §3.6"},
  {"option": 1, "text": "Package boundaries are a proxy for scope, not scope itself. A trivial cross-package rename needs no plan; a complex single-package redesign does.", "cite": "CCA-Prep_Domain-3_v2.md §3.6"},
  {"option": 2, "text": "A shorter plan for a task that needs none is still pure overhead, and it keeps the mode decision detached from the properties that should drive it.", "cite": "CCA-Prep_Domain-3_v2.md §3.6"}]},

19: {
 "stem": "A `/fare-lint` command ships in the repository and every engineer receives it on clone. One wants to run it against a single fare zone at a time rather than editing the command file before each run, so the zone has to arrive at invocation. What does the command file need?",
 "options": [
  "A separate command file per zone, each with its zone identifier written in.",
  "`$ARGUMENTS`, which carries whatever text is typed after the command name.",
  "An `argument-hint` entry, which supplies the zone value when the command runs.",
  "A personal copy under `~/.claude/commands/` that she can edit freely between runs."],
 "correct": 1,
 "whyRight": {"text": "The text typed after the command name is available as `$ARGUMENTS` inside the command file. That is the mechanism for parameterising a shared command without forking it.", "cite": "CCA-Prep_Domain-3_v2.md §3.4"},
 "whyWrong": [
  {"option": 0, "text": "One file per zone multiplies maintenance across every zone and every future change to the lint itself, to avoid a substitution the command file already supports.", "cite": "CCA-Prep_Domain-3_v2.md §3.4"},
  {"option": 2, "text": "`argument-hint` is displayed when invoking the command to prompt for required arguments. It describes the expected input; it does not carry the value.", "cite": "CCA-Prep_Domain-3_v2.md §3.3"},
  {"option": 3, "text": "A personal copy re-creates the per-engineer divergence a shared command exists to prevent, and still requires editing before each run.", "cite": "CCA-Prep_Domain-3_v2.md §3.5"}]},

21: {
 "stem": "A reviewer asks where a skill's tool scoping is configured. One engineer proposes the project's `.mcp.json`, alongside the server definitions; another suggests the root `CLAUDE.md`, since it loads every session. Neither is correct. Where does it belong, and what does that key actually do?",
 "options": [
  "In `.mcp.json`, which governs every capability a session can reach, built-in tools included.",
  "In `CLAUDE.md`, which is always in force and therefore binds the skill while it runs.",
  "In the skill's `SKILL.md` frontmatter, via `allowed-tools`, which scopes what the skill may do.",
  "In the skill's body, as a natural-language constraint the model observes during execution."],
 "correct": 2,
 "whyRight": {"text": "`allowed-tools` in SKILL.md frontmatter is the key that scopes a skill's capabilities — the exam guide's framing is that it restricts tool access during skill execution, for example limiting to file writes to prevent destructive actions.", "cite": "CCA-Prep_Domain-3_v2.md §3.3"},
 "whyWrong": [
  {"option": 0, "text": "`.mcp.json` configures MCP servers and says nothing about which built-in tools a skill may use. This is a named misconception about where scoping lives.", "cite": "CCA-Prep_Domain-3_v2.md §3.3"},
  {"option": 1, "text": "`CLAUDE.md` is always loaded, but loaded guidance is not a capability boundary. Being in force and being enforceable are different things.", "cite": "CCA-Prep_Domain-3_v2.md §3.3"},
  {"option": 3, "text": "A constraint written in prose is probabilistic. Frontmatter is the declarative mechanism, which is the whole reason the key exists.", "cite": "CCA-Prep_Domain-3_v2.md §3.3"}]},

23: {
 "stem": "Eleven hours into cataloguing undocumented fare rules, the agent begins describing \"typical rounding conventions\" rather than the specific rules it identified in hour three, and two later summaries contradict its own earlier findings. Nothing has crashed and the session is still running. What addresses this?",
 "options": [
  "Restart the session, since the accumulated context has become actively misleading.",
  "Raise the summarisation threshold so the early findings survive compression for longer.",
  "Ask the agent to re-read its own earlier messages before producing each new summary.",
  "Write findings to a scratchpad file as they are established and read it back at each continuation."],
 "correct": 3,
 "whyRight": {"text": "Writing intermediate state and key findings to a scratchpad rather than holding them in context is what counteracts context degradation — the failure where the model starts giving inconsistent answers and referencing typical patterns instead of the specific things it discovered earlier.", "cite": "CCA-Prep_Domain-5_v2.md §5.12"},
 "whyWrong": [
  {"option": 0, "text": "Restarting discards eleven hours of findings that were never written down anywhere. It resolves the degradation by destroying the work.", "cite": "CCA-Prep_Domain-5_v2.md §5.12"},
  {"option": 1, "text": "The findings are still in context — that is why the agent can contradict them. Preserving more of a degrading context does not restore its reliability.", "cite": "CCA-Prep_Domain-5_v2.md §5.12"},
  {"option": 2, "text": "Re-reading asks the degrading context to police itself, and it grows more expensive with every turn while the underlying drift continues.", "cite": "CCA-Prep_Domain-5_v2.md §5.12"}]},

25: {
 "stem": "Your `.claude/rules/` directory has grown to fourteen files. A developer notices that a session touching one fares-engine file loaded only two of them, and asks whether the other twelve were skipped in error. Which three statements are correct? Select three.",
 "options": [
  "Rules load automatically only when Claude works on files matching their glob patterns.",
  "Keeping irrelevant rules out of context is the intended behaviour, not a fault to correct.",
  "A convention that should apply everywhere belongs in `CLAUDE.md` rather than behind a glob.",
  "All fourteen load every session; only the two matching ones were shown in the session log.",
  "Rules load in filename order until a token budget is reached, and the rest are dropped.",
  "A file matching no rule glob causes the root `CLAUDE.md` to be skipped for that session too."],
 "correct": [0, 1, 2],
 "whyRight": {"text": "Rules files carry glob frontmatter and load only when Claude works on matching files, which keeps irrelevant rules out of context and saves tokens. Conventions that apply always belong in the root `CLAUDE.md`, which is the split the two mechanisms exist to express.", "cite": "CCA-Prep_Domain-3_v2.md §3.2"},
 "whyWrong": [
  {"option": 3, "text": "Loading is conditional on the glob match, not merely reported that way. Twelve non-matching rules genuinely do not enter context.", "cite": "CCA-Prep_Domain-3_v2.md §3.2"},
  {"option": 4, "text": "There is no filename-order token budget. Selection is by path match, which is what makes it deterministic rather than incidental.", "cite": "CCA-Prep_Domain-3_v2.md §3.2"},
  {"option": 5, "text": "`CLAUDE.md` files are discovered and concatenated independently of any rules match. The two mechanisms do not gate each other.", "cite": "CCA-Prep_Domain-3_v2.md §3.1"}]},

26: {
 "stem": "A gate-fault investigation thread has run to ninety turns. It contains a confirmed firmware version, two station identifiers where the fault reproduces, an agreed rollback threshold, and a great deal of discussion about maintenance windows. The window is filling. What should be kept, and how?",
 "options": [
  "Summarise the whole thread uniformly, so no part of the investigation is privileged over another.",
  "Keep the twenty most recent turns verbatim and drop everything preceding them.",
  "Hold the version, identifiers and threshold verbatim in a structured block, summarise the scheduling discussion, keep recent turns.",
  "Move the entire thread to a scratchpad file and continue in a fresh session with no carried context."],
 "correct": 2,
 "whyRight": {"text": "The hybrid approach: extract the critical structured data — versions, identifiers, agreed thresholds — into a compact block preserved verbatim, compress the low-density discussion, and keep recent exchanges intact for coherence.", "cite": "CCA-Prep_Domain-5_v2.md §5.3"},
 "whyWrong": [
  {"option": 0, "text": "Uniform summarisation destroys precision exactly where it matters. \"A rollback threshold was agreed\" cannot tell the next step what the number is.", "cite": "CCA-Prep_Domain-5_v2.md §5.3"},
  {"option": 1, "text": "A recency window discards the firmware version and station identifiers if they were established early, which after ninety turns is likely.", "cite": "CCA-Prep_Domain-5_v2.md §5.3"},
  {"option": 3, "text": "A scratchpad is right for state that must survive sessions, but discarding all conversational context mid-investigation loses the reasoning the remaining work builds on.", "cite": "CCA-Prep_Domain-5_v2.md §5.12"}]},

27: {
 "stem": "An engineer objects to moving the overnight client-regeneration job onto the Message Batches API, arguing that batch requests cannot define tools and the job needs a schema-lookup tool partway through its analysis. What is the accurate position?",
 "options": [
  "Batch requests do support tools and multi-turn histories; what they cannot do is pause mid-request for a client to return a tool result.",
  "The engineer is right — batch rejects any request payload containing a `tools` array.",
  "Batch supports tools only when `tool_choice` is set to `none` for the whole request.",
  "Tools work in batch, and a client may return results mid-request provided it responds inside the window."],
 "correct": 0,
 "whyRight": {"text": "A batch request's parameters are the same as a regular Messages API call, tools and multi-message histories included, and older material claiming otherwise is wrong. The real constraint is that each request is one shot: if the model responds with `tool_use`, that request completes there, and continuing needs a follow-up submission.",
  "cite": "CCA-Prep_Domain-4_v2.md §4.11"},
 "whyWrong": [
  {"option": 1, "text": "This is the outdated claim the corpus explicitly corrects. Batch payloads accept a `tools` array.", "cite": "CCA-Prep_Domain-4_v2.md §4.11"},
  {"option": 2, "text": "`tool_choice: none` would prevent tool use rather than enable it, and no such condition is attached to batch support.", "cite": "CCA-Prep_Domain-4_v2.md §4.11"},
  {"option": 3, "text": "The first half is right and the second is the exact thing batch cannot do. There is no window inside which a client can answer a mid-request tool call.", "cite": "CCA-Prep_Domain-4_v2.md §4.11"}]},

37: {
 "stem": "The cleanup worker runs from a nightly scheduled job that must exit without a terminal and emit machine-readable output for the tracker. Today the job hangs until the runner's timeout, and on the occasions it is run by hand its output is prose. Which pair of changes fixes both faults?",
 "options": [
  "`--output-format json` alone, which also causes the process to exit once output is written.",
  "`-p` alone, which prints structured output by default whenever no terminal is attached.",
  "`-p` for non-interactive execution, plus `--output-format json` with `--json-schema` for parseable output.",
  "A wrapper that terminates the process once output appears and parses whatever was printed."],
 "correct": 2,
 "whyRight": {"text": "Two separate faults need two separate flags. `-p` processes the prompt, prints to stdout and exits — without it Claude Code waits for interactive input and the pipeline hangs. `--output-format json` with `--json-schema` is what makes the output reliably parseable.", "cite": "CCA-Prep_Domain-3_v2.md §3.8"},
 "whyWrong": [
  {"option": 0, "text": "Output formatting does not imply non-interactive execution. The job would still wait for input it never receives.", "cite": "CCA-Prep_Domain-3_v2.md §3.8"},
  {"option": 1, "text": "`-p` fixes the hang but says nothing about output shape. Prose would keep arriving, correctly and non-interactively.", "cite": "CCA-Prep_Domain-3_v2.md §3.9"},
  {"option": 3, "text": "Killing a process on first output and parsing whatever appeared is a workaround for both faults that guarantees neither, and it truncates any output still being written.", "cite": "CCA-Prep_Domain-3_v2.md §3.8"}]},

40: {
 "stem": "The team now routes generated code to a second instance for review. To improve that review, the second instance is given the generator's full conversation — reasoning, rejected alternatives and all — on the argument that context makes a reviewer better informed. Defects still reach production at the previous rate. Why?",
 "options": [
  "The reviewing instance lacks explicit review criteria, which the generator's context does not supply.",
  "Two instances of one model share the same training, so a second opinion adds nothing in principle.",
  "Review quality depends on the reviewer being the more capable model, not on separate context.",
  "Handing over the generator's reasoning reproduces its anchoring; independence requires the artefact alone."],
 "correct": 3,
 "whyRight": {"text": "Independence means a fresh request containing only the artefact to review plus review criteria — not the generation conversation. Without the generator's justifications in context, the reviewer evaluates the code on its own merits; with them, it re-reads and confirms them.", "cite": "CCA-Prep_Domain-4_v2.md §4.13"},
 "whyWrong": [
  {"option": 0, "text": "Criteria genuinely help, and should be supplied. But adding them while keeping the generator's reasoning leaves the anchoring that is producing the result.", "cite": "CCA-Prep_Domain-4_v2.md §4.13"},
  {"option": 1, "text": "Independent instances of the same model do catch each other's errors — that is the premise of the pattern. Shared training is not what defeats it here.", "cite": "CCA-Prep_Domain-1_v2.md §1.17"},
  {"option": 2, "text": "Capability is a separate axis. A stronger reviewer handed the generator's rationalisations is still reading a case already argued.", "cite": "CCA-Prep_Domain-4_v2.md §4.13"}]},

46: {
 "stem": "Extraction currently asks in the prompt for JSON matching a documented schema. Most outputs parse cleanly, but some arrive wrapped in a markdown fence and a few carry a preamble sentence before the object. An engineer proposes adding a JSON repair library. What removes the problem at its source?",
 "options": [
  "A stricter prompt instruction forbidding code fences and preamble text explicitly.",
  "Define a tool whose input schema is the desired structure, and read the values from the `tool_use` block.",
  "A post-processing step that strips fences and leading prose before the parse is attempted.",
  "A lower temperature, which reduces the model's tendency to add conversational framing."],
 "correct": 1,
 "whyRight": {"text": "Defining a tool whose input schema is your desired output structure and reading the `tool_use` block is the most reliable way to get schema-compliant output — it eliminates the whole syntax-error class, including prose preambles and markdown fences, which prompt-based JSON requests never guarantee against.", "cite": "CCA-Prep_Domain-4_v2.md §4.6"},
 "whyWrong": [
  {"option": 0, "text": "Asking nicely in the prompt is the mechanism already failing. Compliance stays probabilistic however the instruction is worded.", "cite": "CCA-Prep_Domain-4_v2.md §4.6"},
  {"option": 2, "text": "Stripping wrappers treats the symptom and must anticipate every variant. Tool use removes the problem rather than cleaning up after it.", "cite": "CCA-Prep_Domain-4_v2.md §4.6"},
  {"option": 3, "text": "Temperature controls randomness, not adherence to an output contract. A low-temperature model can wrap its JSON just as consistently.", "cite": "CCA-Prep_Domain-4_v2.md §4.4"}]},

47: {
 "stem": "Two requirements arrive together: every response in this reviewer session must stay in a formal, regulator-facing register, and this particular batch summary must come in under 200 words. An engineer puts both into the system prompt. What is wrong with that?",
 "options": [
  "Nothing — the system prompt is the right home for any instruction that shapes the output.",
  "Both belong in the user message, since the system prompt is only consumed on the first turn.",
  "Both belong in the system prompt, but the word limit must be expressed as a token count.",
  "The register is a persistent behavioural constraint and belongs there; the per-batch word limit is a one-off that belongs in the request."],
 "correct": 3,
 "whyRight": {"text": "The system prompt is the correct location for behavioural rules that apply for the entire conversation — tone, persona, standing format requirements. A limit that applies to one batch is not a standing rule, and putting it there means it silently governs every later batch as well.", "cite": "CCA-Prep_Domain-4_v2.md §4.3"},
 "whyWrong": [
  {"option": 0, "text": "Scope is the distinction. Session-wide constraints and single-request instructions have different homes precisely because one should persist and the other should not.", "cite": "CCA-Prep_Domain-4_v2.md §4.3"},
  {"option": 1, "text": "The system prompt is sent with every request and applies throughout. Moving a persistent register requirement into a user message loses authority as the conversation grows.", "cite": "CCA-Prep_Domain-4_v2.md §4.3"},
  {"option": 2, "text": "The unit is not the issue. A token-count version of the same one-off limit would still wrongly persist across every subsequent batch.", "cite": "CCA-Prep_Domain-4_v2.md §4.3"}]},

56: {
 "stem": "As review conversations pass fifty turns, both latency and per-turn cost climb steadily, although the model's replies are no longer than they were at turn five and the review interface has not changed. What explains the increase?",
 "options": [
  "The model produces progressively more internal reasoning as the conversation accumulates.",
  "Every request carries the complete conversation history, so each turn sends more tokens than the last.",
  "The service's conversation store slows down as the stored transcript grows.",
  "Longer sessions are routed to a larger model in order to maintain answer quality."],
 "correct": 1,
 "whyRight": {"text": "The API is stateless, so every request must include the entire conversation history in the `messages` array. More turns means more tokens per request, which is directly more cost and more latency — the corpus's named explanation for exactly this pattern.", "cite": "CCA-Prep_Domain-5_v2.md §5.1"},
 "whyWrong": [
  {"option": 0, "text": "The stem rules this out: replies are the same length at turn fifty as at turn five. Output volume is not what is growing.", "cite": "CCA-Prep_Domain-5_v2.md §5.1"},
  {"option": 2, "text": "Named as a wrong answer — database behaviour is not what makes a long conversation slower. The growth is in what each request carries.", "cite": "CCA-Prep_Domain-5_v2.md §5.1"},
  {"option": 3, "text": "Nothing routes by conversation length, and the interface is unchanged. This invents a mechanism to explain an effect statelessness already accounts for.", "cite": "CCA-Prep_Domain-5_v2.md §5.1"}]},

57: {
 "stem": "A synthesis step has stalled. Two of its five input categories are ambiguous, and it has queued a clarification request to the coordinator for each before producing anything at all. Throughput across the pipeline has dropped while it waits. What should it do?",
 "options": [
  "Continue waiting — synthesising on unverified assumptions is worse than delivering nothing.",
  "Escalate both ambiguities to a human reviewer and hold until a ruling comes back.",
  "Drop the two ambiguous categories and synthesise from the three that are unambiguous.",
  "Proceed on stated assumptions for the two, marking them explicitly so they can be corrected."],
 "correct": 3,
 "whyRight": {"text": "State assumptions explicitly and proceed, inviting correction. The corpus applies this to multi-agent systems as well as user-facing assistants: a synthesis agent should not block awaiting coordinator clarification on every gap.", "cite": "CCA-Prep_Domain-4_v2.md §4.19"},
 "whyWrong": [
  {"option": 0, "text": "Blocking produces nothing at all, which is strictly worse than a result whose assumptions are labelled and therefore checkable.", "cite": "CCA-Prep_Domain-4_v2.md §4.19"},
  {"option": 1, "text": "Escalation is for policy gaps and unresolvable ambiguity. Routine input ambiguity that a stated assumption covers does not warrant a human decision.", "cite": "CCA-Prep_Domain-5_v2.md §5.8"},
  {"option": 2, "text": "Silently dropping two of five categories produces a partial result presented as complete — the failure that coverage annotation exists to prevent.", "cite": "CCA-Prep_Domain-1_v2.md §1.10"}]},

60: {
 "stem": "Two noisy finding categories were switched off a month ago and their prompts have since been rewritten. Reviewer engagement with the four remaining categories has recovered to its former level. The team wants the two back. What should govern the decision?",
 "options": [
  "Re-enable both now — engagement has recovered and the prompts are materially different.",
  "Re-enable them permanently off by default, surfacing them only when a reviewer asks.",
  "Measure each rewritten category's false-positive rate against labelled examples before re-enabling it.",
  "Re-enable one at a time and watch overall engagement, treating any fall as the signal to stop."],
 "correct": 2,
 "whyRight": {"text": "The categories were disabled because their false-positive rate destroyed trust across the whole tool. Re-enabling is justified by evidence that the rate has actually fallen, measured per category against labelled examples — the same per-segment discipline that keeps an aggregate figure from hiding a bad segment.", "cite": "CCA-Prep_Domain-4_v2.md §4.17"},
 "whyWrong": [
  {"option": 0, "text": "A rewritten prompt is a hypothesis, not a result. Recovered engagement measures the four categories still running, not the two that were off.", "cite": "CCA-Prep_Domain-4_v2.md §4.17"},
  {"option": 1, "text": "A category nobody sees by default contributes nothing while still costing maintenance. If it is accurate it should run; if it is not, it should stay off.", "cite": "CCA-Prep_Domain-4_v2.md §4.17"},
  {"option": 3, "text": "Overall engagement is a lagging aggregate that moves only after trust has already been damaged again — the same masking problem, used as the detector.", "cite": "CCA-Prep_Domain-5_v2.md §5.9"}]},
}

# Closing-sentence and name-detector fixes on questions that are otherwise fine.
TWEAKS = {
 5:  ("Handoffs currently reach the human queue as an account number plus a one-line free-text note.",
      "Cases currently reach the human queue as an account number plus a one-line free-text note."),
 7:  ("The agent works through them strictly in turn and the call runs long. What should it do?",
      "The agent works through them strictly in turn and the call runs long. Which approach should it take?"),
 17: ("Maintainers can no longer find anything and every session pays for the whole file.",
      "Nobody can find anything any more, and every session pays for the whole file."),
 34: ("Which two statements are correct? Select two.",
      "Which two statements about the two primitives are correct? Select two."),
}

changed, tweaked = 0, 0
for i in range(1, 5):
    p = os.path.join(HERE, f"block{i}.json")
    b = json.load(open(p, encoding="utf-8"))
    for q in b["questions"]:
        if q["g"] in REPLACEMENTS:
            q.update(REPLACEMENTS[q["g"]])
            changed += 1
        if q["g"] in TWEAKS:
            old, new = TWEAKS[q["g"]]
            if old in q["stem"]:
                q["stem"] = q["stem"].replace(old, new)
                tweaked += 1
    json.dump(b, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print(f"questions rewritten: {changed} (expected {len(REPLACEMENTS)})")
print(f"stem tweaks applied: {tweaked} (expected {len(TWEAKS)})")
assert changed == len(REPLACEMENTS) and tweaked == len(TWEAKS), "patch did not apply cleanly"
