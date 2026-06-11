# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[1.0.0]: https://github.com/zshgustavo/project-structure-main-template/releases/tag/v1.0.0