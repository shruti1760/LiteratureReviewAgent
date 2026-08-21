# Literature Review Agent

A Python prototype that extracts structured information from research-paper PDFs and analyzes the extracted paper with Google Gemini through PydanticAI.

## What Works

The current implementation supports one paper at a time:

1. Extract text from a PDF with PyMuPDF.
2. Split the text into 6,000-character chunks.
3. Send the combined paper context to the Reader agent.
4. Validate the response against the `Paper` Pydantic schema.
5. Send the structured paper to the Analyzer agent.

The Reader-only pipeline writes its result to `paper_output.json`. Literature-review writing, planning, and multi-paper synthesis are not implemented yet.

## Architecture

```text
PDF
 |
 +--> services.pdf_loader.extract_text_from_pdf
 |
 +--> services.text_chunker.chunk_text
 |
 +--> agents.reader.reader_agent --> Paper
                                |
                                +--> agents.analyzer.analyzer_agent --> AnalysisResult
```

`services.orchestrator.LiteratureReviewOrchestrator.analyze_paper()` runs the full Reader-to-Analyzer flow. `test_pipeline.py` runs the Reader-only flow and saves JSON output.

## Requirements

- Python 3.10+
- A Google Gemini API key
- A PDF in the `papers/` directory

The repository currently has no pinned dependencies in `requirements.txt`. Install the packages used by the source before running it:

```bash
python -m pip install pydantic pydantic-ai pymupdf python-dotenv
```

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_api_key
```

Do not commit `.env` or API keys.

## Run It

Create and activate a virtual environment first:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Run Reader extraction for the sample PDF:

```bash
python test_pipeline.py
```

The sample path is documented as `papers/sample.pdf` to keep the example filename generic. Update the hard-coded path in the script to match the PDF available in your local `papers/` directory. The output is saved to `paper_output.json`.

To run the Reader and Analyzer together:

```bash
python test_orchestrator.py
```

The orchestrator also uses the same hard-coded sample PDF path and prints the resulting `Paper` and `AnalysisResult` objects.

## Data Models

`models/schemas.py` defines two output models:

```python
class Paper(BaseModel):
    title: str
    authors: list[str]
    publication_year: int
    abstract: str
    research_problem: str
    methodology: str
    dataset: str
    key_findings: str
    limitations: str

class AnalysisResult(BaseModel):
    key_contribution: str
    strengths: list[str]
    weaknesses: list[str]
    research_gaps: list[str]
    relevance_to_topic: str
```

If information is missing from a paper, the agents are instructed to report that it is not provided rather than inventing it.

## Project Layout

```text
agents/       Reader and Analyzer agent definitions; Writer and Planner are empty placeholders
models/       Pydantic output schemas
services/     PDF extraction, text chunking, and orchestration
papers/       Input PDF files
test_*.py     Standalone scripts and tests for the current components
main.py       Empty placeholder entry point
paper_output.json  Example/generated Reader output
```

## Tests

Most test files are executable scripts rather than a configured pytest suite. Run the component checks individually, for example:

```bash
python test_models.py
python test_pdf.py
python test_chunker.py
python test_reader.py
python test_orchestrator.py
```

Tests that invoke an agent require a valid Gemini API key and may incur API usage. PDF-related checks require the sample PDF to be present.

## Development Status

### Completed Today

- Added the Analyzer agent, which returns `AnalysisResult` data for a structured paper.
- Added `LiteratureReviewOrchestrator.analyze_paper()` for the PDF-to-Reader-to-Analyzer workflow.
- Added retry behavior for Reader-agent failures in the orchestrator.
- Added tests for the `AnalysisResult` model, Analyzer agent, Reader-to-Analyzer flow, and orchestrator.
- Documented the sample PDF as the generic `papers/sample.pdf` path.

### Current Limitations

- Processing is limited to one PDF per run.
- `agents/writer.py` and `agents/planner.py` are still placeholders.
- Input paths are hard-coded in the example scripts.
- `requirements.txt` is not yet populated or pinned.
- Agent tests require a Gemini API key and may incur API usage.

### Next Steps

- Populate and pin `requirements.txt`.
- Make the input PDF configurable from the command line.
- Add multi-paper comparison and synthesis.
- Implement Writer and Planner agents.
- Expand end-to-end tests with mocked model responses.

## Contributing

This is an active development project. To contribute:

1. Create a feature branch
2. Make your changes with clear commit messages
3. Add tests for new functionality
4. Ensure all tests pass before committing

## Documentation

For more detailed information:
- **API Documentation** - See docstrings in `agents/` and `services/`
- **Schema Definitions** - See `models/schemas.py`
- **Example Papers** - Check `papers/` directory

## License

This project is licensed under the MIT License - see the [LICENSE] file for details.

## Author

Shruti Nair

## Support

For issues, questions, or suggestions, please create an issue or reach out.

---

**Last Updated:** 2026-08-21  
**Project Status:** Active Development  
**Current Phase:** Phase 1 - Reader, Analyzer, and Orchestrator
