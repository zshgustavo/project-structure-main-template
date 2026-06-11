You are an AI assistant working on project-structure-main-template.

## Project context

- Monorepo with CrewAI agents in `apps/agent/`
- Primary cloud: Google Cloud Platform (Vertex AI, Gemini)
- Additional LLMs: Claude, GPT, Grok
- IDEs: VS Code, Cursor, PyCharm, IntelliJ, Zed, Antigravity

## Rules

1. Read `AGENTS.md` before making structural changes
2. Prompts live in `prompts/` — do not hardcode in production code
3. Run evals after prompt or routing changes
4. Document decisions in wiki or `docs/adr/`