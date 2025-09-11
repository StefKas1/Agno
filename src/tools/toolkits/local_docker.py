import sys

from agno.agent import Agent
from dotenv import load_dotenv

load_dotenv()

try:
    from agno.tools.docker import DockerTools

    docker_tools = DockerTools(
        enable_container_management=True,
        enable_image_management=True,
        enable_volume_management=True,
        enable_network_management=True,
    )

    # Create an agent with Docker tools
    docker_agent = Agent(
        name="Docker Agent",
        instructions=[
            "You are a Docker management assistant that can perform various Docker operations.",
            "You can manage containers, images, volumes, and networks.",
        ],
        tools=[docker_tools],
        markdown=True,
    )

    # Example: List all running Docker containers
    docker_agent.print_response("List all running Docker containers", stream=True)

    # Example: Pull and run an NGINX container
    docker_agent.print_response("Pull the latest nginx image", stream=True)
    docker_agent.print_response(
        "Run an nginx container named 'web-server' on port 8080", stream=True
    )

except ValueError as e:
    print(f"\nDocker Tool Error: {e}")
    print("\nTroubleshooting steps:")

    if sys.platform == "darwin":  # macOS
        print("1. Ensure Docker Desktop is running")
        print("2. Check Docker Desktop settings")
        print("3. Try running 'docker ps' in terminal to verify access")

    elif sys.platform == "linux":
        print("1. Check if Docker service is running:")
        print("   systemctl status docker")
        print("2. Make sure your user has permissions to access Docker:")
        print("   sudo usermod -aG docker $USER")

    elif sys.platform == "win32":
        print("1. Ensure Docker Desktop is running")
        print("2. Check Docker Desktop settings")
