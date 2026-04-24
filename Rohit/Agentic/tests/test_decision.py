from ..agents.decision_agent import decision_engine

def test_decision_internet():
    assert decision_engine("INTERNET_DOWN") == "CHECK_OUTAGE"

def test_decision_wifi():
    assert decision_engine("INSTALL_WIFI") == "CHECK_AVAILABILITY"