# Claude 101 — Source of Truth (Captured Course Content)

**Source:** https://anthropic.skilljar.com/claude-101
**Captured:** 2026-06-04 via authenticated Chrome session (Ram, Infosys partner access)
**Capture manifest:** 14 lessons total (13 text + 1 quiz). Capture in progress.

> This file is the ground truth. The HTML conversion traces every claim back to this file. Lessons with embedded video are captured via their on-page text + Key Takeaways (Anthropic provides full text alongside video). Where only video exists with no text, it is marked `SOURCE-GAP`.

---

## Lesson 1 — What is Claude? (Section: Meet Claude)

**Estimated time:** 15 minutes (page also notes "10 minutes" for core section)

**Learning objectives:**
- Explain what Claude is and the principles that guide its design
- Describe Claude's core capabilities and how it differs from a simple chatbot
- Identify the different ways to access Claude (web, desktop, and mobile)

**Course roadmap (overview of all 5 sections):**
- **Meet Claude** — What is Claude, how do you talk to it, and how do you get great results?
- **Organizing your work** — How do Projects, Artifacts, and Skills give Claude structure and reusable knowledge?
- **Expanding Claude's reach** — How do Connectors, Enterprise Search, and Research bring your tools and the web into the conversation?
- **Putting it all together** — What does Claude look like in action across roles, and where else can you work with it?
- **Conclusion & certificate** — Where do you go from here, and how do you earn your certificate?

**Intro:** Claude is more than a chatbot—it's an AI assistant designed to be your thinking partner. This lesson covers what makes Claude different from other AI tools and how it can help with a wide variety of work tasks.

**Key takeaways:**
- **Claude is built to be helpful, harmless, and honest:** Claude is guided by principles that help it avoid toxic or discriminatory outputs, avoid helping humans engage in illegal or unethical activities, and broadly behave as a helpful, honest, and harmless AI system. This approach, called **Constitutional AI**, means Claude is trained to align with human values and operate transparently.
- **Claude is more than a chatbot:** Capable of a wide variety of conversational and text-processing tasks while maintaining high reliability and predictability — summarization, search, creative and collaborative writing, Q&A, coding, and more. Think of Claude as a thought partner for complex problems, not just simple questions.
- **Claude is designed to be steerable and collaborative:** Claude can take direction on personality, tone, and behavior. Customers report Claude is much less likely to produce harmful outputs, easier to converse with, and more steerable.
- **You can access Claude wherever you work:** Claude apps are available to all plan types—Free, Pro, Max, Team, and Enterprise. Conversations, projects, memory, and preferences sync across all devices when signed in. Available through web, desktop, and mobile apps.

**Understanding Claude's capabilities:**
- **Writing and content creation:** Collaborate on social media posts, professional emails, complex reports. Claude takes direction on personality and tone; you iterate together on structure and clarity.
- **Research and analysis:** Explore research angles, compile findings, analyze data. You can upload documents — enabled by Claude's large context window, which can ingest 200K+ tokens (about 500 pages of text or more), with up to **1M tokens** available on Pro, Max, Team, and Enterprise plans when using Opus 4.7.
- **Coding assistance:** Claude Opus 4.7 is described as "our most powerful model yet and the best coding model in the world." Helps write, debug, and explain code across multiple languages.
- **Problem-solving and reasoning:** Handles complex cognitive tasks, math, strategic thinking, research. Claude Opus 4.7 and Sonnet 4.7 are hybrid models offering two modes: near-instant responses and extended thinking for deeper reasoning. Extended thinking lets Claude work step-by-step.
- **Learning new things:** Adapts to your learning style and pace. **Learning mode** guides your reasoning process rather than providing answers, helping develop critical thinking.

(Pointers: use-case gallery on claude.com; AI Capabilities course for deeper dive.)

**Ways to access Claude:**
- **Claude.ai** (plus mobile and desktop apps) — primary way most people interact with Claude. Ask questions, brainstorm, create/edit documents. Ideal for conversations, writing, research, analysis, creating files. **This is the course's focus.**
- **Claude Code** — agentic coding tool designed for developers but usable for all kinds of file manipulation on your desktop. Can directly edit files, run commands, create commits.
- **Claude and Slack** — brings Claude into your team's communication tool. Chat in the AI assistant header from any channel/conversation, or mention @Claude in threads. When connected, Claude searches your workspace's channels, DMs, and shared files for context.
- **Claude for Excel** — work with Claude in a sidebar in Microsoft Excel; Claude can read, analyze, modify, and create workbooks. Best for model analysis, assumption updates, error debugging, template population, formula explanations, multi-tab navigation.

(Course focuses primarily on Claude.ai; see Claude Code in Action for dev workflows.)

**Lesson reflection:** What tasks in your current work might benefit from having Claude as a thinking partner? Look at your calendar (or ask Claude to) and identify a few tasks to use Claude for.

**What's next:** Next lesson — navigate the Claude interface, start your first conversation, understand the basics of how Claude responds.

---

## Lesson 2 — Your first conversation with Claude (Section: Meet Claude)

**Estimated time:** 20 minutes
**Contains:** Video — "Getting started with Claude.ai" (key points captured in text below)

**Learning objectives:**
- Start a new conversation with Claude and navigate the interface
- Write effective prompts using clear, specific language
- Upload files and images to provide Claude with additional context
- Use follow-up messages to iterate and refine Claude's responses

**Key takeaways:**
- Claude is a powerful, intelligent collaborator that amplifies your capabilities. Claude brings AI intelligence; you bring the context and expertise that makes the work meaningful.
- The best approach when speaking to Claude is like you would a coworker—naturally, concisely, and conversationally.
- Before your next conversation, consider: setting the stage (your role, objectives, context), defining the task (what action you want Claude to take), and specifying rules (style, tone, examples).
- When you upload relevant documents/background into a chat, Claude considers that content—a shortcut so Claude understands your needs.
- The real power of Claude comes with continued and frequent communication, not just one-off prompts.

**Starting your first conversation:** Open Claude.ai → clean interface with a text input area at the bottom. Prompts can range from simple questions (brainstorm code names) to complex requests to co-create files.

**Writing effective prompts** — all interactions begin with a prompt; prompts + other context impact Claude's response. Speak to Claude like a coworker. A good prompt considers:
- **Setting the stage:** What is your role and objectives? Any context about your work Claude should know?
- **Defining the task:** What action do you want Claude to take? Write, analyze, build, something else?
- **Specifying rules:** What style or tone? Any examples to attach showing what you're looking for?

**Example prompt (uses all three elements):**
> "I'm the marketing lead at an indie streaming startup, and we're preparing an investor pitch deck for Series A investors. Can you research the current state of the independent film streaming market and identify key trends, competitor positioning, and growth opportunities? Use current web research with citations and structure it as a professional report of up to 5 pages, with an executive summary, market analysis, competitive landscape, and growth opportunities."

In this prompt: Setting the stage (investor pitch deck context/objective); Defining the task (research the market + details); Specifying rules (current web research with citations, structured professional report).

**Want to go deeper?** This prompt framework is adapted from the **4D Framework for AI Fluency**, developed through research collaboration between Professor Rick Dakan (Ringling College of Art and Design) and Professor Joseph Feller (University College Cork). Four core competencies—**Delegation, Description, Discernment, and Diligence**—enable effective AI collaboration. (Free AI Fluency course available.)

**Adding context:** Uploads, connectors, and custom preferences give Claude more context. Claude can analyze text and visual elements (images, charts, graphics) in PDFs and documents. Supported file types: PDF, DOCX, CSV, TXT, and common image formats (PNG, JPEG).
Practical uses: summarize a document; describe/analyze an image; identify trends in a spreadsheet; explain code or find bugs. Once uploaded, Claude parses the file; it appears as an attachment you can prompt about.
**Pro-tip:** For preferences in every response, go to Settings > General > 'What personal preferences should Claude consider?'

**Iterating on Claude's responses** — conversations are iterative. Chaining bite-sized prompts allows natural dialogue. If the first response isn't right:
- **Ask follow-up questions:** "Can you expand on the second point?" / "make it more concise?"
- **Provide feedback:** "the tone is too formal. Can you make it more conversational?"
- **Redirect or restart:** Steer back ("I was asking about X, not Y"). Worst case, restart in a new chat to refresh context.
**Pro tip:** Click the pencil icon on any of your messages to edit and resubmit—useful to refine rather than add a new message.

**Personalizing Claude** — two features that help Claude work better over time:
- **Memory** automatically saves key context from conversations (role, preferences, past decisions, working style) so you don't repeat yourself. Review/edit/delete anytime in Settings; syncs across devices.
- **Styles** let you customize how Claude communicates. Choose presets (concise, formal, explanatory) or create a custom style. Applies across all conversations automatically.

**Put it into practice:** Try prompting Claude with a question or task (use-case gallery for ideas).

**What's next:** Next lesson — give Claude direction: adjusting tone, format, and approach.

---

## Lesson 3 — Getting better results (Section: Meet Claude)

**Estimated time:** 15 minutes

**Learning objectives:**
- Recognize common challenges when starting out with AI and use troubleshooting techniques
- Define AI Fluency and know where to learn more
- Explain how you might set up evals to understand how Claude performs with your unique workflows

**Common challenges and how to fix them** (Challenge → What's happening → Try this):
- **Response too generic** → prompt lacked context → Add details about audience, role, constraints. Instead of "Write an email about the project delay," try "Write an email to our enterprise client explaining that the software integration will be delayed by two weeks. They've been patient so far but this is the second delay. Keep it professional but apologetic."
- **Response too long (or too short)** → Claude is guessing at length → Be explicit: "Give me a two-paragraph summary" / "Keep this under 100 words" / "I need a comprehensive analysis—length isn't a concern."
- **Claude didn't follow my format** → understood what, not how → Show, don't just tell. Provide an example of the format, or describe structure: "Use bullet points with bold headers for each section."
- **Got confident-sounding info that turned out wrong** → Claude occasionally generates plausible but incorrect information, especially with specific facts or niche topics → For high-stakes work, verify key facts independently. Ask Claude to cite sources or indicate confidence level. Enable web search to ground responses.
- **Tone isn't right** → Claude defaults to helpful and professional → Describe tone in plain language ("more conversational" / "authoritative and formal"). Provide an example of the style you want.

**The iteration mindset:** Your first prompt rarely produces a perfect result—and that's okay. Treat the initial prompt as the start of a conversation. Effective users:
- Treat first drafts as starting points. Review, identify what's working, refine.
- Give specific feedback. "Make it shorter" is fine, but "Cut the first two paragraphs and make the conclusion more action-oriented" is better.
- Know when to start fresh. Sometimes a new chat with a clearer prompt is faster than redirecting.

**What is AI Fluency?** The ability to collaborate effectively with AI tools—not just which buttons to click, but the judgment to use AI well across situations. The **4D Framework** (Profs. Rick Dakan & Joseph Feller) identifies four core competencies:
- **Delegation:** Deciding what work should be done by humans, what by AI, and how to distribute tasks. Includes understanding your goals, AI capabilities, and making strategic choices.
- **Description:** Effectively communicating with AI systems. Clearly defining outputs, guiding AI processes, specifying desired behaviors/interactions.
- **Discernment:** Thoughtfully and critically evaluating AI outputs, processes, behaviors, interactions. Assessing quality, accuracy, appropriateness; determining improvements.
- **Diligence:** Using AI responsibly and ethically. Thoughtful choices, transparency, accountability for AI-assisted work.

(The Lesson 2 prompt framework is rooted in Description; troubleshooting techniques draw on Discernment and Diligence. Free AI Fluency course available.)

**Evaluating Claude for your workflows** — As you integrate Claude, ask: how do I know if Claude is good at this task? This is where Discernment matters. **Evals** (evaluations) are systematic ways to test how well Claude performs on specific tasks that matter to you.

**Why evals matter:** Your work is unique. Claude might excel at marketing copy but need more guidance for technical documentation in your domain. Running simple evals helps you understand where Claude adds most value, identify tasks needing more context/examples, and build confidence for recurring tasks.

**A simple eval approach:**
1. **Gather examples.** Collect 5–10 examples of a task you do regularly (emails, reports, analyses).
2. **Create test prompts.** Write prompts that would generate similar outputs, including natural context.
3. **Compare outputs.** Run prompts and compare to your examples. Ask: Does Claude capture key information? Is tone/style appropriate? What's missing or could improve?
4. **Refine your approach.** Adjust prompts, add examples to show what good looks like, or identify where human review is essential.

**Example: Using Claude for data analysis** (example from the AI Fluency for nonprofits course, relevant to anyone working with data): Find a dataset you've manually analyzed → create prompts requesting Claude to do the analysis → compare Claude's results to your originals → note patterns and refine (maybe Claude gets the right numbers but misses overall patterns).

**Lesson reflection:** Which common challenges have you encountered? Where would a simple eval help? How might the 4D Framework help your collaboration?

**What's next:** Next lesson — the Claude desktop app and its three interaction modes: Chat, Cowork, and Code.

---

## Lesson 4 — Claude desktop app: Chat, Cowork, Code (Section: Meet Claude)

**Estimated time:** 6 minutes

**Learning objectives:**
- Identify the three modes in the Claude desktop app — Chat, Cowork, and Code — and what each is designed for
- Explain key features unique to each mode, including quick entry, scheduled tasks, and local vs. remote development
- Choose the right mode based on the type of work you need to accomplish

**Overview:** The Claude desktop app gives three ways to work: **Chat, Cowork, Code** — from quick questions to complex research to building software.
- **Chat** is the same Claude from claude.ai, plus quick entry, screenshots, dictation, and connectors that come from running natively on your computer.
- **Cowork** is an agentic tool — you give it a goal, connect it to your tools/resources, and let it do the work. Broader scope: more thorough research and analysis, more complex documents and deliverables.
- **Code** is for building software — writing, testing, deploying code.
- **Cowork and Code run on the same engine.** Both are Claude Code underneath — local to your machine, capable of independent work, able to spin up sub-agents and sustain long tasks.

**Chat** — excels when you need to ask questions, brainstorm, draft, or work through problems back and forth. Same as claude.ai, plus native features:
- **Quick entry.** Double-tap the Option key on Mac to pull up Claude over whatever you're working on. Compact window stays on top as you switch apps.
- **Screenshots and window sharing.** Capture a screenshot or share a window so Claude sees exactly what you're looking at. (Mac)
- **Dictation.** Talk through a problem instead of typing. (Mac)
- **Desktop connectors.** Connect local tools and services so Claude can work with other tools on your machine.
Try it when: staring at an unfamiliar dashboard (screenshot + "what do these metrics mean?"); between meetings structuring a presentation via voice; pulling together notes across Apple Notes via the Notes connector.

**Cowork** — built for work that takes real effort: pulling information from many sources, making sense of it, producing something finished. Can multitask across different parts of a project. Examples: thorough research briefs, cross-source financial analysis, end-to-end contract review, polished slide decks. Before starting, Claude often asks a short set of questions (scope, format, constraints) and builds a plan you can review in the sidebar. Run multiple tasks at once, each in its own conversation.
- **Folder access.** Point Claude to a folder; it reads what's there, figures out what's relevant, saves finished work back. Can also upload files, paste content, or connect tools.
- **Scheduled tasks.** Recurring work on a schedule (daily briefing from Slack + calendar, weekly roundup, morning inbox triage). You define the task and when it runs; Claude handles it automatically each time the app is open. Catches up if computer/app was closed when due.
- **Subagents.** Background workers Claude spins up to handle parts of a task in parallel. Claude breaks a complex task into subtasks, assigns each to a subagent with its own context, coordinates results into one deliverable.
- **Dispatch.** A persistent conversation thread to continue Cowork conversations from your phone (Claude mobile app). Hand Claude tasks that use everything on your computer. Requires both desktop and mobile apps, computer awake, desktop app open.
- **Projects.** Group related tasks into dedicated workspaces with their own files, context, instructions, and memory. Like Claude projects, but they live locally on your desktop, built around tasks you run through Cowork.
- **Browser use.** Connect Claude in Chrome; Claude can navigate websites, interact with pages, pull findings into the task (e.g., check competitor pricing across ten sites).
- **Computer use.** When no connector/plugin exists, Claude can navigate your computer directly — clicking, typing, opening apps. Priority order: connectors first, then Chrome, then screen interaction. Permission prompt before accessing each app; you can set a blocklist. In research preview on Pro and Max plans, macOS only (Windows coming soon).
- **Plugins.** Capabilities Claude doesn't have on its own (live financial data, internal knowledge base search, compliance frameworks). Browse and add from the Cowork interface.
- **Protected environment.** Cowork runs in a contained space; Claude can read/create/edit files within shared folders, but can't access anything outside them.
Cowork is available to Pro, Max, Team, and Enterprise users.

**Code** — access to the power of Claude Code running inside the desktop app; a full development environment. Claude works directly in your codebase: reading, writing, modifying code, running commands. Visual diffs show changes, a built-in terminal shows commands, and git tracks every version for rollback. Where Cowork runs in a contained workspace, Code runs directly in your project with full access to file system, terminal, dev tools.
Where work happens:
- **Local:** Select a folder; Claude works directly with those files, accesses local tools, can run a dev server you preview in your browser.
- **Remote:** Connect a GitHub repo; Claude works in a cloud environment. Sessions continue even if you close the app. Good for larger codebases or keeping development off your local machine.
Three interaction modes (control how much Claude does on its own):
- **Ask:** Claude proposes every change and waits for approval (review a visual diff, accept/reject).
- **Code:** Claude applies file changes automatically but checks before running terminal commands.
- **Plan:** Claude outlines its full approach before touching anything; a plan viewer lets you review.
Run multiple sessions across projects; filter by status (Active/Archived) and environment (Local/Cloud). The Code tab is available on Pro, Max, Team, and Enterprise users.

**Comparing the three modes:**
| | Chat | Cowork | Code |
|---|---|---|---|
| **Optimized for** | Quicker exchanges: exploring ideas, iterative drafting, quick answers, learning through dialogue | Complex or sustained work: research, analysis, file organization, producing finished documents/deliverables | Building software: writing, testing, running, deploying code |
| **Key features** | Quick entry, dictation | Work from local folders, plugins, subagents, scheduled tasks | Ask/Code/Plan modes, visual diffs, git integration, local and remote environments |
| **Tools and extensions** | Connectors, Skills, Claude in Chrome | Connectors (local and remote), Skills, Claude in Chrome, Plugins, Computer Use | Connectors, Skills, Claude in Chrome, Plugins, Hooks |

**Lesson reflection:** Which mode fits the tasks you most commonly use Claude for? How might Cowork have changed a recent multi-source project?

**What's next:** Next module — organize your work and knowledge using Projects.

---

## Lesson 5 — Introduction to projects (Section: Organizing your work and knowledge)

**Estimated time:** 20 minutes
**Contains:** Video — "Introduction to Projects: Getting started with projects in Claude.ai" (key points captured in text below)

**Learning objectives:**
- Explain what projects are and when to use them
- Create a new project with a name, description, and visibility settings
- Add documents and files to your project's knowledge base
- Write effective project instructions to guide Claude's behavior
- Share projects with teammates (for Claude for Work — Team and Enterprise plan — users)

**Key takeaways:**
- **Projects are self-contained workspaces** with their own memory, chat histories, knowledge bases, and customized instructions — dedicated environments for specific work streams.
- **Project knowledge** enhances Claude's understanding by letting you upload relevant documents that Claude references across all chats within that project. No re-uploading the same files.
- **Project instructions** guide Claude's behavior — specify tone, expertise level, response style, and more. They apply to every conversation within the project.
- **Projects scale automatically.** When your knowledge base approaches context limits, Claude seamlessly enables **Retrieval Augmented Generation (RAG)** mode to expand capacity by up to **10x** while maintaining response quality.
- For Claude for Work users, projects enable collaboration — share with teammates for shared context, instructions, and accumulated knowledge.

**What are Projects?** Ideal for storing knowledge Claude should reference, organizing related chats around a topic/work area, and collaborating with team members needing the same shared context.

**When to use Projects** — valuable for ongoing work, not one-off questions. Create a project when you have a workflow with: reference materials you'll reuse (meeting notes, survey results, reports, historical data); consistent requirements for how Claude responds (always formal, always cite sources, always follow our template); team collaboration needs.

**Creating your first project:**
- **Step 1: Set up your project** — Hover the left sidebar, click "Projects" (or go to claude.ai/projects) → "+ New Project" (upper right) → give a descriptive name (e.g., "Q4 Marketing Campaign") → add a brief description (Claude doesn't see it directly; helps you/teammates understand purpose) → choose visibility (private or share with organization for Claude for Work).
- **Step 2: Add project instructions** — Click "Instructions." Good instructions include: context about what you're working on ("This project is for creating marketing content for our B2B software product."); process instructions ("First consider a blog structure that will entice this audience, then write the draft."); tone/style preferences ("Use a professional but conversational tone. Avoid jargon when possible."); specific requirements ("Always include a call-to-action at the end of marketing copy."). Click "Save instructions" — they apply to every chat and work alongside user preferences and styles. Can also automate workflows: "When I upload a meeting transcript, create a structured summary using this template." Think of instructions as programming Claude's behavior for this project.
- **Step 3: Build your knowledge base** — Files menu on the right side of the project's main page. Click "+" to add content. Upload PDF, DOCX, CSV, TXT, HTML, and more; can connect Google Drive. What to upload: reference docs (brand guidelines, style guides, templates), background materials (research reports, meeting notes, requirements docs), examples to emulate, technical docs/specifications. **Pro tip:** Name files descriptively — Claude uses file names to retrieve the right info ("Q4-2024-Brand-Guidelines.pdf" beats "document1.pdf").

**How projects handle large knowledge bases:** Projects automatically scale via **RAG**. Claude automatically finds and uses the most relevant parts of uploaded documents when answering, without you telling it which file. When project knowledge approaches the context window limit, Claude seamlessly enables RAG mode — instead of loading all content at once, it searches and retrieves only the most relevant info. Expands capacity by up to 10x while maintaining quality. You'll see a visual indicator when RAG-enabled, but the experience feels the same.

**Working within your project:** Each conversation automatically has access to your knowledge base and follows your project instructions.

**Collaboration features (Claude for Work — Team and Enterprise):**
- **Permission levels:** **Can view** (see contents, access knowledge, chat — no changes; read-only with discussion rights); **Can edit** (modify instructions, update knowledge, manage members, contribute); **Owner** (control everything including who sees the project; share with specific people or whole org).
- **Sharing your project:** Open the project → click "Share project" (right of the project name) → add members by name/email or paste a list for bulk sharing (shows in their "Shared with you") → or share with "Everyone at [organization]" to make it discoverable in the Team tab. Members get email notifications; find shared projects in "Shared with me."

**Example projects to inspire you:** Q4 product launch (product specs, competitive analysis, messaging notes); Research support (competitive review, user research, customer feedback — synthesize sources, draft reports); Client account hub (brand guidelines, past deliverables, comms history — set instructions to match tone); Event planning workspace (venue contracts, speaker bios, attendee data — run-of-show, communications, post-event reports); Job description generator (past JDs, team charters, headcount docs).

**Best practices for projects:** Start focused, then expand. Keep knowledge base current (outdated docs → outdated responses). Write clear instructions (vague → inconsistent). Name documents descriptively and group related files (Claude uses filenames and proximity to understand relationships). Reference documents by name when asking ("Based on our Q3 report, what were the top customer concerns?").

**Lesson reflection:** What ongoing work could benefit from a dedicated project with persistent context? What documents will you re-upload/re-explain regularly? Any team projects that would benefit from shared knowledge and instructions?

**What's next:** Next lesson — create mini-apps with Artifacts. (More info: Anthropic Help Center.)

---

## Lesson 6 — Creating with artifacts (Section: Organizing your work and knowledge)

**Estimated time:** 20 minutes

**Learning objectives:**
- Explain what artifacts are and when Claude creates them
- Share artifacts with colleagues and publish them publicly
- Troubleshoot common artifact issues

**What are artifacts?** Standalone, interactive outputs Claude creates in a dedicated window alongside your conversation. Instead of a long block of code/text buried in chat, you see content rendered and ready to use — a working website, an interactive chart, or a downloadable document.

Claude automatically creates an artifact when content: is significant and self-contained (typically over 15 lines); is something you'll likely want to edit, iterate on, or reuse; represents complex content standing on its own; is content you'll reference or use later.

**Common artifact types:**
- **Documents** (markdown, plain text, Word, PDF, PowerPoint, Excel): text-heavy content to export/edit — meeting notes, reports, project plans, blog posts.
- **Code snippets:** working code in any language (Python, JavaScript, C++, and more). View, copy, or download.
- **HTML pages:** complete web pages (HTML, CSS, JavaScript in a single file) — landing pages, forms, interactive demos, prototypes.
- **SVG images:** scalable vector graphics for logos, icons, illustrations. Render directly in the artifact window.
- **Mermaid diagrams:** flowcharts, sequence diagrams, Gantt charts, org charts. Describe relationships and Claude creates a diagram to refine.
- **React components:** interactive UI elements with real functionality — calculators, dashboards, games, data visualizations. Include actual logic and respond to user input.

**Creating your first artifact:** Just describe what you want; Claude decides whether to present it as an artifact. Examples: "Create a flowchart showing our customer onboarding process" (Note: Claude may now generate visual diagrams like flowcharts as HTML using Imagine, in addition to code-based artifacts); "Build an interactive dashboard that lets me input monthly expenses and see a breakdown"; "Design a landing page for a productivity app with a hero section and feature list"; "Write a project brief template I can reuse." If Claude doesn't auto-create one, ask: "Create this as an artifact." When generated, it appears in a dedicated window to the right where you can: view different formats (toggle preview vs. underlying code), copy content, download files, view code.

**Sharing and publishing artifacts:**
- **Copy or download:** copy/download buttons in the lower right of the artifact window.
- **Share within your organization (Claude for Work):** Team/Enterprise users share internally; stays within your org, requires team authentication.
- **Publish publicly (Free, Pro, Max):** make accessible to anyone with the link. When you publish: only the selected version becomes public (chat stays private); anyone can view/interact without a Claude account; others can "remix" — open it in their own Claude conversation to modify and build on. To publish, click "Share"/"Publish" (upper right). Unpublish anytime by removing public access. Note: published artifacts are publicly accessible via link (no Claude account needed to view) but are not indexed by search engines (won't appear in Google).

**Tips for getting the most from artifacts:** Be specific ("Build a monthly budget tracker where I can input expenses by category, see a pie chart breakdown, and get a warning when I'm over budget" beats "Build a budget tracker"). Describe the end user (helps Claude make design choices). Iterate incrementally (one feature/change at a time). Request artifacts when needed ("Please create that as an artifact").

**Lesson reflection:** What recurring work could benefit from a reusable interactive artifact? Which processes would be clearer as a flowchart/diagram? What prototype or tool would help test an idea quickly?

**What's next:** Next lesson — Skills: reusable instruction sets that teach Claude specialized workflows.

---

## Lesson 7 — Working with skills (Section: Organizing your work and knowledge)

**Estimated time:** 15 minutes
**Plan availability note:** Skills are currently a feature preview for Pro, Max, Team, and Enterprise plans. Free plan users can read along to understand the concept and skip the hands-on steps.

**Learning objectives:**
- Explain what Skills are and how Claude uses them
- Identify Anthropic's built-in Skills for document creation
- Enable and manage Skills in your settings

**What are Skills?** Folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks — expertise packages that teach Claude how to complete specific tasks in a repeatable way. You've already seen Skills if you've used Claude to create Excel, PowerPoint, Word, or PDF files (those capabilities are powered by Skills behind the scenes). Custom Skills can codify entire repeatable workflows — a quarterly variance analysis methodology, a brand voice review process, a compliance checklist — so Claude follows the same rigorous steps every time.

**Types of Skills:**
- **Anthropic Skills:** created and maintained by Anthropic. Include enhanced document creation for Excel, Word, PowerPoint, PDF. Available to all paid users; Claude invokes them automatically when relevant.
- **Custom Skills:** ones you or your organization create for specialized workflows and domain-specific tasks (e.g., apply company brand guidelines to presentations, structure meeting notes in a specific format, execute your org's data analysis workflows).

**Enabling Skills:** Feature preview for Pro, Max, Team, Enterprise. Requires Code execution and file creation enabled (Skills need Claude's secure sandboxed computing environment). Steps: Settings > Capabilities → ensure Code execution and file creation is on → scroll to Skills → toggle individual skills on/off. For Enterprise, org Owners must first enable Code execution and Skills in Admin settings. For Team plans, the preview is enabled by default at the org level. Once enabled, available Skills appear in settings (Anthropic built-in + any custom uploaded).

**Using Skills in practice:** You typically don't need to think about them — Claude handles skill selection automatically. Example prompts that invoke Skills: "Create an Excel spreadsheet tracking monthly expenses with formulas for totals"; "Turn this meeting notes document into a PowerPoint presentation"; "Generate a PDF report summarizing this data"; "Build a financial model in Excel with scenario analysis." When Claude uses a Skill, you'll see it in Claude's chain of thought; the output is a downloadable file (save to computer or Google Drive).

**File execution:** Claude can work with your actual files (within a contained environment) to create updated versions (note: in Chat, Claude creates a new version of the document rather than editing the original in place). Upload slides, spreadsheets, contracts (.xlsx, .pptx, .docx, .pdf) and Claude creates slides, performs analyses, adds suggested edits. Download or open in Drive. Note: to use these capabilities you'll need to give Claude access to external data sources — toggle **Allow limited network access** on when prompted.

**Security considerations:** Skills can include executable code, so use thoughtfully: only install custom Skills from trusted sources; Anthropic's built-in Skills are tested and maintained by Anthropic; custom Skills you upload are private to your individual account; if installing a custom Skill from an external source, review its contents before use.

**Creating custom skills:** The real power comes from creating your own. Easiest way is through conversation with Claude (no code/manual file creation needed). Steps: Start a new chat and tell Claude what to create ("I want to create a skill for writing quarterly business reviews"); answer Claude's interview questions (what should this skill do? what makes good output? examples of when you'd use it?); upload reference materials (templates, style guides, brand assets, examples); save your skill (Claude generates a properly structured file). See your skills via the **Customize tab** in the left sidebar — view all available skills and edit them manually or by chatting. Your custom Skill appears alongside Anthropic's built-in Skills; Claude auto-invokes it for relevant tasks. Improve with iteration — ask Claude to edit a skill and it updates the files.

**Skills vs. Projects** — "projects store knowledge, skills perform tasks." Projects are knowledge hubs (reference materials Claude needs — project specs, meeting notes, research docs; drawn on across every conversation in the project). Skills are procedural machines (encode how Claude executes a task — steps, order of operations, methodology, run consistently every time). They complement each other: a skill can reference knowledge stored in a project (a "customer call prep" skill pulls from customer profiles in a project's knowledge base). Project = the *what* (information); skill = the *how* (process).

| | Projects | Skills |
|---|---|---|
| **Purpose** | Store knowledge Claude references | Define processes Claude executes |
| **Best for** | Long-term context, reference materials, team collaboration | Repeatable workflows, multi-step tasks, consistent methodology |
| **Example** | Customer hub, research buddy, feedback generator | Process guidelines (brand or legal), blog drafting, PDF creation |
| **Persistence** | Knowledge available across all chats in the project | Instructions applied when the skill is invoked |

**Lesson reflection:** What documents do you create regularly that could benefit from built-in Skills? Any repetitive workflows that are good candidates for custom Skills? How might Skills change how you think about document creation and data analysis?

**What's next:** Next set of lessons — expand Claude's reach with connectors. (More info: Anthropic Help Center.)

---

## Lesson 8 — Connecting your tools (Section: Expanding Claude's reach)

**Estimated time:** 20 minutes

**Learning objectives:**
- Explain what connectors are and why they matter for your work with Claude
- Navigate the connectors directory and set up your first connection
- Use connected tools effectively in your conversations with Claude

**Key takeaways:**
- **Connectors transform Claude from an assistant into an informed collaborator** by giving Claude access to the same tools, data, and context you use every day. Claude works directly with your actual information instead of starting from scratch.
- **Connectors allow Claude to read information and perform actions on your behalf.** Depending on connector and permissions, Claude can search files, retrieve documents, analyze data, create content, update records, and execute tasks across connected applications.
- **The Model Context Protocol (MCP) powers connectors.** Think of MCP like **USB-C for AI** — a universal standard that lets Claude connect to many applications through a single consistent interface. This open standard means developers can build connectors for any tool, and they work seamlessly with Claude.
- **Two types of connectors:** **web connectors** (link Claude to cloud services like Google Drive, Notion, Slack, Asana) and **desktop extensions** (run locally on your computer through the Claude Desktop app, giving Claude access to local files and native applications).

**Finding and connecting tools:** Anthropic maintains a directory at **claude.ai/directory**, organized into two tabs: **Web** (cloud services — Gmail, Notion, Slack, Asana, Linear, Stripe, and more) and **Desktop extensions** (local tools via the Claude Desktop app). You can also click the **+** button (lower left of the chat window) → **Connectors**.

**Setting up a web connector:** Find the connector (claude.ai/directory, or + > Connectors in any chat) → click **Connect** → **Authenticate** (redirected to the service's login; sign in with existing credentials) → **Grant permissions** (review the specific permissions Claude requests, then authorize) → **Test the connection** ("Can you access my [tool name]?"). Once connected, Claude can search, read, and in some cases take actions within that service depending on granted permissions.

**Desktop extensions:** Require the Claude Desktop app rather than the web interface. Let Claude interact with local applications, your file system, and native features on macOS/Windows. Examples: local file access for reading/organizing documents; browser control for automated web tasks; native application integration (like Figma for design work). To install: download and install the Claude Desktop app → Settings > Extensions → browse and click Install → follow extension-specific setup.

**Using connectors in your work** (examples by category):
- **Project management (Asana, Linear, Jira):** "What are my highest priority tasks due this week?"; "Create a new task for reviewing the Q4 budget proposal"; "Summarize the status of our product launch project."
- **Communication (Slack, Gmail):** "Find the email thread where we discussed the vendor contract"; "Draft a reply to the latest message in the #marketing channel"; "What did the team decide about the timeline in yesterday's discussion?"
- **Documentation (Notion, Google Drive, Confluence):** "Search our documentation for our brand voice guidelines"; "Summarize the meeting notes from last week's product review"; "What does our style guide say about using contractions?"
- **Business tools (Stripe, PayPal, Salesforce):** "Show me revenue trends for the past quarter"; "What's the status of the Acme Corp opportunity?"; "List recent transactions over $1,000."

**Security and permissions:**
- **Scoped access:** Permissions are specific to what the connector needs; toggle individual permissions on/off within each application's menu.
- **Claude sees what you see:** Claude can only access data you have access to. Connecting your work email doesn't give Claude access to your CEO's inbox — only your own.
- **Revocable at any time:** Disconnect through Claude's settings or the third-party service's security settings. As with Skills, you can find or build custom connectors — exercise the same caution; only install from trusted sources.

**Lesson reflection:** Which daily work tools would be most valuable to connect? What tasks currently require copy/paste that connectors could automate? Where would combining data from multiple connected sources save time?

**What's next:** Next lesson — Enterprise Search (for Claude for Work users; connects Claude to your org's knowledge with custom prompts). (More info: Anthropic Help Center, claude.ai/directory.)

---

## Lesson 9 — Enterprise search (Section: Expanding Claude's reach)

**Estimated time:** 15 minutes
**Plan availability note:** Enterprise Search is available on Team and Enterprise plans and must be enabled by a workspace admin. Free/Pro/Max users can skip this lesson.

**Learning objectives:**
- Explain what Enterprise Search is and the types of questions it can answer
- Understand how the setup process works for both admins and users
- Recognize how security and permissions protect organizational data

**What is Enterprise Search?** Adds a dedicated **"Ask {Your Org Name}"** option to your sidebar — designed for finding and synthesizing knowledge buried across your company's tools and data sources. Think of it as a **pre-built Project for your entire organization** — your company's knowledge base is already loaded. Unlike regular chats with connectors, Enterprise Search is specifically designed for information gathering, using custom instructions configured by the Anthropic team.

**What can you ask?** Valuable for questions spanning multiple sources or requiring synthesis across your org:
- **Getting up to speed:** "What happened yesterday while I was out?"; "Summarize key updates across the business from the last week"; "What are the current blockers on the Platform project?"
- **Policy and process:** "What is our company's remote work policy?"; "How do I submit an expense report?"; "What's the process for requesting time off?"
- **Research and analysis:** "What are the main reasons customers cite for choosing competitors?"; "Summarize discussions about the Q4 product roadmap"; "Find information about our customer onboarding process."
- **Onboarding new team members:** "How does our authentication system work?"; "Who should I talk to about learning the billing system?"; "What tools does the engineering team use for deployment?"
- **Performance and project tracking:** "Find discussions and documents related to the marketing campaign"; "What were the key decisions from last week's leadership meetings?"; "Summarize team contributions to the Infrastructure initiative."

When you ask, Claude searches across connected tools (SharePoint documents, Slack conversations, Gmail threads, Google Drive files) and synthesizes a unified response — always citing sources for full context.

**Setting up Enterprise Search** — two-step process: admin configures for the org, then individual users authenticate with their personal accounts.
- **For admins (Owners):** Enabled by default for all Team/Enterprise orgs, but an Owner completes initial setup. Click "Ask Your Org" in the left sidebar → "Set up for your org" (or "Disable") → connect your org's tools (required: a connector for **Documents** like Google Drive or SharePoint, and **Chat** like Slack or Microsoft Teams; Email recommended but optional) → "+ Add more" for additional tools → customize the project name (appears as "Ask [Name]" in everyone's sidebar) → add a description → "Finish set up." Once complete, available to all members.
- **For users:** After admin setup, you'll see the "Ask {Org Name}" project starred in your sidebar. Click the project → follow guided onboarding to connect recommended services → authenticate with each service (Slack, Google, Microsoft 365, etc.) → start asking questions. The more connectors enabled, the more comprehensive your results. Add more later via "Connect" in the project's Instructions section.

**Is this safe?** Yes. Enterprise Search only shows what you already have permission to access in the original connected tool. Conversations remain private, and your connected data isn't indexed or stored separately.

**Lesson reflection:** What questions do you frequently ask colleagues that could be answered by searching org documents/communications? Any onboarding/training scenarios where it helps new members? Which data sources are most valuable for your role?

**What's next:** Next lesson — Research mode for deep, multi-step investigations. (More info: Anthropic Help Center.)

---

## Lesson 10 — Research mode for deep dives (Section: Expanding Claude's reach)

**Estimated time:** 15 minutes

**Learning objectives:**
- Explain what Research does: systematic, multi-source investigation
- Identify when to use Research for comprehensive information gathering
- Understand how Research works with extended thinking to deliver thorough reports
- Write effective Research prompts for complex investigations

**Key takeaways:**
- **Research transforms how Claude finds and analyzes information.** Instead of a single search, Claude operates **agentically** — conducting multiple searches that build on each other while determining what to investigate next. It explores different angles automatically and works through open questions systematically.
- **Research delivers comprehensive answers in minutes.** Most reports complete in **5 to 15 minutes**, though complex investigations may take up to **45 minutes** — work that would typically require hours of manual research.
- **Extended thinking is automatically enabled with Research.** This lets Claude both plan its approach thoughtfully and gather comprehensive information, breaking complex requests into manageable pieces.
- **Citations make verification easy.** Research delivers thorough answers complete with easy-to-check citations.

**What is Research?** An advanced feature that transforms Claude from a conversational assistant into a systematic investigator. When enabled, Claude explores your question from multiple angles, synthesizing information from across the web and your connected integrations. Like a skilled research assistant who spends hours gathering, cross-referencing, and compiling a report — in minutes. Valuable when you need more than a quick answer: pulling together multiple sources, comparing perspectives, synthesizing into actionable insights.

**When to use Research:**
- **Use Research when you need:** comprehensive reports synthesizing multiple sources; in-depth analysis across the web and connected integrations (like Google Workspace); thorough investigations that would take hours manually; comparative analysis (competitors, vendor options); reports with verifiable citations. Ideal for: market analysis and competitive research; planning complex projects (team offsites, product launches); synthesizing email/calendar/documents; technical documentation from multiple sources; briefings requiring current, verified info.
- **Consider web search instead when:** you need a quick specific fact (today's stock price, a company's address); the answer needs only one or two sources; speed matters more than comprehensiveness.
- **Consider extended thinking instead when:** you need deep reasoning on a complex problem that doesn't require external info; math problems, code debugging, logical analysis; the answer comes from reasoning rather than gathering information.
- **Consider enterprise search instead when:** answers draw from your org's internal knowledge (documents, Slack threads, emails, meeting notes); onboarding and finding how your company handles something; questions specific to your company, not the public web.

**How Research works** — an agentic, multi-step process beyond a simple web search. Claude autonomously decides what to search next based on what it found, pursuing leads and filling gaps without directing each step.
- **Step 1: Claude plans its approach.** Extended thinking automatically activates — break down the request, identify needed info, plan how to investigate different angles.
- **Step 2: Claude conducts multiple searches.** Many searches that build on each other; determines what to investigate next based on findings.
- **Step 3: Claude synthesizes findings.** After gathering from multiple sources (web + connected integrations like Gmail, Google Calendar, Google Drive), compiles a comprehensive, well-organized report.
- **Step 4: Claude provides citations.** Every claim links back to its source for easy verification.

**Using Research in practice:** Click the **+** button (bottom left of chat) → select **Research** (highlighted once active) → enter your prompt and submit → Claude works in the background with progress indicators. **Important:** Web search must be enabled for Research to function (turn on from the same + menu).

**Tips for effective Research prompts** (Research can take 5–45 min, so prompt crafting pays off):
- **Be specific about your goals.** Instead of "Tell me about the EV market," try "Analyze the electric vehicle battery market—identify key players, technology trends, and supply chain challenges that might affect investment decisions."
- **Specify the sections or structure you want.** E.g., "Compare venue options for a team offsite including: location and accessibility, meeting space and amenities, catering options, and pricing considerations."
- **Include relevant constraints.** Budget ranges, timelines, geographic requirements help Claude focus.
- **Ask Claude to help refine your prompt** before enabling the feature.

**Working with connected integrations:** With Google Workspace or other integrations connected, Claude can pull context from emails, calendar, and documents alongside web research. Examples: "Summarize what's been discussed about Project X across my emails and Slack, then research industry best practices for similar initiatives"; "Review my calendar commitments for next week and research each company I'm meeting with"; "Find all internal documents about our pricing strategy and compare to how competitors are positioning themselves." Steer Claude with "Pull relevant context from my Google Drive" or "Include insights from my recent emails on this topic." **Pro tip:** Turn off web search to do internal-only research across connected tools ("What did our team discuss about the Q3 launch across Slack and Docs?").

**Lesson reflection:** What research tasks typically require gathering from multiple sources? How might combining Research with connected integrations change your workflow? What complex question have you been putting off because it would take too much research time?

**What's next:** Next section — putting it all together: real-world use cases by role, and additional ways to interact with Claude. (More info: Anthropic Help Center.)

---

## Lesson 11 — Claude in action: use-cases by role (Section: Putting it all together)

**Estimated time:** 10 minutes

**Learning objectives:**
- Describe 2-3 use-cases for claude.ai that you can try right away
- Know where to go to find additional use-case inspiration

**Intro:** No matter what you do, Claude can help streamline your work. This lesson highlights practical use cases organized by role. Each use case links to a detailed guide in the **Use Case Gallery** with step-by-step instructions.

**General professional use** (apply across many roles/industries):
- Generate project status reports – keep stakeholders informed with clear, consistent updates
- Analyze patterns in user feedback – extract insights from customer comments and survey responses
- Package your brand guidelines in a skill – create a reusable Claude skill that applies your brand standards

**Sales** (accelerate deal prep, create materials, competitive intelligence):
- Build a battle card library – competitive intelligence resources to win deals
- Prepare for sales deals – research prospects and organize talking points
- Create sales reports – turn pipeline data into clear, actionable reports

**Marketing** (analyze performance data, repurpose content):
- Analyze campaign performance – extract insights from campaign metrics
- Adapt content across platforms – repurpose content for different channels/audiences

**Finance** (build models, draft documents, make sense of spreadsheets):
- Build financial models – create and refine financial projections
- Draft investment memos – structure and write investment analyses
- Understand and extend an inherited spreadsheet – decode complex spreadsheets and add functionality

**HR** (onboarding experiences and documentation):
- Create new hire onboarding guides – comprehensive materials tailored to different roles

**Legal** (track timelines, manage discovery):
- Track discovery timelines and analyze patterns – organize case timelines, identify key patterns

**Research** (plan literature reviews, verify data analysis):
- Plan your literature review – organize your approach to reviewing academic sources
- Verify statistics from raw data – double-check calculations and statistical analyses

**Explore more:** Visit the Use Case Gallery for the full collection.

**What's next:** Final module — more versions of Claude (Claude Code, Claude in Chrome, Claude in Excel, Claude in Slack).

---

## Lesson 12 — Other ways to work with Claude (Section: Putting it all together)

**Estimated time:** 10 minutes

**Learning objectives:**
- Understand when to use additional Claude products including Claude Code, Claude for Slack, Claude for Excel, Claude for PowerPoint, and Claude for Chrome

**Intro:** Claude is an intelligence; claude.ai is just one way of working with it. Claude is also available in specialized tools designed to meet you where you already work. This lesson introduces five additional ways.

**Claude Code** — an agentic coding tool that works where you work (terminal, IDE, browser, or Slack). Understands your codebase, executes commands, handles entire development workflows through natural language.
When to use: build features by describing what you need in plain English (Claude writes code, runs tests, creates commits); debug by pasting error messages; navigate an unfamiliar codebase by asking how parts work together; automate tedious tasks (fixing lint errors, resolving merge conflicts, writing release notes); work in your terminal alongside existing IDE/dev tools.

**Claude in Slack** — integrates directly with Slack; get help in channels/threads or bring Slack context into Claude conversations.
When to use: draft responses, summarize lengthy threads, break down complex discussions without leaving Slack; prepare for meetings by pulling together relevant conversations and shared documents; onboard to a new team by reviewing channel history; hand off coding tasks from a bug report/feature discussion (tag @Claude to spin up a Claude Code session using surrounding context); get quick answers about industry trends, technical concepts, or company info during a conversation.

**Claude for Excel** — brings Claude into Microsoft Excel through a sidebar to analyze, understand, and modify spreadsheets through conversation.
When to use: understand how formulas/calculation flows work across a complex multi-tab workbook; update assumptions/inputs while preserving formula dependencies; debug errors (#REF!, #VALUE!, circular references) by tracing to source and suggesting fixes; create new spreadsheets or populate templates while maintaining formula structure; quickly build pivot tables or charts.

**Claude for PowerPoint** — brings Claude into Microsoft PowerPoint as a sidebar to draft, edit, and restructure presentations through conversation while keeping your existing template and brand styling intact.
When to use: turn an outline/document/notes into a first-draft slide deck without building each slide by hand; rewrite or tighten slide copy (shorten bullets, add speaker notes, adjust tone); restructure an existing deck (reorder sections, split dense slides, merge overlapping ones); apply consistent formatting across the deck; get quick visual suggestions (which layout or chart type fits the point).

**Claude for Chrome** — a browser extension that adds Claude as a sidebar in Google Chrome; can observe what you're working on and take actions directly within your browser.
When to use: summarize articles/research papers/web pages while browsing; draft email responses or manage your inbox; automate repetitive forms; test website features or navigate multi-step workflows without manually clicking; a browsing assistant that maintains context across tabs (great for pulling context from niche internal tools, CRMs, dashboards).
**Important note:** Claude for Chrome is currently in **research preview**. Anthropic recommends using it for low-risk tasks on trusted websites. The extension asks permission before high-risk actions (purchasing, sharing personal data), and certain website categories (financial services, adult content) are blocked by default.

**Summary table:**
| Tool | Best for | Where it runs |
|---|---|---|
| Claude.ai | General tasks, research, writing, analysis, file creation | Web, desktop, and mobile apps |
| Claude Code | Software development, codebase navigation, git workflows | Terminal/command line, IDE, or your browser |
| Claude Cowork | Complex, multi-step tasks: research briefs, document creation, file organization, data analysis | Desktop (and mobile apps via Dispatch) |
| Claude/Claude Code in Slack | Team collaboration, meeting prep, quick answers in context | Slack workspace |
| Claude for Excel | Spreadsheet analysis, financial modeling, formula debugging | Microsoft Excel sidebar |
| Claude for PowerPoint | Slide creation, presentation editing, formatting and design | Microsoft PowerPoint sidebar |
| Claude for Chrome | Web research, email management, browser automation | Chrome browser sidebar |

**What's next:** Wrap up with a course recap and a quiz to earn your certificate of completion (shareable on LinkedIn and with your team).

---

## Lesson 13 — What's next? (Section: Conclusion & certificate)

**Estimated time:** 5 minutes

**Intro:** Congratulations on completing Claude 101! You've built a solid foundation for working with Claude effectively. Recap and resources for continued growth follow.

**What you've learned:**

*Getting started with Claude*
- Claude is an AI assistant built to be helpful, harmless, and honest—more than a chatbot, a thinking partner for complex work
- Access Claude through web, desktop, and mobile apps, with conversations syncing across devices
- Effective prompts set the stage (context), define the task (action), and specify rules (format and style)

*Getting better results*
- Iteration is key—treat first responses as starting points and refine through conversation
- Common challenges like generic responses or wrong tone can be fixed with more specific context
- AI Fluency encompasses four competencies: Delegation, Description, Discernment, and Diligence

*Organizing your work*
- Projects create dedicated workspaces with persistent knowledge, custom instructions, and team collaboration
- Artifacts are standalone outputs like documents, code, diagrams, and interactive tools that Claude creates alongside your conversation
- Skills are instruction packages that teach Claude specialized workflows—including built-in document creation and custom skills you can create

*Expanding Claude's reach*
- Connectors link Claude to your tools (Google Workspace, Slack, Notion, and many more) so it can work with your actual data
- Enterprise Search provides a dedicated project for searching across your organization's knowledge sources
- Research mode conducts systematic, multi-source investigations that would take hours to do manually

*Putting it all together*
- Claude applies across roles—sales, marketing, finance, HR, legal, research, and beyond
- Beyond claude.ai, you can work with Claude through Claude Code, Slack, Excel, and Chrome

**Additional resources:**
- *Learn more about AI and Claude:* AI Fluency courses (free); AI Capabilities and Limitations (free intro course); Use Case Gallery (step-by-step guides and prompts); Anthropic Help Center; Prompting documentation.
- *Product-specific resources:* Claude Code in Action (free course on dev workflows); Introduction to Claude Cowork (free course on the desktop companion for multi-step work); Connector Directory.

**A word of encouragement:** The most important thing now is to get started. Skills sharpen with practice. Start simple—pick one recurring task this week (drafting an email, summarizing meeting notes, analyzing a spreadsheet) and try it with Claude. Iterate. Claude is designed to be a collaborator, not a replacement—the best results come when you bring your expertise, context, and judgment. "You now have the foundation. The rest comes from doing the work."

---

## Lesson 14 — Certificate of completion (Section: Conclusion & certificate) [QUIZ]

**Type:** Quiz Lesson — "Claude 101 Certificate of Completion Quiz" — **13 questions**, behind a graded "Start" gate.

**SOURCE-GAP (intentional):** The 13 official certificate-quiz questions sit behind a graded submission gate that consumes the learner's attempt and records a result. They were deliberately NOT harvested — reproducing a graded certification answer key is out of scope and against the integrity of the assessment. The interactive HTML instead includes **fresh practice MCQs authored from the captured lesson content above** (fully source-grounded), so the learner gets self-assessment without diluting or republishing the official graded quiz. The learner should still take the real quiz on Academy to earn the shareable certificate.

---

## Capture Summary

- **Total lessons:** 14 (5 sections)
- **Text lessons captured in full:** 13/13 ✅
- **Quiz lesson:** 1 (Lesson 14) — existence recorded; questions intentionally not harvested (graded gate) — see SOURCE-GAP note above
- **Embedded videos:** Lessons 2 and 5 contain videos; their content is fully represented in the on-page text + Key Takeaways that Anthropic provides alongside each video. No text-only `SOURCE-GAP` for video.
- **Capture method:** authenticated Chrome session, lesson-by-lesson `get_page_text` extraction.
- **Fidelity note for conversion:** every claim in the HTML must trace to a lesson section above. No external facts to be introduced.



