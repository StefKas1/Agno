from agno.agent import Agent
from agno.tools.python import PythonTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(tools=[PythonTools()])
agent.print_response(
    "Write a python script for fibonacci series and display the result till the 10th number"
)
