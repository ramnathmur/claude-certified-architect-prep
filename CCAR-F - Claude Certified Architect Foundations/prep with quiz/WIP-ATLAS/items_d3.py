# Domain 3 — Claude Code Configuration & Workflows · building: the office

ITEMS = [
{
 "id": "D3-01",
 "title": "CLAUDE.md hierarchy: user, project, directory",
 "concept": "The `CLAUDE.md` configuration hierarchy has three levels: user-level `~/.claude/CLAUDE.md`, project-level `.claude/CLAUDE.md` or root `CLAUDE.md`, and directory-level `CLAUDE.md` files in subdirectories.",
 "tested": "A scenario places an instruction at one level and asks who receives it or which files it governs, or asks where a new instruction should live. Distractors put a convention the whole team needs into user-level configuration, or name a configuration file that does not exist, such as `.claude/config.json`, as a home for instructions.",
 "remember": "Three levels, all loaded: `~/.claude/CLAUDE.md` for one person, `.claude/CLAUDE.md` or root `CLAUDE.md` for the whole repo, a subdirectory `CLAUDE.md` for one area. Choose by who needs it.",
 "analogy": "The office hands every starter the company handbook, pins floor notices where they apply, and lets each person keep sticky notes on their own monitor. Which of the three you write in depends on who has to receive the instruction.",
 "svg": """<rect class="tint" x="40" y="24" width="72" height="80"/>
<line x1="40" y1="52" x2="112" y2="52"/>
<line x1="40" y1="78" x2="112" y2="78"/>
<rect class="paper" x="88" y="30" width="16" height="16" rx="1" transform="rotate(6 96 38)"/>
<rect class="paper" x="88" y="56" width="14" height="18" rx="1"/><line class="thin" x1="91" y1="56" x2="91" y2="74"/>
<rect class="paper" x="88" y="82" width="16" height="18"/>
<text class="lbl" x="48" y="42">user</text>
<text class="lbl" x="48" y="68">proj</text>
<text class="lbl" x="48" y="94">dir</text>
<path class="acc" d="M124 28 h6 v72 h-6"/>
<line class="acc" x1="130" y1="64" x2="140" y2="64"/>""",
 "alt": "Office building with three floors labelled user, proj, dir, bracketed together",
},
{
 "id": "D3-02",
 "title": "User-level is personal — it never reaches teammates",
 "concept": "Instructions in `~/.claude/CLAUDE.md` apply only to that user and are not shared through version control, so a teammate who clones the repo never receives them.",
 "tested": "Three developers follow a convention and a newly joined fourth does not, all on the same repo; the question asks the root cause or the fix. The convention sits in the original developers' `~/.claude/CLAUDE.md`, and moving it to `.claude/CLAUDE.md` or root `CLAUDE.md` fixes it. Distractors look for the cause in the prompt or the model rather than in where the instruction is stored.",
 "remember": "Works for the old hands, not the new joiner → it is user-level. Shared conventions go in the project file, which is version-controlled. `~/.claude/CLAUDE.md` = personal preferences only.",
 "analogy": "A rule written on your own sticky note is invisible to the person hired last week; they were handed the company handbook and nothing else. If the whole floor should follow the rule, it goes in the handbook, which every new starter receives on day one.",
 "svg": """<rect class="acc" x="22" y="18" width="26" height="26" rx="2" transform="rotate(-6 35 31)"/>
<circle cx="44" cy="62" r="8"/><path d="M44 70 v22 M32 80 h24"/>
<circle cx="116" cy="62" r="8"/><path d="M116 70 v22 M104 80 h24"/>
<rect class="tint" x="128" y="76" width="16" height="22" rx="1"/><line class="thin" x1="132" y1="76" x2="132" y2="98"/>
<line class="dash thin" x1="52" y1="34" x2="104" y2="54"/>
<line class="no" x1="72" y1="38" x2="84" y2="50"/><line class="no" x1="84" y1="38" x2="72" y2="50"/>""",
 "alt": "Sticky note at one desk; dashed link to new teammate crossed out",
},
{
 "id": "D3-03",
 "title": "@import keeps CLAUDE.md modular",
 "concept": "A `CLAUDE.md` can reference other files with `@path` syntax, so each package's `CLAUDE.md` pulls in only the standards files that apply to it.",
 "tested": "A monorepo where every package should follow only the standards its maintainers know apply to it, and the question asks how to keep `CLAUDE.md` modular. Answer: `@import` the specific standards files in each package's `CLAUDE.md`. Distractors paste the same text into every file or load one large global standards file everywhere.",
 "remember": "The guide calls it the `@import` syntax for referencing external files from a `CLAUDE.md`. Per-package selection of standards files is the tell.",
 "analogy": "One team's handbook is a thin binder whose tabs point to other binders on the shared shelf: the coding standard, the test standard, and nothing else. The team next door has its own tabs to a different selection, and nobody carries the whole shelf to their desk.",
 "svg": """<rect class="tint" x="16" y="30" width="44" height="60" rx="4"/>
<circle class="thin" cx="26" cy="46" r="3"/><circle class="thin" cx="26" cy="74" r="3"/>
<text class="lbl" x="42" y="64" text-anchor="middle">@</text>
<rect class="accfill" x="60" y="40" width="8" height="10"/><rect class="accfill" x="60" y="66" width="8" height="10"/>
<line class="acc" x1="68" y1="45" x2="94" y2="40"/><line class="acc" x1="68" y1="71" x2="94" y2="76"/>
<rect class="tint" x="96" y="26" width="18" height="26" rx="2"/><line class="thin" x1="100" y1="26" x2="100" y2="52"/>
<rect class="tint" x="96" y="64" width="18" height="26" rx="2"/><line class="thin" x1="100" y1="64" x2="100" y2="90"/>
<rect class="dash" x="124" y="45" width="18" height="26" rx="2"/>""",
 "alt": "Binder with two tabs linking to two of three shelved books",
},
{
 "id": "D3-04",
 "title": ".claude/rules/ splits a monolith into topic files",
 "concept": "`.claude/rules/` holds topic-specific rule files such as `testing.md`, `api-conventions.md` and `deployment.md`, as an alternative to one long monolithic `CLAUDE.md`.",
 "tested": "A `CLAUDE.md` has grown to hundreds of lines and is hard to navigate; the question asks the supported way to reorganise it. Answer: split it into focused topic files in `.claude/rules/`. Distractors add more headings to the one file or point to a mechanism that does not exist.",
 "remember": "Long `CLAUDE.md` → one topic per file in `.claude/rules/`. Rules can also be path-scoped; `CLAUDE.md` is always loaded; skills are on demand.",
 "analogy": "When the handbook grows to a hundred pages, the office breaks it into short chapters on the shelf beside it: one for testing, one for API conventions, one for deployment. Each chapter is quick to find and update, and the handbook itself stays a few pages.",
 "svg": """<rect class="tint" x="16" y="24" width="36" height="80" rx="3"/><line x1="24" y1="24" x2="24" y2="104"/>
<path d="M58 64 h20 M72 58 l6 6 -6 6"/>
<line x1="84" y1="100" x2="148" y2="100"/>
<rect class="acc" x="88" y="52" width="14" height="48" rx="2"/>
<rect class="acc" x="108" y="52" width="14" height="48" rx="2"/>
<rect class="acc" x="128" y="52" width="14" height="48" rx="2"/>
<text class="lbl" x="95" y="44" text-anchor="middle">test</text>
<text class="lbl" x="115" y="44" text-anchor="middle">api</text>
<text class="lbl" x="135" y="44" text-anchor="middle">dep</text>""",
 "alt": "One thick book becoming three thin books labelled test, api, dep",
},
{
 "id": "D3-05",
 "title": "/memory shows what actually loaded",
 "concept": "The `/memory` command lists which memory files are loaded in the current session, which is how you diagnose behaviour that differs from one session or machine to another.",
 "tested": "Claude follows a convention in some sessions but not others, or on one machine but not another; the question asks the first diagnostic step. Answer: run `/memory` to see which files are actually loaded. Distractors repeat the instruction more forcefully each session, treating the symptom rather than the missing file.",
 "remember": "Inconsistent across sessions → `/memory` first, to see the loaded set. Then fix the file's location, not its wording.",
 "analogy": "Before arguing about why one desk follows a rule and the next does not, the office manager walks round and checks what is actually pinned at each desk. `/memory` is that walk-round: it lists which handbook, notices and sticky notes are in force in the session you are sitting in.",
 "svg": """<rect class="paper" x="40" y="18" width="80" height="84" rx="3"/>
<text class="lbl" x="80" y="32" text-anchor="middle">/mem</text>
<rect class="thin" x="50" y="40" width="10" height="10"/><path class="acc" d="M52 45 l3 3 l6 -7"/><line class="thin" x1="68" y1="45" x2="108" y2="45"/>
<rect class="thin" x="50" y="58" width="10" height="10"/><path class="acc" d="M52 63 l3 3 l6 -7"/><line class="thin" x1="68" y1="63" x2="108" y2="63"/>
<rect class="dash thin" x="50" y="76" width="10" height="10"/><line class="dash thin" x1="68" y1="81" x2="108" y2="81"/>""",
 "alt": "Checklist with two ticked entries and one dashed empty entry",
},
{
 "id": "D3-06",
 "title": "Project commands in .claude/commands/, personal in ~/.claude/commands/",
 "concept": "A command file in `.claude/commands/` is version-controlled and available to everyone who clones or pulls the repo; one in `~/.claude/commands/` is personal to that user.",
 "tested": "You want a `/review` command that runs the team checklist, available to every developer who clones or pulls the repo, and the question asks where the file goes. Answer: `.claude/commands/` in the repository. Distractors: `~/.claude/commands/` (personal, not shared), the project `CLAUDE.md` (instructions and context, not command definitions), and a `.claude/config.json` commands array, which does not exist.",
 "remember": "Everyone who clones → `.claude/commands/`. Only me → `~/.claude/commands/`. `CLAUDE.md` holds instructions, not commands; there is no `config.json` commands array.",
 "analogy": "A playbook filed on the office shelf is there for anyone who joins the floor. A playbook kept in your own desk drawer is yours alone, and the handbook is not where playbooks are filed.",
 "svg": """<line x1="16" y1="70" x2="80" y2="70"/>
<rect class="tint" x="20" y="34" width="14" height="36" rx="2"/>
<rect class="acc" x="38" y="30" width="14" height="40" rx="2"/>
<rect class="tint" x="56" y="38" width="14" height="32" rx="2"/>
<text class="lbl" x="48" y="88" text-anchor="middle">team</text>
<rect class="tint" x="100" y="46" width="44" height="24" rx="3"/><line x1="116" y1="58" x2="128" y2="58"/>
<text class="lbl" x="122" y="88" text-anchor="middle">mine</text>
<line x1="16" y1="102" x2="144" y2="102"/>""",
 "alt": "Shelf of playbooks labelled team beside a closed drawer labelled mine",
},
{
 "id": "D3-07",
 "title": "Skills live in .claude/skills/ as SKILL.md with frontmatter",
 "concept": "A skill is a `SKILL.md` file under `.claude/skills/`, and its YAML frontmatter can set `context: fork`, `allowed-tools` and `argument-hint`.",
 "tested": "A question asks where a skill's isolation, tool scope or argument prompting is configured; the answer is the frontmatter of that skill's `SKILL.md`. Distractors place the setting in `CLAUDE.md`, in `.mcp.json`, or in a config file that does not exist.",
 "remember": "`.claude/skills/` → `SKILL.md`. Frontmatter keys to know: `context: fork`, `allowed-tools`, `argument-hint`. Skill behaviour is configured in the skill file.",
 "analogy": "Each playbook on the shelf has a cover sheet stapled to the front saying how it is to be run: in the side room or at your desk, which cupboard keys it may take, and what the request form should ask for. You read the cover sheet before the playbook.",
 "svg": """<rect class="tint" x="40" y="22" width="60" height="80" rx="3"/><line x1="48" y1="22" x2="48" y2="102"/>
<rect class="paper" x="58" y="28" width="58" height="68" rx="2"/>
<line class="acc thin" x1="64" y1="34" x2="110" y2="34"/>
<text class="lbl" x="66" y="48">fork</text>
<text class="lbl" x="66" y="60">tools</text>
<text class="lbl" x="66" y="72">hint</text>
<line class="acc thin" x1="64" y1="78" x2="110" y2="78"/>
<line class="thin" x1="64" y1="86" x2="106" y2="86"/><line class="thin" x1="64" y1="92" x2="96" y2="92"/>""",
 "alt": "Playbook with a cover sheet listing fork, tools, hint",
},
{
 "id": "D3-08",
 "title": "context: fork runs the skill in an isolated sub-agent",
 "concept": "`context: fork` in `SKILL.md` frontmatter runs the skill in an isolated sub-agent context, which prevents its working from polluting the main conversation; the result still comes back.",
 "tested": "A `/analyze-codebase` skill floods the session and Claude loses track of the original task, or an `/explore-alternatives` skill's rejected options bleed into the implementation that follows; the question asks the fix. Answer: add `context: fork` to the skill's frontmatter. Distractors switch to a different model, compress the result to a short summary, or split the skill in two, none of which keeps the output out of the main context.",
 "remember": "Verbose or exploratory skill → `context: fork`. Discovery, analysis and brainstorming run isolated; implementation and conversation stay in the main session.",
 "analogy": "Messy work goes to the side room: the whole-building survey and the brainstorm with its discarded ideas happen in there, and only the conclusion is carried back to the main desk. The desk stays clear for the job that was already in progress.",
 "svg": """<rect class="tint" x="16" y="30" width="64" height="70" rx="3"/>
<rect class="paper" x="28" y="60" width="40" height="14"/>
<rect class="acc" x="96" y="30" width="48" height="70" rx="3"/>
<text class="lbl" x="120" y="24" text-anchor="middle">fork</text>
<path class="thin" d="M104 44 l8 8 l-8 8 l8 8 l-8 8 M118 40 l6 10 l6 -10 l6 10 M106 86 h30 M122 60 l10 10 M132 60 l-10 10"/>
<rect class="paper" x="82" y="60" width="12" height="12" rx="1"/>
<path class="acc" d="M96 66 h-14 M86 61 l-5 5 5 5"/>""",
 "alt": "Main office beside a side room full of scribbles; one note returns",
},
{
 "id": "D3-09",
 "title": "allowed-tools restricts what a skill may do",
 "concept": "`allowed-tools` in `SKILL.md` frontmatter restricts which tools the skill may use while it runs, for example limiting it to file write operations so it cannot take destructive actions.",
 "tested": "A skill should write files but must not be able to run destructive operations, and the question asks how to enforce that. Answer: `allowed-tools` in the skill's frontmatter. Distractors put the restriction in `CLAUDE.md` prose, in `.mcp.json`, or in a config file that does not exist.",
 "remember": "Scope what a skill may do → `allowed-tools` in `SKILL.md` frontmatter. Prose in `CLAUDE.md` is guidance; the frontmatter key is the restriction.",
 "analogy": "The cover sheet of a playbook lists which cupboard keys the person running it is handed. A playbook that only needs to file documents gets the cabinet key and not the key to the shredder, so a slip in the playbook cannot destroy anything.",
 "svg": """<circle class="acc" cx="34" cy="44" r="10"/><path class="acc" d="M44 44 h30 M64 44 v8 M70 44 v8"/>
<rect class="tint" x="88" y="26" width="48" height="40" rx="2"/><line x1="88" y1="46" x2="136" y2="46"/>
<line x1="108" y1="36" x2="116" y2="36"/><line x1="108" y1="56" x2="116" y2="56"/>
<text class="lbl" x="112" y="82" text-anchor="middle">Write</text>
<rect class="tint" x="24" y="76" width="44" height="26" rx="2"/>
<path class="thin" d="M32 76 v-8 h28 v8 M36 90 v8 M46 90 v8 M56 90 v8"/>
<line class="no" x1="36" y1="80" x2="56" y2="98"/><line class="no" x1="56" y1="80" x2="36" y2="98"/>""",
 "alt": "Key beside a filing cabinet labelled Write; shredder crossed out",
},
{
 "id": "D3-10",
 "title": "argument-hint prompts for missing parameters",
 "concept": "`argument-hint` in `SKILL.md` frontmatter tells a developer what parameter to supply when they invoke the skill without arguments.",
 "tested": "Developers keep invoking a skill such as `/migration` with no arguments and get unhelpful results; the question asks which frontmatter field prompts them for the required parameter. Answer: `argument-hint`. Distractors are the other frontmatter keys, `allowed-tools` and `context: fork`, or a check written into `CLAUDE.md`.",
 "remember": "Missing parameter at invocation → `argument-hint`. It prompts for input; it does not restrict tools or isolate context.",
 "analogy": "The request form for a playbook has a printed line saying what must be filled in: the migration name, the ticket number. Someone who hands over a blank form is shown that line instead of receiving a guessed-at result.",
 "svg": """<rect class="paper" x="40" y="18" width="80" height="84" rx="3"/>
<line class="thin" x1="52" y1="34" x2="108" y2="34"/>
<line class="thin" x1="52" y1="46" x2="108" y2="46"/>
<rect class="acc dash" x="52" y="58" width="56" height="16" rx="2"/>
<text class="lbl" x="80" y="70" text-anchor="middle">name</text>
<line class="thin" x1="52" y1="86" x2="108" y2="86"/>
<rect class="thin" x="52" y="92" width="8" height="6"/>""",
 "alt": "Request form with one highlighted blank field labelled name",
},
{
 "id": "D3-11",
 "title": "Personal skill variants without touching the team's",
 "concept": "To customise a team skill for yourself, create a personal variant in `~/.claude/skills/` under a different name, so teammates' copy is untouched.",
 "tested": "A developer wants their own version of the team's `/commit` skill without changing what teammates get. Answer, in the official guide's wording: a personal variant in `~/.claude/skills/` with a different name. Distractors edit the shared `.claude/skills/commit/SKILL.md`, which changes it for everyone, or add personal preferences to the project `CLAUDE.md`.",
 "remember": "Personal variant = `~/.claude/skills/`, different name, teammates unaffected. Editing `.claude/skills/` edits it for everyone.",
 "analogy": "You want your own way of running the sign-off playbook, so you write a copy for your desk drawer and give it your own title. The shelf copy stays as the team wrote it, and nobody else notices your version exists.",
 "svg": """<line x1="16" y1="64" x2="76" y2="64"/>
<rect class="tint" x="24" y="28" width="16" height="36" rx="2"/>
<rect class="tint" x="46" y="32" width="16" height="32" rx="2"/>
<text class="lbl" x="46" y="82" text-anchor="middle">team</text>
<path class="dash thin" d="M64 36 q22 -22 44 -12"/>
<rect class="acc" x="108" y="18" width="16" height="30" rx="2"/>
<rect class="tint" x="92" y="40" width="52" height="24" rx="3"/><line x1="112" y1="52" x2="124" y2="52"/>
<text class="lbl" x="118" y="82" text-anchor="middle">mine</text>""",
 "alt": "Shelved playbook labelled team; personal copy in a drawer labelled mine",
},
{
 "id": "D3-12",
 "title": "Skills are on-demand; CLAUDE.md is always loaded",
 "concept": "`CLAUDE.md` is loaded in every session and holds universal standards; a skill is invoked on demand for a task-specific workflow.",
 "tested": "A `CLAUDE.md` mixes coding standards with PR-review, deployment and migration procedures, and the question asks how to reorganise. Answer: keep universal standards in `CLAUDE.md` and move each workflow into a skill. Distractors move everything into skills, so standards would need invoking every time, or leave the whole file loading in every session.",
 "remember": "Applies every time → `CLAUDE.md`. Runs when someone asks for it → skill. `.claude/rules/` sits between: loaded when a matching path is edited.",
 "analogy": "The handbook is what everyone reads on day one and carries all day; the playbooks stay on the shelf until a specific job comes up. Filing the deployment procedure in the handbook makes everyone carry it to every meeting.",
 "svg": """<line x1="72" y1="44" x2="144" y2="44"/>
<rect class="tint" x="78" y="16" width="12" height="28" rx="2"/>
<rect class="tint" x="94" y="20" width="12" height="24" rx="2"/>
<rect class="tint" x="110" y="14" width="12" height="30" rx="2"/>
<rect class="tint" x="126" y="18" width="12" height="26" rx="2"/>
<line x1="16" y1="100" x2="144" y2="100"/>
<path class="acc" d="M20 96 v-40 h34 v40 z M54 96 v-40 h34 v40 z"/>
<path class="acc thin" d="M26 66 h22 M26 74 h22 M26 82 h14 M60 66 h22 M60 74 h22 M60 82 h14"/>""",
 "alt": "Open handbook on the desk; playbooks waiting on a shelf above",
},
{
 "id": "D3-13",
 "title": "Path-scoped rules: paths: globs in YAML frontmatter",
 "concept": "A `.claude/rules/` file whose YAML frontmatter has a `paths:` field of glob patterns, such as `paths: [\"terraform/**/*\"]`, loads only while editing matching files, keeping irrelevant context and tokens out of the session.",
 "tested": "Conventions for one technology, such as Terraform, should apply only when working on those files, and the question asks how to load them conditionally. Answer: a `.claude/rules/` file with `paths:` globs in its frontmatter. Distractors put the conventions in root `CLAUDE.md`, which loads every session, or expect Claude to infer which section applies.",
 "remember": "`paths:` plus glob in a rules file's YAML frontmatter = loads on match only. A type glob such as `**/*.test.tsx` matches regardless of directory.",
 "analogy": "The shop-floor rules hang inside the shop-floor door, not in the handbook: you read them when you walk onto that floor and not before. Anyone working in accounts never sees them and is not slowed down by them.",
 "svg": """<rect class="tint" x="88" y="20" width="44" height="86" rx="2"/>
<circle class="thin" cx="124" cy="66" r="2"/>
<rect class="paper" x="94" y="30" width="32" height="22" rx="1"/>
<rect class="acc" x="94" y="30" width="32" height="22" rx="1"/>
<text class="lbl" x="110" y="45" text-anchor="middle">**/*</text>
<rect class="tint" x="16" y="62" width="52" height="16" rx="2"/>
<rect class="dash thin" x="28" y="30" width="28" height="22"/>""",
 "alt": "Door with a rule notice on it; empty dashed notice elsewhere",
},
{
 "id": "D3-14",
 "title": "Glob rules beat per-directory CLAUDE.md for scattered files",
 "concept": "For conventions that must apply to files spread across many directories, such as `Button.test.tsx` beside `Button.tsx` everywhere, one glob rule (`**/*.test.tsx`) beats a `CLAUDE.md` in every subdirectory.",
 "tested": "Test files sit beside the code they test across the whole tree, each area has its own conventions, and the question asks the most maintainable way to apply the right conventions automatically. Answer: `.claude/rules/` with glob patterns. Distractors: consolidating under headings in root `CLAUDE.md` (relies on inference), a skill per code type (needs invoking), a `CLAUDE.md` in every subdirectory (bound to its folder, so it cannot follow scattered files).",
 "remember": "Spread across directories → one glob rule. A directory-level `CLAUDE.md` is bound to its folder. \"Automatically\" plus \"regardless of location\" is the tell.",
 "analogy": "Test benches are dotted around every floor of the building, so one rule is posted for anyone who sits at a test bench, wherever it is. Pinning a copy in every corridor means keeping a dozen copies in step.",
 "svg": """<rect class="tint" x="56" y="20" width="88" height="88"/>
<line x1="56" y1="49" x2="144" y2="49"/><line x1="56" y1="78" x2="144" y2="78"/>
<circle class="accfill" cx="70" cy="36" r="4"/><circle class="accfill" cx="120" cy="36" r="4"/>
<circle class="accfill" cx="96" cy="64" r="4"/><circle class="accfill" cx="130" cy="64" r="4"/>
<circle class="accfill" cx="76" cy="94" r="4"/><circle class="accfill" cx="112" cy="94" r="4"/>
<rect class="paper" x="12" y="44" width="34" height="36" rx="2"/>
<text class="lbl" x="29" y="66" text-anchor="middle">**/*</text>
<line class="acc" x1="46" y1="62" x2="56" y2="62"/>""",
 "alt": "Building with test benches on every floor; one rule sheet covers all",
},
{
 "id": "D3-15",
 "title": "Plan mode for architecture; direct execution for scoped fixes",
 "concept": "Plan mode suits large-scale, multi-file or architectural work with several valid approaches, exploring and designing before committing to changes; direct execution suits simple, well-scoped changes such as one validation check in one function.",
 "tested": "The scenario states its scope up front — restructuring a monolith into microservices, a library migration touching 45+ files, choosing between integration approaches with different infrastructure needs — or a single-file bug with a clear stack trace, and asks which approach to take. Distractors start in direct execution and switch to plan mode only if complexity appears, or hand over exhaustive upfront instructions without exploring. A migration is planned first, then executed directly.",
 "remember": "Dozens of files, design decisions, several valid approaches → plan first. One file, clear trace → go direct. Complexity stated in the task is a reason to plan now, not to switch later.",
 "analogy": "Knocking through the wall between two departments starts with the architect's drawing: where the load sits, what runs inside the wall, which of three layouts to build. Fixing a squeaky hinge on one door goes straight to the handyman, and nobody draws it first.",
 "svg": """<rect class="tint" x="16" y="24" width="76" height="60" rx="3"/>
<path class="acc dash" d="M28 36 h24 v20 h-24 z M60 36 h20 v36 h-20"/>
<text class="lbl" x="40" y="76">45+</text>
<rect class="paper" x="112" y="34" width="28" height="60" rx="2"/>
<circle class="thin" cx="134" cy="66" r="2"/>
<rect class="thin" x="110" y="42" width="4" height="8"/><rect class="thin" x="110" y="78" width="4" height="8"/>
<line x1="16" y1="100" x2="144" y2="100"/>""",
 "alt": "Architect's blueprint marked 45+ beside a single door with hinges",
},
{
 "id": "D3-16",
 "title": "Explore subagent keeps discovery noise out of main context",
 "concept": "The Explore subagent runs verbose discovery in its own context and returns a summary, so the main conversation keeps room for the phases that follow.",
 "tested": "A multi-phase task's discovery phase would fill the context window before implementation starts, and the question asks how to preserve the main context. Answer: run discovery in the Explore subagent and take back the summary, which keeps the verbose output out of the main window in the first place. The paired option is `/compact`, which the guide lists for reducing usage once a session has already filled.",
 "remember": "Verbose discovery → Explore subagent, summary comes back. `/compact` is a guide-listed technique for a session that has already filled, not a wrong answer in itself.",
 "analogy": "The survey of every floor is done by a runner who comes back with a one-page note, rather than by dragging every drawer's contents onto your desk. Tidying the desk afterwards is a real option; sending the runner is what keeps it clear.",
 "svg": """<rect class="tint" x="16" y="70" width="52" height="30" rx="3"/>
<circle cx="42" cy="50" r="7"/><path d="M42 57 v13"/>
<rect class="tint" x="100" y="90" width="40" height="8"/>
<rect class="tint" x="104" y="80" width="34" height="8"/>
<rect class="tint" x="98" y="70" width="38" height="8"/>
<rect class="tint" x="102" y="60" width="30" height="8"/>
<rect class="tint" x="106" y="50" width="26" height="8"/>
<rect class="tint" x="100" y="40" width="34" height="8"/>
<rect class="acc" x="70" y="52" width="14" height="16" rx="1"/>
<path class="acc" d="M96 60 h-8 M92 56 l-4 4 4 4"/>""",
 "alt": "Desk kept clear; a heap of papers elsewhere sends back one small note",
},
{
 "id": "D3-17",
 "title": "Two or three concrete input/output examples beat more prose",
 "concept": "When a prose description of a transformation is interpreted inconsistently, two or three concrete input/output examples communicate the expected result more effectively than more prose.",
 "tested": "A transformation described in natural language produces differently shaped output on each run, and the question asks the most effective clarification. Answer: add 2–3 concrete input→output pairs. Distractors lengthen the description or restate the requirement more emphatically.",
 "remember": "Inconsistent results from a description → show 2–3 input/output pairs. The examples show the pattern; the model applies it to new inputs.",
 "analogy": "Describing the filing format in a memo produces a different layout from every clerk; laying two finished folders on the desk and saying 'like these' gets the same layout from all of them. The clerks then apply that layout to folders they have never seen.",
 "svg": """<rect class="paper" x="20" y="22" width="30" height="30" rx="2"/><path class="thin" d="M26 32 h18 M26 40 h18"/>
<path class="acc" d="M56 37 h24 M74 32 l6 5 -6 5"/>
<rect class="acc" x="86" y="22" width="30" height="30" rx="2"/><path class="acc thin" d="M92 32 h18 M92 42 h10"/>
<rect class="paper" x="20" y="64" width="30" height="30" rx="2"/><path class="thin" d="M26 74 h18 M26 82 h18"/>
<path class="acc" d="M56 79 h24 M74 74 l6 5 -6 5"/>
<rect class="acc" x="86" y="64" width="30" height="30" rx="2"/><path class="acc thin" d="M92 74 h18 M92 84 h10"/>
<text class="lbl" x="35" y="110" text-anchor="middle">in</text>
<text class="lbl" x="101" y="110" text-anchor="middle">out</text>""",
 "alt": "Two input pages each transformed into a matching output page",
},
{
 "id": "D3-18",
 "title": "Test-driven iteration: write the tests, share the failures",
 "concept": "Write the test suite first (expected behaviour, edge cases, performance requirements), then iterate by sharing test failures; a specific test with example input and expected output is how you fix an edge case.",
 "tested": "A migration script mishandles null values and the developer keeps describing the bug in prose and getting partial fixes; or a question asks how to structure a build so each round of refinement is targeted. Answer: tests first, failures fed back; for the edge case, a concrete failing test with input and expected output. Distractors re-describe the bug more emphatically or write tests only after generation, as verification.",
 "remember": "Suite first, failures back, repeat. Edge case → a specific test case, not a stronger adjective. Tests written afterwards are verification, not test-driven iteration.",
 "analogy": "The office writes the acceptance checklist before the contractor starts — the everyday cases, the awkward ones, how fast the door must close — and on each visit hands over the items still failing. When one drawer sticks on an empty folder, the note names that drawer and what it should do.",
 "svg": """<rect class="paper" x="24" y="18" width="70" height="84" rx="3"/>
<rect class="thin" x="32" y="32" width="10" height="10"/><path class="thin" d="M34 37 l3 3 6 -7"/><line class="thin" x1="50" y1="37" x2="84" y2="37"/>
<rect class="thin" x="32" y="52" width="10" height="10"/><path class="acc" d="M34 54 l6 6 M40 54 l-6 6"/><line class="acc" x1="50" y1="57" x2="84" y2="57"/>
<rect class="thin" x="32" y="72" width="10" height="10"/><path class="thin" d="M34 77 l3 3 6 -7"/><line class="thin" x1="50" y1="77" x2="84" y2="77"/>
<path class="acc" d="M96 57 h12 M104 52 l5 5 -5 5"/>
<rect class="tint" x="110" y="40" width="34" height="40" rx="3"/>
<path class="thin" d="M118 52 h18 M118 60 h12 M118 68 h16"/>""",
 "alt": "Checklist with one failing item sent back to the code",
},
{
 "id": "D3-19",
 "title": "The interview pattern: Claude asks first",
 "concept": "The interview pattern has Claude ask questions before implementing, surfacing considerations such as cache invalidation strategies and failure modes that the developer had not anticipated.",
 "tested": "A developer in an unfamiliar domain gets three generated versions of a caching layer, each missing a different requirement, and the question asks the better approach. Answer: have Claude interview the developer first. Distractors keep correcting one missed requirement per iteration or write a longer brief from the developer's own incomplete picture.",
 "remember": "Unfamiliar domain, unknown unknowns → ask Claude to ask you first. One interview turn replaces several correction cycles.",
 "analogy": "Before the fit-out crew touches the new floor, the architect sits you down and asks about power load, who needs to reach what, and what happens when the lift is out — the questions you would not have known to raise. It is a short meeting compared with rebuilding the floor three times.",
 "svg": """<circle cx="40" cy="58" r="9"/><path d="M40 67 v26 M26 78 h28"/>
<circle cx="120" cy="58" r="9"/><path d="M120 67 v26 M106 78 h28"/>
<path class="acc" d="M50 20 h40 v22 h-30 l-6 8 v-8 h-4 z"/>
<text class="lbl" x="70" y="36" text-anchor="middle">?</text>
<rect class="paper" x="132" y="18" width="14" height="18" rx="1"/>
<path class="thin" d="M135 24 h8 M135 29 h8"/>""",
 "alt": "Two figures; the architect's speech bubble holds a question mark",
},
{
 "id": "D3-20",
 "title": "Interacting issues in one message; independent ones sequentially",
 "concept": "Issues whose fixes interact go to Claude in one detailed message so it can design a single coherent change; independent issues can be fixed one at a time.",
 "tested": "A review turns up several problems in one function — a locking bug, a retry bug that depends on the locking behaviour, and an unrelated typo — and the question asks how to feed them back. Answer: the interacting pair together in one message; the independent item can go separately. The distractor is one issue per message regardless, which lets sequential fixes to interacting problems conflict.",
 "remember": "Fixes affect each other → one message. Fixes are unrelated → sequential is fine. Ask whether fix A changes what fix B should be.",
 "analogy": "If the new door swing and the new desk position depend on each other, both go on one work order so the handyman plans them together. The flickering light in the corridor is a separate ticket and can wait its turn.",
 "svg": """<rect class="paper" x="16" y="18" width="80" height="84" rx="3"/>
<rect class="acc" x="28" y="30" width="20" height="16" rx="2"/>
<text class="lbl" x="38" y="42" text-anchor="middle">A</text>
<rect class="acc" x="60" y="60" width="20" height="16" rx="2"/>
<text class="lbl" x="70" y="72" text-anchor="middle">B</text>
<polyline class="acc" points="48,38 54,38 54,68 60,68"/>
<line class="thin" x1="28" y1="88" x2="84" y2="88"/>
<rect class="paper" x="108" y="30" width="36" height="40" rx="3"/>
<rect class="thin" x="118" y="42" width="16" height="14" rx="2"/>
<text class="lbl" x="126" y="53" text-anchor="middle">C</text>""",
 "alt": "One work order linking items A and B; item C on its own ticket",
},
{
 "id": "D3-21",
 "title": "-p / --print runs Claude Code non-interactively",
 "concept": "The `-p` (or `--print`) flag runs Claude Code non-interactively: it processes the prompt, prints the result to stdout and exits, so a CI job does not hang waiting for input.",
 "tested": "A pipeline runs `claude \"Analyze this pull request for security issues\"` and hangs, with logs showing Claude Code waiting for interactive input; the question asks the correct fix. Answer: `claude -p \"...\"`. Distractors are `CLAUDE_HEADLESS=true` and `--batch`, neither of which exists, and `< /dev/null`, a Unix workaround rather than the documented approach.",
 "remember": "CI hangs waiting for input → add `-p`. `--batch` and `CLAUDE_HEADLESS` do not exist; `< /dev/null` is a workaround, not the answer.",
 "analogy": "The overnight audit robot is switched on with one instruction and left alone; `-p` is the setting that makes it do the job, print its report and power down instead of standing at the desk waiting for a reply. Without it, the robot waits all night for an answer that never comes.",
 "svg": """<rect class="tint" x="60" y="26" width="40" height="30" rx="4"/>
<circle class="thin" cx="72" cy="40" r="3"/><circle class="thin" cx="88" cy="40" r="3"/>
<line x1="80" y1="26" x2="80" y2="16"/><circle class="accfill" cx="80" cy="14" r="3"/>
<rect class="tint" x="54" y="60" width="52" height="34" rx="4"/>
<rect class="acc" x="66" y="70" width="28" height="16" rx="3"/>
<text class="lbl" x="80" y="82" text-anchor="middle">-p</text>
<path class="paper" d="M112 66 h30 v28 h-30 z"/>
<line class="thin" x1="118" y1="74" x2="136" y2="74"/><line class="thin" x1="118" y1="82" x2="136" y2="82"/>
<rect class="paper" x="10" y="30" width="40" height="24" rx="2"/>
<text class="lbl" x="30" y="46" text-anchor="middle">batch</text>
<line class="no" x1="16" y1="34" x2="44" y2="50"/><line class="no" x1="44" y1="34" x2="16" y2="50"/>""",
 "alt": "Audit robot tagged -p printing a report; a batch note crossed out",
},
{
 "id": "D3-22",
 "title": "--output-format json with --json-schema for machine-readable findings",
 "concept": "`--output-format json` with `--json-schema` makes CI-invoked Claude Code emit structured, schema-conforming findings that a script can parse and post as inline PR comments.",
 "tested": "A team wants each review finding auto-posted as an inline PR comment with file, line, severity and suggested fix, and the question asks how to get reliably parseable output. Answer: `--output-format json` with `--json-schema`. Distractors add an output-format section to `CLAUDE.md` or a format instruction in the prompt, neither of which guarantees consistent structure.",
 "remember": "Machine-parseable CI output → `--output-format json` plus `--json-schema`. Format requests in prose are the distractor.",
 "analogy": "The audit robot's report goes onto a fixed form with the same boxes every night — room, shelf, severity, fix — so the clerk's script can staple each finding to the right page of the file. A free-text report, however carefully requested, comes back laid out differently each night.",
 "svg": """<text class="lbl" x="46" y="20" text-anchor="middle">json</text>
<rect class="acc" x="16" y="26" width="60" height="78" rx="3"/>
<rect class="thin" x="24" y="36" width="10" height="10"/><line class="thin" x1="40" y1="41" x2="68" y2="41"/>
<rect class="thin" x="24" y="58" width="10" height="10"/><line class="thin" x1="40" y1="63" x2="68" y2="63"/>
<rect class="thin" x="24" y="80" width="10" height="10"/><line class="thin" x1="40" y1="85" x2="68" y2="85"/>
<path d="M82 64 h18 M94 58 l6 6 -6 6"/>
<rect class="paper" x="108" y="26" width="36" height="78" rx="2"/>
<path class="thin" d="M116 38 h20 M116 48 h20 M116 58 h20 M116 68 h20 M116 78 h20 M116 88 h20"/>
<circle class="accfill" cx="108" cy="48" r="3"/><circle class="accfill" cx="108" cy="68" r="3"/><circle class="accfill" cx="108" cy="88" r="3"/>""",
 "alt": "Fixed json form feeding pinned comments onto a document",
},
{
 "id": "D3-23",
 "title": "CLAUDE.md gives CI Claude your standards, fixtures and criteria",
 "concept": "`CLAUDE.md` is how CI-invoked Claude Code gets project context — testing standards, fixture conventions, review criteria and what counts as a valuable test — which raises test quality and cuts low-value output.",
 "tested": "CI-generated tests are trivial or ignore the fixtures the team already has, or automated review does not apply the team's criteria; the question asks where that context belongs. Answer: document it in `CLAUDE.md`. Distractors reach for a mechanism that does not exist or leave the context out and rely on the model to infer it.",
 "remember": "Project context for CI Claude lives in `CLAUDE.md`: testing standards, valuable-test criteria, available fixtures, review criteria. The same project file interactive sessions read.",
 "analogy": "The audit robot reads the company handbook before it starts, the same one the staff read: which tests matter, where the fixtures are kept, what a real finding looks like. Without it the robot files a stack of trivial notes.",
 "svg": """<rect class="tint" x="24" y="30" width="30" height="24" rx="4"/>
<circle class="thin" cx="33" cy="42" r="2"/><circle class="thin" cx="45" cy="42" r="2"/>
<line x1="39" y1="30" x2="39" y2="20"/><circle class="accfill" cx="39" cy="18" r="3"/>
<rect class="tint" x="20" y="58" width="38" height="30" rx="4"/>
<line class="dash thin" x1="62" y1="44" x2="82" y2="52"/>
<rect class="acc" x="86" y="26" width="52" height="66" rx="3"/>
<line class="acc" x1="96" y1="26" x2="96" y2="92"/>
<path class="acc thin" d="M104 40 h24 M104 52 h24 M104 64 h24 M104 76 h16"/>""",
 "alt": "Audit robot reading the company handbook",
},
{
 "id": "D3-24",
 "title": "Re-reviews see prior findings; test generation sees existing tests",
 "concept": "A re-run review gets last run's findings in context and reports only new or still-unaddressed issues; test generation gets the existing test files in context so it does not suggest duplicate scenarios.",
 "tested": "A CI review posts near-duplicate comments after every follow-up push, or generated tests repeat scenarios the suite already covers; the question asks the fix. Answer: put the earlier findings, or the existing tests, in context and instruct Claude accordingly. The distractor starts each run from a blank slate for the sake of objectivity, which re-litigates settled findings.",
 "remember": "Re-run → previous findings in context, report only new or unaddressed. Test generation → existing tests in context, no duplicates. Prior review findings travel; the generating session's own reasoning must not (D4-22).",
 "analogy": "On its second night in the same room the robot is handed last night's report and told to note only what is new or still not fixed, so the file does not fill with repeated notes. When it writes new checklists it is shown the ones already in the binder.",
 "svg": """<rect class="tint" x="16" y="24" width="50" height="70" rx="3"/>
<path class="thin" d="M24 38 h34 M24 50 h34 M24 62 h34 M24 74 h34"/>
<path d="M70 59 h18 M82 53 l6 6 -6 6"/>
<rect class="paper" x="94" y="24" width="50" height="70" rx="3"/>
<path class="dash thin" d="M102 38 h34 M102 50 h34 M102 62 h34 M102 74 h34"/>
<circle class="accfill" cx="99" cy="84" r="3"/><path class="acc" d="M106 84 h30"/>
<text class="lbl" x="41" y="110" text-anchor="middle">prev</text>
<text class="lbl" x="119" y="110" text-anchor="middle">new</text>""",
 "alt": "Yesterday's report feeding today's, which adds only one new line",
},
]
