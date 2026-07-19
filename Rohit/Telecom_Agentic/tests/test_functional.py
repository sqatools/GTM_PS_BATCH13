from ..agents.intent_agent import IntentAgent

def test_network_issue():

    print("\nStarting Functional Test")

    agent = IntentAgent()

    query = "Internet not working"

    print(f"Input Query: {query}")

    result = agent.detect_intent(query)

    print(f"Detected Intent: {result}")

    assert result == "NETWORK_ISSUE"

    print("Functional Test Passed")