import pytest
from selenium import webdriver



@pytest.fixture(scope="function", autouse=True)
def setup():
    print("\n---Launch URL : https://www.google.com ----")
    yield
    print("\n-- closing browser ----")

@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
