import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools, MultiMCPTools
from dotenv import load_dotenv

# This is the URL of the MCP server we want to use.
server_url = "http://localhost:8000/sse"


async def run_agent(message: str) -> None:
    # Initialize and connect to the SSE MCP server
    mcp_tools = MCPTools(transport="sse", url=server_url)
    await mcp_tools.connect()

    try:
        agent = Agent(
            model=OpenAIChat(id="gpt-5-mini"),
            tools=[mcp_tools],
            markdown=True,
        )
        await agent.aprint_response(message=message, stream=True, markdown=True)
    finally:
        await mcp_tools.close()


# Using MultiMCPTools, we can connect to multiple MCP servers at once, even if they use different transports.
# In this example we connect to both our example server (SSE transport), and a different server (stdio transport).
async def run_agent_with_multimcp(message: str) -> None:
    # Initialize and connect to multiple MCP servers with different transports
    mcp_tools = MultiMCPTools(
        commands=["npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt"],
        urls=[server_url],
        urls_transports=["sse"],
    )
    await mcp_tools.connect()

    try:
        agent = Agent(
            model=OpenAIChat(id="gpt-5-mini"),
            tools=[mcp_tools],
            markdown=True,
        )
        await agent.aprint_response(message=message, stream=True, markdown=True)
    finally:
        await mcp_tools.close()


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(run_agent("Do I have any birthdays this week?"))
    asyncio.run(
        run_agent_with_multimcp(
            "Can you check when is my mom's birthday, and if there are any AirBnb listings in SF for two people for that day?"
        )
    )
