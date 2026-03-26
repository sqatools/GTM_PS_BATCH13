class TicketService:
    def create_ticket(self, user_input, escalation_data):
        ticket = {
            "ticket_id": "TCKT12345",
            "issue": user_input,
            "assigned_team": escalation_data["team"],
            "level": escalation_data["level"],
            "status": "Open"
        }

        print("\n🎫 TICKET CREATED")
        print(f"Ticket ID: {ticket['ticket_id']}")
        print(f"Assigned Team: {ticket['assigned_team']}")
        print(f"Level: {ticket['level']}")

        return ticket