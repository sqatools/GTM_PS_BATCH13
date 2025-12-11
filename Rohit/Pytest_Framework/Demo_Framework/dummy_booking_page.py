from selenium_base import SeleniumBase
from dummy_booking_page_locator import *

class DummyBookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_dummy_website(self, url):
        self.driver.get(url)

    def enter_from_city(self, from_city):
        self.enter_text(from_city_field, from_city)

    def enter_destination_city(self, dest_city):
        self.enter_text(dest_city_field, dest_city)

    def enter_billing_name(self, bill_name):
        self.enter_text(billing_name_field, bill_name)