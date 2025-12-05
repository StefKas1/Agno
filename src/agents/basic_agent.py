from agno.agent import Agent, RunOutput
from agno.models.openai import OpenAIChat
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-5-nano"),
    tools=[HackerNewsTools()],
    instructions="Write a report on the topic. Output only the report.",
    markdown=True,
)

# Run agent and return the response as a variable
response: RunOutput = agent.run("Trending startups and products.")

# Print the response in markdown format
pprint_run_response(response, markdown=True)
