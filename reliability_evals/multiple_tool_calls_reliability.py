from typing import Optional

from agno.agent import Agent
from agno.eval.reliability import ReliabilityEval, ReliabilityResult
from agno.models.openai import OpenAIChat
from agno.run.agent import RunOutput
from agno.tools.calculator import CalculatorTools
from dotenv import load_dotenv

load_dotenv()


def multiply_and_exponentiate():
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[CalculatorTools()],
    )
    response: RunOutput = agent.run(
        "What is 10*5 then to the power of 2? do it step by step"
    )
    evaluation = ReliabilityEval(
        name="Tool Calls Reliability",
        agent_response=response,
        expected_tool_calls=["multiply", "exponentiate"],
    )
    result: Optional[ReliabilityResult] = evaluation.run(print_results=True)
    if result:
        result.assert_passed()


if __name__ == "__main__":
    multiply_and_exponentiate()
