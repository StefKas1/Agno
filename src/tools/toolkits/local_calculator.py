from agno.agent import Agent
from agno.tools.calculator import CalculatorTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    tools=[CalculatorTools()],
    markdown=True,
)

agent.print_response("What is 10*5 then to the power of 2, do it step by step")
