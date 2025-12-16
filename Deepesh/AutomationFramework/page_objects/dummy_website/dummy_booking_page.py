# from selenium_base import SeleniumBase
from ...base.selenium_base import SeleniumBase
# from base.selenium_base import SeleniumBase
from .dummy_booking_page_locator import *


class DummyBookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_dummy_website(self, url):
        self.log.info(f"Launch website url: {url}")
        self.driver.get(url)

    def enter_from_city(self, from_city):
        self.log.info(f"enter from city name: {from_city}")
        self.enter_text(from_city_field, from_city)

    def enter_destination_city(self, dest_city):
        self.log.info(f"enter destination city name: {dest_city}")
        self.enter_text(dest_city_field, dest_city)

    def enter_billing_name(self, bill_name):
        self.log.info(f"enter billing name: {bill_name}")
        self.enter_text(billing_name_field, bill_name)

    def enter_date_of_birth(self, dob):
        self.log.info(f"select date of birth: {dob}")
        self.enter_text(dob_calender, dob)

    def select_male_radio(self):
        self.log.info(f"select male radio button")
        self.click_element(male_radio_btn)

    def select_number_of_travellers(self, value):
        self.log.info(f"select number of travellers")
        self.select_dropdown_value(travellers_dropdown, value)
