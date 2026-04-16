class NotificationService:
 def notify(self, ticket):
    print("\n📩 CUSTOMER NOTIFICATION")
    assigned_team = ticket.get('assigned_team', 'Support Team')
    print(f"Your issue is assigned to {assigned_team}")
    ticket_id = ticket.get('ticket_id', 'Unknown')
    print(f"Ticket ID: {ticket_id}")