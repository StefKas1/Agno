from agno.agent import Agent
from agno.tools.website import WebsiteTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(tools=[WebsiteTools()], show_tool_calls=True)
agent.print_response(
    "Search web page: 'https://docs.agno.com/introduction'", markdown=True
)
