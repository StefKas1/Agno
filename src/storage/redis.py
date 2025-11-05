from agno.agent import Agent
from agno.db.redis import RedisDb
from dotenv import load_dotenv

load_dotenv()

# docker run -d \
#   --name my-redis \
#   -p 6379:6379 \
#   redis

# Initialize Redis db (use the right db_url for your setup)
db = RedisDb(db_url="redis://localhost:6379")

# Create agent with Redis db
agent = Agent(db=db)
