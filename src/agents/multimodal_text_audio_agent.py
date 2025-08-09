import requests
from agno.agent import Agent
from agno.media import Audio
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

agent = Agent(
    model=OpenAIChat(id="gpt-4o-audio-preview", modalities=["text"]),
    markdown=True,
)

if __name__ == "__main__":
    load_dotenv()

    # Fetch the audio file
    url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
    response = requests.get(url)
    response.raise_for_status()
    wav_data = response.content

    agent.print_response(
        "What is in this audio?", audio=[Audio(content=wav_data, format="wav")]
    )
