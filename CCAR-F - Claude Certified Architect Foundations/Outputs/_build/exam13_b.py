# -*- coding: utf-8 -*-
"""Exam 13 - blocks 3 and 4."""
S = "§"

BLOCK3 = dict(label="Code Generation with Claude Code", narrative=(
 "Your team uses Claude Code across a monorepo holding a TypeScript web client, a Python data service, and shared "
 "infrastructure definitions. Across this block the workspace is progressively configured - memory files, "
 "path-scoped conventions, commands and skills, planning behaviour - and then pushed into longer sessions where "
 "context management starts to matter."))

BLOCK4 = dict(label="Structured Data Extraction", narrative=(
 "You maintain a pipeline that extracts structured records from unstructured documents - supplier invoices, "
 "inspection reports, contract addenda - validates them against JSON schemas, and feeds downstream systems. "
 "Across this block the pipeline moves from getting the shape right, through validation and volume, to deciding "
 "what a human still needs to look at."))

Q = []
def q(g, block, label, domain, stem, options, correct, right, wrong):
    Q.append(dict(g=g, block=block, blockLabel=label, domain=domain, stem=stem, options=options,
                  correct=correct, whyRight=dict(text=right[0], cite=right[1]),
                  whyWrong=[dict(option=o, text=t, cite=c) for o, t, c in wrong]))

B, L = 2, BLOCK3["label"]

q(31, B, L, "D3",
 "The repository root `CLAUDE.md` says to use four-space indentation in Python. A `CLAUDE.md` inside `services/ingest/` says to follow the project formatter's defaults, which produce four spaces. A developer working in `services/ingest/` assumes only the nearer file is in effect and deletes the root file's Python section as redundant. Formatting conventions elsewhere in the repo immediately drift. What did the developer misunderstand?",
 ["Directory-level `CLAUDE.md` files take precedence over the root file, so the root file's Python section was already inert.",
  "Only the file nearest the working directory loads, so the root file was never contributing anything to that session.",
  "The root file loads only when no directory-level file exists anywhere in the path being worked on.",
  "The levels concatenate from the root down to the working directory - both files were loaded, and neither overrode the other."],
 3,
 ("CLAUDE.md levels concatenate in load order from root toward the working directory. Nothing overrides anything; removing the root section removed it for every directory that had no local equivalent.", "D3 " + S + "3.1"),
 [(0, "There is no precedence relationship between the levels. Treating the nearer file as a replacement for the further one is the specific misconception here.", "D3 " + S + "3.1"),
  (1, "All applicable levels load. Assuming a single winner is what led to deleting content that was doing real work.", "D3 " + S + "3.1"),
  (2, "Root content is not conditional on the absence of directory-level files. Both are loaded together.", "D3 " + S + "3.1")])

q(32, B, L, "D3",
 "The root `CLAUDE.md` has grown to cover testing standards, API conventions, deployment rules, security review criteria and dependency policy - most of which is irrelevant to any one package. Maintainers of each package know which standards apply to their code. What is the most appropriate way to reorganise it?",
 ["Keep a thin root file and use `@import` in each package's `CLAUDE.md` to pull in only the standards files that package's maintainers judge relevant.",
  "Move every standard into `.claude/skills/` so engineers load the ones they need by invoking a skill.",
  "Leave the file intact but add a table of contents at the top so the model can locate the relevant section.",
  "Duplicate the relevant sections into a `CLAUDE.md` inside each package directory and delete the root file."],
 0,
 ("`@import` is the mechanism for keeping CLAUDE.md modular: standards live in their own files and each package imports the ones that apply, using the maintainers' own domain knowledge.", "D3 " + S + "3.1; D3 " + S + "3.11"),
 [(1, "Skills are invoked on demand. Coding standards that must apply to every edit cannot depend on someone remembering to load them.", "D3 " + S + "3.3"),
  (2, "A table of contents leaves the whole file loaded in every session and still relies on the model selecting the right section by inference.", "D3 " + S + "3.11"),
  (3, "Duplication means five copies drifting apart, and deleting the root file removes the genuinely universal standards along with the rest.", "D3 " + S + "3.1")])

q(33, B, L, "D3",
 "Integration tests live beside the code they exercise - `client/checkout/checkout.integration.ts`, `services/ingest/parser.integration.py` - and are scattered through the tree. They share one convention set that applies nowhere else. The convention must take effect automatically whenever one is edited, without loading in unrelated sessions. Where should it live?",
 ["In the root `CLAUDE.md`, under a heading that names integration tests, so it is present in every session.",
  "In a `CLAUDE.md` inside each directory that currently contains an integration test.",
  "In a `.claude/rules/` file whose YAML frontmatter sets `paths: [\"**/*.integration.*\"]`.",
  "In a `.claude/skills/` skill that an engineer invokes when starting integration-test work."],
 2,
 ("Path-scoped rules with a glob attach conventions to files by pattern regardless of directory, and load only when a matching file is touched. That is exactly the requirement: automatic, scoped, and quiet elsewhere.", "D3 " + S + "3.2"),
 [(0, "A root-level section loads in every session, including the many that never touch an integration test, and relies on the model inferring when it applies.", "D3 " + S + "3.2"),
  (1, "Directory-bound files cannot follow a file type scattered across the tree, and every new test directory needs another copy.", "D3 " + S + "3.2"),
  (3, "A skill requires invocation. The requirement is automatic application based on the file being edited.", "D3 " + S + "3.3")])

q(34, B, L, "D3",
 "A `/scaffold-endpoint` skill generates boilerplate files. During a review of an incident where it deleted an unrelated module, you find its frontmatter contains `context: fork` and nothing else. An engineer says the fork setting should have prevented the deletion. What is the accurate assessment?",
 ["`context: fork` restricts a skill to read-only operations, so the deletion indicates the frontmatter was not being applied.",
  "`context: fork` isolates the skill's output from the main conversation; restricting what it may do requires `allowed-tools`.",
  "`context: fork` restricts tool access only when `allowed-tools` is also present, so the missing field disabled both protections.",
  "`context: fork` prevents writes outside the skill's own directory, so the deletion must have originated in the main session."],
 1,
 ("The two fields do different jobs. `context: fork` runs the skill in an isolated subagent context so its output does not pollute the main conversation. Restricting what a skill may touch is `allowed-tools`.", "D3 " + S + "3.3; Key Distinctions #13"),
 [(0, "Isolation of context is not restriction of capability. `context: fork` says nothing about which tools may run.", "D3 " + S + "3.3"),
  (2, "The fields are independent. `context: fork` does not become a tool restriction in the presence of another field.", "D3 " + S + "3.3"),
  (3, "There is no directory-scoping behaviour attached to `context: fork`. Write scope is governed by tool access.", "D3 " + S + "3.3")])

q(35, B, L, "D3",
 "The team's `/review` command lives in `.claude/commands/review.md` and has been in the repository for months. A new engineer proposes rewriting it as a skill in `.claude/skills/`, on the grounds that commands in `.claude/commands/` are legacy and no longer supported. How should you respond?",
 ["Project-scoped commands in `.claude/commands/` remain a supported mechanism, shared through version control; the choice between a command and a skill is about how the workflow should be invoked, not about obsolescence.",
  "Agree and migrate, since skills supersede commands and offer frontmatter options that commands cannot express.",
  "Agree in principle but keep both, so engineers who have memorised the command retain a working path.",
  "Disagree, because skills cannot be scoped to a project and migrating would make the workflow personal rather than shared."],
 0,
 ("Project-scoped slash commands in `.claude/commands/` are current and version-controlled. Skills and commands coexist; nothing has deprecated the commands directory.", "D3 " + S + "3.4"),
 [(1, "The premise is false. Commands are not superseded, so 'migrate because the old thing stopped working' rests on a fabricated obsolescence.", "D3 " + S + "3.4"),
  (2, "Keeping two copies of one workflow doubles maintenance to hedge against a problem that does not exist.", "D3 " + S + "3.4"),
  (3, "Skills can be project-scoped in `.claude/skills/` and shared through version control just as commands are.", "D3 " + S + "3.3")])

q(36, B, L, "D3",
 "Two tasks arrive. The first: split a shared utilities package into three packages, which changes import paths in roughly 60 files and requires deciding where several ambiguous helpers belong. The second: a null check is missing in one function, with a stack trace pointing at the exact line. How should each be approached?",
 ["Plan mode for both, since planning costs little and produces a record of intent for either size of change.",
  "Direct execution for both, since the package split's shape will become clear once the first few files are moved.",
  "Direct execution for the package split with detailed upfront instructions, and plan mode for the null check so the fix can be validated against the trace first.",
  "Plan mode for the package split, because it is large-scale with genuine design decisions; direct execution for the null check, because it is well-scoped with a known cause."],
 3,
 ("Plan mode is for large-scale change, multiple valid approaches and architectural decisions. Direct execution is for well-understood, well-scoped work. These two tasks sit at opposite ends.", "D3 " + S + "3.6"),
 [(0, "Planning a single-line fix with a known cause adds a step for a change that has no design space.", "D3 " + S + "3.6"),
  (1, "Discovering the boundaries by moving files is exactly the rework plan mode exists to prevent.", "D3 " + S + "3.6"),
  (2, "This inverts the criteria: comprehensive upfront instructions for the split presume the answer before exploring, and the null check needs no exploration at all.", "D3 " + S + "3.6")])

q(37, B, L, "D2",
 "Before deleting a deprecated helper named `normalizeCurrency`, an engineer asks the assistant to find every file that would break. The assistant runs `Glob(\"**/normalizeCurrency*\")`, gets two matches - the helper's own module and its test - and reports that removal is safe. A manual check finds fourteen files that call it. What should the assistant have used?",
 ["`Glob` with a broader pattern such as `**/*currency*` to catch files whose names relate to the helper.",
  "`Read` on each file under the utilities package to inspect what each one exports and imports.",
  "`Grep` for `normalizeCurrency` across the codebase, since the target is the symbol's appearance inside file contents.",
  "`Bash` with a recursive text search, since finding call sites is outside the built-in tools' scope."],
 2,
 ("Grep searches file contents; Glob matches file names and paths. Call sites are content, so Grep is the correct tool - Glob could only ever find files whose names contain the string.", "D2 " + S + "2.9; Key Distinctions #26"),
 [(0, "Broadening a name pattern still searches names. A file called `checkout.ts` that calls the helper matches no name pattern at all.", "D2 " + S + "2.9"),
  (1, "Reading every file in a package to find callers burns context on files that never mention the symbol, and misses callers outside that package.", "D2 " + S + "2.9"),
  (3, "Shelling out bypasses the tool built for content search. Grep is the sanctioned mechanism.", "D2 " + S + "2.9")])

q(38, B, L, "D3",
 "You need generated migration scripts to follow a specific transformation: legacy date strings in several formats normalised to ISO 8601, with nulls preserved rather than defaulted. Three rounds of increasingly detailed prose instructions have produced three different interpretations. What is the most effective next step?",
 ["Provide two or three concrete input/output examples showing exactly what each input format should become, including a null case.",
  "Restate the instruction more precisely, enumerating each legacy format and the rule that applies to it.",
  "Ask the model to explain its interpretation before generating, so misunderstandings can be corrected upfront.",
  "Write the transformation function by hand and ask the model to apply the same pattern to the remaining scripts."],
 0,
 ("Concrete input/output examples are the corpus's answer when prose descriptions are being interpreted inconsistently. Three rounds of prose have already established that more prose is not the lever.", "D3 " + S + "3.7"),
 [(1, "This is a fourth round of the approach that has failed three times. Enumeration is still prose.", "D3 " + S + "3.7"),
  (2, "Surfacing the interpretation is useful for design questions in unfamiliar domains. Here the requirement is known - it is the communication of it that is failing.", "D3 " + S + "3.7"),
  (3, "Hand-writing the function abandons the task rather than fixing the instruction, and leaves the same ambiguity for every later transformation.", "D3 " + S + "3.7")])

q(39, B, L, "D3",
 "You are about to add a caching layer to a service in a domain you do not know well. You can describe the outcome you want but suspect there are considerations you have not thought of - invalidation, failure behaviour under load, consistency guarantees. What technique surfaces those before implementation?",
 ["Write a test suite covering the behaviour you can specify, then iterate on failures until the design settles.",
  "Ask the model to interview you - to put questions to you about the design before it writes anything.",
  "Ask for three candidate implementations and compare them to infer which considerations matter.",
  "Enter plan mode and let the exploration of the codebase reveal the relevant constraints."],
 1,
 ("The interview pattern has the model put questions to you, surfacing considerations you had not anticipated. It is specifically the technique for entering an unfamiliar domain.", "D3 " + S + "3.7"),
 [(0, "Tests can only cover behaviour you already thought to specify. The gap here is in knowing what to specify.", "D3 " + S + "3.7"),
  (2, "Comparing three implementations makes you infer the considerations from code, which is slower and leaves silent omissions silent.", "D3 " + S + "3.7"),
  (3, "Plan mode explores the codebase. It does not surface domain considerations that are absent from the code you already have.", "D3 " + S + "3.6")])

q(40, B, L, "D3",
 "The repository ships a `/commit` skill at `.claude/skills/commit/SKILL.md` enforcing the team's message format. One engineer wants an extra step in their own runs - appending a ticket reference pulled from the branch name - without changing the team's behaviour. They create `~/.claude/skills/commit/SKILL.md`. What happens, and is it the right approach?",
 ["Both load and their instructions are concatenated, so the engineer's step is added on top of the team's format.",
  "The project skill wins for a project checkout, so the personal file has no effect and a differently named skill is required.",
  "The two conflict and the skill fails to load, so the engineer must rename theirs to avoid the collision.",
  "The personal skill overrides the project one for that engineer only - which is the sanctioned way to customise without forking the team's skill or learning a new command name."],
 3,
 ("A personal skill sharing a project skill's name overrides it for that user alone. This is the documented mechanism for individual customisation without changing the team's version.", "D3 " + S + "3.5; Key Distinctions #4"),
 [(0, "Skills do not concatenate the way memory files do. One definition is in effect.", "D3 " + S + "3.5"),
  (1, "Precedence runs the other way: the personal skill takes effect for its owner.", "D3 " + S + "3.5"),
  (2, "A shared name is not an error condition. Overriding by name is the intended behaviour.", "D3 " + S + "3.5")])

q(41, B, L, "D3",
 "A `CLAUDE.md` opens with four paragraphs on the product's history and market position, then a section on team culture, then the coding standards. Engineers report that standards buried near the end are applied inconsistently, and every session pays for the whole file. What is the most appropriate revision?",
 ["Move the standards to the top and leave the background material below, so the important content is read first.",
  "Split the file so that background sits in a README and the standards move to `.claude/rules/` with path globs.",
  "Cut the background and culture material and keep the file to the operative instructions the model needs to act on.",
  "Convert the whole file into a skill so its content loads only when an engineer decides it is relevant."],
 2,
 ("CLAUDE.md is for instructions that change what the model does. Narrative background and culture prose consume the budget of every session without affecting behaviour; removing them is the direct fix.", "D3 " + S + "3.11"),
 [(0, "Reordering keeps paying for the irrelevant material in every session and only partially mitigates the position problem.", "D3 " + S + "3.11"),
  (1, "Partly right, and it addresses one symptom - but standards that are genuinely universal belong in CLAUDE.md, and this leaves the background in the repository rather than out of the loaded context.", "D3 " + S + "3.11; D3 " + S + "3.2"),
  (3, "Universal standards must not depend on invocation. Making them a skill means they apply only when someone remembers.", "D3 " + S + "3.3")])

q(42, B, L, "D5",
 "A long refactoring session runs for several hours. Early on you correct the assistant: the legacy adapter must keep its synchronous interface because two external consumers depend on it. Around ninety minutes later it proposes an async signature for that adapter again. A sliding window keeps the most recent turns verbatim. What design fixes this?",
 ["Increase the sliding window so more of the early conversation stays verbatim.",
  "A hybrid context strategy: recent turns verbatim, a running summary of the middle, and a never-dropped structured facts block holding standing constraints like this one.",
  "Restate the constraint at the start of every request for the remainder of the session.",
  "Start a fresh session whenever the window fills, seeded with the current file state."],
 1,
 ("The hybrid approach is what the corpus prescribes for long sessions: recent turns verbatim, a running summary behind them, and a structured facts block that is never dropped - which is where a standing constraint belongs.", "D5 " + S + "5.13; D5 " + S + "5.3"),
 [(0, "A bigger fixed window delays the same loss. The constraint eventually falls off whatever the size.", "D5 " + S + "5.13"),
  (2, "Manual restatement puts the burden on the human every turn and fails the moment they forget.", "D5 " + S + "5.4"),
  (3, "A fresh session seeded with file state loses the constraint entirely - it lives in the conversation, not in the code.", "D5 " + S + "5.13")])

q(43, B, L, "D3",
 "Three weeks ago you ran a named session that mapped the payment module's dependencies in detail. Since then the module has been substantially rewritten: two files split, one deleted, several interfaces changed. You need to continue the analysis. What is the more reliable approach?",
 ["Start a fresh session and inject a structured summary of the earlier findings, since the prior tool results no longer describe the code that exists.",
  "Resume the named session with `--resume`, since it holds three weeks of accumulated understanding that would be expensive to rebuild.",
  "Resume the named session and instruct it to re-read every file in the module before continuing.",
  "Fork the earlier session so the original analysis is preserved while the new work proceeds on a branch."],
 0,
 ("When prior tool results are stale, a fresh session seeded with a structured summary is more reliable than resuming. Resumption carries the old observations forward as though they still described the code.", "D3 " + S + "3.12; D1 " + S + "1.16"),
 [(1, "The accumulated understanding is precisely what has gone stale. Resuming is right when prior context is mostly still valid, which is not the case after a substantial rewrite.", "D1 " + S + "1.16"),
  (2, "Full re-reading inside a resumed session pays the rebuild cost anyway while keeping the stale observations in context to conflict with what is re-read.", "D1 " + S + "1.16"),
  (3, "Forking branches from a baseline to explore divergent approaches. Here the baseline itself is out of date, so both branches inherit the problem.", "D1 " + S + "1.16")])

q(44, B, L, "D5",
 "Understanding an unfamiliar service requires tracing every caller of its event bus, enumerating its configuration surface, and mapping which modules touch persistence - all before any implementation begins. Previous attempts filled the context with file listings and search output, leaving little room for the actual work. What is the most effective approach?",
 ["Run `/compact` once the discovery phase completes, then begin implementation in the compacted session.",
  "Raise the session's context limit for the duration of the discovery phase.",
  "Delegate each discovery question to a subagent that returns a concise summary, keeping the main session for coordination and implementation.",
  "Perform the discovery in one session and the implementation in a separate session with no shared context."],
 2,
 ("Subagent delegation isolates verbose exploration and returns summaries, so the main session keeps the high-level thread and the context room to implement.", "D5 " + S + "5.6; D3 " + S + "3.6"),
 [(0, "Compacting mid-task discards precision the implementation phase still needs. Isolation prevents the problem; compaction reacts to it.", "D5 " + S + "5.6; Key Distinctions #22"),
  (1, "This treats a budget symptom rather than the pattern. Verbose discovery output is not worth keeping in full regardless of the budget available.", "D5 " + S + "5.6"),
  (3, "A clean separation throws away the findings along with the noise; the implementation session starts with nothing.", "D5 " + S + "5.6")])

q(45, B, L, "D3",
 "A nightly job runs `claude \"Summarise the day's dependency changes and flag risky upgrades\"` and pipes stdout into a parser that expects `{\"changes\": [...], \"risks\": [...]}`. The job hangs some nights and, when it does complete, the parser fails on prose wrapped around the JSON. What combination fixes both problems?",
 ["Add `-p` and instruct the model in the prompt to reply with JSON only and no surrounding prose.",
  "Add `--output-format json` alone, which both suppresses interactive input and constrains the output shape.",
  "Add `-p` and post-process the output with a regular expression that extracts the first JSON object it finds.",
  "Add `-p` for non-interactive execution, and `--output-format json` with `--json-schema` to enforce the expected structure."],
 3,
 ("Two separate defects need two flags: `-p` (or `--print`) runs non-interactively so the job cannot hang on input, and `--output-format json` with `--json-schema` enforces a machine-parseable structure rather than requesting one.", "D3 " + S + "3.8; D3 " + S + "3.9"),
 [(0, "`-p` fixes the hang, but asking for JSON in the prompt is a request, not an enforcement - the prose wrapper can return at any time.", "D3 " + S + "3.9"),
  (1, "`--output-format json` addresses the output shape only. Without `-p` the job still waits for interactive input.", "D3 " + S + "3.8"),
  (2, "Extracting with a regular expression is a downstream workaround for output the CLI can enforce directly.", "D3 " + S + "3.9")])

# ---------------------------------------------------------------- BLOCK 4
B, L = 3, BLOCK4["label"]

q(46, B, L, "D4",
 "The extraction step sometimes returns a conversational reply - 'This document appears to be a delivery note rather than an invoice, so I have not extracted invoice fields' - instead of calling any extraction tool. Downstream, this arrives as unparseable output. Three extraction schemas exist and the document type is not known in advance. What configuration guarantees a tool call?",
 ["`tool_choice: \"auto\"` with a prompt instruction that a tool must always be called.",
  "`tool_choice: {\"type\": \"tool\", \"name\": \"extract_invoice\"}`, forcing the invoice schema on every document.",
  "`tool_choice: \"any\"`, which requires a tool call while leaving the model free to choose which schema fits.",
  "A required field in each schema marking the document type, so a response without a tool call fails validation."],
 2,
 ("`\"any\"` guarantees that a tool is called while leaving the choice of tool to the model - exactly right when several schemas exist and the document type is unknown.", "D4 " + S + "4.6; D2 " + S + "2.1"),
 [(0, "`\"auto\"` permits a text response. That is the behaviour being observed, and a prompt instruction does not change what the setting allows.", "D4 " + S + "4.6"),
  (1, "Forcing one named tool guarantees a call but applies the invoice schema to delivery notes and everything else.", "D4 " + S + "4.6"),
  (3, "Schema validation applies to a tool call's arguments. It cannot fire when no tool was called at all.", "D4 " + S + "4.7")])

q(47, B, L, "D4",
 "Extraction now runs through `tool_use` with a strict JSON schema. Malformed-JSON errors have disappeared. QA still finds records where the line items sum to £4,180 while `invoice_total` reads £4,810, and occasional records where the supplier's VAT number sits in the `supplier_reference` field. An engineer concludes the schema is not being enforced. What is the accurate assessment?",
 ["The schema is not being enforced; a strict schema would reject a record whose line items do not sum to its total.",
  "The schema is working as designed. Strict schemas eliminate syntax errors; they do not detect semantic errors like a wrong sum or a value in the wrong field.",
  "The schema is too permissive; making every field required would surface both defects at validation time.",
  "The failures indicate the wrong tool was selected, since a correctly matched schema would place each value in its intended field."],
 1,
 ("A strict schema guarantees shape, not meaning. Arithmetic that does not reconcile and values placed in the wrong valid field are semantic errors and pass schema validation cleanly.", "D4 " + S + "4.7"),
 [(0, "JSON Schema has no concept of a cross-field arithmetic relationship. Both records are structurally valid.", "D4 " + S + "4.7"),
  (2, "Required fields ensure presence, not correctness. A required `invoice_total` accepts a wrong number as readily as a right one.", "D4 " + S + "4.5"),
  (3, "A misplaced value within the correct schema is a semantic error, not evidence that a different schema should have been chosen.", "D4 " + S + "4.7")])

q(48, B, L, "D4",
 "Inspection reports vary: some record a site engineer's name and licence number, many do not. The schema marks both as required strings. QA finds the pipeline is emitting plausible-looking names and licence numbers for reports that contain neither. What is the most effective fix?",
 ["Add a prompt instruction that fabricating values is prohibited and that unknown fields should be left blank.",
  "Add a validation step that cross-checks every extracted licence number against the licensing register.",
  "Add a few-shot example showing a report with no engineer details and an empty string in both fields.",
  "Make both fields optional and nullable, so the model can return null when the document does not contain them."],
 3,
 ("A required field creates pressure to produce a value. Making the field nullable removes the pressure and gives the model a correct way to say the information is absent - the corpus's named fabrication-prevention measure.", "D4 " + S + "4.5"),
 [(0, "A prohibition still leaves the schema demanding a string. The instruction and the structure pull in opposite directions, and the structure wins often enough to matter.", "D4 " + S + "4.5"),
  (1, "Register lookups catch some fabrications after the fact at significant cost, and do nothing about names.", "D4 " + S + "4.5"),
  (2, "An example helps, but the schema still requires a string; an empty string is also a poorer signal than an explicit null.", "D4 " + S + "4.5")])

q(49, B, L, "D4",
 "Two validation failures recur. In the first, `service_period_end` comes back as '31/03/26' where the schema wants ISO 8601. In the second, `parent_contract_id` is missing because the addendum references a master agreement that is not in the supplied document. Both currently trigger the same retry-with-error-feedback loop. What should change?",
 ["Retry the date-format failure with the validation error appended; stop retrying the missing contract ID and route it for enrichment or human review.",
  "Retry both but cap the missing-ID case at one attempt, since a second pass occasionally recovers it from context.",
  "Stop retrying both and route every validation failure to human review, since retries have not eliminated either.",
  "Retry both with the full document re-attached, since the smaller context of the retry may be why recovery fails."],
 0,
 ("Retries recover format and structural errors, where the information is present but expressed wrongly. They cannot recover information that is absent from the source - no amount of re-asking puts the master agreement into the document.", "D4 " + S + "4.9"),
 [(1, "A capped retry on absent information is still a retry on absent information. It cannot occasionally succeed, because the value is not there to find.", "D4 " + S + "4.9"),
  (2, "Abandoning retries discards the case where they reliably work. The date format is exactly what retry-with-feedback is for.", "D4 " + S + "4.9"),
  (3, "The document was already supplied. Re-attaching it does not add the referenced external agreement.", "D4 " + S + "4.9")])

q(50, B, L, "D4",
 "Invoices state a net amount, a VAT rate and sometimes a discount applied before tax. The pipeline must emit the gross total. Extraction is accurate on invoices where the gross is printed, and wrong on invoices where it must be derived - the discount is often applied after tax, or omitted. The schema and few-shot examples are already in place. What is the most effective addition?",
 ["More few-shot examples covering the discount-before-tax and no-discount cases.",
  "A post-extraction validation rule that recomputes the gross and rejects records that disagree.",
  "A step-by-step instruction in the prompt setting out the calculation order: apply the discount to the net, then apply VAT to the discounted net.",
  "A separate extraction pass dedicated to the discount field, run before the totals pass."],
 2,
 ("A multi-step numeric derivation calls for an explicit reasoning cue that sets out the order of operations. Few-shot examples demonstrate format and judgement; they do not reliably convey an arithmetic procedure.", "D4 " + S + "4.2"),
 [(0, "More examples of the same kind address consistency of shape. The failure here is in the sequence of the calculation, which examples convey only implicitly.", "D4 " + S + "4.2; D4 " + S + "4.1"),
  (1, "Recomputation detects the error without fixing it, and it needs the same correct calculation order that the prompt is currently missing.", "D4 " + S + "4.10"),
  (3, "Extracting the discount separately still leaves the model to combine the figures in the right order.", "D4 " + S + "4.2")])

q(51, B, L, "D4",
 "Contract addenda cite their parent agreement in three ways: an inline reference in the opening clause, an entry in a schedule at the end, or a footnote on the signature page. Extraction is reliable for the inline form and inconsistent for the other two. Which addition most improves this?",
 ["A longer field description in the schema explaining that the reference may appear anywhere in the document.",
  "A prompt instruction to read the entire document before extracting rather than stopping at the first match.",
  "A pre-processing step that locates the reference with a regular expression and injects it into the prompt.",
  "Two or three few-shot examples showing correct extraction from a schedule-style document and a footnote-style document."],
 3,
 ("Few-shot examples demonstrating varied document structures are the corpus's answer for inconsistent extraction across structural variety. They show the model what the same field looks like in each layout.", "D4 " + S + "4.1"),
 [(0, "A field description states that variety exists without showing what it looks like. That is the gap examples close.", "D4 " + S + "4.1"),
  (1, "Instructing thoroughness does not teach the model to recognise a footnote reference as the same entity as an inline one.", "D4 " + S + "4.1"),
  (2, "A regular expression brittle enough to catch three layouts becomes its own maintenance problem, and it bypasses the model rather than improving it.", "D4 " + S + "4.1")])

q(52, B, L, "D5",
 "Extraction accuracy is reported at 96.4% overall, and on that basis the team proposes auto-approving every record the model marks high-confidence. Reviewers object that they keep finding errors in exactly those records. What should be established before automating?",
 ["A higher confidence threshold, so only the most certain extractions bypass review.",
  "Accuracy broken down by document type and by field, plus stratified random sampling of high-confidence records to measure their true error rate.",
  "A second extraction pass whose output is compared with the first, with disagreements routed to review.",
  "A rule that any record with a null in a required-adjacent field is routed to review regardless of confidence."],
 1,
 ("An aggregate figure can hide a document type or a field performing badly. Segmenting accuracy and sampling the high-confidence tail is how you find out whether the confidence signal deserves the trust being placed in it.", "D5 " + S + "5.9"),
 [(0, "Raising an uncalibrated threshold shrinks the automated set without establishing that the signal means anything.", "D5 " + S + "5.9"),
  (2, "Two passes from the same model tend to agree in the same wrong ways, and agreement is not accuracy.", "D5 " + S + "5.9; D4 " + S + "4.13"),
  (3, "A null-based rule catches one error shape. It says nothing about the segments where the model is confidently wrong.", "D5 " + S + "5.9")])

q(53, B, L, "D4",
 "A nightly batch of 340 inspection reports is submitted through the Message Batches API. In the morning, 327 have succeeded and 13 have failed because those particular scans exceeded a per-request size limit. What is the most effective way to proceed?",
 ["Resubmit the whole batch tonight with every document chunked, so the size limit cannot be hit again.",
  "Move the 13 oversized documents to the synchronous API, since batch has proven unsuitable for them.",
  "Identify the 13 by their `custom_id` values, chunk those documents, and resubmit only them.",
  "Reduce tonight's batch size so that fewer documents compete for the per-request budget."],
 2,
 ("`custom_id` is the join key between requests and responses; it is how you identify precisely which documents failed. Resubmitting only those, with the fix applied, is the documented failure-handling pattern.", "D4 " + S + "4.11"),
 [(0, "Reprocessing 327 successful extractions to fix 13 failures multiplies cost and delay for no gain.", "D4 " + S + "4.11"),
  (1, "The synchronous API has the same per-request size limit. Chunking is the fix; the API choice is not the problem.", "D4 " + S + "4.11"),
  (3, "The limit is per request, not per batch. Batch size has no bearing on whether one oversized document fits.", "D4 " + S + "4.11")])

q(54, B, L, "D4",
 "Two extraction workloads exist. The first validates a supplier's invoice at the point of upload, while the supplier waits on screen for a confirmation or a correction prompt. The second reprocesses the previous quarter's archive for an audit due in three weeks. Finance asks whether both can move to the Message Batches API for the 50% saving. How should you respond?",
 ["Move the archive reprocessing to batch and keep the upload validation synchronous, since the supplier is waiting on the result.",
  "Move both, polling for completion and showing the supplier a pending state until the result returns.",
  "Move both, with a timeout that falls back to the synchronous API if the upload validation has not returned within a few minutes.",
  "Keep both synchronous, since splitting one pipeline across two APIs introduces divergence in how results are handled."],
 0,
 ("Batch processing offers the saving in exchange for a processing window of up to 24 hours with no latency guarantee. That is right for a three-week audit and wrong for anything a person is waiting on.", "D4 " + S + "4.11; D3 " + S + "3.10"),
 [(1, "'Usually faster than the worst case' is not a guarantee. A supplier cannot be left in a pending state that may last hours.", "D4 " + S + "4.11"),
  (2, "A fallback means paying for the synchronous call anyway on the blocking path, plus the complexity of running two routes.", "D4 " + S + "4.11"),
  (3, "Refusing the saving on the audit workload to keep one code path forfeits a real benefit; matching each workload to its latency tolerance is the documented approach.", "D4 " + S + "4.11")])

q(55, B, L, "D4",
 "Occasionally an invoice's printed total does not match the sum of its own line items - a supplier error, not an extraction error. Currently the pipeline extracts the printed total and the discrepancy surfaces weeks later in reconciliation. What extraction design surfaces it at the point of extraction?",
 ["Extract the line items only and compute the total downstream, so the printed figure cannot introduce an error.",
  "Reject any document whose printed total does not match the sum of its line items and route it back to the supplier.",
  "Add a prompt instruction to check the arithmetic and to report the correct total when the printed one is wrong.",
  "Extract `stated_total` and `calculated_total` as separate fields and flag records where they disagree."],
 3,
 ("Capturing the stated and the calculated value side by side turns a silent discrepancy into an explicit, checkable signal at extraction time. A `conflict_detected` flag on inconsistent source data serves the same purpose.", "D4 " + S + "4.10"),
 [(0, "Discarding the printed total loses the evidence that the supplier's own document was inconsistent - the very fact reconciliation needs.", "D4 " + S + "4.10"),
  (1, "Rejection is a business decision the extraction layer should not be making unilaterally, and it destroys the record instead of flagging it.", "D4 " + S + "4.10"),
  (2, "Having the model silently substitute its own figure hides the supplier's error rather than surfacing it.", "D4 " + S + "4.10")])

q(56, B, L, "D4",
 "The pipeline emits data-quality findings to the operations team. Dismissal rates by category: missing-VAT-number 7%, date-outside-contract-period 11%, unusual-unit-price 54%, non-standard-supplier-name 61%. The team has begun ignoring the queue wholesale, including the reliable categories. Improving the two weak categories' prompts will take a fortnight. What should you do now?",
 ["Add a confidence score to every finding and surface only those above a threshold while the prompts are improved.",
  "Disable the unusual-unit-price and non-standard-supplier-name categories immediately, then improve their prompts before re-enabling them.",
  "Keep all categories active but re-rank the queue so the reliable categories appear first.",
  "Merge the two weak categories into a single lower-priority category so they occupy less of the queue."],
 1,
 ("A category dismissed more than half the time is destroying trust in the accurate ones. Disabling it now stops the bleed; the prompt work then proceeds without the queue being abandoned in the meantime.", "D4 " + S + "4.17"),
 [(0, "A self-reported confidence score is a poorly calibrated filter, and adding it is itself work that delays the fix while the noise continues.", "D4 " + S + "4.17; D5 " + S + "5.9"),
  (2, "Re-ranking leaves the noise in the queue. The team is already ignoring the queue, so ordering within it changes nothing.", "D4 " + S + "4.17"),
  (3, "Merging two noisy categories produces one noisy category. The dismissal rate is unchanged.", "D4 " + S + "4.17")])

q(57, B, L, "D4",
 "A single prompt asks the model to extract every obligation from a 60-page master services agreement, classify each by risk, and draft a summary memo. Output quality is uneven: obligations from the later sections are frequently missed, and the risk classifications contradict the memo. What is the most effective restructuring?",
 ["Increase the output token allowance so the model has room to complete all three tasks fully.",
  "Ask the model to work more carefully and to double-check the later sections before writing the memo.",
  "Chain the work into sequential passes: extract obligations, then classify the extracted set, then draft the memo from the classified output.",
  "Split the agreement into six ten-page documents and run the same three-part prompt on each."],
 2,
 ("Prompt chaining decomposes one overloaded request into focused sequential passes, each with a single job and the previous pass's output as its input. That is what removes both the coverage loss and the internal contradiction.", "D4 " + S + "4.14"),
 [(0, "The limit is attention across three simultaneous tasks, not output length. More room to write does not improve what was never extracted.", "D4 " + S + "4.14"),
  (1, "Exhortation is not a mechanism. The structural overload remains.", "D4 " + S + "4.14"),
  (3, "Splitting the document alone leaves each run doing all three tasks at once, and it fragments obligations that span sections.", "D4 " + S + "4.14; D4 " + S + "4.12")])

q(58, B, L, "D5",
 "An operator reviews extractions through a chat interface, correcting the model over several turns. On a new deployment the model no longer recalls corrections made two turns earlier. An engineer proposes adding a `session_id` parameter to the API call so the service can maintain the thread. What is the accurate assessment?",
 ["The parameter is correct in principle but must be paired with a vector store for the history to be retrievable.",
  "The correct mechanism is a `conversation_id` returned by the first call and passed to subsequent calls.",
  "Session continuity requires the batch API, which maintains state across a submitted set of requests.",
  "No such parameter exists. The API is stateless - the application must include the prior messages in the `messages[]` array of each request, which is what the new deployment has stopped doing."],
 3,
 ("There is no server-side memory. A model 'remembers' only because the application resends the prior turns in `messages[]`; a deployment that stops doing so loses the thread, and no parameter restores it.", "D5 " + S + "5.1; Key Distinctions #25"),
 [(0, "A vector store serves retrieval over long histories. Ordinary multi-turn continuity is the message array, and the parameter does not exist to pair with anything.", "D5 " + S + "5.1; D5 " + S + "5.7"),
  (1, "Renaming the fabricated parameter does not make it real. No identifier of this kind is returned or accepted.", "D5 " + S + "5.1"),
  (2, "The batch API is for asynchronous volume and does not support multi-turn interaction within a request at all.", "D4 " + S + "4.11")])

q(59, B, L, "D4",
 "A colleague asks you to 'add validation for the new supplier documents.' It is unclear which document types are in scope, whether validation means schema conformance or business-rule checking, and what should happen to records that fail. What is the most effective response?",
 ["State your assumptions explicitly - the document types you will cover, that validation means schema plus the two business rules already in the pipeline, and that failures route to review - then proceed and invite correction.",
  "Ask the four clarifying questions needed to pin down scope before writing anything.",
  "Implement the narrowest reasonable interpretation, since a small change is easier to extend than to unpick.",
  "Choose sensible defaults and proceed without stating them, keeping the exchange short."],
 0,
 ("Proceeding on explicitly stated assumptions, with an invitation to correct them, keeps the work moving and gives the colleague something concrete to react to. Front-loading a list of questions drives abandonment.", "D4 " + S + "4.19"),
 [(1, "Four clarifying questions before any work is the documented abandonment pattern. One genuinely blocking question would be different from four.", "D4 " + S + "4.19"),
  (2, "A narrow implementation without stated assumptions leaves the colleague to discover the scope by inspecting the result.", "D4 " + S + "4.19"),
  (3, "Hidden defaults are the worst case: the work diverges from the intent and neither party knows why until later.", "D4 " + S + "4.19")])

q(60, B, L, "D5",
 "Every extraction turn calls `get_document_metadata`, which returns 60-plus fields: full ingestion history, storage location, checksums, prior processing attempts, permissions. Four fields are actually used. Over a long review session the context fills with metadata and the model's answers become vague. What is the most effective fix?",
 ["Call the tool once at the start of the session and instruct the model to reuse that result for subsequent turns.",
  "Trim the tool's response to the four relevant fields before it enters the conversation.",
  "Summarise the accumulated metadata periodically so the older entries occupy less space.",
  "Move the metadata into a scratchpad file the model can consult when it needs a field."],
 1,
 ("Verbose tool output consumes context out of all proportion to its relevance. Trimming to the relevant fields before the result lands in the conversation stops the accumulation at source.", "D5 " + S + "5.5"),
 [(0, "One call still injects 60-plus fields, and instructing reuse depends on the model remembering to. It reduces frequency rather than volume.", "D5 " + S + "5.5"),
  (2, "Summarising material that should never have entered context spends effort compressing noise, and risks compressing the four fields that matter.", "D5 " + S + "5.5"),
  (3, "A scratchpad persists findings across context boundaries; it is not the tool for filtering a response that is mostly irrelevant on arrival.", "D5 " + S + "5.12")])
