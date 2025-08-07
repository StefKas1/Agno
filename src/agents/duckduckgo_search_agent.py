from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

agent = Agent(tools=[DuckDuckGoTools()], show_tool_calls=True, markdown=True)

if __name__ == "__main__":
    load_dotenv()
    agent.print_response("Whats happening in France?", stream=True)
