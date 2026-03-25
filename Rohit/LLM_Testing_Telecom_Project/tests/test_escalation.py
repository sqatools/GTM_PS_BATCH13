from ..utils.llm_client import ask_llm
from ..utils.validators import escalation_check

def test_escalation():
    response = ask_llm("Internet not working for 2 days")
    assert escalation_check(response)