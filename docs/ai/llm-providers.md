# LLM Providers

## Provider matrix

| Provider | Use case | CrewAI model string | Required env |
|----------|----------|---------------------|--------------|
| **Vertex AI** | Default orchestration, GCP-native | `vertex_ai/gemini-2.0-flash` | `GOOGLE_CLOUD_PROJECT`, `GOOGLE_APPLICATION_CREDENTIALS`, `VERTEX_AI_LOCATION` |
| **Gemini API** | Direct Google AI Studio | `gemini/gemini-2.0-flash` | `GOOGLE_API_KEY` |
| **OpenAI / GPT** | Writing, structured output | `openai/gpt-4o` | `OPENAI_API_KEY` |
| **Anthropic / Claude** | Research, long context | `anthropic/claude-sonnet-4-20250514` | `ANTHROPIC_API_KEY` |
| **Grok (xAI)** | Grok CLI / optional routing | `xai/grok-2-latest` | `XAI_API_KEY` |

Config source of truth: `config/ai/models.json`

## Routing by agent role

| Agent | Primary | Fallback |
|-------|---------|----------|
| Orchestrator | Vertex AI / Gemini | GPT-4o |
| Researcher | Claude Sonnet | Gemini Flash |
| Writer | GPT-4o | Gemini Flash |

Override via env: `LLM_ORCHESTRATOR`, `LLM_RESEARCHER`, `LLM_WRITER`, `LLM_DEFAULT`

Config: `config/ai/routing.json`

## Vertex AI setup

```bash
gcloud services enable aiplatform.googleapis.com
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT=your-project-id
export VERTEX_AI_LOCATION=us-central1
```

## Cost tips

- Use `gemini-2.0-flash` / `gpt-4o-mini` for drafts and evals
- Reserve `claude-sonnet` / `gpt-4o` for final outputs
- Set `guardrails.cost.warn_above_usd_per_run` in `config/ai/guardrails.json`

## Changelog

| Date | Change |
|------|--------|
| 2026-06-10 | Initial provider matrix |