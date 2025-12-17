import pytest
import os
from datetime import datetime
from selenium import webdriver
from ..base.webdriver_factory import WebdriverFactory


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


@pytest.fixture(scope='class')
def get_driver_with_headless(request, pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    headless_value = pytestconfig.getoption("headless")
    if headless_value == "True":
        wf = WebdriverFactory(browser_name, headless_value)
    else:
        wf = WebdriverFactory(browser_name, headless=False)
    driver = wf.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_configure(config):
    # create a logs folder if is not there
    logs_path = os.path.join(os.getcwd(), "logs")
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)

    # create a folder with date name if it is not there
    folder_name = datetime.now().strftime("%d_%m_%Y")
    folder_path = os.path.join(logs_path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # create a log file inside the today date folder.
    unique_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    log_file_name = f"{unique_name}_trace.log"
    log_file_path = os.path.join(folder_path, log_file_name)

    # update log file path in config
    config.option.log_file = log_file_path
