from services.ticket_service import TicketService
from services.notification_service import NotificationService

class ActionAgent:

    def __init__(self):
        self.ticket_service = TicketService()
        self.notification_service = NotificationService()

    def execute(self, user_input, escalation_data):
        print("⚙️ Executing Automated Actions...")

        # Step 1: Create Ticket
        ticket = self.ticket_service.create_ticket(user_input, escalation_data)

        # Step 2: Notify Customer
        self.notification_service.notify(ticket)

        # Step 3: Return final response
        return {
            "status": "Success",
            "ticket": ticket
        }