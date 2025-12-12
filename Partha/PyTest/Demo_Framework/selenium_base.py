from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def get_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_text(self, locator, value):
        self.get_element(locator).send_keys(value)

    def get_text(self, locator):
        return self.get_element(locator).text

    def get_attribute_value(self, locator, attrib):
        return self.get_element(locator).get_attribute(attrib)