---
name: vertex-gcp
description: >
  Configure and deploy agents on Google Cloud Vertex AI. Use when the user
  mentions GCP, Google Cloud, Vertex AI, Gemini on GCP, service accounts,
  or cloud deployment for agents. Triggers: vertex ai, gcp deploy, google
  cloud, gemini vertex, gcloud.
---

# Vertex AI / GCP

Guide for GCP and Vertex AI in this project.

## Prerequisites

1. GCP project with Vertex AI API enabled
2. Service account with Vertex AI User role
3. Credentials via `GOOGLE_APPLICATION_CREDENTIALS` (never commit JSON key files)

## Env vars (`.env`)

```
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
VERTEX_AI_LOCATION=us-central1
```

## CrewAI model strings

```
vertex_ai/gemini-2.0-flash
vertex_ai/gemini-2.5-pro-preview-05-06
```

See `config/ai/models.json` for full list.

## Docs in repo

- `infrastructure/gcp/README.md`
- `docs/ai/llm-providers.md`

## Auth check

```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```