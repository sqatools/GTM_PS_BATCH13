import pytest
from selenium import webdriver

@pytest.fixture(scope="function",autouse=True)
def setup():
    print("\n -- Launch URL www.automationexercise.com--")
    yield
    print("\n -- closing browser--")

@pytest.fixture(scope = 'class', autouse= True)
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()


