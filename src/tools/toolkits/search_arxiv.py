from agno.agent import Agent
from agno.tools.arxiv import ArxivTools
from dotenv import load_dotenv

load_dotenv()


agent = Agent(tools=[ArxivTools()], show_tool_calls=True)
agent.print_response("Search arxiv for 'language models'", markdown=True)
