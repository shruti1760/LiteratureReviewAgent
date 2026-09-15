# Literature Review Agent

A Python prototype for turning a research-paper PDF into structured metadata and a short analysis using Google Gemini through PydanticAI.

## Overview

This project reads a PDF, chunks the extracted text, sends the combined paper context to a reader agent, validates the resulting structured object against a Pydantic schema, and then passes that structured paper to an analyzer agent.

The current workflow is focused on a single paper at a time and is designed for literature review support rather than full multi-paper synthesis.

## What the project does

1. Extracts text from a PDF using PyMuPDF.
2. Splits the raw text into chunks of roughly 6,000 characters.
3. Combines the chunks into a single paper prompt.
4. Uses a Gemini-backed `Reader` agent to extract fields into a `Paper` model.
5. Uses a Gemini-backed `Analyzer` agent to summarize contribution, strengths, weaknesses, gaps, and relevance.
6. Returns the structured paper and analysis objects for inspection or downstream workflows.

## Architecture

```text
PDF file
  |
  v
services/pdf_loader.py -> extract_text_from_pdf()
  |
  v
services/text_chunker.py -> chunk_text()
  |
  v
agents/reader.py -> reader_agent -> Paper
  |
  +--> services/orchestrator.py -> LiteratureReviewOrchestrator.analyze_paper()
           |
           v
         agents/analyzer.py -> analyzer_agent -> AnalysisResult
```

The orchestrator is the main entry point for the full pipeline and is responsible for the Reader-to-Analyzer flow.

## Project structure

```text
agents/
  analyzer.py      Gemini-based analysis agent
  reader.py        Gemini-based extraction agent
  planner.py       Placeholder for future planning logic
  writer.py        Placeholder for future writing logic

models/
  schemas.py       Pydantic models for Paper and AnalysisResult

services/
  orchestrator.py   End-to-end single-paper workflow
  pdf_loader.py    PDF text extraction
  text_chunker.py  Chunking logic for long documents

tests/
  test_analysis_model.py
  test_analyzer.py
  test_chunker.py
  test_models.py
  test_orchestrator.py
  test_pdf.py
  test_pipeline.py
  test_reader_analyzer.py
  test_reader.py

main.py            Placeholder application entry point
requirements.txt   Dependency list (currently to be populated)
paper_output.json  Example output from the Reader pipeline
papers/            Input PDFs
LICENSE            MIT license
README.md          Project documentation
```

## Requirements

- Python 3.10+
- A Google Gemini API key
- A PDF in the `papers/` directory

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` is not populated yet, install the packages used by the current code manually:

```bash
python -m pip install pydantic pydantic-ai pymupdf python-dotenv
```

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_api_key
```

Do not commit `.env` files or API keys.

## Data models

The core output schema is defined in `models/schemas.py`:

```python
class Paper(BaseModel):
    title: str
    authors: List[str]
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

The reader agent is instructed not to invent missing information and to explicitly note when a field is not available.

## Setup

Create and activate a virtual environment:

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

Then install dependencies and set your environment variables.

## Running the app

### Reader-only pipeline

The Reader pipeline extracts structured data from a PDF and saves it as JSON:

```bash
python tests/test_pipeline.py
```

This script currently reads a hard-coded PDF path similar to:

```text
papers/Impact-of-PM-and-BM-on-Success.pdf
```

The output is written to `paper_output.json`.

### Full paper analysis flow

The orchestrator runs the full workflow:

```bash
python tests/test_orchestrator.py
```

This executes:

- PDF extraction
- chunking
- Reader extraction
- Analyzer evaluation
- console output for both the `Paper` and `AnalysisResult` objects

## Test workflow

The repository includes several test files under `tests/`. Most are direct Python scripts, and some require a valid Gemini API key.

Examples:

```bash
python tests/test_pdf.py
python tests/test_chunker.py
python tests/test_reader.py
python tests/test_orchestrator.py
```

If `pytest` is installed, the suite can also be run with:

```bash
pytest
```

> Note: Tests that call an LLM require a valid Gemini API key and may consume API quota.

## Current status

### Completed

- PDF text extraction via PyMuPDF
- Text chunking for long research papers
- Reader agent for structured extraction
- Analyzer agent for contribution and relevance analysis
- Orchestrator for the end-to-end single-paper workflow
- Model validation with Pydantic
- Basic test coverage for the main components

### Current limitations

- Only one paper is processed per run.
- Input paths are hard-coded in the example scripts.
- The `planner.py` and `writer.py` components are still placeholders.
- Multi-paper synthesis and comparison are not yet implemented.
- `requirements.txt` is not fully populated or pin-versioned yet.

### Planned next steps

- Add configurable PDF input and CLI arguments
- Populate and pin dependency versions
- Implement the planner and writer agents
- Support comparison across multiple papers
- Add more robust end-to-end tests and mocked AI responses

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributor

Shruti Nair

---

Last updated: 2026-09-15
