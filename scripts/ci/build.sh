#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

mkdir -p dist
echo "==> Building artifacts (placeholder)" > dist/build-info.txt
echo "Add build steps per app in apps/*/"