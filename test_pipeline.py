from dotenv import load_dotenv
import asyncio

load_dotenv(".env")

from services.pdf_loader import extract_text_from_pdf
from agents.reader import reader_agent


async def main():
    text = extract_text_from_pdf("papers\\294_Final.pdf")

    result = await reader_agent.run(text)

    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())