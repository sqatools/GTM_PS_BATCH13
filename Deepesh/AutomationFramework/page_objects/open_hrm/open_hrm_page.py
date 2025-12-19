from ...base.selenium_base import SeleniumBase
from .open_hrm_page_locator import *

class LoginPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def launch_open_hrl(self, url):
        self.driver.get(url)

    def login_to_open_hrml(self, usernm, passwd):
        self.enter_text(login_page_locator.username_field, usernm)
        self.enter_text(login_page_locator.password_field, passwd)
        self.click_element(login_page_locator.login_button)

    def get_dashboard_heading(self):
        return self.get_text(admin_page_locator.dashboard_heading)


class AdminPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_admin_page(self):
        self.click_element(admin_page_locator.admin_side_menu)

    def add_user(self):
        self.click_element(admin_page_locator.add_user_button)
        self.click_element(admin_page_locator.user_role_dropdown)






