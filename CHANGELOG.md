# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-06-11

### Added
- AI agent layer: CrewAI runtime in `apps/agent/`
- `AGENTS.md`, Grok skills, Cursor rules, and Copilot instructions
- `config/ai/` — model routing, guardrails, and multi-LLM provider config
- `prompts/`, `tests/evals/`, `docs/ai/`, and ADR 0002 (AI architecture)
- GCP / Vertex AI infrastructure notes (`infrastructure/gcp/`)
- Manus IM integration stub (`config/integrations/manus.md`)
- `README-ptbr.md` — Brazilian Portuguese README
- `CONTRIBUTORS.md` with automatic updates on merged PRs
- GitHub workflow to add contributors when pull requests are merged (bots excluded)

### Changed
- Expanded `README.md` with full AI stack, IDE matrix, Wiki links, and env vars
- Updated `CONTRIBUTING.md` with contributor listing policy
- Updated `.env.example` with AI/LLM provider variables
- Updated `.gitignore` for GCP credentials and eval results

## [1.0.0] - 2026-06-10

### Added
- Initial monorepo project structure (apps, packages, services, infrastructure, docs, tests)
- Root `Dockerfile`, `.gitignore`, and `.vscodeignore`
- Docker Compose local stack (Postgres, Redis, Mailpit)
- GitHub CI and release workflows, issue templates, Dependabot
- Architecture docs, getting-started guide, and ADR 0001
- Makefile and setup/CI/deploy scripts

### Changed
- Renamed project from `complex-project` to `project-structure-main-template`
- Restored full `README.md` content

[1.1.0]: https://github.com/zshgustavo/project-structure-main-template/releases/tag/v1.1.0
[1.0.0]: https://github.com/zshgustavo/project-structure-main-template/releases/tag/v1.0.0