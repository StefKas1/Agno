import json
from textwrap import dedent

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv


def get_top_hackernews_stories(num_stories: int = 5) -> str:
    """Fetch and return the top stories from HackerNews.

    Args:
        num_stories: Number of top stories to retrieve (default: 5)
    Returns:
        JSON string containing story details (title, url, score, etc.)
    """
    # Get top stories
    stories = [
        {
            k: v
            for k, v in httpx.get(
                f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
            )
            .json()
            .items()
            if k != "kids"  # Exclude discussion threads
        }
        for id in httpx.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json"
        ).json()[:num_stories]
    ]
    return json.dumps(stories, indent=4)


if __name__ == "__main__":
    load_dotenv()
    # Create a Context-Aware Agent that can access real-time HackerNews data
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        # context is a dictionary that contains a set of functions (or dependencies)
        # Each function in the context is resolved before the agent runs
        # Think of it as dependency injection for Agents
        context={"top_hackernews_stories": get_top_hackernews_stories},
        # Alternatively, you can manually add the context to the instructions
        instructions=dedent("""\
            You are an insightful tech trend observer! 📰

            Here are the top stories on HackerNews:
            {top_hackernews_stories}\
        """),
        # add_state_in_messages will make the `top_hackernews_stories` variable
        # available in the instructions
        add_state_in_messages=True,
        markdown=True,
    )

    # Or set add_context=True to add the entire context to the user message.
    # This way you don’t have to manually add the context to the instructions.
    # # Create a Context-Aware Agent that can access real-time HackerNews data
    # agent = Agent(
    #     model=OpenAIChat(id="gpt-4o"),
    #     context={"top_hackernews_stories": get_top_hackernews_stories},
    #     # We can add the entire context dictionary to the instructions
    #     add_context=True,
    #     markdown=True,
    # )

    # Example usage
    agent.print_response(
        "Summarize the top stories on HackerNews and identify any interesting trends.",
        stream=True,
    )
