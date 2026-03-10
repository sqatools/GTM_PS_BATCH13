# Test Case Agent
# Responsible for generating and managing test cases
from utils.llm import ask_llm

def generate_testcases(requirement):

    prompt = f"""
    Create detailed test cases for:
    {requirement}
    """

    return ask_llm(prompt)