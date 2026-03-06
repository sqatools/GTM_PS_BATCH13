import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store", default="True")


@pytest.fixture(scope="class")
def get_driver(request):

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    options = Options()

    if headless == "True":
        options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    request.cls.driver = driver
    yield driver
    driver.quit()