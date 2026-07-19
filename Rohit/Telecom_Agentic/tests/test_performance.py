import time
from ..main import run_agent


def test_response_time():

    start = time.time()

    run_agent("Internet issue")

    end = time.time()

    assert (end - start) < 5
