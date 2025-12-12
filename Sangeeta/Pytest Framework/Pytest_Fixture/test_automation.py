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
        self.driver.find_element(By.NAME, 'name').send_keys('Sangs-Tester1')
        self.driver.find_element(By.NAME, 'email').send_keys('sangeeta_salian@gmail.com')
        self.driver.find_element(By.XPATH,"//button[@type='submit' and text() = 'Signup']")
        self.driver.find_element(By.XPATH,"//input[@name='title' and text() = 'Mrs']")
        self.click()
        self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys('practice$1')


