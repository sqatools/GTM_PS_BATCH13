from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Selenium_Base:
    def __init__(self,driver,timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,timeout)

    def get_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self,locator):
        self.get_element(locator).click()

    def enter_text(self,locator,value):
        self.get_element(locator).send_keys(value)

    def get_attribute_value(self,locator,attrib):
        return self.get_element(locator).get_attribute(attrib)

    def  elements(self,locator):
        return self.get_element(locator).text

    def select_Dropdown(self,locator,value):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)