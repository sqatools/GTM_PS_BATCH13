from selenium_base import SeleniumBase
from Registrator_Page_locator import *

class AutomationRegistrationPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def lauch_Automation_Regitration_website(self, url):
        self.driver.get(url)

    def enter_First_name(self,first_name):
        self.enter_text(First_name, first_name)

    def enter_Last_name(self,last_name):
        self.enter_text(Last_name, last_name)

    def enter_Address(self, address):
        self.enter_text(Address, address)

    def enter_Email(self, email):
        self.enter_text(Email_address, email)

    def enter_Phone(self, phone):
        self.enter_text(Phone, phone)

    def select_male_radio(self):
        self.click_element(male_radio_btn)

    def select_cricket_checkbox(self):
        self.click_element(Cricket_check_box)

    def enter_Language(self, language):
        self.select_from_dropdown_list(Language_dropdown, Language_options, language)

    def enter_Skills(self, skills):
        self.select_dropdown_by_text(Skills_dropdown,skills)

