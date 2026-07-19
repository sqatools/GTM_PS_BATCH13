class DecisionAgent:

    def make_decision(self, intent):

        if intent == "NETWORK_ISSUE":
            return {
                "team": "L1_SUPPORT",
                "priority": "HIGH",
                "action": "CREATE_INCIDENT"
            }

        elif intent == "WIFI_INSTALLATION":
            return {
                "team": "FIELD_TEAM",
                "priority": "MEDIUM",
                "action": "CREATE_INSTALLATION_REQUEST"
            }

        else:
            return {
                "team": "GENERAL_SUPPORT",
                "priority": "LOW",
                "action": "MANUAL_REVIEW"
            }
