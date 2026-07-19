class APIService:

    def create_ticket(self, issue):

        return {
            "ticket_status": "CREATED",
            "issue": issue
        }
