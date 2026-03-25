def validate_response(actual, expected):
    result = {}

    answer = actual.get("answer", "").lower()
    escalation = actual.get("escalation", "").upper()

    # Detect API failure
    api_failed = "httpconnectionpool" in answer or "error" in answer

    result["api_success"] = not api_failed

    if api_failed:
        result["issue_match"] = False
        result["escalation_match"] = False
        result["no_hallucination"] = False
        return result

    # Normal validation
    result["issue_match"] = expected["expected_issue"] in answer
    result["escalation_match"] = expected["expected_escalation"] == escalation
    result["no_hallucination"] = "unknown" not in answer

    return result