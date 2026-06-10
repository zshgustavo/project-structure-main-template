# Architecture Overview

## High-level design

```
┌─────────────┐     ┌─────────────┐
│   apps/web  │────▶│   apps/api  │
└─────────────┘     └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ packages │ │ services │ │  worker  │
        │   core   │ │   auth   │ │  (jobs)  │
        └──────────┘ └──────────┘ └──────────┘
              │            │
              └─────┬──────┘
                    ▼
            ┌───────────────┐
            │  PostgreSQL   │
            │    Redis      │
            └───────────────┘
```

## Principles

1. **Monorepo, clear boundaries** — apps deploy independently; packages share logic.
2. **Services when needed** — extract to `services/` when a domain needs its own lifecycle.
3. **Infrastructure as code** — all deployment config lives in `infrastructure/`.
4. **Document decisions** — use ADRs in `docs/adr/` for significant choices.

## Data flow

1. Client requests hit `apps/web` or directly `apps/api`.
2. API uses `packages/core` for domain logic.
3. Background work is offloaded to `apps/worker`.
4. Cross-cutting concerns (auth, notifications) may call `services/`.