from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
)


if __name__ == "__main__":
    load_dotenv()
    agent.print_response("What is the stock price of Apple?", stream=True)
