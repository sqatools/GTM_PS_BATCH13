from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Selenium_base:
    def __init__(self, driver):
        self.driver= driver
        self.wait = WebDriverWait(self.driver,10)


    def get_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_text(self, locator, values):
        clear_element = self.get_element(locator)
        self.get_element(locator).send_keys(values)

    def get_elements(self, locator):
       return self.get_element(locator).text

    def drop_down_value(self, locator,values):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(values)


