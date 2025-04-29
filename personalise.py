from agno.agent import Agent
from agno.models.azure import AzureOpenAI

personalisation_agent = Agent(
    name="Personalisation Agent",
    instructions="""
    You are a personalisation expert. Based on reader preferences (political events, economic developments, social issues, crime, and entertainment.), 
    rewrite or reorder the newsletter content to fit the user's interest. 
    If no clear preference is given, keep a balanced mix.
    """,
    model=AzureOpenAI(id="gpt-4o-mini-techops", api_version="2025-01-01-preview"),
)
