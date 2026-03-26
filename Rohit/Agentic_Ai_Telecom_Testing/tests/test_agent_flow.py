from ..main import run_agentic_flow

def test_internet_down():
    run_agentic_flow("Internet not working")

def test_installation():
    run_agentic_flow("Need new wifi connection")