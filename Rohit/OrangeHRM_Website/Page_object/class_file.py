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
        self.click_element(Login_btn)


    #recruitment
    def click_recruitment(self):
        self.click_element(Recruitment)

    def select_Job_title(self):
        self.click_element(Job_title)

    def select_Vacancy(self):
        self.click_element(Job_title)

    def select_Hiring_Manager(self):
        self.click_element(Hiring_Manager)

    def select_Status(self):
        self.click_element(Status)

    def select_Candidate_Name(self):
        self.click_element(Candidate_Name)

    def select_Keywords(self):
        self.click_element(Keywords)

    def select_start_Date_of_Application(self):
        self.click_element(start_Date_of_Application)

    def select_end_Date_of_Application(self):
        self.click_element(end_Date_of_Application)

    def select_Method_of_Application(self):
        self.click_element(Method_of_Application)