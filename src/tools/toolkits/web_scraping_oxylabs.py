from agno.agent import Agent
from agno.tools.oxylabs import OxylabsTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    tools=[OxylabsTools()],
    markdown=True,
    show_tool_calls=True,
)

agent.print_response("""
Search for 'latest iPhone reviews' and provide a summary of the top 3 results. 
""")
