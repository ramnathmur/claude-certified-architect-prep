---
description: Run the CCA-F mock-exam orchestrator (generate or score an exam)
argument-hint: (optional) paste the results JSON from a finished exam, or leave blank to generate
---

You are running the CCA-F mock-exam orchestration pipeline.

Read this file in full and execute it exactly as your operating instructions for this entire session:

`C:\Claude Cowork\Projects\Claude Certified Architect Prep\prep with quiz\CCA-Orchestration-Prompt_v7.md`

It is a self-contained 5-phase prompt. Follow every phase in order, honor all constraints, and run its self-verification checklist before closing. Begin now with Phase 1 (State Load) and emit the SESSION START block, then ask the routing question.

If the user passed a results JSON as an argument to this command, treat it as their answer to the routing question — go to Phase 2 (Score Entry) with it as FORMAT 0 input. Otherwise, ask whether they have results to report or want to generate the next exam, and wait.

$ARGUMENTS
