"""
Planner Agent

Responsibility:
1. Receive customer issue
2. Decide which agent to call
3. Return final response
"""

from ..agents.l1_support_agent import L1SupportAgent
from ..agents.l2_support_agent import L2SupportAgent
from ..agents.network_agent import NetworkAgent
from ..agents.escalation_agent import EscalationAgent
from ..llm.openai_client import ask_llm
from ..tools.crm_tool import CRMTool
from ..tools.network_tool import NetworkTool

class PlannerAgent:

    def __init__(self):

        self.l1 = L1SupportAgent()
        self.l2 = L2SupportAgent()
        self.network = NetworkAgent()
        self.escalation = EscalationAgent()

    def process_ticket(self, ticket):

        issue = ticket["issue"].lower()

        print("Planner Agent Started")

        if "internet" in issue:

            network_status = self.network.check_network(ticket)

            if network_status["status"] == "DOWN":

                return self.l2.handle(ticket)

            return self.l1.handle(ticket)

        elif "wifi installation" in issue:

            return self.escalation.assign_field_engineer(ticket)

        elif "tv" in issue:

            return self.l1.handle(ticket)

        else:

            return {

                "status": "Unknown Issue",

                "assigned_to": "Manual Team"

            }