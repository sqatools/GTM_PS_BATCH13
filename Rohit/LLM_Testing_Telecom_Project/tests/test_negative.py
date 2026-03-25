from ..utils.llm_client import ask_llm

def test_negative_query():
    query = "asdfgh12345"
    response = ask_llm(query)

    print("\n🔹 Query:", query)
    print("🔹 Response:", response)

    assert "didn't understand" in response.lower(), "❌ Should ask clarification for invalid input"

def test_ambiguous_query():
    query = "Not working"
    response = ask_llm(query)

    print("\nQuery:", query)
    print("Response:", response)

    assert "clarify" in response.lower() or "didn't understand" in response.lower()