import time
import pytest
from ...page_objects.dummy_sqawebsite.dummy_sqabooking_data import *
from ...page_objects.dummy_sqawebsite.dummysqa_locator import *
from ...page_objects.dummy_sqawebsite.dummy_sqabooking_page import DummySQABookingPage

@pytest.mark.usefixtures("get_driver")
class TestSqaDummybooking:

    def test_sqalogin(self):
        self.bp = DummySQABookingPage(self.driver)
        self.bp.launch_website(url = website_url)
        self.bp.enter_from_city(from_city = from_city_name)
        self.bp.enter_destination_city(dest_city= dest_city_name)
        self.bp.enter_billing_name(bill_name=billing_name)
        self.dp.enter_date_of_birth(user_dob)
        self.dp.select_number_of_travellers(traveller_details)
        self.dp.select_male_radio()
        time.sleep(10)