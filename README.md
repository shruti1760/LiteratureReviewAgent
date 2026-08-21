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

The sample path is currently hard-coded as `papers/sample.pdf`. The output is saved to `paper_output.json`.

To run the Reader and Analyzer together:

```bash
python test_orchestrator.py
```

The orchestrator also uses the same hard-coded sample PDF and prints the resulting `Paper` and `AnalysisResult` objects.

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

Implemented: PDF text extraction, fixed-size chunking, Reader extraction, Analyzer output schema, orchestration, and sample JSON output.

Planned: configurable input paths, dependency pinning, multi-paper comparison, Writer output generation, and Planner workflow support.
- 📋 Planner agent (planned)
- 📋 Orchestrator service (planned)
- 📋 End-to-end pipeline integration (planned)

### Roadmap

**Phase 1 - Core Pipeline** (Current)
- [x] PDF loading and text extraction
- [x] Text chunking for optimal processing
- [x] Reader agent implementation
- [X] Complete Analyzer agent implementation
- [ ] Complete Writer agent implementation
- [ ] Complete Planner agent implementation
- [ ] Implement Orchestrator service
- [ ] End-to-end integration testing

**Phase 2 - Enhancement**
- [ ] Add support for batch processing multiple papers
- [ ] Implement paper similarity detection
- [ ] Add research gap identification
- [ ] Create visualization tools for paper relationships
- [ ] Support for additional document formats (DOCX, TXT)

**Phase 3 - Production Ready**
- [ ] Add error handling & retry logic
- [ ] Implement caching mechanisms
- [ ] Add logging & monitoring
- [ ] Create CLI interface
- [ ] Build REST API wrapper
- [ ] Add database integration for paper storage

## Configuration

### Environment Variables

```env
# API Configuration
GEMINI_API_KEY=your_api_key_here

# Optional Settings
LOG_LEVEL=INFO
MAX_PAPERS_BATCH=10
CACHE_RESULTS=true
```

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
**Project Status:** Active Development 🚀  
**Current Phase:** Phase 1 - Core Pipeline (Reader Agent Complete)
