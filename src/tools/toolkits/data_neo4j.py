from agno.agent import Agent
from agno.tools.neo4j import Neo4jTools
from dotenv import load_dotenv

load_dotenv()

# docker run -d -p 7474:7474 -p 7687:7687 --name neo4j -e NEO4J_AUTH=neo4j/password neo4j

agent = Agent(
    instructions=[
        "You are a graph database assistant that helps with Neo4j operations",
        "Execute Cypher queries to analyze graph data and relationships",
        "Provide insights about graph structure and patterns",
        "Help with graph data modeling and optimization",
    ],
    tools=[Neo4jTools()],
)

agent.print_response("Show me the schema of the graph database", stream=True)
