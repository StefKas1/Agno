from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.file_generation import FileGenerationTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    db=SqliteDb(db_file="tmp/test.db"),
    tools=[FileGenerationTools(output_directory="tmp")],
    description="You are a helpful assistant that can generate files in various formats.",
    instructions=[
        "When asked to create files, use the appropriate file generation tools.",
        "Always provide meaningful content and appropriate filenames.",
        "Explain what you've created and how it can be used.",
    ],
    markdown=True,
)

if __name__ == "__main__":
    response = agent.run(
        "Create a PDF report about renewable energy trends in 2024. Include sections on solar, wind, and hydroelectric power."
    )
    print(response.content)
    if response.files:
        for file in response.files:
            print(f"Generated file: {file.filename} ({file.size} bytes)")
            if file.url:
                print(f"File location: {file.url}")
    print("")
