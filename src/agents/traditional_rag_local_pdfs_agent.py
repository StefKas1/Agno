from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
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
    knowledge_base = PDFKnowledgeBase(
        # Read PDF from this path
        path="pdfs_for_rag",
        # Store embeddings in the `ai.pdf_documents` table
        vector_db=PgVector(
            table_name="pdf_documents", db_url=db_url, search_type=SearchType.hybrid
        ),
    )
    # Load the knowledge base: Comment after first run
    knowledge_base.load(upsert=True)

    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        knowledge=knowledge_base,
        # add_references=True always adds information from the knowledge base to the prompt,
        # regardless of whether it is relevant to the question or helpful.
        # This is the traditional 2023 RAG approach.
        add_references=True,
        # We can set search_knowledge=True to add a search_knowledge_base() tool to the Agent.
        # Or False so agent does not search knowledge base.
        search_knowledge=False,
        markdown=True,
        # debug_mode=True,
    )
    agent.print_response("How do I make chicken and galangal in coconut milk soup")
