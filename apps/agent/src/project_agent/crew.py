import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


def _llm(model_key: str) -> LLM:
    """Resolve LLM from env override or default model key."""
    env_map = {
        "orchestrator": "LLM_ORCHESTRATOR",
        "researcher": "LLM_RESEARCHER",
        "writer": "LLM_WRITER",
        "default": "LLM_DEFAULT",
    }
    env_var = env_map.get(model_key, "LLM_DEFAULT")
    model = os.getenv(env_var, os.getenv("LLM_DEFAULT", "vertex_ai/gemini-2.0-flash"))
    return LLM(model=model)


@CrewBase
class ProjectAgentCrew:
    """Multi-agent crew with Vertex/Gemini default and multi-provider support."""

    @agent
    def orchestrator(self) -> Agent:
        return Agent(
            config=self.agents_config["orchestrator"],
            llm=_llm("orchestrator"),
            inject_date=True,
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            llm=_llm("researcher"),
            inject_date=True,
            verbose=True,
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
            llm=_llm("writer"),
            inject_date=True,
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def writing_task(self) -> Task:
        return Task(config=self.tasks_config["writing_task"])

    @task
    def orchestration_review(self) -> Task:
        return Task(config=self.tasks_config["orchestration_review"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )