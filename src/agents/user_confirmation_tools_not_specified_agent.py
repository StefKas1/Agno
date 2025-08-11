from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from dotenv import load_dotenv


@tool(requires_confirmation=True)
def sensitive_operation(data: str) -> str:
    """Perform a sensitive operation that requires confirmation."""
    # Implementation here
    return "Operation completed"


agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[sensitive_operation],
)

if __name__ == "__main__":
    load_dotenv()
    # Run the agent
    agent.run("Perform sensitive operation")
    agent.run('Call sensitive_operation with data="test"')

    # Handle confirmation
    if agent.is_paused:
        for tool in agent.run_response.tools_requiring_confirmation:
            # Get user confirmation
            print(f"Tool {tool.tool_name}({tool.tool_args}) requires confirmation")
            confirmed = input(f"Confirm? (y/n): ").lower() == "y"
            tool.confirmed = confirmed

        # Continue execution
        response = agent.continue_run()
        print(response)
    else:
        print("Agent did not wait for confirmation.")
