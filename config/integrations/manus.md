# Manus IM Integration

[Manus](https://manus.im/) is an autonomous AI agent platform with messaging integrations (e.g. Telegram).

## Role in this project

Manus operates as an **external agent channel** — not inside the CrewAI runtime, but as a parallel interface for task delegation and notifications.

## Configuration (placeholder)

| Setting | Value |
|---------|-------|
| Platform | Manus IM (manus.im) |
| Default model | Vertex AI / Gemini (align with `config/ai/routing.json`) |
| Use case | Async tasks, messaging-based workflows |

## Integration points

1. **Input** — user tasks via Manus messaging → map to crew `topic` input
2. **Output** — crew results → format for Manus delivery
3. **Skills** — Manus Skills (platform feature) ↔ project `.grok/skills/` (separate systems; document mappings here)

## Security

- Do not send secrets, `.env` contents, or GCP credentials through Manus channels
- Review [Risk Registry](https://github.com/zshgustavo/project-structure-main-template/wiki/Risk-Registry) before production use

## TODO

- [ ] Define webhook or API bridge between Manus and `apps/api`
- [ ] Document authentication flow
- [ ] Add smoke test for Manus → crew trigger