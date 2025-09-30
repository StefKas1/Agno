from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.memory import MemoryTools
from dotenv import load_dotenv

load_dotenv()


# Create a database connection
db = SqliteDb(db_file="tmp/memory.db")

memory_tools = MemoryTools(
    db=db,
)

agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    tools=[memory_tools],
    markdown=True,
)

agent.print_response(
    "My name is John Doe and I like to hike in the mountains on weekends. "
    "I like to travel to new places and experience different cultures. "
    "I am planning to travel to Africa in December. ",
    user_id="john_doe@example.com",
    stream=True,
)

# This won't use the session history, but instead will use the memory tools to get the memories
agent.print_response(
    "What have you remembered about me?", stream=True, user_id="john_doe@example.com"
)
