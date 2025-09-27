from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()


analyzing_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        ReasoningTools(
            enable_think=True,
            enable_analyze=True,
            add_instructions=True,
            add_few_shot=True,
        ),
        YFinanceTools(),
    ],
    instructions="Use tables where possible",
    markdown=True,
)

analyzing_agent.print_response("Write a report comparing NVDA to TSLA", stream=True)
