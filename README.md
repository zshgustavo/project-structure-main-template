# Project Structure Main Template

A production-ready monorepo scaffold for large, multi-service **AI agent** applications.

**AI stack:** CrewAI · GCP Vertex AI · Gemini · Claude · GPT · Grok · Copilot · Manus IM

## Structure

```
project-structure-main-template/
├── AGENTS.md          # AI assistant instructions (all IDEs)
├── apps/              # agent (CrewAI), api, web, worker
├── packages/          # Shared libraries + tools/
├── prompts/           # System prompts and templates
├── config/ai/         # Model routing, guardrails
├── .grok/skills/      # Grok CLI project skills
├── .cursor/rules/     # Cursor AI rules
├── infrastructure/    # Docker, K8s, Terraform, gcp/
├── docs/ai/           # AI architecture and provider docs
├── tests/evals/       # Agent evaluation suite
└── ...                # services, scripts, assets, etc.
```

See [AGENTS.md](AGENTS.md) for full AI development guide.

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