from dotenv import load_dotenv

load_dotenv(".env")

import asyncio

from agents.analyzer import analyzer_agent
from models.schemas import Paper


paper = Paper(
    title="Example Research Paper",
    authors=["Alice Smith", "Bob Jones"],
    publication_year=2025,
    abstract="This paper proposes an efficient image classification method.",
    research_problem="Improving image classification efficiency.",
    methodology="A lightweight CNN was compared with baseline models.",
    dataset="CIFAR-10",
    key_findings="The proposed model achieved competitive accuracy with fewer parameters.",
    limitations="The evaluation used a limited number of datasets.",
)


async def main():
    result = await analyzer_agent.run(
        f"""
        Analyze the following research paper:

        {paper.model_dump_json(indent=2)}
        """
    )

    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())