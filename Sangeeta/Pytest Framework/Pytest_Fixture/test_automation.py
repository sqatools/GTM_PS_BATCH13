import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestAutomation:
    def test_auto_login(self):
        time.sleep(10)
        #self.driver.find_element(By.XPATH, "//a[contains(text(), ' Signup / Login')]")
        login = self.driver.find_element(By.XPATH,"//a[contains(@href,'/login')]")
        login.click()
        time.sleep(2)


