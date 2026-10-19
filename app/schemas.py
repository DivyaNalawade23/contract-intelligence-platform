from typing import Literal
from pydantic import BaseModel, Field


class ContractFinding(BaseModel):
    title: str = Field(
        description="Short name of the contract issue"
    )

    category: str = Field(
        description="Liability, Renewal, Data protection, Payment, etc."
    )

    severity: Literal["Low", "Medium", "High"] = Field(
        description="Review priority, not a legal conclusion"
    )

    rationale: str = Field(
        description="Why this clause may need human review"
    )

    evidence_quote: str = Field(
        description="Exact short quote copied from the contract"
    )

    page_number: int = Field(
        description="One-based page number containing the quote"
    )

    recommendation: str = Field(
        description="Suggested next step for a qualified reviewer"
    )


class ContractAnalysis(BaseModel):
    contract_type: str
    parties: list[str]
    key_dates: list[str]
    summary: str
    findings: list[ContractFinding]
    limitations: list[str]