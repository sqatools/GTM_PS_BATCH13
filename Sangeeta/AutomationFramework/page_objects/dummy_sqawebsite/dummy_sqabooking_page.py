from ...basepg.selenium_base import SeleniumBase
from .dummysqa_locator import *

class DummySQABookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_dummy_website(self, url):
        self.driver.get(url)

    def enter_from_city(self, from_city):
        self.enter_text(from_city_field, from_city)

    def enter_destination_city(self, to_city):
        self.enter_text(dest_city_field, to_city)

    def enter_billing_name(self, bill_name):
        self.enter_text(billing_name_field, bill_name)

    def enter_date_of_birth(self, dob):
        self.enter_text(dob_calender, dob)

    def select_male_radio(self):
        self.click_element(male_radio_btn)