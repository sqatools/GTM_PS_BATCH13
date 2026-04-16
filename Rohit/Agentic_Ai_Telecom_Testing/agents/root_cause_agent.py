from langchain_openai import ChatOpenAI
from data.mock_data import SERVICEABLE_AREAS, NETWORK_OUTAGES
import json

class RootCauseAgent:

    def __init__(self):
        try:
            self.llm = ChatOpenAI(temperature=0.1, model="gpt-3.5-turbo")
            self.use_llm = True
        except:
            self.use_llm = False

    def analyze(self, intent_data):
        if self.use_llm:
            try:
                prompt = f"""
                Analyze the root cause for a telecom issue.

                Issue Details:
                - Issue Type: {intent_data['issue_type']}
                - Location: {intent_data['location']}
                - Serviceable Areas: {str(SERVICEABLE_AREAS)}
                - Current Network Outages: {str(NETWORK_OUTAGES)}

                Determine the most likely root cause and recommended action.

                Possible root causes:
                - Area Not Serviceable
                - Network Outage
                - Router/Modem Issue
                - Cable Damage
                - Configuration Error
                - Billing/Payment Issue
                - Service Overload

                Actions:
                - Installation Issue
                - Backend Issue
                - Basic Troubleshooting
                - Advanced Technical Support
                - Billing Department

                Return in JSON format:
                {{
                    "root_cause": "cause",
                    "action": "action"
                }}
                """
                response = self.llm.invoke(prompt)
                result = json.loads(response.content.strip())
                return result
            except Exception as e:
                return self._fallback_analyze(intent_data)
        else:
            return self._fallback_analyze(intent_data)

    def _fallback_analyze(self, intent_data):
        location = intent_data.get("location", "Unknown")

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

        issue_type = intent_data.get("issue_type", "General Inquiry")
        if issue_type == "Internet Down":
            return {
                "root_cause": "Router Issue",
                "action": "Basic Troubleshooting"
            }
        elif issue_type == "Installation Delay":
            return {
                "root_cause": "Scheduling Issue",
                "action": "Installation Issue"
            }
        elif issue_type == "Billing Issue":
            return {
                "root_cause": "Billing Error",
                "action": "Billing Department"
            }
        elif issue_type == "Service Quality":
            return {
                "root_cause": "Service Degradation",
                "action": "Network Maintenance"
            }
        else:
            return {
                "root_cause": "General Issue",
                "action": "Basic Troubleshooting"
            }