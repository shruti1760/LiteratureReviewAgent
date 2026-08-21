from models.schemas import AnalysisResult


analysis = AnalysisResult(
    key_contribution="Introduces an improved approach to the research problem.",
    strengths=[
        "Clear methodology",
        "Good experimental evaluation",
    ],
    weaknesses=[
        "Limited dataset",
        "Small evaluation scope",
    ],
    research_gaps=[
        "Needs validation on larger datasets",
    ],
    relevance_to_topic="Highly relevant to the research topic.",
)

print(analysis)