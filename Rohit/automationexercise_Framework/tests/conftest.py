import pytest
from selenium import webdriver
from ..base.Ecommerance import Ecommerce


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome', help="browser to execute the automation")
    parser.addoption("--headless", action='store', default=False, help="browser to execute the automation")


@pytest.fixture(scope="class")
def get_driver_with_headless(request, pytestconfig):
    browser_name = pytestconfig.getoption("browser_name")
    headless_value = pytestconfig.getoption("headless")
    if headless_value == "True":
        wf = Ecommerce(browser_name, headless_value)
    else:
        wf = Ecommerce(browser_name, headless=False)
    driver = wf.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()


