import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser to execute the automation"
    )
    parser.addoption(
        "--headless",
        action="store_true",   # just a flag
        default=False,
        help="Run browser in headless mode"
    )

@pytest.fixture(scope="class")
def get_driver(request, pytestconfig):
    browser_name = pytestconfig.getoption("browser_name")
    headless = pytestconfig.getoption("headless")

    if browser_name.lower() == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    else:
        raise Exception(f"Browser {browser_name} not supported")

    request.cls.driver = driver
    yield
    driver.quit()
