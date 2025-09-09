from agno.agent import Agent
from agno.tools.duckdb import DuckDbTools
from dotenv import load_dotenv

load_dotenv()

# The following agent will analyze the movies file using SQL and return the result
agent = Agent(
    tools=[DuckDbTools()],
    show_tool_calls=True,
    system_message="Use this file for Movies data: https://agno-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
)

agent.print_response(
    "What is the average rating of movies?", markdown=True, stream=False
)
