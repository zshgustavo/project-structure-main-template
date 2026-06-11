# Agent Evaluations

Regression tests for prompt quality and agent behavior.

## Run

```bash
./tests/evals/run.sh
```

Full CrewAI test:

```bash
cd apps/agent && crewai test -n 2
```

## Layout

```
tests/evals/
├── datasets/smoke.jsonl   # Smoke test cases
├── graders/             # Custom scoring logic (add here)
├── results/             # Output (gitignored)
└── run.sh
```

## When to run

- After `prompts/` changes
- After `config/ai/routing.json` or `models.json` changes
- After `agents.yaml` / `tasks.yaml` changes
- Before release tags