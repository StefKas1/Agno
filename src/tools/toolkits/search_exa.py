from agno.agent import Agent
from agno.tools.exa import ExaTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    tools=[
        ExaTools(
            include_domains=["cnbc.com", "reuters.com", "bloomberg.com"],
            category="news",
            text_length_limit=1000,
        )
    ],
    show_tool_calls=True,
)
agent.print_response("Search for AAPL news", markdown=True)
