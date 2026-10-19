# Agentic AI–Driven Contract Intelligence Platform


# Agentic AI–Driven Contract Intelligence Platform

An AI-focused learning and portfolio project for contract document processing, risk flagging, evidence traceability, policy retrieval, agent orchestration, and deployment.

> **Current status: Phase 1 MVP.** The current implementation extracts text from text-based PDF contracts and applies a small, transparent rule-based engine to flag selected clauses for review. LLM-powered analysis, multi-agent orchestration, RAG, database persistence, authentication, and production security controls are planned enhancements and should not be considered implemented unless present in the code.

## Current Features

- Upload text-based contract PDFs through a Streamlit interface.
- Extract text from contract documents.
- Apply deterministic rules to identify selected potential risk indicators.
- Display findings and supporting evidence for human review.
- Show an illustrative demo risk score.
- Download analysis results as JSON.
- Display limitations and items requiring further verification.

## Technology Stack

**Current MVP**
- Python
- Streamlit
- PDF text extraction libraries
- Rule-based text analysis
- JSON

**Planned Technologies**
- Pydantic for structured data validation
- Azure OpenAI for LLM-powered contract analysis
- Embeddings and FAISS for Retrieval-Augmented Generation (RAG)
- LangGraph for workflow orchestration
- FastAPI for REST APIs
- Database storage and audit logging
- Docker and cloud deployment

> Planned technologies are part of the roadmap and may not yet be implemented in the current version.

## Requirements

- Python 3.10 or newer
- VS Code or another Python IDE
- Git (optional)
- Dependencies listed in `requirements.txt`

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/contract-intelligence-platform.git
cd contract-intelligence-platform
```

Replace `YOUR-USERNAME` with your GitHub username and use your actual repository URL.

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked, use the environment's Python executable directly.

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Run the application

```powershell
python -m streamlit run main.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`, and upload a text-based PDF contract.

If PowerShell activation is blocked, install and run without activating:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run main.py
```

## How It Works

1. The user uploads a contract PDF.
2. The application extracts text from the document.
3. A rule-based engine checks the extracted text for selected risk indicators.
4. The application displays findings and available supporting evidence.
5. The user reviews the findings and can download the analysis as JSON.

The actual workflow depends on the code currently implemented in the repository.

## Example Risk Indicators

Depending on the rules implemented, the application may flag clauses relating to:

- Unlimited liability
- Automatic contract renewal
- Data security and breach notification
- Confidentiality obligations
- Indemnification
- Termination conditions

These are examples of clauses worth reviewing, not automatic proof of legal risk.

## Project Roadmap

The following capabilities are planned development phases.

### Phase 1: Document Processing and Rule-Based Analysis
- PDF text extraction
- Basic rule-based risk flagging
- Evidence display
- Streamlit interface
- JSON export

### Phase 2: LLM-Powered Contract Analysis
- Structured contract summaries
- Clause classification and extraction
- Evidence-backed findings
- Azure OpenAI integration
- Output validation

### Phase 3: Policy RAG
- Build a policy document knowledge base
- Generate embeddings
- Retrieve relevant policy passages using FAISS
- Compare contract clauses against policy requirements
- Display supporting policy references

### Phase 4: Agentic Workflow
- Orchestrate extraction, risk analysis, policy retrieval, and validation with LangGraph
- Define clear responsibilities for each workflow stage
- Add error handling and retry logic
- Route uncertain findings to human reviewers

### Phase 5: API and Deployment
- Add FastAPI endpoints
- Containerize the application with Docker
- Configure cloud deployment
- Add automated testing and CI/CD

### Phase 6: Governance and Evaluation
- Add authentication and role-based access control
- Implement audit logging and database persistence
- Establish retention and deletion policies
- Evaluate precision, recall, false positives, and false negatives against reviewed examples
- Conduct privacy and security reviews

## Testing

If tests are available, run:

```powershell
python -m pytest -q
```

A future evaluation dataset should contain synthetic contracts with expected findings reviewed by a qualified person. This will help measure the quality and limitations of the rule-based engine and future AI components.

## Security Considerations

Before using real or confidential contracts, the application requires appropriate security and privacy controls, including:

- Authentication and authorization
- Encryption in transit and at rest
- Secure API key and secret management
- Input validation and upload limits
- Controlled logging and access to contract data
- Data retention and deletion procedures
- Human review of material legal-risk findings

Never commit `.env` files, API keys, credentials, confidential contracts, or other sensitive information to GitHub. Keep local secrets out of version control and use placeholder values in `.env.example`.

## Limitations

- The current MVP uses a limited set of deterministic rules.
- Scanned PDFs require OCR, which is not included unless separately implemented.
- Rules may miss relevant clauses or flag harmless language.
- The demo risk score is illustrative, not a calibrated probability of legal risk.
- Accuracy and business impact have not been established without a formal evaluation.
- The current MVP is not a production-ready legal analysis system.

## Disclaimer

This project is for educational and demonstration purposes only. It does not provide legal advice and must not replace review by a qualified legal professional.
