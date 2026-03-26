class NotificationService:
 def notify(self, ticket):
    print("\n📩 CUSTOMER NOTIFICATION")
    print(f"Your issue is assigned to {ticket['assigned_team']}")
    print(f"Ticket ID: {ticket['ticket_id']}")