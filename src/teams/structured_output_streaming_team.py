from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class MarketAnalysis(BaseModel):
    sector: str = Field(..., description="Market sector being analyzed")
    key_trends: List[str] = Field(..., description="Major trends affecting the sector")
    top_performers: List[str] = Field(
        ..., description="Best performing stocks in the sector"
    )
    market_outlook: str = Field(
        ..., description="Overall market outlook and predictions"
    )
    risk_factors: List[str] = Field(..., description="Key risks to consider")


# Create research agents
trend_analyst = Agent(
    name="Trend Analyst",
    model=OpenAIChat("gpt-4o"),
    role="Analyzes market trends and sector performance.",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True)],
)

risk_assessor = Agent(
    name="Risk Assessor",
    model=OpenAIChat("gpt-4o"),
    role="Identifies and evaluates market risks and opportunities.",
    tools=[YFinanceTools(company_news=True, company_info=True)],
)

# Create streaming team
market_research_team = Team(
    name="Market Research Team",
    mode="coordinate",
    model=OpenAIChat("gpt-4o"),
    members=[trend_analyst, risk_assessor],
    response_model=MarketAnalysis,
    markdown=True,
    show_members_responses=True,
)

# Stream the team response
# When streaming with teams and structured output, you’ll see
# intermediate steps from individual team members, but the
# final structured result is delivered as a single complete chunk
# rather than being streamed progressively
market_research_team.print_response(
    "Analyze the technology sector for Q1 2024",
    stream=True,
    stream_intermediate_steps=True,
)
