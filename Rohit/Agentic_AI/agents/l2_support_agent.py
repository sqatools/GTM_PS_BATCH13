"""
L2 Support Agent

Advanced Network Analysis
"""

from ..tools.network_tool import NetworkTool
from ..tools.ticket_tool import TicketTool


class L2SupportAgent:

    def __init__(self):

        self.network = NetworkTool()

        self.ticket = TicketTool()

    def handle(self, ticket):

        signal = self.network.signal_strength(ticket.get("area"))

        packet_loss = self.network.packet_loss()

        if signal < 30:

            self.ticket.update_status(

                ticket["ticket_id"],

                "Field Visit Required"

            )

            return {

                "status": "Escalated",

                "assigned": "Field Engineer"

            }

        return {

            "status": "Resolved by L2"

        }