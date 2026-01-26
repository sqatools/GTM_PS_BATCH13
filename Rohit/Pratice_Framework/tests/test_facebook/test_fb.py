import time

import pytest
from ...Base.selenium import SeleniumBase
from ...Page.locator_file import *
from ...Page.data_file import *
from ...Page.class_file import PracticeFramework

@pytest.mark.usefixtures("get_driver")
class Test_Facebook:

   def test_facebook_account_creation_functionality(self):
       self.fb = PracticeFramework(self.driver)
       self.fb.launch_url(Facebook_URL)
       self.fb.click_create_account(create_new_account_btn)
       self.fb.enter_first_name(First_Name)
       self.fb.enter_last_name(Surname)
       self.fb.select_day(Day)
       self.fb.select_month(Month)
       self.fb.select_year(Year)
       self.fb.click_gender()
       self.fb.enter_mobile_no(Mobile_number)
       self.fb.enter_password(New_Password)
       self.fb.click_signup_button(Sign_up_btn)
       time.sleep(10)