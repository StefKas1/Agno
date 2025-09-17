import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
from dotenv import load_dotenv


async def run_agent() -> None:
    async with MCPTools(command=f"uvx mcp-server-git") as mcp_tools:
        agent = Agent(model=OpenAIChat(id="gpt-5-mini"), tools=[mcp_tools])
        await agent.aprint_response(
            "What is the license for this project?", stream=True
        )


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(run_agent())
