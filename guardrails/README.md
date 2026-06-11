# Guardrails

Input/output safety policies for agents. Machine-readable rules in `config/ai/guardrails.json`.

## Categories

- **Input** — length limits, injection pattern blocking
- **Output** — citation requirements, token limits
- **Security** — no secrets in logs or responses
- **Cost** — spend warnings per run

Extend with Python validators in this folder when moving beyond JSON config.