# Report Agent
# Responsible for generating test reports and analytics
from utils.llm import ask_llm


def generate_report(test_result):

    prompt = f"""
    Create QA automation test report.

    Result:
    {test_result}
    """

    report = ask_llm(prompt)

    return report