import pytest
from selenium import webdriver
import os
from datetime import datetime


@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store")
    parser.addoption("--headless", action="store_true")

