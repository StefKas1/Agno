import logging

from agno.agent import Agent
from agno.utils.log import configure_agno_logging, log_info
from dotenv import load_dotenv

load_dotenv()

# Set up a custom logger
custom_logger = logging.getLogger("custom_logger")
handler = logging.StreamHandler()
formatter = logging.Formatter("[CUSTOM_LOGGER] %(levelname)s: %(message)s")
handler.setFormatter(formatter)
custom_logger.addHandler(handler)
custom_logger.setLevel(logging.INFO)
custom_logger.propagate = False

# Configure Agno to use the custom logger
configure_agno_logging(custom_default_logger=custom_logger)

# All logging will now use the custom logger
log_info("This is using our custom logger!")

agent = Agent()
agent.print_response("What is 2+2?")
