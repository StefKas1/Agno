from agno.agent import Agent
from agno.models.openai.chat import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    tools=[YFinanceTools()],
    tool_call_limit=1,  # The Agent will not perform more than one tool call.
)

# The first tool call will be performed. The second one will fail gracefully.
agent.print_response(
    "Find me the current price of TSLA, then after that find me the latest news about Tesla.",
    stream=True,
)
