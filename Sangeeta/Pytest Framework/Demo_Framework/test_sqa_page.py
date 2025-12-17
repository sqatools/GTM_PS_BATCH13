import time

import pytest
from sqatools_login_page import SqaBookingPage
from data_file import *

@pytest.mark.usefixtures("get_driver")
class test_Sqa_Dummy_booking:

    def test_sqalogin(self):
        self.bp = SqaBookingPage(self.driver)
        self.bp.launch_website(url)
        self.bp.enter_from_city(from_city = from_city_name)
        self.bp.enter_destination_city(dest_city= dest_city_name)
        self.bp.enter_billing_name(bill_name=billing_name)
        time.sleep(2)


