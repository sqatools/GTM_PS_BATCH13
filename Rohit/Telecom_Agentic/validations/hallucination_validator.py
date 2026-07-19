class HallucinationValidator:

    def validate(self, response):

        blocked_words = ["fake", "incorrect"]

        for word in blocked_words:
            if word in response.lower():
                return False

        return True
