"""
Selenium Tool

Reusable Selenium Operations
"""

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


class SeleniumTool:

    def __init__(self):

        options = Options()

        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(

            options=options

        )

    def open_url(

        self,

        url

    ):

        self.driver.get(url)

    def click(

        self,

        locator

    ):

        self.driver.find_element(

            By.XPATH,

            locator

        ).click()

    def enter_text(

        self,

        locator,

        value

    ):

        self.driver.find_element(

            By.XPATH,

            locator

        ).send_keys(value)

    def get_text(

        self,

        locator

    ):

        return self.driver.find_element(

            By.XPATH,

            locator

        ).text

    def take_screenshot(

        self,

        name

    ):

        self.driver.save_screenshot(

            f"screenshots/{name}.png"

        )

    def close_browser(self):

        self.driver.quit()