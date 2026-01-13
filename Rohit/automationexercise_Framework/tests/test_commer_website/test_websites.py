import time

import pytest
from ...Page_objects.Commer_website.locator_file import *
from ...Page_objects.Commer_website.data_file import *
from ...Page_objects.Commer_website.class_file import CommerWebsite

@pytest.mark.usefixtures("setup")

class Test_Commer_Website:

      def test_Signup_functionality(self):
          self.comm = CommerWebsite(self.driver)
          self.comm.launch_url(url=website_url)
          self.comm.enter_User_Name(User_Name)
          self.comm.enter_User_Email_address(User_Email_address)
          self.comm.click_signup_button()
          time.sleep(10)
          self.comm.click_select_MR()
          self.comm.enter_password(Password)
          self.comm.select_date(Date)
          self.comm.select_month(Month)
          self.comm.select_year(Year)
          self.comm.click_specail_offer_checkbox()
          self.comm.enter_First_Name(First_Name)
          self.comm.enter_Last_Name(Last_Name)
          self.comm.enter_company_name(Company)
          self.comm.enter_address(Address)
         # self.comm.select_country(Country)
          self.comm.enter_state(State)
          self.comm.enter_city(City)
          self.comm.enter_zipocde(Zipcode)
          self.comm.enter_mobile(Mobile_number)
          self.comm.click_Create_Account_button()
          self.comm.click_continue_button()