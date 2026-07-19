import random

class ActionAgent:

    def execute_action(self, decision):

        ticket_id = random.randint(1000, 9999)

        return {
            "ticket_id": ticket_id,
            "status": "OPEN",
            "assigned_team": decision["team"],
            "priority": decision["priority"]
        }
