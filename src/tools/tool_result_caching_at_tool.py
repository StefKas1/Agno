from agno.agent import Agent
from agno.tools import tool
from dotenv import load_dotenv

load_dotenv()


@tool(cache_results=True)
def get_stock_price(ticker: str) -> str:
    """Get the current stock price of a given ticker"""

    # ... Long running operation

    return f"The current stock price of {ticker} is 100"


agent = Agent(tools=[get_stock_price])
agent.print_response("What is the current stock price for AAPL?")
