# ADR 0002: AI Agent Architecture

## Status

Accepted

## Context

The project evolves from a stack-agnostic monorepo template into a multi-agent AI application. The owner uses CrewAI, GCP Vertex AI, Gemini, Claude, GPT, Grok, Copilot, Manus IM, and multiple IDEs.

We need a consistent architecture for agent runtime, prompt management, model routing, and IDE assistant conventions.

## Decision

1. **CrewAI** in `apps/agent/` as the primary agent runtime
2. **Vertex AI / Gemini** as default cloud LLM provider (GCP-first)
3. **LiteLLM model strings** in `config/ai/` for multi-provider routing
4. **Prompts as files** in `prompts/` — not hardcoded in production
5. **`AGENTS.md`** at repo root as the shared contract for all IDE AI assistants
6. **Grok skills** in `.grok/skills/` for CLI workflows
7. **Manus IM** documented as external channel in `config/integrations/manus.md`
8. **Evals** in `tests/evals/` required before prompt/routing release changes

## Consequences

**Positive**

- Single agent runtime with clear config boundaries
- Multi-IDE and multi-LLM without vendor lock-in to one assistant
- GCP-native path for production on Vertex AI

**Negative**

- Multiple config files to keep in sync (`AGENTS.md`, Copilot, Cursor rules)
- LiteLLM model strings must be validated when providers update model names

## References

- `docs/ai/architecture.md`
- `config/ai/models.json`
- Wiki: Stack Decisions, Risk Registry