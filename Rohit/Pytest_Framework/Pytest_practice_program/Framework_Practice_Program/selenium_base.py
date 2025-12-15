from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class SeleniumBase():
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def get_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_text(self, locator, text):
        self.get_element(locator).send_keys(text)

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def get_attribute_value(self, locator, attrib):
        return self.get_element(locator).get_attribute(attrib)


    def Select_dropdown_value(self, locator, value):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)

    def select_dropdown_by_text(self, locator, value):
        element = self.get_element(locator)
        Select(element).select_by_visible_text(value)

    def select_from_dropdown_list(self, dropdown_locator, options_locator, value):
        self.click_element(dropdown_locator)
        options = self.wait.until(EC.presence_of_all_elements_located(options_locator))

        for opt in options:
            if opt.text.strip() == value:
                opt.click()
                break