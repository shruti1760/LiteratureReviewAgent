from dotenv import load_dotenv

load_dotenv()

import asyncio

from services.orchestrator import LiteratureReviewOrchestrator


async def main():
    orchestrator = LiteratureReviewOrchestrator()

    paper, analysis = await orchestrator.analyze_paper(
        "papers/Impact-of-PM-and-BM-on-Success.pdf"
    )

    print("\n===== PAPER =====")
    print(paper)

    print("\n===== ANALYSIS =====")
    print(analysis)


if __name__ == "__main__":
    asyncio.run(main())