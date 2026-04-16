from langchain_openai import ChatOpenAI
import json

class EscalationAgent:

    def __init__(self):
        try:
            self.llm = ChatOpenAI(temperature=0.1, model="gpt-3.5-turbo")
            self.use_llm = True
        except:
            self.use_llm = False

    def decide(self, root_cause_data):
        if self.use_llm:
            try:
                priority = root_cause_data.get("priority", "Medium")
                prompt = f"""
                Based on the root cause analysis, determine the appropriate escalation level for this telecom issue.

                Root Cause: {root_cause_data['root_cause']}
                Recommended Action: {root_cause_data['action']}
                Priority Level: {priority}

                Escalation Levels:
                - L1: Basic customer support, simple troubleshooting
                - L2: Technical support, field engineers, network issues
                - L3: Senior technical experts, complex infrastructure issues

                Teams:
                - Customer Support
                - Network Team
                - Field Engineering
                - Billing Department
                - Management

                Actions:
                - Troubleshoot
                - Field Engineer Required
                - Network Maintenance
                - Billing Review
                - Priority Escalation

                Consider priority and complexity to decide escalation.

                Return in JSON format:
                {{
                    "level": "L1/L2/L3",
                    "team": "team_name",
                    "action": "action_description"
                }}
                """
                response = self.llm.invoke(prompt)
                result = json.loads(response.content.strip())
                return result
            except Exception as e:
                return self._fallback_decide(root_cause_data)
        else:
            return self._fallback_decide(root_cause_data)

    def _fallback_decide(self, root_cause_data):
        cause = root_cause_data["root_cause"]

        if cause in ["Router Issue", "Configuration Error"]:
            return {
                "level": "L1",
                "team": "Customer Support",
                "action": "Troubleshoot"
            }
        elif cause in ["Network Outage", "Cable Damage", "Service Overload", "Service Degradation"]:
            return {
                "level": "L2",
                "team": "Network Team",
                "action": "Field Engineer Required"
            }
        elif cause == "Area Not Serviceable":
            return {
                "level": "L2",
                "team": "Field Engineering",
                "action": "Installation Assessment"
            }
        elif cause in ["Scheduling Issue", "Billing Error"]:
            return {
                "level": "L2",
                "team": "Technical Support",
                "action": "Advanced Troubleshooting"
            }
        else:
            return {
                "level": "L2",
                "team": "Technical Support",
                "action": "Advanced Troubleshooting"
            }

