from agno.agent import Agent
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(tools=[WikipediaTools()], show_tool_calls=True)
agent.print_response("Search wikipedia for 'artificial intelligence'")
