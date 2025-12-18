from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Seleniumbase:
    def __init__(self,driver,timeout=30):
        self.driver=driver
        self.wait=WebDriverWait(driver,timeout=timeout)
    def get_element(self,locator):
        return self.wait.until(ec.presence_of_element_located(locator))
    def click_element(self,locator):
        self.get_element(locator).click()
    def enter_text(self,locator,value):
        self.get_element(locator).send_keys(value)
    def get_text(self,locator):
        return self.get_element(locator).text
    def get_attribute_value(self,locator,attrib):
        return self.get_element(locator).get_attribute(attrib)
class WebdriverFactory:
    def __init__(self, browser, headless=False):
        self.browser = browser.lower()
        self.headless = headless

    def get_driver_instance(self):

        if self.browser == "chrome":
            options = ChromeOptions()
            if self.headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=options)

        elif self.browser == "firefox":
            options = FirefoxOptions()
            options.headless = self.headless
            driver = webdriver.Firefox(options=options)

        elif self.browser == "edge":
            options = EdgeOptions()
            if self.headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
            driver = webdriver.Edge(options=options)

        else:
            raise ValueError(f"Unsupported browser: {self.browser}")

        return driver