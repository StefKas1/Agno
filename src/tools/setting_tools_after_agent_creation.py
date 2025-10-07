import random

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools import tool
from agno.tools.calculator import CalculatorTools
from dotenv import load_dotenv

load_dotenv()

agent1 = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4"),
)

agent2 = Agent(
    name="Company Info Searcher",
    model=OpenAIChat("gpt-4"),
)

team = Team(
    name="Stock Research Team",
    model=OpenAIChat("gpt-4"),
    members=[agent1, agent2],
    tools=[CalculatorTools()],
    markdown=True,
    show_members_responses=True,
)


@tool
def get_stock_price(stock_symbol: str) -> str:
    """Get the current stock price of a stock."""
    return f"The current stock price of {stock_symbol} is {random.randint(100, 1000)}."


@tool
def get_stock_availability(stock_symbol: str) -> str:
    """Get the current availability of a stock."""
    return (
        f"The current stock available of {stock_symbol} is {random.randint(100, 1000)}."
    )


# This will remove any other tools already assigned to your Agent or Team
# and override it with the list of tools provided to set_tools
team.set_tools([get_stock_price, get_stock_availability])

team.print_response("What is the current stock price of NVDA?", stream=True)
team.print_response("How much stock NVDA stock is available?", stream=True)
