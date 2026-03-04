import pytest
import requests


@pytest.fixture(scope="function")
def driver():
    """Provide a requests.Session for API tests."""
    session = requests.Session()
    yield session
    session.close()
