from ...base.Naukriselenium import NaukriSelenium
from ...Page_objects.naukri_flow.naukri_locator import *
from ...Page_objects.naukri_flow.naukri_datafile import *

class Automation(NaukriSelenium):
    def __init__(self,driver):
        super().__init__(driver)

    def launch_naukri_url(self):
        self.driver.get(Naukri_Url)

    def click_naulkri_login(self):
        self.click_element(Login_btn)

    def enter_naukri_username(self,nkusername):
        self.enter_text(Naukri_User_name,nkusername)

    def enter_naukri_password(self,nkpassword):
        self.enter_text(Naukri_Password,nkpassword)

    def click_naukri_loginbtn(self):
        self.click_element(Naukri_login_btn)