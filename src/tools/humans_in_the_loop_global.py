import json
from typing import Any, Callable, Dict

import httpx
from agno.agent import Agent
from agno.exceptions import StopAgentRun
from agno.models.openai import OpenAIChat
from agno.tools import tool
from dotenv import load_dotenv
from rich.console import Console
from rich.live import Live
from rich.prompt import Prompt

console = Console()

# Global Live object
live = None  # will be assigned in main


def confirmation_hook(
    function_name: str, function_call: Callable, arguments: Dict[str, Any]
):
    global live
    if live is not None:
        live.stop()

    console.print(f"\nAbout to run [bold blue]{function_name}[/]")
    message = (
        Prompt.ask("Do you want to continue?", choices=["y", "n"], default="y")
        .strip()
        .lower()
    )

    if live is not None:
        live.start()

    if message != "y":
        raise StopAgentRun(
            "Tool call cancelled by user",
            agent_message="Stopping execution as permission was not granted.",
        )

    return function_call(**arguments)


@tool(tool_hooks=[confirmation_hook])
def get_top_hackernews_stories(num_stories: int) -> str:
    """Fetch top stories from Hacker News."""
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    final_stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        story.pop("text", None) if "text" in story else None
        final_stories.append(story)

    return json.dumps(final_stories)


if __name__ == "__main__":
    load_dotenv()
    with Live(console=console, refresh_per_second=4) as live_instance:
        live = live_instance  # assign to global for the hook

        agent = Agent(
            model=OpenAIChat(id="gpt-4o-mini"),
            tools=[get_top_hackernews_stories],  # keep original function
            markdown=True,
        )

        agent.print_response(
            "Fetch the top 2 hackernews stories?", stream=True, console=console
        )
