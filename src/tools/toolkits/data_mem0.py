from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mem0 import Mem0Tools
from dotenv import load_dotenv

load_dotenv()

# Requires Mem0 API key for cloud usage or local configuration for self-hosted deployments

USER_ID = "jane_doe"
SESSION_ID = "agno_session"

# Initialize the Agent with Mem0Tools
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[Mem0Tools()],
    user_id=USER_ID,
    session_id=SESSION_ID,
    add_state_in_messages=True,
    markdown=True,
    instructions=dedent(
        """
        You have an evolving memory of this user. Proactively capture new 
        personal details, preferences, plans, and relevant context the user 
        shares, and naturally bring them up in later conversation. Before 
        answering questions about past details, recall from your memory 
        to provide precise and personalized responses. Keep your memory concise: store only meaningful 
        information that enhances long-term dialogue. If the user asks to start fresh,
        clear all remembered information and proceed anew.
        """
    ),
    show_tool_calls=True,
)

# Interact with the Agent to store memories
agent.print_response("I live in NYC")
agent.print_response("I lived in San Francisco for 5 years previously")
agent.print_response("I'm going to a Taylor Swift concert tomorrow")

# Query the stored memories
agent.print_response("Summarize all the details of the conversation")
