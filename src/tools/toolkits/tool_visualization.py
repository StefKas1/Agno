from agno.agent import Agent
from agno.tools.visualization import VisualizationTools
from dotenv import load_dotenv

load_dotenv()

# Uses matplotlib
agent = Agent(
    instructions=[
        "You are a data visualization assistant that creates charts and plots",
        "Generate clear, informative visualizations based on user data",
        "Save charts to files and provide insights about the data",
        "Choose appropriate chart types for different data patterns",
    ],
    tools=[VisualizationTools(output_dir="my_charts")],
)

agent.print_response(
    "Create a bar chart showing sales by quarter: Q1=100, Q2=150, Q3=120, Q4=180",
    stream=True,
)
