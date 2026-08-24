# Domain 2 part B — Tool Design & MCP Integration · building: the library

ITEMS = [
{
 "id": "D2-11",
 "title": "${ENV_VAR} expansion keeps secrets out of the repo",
 "concept": "`.mcp.json` supports `${VAR_NAME}` expansion, so the shared server config can be version-controlled while each developer's token is supplied from their own environment at runtime.",
 "tested": "A team shares one MCP server and every developer has a different token; the question asks how to configure it. Answer: the server in project-scoped `.mcp.json` with `${GITHUB_TOKEN}` expansion, the variable name documented for the team. Distractors have each developer add the server in `~/.claude.json`, which leaves the team on inconsistent tooling, or commit a token value into the repo.",
 "remember": "Shared server, per-developer secret: `.mcp.json` with `${GITHUB_TOKEN}`. The repo holds the variable name, the environment holds the value. Any option that commits a token value is wrong.",
 "analogy": "The institutional subscription is posted on the reading-room wall for everyone: same databases, same terms. The PIN is not posted, because each reader keys in the one on their own card. Pinning a PIN to the wall would hand that reader's account to the whole town.",
 "svg": """<rect class="paper" x="14" y="18" width="64" height="86" rx="3"/>
<line class="thin" x1="24" y1="30" x2="68" y2="30"/>
<circle class="thin" cx="30" cy="46" r="6"/>
<path class="thin" d="M36 46 h22 M52 46 v5 M58 46 v5"/>
<line class="no" x1="36" y1="39" x2="50" y2="53"/>
<line class="no" x1="50" y1="39" x2="36" y2="53"/>
<rect class="acc dash" x="22" y="68" width="48" height="18" rx="2"/>
<text class="lbl" x="46" y="80" text-anchor="middle">${T}</text>
<path class="acc" d="M100 77 h-18 M86 72 l-5 5 5 5"/>
<circle class="acc" cx="112" cy="77" r="8"/>
<path class="acc" d="M120 77 h22 M134 77 v6 M140 77 v6"/>
<text class="lbl" x="118" y="58" text-anchor="middle">env</text>""",
 "alt": "Config sheet with a placeholder slot; a committed key crossed out",
},
{
 "id": "D2-12",
 "title": "Discovered at connection, all servers' tools are available together",
 "concept": "Tools from all configured MCP servers are discovered when Claude Code connects to them, and every one of those tools is available to the agent at the same time.",
 "tested": "A developer has a shared server in `.mcp.json` and a personal experimental one in `~/.claude.json`, and the question asks what the agent can call. Answer: the tools of both, discovered at connection and offered together. Distractors have one scope replace the other, or require the agent to select which server is active before it can call anything.",
 "remember": "All configured servers connect, all their tools are on the table at once. The two scopes add up; neither `.mcp.json` nor `~/.claude.json` switches the other off.",
 "analogy": "Your card opens the institutional databases and the ones you subscribed to yourself, and at the terminal both lists come up on one screen. The library does not make you nominate a single provider for the afternoon and lock the rest away.",
 "svg": """<rect class="tint" x="10" y="20" width="42" height="26" rx="3"/>
<text class="lbl" x="31" y="37" text-anchor="middle">proj</text>
<rect class="tint" x="10" y="76" width="42" height="26" rx="3"/>
<text class="lbl" x="31" y="93" text-anchor="middle">user</text>
<path d="M52 33 h14 v28"/>
<path d="M52 89 h14 v-28"/>
<path d="M66 61 h14 M74 56 l6 5 -6 5"/>
<rect class="tint" x="84" y="32" width="60" height="58" rx="3"/>
<rect class="acc" x="92" y="40" width="18" height="16" rx="2"/>
<rect class="acc" x="118" y="40" width="18" height="16" rx="2"/>
<rect class="acc" x="92" y="66" width="18" height="16" rx="2"/>
<rect class="acc" x="118" y="66" width="18" height="16" rx="2"/>""",
 "alt": "Two servers labelled proj and user feeding one tray of four tools",
},
{
 "id": "D2-13",
 "title": "MCP resources expose content catalogs",
 "concept": "MCP resources expose content catalogs such as issue summaries, documentation hierarchies and database schemas, giving the agent visibility into available data without exploratory tool calls.",
 "tested": "An agent working against a project tracker spends turns guessing queries to discover what issues exist, and the question asks how to give it visibility. Answer: expose the catalog as an MCP resource, which the agent reads as context and then follows with targeted tool calls. Distractors add a `list_everything` tool the agent has to remember to call, or paste the whole issue database into the system prompt.",
 "remember": "Resources are read, tools act. An agent guessing queries to find out what exists needs the catalog exposed as a resource, not added as another tool.",
 "analogy": "The card catalog by the door tells you what the library holds before you walk a single aisle. Nothing is fetched and nothing is checked out; you read it, then send one request slip for the shelf you actually want.",
 "svg": """<rect class="acc" x="12" y="34" width="56" height="46" rx="3"/>
<line class="acc" x1="12" y1="57" x2="68" y2="57"/>
<line class="acc" x1="32" y1="45" x2="48" y2="45"/>
<line class="acc" x1="32" y1="69" x2="48" y2="69"/>
<path class="acc" d="M74 57 h16 M84 52 l6 5 -6 5"/>
<line x1="96" y1="60" x2="150" y2="60"/>
<rect class="tint" x="100" y="28" width="11" height="32" rx="1"/>
<rect class="accfill" x="115" y="22" width="11" height="38" rx="1"/>
<rect class="tint" x="130" y="32" width="11" height="28" rx="1"/>
<polyline class="thin" points="96,100 109,84 122,100 135,84 148,100"/>
<line class="no" x1="114" y1="84" x2="130" y2="100"/>
<line class="no" x1="130" y1="84" x2="114" y2="100"/>""",
 "alt": "Card catalog points to one book; a wandering search path crossed out",
},
{
 "id": "D2-14",
 "title": "Fix the description when the agent prefers Grep",
 "concept": "An agent that keeps choosing a built-in such as `Grep` over a more capable MCP tool is fixed by enhancing that tool's description to detail its capabilities and outputs.",
 "tested": "A semantic, index-backed code-search server is installed and the agent keeps reaching for `Grep`; the question asks the most effective fix. Answer: enhance the MCP tool's description to state what it returns that `Grep` cannot. Distractors remove or disable `Grep`, which breaks legitimate content searches, or add a blanket system-prompt rule to prefer MCP tools, which misroutes the cases where the built-in is the right tool.",
 "remember": "Selection runs on descriptions, so fix the signal before removing the built-in. Name the capability and the output that the built-in cannot provide.",
 "analogy": "The blurb on the new research room's door says only that it searches text, so readers keep using the plain word-match terminal they already know. Rewrite the blurb to say what it returns that word-matching cannot, and they come in. Taking the old terminal away would only strand the readers whose question really was a word match.",
 "svg": """<rect class="tint" x="12" y="34" width="44" height="70" rx="2"/>
<text class="lbl" x="34" y="28" text-anchor="middle">grep</text>
<circle class="thin" cx="48" cy="70" r="2"/>
<rect class="thin" x="24" y="66" width="20" height="16" rx="2"/>
<path class="thin" d="M28 66 v-6 a6 6 0 0 1 12 0 v6"/>
<line class="no" x1="27" y1="67" x2="41" y2="81"/>
<line class="no" x1="41" y1="67" x2="27" y2="81"/>
<rect class="tint" x="76" y="34" width="68" height="70" rx="2"/>
<circle class="thin" cx="136" cy="70" r="2"/>
<rect class="acc" x="86" y="44" width="48" height="28" rx="2"/>
<path class="acc thin" d="M94 54 h32 M94 62 h22"/>
<text class="lbl" x="110" y="28" text-anchor="middle">mcp</text>""",
 "alt": "MCP door gains a detailed sign; padlock on grep crossed out",
},
{
 "id": "D2-15",
 "title": "Community server for standard integrations, custom for team workflows",
 "concept": "For standard integrations such as Jira, choose an existing community MCP server, and reserve custom server implementations for workflows specific to your team.",
 "tested": "A team needs its agent to reach a standard system such as Jira and also to run one workflow nobody else has, and the question asks what to build. Answer: adopt the community server for Jira, write a custom server only for the team-specific workflow. The distractor builds a Jira server from scratch for control, taking on the maintenance of a problem that is already solved.",
 "remember": "Standard integration: existing community server. Team-specific workflow: custom server. Building your own Jira server is effort spent in the wrong place.",
 "analogy": "A book that every library in the country already holds arrives by interlibrary loan in two days. You build your own archive for the material that exists nowhere else, the parish registers and the town's own papers. Nobody re-buys the national collection to keep a copy on site.",
 "svg": """<rect class="tint" x="12" y="32" width="46" height="38" rx="3"/>
<path d="M12 32 l23 -12 l23 12"/>
<path d="M62 50 h24 M80 45 l6 5 -6 5"/>
<rect class="tint" x="92" y="32" width="50" height="38" rx="3"/>
<path d="M92 32 l25 -12 l25 12"/>
<text class="lbl" x="32" y="78" text-anchor="middle">copy</text>
<rect class="dash" x="16" y="82" width="32" height="24" rx="2"/>
<line class="no" x1="22" y1="88" x2="42" y2="100"/>
<line class="no" x1="42" y1="88" x2="22" y2="100"/>
<text class="lbl" x="120" y="78" text-anchor="middle">own</text>
<rect class="acc" x="104" y="82" width="32" height="24" rx="2"/>
<line class="acc" x1="112" y1="82" x2="112" y2="106"/>""",
 "alt": "Book arrives on loan from another library; a rebuilt copy crossed out",
},
{
 "id": "D2-16",
 "title": "Grep searches inside files; Glob matches paths",
 "concept": "`Grep` searches file contents for patterns such as function names, error messages and import statements, while `Glob` matches file paths by name or extension pattern.",
 "tested": "One question asks for every file that references a deprecated function, another for every TypeScript test file, and each offers the opposite tool. `Glob **/formatDate*` finds only files named after the function and not the files that call it; grepping for the word `test` matches unrelated files and misses tests that never contain the word.",
 "remember": "Inside files: `Grep`. File names and paths: `Glob`. Callers, error strings and imports are content; `**/*.test.tsx` is a path pattern.",
 "analogy": "The library's full-text search reads every page and returns the books that mention a name; the title index reads only the spines. Ask the title index who cited an author and it hands back the one book with that author's name on the cover.",
 "svg": """<rect class="tint" x="10" y="26" width="60" height="66" rx="3"/>
<line x1="40" y1="26" x2="40" y2="92"/>
<path class="thin" d="M16 40 h18 M46 40 h18 M16 52 h18 M46 52 h18 M16 64 h18 M46 64 h18"/>
<rect class="accfill" x="46" y="72" width="16" height="7" rx="2"/>
<text class="lbl" x="40" y="106" text-anchor="middle">grep</text>
<line x1="88" y1="92" x2="150" y2="92"/>
<rect class="tint" x="92" y="52" width="12" height="40" rx="1"/>
<rect class="acc" x="108" y="44" width="12" height="48" rx="1"/>
<rect class="tint" x="124" y="54" width="12" height="38" rx="1"/>
<rect class="tint" x="138" y="48" width="12" height="44" rx="1"/>
<text class="lbl" x="120" y="106" text-anchor="middle">glob</text>""",
 "alt": "Open book with a highlighted line; shelf with one spine marked",
},
{
 "id": "D2-17",
 "title": "Edit needs a unique anchor; otherwise Read + Write",
 "concept": "`Read` and `Write` handle whole files while `Edit` replaces a unique text match, so when the anchor appears more than once `Edit` fails and `Read` then `Write` is the fallback.",
 "tested": "`Edit` fails on a file because the anchor text is not unique, and the question asks the next step. Answer: `Read` the file, modify the content, then `Write` it back. Distractors retry `Edit` with a shorter anchor, which is more likely to be non-unique rather than less, or force the replacement with `sed` through `Bash`, bypassing the tool designed for the job.",
 "remember": "`Edit` needs exactly one occurrence. Non-unique anchor: `Read` + `Write`. A shorter anchor matches more places, not fewer, and `sed` via `Bash` is not the sanctioned fallback.",
 "analogy": "Pencilling a correction works while the phrase sits on one page only; when the same phrase appears on three, the pencil has nowhere to land. The sheet then comes out of the binder, is re-typed in full, and goes back in. Shortening the phrase you are hunting for only puts it on more pages.",
 "svg": """<rect class="paper" x="10" y="16" width="56" height="74" rx="3"/>
<line class="thin" x1="18" y1="28" x2="58" y2="28"/>
<rect class="tint" x="18" y="36" width="26" height="9" rx="2"/>
<line class="thin" x1="18" y1="54" x2="58" y2="54"/>
<rect class="tint" x="18" y="62" width="26" height="9" rx="2"/>
<line class="thin" x1="18" y1="80" x2="58" y2="80"/>
<line class="no" x1="42" y1="46" x2="58" y2="62"/>
<line class="no" x1="58" y1="46" x2="42" y2="62"/>
<path class="acc" d="M72 53 h16 M84 48 l5 5 -5 5"/>
<rect class="acc" x="94" y="16" width="52" height="74" rx="3"/>
<path class="acc thin" d="M102 30 h36 M102 42 h36 M102 54 h36 M102 66 h36 M102 78 h24"/>
<text class="lbl" x="120" y="106" text-anchor="middle">R+W</text>""",
 "alt": "Page with the same phrase twice, crossed; whole sheet re-typed instead",
},
{
 "id": "D2-18",
 "title": "Grep to find entry points, then Read to trace",
 "concept": "Codebase understanding is built incrementally: `Grep` locates entry points, then `Read` follows imports and traces flows, rather than reading every file up front.",
 "tested": "A question asks how to build understanding of an unfamiliar codebase. Answer: `Grep` for entry points, then `Read` the files it turns up and follow their imports. Distractors read every file first for full context, or `Glob` the whole tree and `Read` each match before searching, which is the same anti-pattern with an extra step.",
 "remember": "Search first, read second, repeat: content search drives discovery and reads stay targeted. Reading or globbing the whole tree up front is the anti-pattern.",
 "analogy": "A reader after one citation asks at the desk for the shelfmark, walks to that shelf, and follows the footnotes from there. Carrying every book on the floor to a table first fills the table before any reading begins.",
 "svg": """<line x1="10" y1="40" x2="70" y2="40"/>
<rect class="tint" x="14" y="16" width="10" height="24" rx="1"/>
<rect class="acc" x="28" y="12" width="10" height="28" rx="1"/>
<rect class="tint" x="42" y="18" width="10" height="22" rx="1"/>
<rect class="tint" x="56" y="14" width="10" height="26" rx="1"/>
<circle cx="33" cy="30" r="10"/>
<line x1="40" y1="37" x2="50" y2="47"/>
<path class="acc" d="M74 26 h16 M84 21 l6 5 -6 5"/>
<rect class="paper" x="96" y="10" width="24" height="32" rx="2"/>
<path class="acc" d="M108 44 v14 h12 M116 53 l5 5 -5 5"/>
<rect class="paper" x="124" y="44" width="24" height="32" rx="2"/>
<rect class="tint" x="14" y="74" width="50" height="8" rx="2"/>
<rect class="tint" x="20" y="84" width="38" height="8" rx="2"/>
<rect class="tint" x="16" y="94" width="46" height="8" rx="2"/>
<line class="no" x1="29" y1="79" x2="49" y2="97"/>
<line class="no" x1="49" y1="79" x2="29" y2="97"/>""",
 "alt": "Magnifier picks one book, two pages traced, a stacked pile crossed out",
},
{
 "id": "D2-19",
 "title": "List every exported name, then search each one",
 "concept": "Tracing a function's usage across wrapper modules starts by identifying every exported name, then searching for each of those names across the codebase.",
 "tested": "A function is re-exported through wrapper modules under a second name and a rename has to reach every caller; the question asks how to find them all. Answer: collect the exported names from the wrapper modules first, then search for each name. The distractor searches the original name alone and reports those call sites as the complete set, missing every consumer that imports the wrapper.",
 "remember": "Two passes: gather every exported name, wrapper aliases included, then search each name. One search on the original name misses the callers that import the wrapper.",
 "analogy": "A work reissued under a second title sits on the shelves twice, and a search for the first title returns half the readers who cited it. The librarian checks the front matter for every title the work has carried, then searches each one in turn.",
 "svg": """<rect class="tint" x="10" y="32" width="42" height="56" rx="3"/>
<line x1="18" y1="32" x2="18" y2="88"/>
<text class="lbl" x="36" y="56" text-anchor="middle">calc</text>
<text class="lbl" x="36" y="74" text-anchor="middle">get</text>
<path class="acc" d="M56 48 h18 M68 43 l6 5 -6 5"/>
<path class="acc" d="M56 86 h18 M68 81 l6 5 -6 5"/>
<rect class="paper" x="80" y="32" width="66" height="32" rx="2"/>
<circle class="accfill" cx="92" cy="48" r="4"/>
<circle class="accfill" cx="110" cy="48" r="4"/>
<circle class="accfill" cx="128" cy="48" r="4"/>
<rect class="paper" x="80" y="70" width="66" height="32" rx="2"/>
<circle class="accfill" cx="96" cy="86" r="4"/>
<circle class="accfill" cx="120" cy="86" r="4"/>""",
 "alt": "One book listed under two titles, each search returning its own hits",
},
]
