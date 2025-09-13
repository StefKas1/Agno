from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    instructions=[
        "You are a logical reasoning assistant that breaks down complex problems",
        "Use step-by-step thinking to analyze situations thoroughly",
        "Apply structured reasoning to reach well-founded conclusions",
        "Show your reasoning process clearly to help users understand your logic",
    ],
    tools=[ReasoningTools()],
)

agent.print_response(
    "Analyze the pros and cons of remote work for software developers", stream=True
)
