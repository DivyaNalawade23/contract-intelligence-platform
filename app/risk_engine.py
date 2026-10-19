import re

# This is a demo rule set, not legal advice or a substitute for an organization's policy.
RULES = [
    {
        "id": "R001",
        "title": "Potentially unlimited liability",
        "category": "Liability",
        "severity": "High",
        "patterns": [
            r"unlimited liability",
            r"liability shall be unlimited",
            r"without limitation of liability",
        ],
        "recommendation": "Ask an authorized reviewer to assess whether a reasonable liability cap is needed.",
    },
    {
        "id": "R002",
        "title": "Automatic renewal",
        "category": "Renewal",
        "severity": "Medium",
        "patterns": [
            r"automatically renew",
            r"automatic renewal",
            r"renewal term",
        ],
        "recommendation": "Verify the renewal term, notice deadline, and reminder process.",
    },
    {
        "id": "R003",
        "title": "Potentially missing data-breach notification terms",
        "category": "Data protection",
        "severity": "High",
        "patterns": [
            r"data breach",
            r"security incident",
            r"personal data breach",
        ],
        "recommendation": "Check whether the contract defines notification timing, responsibilities, and escalation.",
    },
    {
        "id": "R004",
        "title": "Termination clause present",
        "category": "Termination",
        "severity": "Low",
        "patterns": [
            r"terminate this agreement",
            r"termination for convenience",
            r"terminate the agreement",
        ],
        "recommendation": "Review termination rights, notice periods, and post-termination obligations.",
    },
    {
        "id": "R005",
        "title": "Indemnification clause",
        "category": "Indemnity",
        "severity": "Medium",
        "patterns": [
            r"indemnify",
            r"indemnification",
            r"hold harmless",
        ],
        "recommendation": "Review the scope of indemnity, covered losses, exclusions, and any liability cap.",
    },
    {
        "id": "R006",
        "title": "Confidentiality clause present",
        "category": "Confidentiality",
        "severity": "Low",
        "patterns": [
            r"confidential information",
            r"confidentiality obligations",
        ],
        "recommendation": "Check duration, exclusions, permitted disclosures, and handling obligations.",
    },
]

SEVERITY_POINTS = {"Low": 5, "Medium": 15, "High": 25}


def analyze_contract(pages: list[dict]) -> dict:
    """Find rule-triggering phrases and attach page-level evidence snippets."""
    findings = []
    for rule in RULES:
        matches = []
        for page in pages:
            page_text = page.get("text", "")
            for pattern in rule["patterns"]:
                for match in re.finditer(pattern, page_text, flags=re.IGNORECASE):
                    start = max(0, match.start() - 100)
                    end = min(len(page_text), match.end() + 140)
                    snippet = re.sub(r"\s+", " ", page_text[start:end]).strip()
                    matches.append({
                        "page": page["page"],
                        "matched_text": match.group(0),
                        "evidence": snippet,
                    })
                    break
            if matches and matches[-1]["page"] == page["page"]:
                # One evidence snippet per rule per page is enough for this MVP.
                continue

        if matches:
            findings.append({
                "rule_id": rule["id"],
                "title": rule["title"],
                "category": rule["category"],
                "severity": rule["severity"],
                "status": "Flagged for review",
                "evidence": matches[:5],
                "recommendation": rule["recommendation"],
            })

    # Transparent demo score: sum severity weights, capped at 100.
    # This is not a statistically validated probability of legal risk.
    raw_score = sum(SEVERITY_POINTS[item["severity"]] for item in findings)
    score = min(100, raw_score)
    if score >= 50:
        overall = "High"
    elif score >= 20:
        overall = "Medium"
    else:
        overall = "Low"

    return {
        "overall_risk": overall,
        "risk_score": score,
        "findings_count": len(findings),
        "findings": findings,
        "scoring_note": (
            "Demo heuristic score based on detected rule severity. It is not a legal opinion, "
            "a calibrated probability, or a validated business KPI."
        ),
    }
