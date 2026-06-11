# GitHub Copilot Instructions

This is a **multi-agent AI monorepo** using CrewAI, GCP Vertex AI, Gemini, Claude, and GPT.

## Read first

- Root `AGENTS.md` — full conventions for all AI assistants
- `apps/agent/` — CrewAI runtime (Python, `uv`, YAML agent config)
- `config/ai/` — model routing; do not hardcode providers in application code

## When editing Python (CrewAI)

- Use `crewai.LLM(model="provider/model")` — never raw OpenAI clients
- Agent config lives in `apps/agent/src/project_agent/config/agents.yaml`
- Prompts live in `prompts/` — prefer files over inline strings
- Python `>=3.10,<3.14`; manage deps with `uv` in `apps/agent`

## When editing configs

- LLM keys go in `.env` only (see `.env.example`)
- Never commit `GOOGLE_APPLICATION_CREDENTIALS` JSON files

## Quality

- Run `crewai test` after agent/task changes
- Run `./tests/evals/run.sh` after prompt or routing changes