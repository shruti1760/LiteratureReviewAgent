from pydantic_ai import Agent

from models.schemas import Paper


reader_agent = Agent(
    "google:gemini-3.5-flash",
    output_type=Paper,
    system_prompt="""
    You are a research paper reader.

    Extract the important information from the provided research paper
    and return it in the required Paper structure.

    Do not invent information.
    If a field is not available in the paper, clearly indicate that it
    is not provided.
    """,
)