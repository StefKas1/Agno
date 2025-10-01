import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.utils.log import logger
from dotenv import load_dotenv

load_dotenv()


async def atask1(delay: int):
    """Simulate a task that takes a random amount of time to complete
    Args:
        delay (int): The amount of time to delay the task
    """
    logger.info("Task 1 has started")
    for _ in range(delay):
        await asyncio.sleep(1)
        logger.info("Task 1 has slept for 1s")
    logger.info("Task 1 has completed")
    return f"Task 1 completed in {delay:.2f}s"


async def atask2(delay: int):
    """Simulate a task that takes a random amount of time to complete
    Args:
        delay (int): The amount of time to delay the task
    """
    logger.info("Task 2 has started")
    for _ in range(delay):
        await asyncio.sleep(1)
        logger.info("Task 2 has slept for 1s")
    logger.info("Task 2 has completed")
    return f"Task 2 completed in {delay:.2f}s"


async def atask3(delay: int):
    """Simulate a task that takes a random amount of time to complete
    Args:
        delay (int): The amount of time to delay the task
    """
    logger.info("Task 3 has started")
    for _ in range(delay):
        await asyncio.sleep(1)
        logger.info("Task 3 has slept for 1s")
    logger.info("Task 3 has completed")
    return f"Task 3 completed in {delay:.2f}s"


async_agent = Agent(
    # Concurrent execution of tools requires a model that supports parallel function calling.
    model=OpenAIChat(id="gpt-5-mini"),
    # Provide your Agent with a list of tools, preferably asynchronous for optimal performance.
    # However, synchronous functions can also be used since they will execute concurrently on separate threads.
    tools=[atask2, atask1, atask3],
    markdown=True,
)

# Run the Agent using either the arun or aprint_response method, enabling concurrent execution of tool calls.
asyncio.run(
    async_agent.aprint_response("Please run all tasks with a delay of 3s", stream=True)
)
