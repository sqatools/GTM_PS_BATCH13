class ErrorAgent:

    def detect_error(self, system_status):

        if system_status == "DOWN":
            return True

        return False
