from io import BytesIO

from agno.agent import Agent, RunOutput  # noqa
from agno.models.google import Gemini
from dotenv import load_dotenv
from PIL import Image

load_dotenv()


# No system message should be provided
agent = Agent(
    model=Gemini(
        id="gemini-2.5-flash-image",
        response_modalities=[
            "Text",
            "Image",
        ],  # This means to generate both images and text
    )
)

# Print the response in the terminal
run_response = agent.run("Make me an image of a cat in a tree.")

if run_response and isinstance(run_response, RunOutput) and run_response.images:
    for image_response in run_response.images:
        image_bytes = image_response.content
        if image_bytes:
            image = Image.open(BytesIO(image_bytes))
            image.show()
            # Save the image to a file
            # image.save("generated_image.png")
else:
    print("No images found in run response")
