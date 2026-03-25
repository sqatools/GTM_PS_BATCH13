from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class SeleniumBase():
    def __init__(self, driver,timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self,locator):
        self.get_element(locator).click()

    def enter_text(self,locator,text):
        self.get_element(locator).send_keys(text)

    def elements(self,locator):
        return self.get_element(locator).text

    def select_dropdown(self,locator,value):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)