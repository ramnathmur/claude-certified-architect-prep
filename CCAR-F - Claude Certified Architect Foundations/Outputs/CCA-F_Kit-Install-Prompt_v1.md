# CCA-F Practice Test Kit — installer

**How to use this file:** open Claude Code with this folder as your working directory, then paste everything below the line into it. It sets the kit up and checks that it works. It takes about a minute and changes nothing outside this folder.

---

You are installing the CCA-F practice test kit on this machine. Work only inside the folder you were opened in. Do not download anything, and do not touch anything outside this folder.

## STEP 1 — Confirm what is here

List the current folder. You are expecting these three files beside this one:

- `2-GENERATE-TEST-PROMPT.md` — the generator
- `CCA-F_Generator-Corpus_v1.md` — the grounding corpus
- `README-FIRST.txt` — the plain-text summary

If either of the first two is missing, stop and tell the user which one, and that the zip needs re-extracting. Do not attempt to reconstruct a missing file or carry on without it.

Note the folder's absolute path. You will need it in Step 4.

## STEP 2 — Check the corpus is intact

Read `CCA-F_Generator-Corpus_v1.md` and count its numbered section headings — lines matching `## §N.M`.

- **Expected: exactly 73**, distributed 18 / 9 / 12 / 20 / 14 across domains 1 to 5.
- It should also contain seven `# Part` headings, numbered 0 through 6.

Report the counts you actually measured. If they do not match, say so plainly and stop — a truncated corpus produces confidently wrong questions, which is worse than no practice material.

## STEP 3 — Extract the renderer

`2-GENERATE-TEST-PROMPT.md` carries the complete HTML renderer inside it, between two markers. Pull it out into its own file so the generator does not have to extract it on every run.

If Python is available, this is the reliable way — it copies bytes rather than retyping them:

```python
import re
src = open("2-GENERATE-TEST-PROMPT.md", encoding="utf-8").read()
shell = re.search(r"<!-- SHELL-BEGIN -->\n(.*?)\n<!-- SHELL-END -->", src, re.S).group(1)
open("Test-Blank.html", "w", encoding="utf-8").write(shell)
print("renderer extracted:", len(shell), "bytes")
```

If Python is not available, read the block between `<!-- SHELL-BEGIN -->` and `<!-- SHELL-END -->` and write it out to `Test-Blank.html` yourself, exactly as it appears — no reformatting, no tidying, no omissions.

Then verify the result:

- It should be **between 36,000 and 39,000 bytes**. The exact figure varies because Windows may write line endings as two bytes rather than one — anything in that range is correct.
- It must contain `const DATA = `, `function initChrome`, and `function submitExam`.
- It must contain **no** references to `../Learning%20corpus` or `../README.html`. If it does, the extraction picked up the wrong region — stop and report it.

## STEP 4 — Register the `/cca-exam` command

Create `.claude/commands/cca-exam.md` inside this folder, so the generator can be launched by typing `/cca-exam`. Write exactly this, with `<KIT>` replaced by the absolute folder path from Step 1:

```markdown
---
description: Generate a new CCA-F practice test
---

Read this file in full and execute it as your operating instructions for this session:

`<KIT>\2-GENERATE-TEST-PROMPT.md`

The grounding corpus is at `<KIT>\CCA-F_Generator-Corpus_v1.md` and the blank renderer is already extracted at `<KIT>\Test-Blank.html` — use that file rather than re-extracting from the appendix. Write the finished test into `<KIT>\tests\`.

Begin at PHASE 0.

$ARGUMENTS
```

If `.claude/commands/cca-exam.md` already exists, show the user what is there and ask before replacing it.

## STEP 5 — Create the output folder

Create a `tests/` subfolder if it does not exist. Generated tests land there. Leave it alone if it already has files in it.

## STEP 6 — Self-test

Confirm each of these and report the measured value, not a claim:

1. `Test-Blank.html` exists, is between 36,000 and 39,000 bytes, and carries no `../Learning%20corpus` references.
2. `CCA-F_Generator-Corpus_v1.md` has 73 numbered sections.
3. `.claude/commands/cca-exam.md` exists and its path placeholders are filled in with the real folder path — no `<KIT>` left anywhere in it.
4. `tests/` exists.
5. Report whether Python is available (`python --version`). It is not required — it makes two helper steps faster, and you can do the same work with your own file tools if it is absent.

## STEP 7 — Tell the user where they stand

Report, briefly:

- What you created, with the folder path.
- The corpus section count you measured and the renderer size you measured.
- That they generate a test by **restarting Claude Code in this folder and typing `/cca-exam`** — the slash command is only picked up when Claude Code starts, so a restart is required before it appears.
- That a full test takes 20 to 40 minutes and writes 60 questions with 240 explanations, so it is worth starting when they have the session free.
- That the finished test is a single HTML file in `tests/` which opens in any browser with nothing installed and nothing sent anywhere.

Do not generate a test now. Installation only.
