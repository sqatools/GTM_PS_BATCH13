from ..agents.intent_agent import detect_intent
from ..agents.decision_agent import decision_engine
from ..agents.action_agent import take_action

def test_full_flow_wifi():
    query = "Install wifi at my home"

    intent = detect_intent(query)
    decision = decision_engine(intent)
    result = take_action(decision)

    assert result["status"] == "Network Restarted Successfully"

def test_full_flow_internet():
    query = "Internet is down"

    intent = detect_intent(query)
    decision = decision_engine(intent)
    result = take_action(decision)

    assert "Network" in result["status"]

def test_ticket_created():
    query = "Internet is down"

    intent = detect_intent(query)
    decision = decision_engine(intent)
    result = take_action(decision)

    assert 'ticket_id' in result
    assert result["status"] != ""