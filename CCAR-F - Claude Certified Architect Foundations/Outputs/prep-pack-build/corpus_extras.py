"""Student-facing index page + cleanup of author-facing matter in the corpus sources."""
import re


def clean(md):
    """Strip author-facing front matter and neutralise pointers to files that are not shipped."""
    out = []
    for ln in md.split('\n'):
        st = ln.strip()
        if re.match(r'^\*\*(Source|Version|Changelog)\b', st):
            continue
        out.append(ln)
    md = '\n'.join(out)
    # collapse the blank run left where the front matter was
    md = re.sub(r'(\A# [^\n]+\n)\n{2,}', r'\1\n', md)
    # markdown links to files we do not ship -> plain text
    md = re.sub(r'\[([^\]]+)\]\((?!https?:)[^)]*\.(?:md|py|pdf|txt|html)\)', r'\1', md)
    # in-text pointers to internal working files -> something a student can act on
    md = re.sub(r'See\s+`CURRENT-DOCS-DELTA_v1\.md`\s*§D\d+\.?',
                'Answer the exam with the official framing.', md)
    md = re.sub(r'`(CURRENT-DOCS-DELTA_v1|PRACTICE-TEST-STEMS_v1|QUESTION-ARCHETYPE-BANLIST|'
                r'SESSION-STATE|CCA-Prep_Corpus-Index_v\d|CCA-Prep_Exam-Mechanics_v\d|'
                r'CCA-Prep_Key-Distinctions_v\d)[^`]*`',
                'the project working notes', md)
    md = re.sub(r'`CCA-Prep_Domain-(\d)_v\d\.md`', r'domain \1 of this corpus', md)

    # One note in D3 is written to the question author, not the candidate. The underlying
    # fact is worth keeping; the instruction to the author is not.
    old_note_start = '> **⚠ Currency note — import depth is contested, do not key a question on it**'
    if old_note_start in md:
        start = md.index(old_note_start)
        end = md.index('\n\n', md.index('**Generator rule:**', start))
        md = md[:start] + STUDENT_CURRENCY_NOTE + md[end:]
    return md


STUDENT_CURRENCY_NOTE = """> **⚠ Import depth: the sources disagree, and the exam does not test the number.**
>
> - Community study guides say the maximum `@import` nesting depth is **5**.
> - Current Anthropic product documentation says **four hops**
>   (https://code.claude.com/docs/en/memory).
> - The official Exam Guide is **silent**. Task statement 3.1 names "the `@import` syntax for
>   referencing external files" and the appendix names "`@import` patterns"; neither gives a depth.
>
> Learn that imports nest and that the depth is bounded. Do not memorise the digit, and do not
> rule an option in or out because it says 4 rather than 5 — no exam item turns on it."""


INDEX_MD = """# The corpus

This is the source layer of the pack. The five pages above hold **73 numbered sections** covering
everything the exam tests, and they are what every other file here was written from.

## Why you would open it

Every answer explanation in the practice tests, and every card on the Trap Sheet, ends with a citation
like `§4.9`. That is a section number in this document. Those citations are live links: click one and it
opens the exact section, on the right page, with the full treatment behind the one-line explanation you
just read.

You do not read this front to back. You arrive here from a question you got wrong.

## What is on each page

| Page | Domain | Weight | Sections |
|---|---|---|---|
| D1 | Agentic Architecture & Orchestration | 27% | 18 |
| D2 | Tool Design & MCP Integration | 18% | 9 |
| D3 | Claude Code Configuration & Workflows | 20% | 12 |
| D4 | Prompt Engineering & Structured Output | 20% | 20 |
| D5 | Context Management & Reliability | 15% | 14 |

Section numbering matches the domain: `§3.7` is the seventh section of D3. Each page opens with a jump
list of its own sections, and the arrow keys move between pages.

## The six scenarios

Every exam question is framed inside one of six production scenarios, and a sitting draws four of them:
**Customer Support** · **Code Generation** · **Multi-Agent Research** · **Developer Productivity** ·
**Claude Code CI/CD** · **Structured Data Extraction**. The scenario changes the surface a trap hides on,
never the concept being tested.

## Where this comes from

Anthropic's official *Claude Certified Architect – Foundations Exam Guide* — its five domains, thirty task
statements, six scenarios and two scope lists — supported by Anthropic's product documentation for
mechanism-level depth.

> **On guide versions.** Most of this pack cites **v0.2 (30 June 2026)**, which is what it was authored
> against. Anthropic has since republished the guide as **v1.0 (effective July 2026)**, under the official
> exam code **CCAR-F**. A measured diff of the two found the domain weights, all six scenarios, all thirty
> task statements and both scope lists **identical**, so nothing you study here is stale. Where this
> material and current product documentation disagree on a detail, the exam follows the guide's framing —
> answer with that, and verify product behaviour against the live docs when you do the real work.
"""
