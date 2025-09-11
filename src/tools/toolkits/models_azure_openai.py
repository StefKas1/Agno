from agno.agent import Agent
from agno.tools.models.azure_openai import AzureOpenAITools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    instructions=[
        "You are an AI image generation assistant using Azure OpenAI",
        "Generate high-quality images based on user descriptions",
        "Provide detailed descriptions of the generated images",
    ],
    tools=[AzureOpenAITools()],
)


agent.print_response("Generate an image of a sunset over mountains", stream=True)
