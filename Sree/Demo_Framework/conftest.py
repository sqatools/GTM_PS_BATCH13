import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium_base import WebdriverFactory


"""@pytest.fixture(scope='class')

def get_driver(request):
    driver =webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver=driver
    yield()
    driver.close()"""


@pytest.fixture(scope="class")
def get_driver(request, pytestconfig):

    browser_name = pytestconfig.getoption("browser")
    headless_value = pytestconfig.getoption("headless").lower() == "true"

    driver = WebdriverFactory(
        browser=browser_name,
        headless=headless_value
    ).get_driver_instance()

    request.cls.driver = driver
    yield
    driver.quit()
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to execute the automation"
    )
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        choices=["true", "false"],
        help="Run browser in headless mode"
    )