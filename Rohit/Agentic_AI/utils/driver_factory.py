"""
Driver Factory

Supports:
Chrome
Edge
Headless Chrome
"""

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome"):

        if browser.lower() == "chrome":

            options = Options()

            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(
                options=options
            )

            return driver

        if browser.lower() == "headless":

            options = Options()

            options.add_argument("--headless")

            driver = webdriver.Chrome(
                options=options
            )

            return driver

        return webdriver.Chrome()