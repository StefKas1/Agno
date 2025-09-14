from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    tools=[YouTubeTools()],
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

agent.print_response(
    "Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True
)
