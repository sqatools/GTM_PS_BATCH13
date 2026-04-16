from langchain_openai import ChatOpenAI
import os
import json

class IntentAgent:

    def __init__(self):
        try:
            self.llm = ChatOpenAI(temperature=0.1, model="gpt-3.5-turbo")
            self.use_llm = True
        except:
            self.use_llm = False

    def analyze(self, user_input):
        if self.use_llm:
            try:
                prompt = f"""
                Analyze the following customer complaint for a telecom service provider (Charter).
                Services include Television, Wifi, Mobile recharge.

                Customer complaint: {user_input}

                Determine:
                1. Issue type (Internet Down, Installation Delay, Billing Issue, Service Quality, General Inquiry)
                2. Priority level (High, Medium, Low)
                3. Location mentioned (if any, otherwise 'Unknown')

                Return in JSON format:
                {{
                    "issue_type": "type",
                    "priority": "level",
                    "location": "location"
                }}
                """
                response = self.llm.invoke(prompt)
                result = json.loads(response.content.strip())
                return result
            except Exception as e:
                return self._fallback_analyze(user_input)
        else:
            return self._fallback_analyze(user_input)

    def _fallback_analyze(self, user_input):
        user_input = user_input.lower()

        if "internet" in user_input and ("down" in user_input or "not working" in user_input or "no internet" in user_input):
            issue_type = "Internet Down"
            priority = "High"
        elif "new connection" in user_input or "wifi" in user_input or "install" in user_input:
            issue_type = "Installation Delay"
            priority = "Medium"
        elif "bill" in user_input or "charge" in user_input or "payment" in user_input:
            issue_type = "Billing Issue"
            priority = "Medium"
        elif "slow" in user_input or "speed" in user_input or "quality" in user_input:
            issue_type = "Service Quality"
            priority = "Medium"
        else:
            issue_type = "General Inquiry"
            priority = "Low"

        return {
            "issue_type": issue_type,
            "priority": priority,
            "location": "Unknown"
        }