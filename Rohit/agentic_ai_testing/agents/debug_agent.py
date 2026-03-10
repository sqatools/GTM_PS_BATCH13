# Debug Agent
# Responsible for debugging and fixing test failures
from utils.llm import ask_llm

def fix_error(error_log, code):

    prompt = f"""
    Fix the selenium pytest automation script.

    Error:
    {error_log}

    Code:
    {code}
    """

    return ask_llm(prompt)