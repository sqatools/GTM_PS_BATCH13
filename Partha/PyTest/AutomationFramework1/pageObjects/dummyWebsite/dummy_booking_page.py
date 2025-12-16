from ...basePackage.selenium_base import SeleniumBase
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
        self.log.info(f"enter dest city name: {dest_city}")
        self.enter_text(dest_city_field, dest_city)

    def enter_billing_name(self, bill_name):
        self.log.info(f"enter the billing name: {bill_name}")
        self.enter_text(billing_name_field, bill_name)

    def enter_billing_phone_number(self, bill_phone_number):
        self.log.info(f"enter the billing phone number: {bill_phone_number}")
        self.enter_text(billing_phone_field, bill_phone_number)

    def enter_dob(self, dob):
        self.log.info(f"Select Date of Birth from Calendar: {dob}")
        self.enter_text(dob_cal, dob)

    def select_gender_radio(self):
        self.log.info(f"Select Female Gender Radio button")
        self.click_element(female_radio_btn)

    def select_no_of_Trav(self,value):
        self.log.info(f"Select number of Travellers from dropdown")
        self.select_dropdown_value(travellers_dropdown, value)