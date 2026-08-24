# CCAO-F — Background Material Index

**Compiled:** 2026-08-19 · **Covers:** the four-to-five weeks to the sitting
**Rule:** every entry states where it came from. Nothing here is recalled from memory — each URL was
retrieved in the session that built this file, or is marked as needing sign-in.

Material is tiered by how much it decides the outcome. Tier 0 blocks everything. Tier 1 is the
syllabus. Tier 2 is the product surface, which is the real gap. Tier 3 is governance. Tier 4 is what
Ram already owns and should not rebuild.

---

## TIER 0 — Blocking. Nothing downstream is trustworthy without these.

| # | Item | Where | Status |
|---|---|---|---|
| 0.1 | **CCAO-F Exam Guide (PDF)** | Anthropic Academy → CCAO-F certification page → certifications page | ⛔ Needs Partner Network sign-in. **Do this first.** |
| 0.2 | Certification Terms and Conditions (PDF) | Same page | ⛔ Needs sign-in |
| 0.3 | Anthropic Certification Exam Policy (PDF) | Same page | ⛔ Needs sign-in |
| 0.4 | [Pearson VUE Anthropic program page](https://www.pearsonvue.com/us/en/anthropic.html) | Public | ✅ Retrieved 2026-08-19. Confirms exam code CCAO-F and the 4-attempts / 14-30-90-day retake policy |

Drop 0.1 into `sources/` and every ⚠️ in `EXAM-FACTS_v1.md` resolves in one pass.

---

## TIER 1 — The official syllabus (Anthropic Partner Academy)

**Prep path: "Claude Certified Associate – Foundations Prep Course" — 8 lessons, 389 min (~6.5 h).**
Retrieved from the Academy path page, 2026-08-19.

| # | Lesson | Min | Maps to blueprint domain |
|---|---|---|---|
| 1.1 | Claude Platform & Model Foundations | 59 | Product and Model Selection |
| 1.2 | Prompting & Task Execution | 53 | Prompting and Task Execution |
| 1.3 | Evaluating & Validating Claude's Output | 74 | Output Evaluation and Validation |
| 1.4 | Workflow Integration & Solution Design | 63 | Workflow Integration and Solution Design |
| 1.5 | Configuration & Knowledge Management | 47 | Configuration and Knowledge Management |
| 1.6 | Governance, Risk & Responsible Use | 55 | Governance, Risk and Responsible Use |
| 1.7 | Troubleshooting & Optimization | 30 | Troubleshooting and Optimisation |
| 1.8 | Course Summary & Next Steps | 8 | — |

**Stated prerequisite courses:** Claude 101 · AI Fluency: Framework & Foundations · AI Capabilities
and Limitations. All three were covered on the CCAR-F run — confirm rather than re-sit.

**Stated audience:** *"people already using AI-powered productivity tools in their work"* — operations,
marketing, project management, education, communications. **Stated purpose:** *"operate Claude with
professional discipline, turning everyday business problems into reliable Claude workflows you can
stand behind."*

> The lesson titles are load-bearing evidence here, not just a study plan. Six of the seven community
> domain names match them near-verbatim, and lesson minutes track the claimed weightings closely. The
> arithmetic is in `EXAM-FACTS_v1.md`.

---

## TIER 2 — Product surface. **This is the gap. Spend the most time here.**

Roughly 26% of the paper — Product/Model Selection (12%) plus Configuration and Knowledge Management
(12%), plus parts of Workflow Integration — is product-surface knowledge that the CCAR-F corpus does
not contain. It is the least demanding and most easily under-prepared material on the syllabus.

**Anthropic Help Centre** — `support.claude.com`. URLs retrieved 2026-08-19.

| Article | Why it matters |
|---|---|
| [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects) | Self-contained workspaces with their own chat history and knowledge base. Core Configuration/Knowledge content |
| [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) | The operational detail — the kind of thing an Associate item turns on |
| [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) | Custom instructions, styles, preferences |
| [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills) | Skills at product level, not SDK level |
| [Help Centre home](https://support.claude.com/en/) | Work the Claude collection systematically |

**Plan-tier facts are examinable and easy to lose marks on.** Examples confirmed from the Help Centre
on 2026-08-19: free accounts cap at five projects; enhanced project knowledge with RAG is paid plans
only (Pro, Max, Team, Enterprise) and expands capacity up to 10×; project instructions are paid-plan
only; project sharing requires Team or Enterprise. Build a plan-tier comparison table into the
Configuration domain file and drill it — this is exactly the flavour of detail that separates a 78%
from a 90% on a practitioner exam.

**Product docs** — note the domains moved: `platform.claude.com/docs` for the platform,
`code.claude.com/docs` for Claude Code. Both retrieved 2026-08-19. For CCAO-F, read the product and
model-selection pages; skip the API and SDK reference material, which is out of scope for a no-code
exam.

---

## TIER 3 — Governance, Risk and Responsible Use (15%)

Same underlying Anthropic material as the CCAR-P Tier 3, read one altitude lower: what a business
user must not do, and how an organisation keeps use responsible. URLs retrieved 2026-08-18 in the
CCAR-P session.

| Source | Note |
|---|---|
| Anthropic Usage Policy | Prohibited uses. Likely direct exam content |
| [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) | Read for vocabulary, not depth. An Associate item will not ask about ASL thresholds |
| [Transparency Hub / voluntary commitments](https://www.anthropic.com/transparency/voluntary-commitments) | Anthropic's stated obligations |
| Enterprise controls: SSO, SCIM, audit logs, role-based permissions | The admin-side answer to "how does an organisation govern this" |

Data handling — what is retained, what trains models, what an admin can see — belongs here too and is
better sourced from the Help Centre than the engineering blog.

---

## TIER 4 — Assets Ram already owns (do not rebuild)

| Asset | Location | Reuse |
|---|---|---|
| CCAR-F corpus D4 `_v2` (prompting) | `..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\` | Direct feed for Prompting and Task Execution (14%), **brought down a tier** — drop anything assuming API or SDK access |
| CCAR-F corpus D5 `_v2` (context/reliability) | Same folder | Partial feed for Troubleshooting and Optimisation (10%) |
| `EXAM-LOG.md` + `CCA-Orchestration-Prompt_v10.md` | Same folder | The mock-generation engine that produced 14 papers. Ported here as `CCAO-F-Orchestration-Prompt_v1.md` |
| Full 64-card miss corpus | `..\CCAR-F - ...\prep with quiz\CCA-Prep_Missed-Questions-Review_v1.html` | The habit-level errors carry over even though the syllabus does not |
| Eval Design Blueprint | `my blueprints\eval-blueprint\` | Output Evaluation and Validation (21%) — but this is written at architect altitude and needs heavy simplification for a desk-level exam |

---

## Community sources — read, never generate from

Both state, or are, independent resources unaffiliated with Anthropic. They are useful for shaping
reading order and nothing else.

| Source | Retrieved | Use |
|---|---|---|
| `claudecertificationguide.com/associate-foundations` | 2026-08-19 | The domain list and weightings in the UNVERIFIED table. Site states it is *"not affiliated with, endorsed by, or sponsored by Anthropic"* |
| `ravikirans.com` CCAO-F study guide | 2026-08-19 | Independent corroboration of the same weightings; attributes them to "the official CCAO-F blueprint" without linking it |

---

## Carry-over habits from the CCAR-F sitting

The six objectives that scored 0% on the real CCAR-F paper are all Claude Code, subagent and context
material — none of it is in CCAO-F scope. Nothing content-level carries over.

What does carry over is behavioural, from all 64 documented misses:

1. Reaching for a workaround beside a mechanism instead of a narrow adjustment to it.
2. Losing multiple-response items by being majority-right — all-or-nothing scoring cost eight marks.
3. Choosing an option because of how it *sounds* — safer, more architected, more thorough — rather
   than because it matches the requirement the scenario actually states.

Habit 3 is the dangerous one on this exam specifically. Sitting a tier below your own credential, the
architected-sounding answer will be a distractor more often than it will be correct.
