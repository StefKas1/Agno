import base64

import requests
from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()


def image_url_to_data_url(image_url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(image_url, headers=headers)
    response.raise_for_status()
    mime_type = response.headers.get("Content-Type", "image/jpeg")
    base64_data = base64.b64encode(response.content).decode("utf-8")
    return f"data:{mime_type};base64,{base64_data}"


image_data_url = image_url_to_data_url(
    "https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[Image(url=image_data_url)],
    stream=True,
)
