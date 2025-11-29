import logging

from agno.agent import Agent
from agno.team import Team
from agno.utils.log import configure_agno_logging, log_info
from agno.workflow import Workflow
from agno.workflow.step import Step
from dotenv import load_dotenv

load_dotenv()

# Create custom loggers for different components
custom_agent_logger = logging.getLogger("agent_logger")
custom_team_logger = logging.getLogger("team_logger")
custom_workflow_logger = logging.getLogger("workflow_logger")

# Configure handlers and formatters for each
for logger in [custom_agent_logger, custom_team_logger, custom_workflow_logger]:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(name)s] %(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False

# Workflow logs at DEBUG level when debug_mode is enabled
# Set workflow logger to DEBUG to see these logs
custom_workflow_logger.setLevel(logging.DEBUG)

# Apply the configuration
configure_agno_logging(
    custom_default_logger=custom_agent_logger,
    custom_agent_logger=custom_agent_logger,
    custom_team_logger=custom_team_logger,
    custom_workflow_logger=custom_workflow_logger,
)

# All logging will now use the custom agent logger by default
log_info("Using custom loggers!")

# Create agent and team
agent = Agent()
team = Team(members=[agent])

# Agent will use custom_agent_logger
agent.print_response("What is 2+2?")

# Team will use custom_team_logger
team.print_response("Tell me a short joke")

# Workflow will use custom_workflow_logger
workflow = Workflow(debug_mode=True, steps=[Step(name="step1", agent=agent)])
workflow.print_response("Tell me a fun fact")
