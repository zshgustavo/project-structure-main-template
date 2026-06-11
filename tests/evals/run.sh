#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

RESULTS_DIR="tests/evals/results"
mkdir -p "$RESULTS_DIR"
TIMESTAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="$RESULTS_DIR/eval-${TIMESTAMP}.txt"

echo "==> Running agent eval suite (smoke)" | tee "$OUT"
echo "Dataset: tests/evals/datasets/smoke.jsonl" | tee -a "$OUT"
echo "" | tee -a "$OUT"

# Placeholder — replace with real eval runner (e.g. crewai test, custom grader)
if [[ -f "apps/agent/pyproject.toml" ]]; then
  echo "CrewAI app found. Run full evals with:" | tee -a "$OUT"
  echo "  cd apps/agent && uv sync && crewai test -n 1" | tee -a "$OUT"
else
  echo "WARN: apps/agent not found" | tee -a "$OUT"
fi

echo "" | tee -a "$OUT"
echo "==> Smoke eval complete (placeholder)" | tee -a "$OUT"
echo "Results: $OUT"