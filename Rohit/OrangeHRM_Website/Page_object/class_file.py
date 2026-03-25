from ..base.selenium import SeleniumBase
from ..Page_object.locator import *


class OrangeHRM(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def lanuch_url(self,url):
        self.driver.get(url)

    def enter_user_name(self,username):
        self.enter_text(user_name,username)

    def enter_password(self,Psd):
        self.enter_text(Password,Psd)

    def click_login(self):
        self.click_element(Password)