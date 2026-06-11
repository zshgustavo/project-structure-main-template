# IDE Setup for AI Development

This project supports multiple IDEs. All read or can be pointed to root **`AGENTS.md`**.

## IDE matrix

| IDE | AI assistant | Config files |
|-----|--------------|--------------|
| **VS Code** | GitHub Copilot | `.github/copilot-instructions.md`, `.vscode/settings.json` |
| **Cursor** | Cursor Agent | `.cursor/rules/ai-project.mdc`, `AGENTS.md` |
| **PyCharm** | Copilot / Junie | `AGENTS.md` (paste or index as project context) |
| **IntelliJ** | Copilot / Junie | `AGENTS.md` |
| **Zed** | Built-in AI | `AGENTS.md` |
| **Antigravity** | Agent mode | `AGENTS.md` |
| **Grok CLI** | Grok | `.grok/skills/` |

## Recommended extensions (VS Code / Cursor)

Already in `.vscode/extensions.json`:

- EditorConfig
- GitHub Pull Requests
- Docker
- Terraform

Add for AI work:

- Python (ms-python.python)
- Pylance
- GitHub Copilot (if using Copilot)

## Python interpreter

Point to `apps/agent/.venv` after `uv sync`:

```bash
cd apps/agent && uv sync
```

## Grok skills (this project)

| Skill | Command | Purpose |
|-------|---------|---------|
| `run-crew` | `/run-crew` | Execute CrewAI |
| `run-evals` | `/run-evals` | Agent eval suite |
| `vertex-gcp` | `/vertex-gcp` | GCP / Vertex setup |

## Consistency rule

When you change AI conventions, update **all** of:

1. `AGENTS.md`
2. `.github/copilot-instructions.md`
3. `.cursor/rules/ai-project.mdc` (if Cursor-specific)
4. Wiki [Stack Decisions](https://github.com/zshgustavo/project-structure-main-template/wiki/Stack-Decisions)