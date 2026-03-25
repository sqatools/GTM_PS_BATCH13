import time
from ..utils.llm_client import ask_llm

def test_response_time():
    query = "WiFi not working"

    start = time.perf_counter()
    response = ask_llm(query)
    end = time.perf_counter()

    response_time = end - start

    print("\nQuery:", query)
    print("Response:", response)
    print(f"\nResponse Time: {response_time:.6f} seconds")

    assert response_time < 1