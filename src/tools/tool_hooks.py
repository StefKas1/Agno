import time
from typing import Any, Callable, Dict

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger
from dotenv import load_dotenv

load_dotenv()


def logger_hook(function_name: str, function_call: Callable, arguments: Dict[str, Any]):
    """Log the duration of the function call"""
    print(f"[DEBUG] Hook triggered: {function_name} with args {arguments}")
    start_time = time.time()

    # Call the function
    result = function_call(**arguments)

    end_time = time.time()
    duration = end_time - start_time

    logger.info(f"Function {function_name} took {duration:.2f} seconds to execute")
    # Return the result
    return result


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    tool_hooks=[logger_hook],  # Hook will only be used if tool is used by agent
    show_tool_calls=True,
)

agent.print_response("What is the stock price of Apple?", stream=True)
