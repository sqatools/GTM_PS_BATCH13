from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumBase:
     def __init__(self, driver, timeout=30):
         self.driver = driver
         self.wait = WebDriverWait(driver,10)


     def get_elements(self,locator):
         return self.wait.until(EC.presence_of_element_located(locator))

     def click_element(self,locator):
         self.get_elements(locator).click()

     def get_element(self,locator):
         return self.get_elements(locator).text

     def enter_text(self,locator):
         self.get_elements(locator).send_keys(locator)


