import pytest
import time
from ..pageObjects.dummyWebsite.dummy_booking_page import DummyBookingPage
from ..pageObjects.dummyWebsite.dummy_booking_data_file import *

@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:
    def test_dummy_booking_verify(self):
        self.dp = DummyBookingPage(self.driver)
        self.dp.launch_dummy_website(url=website_url)
        self.dp.enter_from_city(from_city=from_city_name)
        self.dp.enter_destination_city(dest_city=dest_city_name)
        self.dp.enter_dob(user_dob)
        self.dp.select_no_of_Trav(traveller_details)
        self.dp.select_gender_radio()
        self.dp.enter_billing_name(bill_name=billing_name)
        self.dp.enter_billing_phone_number(bill_phone_number=billing_phone)
        time.sleep(10)