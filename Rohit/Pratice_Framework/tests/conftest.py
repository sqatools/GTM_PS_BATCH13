import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome', help="browser to execute the automation")
    parser.addoption("--headless", action='store', default='False', help="run browser in headless mode")
