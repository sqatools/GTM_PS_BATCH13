from ..Base.selenium import Selenium_Base
from ..Page_objects.locator import *

class Practice_Automation(Selenium_Base):
    def __init__(self,driver):
        super().__init__(driver)

    def launch_url(self,url):
        self.driver.get(url)

    def enter_name(self,name):
        self.enter_text(Name,name)

    def enter_email(self,email):
        self.enter_text(Email,email)

    def enter_phone(self,phone):
        self.enter_text(Phone,phone)

    def enter_address(self,address):
        self.enter_text(Address,address)

    def Click_Gender(self):
        self.click_element(Gender_Male)

    def Click_Day(self):
        self.click_element(Day_Wednesday)

    def select_country(self,country_name):
        self.select_Drop_down(Country,country_name)