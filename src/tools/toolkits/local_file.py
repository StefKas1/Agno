from agno.agent import Agent
from agno.tools.file import FileTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(tools=[FileTools()])
agent.print_response(
    "What is the most advanced LLM currently? Save the answer to a file.", markdown=True
)
