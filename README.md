# Literature Review Agent

An intelligent, agentic literature review assistant built with **PydanticAI** that automates the extraction, analysis, and synthesis of research papers into structured literature reviews.

## Overview

Literature Review Agent is a multi-agent system designed to streamline academic research workflows by automatically processing research papers and generating comprehensive literature reviews. The system leverages large language models to understand research content, extract key insights, identify patterns, and synthesize findings across multiple papers.

## Features & Goals

The Literature Review Agent is designed to:

- **Extract Structured Information** - Automatically parse research papers and extract key metadata (title, authors, abstract, methodology, findings, etc.)
- **Analyze Research Papers** - Identify similarities, differences, research gaps, and emerging themes across papers
- **Generate Literature Reviews** - Synthesize extracted information into coherent, well-organized literature reviews
- **Interpret Review Tasks** - Understand user requirements for literature review generation
- **Track Research Connections** - Build knowledge graphs showing relationships between papers and research areas

## Architecture

The system follows a modular pipeline architecture:

```
PDF Files
   ↓
PDF Loader Service
   ↓
Orchestrator Service
   ↓
Planner Agent (Plan review strategy)
   ↓
Reader Agent (Extract paper information)
   ↓
Analyzer Agent (Analyze & compare papers)
   ↓
Writer Agent (Generate literature review)
   ↓
Structured Literature Review
```

### Agent Roles

| Agent | Status | Responsibility |
|-------|--------|-----------------|
| **Reader** | ✅ Implemented | Extract structured information from research papers (Google Gemini) |
| **Analyzer** | 📋 Planned | Compare papers, identify gaps, analyze trends |
| **Writer** | 📋 Planned | Generate formatted literature review documents |
| **Planner** | 📋 Planned | Plan and orchestrate the review workflow |

## Project Structure

```
LiteratureReviewAgent/
├── agents/                 # AI agent implementations
│   ├── reader.py          # ✅ Extract paper information (Google Gemini)
│   ├── analyzer.py        # Analyze and compare papers (skeleton)
│   ├── writer.py          # Generate literature review output (skeleton)
│   └── planner.py         # Plan review workflow (skeleton)
├── services/              # Business logic & utilities
│   ├── pdf_loader.py      # ✅ PDF extraction & text parsing (PyMuPDF)
│   ├── text_chunker.py    # ✅ Text chunking for processing
│   └── orchestrator.py    # Coordinate multi-agent workflow (skeleton)
├── models/                # Data structures & schemas
│   └── schemas.py         # ✅ Pydantic models (Paper)
├── papers/                # Sample research papers (PDF)
├── test_pipeline.py       # ✅ Main pipeline integration tests (entry point)
├── test_reader.py         # Reader agent tests
├── test_models.py         # Schema validation tests
├── test_pdf.py            # PDF loading tests
├── test_chunker.py        # Text chunker tests
├── main.py                # Entry point (empty - use test_pipeline.py)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
└── .venv/                 # Python virtual environment
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip package manager
- A Google API key for Gemini (or other supported LLM)

### Installation

1. **Clone the repository** (or navigate to your project directory)

```bash
cd LiteratureReviewAgent
```

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_api_key_here
```

### Usage

#### Extract Information from a Single Paper

```bash
python test_pipeline.py
```

This will:
1. Load a PDF from `papers/` directory
2. Chunk the text content for optimal processing
3. Use the Reader agent (Google Gemini) to parse and structure the information
4. Output structured paper data as a `Paper` object

#### Example Code

```python
from services.pdf_loader import extract_text_from_pdf
from services.text_chunker import chunk_text
from agents.reader import reader_agent
import asyncio

async def review_paper(pdf_path: str):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Chunk text for better processing
    chunks = chunk_text(text)
    paper_context = "\n\n".join(
        f"--- Paper Chunk {i + 1} ---\n{chunk}"
        for i, chunk in enumerate(chunks)
    )
    
    # Process with Reader agent
    result = await reader_agent.run(paper_context)
    
    # Get structured paper information
    paper = result.output
    print(f"Title: {paper.title}")
    print(f"Authors: {paper.authors}")
    print(f"Year: {paper.publication_year}")
    print(f"Key Findings: {paper.key_findings}")
    
    return paper

# Run it
asyncio.run(review_paper("papers/sample.pdf"))
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest test_pipeline.py -v

# Run with coverage
pytest --cov=.
```

## 📊 Data Models

### Paper Schema

The system extracts and structures paper information using the `Paper` model:

```python
class Paper(BaseModel):
    title: str              # Paper title
    authors: List[str]      # List of author names
    publication_year: int   # Year of publication
    abstract: str          # Paper abstract
    research_problem: str  # Problem being addressed
    methodology: str       # Research methodology
    dataset: str           # Datasets used
    key_findings: str      # Main findings & conclusions
    limitations: str       # Acknowledged limitations
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **AI Framework** | [PydanticAI](https://docs.pydantic.dev/latest/api/pydantic_ai/) |
| **LLM** | Google Gemini 3.5 Flash |
| **Data Validation** | Pydantic v2 |
| **PDF Processing** | PyMuPDF (fitz) |
| **Async Runtime** | asyncio |
| **Environment Management** | python-dotenv |

## Dependencies

Key packages:
- **pydantic-ai** - Agentic AI framework with LLM integration
- **pydantic** - Data validation & serialization (v2)
- **pymupdf** - PDF text extraction and processing
- **python-dotenv** - Environment variable management
- **google-generativeai** - Google Gemini API integration (required for Reader agent)

See `requirements.txt` for the complete dependency list.

## Development Status

### Current Progress
- ✅ Project structure initialized
- ✅ PDF loading service implemented (PyMuPDF)
- ✅ Text chunking service implemented
- ✅ Reader agent with Google Gemini integration operational
- ✅ Pydantic models and schemas defined
- ✅ Test pipeline framework in place
- 📋 Analyzer agent (planned)
- 📋 Writer agent (planned)
- 📋 Planner agent (planned)
- 📋 Orchestrator service (planned)
- 📋 End-to-end pipeline integration (planned)

### Roadmap

**Phase 1 - Core Pipeline** (Current)
- [x] PDF loading and text extraction
- [x] Text chunking for optimal processing
- [x] Reader agent implementation
- [ ] Complete Analyzer agent implementation
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

**Last Updated:** 2026-08-18  
**Project Status:** Active Development 🚀  
**Current Phase:** Phase 1 - Core Pipeline (Reader Agent Complete)
