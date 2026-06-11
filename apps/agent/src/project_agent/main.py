#!/usr/bin/env python
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[4] / ".env")

from project_agent.crew import ProjectAgentCrew


def run():
    inputs = {"topic": "AI agent architecture on GCP with CrewAI"}
    ProjectAgentCrew().crew().kickoff(inputs=inputs)


def test():
    inputs = {"topic": "smoke test"}
    ProjectAgentCrew().crew().test(n_iterations=1, inputs=inputs)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        run()