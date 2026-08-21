from pydantic_ai import Agent

from models.schemas import Paper, AnalysisResult


analyzer_agent = Agent(
    "google:gemini-3.5-flash",
    output_type=AnalysisResult,
    system_prompt="""
    You are a research paper analysis agent.

    Analyze the provided research paper information and identify:

    - The paper's main contribution
    - Its strengths
    - Its weaknesses
    - Potential research gaps
    - Its relevance to the research topic

    Base your analysis only on the information provided.
    Do not invent facts or unsupported claims.
    """,
)