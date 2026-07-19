from ..main import run_agent


def test_regression():

    response = run_agent("Wifi installation required")

    assert "Ticket" in response
