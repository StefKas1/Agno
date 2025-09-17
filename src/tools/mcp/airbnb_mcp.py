"""🏠 MCP Airbnb Agent - Search for Airbnb listings!

This example shows how to create an agent that uses MCP to search for Airbnb listings.

"""

import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
from agno.utils.pprint import apprint_run_response
from dotenv import load_dotenv

# Might not work on Windows
# 1. Add MCP server to .vscode/mcp.json
# 2. Start MCP server
# ^^ Both, 1. and 2. are not needed, Agno starts the MCP server directly via
# stdio (standard input/output); simply initialize the MCPTools class with its command argument;
# the command you pass is the one used to run the MCP server the agent will have access to


async def run_agent(message: str) -> None:
    async with MCPTools(
        "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt"
    ) as mcp_tools:
        agent = Agent(
            agent=Agent(model=OpenAIChat(id="gpt-5-mini")),
            tools=[mcp_tools],
            markdown=True,
        )

        response_stream = await agent.arun(message, stream=True)
        await apprint_run_response(response_stream, markdown=True)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(
        run_agent(
            "What listings are available in San Francisco for 2 people for 3 nights from 1 to 4 August 2025?"
        )
    )
