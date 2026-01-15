import pytest
from selenium import webdriver
from ..base.Ecommerance import Ecommerce


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome', help="browser to execute the automation")
    parser.addoption("--headless", action='store', default='False', help="run browser in headless mode")


@pytest.fixture(scope="class")
def get_driver_with_headless(request, pytestconfig):
    browser_name = pytestconfig.getoption("browser_name")
    headless_value = pytestconfig.getoption("headless").lower() == "true"
    wf = Ecommerce(browser_name, headless=headless_value)
    driver = wf.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()


