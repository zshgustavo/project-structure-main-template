# Contributing

Thank you for contributing to this project.

## Getting started

1. Fork the repository and clone it locally.
2. Copy `.env.example` to `.env` and fill in required values.
3. Run setup: `./scripts/setup/install.sh`
4. Start local services: `docker compose up -d`

## Development workflow

1. Create a branch from `main`: `feature/`, `fix/`, or `chore/` prefix.
2. Make changes in the appropriate `apps/`, `packages/`, or `services/` directory.
3. Add or update tests under `tests/`.
4. Run lint and tests before opening a PR.
5. Open a pull request using the provided template.

## Code standards

- Keep shared logic in `packages/`, not duplicated across apps.
- Document architectural decisions in `docs/adr/`.
- Prefer small, focused PRs with clear descriptions.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(api): add user registration endpoint
fix(web): resolve hydration mismatch on dashboard
docs: update deployment guide
```

## Questions

Open a GitHub issue or discussion for questions before large changes.