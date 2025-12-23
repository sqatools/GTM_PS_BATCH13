from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)


    def get_element(self,locator, cond=EC.presence_of_element_located):
        return self.wait.until(cond(locator))

    def click_element(self, locator, **kwargs):
        self.get_element(locator, **kwargs).click()

    def enter_text(self, locator, values):
        elem = self.get_element(locator)
        elem.clear()
        elem.send_keys(values)

    def get_elements(self, locator):
        return self.get_elements(locator).text

    def get_attribute(self, locator, attrib):
        return self.get_element(locator).get_attribute(attrib)

    def click_Registration_button(self,locator):
        self.click_element(locator, cond=EC.element_to_be_clickable)
        #self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_customer_Login_button(self,locator):
       # element = self.wait.until(EC.visibility_of_element_located(locator))
        element= self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def select_dropdown_by_visible_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_visible_text(text)

    def select_dropdown_by_value(self, locator, value):
        dropdown = self.wait.until(EC.presence_of_element_located(locator))
        Select(dropdown).select_by_value(value)

    def select_dropdown_by_index(self, locator,index):
        dropdown = self.wait.until(EC.presence_of_element_located(locator))
        Select(dropdown).select_by_index(index)






