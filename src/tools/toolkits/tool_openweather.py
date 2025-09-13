from agno.agent import Agent
from agno.tools.openweather import OpenWeatherTools
from dotenv import load_dotenv

load_dotenv()

# Create an agent with OpenWeatherTools
agent = Agent(
    tools=[
        OpenWeatherTools(
            units="imperial",  # Options: 'standard', 'metric', 'imperial'
        )
    ],
    markdown=True,
)

# Get current weather for a location
agent.print_response("What's the current weather in Tokyo?", markdown=True)
