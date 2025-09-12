from agno.agent import Agent
from agno.tools.openai import OpenAITools
from agno.utils.media import save_base64_data
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="OpenAI Image Generation Agent",
    tools=[OpenAITools(image_model="dall-e-3")],
    markdown=True,
)

response = agent.run("Generate a photorealistic image of a cozy coffee shop interior")

if response.images:
    save_base64_data(response.images[0].content, "tmp/coffee_shop.png")
