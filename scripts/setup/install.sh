#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

echo "==> Setting up project-structure-main-template"

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "Created .env from .env.example"
fi

echo "==> Starting local infrastructure"
docker compose up -d

echo "==> Setup complete"
echo "Next: implement app-specific install steps in apps/*/ and packages/*/"