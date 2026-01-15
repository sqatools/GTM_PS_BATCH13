import pytest
from selenium import webdriver
import os
from datetime import datetime


@pytest.fixture(scope="class")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()

'''
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
'''

