from ..main import run_agent


def test_complete_flow():

    response = run_agent("Internet is down")

    assert "Ticket" in response
