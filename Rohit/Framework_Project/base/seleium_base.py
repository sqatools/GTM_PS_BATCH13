from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from Rohit.Framework_Automation_Practice.Page_objects.website.website_locator import Login_btn
from Rohit.Framework_Project.Page_objects.banking_website.banking_website_locator import Register_btn


class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)


    def get_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_text(self, locator, values):
        self.get_element(locator).send_keys(values)

    def get_elements(self, locator):
        return self.get_elements(locator).text

    def get_attribute(self, locator, attrib):
        return self.get_element(locator).get_attribute(attrib)

    def select_dropdown_value(self, locator, value):
        element = self.wait.until(EC.presence_of_element_located(locator))
        Select(element).select_by_visible_text(value)

    def click_Registration_button(self):
        self.wait.until(EC.element_to_be_clickable(Register_btn)).click()

    def click_customer_Login_button(self):
        element = self.wait.until(EC.visibility_of_element_located(Login_btn))
        self.wait.until(EC.element_to_be_clickable(Login_btn))
        element.click()

