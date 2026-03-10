import pytest
import json
import os
from clients.llm_client import send_prompt

# Enable test mode to skip API key validation
os.environ['TEST_MODE'] = 'true'


# Fixture to load prompt test data
@pytest.fixture(scope="session")
def load_prompts():

    with open("test_data/prompts.json") as f:
        data = json.load(f)

    return data


# Fixture to send prompt and return response
@pytest.fixture
def llm_response():

    def _get_response(prompt):
        response = send_prompt(prompt)
        print("\nLLM Response:", response)
        return response

    return _get_response


# Fixture for logging test start
@pytest.fixture(autouse=True)
def test_logger():

    print("\n----- Test Started -----")

    yield

    print("\n----- Test Finished -----")