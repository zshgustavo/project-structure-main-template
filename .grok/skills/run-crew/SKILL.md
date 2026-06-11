---
name: run-crew
description: >
  Run the CrewAI multi-agent crew in apps/agent. Use when the user asks to
  run agents, kickoff the crew, test agents, or execute CrewAI workflows.
  Triggers: run crew, kickoff, crewai run, test agents, multi-agent run.
---

# Run Crew

Execute the CrewAI runtime in `apps/agent/`.

## Steps

1. Confirm `.env` exists at repo root (copy from `.env.example` if missing).
2. Run from `apps/agent/`:

```bash
cd apps/agent
uv sync
crewai run
```

## Test mode

```bash
cd apps/agent
crewai test -n 2
```

## Custom topic

Edit `inputs` in `apps/agent/src/project_agent/main.py` or pass via future API.

## Troubleshooting

- Missing API key → check `.env` for `GOOGLE_CLOUD_PROJECT`, `OPENAI_API_KEY`, etc.
- Wrong model → check `config/ai/routing.json` and `LLM_*` env overrides
- Version issues → `uv run python -c "import crewai; print(crewai.__version__)"`