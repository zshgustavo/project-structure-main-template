# API

Backend application — REST or GraphQL API.

## Responsibilities

- HTTP routing and request validation
- Authentication middleware
- Orchestration of domain logic from `packages/core`

## Local development

```bash
# Add your run command, e.g.:
# npm run dev
# uvicorn main:app --reload
```

## Environment

Uses root `.env`. Key variables: `API_PORT`, `DATABASE_URL`, `JWT_SECRET`.