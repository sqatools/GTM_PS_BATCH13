import time

import pytest
#from dummy_booking_page import DummyBookingPage
from ...page_objects.dummy_website.dummy_booking_page import DummyBookingPage
from ...page_objects.dummy_website.dummy_booking_page_data import *
#from page_objects.dummy_website.dummy_booking_page_data import *
#from data_file import *

@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:

    def test_dummy_booking_verify(self):
        self.dp = DummyBookingPage(self.driver)
        self.dp.launch_dummy_website(url=website_url)
        self.dp.enter_from_city(from_city=from_city_name)
        self.dp.enter_destination_city(dest_city=dest_city_name)
        self.dp.enter_billing_name(bill_name=billing_name)
        self.dp.enter_date_of_birth(user_dob)
        self.dp.select_number_of_travellers(traveller_details)
        self.dp.select_male_radio()
        time.sleep(10)

