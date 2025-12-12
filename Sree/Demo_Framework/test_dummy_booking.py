import time

import pytest
from dummy_booking_page import DummyBookingPage
from data_file import *

@pytest.mark.usefixtures("get_driver")
class Testdummybooking:

    def test_dummy_booking_verify(self):
        self.obj=DummyBookingPage(self.driver)
        self.obj.launch_dummy_website(url=website_url)
        self.obj.enterfromcity(fromcity=from_city_name)
        self.obj.enterdistination(destinationcity=dest_city_name)
        self.obj.enterbillingname(billname=billing_name)
        time.sleep(10)