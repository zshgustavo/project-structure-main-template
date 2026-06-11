# Google Cloud Platform — Vertex AI

GCP infrastructure notes for agent deployment.

## Services

| Service | Purpose |
|---------|---------|
| **Vertex AI** | Gemini model hosting (primary) |
| **Cloud Run** | Containerized agent/API (future) |
| **Cloud Storage** | Knowledge files, eval datasets |
| **Secret Manager** | API keys and service account refs |
| **Artifact Registry** | Docker images |

## Setup

```bash
gcloud services enable aiplatform.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable secretmanager.googleapis.com

gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

## Environment

```
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=/path/to/sa.json
VERTEX_AI_LOCATION=us-central1
```

## Terraform

Extend `infrastructure/terraform/` with GCP provider modules when ready.

## Related

- `config/ai/models.json` — Vertex model strings
- `.grok/skills/vertex-gcp/SKILL.md` — Grok workflow
- `docs/ai/llm-providers.md`