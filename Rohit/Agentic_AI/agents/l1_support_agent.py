"""
L1 Support Agent

Basic troubleshooting
"""

from ..tools.crm_tool import CRMTool
from ..tools.network_tool import NetworkTool


class L1SupportAgent:

    def __init__(self):

        self.crm = CRMTool()
        self.network = NetworkTool()

    def handle(self, ticket):

        customer = self.crm.get_customer(ticket["customer_id"])

        router = self.network.router_status(customer["router"])

        if router == "ONLINE":

            return {

                "status": "Resolved",

                "message": "Restart router completed",

                "assigned": "L1"

            }

        return {

            "status": "Escalate",

            "assigned": "L2"

        }