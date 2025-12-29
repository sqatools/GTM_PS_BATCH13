import time

import pytest
import self
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestFacebook:

    def test_facebook_login(self):
      time.sleep(10)
      self.driver.find_element(By.NAME , "email").send_keys("user1@gmail.com")
      self.driver.find_element(By.NAME , "Pass").send_keys("user@1234")
      time.sleep(5)
      self.driver.find_element(By.NAME , "Login").click()
    def test_dummy_booking(self):
       self.driver.get("https://sqatools.in/dummy-booking-website/")
       self.driver.find_element(By.NAME , "fromcity").send_keys("Mumbai")
       self.driver.find_element(By.NAME , "destcity").send_keys("Pune")
       self.driver.find_element(By.ID , "departdate").send_keys("12/11/2025")
       self.driver.find_element(By.ID , "whatsapp").click()

