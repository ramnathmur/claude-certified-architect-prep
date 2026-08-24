# Domain 3 — Claude Code Configuration & Workflows (20%)
S = 'stroke="#15130F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"'

ITEMS = [
{
 "title": "Where does this live? — the house",
 "world": "house", "flag": "live", "cite": "D3 §3.1–§3.4 · KD#1,#3",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M14 52L60 18l46 34v52H14z" fill="#fff"/>
   <rect x="24" y="60" width="26" height="20" rx="3" fill="#DFF2E7"/>
   <path d="M30 66h14M30 74h10" stroke-width="3"/>
   <rect x="62" y="60" width="18" height="26" rx="3" fill="#2E7D5B"/>
   <path d="M68 70h6" stroke="#fff" stroke-width="3"/>
   <rect x="86" y="64" width="14" height="20" rx="2" fill="#FDF0D8"/>
   <path d="M89 70h8M89 76h8" stroke-width="2.5"/></g></svg>''',
 "story": "<b>CLAUDE.md</b> is the note on the fridge — everyone reads it every day whether it applies or not. "
          "<b>.claude/rules/</b> is the laminated sign inside the bathroom door: read <b>only when you are in "
          "that room</b>. <b>Skills</b> are the recipe book you take down on purpose.",
 "tell": "You have picked <code>.claude/rules/</code> wrongly four times across three papers. "
         "If the question is not about <b>which files you are touching</b>, it is not rules.",
},
{
 "title": "The hierarchy concatenates — nothing overrides",
 "world": "house", "flag": "live", "cite": "D3 §3.1",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="26" y="18" width="68" height="20" rx="4" fill="#fff"/>
   <rect x="26" y="44" width="68" height="20" rx="4" fill="#DFF2E7"/>
   <rect x="26" y="70" width="68" height="20" rx="4" fill="#fff"/>
   <path d="M60 38v6M60 64v6" stroke-width="4"/>
   <path d="M14 20v76" stroke="#2E7D5B" stroke-width="4"/>
   <path d="M10 96h8" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Every discovered file is <b>stacked into context together</b>, root down to where you are working. "
          "A directory-level file does not replace the project one — Claude sees both, contradictions and all.",
 "tell": "There is no documented override precedence between CLAUDE.md levels. If two files disagree, "
         "edit the files. Conflicts do not resolve themselves by depth.",
},
{
 "title": "/memory tells you what actually loaded",
 "world": "house", "flag": "live", "cite": "D3 §3.1",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="18" y="24" width="52" height="66" rx="5" fill="#fff"/>
   <path d="M28 42h32M28 56h32M28 70h20" stroke-width="3"/>
   <circle cx="82" cy="46" r="17" fill="none" stroke="#2E7D5B" stroke-width="5"/>
   <path d="M94 58l12 12" stroke="#2E7D5B" stroke-width="5"/>
   <path d="M76 46l4 4 8-9" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "\"It follows the rule on Tuesdays\" is not a prompting problem. It is a <b>discovery</b> problem — "
          "and there is a command that just tells you which memory files are in the room.",
 "tell": "Works on one machine, not another → run <code>/memory</code> and compare. Diagnose before you "
         "move the file, and long before you restate the rule louder.",
},
{
 "title": "Project scope ships, user scope does not",
 "world": "house", "cite": "D3 §3.1 · KD#1",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="34" width="42" height="52" rx="5" fill="#2E7D5B"/>
   <path d="M24 52h22M24 64h22" stroke="#fff" stroke-width="3"/>
   <rect x="66" y="34" width="40" height="52" rx="5" fill="#fff"/>
   <path d="M76 52h20M76 64h14" stroke-width="3"/>
   <circle cx="86" cy="24" r="9" fill="#FDF0D8"/>
   <path d="M14 96h42" stroke="#2E7D5B" stroke-width="5"/></g></svg>''',
 "story": "The new teammate does not follow the convention because <b>the convention was never in the repo</b> "
          "— it has been sitting in three people's home directories all along.",
 "tell": "Everyone-but-the-new-person follows it → it is in <code>~/.claude/CLAUDE.md</code>. "
         "Move it to the project file, which is version-controlled.",
},
{
 "title": "@import keeps CLAUDE.md modular",
 "world": "house", "cite": "D3 §3.1",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="20" width="44" height="34" rx="5" fill="#fff"/>
   <path d="M24 34h26M24 44h16" stroke-width="3"/>
   <path d="M60 40h16v28h14" stroke="#2E7D5B"/>
   <rect x="72" y="56" width="34" height="24" rx="4" fill="#DFF2E7"/>
   <rect x="42" y="76" width="34" height="24" rx="4" fill="#DFF2E7"/>
   <path d="M38 44v42h4" stroke="#2E7D5B"/></g></svg>''',
 "story": "<code>@./standards/testing.md</code> pulls a file in where it sits. Each package imports only the "
          "standards its maintainers know apply — instead of one giant file everybody loads.",
 "tell": "<code>@</code> immediately before the path, no space. Relative paths resolve from the importing "
         "file. Maximum nesting depth is <b>5</b>.",
},
{
 "title": "Rules load on a glob, not on a mood",
 "world": "house", "cite": "D3 §3.2 · KD#3",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="22" width="88" height="24" rx="5" fill="#DFF2E7"/>
   <path d="M26 34h30" stroke-width="3"/>
   <path d="M74 28l6 6-6 6" stroke="#2E7D5B" stroke-width="4"/>
   <rect x="16" y="56" width="40" height="20" rx="4" fill="#fff"/>
   <rect x="64" y="56" width="40" height="20" rx="4" fill="#fff"/>
   <rect x="16" y="84" width="40" height="20" rx="4" fill="#fff"/>
   <path d="M24 66h20" stroke-width="3"/><path d="M72 66h20" stroke-width="3"/>
   <path d="M24 94h20" stroke-width="3"/></g></svg>''',
 "story": "Test files, API handlers and models sit side by side in every folder. A per-directory file cannot "
          "help. A <b>pattern on the filename</b> can.",
 "tell": "YAML frontmatter <code>paths:</code> globs. Loads only on matching files, so irrelevant "
         "conventions stay out of context. No precedence ordering, no registration step.",
},
{
 "title": "context: fork keeps the mess out of the room",
 "world": "house", "cite": "D3 §3.3 · KD#13",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="30" width="40" height="60" rx="5" fill="#fff"/>
   <path d="M22 46h24M22 58h24M22 70h14" stroke-width="3"/>
   <path d="M54 50h14" stroke-dasharray="5 5"/>
   <rect x="68" y="26" width="38" height="68" rx="5" fill="#DFF2E7" stroke-dasharray="8 6"/>
   <path d="M76 40h22M76 50h22M76 60h22M76 70h22M76 80h14" stroke-width="2.5"/></g></svg>''',
 "story": "The exploration generates four thousand lines. Run it in a <b>side room</b> and only the summary "
          "comes back through the door.",
 "tell": "Skill floods the session or rejected alternatives bleed into later turns → <code>context: fork</code>. "
         "Scoping what it may touch → <code>allowed-tools</code>, in SKILL.md frontmatter. Never <code>.mcp.json</code>.",
},
{
 "title": "Commands in the repo ship with the clone",
 "world": "house", "cite": "D3 §3.4",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="18" y="30" width="84" height="56" rx="6" fill="#fff"/>
   <path d="M18 48h84"/>
   <circle cx="30" cy="39" r="4" fill="#2E7D5B"/>
   <rect x="30" y="58" width="42" height="14" rx="4" fill="#DFF2E7"/>
   <path d="M38 65h26" stroke-width="3"/>
   <path d="M82 58v20M74 70l8 8 8-8" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Six people building six private versions of the same prompt is the smell. Put it in the repo and "
          "it arrives with the next <code>git pull</code>, configured by nobody.",
 "tell": "Team-wide → <code>.claude/commands/</code> in the repo. Just you → <code>~/.claude/commands/</code>. "
         "A personal skill of the same name <b>overrides</b> the project one.",
},
{
 "title": "Your version of /commit beats the team's",
 "world": "house", "cite": "D3 §3.5 · KD#4",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="26" width="44" height="34" rx="5" fill="#fff"/>
   <path d="M26 43h24" stroke-width="3.5"/>
   <rect x="16" y="70" width="44" height="34" rx="5" fill="#2E7D5B"/>
   <path d="M26 87h24" stroke="#fff" stroke-width="3.5"/>
   <path d="M70 87h20" stroke="#2E7D5B" stroke-width="4"/>
   <path d="M82 81l8 6-8 6" stroke="#2E7D5B" stroke-width="4"/>
   <circle cx="100" cy="43" r="9" fill="#DFF2E7"/></g></svg>''',
 "story": "Same name, personal wins. That is the point — you can tune the team's command for yourself "
          "<b>without forking it or inventing a name nobody else uses</b>.",
 "tell": "Customise <code>/commit</code> privately → <code>~/.claude/skills/commit/SKILL.md</code>, same "
         "name. Creating <code>/my-commit</code> is the wrong answer: it loses the familiar command.",
},
{
 "title": "Plan up front or pay for the rework",
 "world": "house", "cite": "D3 §3.6",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="20" width="52" height="68" rx="5" fill="#fff"/>
   <path d="M26 36h32M26 48h32M26 60h20" stroke-width="3"/>
   <path d="M76 34v46" stroke="#2E7D5B" stroke-width="4"/>
   <path d="M76 30l-8 8M76 30l8 8" stroke="#2E7D5B" stroke-width="4"/>
   <circle cx="94" cy="72" r="12" fill="#FF4757"/>
   <path d="M89 67l10 10M99 67l-10 10" stroke="#fff" stroke-width="3.5"/></g></svg>''',
 "story": "\"I will start coding and switch to planning if it gets hairy\" means discovering the hard part "
          "<b>after</b> writing the edits you now have to undo.",
 "tell": "Dozens of files, several viable approaches, a 45-file migration → plan first. Clear spec, single "
         "file, known stack trace → just do it. Reactive switching is the named trap.",
},
{
 "title": "Let it interview you first",
 "world": "house", "cite": "D3 §3.7.1",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="38" cy="40" r="16" fill="#fff"/>
   <path d="M22 92c0-12 7-20 16-20s16 8 16 20"/>
   <rect x="62" y="22" width="44" height="34" rx="8" fill="#DFF2E7"/>
   <path d="M72 34h24M72 44h14" stroke-width="3"/>
   <path d="M74 56l-6 12 14-12"/>
   <path d="M84 74v6M84 88v4" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Three generated versions, three different missed requirements, and the person asking does not know "
          "the domain well enough to have listed them. <b>Reverse the direction</b>: let it ask.",
 "tell": "Unfamiliar domain + underspecified brief → one interview turn beats several correction cycles. "
         "A longer spec written by someone who does not know the rules cannot contain the rules.",
},
{
 "title": "Write the failing test, not a better description",
 "world": "house", "cite": "D3 §3.7.2",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="18" y="26" width="84" height="30" rx="5" fill="#FF4757"/>
   <path d="M30 41h20M62 41h28" stroke="#fff" stroke-width="3.5"/>
   <circle cx="56" cy="41" r="5" fill="#fff"/>
   <rect x="18" y="66" width="84" height="30" rx="5" fill="#DFF2E7"/>
   <path d="M30 81l8 8 16-18" stroke="#2E7D5B" stroke-width="5"/>
   <path d="M64 81h26" stroke-width="3.5"/></g></svg>''',
 "story": "Prose about an edge case is interpreted differently every time. A test with the <b>exact row in "
          "and the exact row out</b> is a machine-checkable definition of done.",
 "tell": "Three rounds of describing the bug, three partial fixes → give it the concrete failing case. "
         "Writing tests <b>after</b> is verification, not test-driven iteration.",
},
{
 "title": "Examples supersede prose — they do not join it",
 "world": "house", "flag": "live", "cite": "D3 §3.7.3 · KD#16",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="20" width="40" height="26" rx="4" fill="#fff"/>
   <path d="M24 30h24M24 38h16" stroke-width="3"/>
   <path d="M62 33h16" stroke="#2E7D5B" stroke-width="4"/>
   <path d="M72 27l8 6-8 6" stroke="#2E7D5B" stroke-width="4"/>
   <rect x="84" y="20" width="22" height="26" rx="4" fill="#DFF2E7"/>
   <rect x="16" y="62" width="40" height="26" rx="4" fill="#fff"/>
   <path d="M62 75h16" stroke="#2E7D5B" stroke-width="4"/>
   <path d="M72 69l8 6-8 6" stroke="#2E7D5B" stroke-width="4"/>
   <rect x="84" y="62" width="22" height="26" rx="4" fill="#DFF2E7"/></g></svg>''',
 "story": "Once wording has failed to produce a consistent shape, <b>rewording it again is not a second "
          "helpful action</b> — it is the thing that already did not work.",
 "tell": "Exam 17 cost you this one: you picked examples <b>and</b> \"rewrite the paragraphs more precisely\". "
         "2–3 concrete input→output pairs. Not more adjectives alongside them.",
},
{
 "title": "Batch feedback on interaction, not on size",
 "world": "house", "flag": "live", "cite": "D3 §3.7.4",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="38" cy="38" r="14" fill="#DFF2E7"/><circle cx="66" cy="38" r="14" fill="#DFF2E7"/>
   <path d="M52 38h0" /><path d="M45 30l14 16M59 30L45 46" stroke="#2E7D5B" stroke-width="3"/>
   <circle cx="52" cy="84" r="14" fill="#fff"/>
   <path d="M52 62v8" stroke-dasharray="4 5"/>
   <path d="M88 26v72" stroke="#15130F" stroke-width="4" stroke-dasharray="7 7"/></g></svg>''',
 "story": "The locking bug and the retry bug are <b>welded together</b> — fix them apart and the second patch "
          "contradicts the first. The typo is welded to nothing.",
 "tell": "The axis is <b>interacting vs independent</b>. Not mechanical vs substantive, not big vs small. "
         "Interacting issues go in one message; independent ones go one at a time.",
},
{
 "title": "CI needs -p, and it needs last run's findings",
 "world": "house", "cite": "D3 §3.8 · KD#15",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="26" width="92" height="30" rx="5" fill="#15130F"/>
   <path d="M24 41h10" stroke="#DFF2E7" stroke-width="4"/>
   <path d="M42 41h44" stroke="#2E7D5B" stroke-width="4"/>
   <rect x="14" y="68" width="42" height="34" rx="5" fill="#fff"/>
   <path d="M24 82h22M24 92h14" stroke-width="3"/>
   <path d="M60 85h14" stroke="#2E7D5B" stroke-width="4"/>
   <path d="M68 79l8 6-8 6" stroke="#2E7D5B" stroke-width="4"/>
   <rect x="80" y="68" width="26" height="34" rx="5" fill="#DFF2E7"/></g></svg>''',
 "story": "Without <code>-p</code> the pipeline hangs waiting for a human who is not there. And a reviewer "
          "with <b>no memory of last run</b> re-posts every comment it already made.",
 "tell": "<code>-p</code>/<code>--print</code> is the documented flag — <code>--batch</code> and "
         "<code>CLAUDE_HEADLESS</code> do not exist. Feed prior findings into the re-run and ask for new or "
         "unresolved only.",
},
{
 "title": "An iterative review cannot run on batch",
 "world": "bay", "cite": "D3 §3.10 · KD#14",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="34" width="52" height="34" rx="5" fill="#DBF1F4"/>
   <path d="M66 51h16" stroke="#0E7C8C" stroke-width="4"/>
   <rect x="82" y="34" width="24" height="34" rx="5" fill="#fff"/>
   <path d="M40 68v14" stroke="#FF4757" stroke-width="4"/>
   <path d="M28 88l24-12M28 76l24 12" stroke="#FF4757" stroke-width="4"/>
   <circle cx="40" cy="98" r="7" fill="#FF4757"/></g></svg>''',
 "story": "A review that <b>fetches related files mid-analysis</b> needs a conversation. Batch is one shot: "
          "submit, get one response back, done. There is no point at which your code can hand it a tool result "
          "and let it carry on thinking.",
 "tell": "Iterative tool-calling review → synchronous, whatever the cost saving. Overnight tech-debt "
         "reports, nightly test generation, weekly audits → batch.",
},
{
 "title": "Structured output from the CLI",
 "world": "house", "cite": "D3 §3.9",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="24" width="88" height="72" rx="6" fill="#fff"/>
   <path d="M16 44h88"/>
   <path d="M28 60h20M28 74h30" stroke-width="3"/>
   <rect x="62" y="54" width="32" height="30" rx="4" fill="#DFF2E7"/>
   <path d="M70 64h16M70 74h10" stroke-width="3"/>
   <circle cx="28" cy="34" r="4" fill="#2E7D5B"/></g></svg>''',
 "story": "If a script has to post file, line, severity and a fix to an API, you do not want prose that a "
          "regex nearly parses. You want a <b>shape that is guaranteed</b>.",
 "tell": "<code>--output-format json</code> with <code>--json-schema</code>. Not a format section in "
         "CLAUDE.md, not a prompt instruction, not a more forgiving parser.",
},
{
 "title": "CLAUDE.md holds standards; skills hold procedures",
 "world": "house", "flag": "live", "cite": "D3 §3.11",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="18" width="88" height="34" rx="5" fill="#fff"/>
   <path d="M26 30h30M26 40h50" stroke-width="3"/>
   <path d="M78 24l8 8-8 8" stroke="#FF4757" stroke-width="4"/>
   <rect x="16" y="64" width="40" height="38" rx="5" fill="#DFF2E7"/>
   <path d="M24 78h24M24 88h16" stroke-width="3"/>
   <rect x="66" y="64" width="38" height="38" rx="5" fill="#DFF2E7"/>
   <path d="M74 78h22M74 88h14" stroke-width="3"/></g></svg>''',
 "story": "400 lines mixing naming standards with a release checklist and a migration runbook. The standards "
          "must load every session. The runbook must load <b>the day you migrate</b>.",
 "tell": "Keep universal standards in CLAUDE.md; move workflow procedures to skills. And background prose "
         "about company history? Just cut it — it changes nothing the model does.",
},
{
 "title": "/compact loses the numbers",
 "world": "bay", "cite": "D3 §3.12 · KD#22",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="24" width="44" height="72" rx="5" fill="#fff"/>
   <path d="M22 40h28M22 52h28M22 64h20M22 76h24" stroke-width="3"/>
   <path d="M66 60h12" stroke="#0E7C8C" stroke-width="4"/>
   <rect x="80" y="46" width="26" height="28" rx="4" fill="#DBF1F4"/>
   <path d="M86 58h14" stroke-width="3"/>
   <path d="M86 66h6" stroke="#FF4757" stroke-width="3"/></g></svg>''',
 "story": "Compaction keeps the story and blurs the <b>digits</b>. \"£310 on the 12th\" becomes \"a payment "
          "plan was discussed\", which is useless if the next step needs £310.",
 "tell": "Discovery about to flood the window → Explore subagent, which returns a summary. Mid-task with "
         "exact values still needed → do not <code>/compact</code>.",
},
]
