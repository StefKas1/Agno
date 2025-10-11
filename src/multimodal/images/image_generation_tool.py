from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.openai import OpenAITools
from agno.utils.media import save_base64_data
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    db=SqliteDb(db_file="tmp/test.db"),
    tools=[OpenAITools(image_model="gpt-image-1")],
    add_history_to_context=True,
    markdown=True,
)

response = agent.run(
    "Generate a photorealistic image of a cozy coffee shop interior",
)

if response.images and response.images[0].content:
    save_base64_data(str(response.images[0].content), "tmp/coffee_shop.png")
