from agno.agent import Agent
from agno.db.sqlite import AsyncSqliteDb
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from dotenv import load_dotenv

# 1. Start your AgentOS:
# python src/agentos/main_agent_os.py

# 2. Access your running instance:
# a) App Interface: http://localhost:7777 - Use this URL when connecting to the AgentOS control plane
# b) API Documentation: http://localhost:7777/docs - Interactive API documentation and testing
# c) Configuration: http://localhost:7777/config - View AgentOS configuration

# It is recommended to use all of the async building blocks of Agno
# when building your AgentOS. For example, use async tool definitions,
# async database connections, async pre/post hooks, etc.
# This helps unlock maximum concurrency and performance when running your AgentOS.

assistant = Agent(
    name="Assistant",
    model=OpenAIChat(id="gpt-4o"),
    db=AsyncSqliteDb(db_file="my_os.db"),
    instructions=["You are a helpful AI assistant."],
    markdown=True,
)

agent_os = AgentOS(
    id="my-first-os",
    description="My first AgentOS",
    agents=[assistant],
)

app = agent_os.get_app()

if __name__ == "__main__":
    load_dotenv()
    # Default port is 7777; change with port=...
    agent_os.serve(app="main_agent_os:app", reload=True)
