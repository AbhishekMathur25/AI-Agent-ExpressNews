from agno.models.azure import AzureOpenAI
from agno.team.team import Team
from research import research_agent
from writer import writer_agent
from editor import editor_agent
from personalise import personalisation_agent


agent_team = Team(
    name="Discussion Team",
    mode="collaborate",
    model=AzureOpenAI(
        id="gpt-4o-mini",
        api_version="2024-01-01"
    ),
    members=[
        research_agent,
        writer_agent,
        editor_agent,
        personalisation_agent,
    ],
    instructions=["you are a newletter company Name:- ExpressNews and you are going to write a detailed newsletter for 3-4 lines about every latest news in the world",
                  "Don't add date in the newsletter",
                  "Search for the latest news in the world",
                  "Write a newsletter about the latest news in the world",
                  "Proofread the newsletter and improve flow",
                  "Personalise the newsletter based on reader preferences (tech, politics, entertainment, etc.)",
                ],
    show_tool_calls=False,
    markdown=True,
    show_members_responses=False,
    debug_mode=False,
)

def main():
    agent_team.print_response(
        message="write a newsletter about the latest news in the world",
        stream=False,
        stream_intermediate_steps=False,
    )

if __name__ == "__main__":
    main()
