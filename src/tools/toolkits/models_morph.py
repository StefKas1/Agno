from agno.agent import Agent
from agno.tools.models.morph import MorphTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    instructions=[
        "You are a code editing assistant using Morph's advanced AI capabilities",
        "Help users modify, improve, and refactor their code intelligently",
        "Apply code changes efficiently while maintaining code quality",
        "Provide explanations for the modifications made",
    ],
    tools=[MorphTools()],
)

agent.print_response(
    "Refactor this Python function to be more efficient and add type hints", stream=True
)
