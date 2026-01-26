from ..Base.selenium import SeleniumBase
from ..Page.locator_file import *

class PracticeFramework(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)


    def launch_url(self,url):
        self.driver.get(url)

    def click_create_account(self,create_new_account_btn):
        self.click_element(create_new_account_btn)

    def enter_first_name(self,fname):
        self.enter_text(First_Name,fname)

    def enter_last_name(self,lname):
        self.enter_text(Surname,lname)

    def select_day(self,day):
        self.enter_text(Day,day)

    def select_month(self,month):
        self.enter_text(Month,month)

    def select_year(self,year):
        self.enter_text(Year,year)

    def click_gender(self):
        self.click_element(Gender)

    def enter_mobile_no(self,mb):
        self.enter_text(Mobile_number,mb)

    def enter_password(self,np):
        self.enter_text(New_Password,np)

    def click_signup_button(self,signup_btn):
       self.click_element(signup_btn)
