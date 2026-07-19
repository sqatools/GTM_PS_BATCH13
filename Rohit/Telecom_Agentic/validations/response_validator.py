class ResponseValidator:

    def validate_response(self, response):

        if len(response) < 5:
            return False

        return True
