# Script Agent
# Responsible for generating test automation scripts
from utils.llm import ask_llm

def generate_script(testcases):

    prompt = f"""
    Write Selenium pytest automation script for:
    {testcases}
    """

    return ask_llm(prompt)