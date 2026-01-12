import time

import pytest
from ...Page_objects.Commer_website.locator_file import *
from ...Page_objects.Commer_website.data_file import *
from ...Page_objects.Commer_website.class_file import CommerWebsite

@pytest.mark.usefixtures("get_driver")

class Test_Commer_Website:

      def test_Signup_functionality(self):
          self.comm = CommerWebsite(self.driver)
          self.comm.launch_url(url=website_url)
          self.comm.enter_User_Name(User_Name)
          self.comm.enter_User_Email_address(User_Email_address)
          self.comm.click_signup_button()
          time.sleep(10)