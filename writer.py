from agno.agent import Agent
from agno.models.azure import AzureOpenAI

writer_agent = Agent(
    name="Writer Agent",
    instructions="""
    You are a professional newsletter writer. 
    Based on the research content, write clear, engaging, and accurate summaries in a consistent tone. 
    Use 5 lines paragraphs and make the content readable for a general audience, but it should be in detail. 
    should contains political events, economic developments, social issues, crime, and entertainment.
    Avoid repetition, and highlight key facts in bullet points where appropriate.
    """,
    model=AzureOpenAI(id="gpt-4o-mini-techops", api_version="2025-01-01-preview"),
    search_knowledge=True,
)
