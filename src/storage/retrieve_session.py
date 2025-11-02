from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

# Setup your database
db = SqliteDb(db_file="agno.db")

# Setup your Agent with the database
agent = Agent(db=db)

# Run the Agent, effectively creating and persisting a session
agent.print_response("What is the capital of France?", session_id="123")

# Retrieve our freshly created session
session_history = agent.get_session(session_id="123")
