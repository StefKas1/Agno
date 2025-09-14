from agno.agent import Agent
from agno.tools.webtools import WebTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    instructions=[
        "You are a web utility assistant that helps with URL operations",
        "Expand shortened URLs to show their final destinations",
        "Help users understand where links lead before visiting them",
        "Provide clear information about URL expansions and redirects",
    ],
    tools=[WebTools()],
)

agent.print_response("Expand this shortened URL: https://bit.ly/3example", stream=True)
