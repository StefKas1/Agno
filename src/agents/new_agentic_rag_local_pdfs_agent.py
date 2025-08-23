from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.vectordb.pgvector import PgVector, SearchType
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    knowledge_base = PDFKnowledgeBase(
        # Read PDF from this path
        path="pdfs_for_rag",
        # Store embeddings in the `ai.gradio_pdf_documents` table
        vector_db=PgVector(
            table_name="gradio_pdf_documents",
            db_url=db_url,
            search_type=SearchType.hybrid,
        ),
    )
    # Load the knowledge base: Comment out after first run
    knowledge_base.load(upsert=True)

    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        knowledge=knowledge_base,
        search_knowledge=True,
        read_chat_history=True,
        show_tool_calls=True,
        markdown=True,
    )
    agent.print_response(
        "How do I make chicken and galangal in coconut milk soup", stream=True
    )
    agent.print_response("What was my last question?", markdown=True)
