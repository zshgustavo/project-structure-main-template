# Crew input template

Use this template when kicking off the CrewAI crew programmatically or via CLI.

```json
{
  "topic": "<describe the task or question>",
  "constraints": "<optional: time, format, audience>",
  "context": "<optional: links, files, prior decisions>"
}
```

## Example

```json
{
  "topic": "Compare Vertex AI vs direct Gemini API for this project's agent runtime",
  "constraints": "Under 500 words, markdown output, technical audience",
  "context": "See config/ai/models.json and docs/ai/llm-providers.md"
}
```