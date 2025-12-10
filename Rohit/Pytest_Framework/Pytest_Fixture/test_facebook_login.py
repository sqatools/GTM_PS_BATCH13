import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("get_driver")
class TestFacebook:
    def test_facebook_login(self):
        time.sleep(10)
        self.driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
        self.driver.find_element(By.NAME, "pass").send_keys("user@1234")
        time.sleep(5)
        self.driver.find_element(By.NAME, "login").click()


#python -m pytest -v -s .\test_facebook_login.py