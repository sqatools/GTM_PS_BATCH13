class ResponseAgent:

    def generate_response(self, action_result):

        return f"""
Ticket Created Successfully

Ticket ID: {action_result['ticket_id']}
Status: {action_result['status']}
Assigned Team: {action_result['assigned_team']}
Priority: {action_result['priority']}
"""
