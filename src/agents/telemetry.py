from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # https://docs.agno.com/basics/telemetry
    telemetry=False,  # Disables telemetry
)


if __name__ == "__main__":
    load_dotenv()
    agent.print_response("What is the stock price of Apple?")
