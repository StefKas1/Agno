from typing import List, Optional

import typer
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.storage.postgres import PostgresStorage
from agno.vectordb.pgvector import PgVector, SearchType
from dotenv import load_dotenv

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

# 2. Install required libraries
# pip install -U pgvector pypdf "psycopg[binary]" sqlalchemy

# 3. Run this .py file

# Run the agent
# Now the agent continues across sessions. Ask a question:
# How do I make pad thai?

# Then message bye to exit, start the app again and ask:
# What was my last message?

# Start a new session
# Run the storage_cli_agent.py file with the --new flag to start a new session:
# python storage_cli_agent.py --new


def pdf_agent(new: bool = False, user: str = "user"):
    session_id: Optional[str] = None

    if not new:
        existing_sessions: List[str] = storage.get_all_session_ids(user)
        if len(existing_sessions) > 0:
            session_id = existing_sessions[0]

    agent = Agent(
        session_id=session_id,
        user_id=user,
        knowledge=knowledge_base,
        storage=storage,
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the agent to read the chat history
        read_chat_history=True,
        # We can also automatically add the chat history to the messages sent to the model
        # But giving the model the chat history is not always useful, so we give it a tool instead
        # to only use when needed.
        # add_history_to_messages=True,
        # Number of historical responses to add to the messages.
        # num_history_responses=3,
    )
    if session_id is None:
        session_id = agent.session_id
        print(f"Started Session: {session_id}\n")
    else:
        print(f"Continuing Session: {session_id}\n")

    # Runs the agent as a cli app
    agent.cli_app(markdown=True)


if __name__ == "__main__":
    load_dotenv()

    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(
            table_name="recipes", db_url=db_url, search_type=SearchType.hybrid
        ),
    )
    storage = PostgresStorage(table_name="pdf_agent", db_url=db_url)

    # Load the knowledge base: Comment after first run
    knowledge_base.load(upsert=True)

    typer.run(pdf_agent)
