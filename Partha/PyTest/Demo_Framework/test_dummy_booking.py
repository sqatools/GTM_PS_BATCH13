import pytest
import time
from dummy_booking_page import DummyBookingPage
from data_file import *

@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:
    def test_dummy_booking_verify(self):
        self.dp = DummyBookingPage(self.driver)
        self.dp.launch_dummy_website(url=website_url)
        self.dp.enter_from_city(from_city=from_city_name)
        self.dp.enter_destination_city(dest_city=dest_city_name)
        self.dp.enter_billing_name(bill_name=billing_name)
        self.dp.enter_billing_phone_number(bill_phone_number=billing_phone)
        time.sleep(10)