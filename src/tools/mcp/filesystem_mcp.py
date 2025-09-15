import asyncio
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
from dotenv import load_dotenv

# Might not work on Windows
# 1. Add MCP server to .vscode/mcp.json
# 2. Start MCP server


async def run_agent(message: str) -> None:
    """Run the filesystem agent with the given message."""

    file_path = str(Path(__file__).parent.parent.parent.parent)

    # MCP server to access the filesystem (via `npx`)
    async with MCPTools(
        f"npx -y @modelcontextprotocol/server-filesystem {file_path}"
    ) as mcp_tools:
        agent = Agent(
            model=OpenAIChat(id="gpt-5-mini"),
            tools=[mcp_tools],
            instructions=dedent("""\
                You are a filesystem assistant. Help users explore files and directories.

                - Navigate the filesystem to answer questions
                - Use the list_allowed_directories tool to find directories that you can access
                - Provide clear context about files you examine
                - Use headings to organize your responses
                - Be concise and focus on relevant information\
            """),
            markdown=True,
        )

        # Run the agent
        await agent.aprint_response(message, stream=True)


# Example usage
if __name__ == "__main__":
    load_dotenv()
    # Basic example - exploring project license
    asyncio.run(run_agent("What is the license for this project?"))
