import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools, MultiMCPTools
from dotenv import load_dotenv

# 1. Run: sse_server_mcp.py

# This is the URL of the MCP server we want to use.
server_url = "http://localhost:8000/sse"


async def run_agent(message: str) -> None:
    async with MCPTools(transport="sse", url=server_url) as mcp_tools:
        agent = Agent(
            model=OpenAIChat(id="gpt-5-mini"),
            tools=[mcp_tools],
            markdown=True,
        )
        await agent.aprint_response(message=message, stream=True, markdown=True)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(run_agent("Do I have any birthdays this week?"))
