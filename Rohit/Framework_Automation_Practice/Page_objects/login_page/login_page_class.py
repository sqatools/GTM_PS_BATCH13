from ...base.selenium_base import SeleniumBase
from ..login_page.login_locator import *

class login_Page(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def launch_login_page(self,url):
        self.driver.get(url)

    def user_name(self,username):
        self.enter_text(Username,username)

    def user_password(self,psd):
        self.enter_text(Password,psd)

    def click_submit(self):
        self.click_element(login_Submit)

    def click_contact(self):
        self.click_element(Contact_tab)

    def enter_First_name(self,first_name):
        self.enter_text(First_name, first_name)

    def enter_Last_name(self,last_name):
        self.enter_text(Last_name, last_name)

    def enter_email(self,email):
        self.enter_text(Email, email)

    def enter_message(self,message):
        self.enter_text(Message, message)

    def click_contact_Submit(self):
        self.click_element(Contact_Submit)

