from agno.agent import Agent
from agno.tools.postgres import PostgresTools
from dotenv import load_dotenv

load_dotenv()

# 1. Run PgVector (vector database) via Docker
# docker run -d \
#   -e POSTGRES_DB=ai \
#   -e POSTGRES_USER=ai \
#   -e POSTGRES_PASSWORD=ai \
#   -e PGDATA=/var/lib/postgresql/data/pgdata \
#   -v pgvolume:/var/lib/postgresql/data \
#   -p 5532:5432 \
#   --name pgvector \
#   agnohq/pgvector:16


# Initialize PostgresTools with connection details
postgres_tools = PostgresTools(
    host="localhost", port=5532, db_name="ai", user="ai", password="ai"
)

# Create an agent with the PostgresTools
agent = Agent(tools=[postgres_tools])

# Example: Ask the agent to run a SQL query
agent.print_response("""
Please run a SQL query to get all users from the users table
who signed up in the last 30 days
""")
