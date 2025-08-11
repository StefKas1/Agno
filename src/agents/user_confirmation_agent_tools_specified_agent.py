from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.yfinance import YFinanceTools
from agno.utils import pprint
from dotenv import load_dotenv

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(requires_confirmation_tools=["get_current_stock_price"])],
)


if __name__ == "__main__":
    load_dotenv()
    agent.run("What is the current stock price of Apple?")
    if agent.is_paused:
        for tool in agent.run_response.tools_requiring_confirmation:
            print(f"Tool {tool.tool_name}({tool.tool_args}) requires confirmation")
            answer = input(f"Confirm? (y/n): ").lower()
            confirmed = answer == "y"

            if answer == "n":
                tool.confirmed = False  # Prohibits use of tool
            else:
                # We update the tools in place
                tool.confirmed = True  # Allows use of tool

        run_response = agent.continue_run()
        pprint.pprint_run_response(run_response)
