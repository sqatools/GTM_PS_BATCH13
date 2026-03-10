# Requirement Agent
# Responsible for gathering and analyzing test requirements
from utils.llm import ask_llm

def analyze_requirement(prompt):

    instruction = f"""
    Analyze the requirement and extract:
    - Feature
    - Test scenarios
    """

    return ask_llm(prompt + instruction)