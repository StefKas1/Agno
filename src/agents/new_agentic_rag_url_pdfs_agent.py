from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
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

if __name__ == "__main__":
    load_dotenv()

    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(
            table_name="recipes", db_url=db_url, search_type=SearchType.hybrid
        ),
    )
    # Load the knowledge base: Comment out after first run
    knowledge_base.load(upsert=True)

    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        knowledge=knowledge_base,
        # Add a tool to search the knowledge base which enables agentic RAG.
        search_knowledge=True,
        # Add a tool to read chat history.
        read_chat_history=True,
        show_tool_calls=True,
        markdown=True,
        # debug_mode=True,
    )
    agent.print_response(
        "How do I make chicken and galangal in coconut milk soup", stream=True
    )
    agent.print_response("What was my last question?", markdown=True)
