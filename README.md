# Project Structure Main Template

A production-ready monorepo scaffold for large, multi-service **AI agent** applications.

**AI stack:** CrewAI · GCP Vertex AI · Gemini · Claude · GPT · Grok · Copilot · Manus IM

**Repository:** [github.com/zshgustavo/project-structure-main-template](https://github.com/zshgustavo/project-structure-main-template)  
**Wiki:** [GitHub Wiki documentation](https://github.com/zshgustavo/project-structure-main-template/wiki)  
**Current release:** `v1.0.0`  
**Portuguese README:** [README-ptbr.md](README-ptbr.md)

---

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
├── services/          # Microservices (auth, notifications, etc.)
├── scripts/           # Setup, CI, and deploy
└── ...                # tests, config, assets, etc.
```

See [AGENTS.md](AGENTS.md) for the full AI development guide.

---

## Quick start

### Local infrastructure

```bash
cp .env.example .env
./scripts/setup/install.sh
docker compose up -d
```

### CrewAI agents

```bash
cd apps/agent
uv sync
crewai run
```

### Agent evaluations

```bash
./tests/evals/run.sh
# or
cd apps/agent && crewai test -n 2
```

---

## Apps

| App      | Description                       | Port |
|----------|-----------------------------------|------|
| `agent`  | Multi-agent runtime (CrewAI)      | —    |
| `api`    | REST/GraphQL backend              | 4000 |
| `web`    | Frontend application              | 3000 |
| `worker` | Background job processor          | —    |

---

## Packages

| Package  | Description                    |
|----------|--------------------------------|
| `core`   | Business logic & domain models |
| `ui`     | Shared UI components           |
| `config` | Shared configuration utilities |
| `types`  | Shared TypeScript/types        |
| `tools`  | Reusable tools for agents      |

---

## AI stack

| Component         | Technology                        | Config location              |
|-------------------|-----------------------------------|------------------------------|
| Agent runtime     | CrewAI                            | `apps/agent/`                |
| Primary cloud     | Google Cloud Platform (Vertex AI) | `infrastructure/gcp/`        |
| Default LLM       | Gemini via Vertex AI              | `config/ai/models.json`      |
| Additional LLMs   | Claude, GPT, Grok                 | `config/ai/routing.json`     |
| External channel  | Manus IM                          | `config/integrations/manus.md` |
| IDE assistants    | Grok, Copilot, Claude, GPT        | `AGENTS.md`, `.grok/skills/` |

### Default model routing

| Agent        | Primary model            |
|--------------|--------------------------|
| Orchestrator | Vertex AI / Gemini Flash |
| Researcher   | Claude Sonnet            |
| Writer       | GPT-4o                   |

Override via `.env`: `LLM_ORCHESTRATOR`, `LLM_RESEARCHER`, `LLM_WRITER`, `LLM_DEFAULT`

---

## Supported IDEs

| IDE          | AI assistant   | Configuration                       |
|--------------|----------------|-------------------------------------|
| VS Code      | GitHub Copilot | `.github/copilot-instructions.md`   |
| Cursor       | Cursor Agent   | `.cursor/rules/ai-project.mdc`      |
| PyCharm      | Copilot        | `AGENTS.md`                         |
| IntelliJ     | Copilot        | `AGENTS.md`                         |
| Zed          | Built-in AI    | `AGENTS.md`                         |
| Antigravity  | Agent mode     | `AGENTS.md`                         |
| Grok CLI     | Grok           | `.grok/skills/`                     |

---

## Documentation

### In the repository

- [Getting started](docs/guides/getting-started.md)
- [Architecture overview](docs/architecture/overview.md)
- [AI architecture](docs/ai/architecture.md)
- [LLM providers](docs/ai/llm-providers.md)
- [IDE setup](docs/ai/ide-setup.md)
- [API reference](docs/api/README.md)
- [ADRs — architecture decisions](docs/adr/)

### On the Wiki

- [Work Needed](https://github.com/zshgustavo/project-structure-main-template/wiki/WORKNEEDED) — project history and remaining tasks
- [Stack Decisions](https://github.com/zshgustavo/project-structure-main-template/wiki/Stack-Decisions) — technology choices
- [Runbook](https://github.com/zshgustavo/project-structure-main-template/wiki/Runbook) — step-by-step when things go wrong
- [Risk Registry](https://github.com/zshgustavo/project-structure-main-template/wiki/Risk-Registry) — risk tracking
- [Templates](https://github.com/zshgustavo/project-structure-main-template/wiki/Home) — ADR, deployment, and more

---

## Development

```bash
# General tests
./scripts/ci/test.sh

# Lint
./scripts/ci/lint.sh

# Build
./scripts/ci/build.sh

# Deploy to staging
./scripts/deploy/staging.sh

# Makefile shortcuts
make setup
make test
make lint
make up
```

---

## Local infrastructure (Docker Compose)

| Service  | Port | Purpose              |
|----------|------|----------------------|
| Postgres | 5432 | Database             |
| Redis    | 6379 | Cache / queues       |
| Mailpit  | 8025 | Dev email (web UI)   |

---

## Environment variables

Copy `.env.example` to `.env` and fill in:

- **Application:** `APP_NAME`, `DATABASE_URL`, `REDIS_URL`
- **Vertex AI / GCP:** `GOOGLE_CLOUD_PROJECT`, `GOOGLE_APPLICATION_CREDENTIALS`, `VERTEX_AI_LOCATION`
- **Gemini API:** `GOOGLE_API_KEY`
- **OpenAI / GPT:** `OPENAI_API_KEY`
- **Anthropic / Claude:** `ANTHROPIC_API_KEY`
- **Grok (xAI):** `XAI_API_KEY`

Never commit `.env` files or service account key files.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

Use [Conventional Commits](https://www.conventionalcommits.org/) and open PRs with the template in `.github/pull_request_template.md`.

---

## License

[MIT](LICENSE)

---

## See also

- [README in Brazilian Portuguese](README-ptbr.md)
- [AGENTS.md](AGENTS.md) — shared contract for AI assistants