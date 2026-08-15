# 📚 Literature Review Agent

An intelligent, agentic literature review assistant built with **PydanticAI** that automates the extraction, analysis, and synthesis of research papers into structured literature reviews.

## 🎯 Overview

Literature Review Agent is a multi-agent system designed to streamline academic research workflows by automatically processing research papers and generating comprehensive literature reviews. The system leverages large language models to understand research content, extract key insights, identify patterns, and synthesize findings across multiple papers.

## ✨ Features & Goals

The Literature Review Agent is designed to:

- **📖 Extract Structured Information** - Automatically parse research papers and extract key metadata (title, authors, abstract, methodology, findings, etc.)
- **🔍 Analyze Research Papers** - Identify similarities, differences, research gaps, and emerging themes across papers
- **📝 Generate Literature Reviews** - Synthesize extracted information into coherent, well-organized literature reviews
- **🎯 Interpret Review Tasks** - Understand user requirements for literature review generation
- **🔗 Track Research Connections** - Build knowledge graphs showing relationships between papers and research areas

## 🏗️ Architecture

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
| **Reader** | ✅ Active | Extract structured information from research papers |
| **Analyzer** | 🚧 In Progress | Compare papers, identify gaps, analyze trends |
| **Writer** | 🚧 In Progress | Generate formatted literature review documents |
| **Planner** | 🚧 In Progress | Plan and orchestrate the review workflow |

## 📁 Project Structure

```
LiteratureReviewAgent/
├── agents/                 # AI agent implementations
│   ├── reader.py          # Extract paper information (Google Gemini)
│   ├── analyzer.py        # Analyze and compare papers
│   ├── writer.py          # Generate literature review output
│   └── planner.py         # Plan review workflow
├── services/              # Business logic & utilities
│   ├── pdf_loader.py      # PDF extraction & text parsing
│   └── orchestrator.py    # Coordinate multi-agent workflow
├── models/                # Data structures & schemas
│   └── schemas.py         # Pydantic models (Paper, Review, etc.)
├── papers/                # Sample research papers (PDF)
├── tests/                 # Test suite
│   ├── test_pipeline.py   # Integration tests
│   ├── test_reader.py     # Reader agent tests
│   ├── test_models.py     # Schema validation tests
│   └── test_pdf.py        # PDF loading tests
├── main.py/               # Entry point & configuration
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Project documentation
├── .env                   # Environment variables (API keys)
└── .venv/                 # Python virtual environment
```

## 🚀 Getting Started

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
pip install -r main.py/requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_api_key_here
```

### Usage

#### Extract Information from a Single Paper

```bash
python main.py
```

This will:
1. Load a PDF from `papers/` directory
2. Extract text content
3. Use the Reader agent to parse and structure the information
4. Output structured paper data

#### Example Code

```python
from services.pdf_loader import extract_text_from_pdf
from agents.reader import reader_agent
import asyncio

async def review_paper(pdf_path: str):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Process with Reader agent
    result = await reader_agent.run(text)
    
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

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **AI Framework** | [PydanticAI](https://docs.pydantic.dev/latest/api/pydantic_ai/) |
| **LLM** | Google Gemini 3.5 Flash |
| **Data Validation** | Pydantic v2 |
| **PDF Processing** | PyMuPDF (fitz) |
| **Async Runtime** | asyncio |
| **Environment Management** | python-dotenv |

## 📦 Dependencies

Key packages:
- **pydantic-ai** - Agentic AI framework
- **pydantic** - Data validation & serialization
- **pymupdf** - PDF text extraction
- **python-dotenv** - Environment variable management

See `main.py/requirements.txt` for complete dependency list.

## 🚧 Development Status

### Current Progress
- ✅ Project structure initialized
- ✅ PDF loading service implemented
- ✅ Reader agent (with Google Gemini integration) operational
- 🚧 Analyzer agent (in development)
- 🚧 Writer agent (in development)
- 🚧 Planner agent (in development)
- 🚧 Orchestrator service (in development)
- 🚧 End-to-end pipeline integration

### Roadmap

**Phase 1 - Core Pipeline** (Current)
- [ ] Complete Analyzer agent implementation
- [ ] Complete Writer agent implementation
- [ ] Complete Planner agent implementation
- [ ] Implement Orchestrator service

**Phase 2 - Enhancement**
- [ ] Add support for batch processing multiple papers
- [ ] Implement paper similarity detection
- [ ] Add research gap identification
- [ ] Create visualization tools for paper relationships

**Phase 3 - Production Ready**
- [ ] Add error handling & retry logic
- [ ] Implement caching mechanisms
- [ ] Add logging & monitoring
- [ ] Create CLI interface
- [ ] Build REST API wrapper
- [ ] Add database integration (optional)

## 🔧 Configuration

### Environment Variables

```env
# API Configuration
GEMINI_API_KEY=your_api_key_here

# Optional Settings
LOG_LEVEL=INFO
MAX_PAPERS_BATCH=10
CACHE_RESULTS=true
```

## 📝 Contributing

This is an active development project. To contribute:

1. Create a feature branch
2. Make your changes with clear commit messages
3. Add tests for new functionality
4. Ensure all tests pass before committing

## 📖 Documentation

For more detailed information:
- **API Documentation** - See docstrings in `agents/` and `services/`
- **Schema Definitions** - See `models/schemas.py`
- **Example Papers** - Check `papers/` directory

## ⚖️ License

[Add your license here]

## 👤 Author

[Add author information]

## 🤝 Support

For issues, questions, or suggestions, please create an issue or reach out.

---

**Last Updated:** 2026-08-15  
**Project Status:** Active Development 🚀
