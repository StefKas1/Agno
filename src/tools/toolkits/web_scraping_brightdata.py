from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.brightdata import BrightDataTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        BrightDataTools(
            get_screenshot=True,
        )
    ],
    markdown=True,
    show_tool_calls=True,
)

# Example 1: Scrape a webpage as Markdown
agent.print_response(
    "Scrape this webpage as markdown: https://docs.agno.com/introduction",
)
