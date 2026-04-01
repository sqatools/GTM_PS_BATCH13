class EscalationAgent:

    def decide(self, root_cause_data):
        cause = root_cause_data["root_cause"]

        if cause == "Router Issue":
            return {
                "level": "L1",
                "team": "Customer Support",
                "action": "Troubleshoot"
            }

        else:
            return {
                "level": "L2",
                "team": "Network Team",
                "action": "Field Engineer Required"
            }

