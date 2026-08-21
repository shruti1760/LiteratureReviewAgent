from dotenv import load_dotenv

load_dotenv()

import asyncio

from services.pdf_loader import extract_text_from_pdf
from services.text_chunker import chunk_text
from agents.reader import reader_agent
from agents.analyzer import analyzer_agent


async def main():
    # 1. Read PDF
    text = extract_text_from_pdf(
        "papers/Impact-of-PM-and-BM-on-Success.pdf"
    )

    # 2. Split into chunks
    chunks = chunk_text(text)

    paper_context = "\n\n".join(
        f"--- Paper Chunk {i + 1} ---\n{chunk}"
        for i, chunk in enumerate(chunks)
    )

    # 3. Reader extracts structured information
    reader_prompt = f"""
    The following text contains multiple chunks from the SAME research paper.

    Extract the information required for the Paper structure.

    Do not invent information.

    PAPER CONTENT:

    {paper_context}
    """

    reader_result = await reader_agent.run(reader_prompt)

    paper = reader_result.output

    print("\n===== READER OUTPUT =====")
    print(paper)

    # 4. Analyzer receives the Reader's output
    analyzer_prompt = f"""
    Analyze the following research paper.

    PAPER:
    {paper.model_dump_json(indent=2)}
    """

    analyzer_result = await analyzer_agent.run(analyzer_prompt)

    print("\n===== ANALYZER OUTPUT =====")
    print(analyzer_result.output)


if __name__ == "__main__":
    asyncio.run(main())