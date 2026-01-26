from ..base.selenium_base import SeleniumBase
from ..Page.locator_file import *

class MockBankPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_url(self,url):
        self.driver.get(url)

    def click_signup(self):
        self.click_element(Sigup_btn)