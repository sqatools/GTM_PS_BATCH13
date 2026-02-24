import time

import pytest
from ...Page.locator_file import *
from ...Page.data_file import *
from ...Page.class_file import Practice_Automation
from ...base.selenium import Base_Hitachi

@pytest.mark.usefixtures("get_driver")

class Test_Pratice_Automation_site:

     def test_registration_functionality(self):
         self.tp = Practice_Automation(self.driver)
         self.tp.launch_url(url=web_url)
         self.tp.click_on_My_Account()
         self.tp.enter_Register_Email_Address(Email_Address)
         self.tp.enter_Register_Password(Password_btn)
         self.tp.click_on_Register_btn()
         self.tp.click_sign_out_btn()

     def test_login_functionality(self):
         self.tp = Practice_Automation(self.driver)
         self.tp.enter_Login_username(Login_Username)
         self.tp.enter_login_password(Login_Psd)
         self.tp.click_on_login_button()
         self.tp.click_logout_btn()

