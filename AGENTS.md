# AGENTS.md — AI Coding Assistant Guide

> Instructions for AI assistants working in this repo: **Grok**, **GitHub Copilot**, **Claude**, **GPT**, and IDE agents in **VS Code**, **Cursor**, **PyCharm**, **IntelliJ**, **Zed**, and **Antigravity**.

**Stack:** CrewAI · Grok · GCP · Vertex AI · Gemini · Manus IM · Claude · GPT · Copilot

---

## Project overview

Monorepo template evolving into a **multi-agent AI application**:

| Path | Purpose |
|------|---------|
| `apps/agent/` | CrewAI crews — primary agent runtime |
| `apps/api/` | HTTP API (future — expose agent endpoints) |
| `prompts/` | System prompts and templates |
| `config/ai/` | Model routing, guardrails, provider config |
| `packages/tools/` | Shared tools for agents |
| `tests/evals/` | LLM/agent quality evaluation |
| `.grok/skills/` | Grok CLI project skills |
| `.cursor/rules/` | Cursor-specific rules |
| `infrastructure/gcp/` | Vertex AI / GCP deployment notes |
| `docs/ai/` | AI architecture and provider docs |

**Wiki (source of truth for ops):** [GitHub Wiki](https://github.com/zshgustavo/project-structure-main-template/wiki)

---

## Before writing CrewAI code

1. Check installed version: `cd apps/agent && uv run python -c "import crewai; print(crewai.__version__)"`
2. Check PyPI latest: `https://pypi.org/pypi/crewai/json`
3. Read live docs if API is uncertain: `https://docs.crewai.com/en/concepts/<feature>`
4. **Live docs win** over training data when they conflict

### CrewAI patterns to use

```python
from crewai import LLM, Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task

# LLM via LiteLLM string (multi-provider)
llm = LLM(model="openai/gpt-4o")
llm = LLM(model="gemini/gemini-2.0-flash")
llm = LLM(model="vertex_ai/gemini-2.0-flash")
llm = LLM(model="anthropic/claude-sonnet-4-20250514")
```

### Patterns to NEVER use

- `ChatOpenAI(model_name=...)` → use `crewai.LLM`
- Raw OpenAI client objects → use `crewai.LLM` wrapper
- Hardcoded API keys in source → use `.env`

---

## LLM provider routing

Configured in `config/ai/models.json` and `config/ai/routing.json`.

| Provider | Env vars | CrewAI model string |
|----------|----------|---------------------|
| **OpenAI / GPT** | `OPENAI_API_KEY` | `openai/gpt-4o` |
| **Anthropic / Claude** | `ANTHROPIC_API_KEY` | `anthropic/claude-sonnet-4-20250514` |
| **Google Gemini** | `GOOGLE_API_KEY` | `gemini/gemini-2.0-flash` |
| **Vertex AI** | `GOOGLE_CLOUD_PROJECT`, `GOOGLE_APPLICATION_CREDENTIALS` | `vertex_ai/gemini-2.0-flash` |
| **Grok** | `XAI_API_KEY` | via LiteLLM if configured |

Default routing: orchestrator → Vertex/Gemini, fallback → GPT, research → Claude.

---

## Commands

```bash
# CrewAI (from apps/agent)
cd apps/agent
uv sync
crewai run                  # Run crew
crewai test -n 2            # Test crew
crewai train -n 5 -f training.json

# Evals
./tests/evals/run.sh

# Local infra
docker compose up -d

# Monorepo shortcuts (root)
make setup
make test
```

---

## IDE-specific notes

| IDE | Config location | Notes |
|-----|-----------------|-------|
| **Cursor** | `.cursor/rules/`, `.cursor/mcp.json` | Reads `AGENTS.md` automatically |
| **VS Code** | `.vscode/settings.json` | Copilot: `.github/copilot-instructions.md` |
| **PyCharm / IntelliJ** | `.idea/` (gitignored) | Use root `AGENTS.md` as context |
| **Zed** | `AGENTS.md` | Supports AGENTS.md convention |
| **Antigravity** | `AGENTS.md` | Same convention as Cursor family |
| **Grok CLI** | `.grok/skills/` | Project-scoped skills auto-reload |

---

## Do

- Keep agent definitions in `apps/agent/src/project_agent/config/agents.yaml`
- Keep prompts in `prompts/` — not inline in Python unless prototyping
- Document model changes in `docs/ai/llm-providers.md` and wiki Stack Decisions
- Add ADRs in `docs/adr/` for significant AI architecture choices
- Run evals before changing production prompts
- Use `uv` for Python dependency management in `apps/agent`
- Store GCP credentials outside repo (`GOOGLE_APPLICATION_CREDENTIALS`)

## Don't

- Commit API keys, service account JSON, or `.env`
- Change `config/ai/routing.json` without updating evals
- Add agent tools without schema/tests in `packages/tools/`
- Bypass guardrails in `config/ai/guardrails.json` for production paths

---

## External integrations

| System | Config | Docs |
|--------|--------|------|
| **Manus IM** | `config/integrations/manus.md` | External autonomous agent; Telegram/messaging |
| **Vertex AI** | `infrastructure/gcp/` | GCP model hosting |
| **GitHub Copilot** | `.github/copilot-instructions.md` | IDE assistant |

---

## Related docs

- [docs/ai/architecture.md](docs/ai/architecture.md)
- [docs/ai/llm-providers.md](docs/ai/llm-providers.md)
- [docs/ai/ide-setup.md](docs/ai/ide-setup.md)
- [docs/adr/0002-ai-agent-architecture.md](docs/adr/0002-ai-agent-architecture.md)
- Wiki: [Stack Decisions](https://github.com/zshgustavo/project-structure-main-template/wiki/Stack-Decisions)
- Wiki: [Risk Registry](https://github.com/zshgustavo/project-structure-main-template/wiki/Risk-Registry)
- Wiki: [Runbook](https://github.com/zshgustavo/project-structure-main-template/wiki/Runbook)