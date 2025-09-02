import json
import time
from typing import Any, Callable, Dict, Iterator

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger
from dotenv import load_dotenv

load_dotenv()


def logger_hook(function_name: str, function_call: Callable, arguments: Dict[str, Any]):
    """Log the duration of the function call"""
    print(f"[DEBUG] Hook triggered: {function_name} with args {arguments}")
    start_time = time.time()

    # Call the function
    result = function_call(**arguments)

    end_time = time.time()
    duration = end_time - start_time

    logger.info(f"Function {function_name} took {duration:.2f} seconds to execute")
    # Return the result
    return result


def confirmation_hook(
    function_name: str, function_call: Callable, arguments: Dict[str, Any]
):
    """Confirm the function call"""
    if function_name != "get_top_hackernews_stories":
        raise ValueError("This tool is not allowed to be called")
    return function_call(**arguments)


# Multiple tool hooks: They will be applied in the order they are assigned
@tool(tool_hooks=[logger_hook, confirmation_hook])
def get_top_hackernews_stories(num_stories: int) -> Iterator[str]:
    """Fetch top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to retrieve
    """
    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Yield story details
    final_stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        final_stories.append(story)

    return json.dumps(final_stories)


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[get_top_hackernews_stories],
)


agent.print_response("What is the top hackernews story?", stream=True)
