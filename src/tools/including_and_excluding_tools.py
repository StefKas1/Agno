from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    tools=[
        CalculatorTools(
            exclude_tools=["exponentiate", "factorial", "is_prime", "square_root"],
        ),
        DuckDuckGoTools(include_tools=["duckduckgo_search"]),
    ],
    markdown=True,
)

agent.print_response(
    "Search the web for a difficult sum that can be done with normal arithmetic and solve it.",
)
