class ReasoningValidator:

    def validate_reasoning(self, decision):

        required_keys = ["team", "priority"]

        for key in required_keys:
            if key not in decision:
                return False

        return True
