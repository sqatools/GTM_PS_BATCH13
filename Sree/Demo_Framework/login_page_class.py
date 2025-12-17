from selenium_base import Seleniumbase
from Login_page_locator import *

class LoginPage(Seleniumbase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_login_page(self, login_url):
        self.driver.get(login_url)

    def enter_username(self, username):
        self.enter_text(username_field, username)

    def enter_password(self, password):
        self.enter_text(password_field, password)

    def click_login_button(self):
        self.click_element(login_button)