class SecurityValidator:

    def detect_prompt_injection(self, query):

        suspicious_keywords = [
            "ignore previous instruction",
            "hack",
            "bypass"
        ]

        for word in suspicious_keywords:
            if word in query.lower():
                return True

        return False
