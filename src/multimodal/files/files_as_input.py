from agno.agent import Agent
from agno.db.in_memory import InMemoryDb
from agno.media import File
from agno.models.anthropic import Claude
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Claude(id="claude-sonnet-4-0"),
    db=InMemoryDb(),
    markdown=True,
)

agent.print_response(
    "Summarize the contents of the attached file.",
    files=[
        File(url="https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"),
    ],
)
