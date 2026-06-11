# Shared Agent Tools

Reusable tools consumed by CrewAI agents in `apps/agent/`.

## Convention

```
packages/tools/
├── <tool_name>/
│   ├── schema.json      # Tool input/output schema
│   ├── implementation.py
│   └── test_tool.py
```

Register tools in `apps/agent/src/project_agent/crew.py`.

## Examples to add

- GCP resource lookup (Vertex, Cloud Run status)
- Wiki / docs search
- GitHub issue fetcher