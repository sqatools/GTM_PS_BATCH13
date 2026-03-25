from ..utils.llm_client import ask_llm

def test_intent_wifi():
    response = ask_llm("Internet not working")
    assert "router" in response.lower()