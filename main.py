import json
import streamlit as st
from app.analyzer import analyze_pdf

st.set_page_config(
    page_title="Contract Intelligence Platform",
    page_icon="📄",
    layout="wide",
)

st.title("Agentic AI–Driven Contract Intelligence Platform")
st.caption(
    "Contract review assistant: PDF text extraction, risk analysis, "
    "and evidence-backed findings."
)

with st.sidebar:
    st.header("About this demo")
    st.write(
        "This application analyzes contracts using rule-based analysis "
        "or Azure OpenAI when configured. All findings require human review."
    )
    st.warning("Not legal advice. Have a qualified reviewer assess all findings.")

uploaded = st.file_uploader(
    "Upload a text-based contract PDF",
    type=["pdf"],
)

# Clear old results when a different PDF is uploaded.
if uploaded:
    upload_key = f"{uploaded.name}:{uploaded.size}"

    if st.session_state.get("upload_key") != upload_key:
        st.session_state["upload_key"] = upload_key
        st.session_state.pop("analysis_result", None)
else:
    st.session_state.pop("upload_key", None)
    st.session_state.pop("analysis_result", None)

if uploaded:
    if uploaded.size > 15 * 1024 * 1024:
        st.error("File is larger than the 15 MB demo limit.")
        st.stop()

    if st.button("Analyze contract", type="primary"):
        with st.spinner("Extracting text and analyzing the contract..."):
            try:
                result = analyze_pdf(
                    uploaded.getvalue(),
                    uploaded.name,
                )
                st.session_state["analysis_result"] = result

            except ValueError as exc:
                st.error(str(exc))

            except Exception as exc:
                print(
                    f"Contract analysis failed: "
                    f"{type(exc).__name__}: {exc}"
                )
                st.error(
                    "Contract analysis failed. Check the terminal logs "
                    "and verify your configuration."
                )

# Display the analysis.
result = st.session_state.get("analysis_result")

if result:
    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Pages",
        result.get("page_count", "—"),
    )

    col2.metric(
        "Findings",
        result.get(
            "findings_count",
            len(result.get("findings", [])),
        ),
    )

    risk_score = result.get("risk_score")

    col3.metric(
        "Demo risk score",
        f"{risk_score}/100" if risk_score is not None else "N/A",
        result.get("overall_risk", ""),
    )

    st.caption(
        f'Analysis mode: {result.get("analysis_mode", "Unknown")}'
    )

    # Contract summary.
    if result.get("summary"):
        st.subheader("Contract Summary")
        st.write(result["summary"])

    if result.get("contract_type"):
        st.write(
            "**Contract type:**",
            result["contract_type"],
        )

    if result.get("parties"):
        st.write(
            "**Parties:**",
            ", ".join(result["parties"]),
        )

    # Dates and deadlines.
    if result.get("key_dates"):
        st.subheader("Key Dates and Deadlines")

        for date_item in result["key_dates"]:
            st.write(f"- {date_item}")

    # Limitations.
    if result.get("limitations"):
        with st.expander("Limitations and items to verify"):
            for item in result["limitations"]:
                st.write(f"- {item}")

    # Evidence validation warning.
    rejected_count = result.get("rejected_evidence_count", 0)

    if rejected_count > 0:
        st.warning(
            f"{rejected_count} finding(s) were omitted because "
            "their quoted evidence could not be verified."
        )

    # Findings — displayed regardless of rejected evidence.
    st.subheader("Findings Requiring Review")

    findings = result.get("findings", [])

    if not findings:
        st.success(
            "No findings were returned. This does not prove "
            "that the contract is risk-free."
        )

    for finding in findings:
        severity = finding.get("severity", "Unspecified")
        title = finding.get("title", "Untitled finding")
        category = finding.get("category", "Uncategorized")

        with st.expander(
            f"{severity} · {title} ({category})",
            expanded=True,
        ):
            if finding.get("status"):
                st.write(f'**Status:** {finding["status"]}')

            if finding.get("rationale"):
                st.write(
                    f'**Why it was flagged:** {finding["rationale"]}'
                )

            if finding.get("recommendation"):
                st.write(
                    f'**Suggested review:** '
                    f'{finding["recommendation"]}'
                )

            evidence_items = finding.get("evidence", [])

            if evidence_items:
                st.write("**Evidence from the contract**")

                for evidence in evidence_items:
                    page = evidence.get(
                        "page",
                        evidence.get("page_number", "?"),
                    )

                    matched_text = evidence.get("matched_text")
                    quote = evidence.get(
                        "evidence",
                        evidence.get("evidence_quote", ""),
                    )

                    if matched_text:
                        st.caption(
                            f'Page {page} · matched: "{matched_text}"'
                        )
                    else:
                        st.caption(f"Page {page}")

                    if quote:
                        st.write(f"> {quote}")

            elif finding.get("evidence_quote"):
                st.caption(
                    f'Page {finding.get("page_number", "?")}'
                )
                st.write(f'> {finding["evidence_quote"]}')

            else:
                st.caption(
                    "No evidence quote was supplied for this finding."
                )

    # Risk-score explanation.
    if result.get("scoring_note"):
        st.info(result["scoring_note"])
    else:
        st.caption(
            "The displayed score is a demo heuristic, "
            "not a probability of legal risk."
        )

    # Download analysis as JSON.
    downloadable = {
        key: value
        for key, value in result.items()
        if key not in {"extracted_text", "api_key", "client"}
    }

    st.download_button(
        label="Download analysis JSON",
        data=json.dumps(
            downloadable,
            indent=2,
            ensure_ascii=False,
        ),
        file_name="contract_analysis.json",
        mime="application/json",
    )

    # Extracted document text.
    if result.get("extracted_text"):
        with st.expander("View extracted text"):
            st.text(result["extracted_text"])
            