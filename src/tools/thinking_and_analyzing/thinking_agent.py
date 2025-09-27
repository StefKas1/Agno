from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()


thinking_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(),
    ],
    instructions="Use tables where possible",
    markdown=True,
)

thinking_agent.print_response("Write a report comparing NVDA to TSLA", stream=True)
