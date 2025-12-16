from ...base.selenium_base import SeleniumBase
from .website_locator import *

class WebsitePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def enter_Name(self, name):
        self.enter_text(Name, name)

    def enter_Email(self, email):
        self.enter_text(Email, email)

    def Select_male_radio(self):
        self.click_element(male_radio_btn)

    def enter_Mobile(self, mobile):
        self.enter_text(Mobile, mobile)

    def enter_date_of_birth(self, birthday):
        self.enter_text(dob_calender, birthday)

    def enter_Subjects(self, subj):
        self.enter_text(Subjects, subj)

    def select_Hobbies_Sport_checkbox(self):
        self.click_element(Hobbies_Sports_checkbox)

    def upload_file(self, file_path):
        self.enter_text(Picture_locator, file_path)

    def enter_current_Address(self, address):
        self.enter_text(Current_Address, address)

    def enter_state(self, value):
        self.select_dropdown_value(State, value)

    def enter_city(self, value):
        self.select_dropdown_value(City, value)

    def enter_login_btn(self):
        self.click_element(Login_btn)