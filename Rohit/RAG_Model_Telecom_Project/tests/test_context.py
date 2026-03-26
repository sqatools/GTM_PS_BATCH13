from ..main import ask

def test_context_usage():
    query = "Internet down for 40 minutes"
    response = ask(query)

    print("\n================ CONTEXT VALIDATION ================")
    print(f"🔹 Query    : {query}")
    print(f"🔹 Response : {response}")

    assert "L2" in response or "escalate" in response