import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("OrangeHRM_Webite")
class TestOrangeHRM:
    def test_login(self):
        time.sleep(5)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)