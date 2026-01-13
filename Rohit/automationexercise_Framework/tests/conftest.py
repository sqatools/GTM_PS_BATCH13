import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Add CLI options
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser to execute the automation"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )

# Fixture to initialize driver
@pytest.fixture(scope="class")
def get_driver(request, pytestconfig):
    browser_name = pytestconfig.getoption("browser_name").lower()
    headless = pytestconfig.getoption("headless")

    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless=new")  # safer for latest Chrome
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    else:
        raise Exception(f"Browser '{browser_name}' is not supported!")

    driver.maximize_window()
    request.cls.driver = driver  # attach to the test class
    yield driver  # yield driver instance to tests
    driver.quit()
