from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import logging


class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)
        self.log = logging.getLogger(__name__)

    def get_element(self, locator, cond=ec.presence_of_element_located):
        self.log.info(f"getting element with locator: {locator}")
        return self.wait.until(cond(locator))

    def get_elements_list(self, locator, cond=ec.visibility_of_all_elements_located):
        self.log.info(f"getting elements with locator: {locator}")
        return self.wait.until(cond(locator))

    def click_element(self, locator):
        self.log.info(f"clicking on element with locator: {locator}")
        self.get_element(locator).click()

    def enter_text(self, locator, value):
        self.log.info(f"entering text: {value}, with locator: {locator}")
        self.get_element(locator).send_keys(value)

    def get_text(self, locator):
        self.log.info(f"getting text with locator: {locator}")
        return self.get_element(locator).text

    def get_attribute_value(self, locator, attrib):
        self.log.info(f"get attribute: {attrib}, value with locator: {locator}")
        return self.get_element(locator).get_attribute(attrib)

    def select_dropdown_value(self, locator, value):
        self.log.info(f"selecting value: {value}, with locator: {locator}")
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)
