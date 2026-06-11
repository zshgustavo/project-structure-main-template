# Agent — CrewAI Runtime

Primary multi-agent application for this monorepo.

## Stack

- **Framework:** CrewAI
- **LLMs:** Vertex AI / Gemini (default), GPT, Claude
- **Cloud:** Google Cloud Platform
- **Assistants:** Grok, Copilot, Manus IM (external)

## Quick start

```bash
cd apps/agent
cp ../../.env.example ../../.env   # or symlink
uv sync
crewai run
```

## Structure

```
apps/agent/
├── pyproject.toml
├── knowledge/          # RAG knowledge sources
└── src/project_agent/
    ├── main.py
    ├── crew.py
    └── config/
        ├── agents.yaml
        ├── tasks.yaml
        └── tools/
```

## Model configuration

Models are defined in `config/ai/models.json` at repo root. Agents reference them via `llm` in `crew.py` or env-driven routing.

## Commands

| Command | Description |
|---------|-------------|
| `crewai run` | Execute the crew |
| `crewai test -n 2` | Test with 2 iterations |
| `crewai train -n 5 -f training.json` | Train crew |