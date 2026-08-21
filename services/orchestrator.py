from agents.reader import reader_agent
from agents.analyzer import analyzer_agent
from services.pdf_loader import extract_text_from_pdf
from services.text_chunker import chunk_text


class LiteratureReviewOrchestrator:

    async def run_reader(self, prompt: str):
        try:
            return await reader_agent.run(prompt)

        except Exception as e:
            print(f"Reader failed: {e}")
            print("Retrying Reader Agent...")
            return await reader_agent.run(prompt)

    async def analyze_paper(self, file_path: str):

        # 1. Extract text from the PDF
        text = extract_text_from_pdf(file_path)

        # 2. Split the paper into chunks
        chunks = chunk_text(text)

        # 3. Prepare the chunks for the Reader
        paper_context = "\n\n".join(
            f"--- Paper Chunk {i + 1} ---\n{chunk}"
            for i, chunk in enumerate(chunks)
        )

        # 4. Ask Reader Agent to extract structured information
        reader_prompt = f"""
        The following text contains multiple chunks from the SAME research paper.

        Extract the information required for the Paper structure.

        Do not invent information.

        PAPER CONTENT:

        {paper_context}
        """

        reader_result = await self.run_reader(reader_prompt)

        paper = reader_result.output

        # 5. Send the structured Paper to the Analyzer
        analyzer_prompt = f"""
        Analyze the following research paper.

        PAPER:
        {paper.model_dump_json(indent=2)}
        """

        analyzer_result = await analyzer_agent.run(analyzer_prompt)

        return paper, analyzer_result.output