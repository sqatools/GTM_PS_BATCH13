from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_option
from selenium.webdriver.firefox.options import Options as firefox_option
from selenium.webdriver.edge.options import Options as edge_option

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
    def __init__(self,browser,headles=False):
        self.browser=browser
        self.headless=headles
    def get_driver_instance(self):
        driver=None
        if self.browser.lower()=='chrome':
            opt=chrome_option()
            if self.headless:
                opt.add_argument("--headless")
            driver= webdriver.Chrome(options=opt)
        elif self.browser.lower()=='firefox':
            opt=firefox_option()
            if self.headless:
                opt.add_argument("--headless")
            driver=webdriver.Firefox(options=opt)
        elif self.browser.lower()=='edge':
            opt=edge_option()
            if self.headless:
                opt.add_argument("--headless")
            driver =webdriver.Edge(options=opt)
        driver.maximize_window()
        return driver
