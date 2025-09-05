from agno.agent import Agent
from agno.tools.linkup import LinkupTools
from dotenv import load_dotenv

load_dotenv()


agent = Agent(tools=[LinkupTools()], show_tool_calls=True)
agent.print_response("What's the latest news in French politics?", markdown=True)
