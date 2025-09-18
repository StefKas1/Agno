import asyncio
import os

from agno.agent import Agent
from agno.tools.mcp import MultiMCPTools
from dotenv import load_dotenv


async def run_agent(message: str) -> None:
    """Run the Airbnb and Google Maps agent with the given message."""

    env = {
        **os.environ,
        "GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY"),
    }

    async with MultiMCPTools(
        [
            "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt",
            "npx -y @modelcontextprotocol/server-google-maps",
        ],
        env=env,
    ) as mcp_tools:
        agent = Agent(
            tools=[mcp_tools],
            markdown=True,
        )

        await agent.aprint_response(message, stream=True)


# Example usage
if __name__ == "__main__":
    load_dotenv()
    # Pull request example
    asyncio.run(
        run_agent(
            "What listings are available in Cape Town for 2 people for 3 nights from 1 to 4 August 2025?"
        )
    )
