from agno.agent import Agent
from agno.tools.jina import JinaReaderTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(tools=[JinaReaderTools()])
agent.print_response("Summarize: https://github.com/agno-agi/agno")
