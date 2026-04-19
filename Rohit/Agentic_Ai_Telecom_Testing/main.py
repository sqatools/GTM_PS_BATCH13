from agents.intent_agent import IntentAgent
from agents.root_cause_agent import RootCauseAgent
from agents.escalation_agent import EscalationAgent
from agents.action_agent import ActionAgent


def run_agentic_flow(user_input):
    print("\n" + "="*60)
    print(f"🚀 CUSTOMER ISSUE: {user_input}")
    print("="*60)

    intent_agent = IntentAgent()
    root_agent = RootCauseAgent()
    escalation_agent = EscalationAgent()
    action_agent = ActionAgent()

    # Step 1
    intent_data = intent_agent.analyze(user_input)
    print("\n🔍 STEP 1: Intent Detection")
    print(intent_data)

    # Step 2
    root_data = root_agent.analyze(intent_data)
    print("\n🧠 STEP 2: Root Cause Analysis")
    print(root_data)

    # Step 3
    escalation_data = escalation_agent.decide(root_data)
    print("\n📊 STEP 3: Escalation Decision")
    print(escalation_data)

    # Step 4
    result = action_agent.execute(user_input, escalation_data)

    print("\n⚙️ STEP 4: Automated Action")
    print(result)

    print("\n✅ FINAL STATUS: Issue handled successfully")
    return result


if __name__ == "__main__":
    # Example usage
    print("🤖 Agentic AI Telecom Customer Service System")
    print("=" * 50)

    # Test scenarios
    test_cases = [
        "My internet is not working since morning",
        "I need wifi connection in my new apartment",
        "I was overcharged on my bill",
        "My internet speed is very slow",
        "What packages do you offer?"
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*20} TEST CASE {i} {'='*20}")
        run_agentic_flow(test_case)

    print("\n" + "="*60)
    print("🎉 All test cases completed!")
    print("To run interactively, call: run_agentic_flow('your customer issue')")
    print("="*60)