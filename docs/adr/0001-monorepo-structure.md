# ADR 0001: Monorepo Structure

## Status

Accepted

## Context

The project spans multiple deployable applications, shared libraries, and optional microservices. We need a structure that scales with team size and deployment complexity.

## Decision

Adopt a monorepo with:

- `apps/` for deployable applications
- `packages/` for shared internal libraries
- `services/` for independently versioned microservices
- `infrastructure/` for IaC and container configs

## Consequences

**Positive**

- Shared code is versioned together; no cross-repo dependency hell.
- Single CI pipeline can test the full system.
- Easier refactoring across boundaries.

**Negative**

- Repo size grows; requires disciplined ownership per directory.
- CI must support selective builds (add path filters later).