---
name: run-evals
description: >
  Run LLM/agent evaluation suite in tests/evals. Use when the user asks to
  evaluate agents, test prompt quality, run evals, or check regression after
  prompt or model routing changes. Triggers: run evals, evaluate agents,
  prompt regression, eval suite.
---

# Run Evals

Execute the agent evaluation suite.

## Steps

1. From repo root:

```bash
./tests/evals/run.sh
```

2. Review output in `tests/evals/results/` (gitignored).

3. If evals fail after prompt/routing changes:
   - Check `config/ai/routing.json`
   - Check `prompts/system/`
   - Update `tests/evals/datasets/smoke.jsonl` if expectations changed intentionally

## When to run

- After changing `prompts/`
- After changing `config/ai/routing.json` or `models.json`
- After modifying `agents.yaml` or `tasks.yaml`
- Before tagging a release