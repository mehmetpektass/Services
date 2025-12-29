from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from tools.custom_tool import FiqhSearchTool
import os
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class FiqhAgenticRagApi():
    """FiqhAgenticRagApi crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    def __init__(self):
        self.gemini_llm = LLM(
            model=os.getenv("GROQ_MODEL"),
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.3,
        )

    @agent
    def db_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['db_researcher'], # type: ignore[index]
            tools=[FiqhSearchTool()],
            verbose=True,
            llm=self.gemini_llm,
            max_iter=1,
        )

    @agent
    def fiqh_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['fiqh_writer'], # type: ignore[index]
            verbose=True,
            llm=self.gemini_llm,
        )
        
    @agent
    def content_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_reviewer'], # type: ignore[index]
            verbose=True,
            llm=self.gemini_llm,
        )    


    @task
    def search_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_task'], # type: ignore[index]
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'], # type: ignore[index]
        )
    
    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'], # type: ignore[index]
        )    

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
        
if __name__ == "__main__":
    print("Fiqh Agentic RAG Crew starting...")
    
    inputs = {'question': 'Kerahat vakitleri her mezhep için aynı mıdır'}

    fiqh_crew = FiqhAgenticRagApi()
    
    # Execute
    result = fiqh_crew.crew().kickoff(inputs=inputs)
    print("\n\n########################")
    print("## Result ##")
    print("########################\n")
    print(result)
