import os

from dotenv import load_dotenv

from app.document_processor import extract_pdf_text
from app.risk_engine import analyze_contract
from app.azure_llm import analyze_with_azure

load_dotenv()


def analyze_pdf(
    pdf_bytes: bytes,
    filename: str = "contract.pdf",
) -> dict:

    extracted = extract_pdf_text(pdf_bytes)
    pages = extracted["pages"]

    use_azure = (
        os.getenv("USE_AZURE_LLM", "false")
        .strip()
        .lower()
        in {"1", "true", "yes"}
    )

    if use_azure:
        # If Azure fails, show the error instead of silently
        # pretending that the rule-based analyzer ran successfully.
        result = analyze_with_azure(pages)

    else:
        # Existing Phase 1 behavior.
        result = analyze_contract(pages)

        result["analysis_mode"] = "Phase 1 rule-based"
        result["contract_type"] = "Not extracted in rule-based mode"
        result["parties"] = []
        result["key_dates"] = []
        result["summary"] = "Rule-based keyword scan only."
        result["limitations"] = [
            "LLM analysis is disabled. Only predefined keyword rules ran."
        ]
        result["rejected_evidence_count"] = 0
        result["page_count"] = extracted["page_count"]

    result["filename"] = filename
    result["extracted_text"] = extracted["text"]

    return result