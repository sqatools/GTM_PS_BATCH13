from Rohit.Framework_Project.Page_objects.banking_website.banking_website_locator import Username, Password
from ...base.selenium_base import SeleniumBase
from ..Open_HRM_website.Open_HRM_locator import *

class Open_HRM_Login(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def launch_open_HRM_website(self, url):
        self.driver.get(url)

    def login_to_open_HRM_website(self,usernm,psd):
        self.enter_text(Open_HRM_Login_locator.Username,usernm)
        self.enter_text(Open_HRM_Login_locator.Password,psd)
        self.click_element(Open_HRM_Login_locator.Login_btn)

    def get_dashboard_heading(self):
        return self.get_text()

class AdminPage(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def navigate_to_admin_page(self):
        self.click_element()

    def add_user(self):
        pass