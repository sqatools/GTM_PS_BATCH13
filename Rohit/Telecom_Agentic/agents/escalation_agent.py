class EscalationAgent:

    def escalate_ticket(self, downtime_hours):

        if downtime_hours > 4:
            return "L2_SUPPORT"

        elif downtime_hours > 8:
            return "L3_SUPPORT"

        return "L1_SUPPORT"
