def validate_response(query, response):
    return {
        "correctness": "restart" in response.lower() or "internet" in response.lower(),
        "relevance": "billing" not in response.lower(),
        "completeness": len(response) > 20,
        "clarity": True,
        "no_hallucination": "unknown data" not in response.lower()
    }