from agno.agent import Agent
from agno.tools.scrapegraph import ScrapeGraphTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    tools=[ScrapeGraphTools(smartscraper=True)],
    show_tool_calls=True,
)

agent.print_response(
    """
    Use smartscraper to extract the following from https://www.wired.com/category/science/:
- News articles
- Headlines
- Images
- Links
- Author
""",
)
