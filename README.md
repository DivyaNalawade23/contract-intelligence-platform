# Agentic AI–Driven Contract Intelligence Platform

A learning project for contract document processing, risk flagging, evidence traceability, agent orchestration, RAG, validation, and deployment.

## Current status

**Phase 1 MVP only.** The current app extracts text from text-based PDFs and runs a small, transparent rule set. It does **not** yet contain LLM-powered agents, RAG, authentication, database persistence, or production security controls.

The heuristic score is illustrative and is not a legal-risk probability. Findings must be reviewed by a qualified person.

## Requirements

- Python 3.10+ (recommended)
- VS Code or another Python IDE

## Run on Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run main.py
```

If activation is blocked, run the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run main.py
```

Open the local URL printed by Streamlit and upload a text-based PDF. Scanned PDFs need OCR, which is not yet included.

## Tests

```powershell
pytest -q
```

## Architecture plan

1. Document ingestion and page-level text extraction
2. Clause extraction with structured Pydantic schemas
3. Risk analysis with evidence and page references
4. Policy RAG (embeddings + FAISS)
5. LangGraph workflow: extraction -> risk -> policy retrieval -> validation
6. Human review for high-severity or uncertain findings
7. FastAPI endpoints and Streamlit UI
8. Database persistence, audit events, access control and tests
9. Docker packaging and cloud deployment

## Suggested next steps

- Add OCR for scanned contracts.
- Create a synthetic contract dataset with expected findings.
- Measure precision, recall, false positives and false negatives against reviewed labels.
- Add policy retrieval and LLM analysis only after the baseline is tested.
- Add authentication, authorization, encryption, secret management, retention rules, and security review before using confidential contracts.
