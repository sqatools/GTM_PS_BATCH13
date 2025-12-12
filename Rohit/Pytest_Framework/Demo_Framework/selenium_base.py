from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def get_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_text(self, locator, values):
        self.get_element(locator).send_keys(values)

    def get_elements(self, locator):
        return  self.get_element(locator).text

    def get_attribute_value(self, locator, attrib):
        return self.get_element(locator).get_attribute(attrib)