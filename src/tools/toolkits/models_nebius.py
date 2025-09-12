from agno.agent import Agent
from agno.tools.models.nebius import NebiusTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    instructions=[
        "You are an AI image generation assistant using Nebius AI Studio",
        "Create high-quality images based on user descriptions",
        "Provide detailed information about the generated images",
        "Help users refine their prompts for better results",
    ],
    tools=[NebiusTools()],
)

agent.print_response(
    "Generate an image of a futuristic city with flying cars at sunset", stream=True
)
