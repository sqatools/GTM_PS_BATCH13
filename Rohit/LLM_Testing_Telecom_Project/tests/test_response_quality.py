from ..utils.llm_client import ask_llm
from ..utils.validators import (
    is_relevant,
    has_troubleshooting_steps,
    escalation_check,
    hallucination_check
)

def test_response_quality():
    query = "My Internet is down since morning"
    response = ask_llm(query)

    print("\nQuery:", query)
    print("Response:", response)

    relevance = is_relevant(response)
    troubleshooting = has_troubleshooting_steps(response)
    escalation = escalation_check(response)
    hallucination = hallucination_check(response)

    print("🔹 Relevance:", relevance)
    print("🔹 Troubleshooting:", troubleshooting)
    print("🔹 Escalation:", escalation)
    print("🔹 Hallucination:", hallucination)

    assert relevance
    assert troubleshooting
    assert escalation
    assert hallucination