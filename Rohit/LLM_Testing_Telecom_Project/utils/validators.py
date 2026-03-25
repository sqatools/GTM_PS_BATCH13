def is_relevant(response):
    return len(response) > 10


def has_troubleshooting_steps(response):
    keywords = ["restart", "check"]
    return any(word in response.lower() for word in keywords)


def escalation_check(response):
    keywords = ["escalate", "ticket", "technical team"]
    return any(word in response.lower() for word in keywords)

def hallucination_check(response):
    fake_words = ["guaranteed", "100% fixed", "technician assigned"]
    return not any(word in response.lower() for word in fake_words)

def is_complete(response):
    return len(response.split()) > 5

response = "This is a sample response with more than five words"

assert is_complete(response), "❌ Response not complete"