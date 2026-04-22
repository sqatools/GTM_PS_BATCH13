def call_llm(prompt: str) -> str:
    # Mock LLM response (replace with real LLM later)
    if "internet" in prompt.lower():
        return "INTERNET_DOWN"
    elif "wifi" in prompt.lower():
        return "INSTALL_WIFI"
    return "UNKNOWN"