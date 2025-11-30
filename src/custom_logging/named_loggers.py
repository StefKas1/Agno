import logging

from agno.agent import Agent
from agno.team import Team
from agno.workflow import Workflow
from agno.workflow.step import Step
from dotenv import load_dotenv

load_dotenv()

# Set up named loggers BEFORE creating agents/teams/workflows
logger_configs = [
    ("agno", "agent.log"),
    ("agno-team", "team.log"),
    ("agno-workflow", "workflow.log"),
]

for logger_name, log_file in logger_configs:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file)
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(handler)
    logger.propagate = False

# Agno will automatically detect and use these loggers
agent = Agent()
agent.print_response("Hello from agent!")  # Agent logs will go to agent.log

team = Team(members=[agent])
team.print_response("Hello from team!")  # Team logs will go to team.log

# Workflow requires debug mode to use the workflow logger
workflow = Workflow(debug_mode=True, steps=[Step(name="step1", agent=agent)])
workflow.run("Hello from workflow!")  # Workflow logs will go to workflow.log
