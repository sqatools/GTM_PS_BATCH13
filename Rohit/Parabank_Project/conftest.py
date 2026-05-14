from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture(scope="class")
def get_driver(request):
    options = Options()

    options.add_argument("--headless")  # MUST for Docker
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    request.cls.driver = driver
    yield driver
    driver.close()