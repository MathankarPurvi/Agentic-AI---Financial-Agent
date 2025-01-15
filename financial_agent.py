from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

## web search agent

web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-Versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,

)

## financial agent

finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-Versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),

    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

## multi_ai_agent

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-Versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
