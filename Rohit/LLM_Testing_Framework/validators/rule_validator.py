def validate_response_format(response):

    if not response:
        return False, "Empty response"

    if len(response) < 10:
        return False, "Response too short"

    return True, "Valid response"


def check_keywords(response, keywords):

    for word in keywords:
        if word.lower() not in response.lower():
            return False, f"{word} not found"

    return True, "Keywords found"