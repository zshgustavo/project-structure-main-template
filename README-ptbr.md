# Project Structure Main Template

Modelo de monorepo pronto para produção, voltado a aplicações complexas e multi-serviço com **agentes de IA**.

**Stack de IA:** CrewAI · GCP Vertex AI · Gemini · Claude · GPT · Grok · Copilot · Manus IM

**Repositório:** [github.com/zshgustavo/project-structure-main-template](https://github.com/zshgustavo/project-structure-main-template)  
**Wiki:** [Documentação no GitHub Wiki](https://github.com/zshgustavo/project-structure-main-template/wiki)  
**Versão atual:** `v1.0.0`

---

## Estrutura do projeto

```
project-structure-main-template/
├── AGENTS.md          # Instruções para assistentes de IA (todas as IDEs)
├── apps/              # agent (CrewAI), api, web, worker
├── packages/          # Bibliotecas compartilhadas + tools/
├── prompts/           # Prompts de sistema e templates
├── config/ai/         # Roteamento de modelos e guardrails
├── .grok/skills/      # Skills do Grok CLI (escopo do projeto)
├── .cursor/rules/     # Regras do Cursor
├── infrastructure/    # Docker, K8s, Terraform, gcp/
├── docs/ai/           # Arquitetura de IA e provedores
├── tests/evals/       # Suite de avaliação de agentes
├── services/          # Microsserviços (auth, notifications, etc.)
├── scripts/           # Setup, CI e deploy
└── ...                # tests, config, assets, etc.
```

Consulte [AGENTS.md](AGENTS.md) para o guia completo de desenvolvimento com IA.

---

## Início rápido

### Infraestrutura local

```bash
cp .env.example .env
./scripts/setup/install.sh
docker compose up -d
```

### Agentes CrewAI

```bash
cd apps/agent
uv sync
crewai run
```

### Testes de agentes

```bash
./tests/evals/run.sh
# ou
cd apps/agent && crewai test -n 2
```

---

## Aplicações (`apps/`)

| App      | Descrição                         | Porta |
|----------|-----------------------------------|-------|
| `agent`  | Runtime multi-agente (CrewAI)     | —     |
| `api`    | Backend REST/GraphQL              | 4000  |
| `web`    | Aplicação frontend                | 3000  |
| `worker` | Processador de jobs em background | —     |

---

## Pacotes compartilhados (`packages/`)

| Pacote   | Descrição                              |
|----------|----------------------------------------|
| `core`   | Lógica de negócio e modelos de domínio |
| `ui`     | Componentes de UI compartilhados       |
| `config` | Utilitários de configuração            |
| `types`  | Tipos compartilhados (TypeScript etc.) |
| `tools`  | Ferramentas reutilizáveis para agentes |

---

## Stack de IA

| Componente        | Tecnologia                          | Onde configurar              |
|-------------------|-------------------------------------|------------------------------|
| Runtime de agentes| CrewAI                              | `apps/agent/`                |
| Cloud principal   | Google Cloud Platform (Vertex AI)   | `infrastructure/gcp/`        |
| LLM padrão        | Gemini via Vertex AI                | `config/ai/models.json`      |
| LLMs adicionais   | Claude, GPT, Grok                   | `config/ai/routing.json`     |
| Canal externo     | Manus IM                            | `config/integrations/manus.md` |
| Assistentes IDE   | Grok, Copilot, Claude, GPT          | `AGENTS.md`, `.grok/skills/` |

### Roteamento padrão de modelos

| Agente        | Modelo principal              |
|---------------|-------------------------------|
| Orquestrador  | Vertex AI / Gemini Flash      |
| Pesquisador   | Claude Sonnet                 |
| Escritor      | GPT-4o                        |

Variáveis de override no `.env`: `LLM_ORCHESTRATOR`, `LLM_RESEARCHER`, `LLM_WRITER`, `LLM_DEFAULT`

---

## IDEs suportadas

| IDE            | Assistente de IA | Configuração                          |
|----------------|------------------|---------------------------------------|
| VS Code        | GitHub Copilot   | `.github/copilot-instructions.md`   |
| Cursor         | Cursor Agent     | `.cursor/rules/ai-project.mdc`        |
| PyCharm        | Copilot          | `AGENTS.md`                           |
| IntelliJ       | Copilot          | `AGENTS.md`                           |
| Zed            | IA integrada     | `AGENTS.md`                           |
| Antigravity    | Modo agente      | `AGENTS.md`                           |
| Grok CLI       | Grok             | `.grok/skills/`                       |

---

## Documentação

### No repositório

- [Primeiros passos](docs/guides/getting-started.md)
- [Visão geral da arquitetura](docs/architecture/overview.md)
- [Arquitetura de IA](docs/ai/architecture.md)
- [Provedores de LLM](docs/ai/llm-providers.md)
- [Configuração de IDEs](docs/ai/ide-setup.md)
- [Referência da API](docs/api/README.md)
- [ADRs — decisões de arquitetura](docs/adr/)

### Na Wiki (GitHub)

- [Work Needed](https://github.com/zshgustavo/project-structure-main-template/wiki/WORKNEEDED) — histórico e tarefas pendentes
- [Stack Decisions](https://github.com/zshgustavo/project-structure-main-template/wiki/Stack-Decisions) — decisões de tecnologia
- [Runbook](https://github.com/zshgustavo/project-structure-main-template/wiki/Runbook) — o que fazer quando algo dá errado
- [Risk Registry](https://github.com/zshgustavo/project-structure-main-template/wiki/Risk-Registry) — registro de riscos
- [Templates](https://github.com/zshgustavo/project-structure-main-template/wiki/Home) — ADR, deploy, etc.

---

## Desenvolvimento

```bash
# Testes gerais
./scripts/ci/test.sh

# Lint
./scripts/ci/lint.sh

# Build
./scripts/ci/build.sh

# Deploy em staging
./scripts/deploy/staging.sh

# Atalhos via Makefile
make setup
make test
make lint
make up
```

---

## Infraestrutura local (Docker Compose)

| Serviço  | Porta | Uso                    |
|----------|-------|------------------------|
| Postgres | 5432  | Banco de dados         |
| Redis    | 6379  | Cache / filas          |
| Mailpit  | 8025  | E-mail de desenvolvimento |

---

## Variáveis de ambiente

Copie `.env.example` para `.env` e preencha:

- **Aplicação:** `APP_NAME`, `DATABASE_URL`, `REDIS_URL`
- **Vertex AI / GCP:** `GOOGLE_CLOUD_PROJECT`, `GOOGLE_APPLICATION_CREDENTIALS`, `VERTEX_AI_LOCATION`
- **Gemini API:** `GOOGLE_API_KEY`
- **OpenAI / GPT:** `OPENAI_API_KEY`
- **Anthropic / Claude:** `ANTHROPIC_API_KEY`
- **Grok (xAI):** `XAI_API_KEY`

Nunca commite arquivos `.env` ou chaves de service account.

---

## Contribuindo

Consulte [CONTRIBUTING.md](CONTRIBUTING.md).

Use [Conventional Commits](https://www.conventionalcommits.org/) e abra PRs com o template fornecido em `.github/pull_request_template.md`.

---

## Licença

[MIT](LICENSE)

---

## Leia também

- [README em inglês](README.md)
- [AGENTS.md](AGENTS.md) — contrato compartilhado para assistentes de IA