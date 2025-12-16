import time

import pytest
#from dummy_booking_page import DummyBookingPage
#from data_file import *
#from ...Page_objects.dummy_website.dummy_booking_page import DummyBookingPage
#from ...Page_objects.dummy_website.data_file import *

from ...page_objects.dummy_website.dummy_booking_page import DummyBookingPage
from ...page_objects.dummy_website.data_file import *

@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:
      def test_dummy_booking_verify(self):
          self.dp = DummyBookingPage(self.driver)
          self.dp.launch_dummy_website(url=website_url)
          self.dp.enter_from_city(from_city=from_city_name)
          self.dp.enter_destination_city(dest_city=dest_city_name)
          self.dp.enter_billing_name(bill_name=billing_name)
          time.sleep(10)
          self.dp.enter_date_of_birth(user_dob)
          self.dp.enter_number_of_travellers(traveller_details)
          self.dp.select_male_radio()
          time.sleep(10)



#PS C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\AutomationFramework> python -m pytest -v .\tests\dummy_booking\test_dummy_booking.py

#python -m pytest -v .\tests\dummy_booking\test_dummy_booking.py  -> Always try to execute from root directory
