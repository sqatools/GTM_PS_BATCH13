from ..utils.llm_client import ask_llm

def test_context_basic():
    response1 = ask_llm("Internet not working")
    response2 = ask_llm("Still not working")

    print("\n🔹 Basic First Response:", response1)
    print("🔹 Basic Second Response:", response2)

    assert response1 != "", "❌ First response is empty"
    assert response2 != "", "❌ Second response is empty"


def test_context_with_memory():
    response1 = ask_llm("Internet not working")
    response2 = ask_llm("Still not working", context="internet_issue")

    print("\n🔹 First Response:", response1)
    print("🔹 Follow-up Response:", response2)

    assert "escalate" in response2.lower(), "❌ Context not handled properly"