from ..utils.llm_helper import call_llm

VALID_INTENTS = ["INSTALL_WIFI", "INTERNET_DOWN"]

def detect_intent(query: str) -> str:
    prompt = f"""
    Classify the user request into one of:
    {VALID_INTENTS}

    User: {query}
    Return only intent.
    """

    response = call_llm(prompt)

    for intent in VALID_INTENTS:
        if intent in response:
            return intent

    return "UNKNOWN"