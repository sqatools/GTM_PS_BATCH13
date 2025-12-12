from selenium_base import Seleniumbase
from dummy_booking_page_locator import *

class DummyBookingPage(Seleniumbase):
    def __init__(self,driver):
        super().__init__(driver)
    def launch_dummy_website(self,url):
        self.driver.get(url)
    def enterfromcity(self,fromcity):
        self.enter_text(from_city_field,fromcity)
    def enterdistination(self,destinationcity):
        self.enter_text(dest_city_field,destinationcity)
    def enterbillingname(self,billname):
        self.enter_text(billing_name_field,billname)
