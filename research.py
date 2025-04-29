from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.hackernews import HackerNewsTools



research_agent = Agent(
    name="Research Agent",
    tools=[GoogleSearchTools(),HackerNewsTools()],
    instructions="You are a research agent. Your task is to scrape top 3 news for today date in very detail on political events, economic developments, social issues, crime, and entertainment.",
    model=AzureOpenAI(id="gpt-4o-mini",api_version="2024-01-01"),
)
