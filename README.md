# Project Structure Main Template

A production-ready monorepo scaffold for large, multi-service applications.

## Structure

```
project-structure-main-template/
├── apps/              # Deployable applications (api, web, worker)
├── packages/          # Shared libraries consumed by apps & services
├── services/          # Standalone microservices
├── infrastructure/    # Docker, Kubernetes, Terraform
├── docs/              # Architecture, API specs, ADRs, guides
├── scripts/           # Setup, deploy, and CI helper scripts
├── tests/             # Cross-cutting test suites
├── config/            # Environment configs and schemas
├── tools/             # Internal dev tooling
└── assets/            # Static assets (images, fonts)
```

## Quick start

```bash
cp .env.example .env
./scripts/setup/install.sh
docker compose up -d
```

## Apps

| App     | Description              | Port |
|---------|--------------------------|------|
| `api`   | REST/GraphQL backend     | 4000 |
| `web`   | Frontend application     | 3000 |
| `worker`| Background job processor | —    |

## Packages

| Package  | Description                    |
|----------|--------------------------------|
| `core`   | Business logic & domain models |
| `ui`     | Shared UI components           |
| `config` | Shared configuration utilities |
| `types`  | Shared TypeScript/types        |

## Documentation

- [Getting started](docs/guides/getting-started.md)
- [Architecture overview](docs/architecture/overview.md)
- [API reference](docs/api/README.md)
- [ADRs](docs/adr/)

## Development

```bash
# Run all tests
./scripts/ci/test.sh

# Lint
./scripts/ci/lint.sh

# Deploy to staging
./scripts/deploy/staging.sh
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)