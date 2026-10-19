# Interview Project Story — Agentic AI–Driven Contract Intelligence Platform

> **Important:** Use this as a project plan/story template until you have implemented and tested each feature. Do not claim production deployment, measured business impact, team leadership, or enterprise usage unless those are true.

## 1. Project overview

"I am building an Agentic AI–Driven Contract Intelligence Platform to help reviewers analyze contracts more consistently. The system extracts document text, identifies clauses that may need attention, links findings to page-level evidence, and generates a structured report for human review."

## 2. Business problem

"Manual contract review can be time-consuming, and important terms may be overlooked when reviewers handle many documents. The goal is to support reviewers by highlighting potentially important clauses and making the evidence easy to inspect. The tool is decision support, not an automated legal decision-maker."

## 3. Workflow

1. A user uploads a PDF contract.
2. The ingestion module validates the file and extracts text by page.
3. An extraction stage identifies contract entities, dates, obligations, and clauses.
4. A risk-analysis stage checks contract clauses against configured rules and review policies.
5. A policy-retrieval stage retrieves relevant internal guidance.
6. A validation stage checks the output schema, evidence, page references, and unsupported claims.
7. High-risk or uncertain results are routed to a human reviewer.
8. The system produces a report and records audit events.

## 4. Technology choices

- Python for application logic.
- PyMuPDF for PDF text extraction.
- Pydantic for structured output validation.
- Streamlit for the initial user interface.
- FastAPI for API integration in a later phase.
- LangGraph for explicit, testable workflow orchestration.
- Sentence Transformers and FAISS for a local policy-retrieval prototype.
- SQLite/PostgreSQL for persistence in later phases.
- Docker for reproducible packaging.

Only list components you have actually implemented when answering an interviewer about completed work.

## 5. Agent responsibilities

- **Extraction stage:** identifies parties, dates, obligations, and clause text.
- **Risk stage:** flags terms against explicit criteria and produces evidence-backed findings.
- **Policy stage:** retrieves the relevant review-policy passages.
- **Validation stage:** verifies schema, evidence references, and required fields; invalid results are retried or sent for human review.
- **Orchestrator:** controls order, state, errors, and approval gates.

These stages can be implemented as separate nodes; they do not need to be autonomous agents that freely message one another.

## 6. Risk scoring

"For the baseline, I use a transparent rule-based score to make behavior explainable. I would not interpret that score as a calibrated probability. To improve it, I would label a representative dataset with domain reviewers, compare predicted flags with reviewed labels, measure precision and recall, inspect false negatives, and tune the score against an agreed review policy."

## 7. Governance and reliability

- Preserve page references and evidence snippets for each finding.
- Reject malformed model outputs using a schema.
- Do not accept a risk claim without supporting contract text or a policy source.
- Keep a record of input file hash, run status, rule/model version, findings, reviewer decisions, and timestamps.
- Protect confidential contracts with authentication, authorization, encryption, secure secrets, limited retention, and access logs.
- Require human review for consequential legal interpretations.

## 8. Evaluation plan

Build a synthetic or appropriately authorized dataset with reviewer-labeled clauses. Report:
- Clause extraction precision/recall/F1.
- Risk category precision/recall and false-negative rate.
- Evidence citation correctness.
- Invalid-output rate.
- Average processing latency and cost per document.
- Reviewer acceptance/correction rate.

Do not invent numerical results. Add results only after running experiments.

## 9. Interview answer: "What was your contribution?"

"For this implementation, I worked on [list only the modules you personally built]. I designed the document ingestion flow, structured the analysis output, implemented the rule-based baseline, and tested the findings against sample contracts. My next steps are to add policy retrieval, controlled multi-stage orchestration, validation, and deployment."

Edit this answer to match your actual work.

## 10. Limitations and future work

- Scanned PDFs need OCR.
- Keyword rules can miss paraphrases and can create false positives.
- Legal interpretation depends on jurisdiction, context, and organizational policy.
- The score is not a legal-risk probability.
- A production system needs a reviewed evaluation set, security controls, auditability, monitoring, and human oversight.
