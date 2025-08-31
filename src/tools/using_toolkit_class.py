from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from dotenv import load_dotenv

load_dotenv()

"""
In this example, the GoogleSearchTools toolkit is configured to stop 
the agent after executing the google_search function and 
to show the result of this function.
"""

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        GoogleSearchTools(
            stop_after_tool_call_tools=["google_search"],
            show_result_tools=["google_search"],
        )
    ],
    show_tool_calls=True,
)

agent.print_response("What's the latest about gpt 4.5?", markdown=True)
