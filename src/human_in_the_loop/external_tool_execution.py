import subprocess

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.utils import pprint
from dotenv import load_dotenv

load_dotenv()


# We have to create a tool with the correct name, arguments and docstring for the agent to know what to call.
@tool(external_execution=True)
def execute_shell_command(command: str) -> str:
    """Execute a shell command.

    Args:
        command (str): The shell command to execute

    Returns:
        str: The output of the shell command
    """
    return subprocess.check_output(command, shell=True).decode("utf-8")


agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    tools=[execute_shell_command],
    markdown=True,
)

run_response = agent.run("What files do I have in my current directory?")
if run_response.is_paused:
    for tool in run_response.tools_awaiting_external_execution:
        if tool.tool_name == execute_shell_command.name:
            print(f"Executing {tool.tool_name} with args {tool.tool_args} externally")

            # We execute the tool ourselves. You can execute any function or process here and use the tool_args as input.
            result = execute_shell_command.entrypoint(**tool.tool_args)
            # We have to set the result on the tool execution object so that the agent can continue
            tool.result = result

    run_response = agent.continue_run(run_response=run_response)
    pprint.pprint_run_response(run_response)
