class IntentAgent:

    def detect_intent(self, user_query):

        if "internet" in user_query.lower():
            return "NETWORK_ISSUE"

        elif "wifi" in user_query.lower():
            return "WIFI_INSTALLATION"

        elif "recharge" in user_query.lower():
            return "MOBILE_RECHARGE"

        else:
            return "UNKNOWN"
