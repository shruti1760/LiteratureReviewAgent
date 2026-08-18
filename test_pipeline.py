from dotenv import load_dotenv

load_dotenv()

import asyncio

from services.pdf_loader import extract_text_from_pdf
from services.text_chunker import chunk_text
from agents.reader import reader_agent


async def main():
    text = extract_text_from_pdf("papers\\Impact-of-PM-and-BM-on-Success.pdf")

    chunks = chunk_text(text)

    paper_context = "\n\n".join(
        f"--- Paper Chunk {i + 1} ---\n{chunk}"
        for i, chunk in enumerate(chunks)
    )

    prompt = f"""
    The following text contains multiple chunks from the SAME research paper.

    Read all chunks together and extract the information needed for the
    Paper structure.

    Do not treat each chunk as a separate paper.
    Do not invent information.

    PAPER CONTENT:

    {paper_context}
    """

    result = await reader_agent.run(prompt)

    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())