# Claude Code Skill Authoring Spec

A **skill** is a reusable, model-invoked capability packaged as a folder containing a
`SKILL.md` file. When its `description` matches the user's request (or the user types
`/skill-name`), Claude loads the skill body as instructions and follows them.

This document is the spec/standard for writing new skills. The companion `SKILL.md`
in this folder is a copy-paste starting template.

---

## 1. File layout

```
.claude/skills/
  my-skill-name/
    SKILL.md          # required — frontmatter + instructions
    reference.md      # optional — extra docs the skill can Read on demand
    scripts/          # optional — helper scripts the skill invokes
    templates/        # optional — files the skill copies or fills in
```

- The **folder name** should match the skill `name`.
- Discovery locations (highest precedence first):
  - Project: `<repo>/.claude/skills/`
  - User: `~/.claude/skills/` (Windows: `C:\Users\<you>\.claude\skills\`)
  - Plugin-provided skills (namespaced as `plugin:skill`)

---

## 2. Frontmatter (YAML)

| Field | Required | Purpose |
|-------|----------|---------|
| `name` | yes | Kebab-case identifier. Becomes the `/slash-command`. Match the folder name. |
| `description` | yes | The single most important field. WHAT + WHEN. This is all the model sees when deciding to load the skill. |
| `allowed-tools` | no | Comma-separated tool allowlist (e.g. `Read, Edit, Bash`). Omit to allow all tools. |
| `argument-hint` | no | Usage hint shown in the UI, e.g. `<pr-number>`. |

### Writing a good `description`
- Lead with the trigger: *"Use when the user wants to…"*.
- Name concrete tasks, file types, and phrasings the user is likely to say.
- Include when **not** to use it, if there's a cheaper default path.
- Keep it to 1–2 sentences. It's matched against intent, not keywords alone.

Good: `Deploy the web app to staging. Use when the user says "deploy", "ship to staging", or asks to push the current branch live. Not for production deploys.`

Weak: `Helps with deployment.`

---

## 3. Body (Markdown instructions)

The body is loaded into context **every time the skill runs**, so keep it lean.
Recommended sections (all optional, but this order reads well):

1. **When to use** — restate triggers and the non-use case.
2. **Inputs** — `$ARGUMENTS`, `$1`/`$2` positional args, expected files/state.
3. **Steps** — numbered, imperative. Each step says what to do, what "done" looks
   like, and which tool to prefer.
4. **Constraints** — hard rules ("never push without asking").
5. **Examples** — wrap representative runs in `<example>…</example>` tags.

### Arguments
- `$ARGUMENTS` expands to everything the user typed after the command.
- `$1`, `$2`, … expand to individual positional tokens.

### Progressive disclosure
Put bulky detail (long checklists, API references, large templates) in separate
files and tell the skill to `Read` them only when needed. This keeps the always-loaded
body small while still giving the skill depth on demand.

---

## 4. Design principles

- **One job per skill.** If a skill needs "and also…", split it.
- **Deterministic where it matters.** Spell out exact commands, file paths, and
  verification steps rather than leaving them to inference.
- **Always verify.** A skill that changes state must include a step that confirms the
  change (run tests, re-read the file, check output) before reporting success.
- **Fail loudly.** Tell the skill what to do when a precondition is missing (e.g.
  "if not in a git repo, stop and tell the user").
- **Match the codebase.** Instruct the skill to follow surrounding conventions, not
  impose new ones.

---

## 5. Authoring checklist

- [ ] Folder name matches `name`.
- [ ] `description` states WHAT and WHEN, with concrete triggers.
- [ ] Body is lean; bulky reference material is in separate Read-on-demand files.
- [ ] Steps are numbered and imperative, each with a clear "done" condition.
- [ ] A verification step exists for any state-changing skill.
- [ ] Constraints list the things the model must never do.
- [ ] At least one `<example>` showing a real invocation.
- [ ] `allowed-tools` set if the skill should be sandboxed to specific tools.
- [ ] Tested by invoking `/my-skill-name` and by a natural-language request that
      should trigger it.

---

## 6. Minimal example

```markdown
---
name: changelog-entry
description: Add an entry to CHANGELOG.md from the current staged changes. Use when the user asks to "update the changelog" or "add a changelog entry" before a release.
allowed-tools: Read, Edit, Bash
---

# Changelog Entry

## Steps
1. Run `git diff --staged --stat` to see what changed.
2. Read CHANGELOG.md; find the "Unreleased" section (create it if missing).
3. Add a bullet under the right category (Added / Changed / Fixed) summarizing the change.
4. Show the user the added line and confirm wording before finishing.

## Constraints
- Never edit released/version-tagged sections.
- If there are no staged changes, stop and tell the user.
```
