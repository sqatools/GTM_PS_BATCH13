class IntentAgent:

    def analyze(self, user_input):
        user_input = user_input.lower()

        if "not working" in user_input or "internet down" in user_input:
            issue_type = "Internet Down"
            priority = "High"

        elif "new connection" in user_input or "wifi" in user_input:
            issue_type = "Installation Delay"
            priority = "Medium"

        else:
            issue_type = "General Issue"
            priority = "Low"

        return {
            "issue_type": issue_type,
            "priority": priority,
            "location": "Pune"
        }