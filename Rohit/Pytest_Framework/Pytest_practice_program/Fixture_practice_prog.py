import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function", autouse=True)
def driver_function():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.close()

class Test_login:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver_function):
        self.driver = driver_function

    def test_practice_test_login(self):
        self.driver.find_element(By.ID,"username").send_keys("student")
        self.driver.find_element(By.NAME,"password").send_keys("Password123")
        self.driver.find_element(By.ID,"submit").click()
        time.sleep(10)


    def test_contact_tab(self):
        self.driver.find_element(By.XPATH,"//a[text()='Contact']").click()
        self.driver.find_element(By.ID,"wpforms-161-field_0").send_keys("Rohit")
        self.driver.find_element(By.ID,"wpforms-161-field_0-last").send_keys("Chavan")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Dheeraj_chavan@gmail.com")
        self.driver.find_element(By.XPATH,"//textarea[@id='wpforms-161-field_2']").send_keys("Learning Python")
        time.sleep(10)

