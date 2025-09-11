from agno.agent import Agent
from agno.tools.local_file_system import LocalFileSystemTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    instructions=[
        "You are a file management assistant that helps save content to local files",
        "Create files with appropriate names and extensions",
        "Organize files in the specified directory structure",
        "Provide clear feedback about file operations",
    ],
    tools=[LocalFileSystemTools(target_directory="./output")],
)

agent.print_response(
    "Save this meeting summary to a file: 'Discussed Q4 goals and budget allocation'",
    stream=True,
)
