from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Install and run frontend:
# 0. cd src
# 0. Clone Agent UI: npx create-agent-ui@latest
# 1. Run agent-ui: agent-ui && npm run dev
# 2. Open: http://localhost:3000

# Run backend
# 3. Run this Python file (agent OS)


agent_storage: str = "tmp/agents.db"

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    # Store the agent sessions in a sqlite database
    db=SqliteDb(db_file=agent_storage),
    # Adds the current date and time to the context
    add_datetime_to_context=True,
    # Adds the history of the conversation to the messages
    add_history_to_context=True,
    # Number of history responses to add to the messages
    num_history_runs=5,
    # Adds markdown formatting to the messages
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools()],
    instructions=["Always use tables to display data"],
    db=SqliteDb(db_file=agent_storage),
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,
)

agent_os = AgentOS(agents=[web_agent, finance_agent])
app = agent_os.get_app()

if __name__ == "__main__":
    load_dotenv()
    agent_os.serve("agentos:app", reload=True)
