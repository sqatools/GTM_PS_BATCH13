import pytest
from selenium import webdriver
from config.config import BROWSER


@pytest.fixture
def driver():

    if BROWSER == "chrome":
        driver = webdriver.Chrome()

    elif BROWSER == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()