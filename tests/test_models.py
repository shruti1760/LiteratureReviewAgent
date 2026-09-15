from models.schemas import Paper


paper = Paper(
    title="Example Research Paper",
    authors=["Alice", "Bob"],
    publication_year=2025,
    abstract="This paper investigates an example problem.",
    research_problem="How can we solve the example problem?",
    methodology="Experimental approach",
    dataset="Example Dataset",
    key_findings="The proposed method improved performance.",
    limitations="The dataset was relatively small.",
)

print(paper)