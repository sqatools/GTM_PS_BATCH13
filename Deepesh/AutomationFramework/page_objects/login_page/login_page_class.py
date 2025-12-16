from ...base.selenium_base import SeleniumBase
from .login_page_locator import *


class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(username_field, username)

    def enter_password(self, password):
        self.enter_text(password_field, password)

    def click_login_button(self):
        self.click_element(login_button)
