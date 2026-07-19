from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class NaukriSelenium:
    def __init__(self,driver,timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self,locator):
        self.get_element(locator).click()

    def enter_text(self,locator,text):
        self.get_element(locator).send_keys(text)

    def element(self,locator):
        return self.get_element(locator).text

    def drop_down(self,locator,value):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)

    def select_years_from_drop_down(self, select_years_dp, value):
        self.get_element(select_years_dp).click()
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()