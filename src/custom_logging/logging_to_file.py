import logging
from pathlib import Path

from agno.agent import Agent
from agno.utils.log import configure_agno_logging, log_info
from dotenv import load_dotenv

load_dotenv()

# Create a custom logger that writes to a file
custom_logger = logging.getLogger("file_logger")

# Ensure tmp directory exists
log_file_path = Path("tmp/log.txt")
log_file_path.parent.mkdir(parents=True, exist_ok=True)

# Use FileHandler to write to file
handler = logging.FileHandler(log_file_path)
formatter = logging.Formatter("%(levelname)s: %(message)s")
handler.setFormatter(formatter)
custom_logger.addHandler(handler)
custom_logger.setLevel(logging.INFO)
custom_logger.propagate = False

# Configure Agno to use the file logger
configure_agno_logging(custom_default_logger=custom_logger)

# All logs will be written to tmp/log.txt
log_info("This is using our file logger!")

agent = Agent()
agent.print_response("Tell me a fun fact")
