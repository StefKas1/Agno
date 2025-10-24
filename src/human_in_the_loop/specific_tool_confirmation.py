from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.yfinance import YFinanceTools
from agno.utils import pprint
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt

load_dotenv()

console = Console()

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(requires_confirmation_tools=["get_current_stock_price"])],
    markdown=True,
)

run_response = agent.run("What is the current stock price of Apple?")
if run_response.is_paused:  # Or agent.run_response.is_paused
    for tool in run_response.tools_requiring_confirmation:  # type: ignore
        # Ask for confirmation
        console.print(
            f"Tool name [bold blue]{tool.tool_name}({tool.tool_args})[/] requires confirmation."
        )
        message = (
            Prompt.ask("Do you want to continue?", choices=["y", "n"], default="y")
            .strip()
            .lower()
        )

        if message == "n":
            tool.confirmed = False
        else:
            # We update the tools in place
            tool.confirmed = True

    run_response = agent.continue_run(run_response=run_response)
    pprint.pprint_run_response(run_response)
