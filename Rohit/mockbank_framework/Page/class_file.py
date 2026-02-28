from ..Page.locator_file import *
from ..base.selenium import Base_Hitachi

class Practice_Automation(Base_Hitachi):
    def __init__(self,driver):
        super().__init__(driver)

    def launch_url(self,url):
        self.driver.get(url)

    def click_on_My_Account(self):
        self.click_element(My_Account)

    def enter_Register_Email_Address(self,email_add):
        self.enter_text(Email_Address,email_add)

    def enter_Register_Password(self,password):
        self.enter_text(Password_btn,password)

    def click_on_Register_btn(self):
        self.click_element(Register_btn)

    def click_sign_out_btn(self):
        self.click_element(Sign_out_btn)

    # Login
    def enter_Login_username(self,Lg_user_name):
        self.enter_text(Login_Username,Lg_user_name)

    def enter_login_password(self,password):
        self.enter_text(Login_Psd,password)

    def click_on_login_button(self):
        self.click_element(Login_btn)

    def click_logout_btn(self):
        self.click_element(Logout_btn)