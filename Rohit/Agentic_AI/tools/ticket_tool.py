"""
Ticket Tool

Responsible for:
1. Create Ticket
2. Update Ticket
3. Close Ticket
4. Get Ticket Details
"""


class TicketTool:

    def __init__(self):

        self.tickets = {}

    def create_ticket(

        self,

        ticket_id,

        customer,

        issue

    ):

        self.tickets[ticket_id] = {

            "customer": customer,

            "issue": issue,

            "status": "OPEN"

        }

        return self.tickets[ticket_id]

    def update_status(

        self,

        ticket_id,

        status

    ):

        if ticket_id in self.tickets:

            self.tickets[ticket_id]["status"] = status

        return self.tickets.get(ticket_id)

    def close_ticket(

        self,

        ticket_id

    ):

        return self.update_status(

            ticket_id,

            "CLOSED"

        )

    def get_ticket(

        self,

        ticket_id

    ):

        return self.tickets.get(ticket_id)