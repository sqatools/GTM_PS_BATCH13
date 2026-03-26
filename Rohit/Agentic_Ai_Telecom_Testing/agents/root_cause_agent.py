from data.mock_data import SERVICEABLE_AREAS
from data.mock_data import NETWORK_OUTAGES

class RootCauseAgent:

    def analyze(self, intent_data):
        location = intent_data["location"]

        if location not in SERVICEABLE_AREAS:
            return {
                "root_cause": "Area Not Serviceable",
                "action": "Installation Issue"
            }

        if location in NETWORK_OUTAGES:
            return {
                "root_cause": "Network Outage",
                "action": "Backend Issue"
            }

        return {
            "root_cause": "Router Issue",
            "action": "Basic Troubleshooting"
        }