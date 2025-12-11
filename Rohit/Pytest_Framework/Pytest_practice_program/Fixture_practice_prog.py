import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function", autouse=True)
def function():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.close()

class Test_login:
    def test_practice_test_login(self,function):
            driver = function
            driver.find_element(By.ID,"username").send_keys("student")
            driver.find_element(By.NAME,"password").send_keys("Password123")
            driver.find_element(By.ID,"submit").click()
            time.sleep(10)


    def test_contact_tab(self,function):
        driver = function
        driver.find_element(By.XPATH,"//a[text()='Contact']").click()
        driver.find_element(By.ID,"wpforms-161-field_0").send_keys("Rohit")
        driver.find_element(By.ID,"wpforms-161-field_0-last").send_keys("Chavan")
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Dheeraj_chavan@gmail.com")
        driver.find_element(By.XPATH,"//textarea[@id='wpforms-161-field_2']").send_keys("Learning Python")
        time.sleep(10)

