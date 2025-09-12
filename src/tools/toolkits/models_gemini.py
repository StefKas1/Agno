from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models.gemini import GeminiTools
from agno.utils.media import save_base64_data
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    tools=[GeminiTools()],
)

response = agent.run(
    "Create an artistic portrait of a cyberpunk samurai in a rainy city"
)
if response.images:
    save_base64_data(response.images[0].content, "tmp/cyberpunk_samurai.png")
