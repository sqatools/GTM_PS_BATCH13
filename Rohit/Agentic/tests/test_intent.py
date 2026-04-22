from ..agents.intent_agent import detect_intent

def test_internet_down():
    result = detect_intent("My internet is not working")
    assert result == "INTERNET_DOWN"

def test_wifi_install():
    result = detect_intent("I want new wifi connection")
    assert result == "INTERNET_DOWN"