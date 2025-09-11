from agno.agent import Agent
from agno.tools.sql import SQLTools
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

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(tools=[SQLTools(db_url=db_url)])
agent.print_response(
    "List the tables in the database. Tell me about contents of one of the tables",
    markdown=True,
)
