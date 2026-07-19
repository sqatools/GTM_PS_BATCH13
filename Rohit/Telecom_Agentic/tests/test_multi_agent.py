from ..agents.intent_agent import IntentAgent
from ..agents.decision_agent import DecisionAgent
from ..agents.action_agent import ActionAgent

def test_multi_agent_workflow():

    print("\n===== Multi Agent Workflow Test =====")

    query = "Internet down in my area"

    print(f"Customer Query: {query}")

    # Intent Agent
    intent_agent = IntentAgent()

    intent = intent_agent.detect_intent(query)

    print(f"Intent Agent Output: {intent}")

    # Decision Agent
    decision_agent = DecisionAgent()

    decision = decision_agent.make_decision(intent)

    print(f"Decision Agent Output: {decision}")

    # Action Agent
    action_agent = ActionAgent()

    action = action_agent.execute_action(decision)

    print(f"Action Agent Output: {action}")

    assert action["status"] == "OPEN"

    print("Multi-Agent Workflow PASSED")