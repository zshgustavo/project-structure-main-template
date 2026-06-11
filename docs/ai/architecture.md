# AI Architecture

## High-level flow

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   IDEs      │   │  Manus IM   │   │  apps/api   │
│ Grok/Copilot│   │  (external) │   │  (future)   │
└──────┬──────┘   └──────┬──────┘   └──────┬──────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
              ┌─────────────────────┐
              │    apps/agent       │
              │    CrewAI Crew      │
              │  orchestrator       │
              │  researcher         │
              │  writer             │
              └──────────┬──────────┘
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Vertex AI   │  │ Claude      │  │ GPT         │
│ Gemini/GCP  │  │ Anthropic   │  │ OpenAI      │
└─────────────┘  └─────────────┘  └─────────────┘
```

## Components

| Component | Location | Role |
|-----------|----------|------|
| Agent runtime | `apps/agent/` | CrewAI orchestration |
| Prompts | `prompts/` | System and task prompts |
| Model config | `config/ai/` | Routing, guardrails |
| Tools | `packages/tools/` | Shared agent tools |
| Evals | `tests/evals/` | Quality regression |
| Grok skills | `.grok/skills/` | CLI workflows |
| GCP infra | `infrastructure/gcp/` | Vertex deployment |

## Design principles

1. **Prompts as files** — versioned, reviewable, eval-able
2. **Provider-agnostic routing** — LiteLLM strings in config, not hardcoded
3. **GCP-first** — Vertex AI as default; GPT/Claude as specialists
4. **Multi-IDE** — `AGENTS.md` as shared contract across all editors
5. **Eval before release** — prompt/routing changes require eval pass

## Related

- [ADR 0002](../adr/0002-ai-agent-architecture.md)
- [LLM providers](llm-providers.md)
- [IDE setup](ide-setup.md)