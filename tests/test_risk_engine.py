from app.risk_engine import analyze_contract


def test_unlimited_liability_is_flagged():
    result = analyze_contract([
        {"page": 1, "text": "The supplier has unlimited liability under this agreement."}
    ])
    assert any(item["rule_id"] == "R001" for item in result["findings"])


def test_empty_text_has_no_findings():
    result = analyze_contract([{"page": 1, "text": "A simple document with no known trigger phrases."}])
    assert result["findings_count"] == 0
    assert result["risk_score"] == 0
