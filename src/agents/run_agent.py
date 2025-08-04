from typing import Iterator

from agno.agent import Agent, RunResponse, RunResponseEvent
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))

    # Run agent and return the response as a variable
    response: RunResponse = agent.run("Tell me a 5 second short story about a robot")
    # Print the response in markdown format
    pprint_run_response(response, markdown=True)

    # Run agent and return the response as a stream
    response_stream: Iterator[RunResponseEvent] = agent.run(
        "Tell me a 5 second short story about a lion", stream=True
    )
    # Print the response stream in markdown format
    pprint_run_response(response_stream, markdown=True)

    # Stream with intermediate steps
    response_stream = agent.run(
        "Your prompt", stream=True, stream_intermediate_steps=True
    )
    for event in response_stream:
        if event.event == "RunResponseContent":
            print(f"Content: {event.content}")
        elif event.event == "ToolCallStarted":
            print(f"Tool call started: {event.tool}")
        elif event.event == "ReasoningStep":
            print(f"Reasoning step: {event.content}")
        else:
            print("...")

    # Can store all events that happened during a run on the RunResponse object
    agent = Agent(model=OpenAIChat(id="gpt-4o-mini"), store_events=True)
    response = agent.run(
        "Tell me a 5 second short story about a lion",
        stream=True,
        stream_intermediate_steps=True,
    )
    pprint_run_response(response)
    for event in agent.run_response.events:
        print(event.event)
