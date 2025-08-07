from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
memory = Memory(db=memory_db)

user_id = "jon_hamm@example.com"
session_id = "1001"

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    memory=memory,
    enable_session_summaries=True,
)

if __name__ == "__main__":
    load_dotenv()
    agent.print_response(
        "What can you tell me about quantum computing?",
        stream=True,
        user_id=user_id,
        session_id=session_id,
    )

    agent.print_response(
        "I would also like to know about LLMs?",
        stream=True,
        user_id=user_id,
        session_id=session_id,
    )

    session_summary = memory.get_session_summary(user_id=user_id, session_id=session_id)
    print(f"Session summary: {session_summary.summary}\n")
