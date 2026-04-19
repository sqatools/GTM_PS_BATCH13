import pytest
from selenium  import webdriver

@pytest.fixture(scope='class')
def get_Driver(request):
    driver= webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()