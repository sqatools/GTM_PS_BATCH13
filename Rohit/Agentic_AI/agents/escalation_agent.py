"""
Escalation Agent

Assign technician
Generate work order
"""


class EscalationAgent:

    def assign_field_engineer(self, ticket):

        work_order = {

            "ticket_id": ticket["ticket_id"],

            "engineer": "Rahul Patil",

            "eta": "2 Hours"

        }

        return {

            "status": "Assigned",

            "work_order": work_order

        }