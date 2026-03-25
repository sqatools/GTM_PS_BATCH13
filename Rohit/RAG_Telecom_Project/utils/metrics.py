def calculate_metrics(results):
    total = len(results)

    issue_pass = sum(1 for r in results if r["issue_match"])
    escalation_pass = sum(1 for r in results if r["escalation_match"])
    no_hallucination_pass = sum(1 for r in results if r["no_hallucination"])

    return {
        "issue_accuracy": issue_pass / total,
        "escalation_accuracy": escalation_pass / total,
        "hallucination_score": no_hallucination_pass / total
    }