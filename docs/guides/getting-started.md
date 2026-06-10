# Getting Started

## Prerequisites

- Docker & Docker Compose
- Git
- Your language runtime(s) — add specifics per app

## Local setup

```bash
git clone <your-repo-url>
cd project-structure-main-template
cp .env.example .env
./scripts/setup/install.sh
```

## Project layout

| Path | Purpose |
|------|---------|
| `apps/` | User-facing deployables |
| `packages/` | Shared code — import, don't copy |
| `services/` | Independently deployable microservices |
| `tests/` | Cross-app integration & e2e tests |

## Running apps

Add run commands here once you choose your stack, e.g.:

```bash
# apps/api
# apps/web
# apps/worker
```

## Next steps

- Read the [architecture overview](../architecture/overview.md)
- Review existing [ADRs](../adr/)
- Open a PR following [CONTRIBUTING.md](../../CONTRIBUTING.md)