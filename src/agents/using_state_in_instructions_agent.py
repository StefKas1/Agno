from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Initialize the session state with a variable
    session_state={"user_name": "John"},
    # You can use variables from the session state in the instructions
    instructions="Users name is {user_name}",  # Don’t use f-string in instructions. Directly use the {key} syntax, Agno substitutes the values for you
    show_tool_calls=True,
    add_state_in_messages=True,
    markdown=True,
)

if __name__ == "__main__":
    load_dotenv()
    agent.print_response("What is my name?", stream=True)
