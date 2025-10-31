from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

# Setup your database
db = SqliteDb(db_file="agno.db")

# Setup your Agent with the database and add the session history to the context
agent = Agent(
    db=db,
    add_history_to_context=True,  # Automatically add the persisted session history to the context
    num_history_runs=3,  # Specify how many messages to add to the context
)

agent.print_response("What is the weather in France?", stream=True)
agent.print_response("What is the capital?", stream=True)
