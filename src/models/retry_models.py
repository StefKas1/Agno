from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="Share 15 minute healthy recipes.",
    markdown=True,
    exponential_backoff=True,  # True to automatically retry requests that fail due to third-party model provider errors
    retries=2,
    delay_between_retries=1,
)


if __name__ == "__main__":
    load_dotenv()
    agent.print_response("Share a breakfast recipe.", stream=True)
