from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class StockAnalysis(BaseModel):
    symbol: str
    company_name: str
    analysis: str


class CompanyAnalysis(BaseModel):
    company_name: str
    analysis: str


class StockReport(BaseModel):
    symbol: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Full company name")
    current_price: str = Field(..., description="Current stock price")
    analysis: str = Field(
        ..., description="Comprehensive analysis combining multiple perspectives"
    )
    recommendation: str = Field(
        ..., description="Investment recommendation: Buy, Hold, or Sell"
    )


# Create specialized agents
stock_searcher = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
    response_model=StockAnalysis,
    role="Searches for current stock information and price data.",
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
        )
    ],
)

company_info_agent = Agent(
    name="Company Info Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Researches company fundamentals and recent news.",
    response_model=CompanyAnalysis,
    tools=[
        YFinanceTools(
            stock_price=False,
            company_info=True,
            company_news=True,
        )
    ],
)

# Create team with structured output
stock_research_team = Team(
    name="Stock Research Team",
    mode="coordinate",
    model=OpenAIChat("gpt-4o"),
    members=[stock_searcher, company_info_agent],
    response_model=StockReport,
    markdown=True,
    show_members_responses=True,
)

stock_research_team.print_response("Give me a comprehensive stock report for NVDA")
