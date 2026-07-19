from agents.intent_agent import IntentAgent
from agents.decision_agent import DecisionAgent
from agents.action_agent import ActionAgent
from agents.response_agent import ResponseAgent
from agents.memory_agent import MemoryAgent


def run_agent(user_query):

    memory = MemoryAgent()

    intent_agent = IntentAgent()
    decision_agent = DecisionAgent()
    action_agent = ActionAgent()
    response_agent = ResponseAgent()

    # Step 1 - Detect Intent
    intent = intent_agent.detect_intent(user_query)

    # Step 2 - Decide Action
    decision = decision_agent.make_decision(intent)

    # Step 3 - Execute Action
    action_result = action_agent.execute_action(decision)

    # Step 4 - Save Memory
    memory.save_conversation(user_query, action_result)

    # Step 5 - Generate Response
    final_response = response_agent.generate_response(action_result)

    return final_response


if __name__ == "__main__":

    user_query = "Internet is down from last 5 hours"

    response = run_agent(user_query)

    print("\nFinal Response:")
    print(response)
