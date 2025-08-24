from typing import Iterator

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.yfinance import YFinanceTools
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv
from rich.pretty import pprint

load_dotenv()

# Create team members
stock_searcher = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a stock.",
    tools=[YFinanceTools()],
)

# Create the team
team = Team(
    name="Stock Research Team",
    model=OpenAIChat("gpt-4o"),
    members=[stock_searcher],
    markdown=True,
)

# Run the team
run_stream: Iterator[RunResponse] = team.run(
    "What is the stock price of NVDA", stream=True
)
pprint_run_response(run_stream, markdown=True)

# Print team leader message metrics
print("---" * 5, "Team Leader Message Metrics", "---" * 5)
if team.run_response.messages:
    for message in team.run_response.messages:
        if message.role == "assistant":
            if message.content:
                print(f"Message: {message.content}")
            elif message.tool_calls:
                print(f"Tool calls: {message.tool_calls}")
            print("---" * 5, "Metrics", "---" * 5)
            pprint(message.metrics)
            print("---" * 20)

# Print aggregated team leader metrics
print("---" * 5, "Aggregated Metrics of Team Agent", "---" * 5)
pprint(team.run_response.metrics)

# Print team leader session metrics
print("---" * 5, "Session Metrics", "---" * 5)
pprint(team.session_metrics)

# Print team member message metrics
print("---" * 5, "Team Member Message Metrics", "---" * 5)
if team.run_response.member_responses:
    for member_response in team.run_response.member_responses:
        if member_response.messages:
            for message in member_response.messages:
                if message.role == "assistant":
                    if message.content:
                        print(f"Message: {message.content}")
                    elif message.tool_calls:
                        print(f"Tool calls: {message.tool_calls}")
                    print("---" * 5, "Metrics", "---" * 5)
                    pprint(message.metrics)
                    print("---" * 20)

# Print full team session metrics (including all members)
print("---" * 5, "Full Team Session Metrics", "---" * 5)
pprint(team.full_team_session_metrics)