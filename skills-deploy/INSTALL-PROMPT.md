# Install: prompty + sync-up Claude Code skills

This folder was unzipped from `claude-skills-bundle.zip`. It contains two Claude
Code skill folders — `prompty/` and `sync-up/` — sitting right next to this
file. Install both as **user-level** skills on this machine.

Do the following:

1. Confirm this folder contains `prompty/SKILL.md` and `sync-up/SKILL.md`. If
   either is missing, stop and tell me.
2. Find (or create) my user-level skills directory: `~/.claude/skills`
   (resolve `~` for this OS — e.g. `$HOME/.claude/skills` on macOS/Linux,
   `%USERPROFILE%\.claude\skills` on Windows).
3. For each of `prompty` and `sync-up`:
   - If a folder with that name already exists at the destination, don't
     overwrite it silently — copy the new one in as `<name>-incoming`
     instead and tell me, so I can decide, rather than clobbering whatever
     is already there.
   - Otherwise, copy (don't move) the whole folder into the destination
     skills directory, keeping its full contents intact.
4. Verify the copy: list the destination skills directory and confirm
   `prompty/SKILL.md` and `sync-up/SKILL.md` both exist and are non-empty.
5. Tell me what got installed, where, and whether I need to restart Claude
   Code (or start a new session) for the two skills to show up.

Everything here is a local file copy — no network access needed, and the
original unzipped folder is left untouched as a backup.
