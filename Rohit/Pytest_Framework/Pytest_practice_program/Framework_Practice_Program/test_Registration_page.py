import time

import pytest

from Automation_Registration_page import AutomationRegistrationPage
from data_file import *

@pytest.mark.usefixtures("get_driver")

class TestRegistrationPage:
    def test_registration_page(self):
        self.rp = AutomationRegistrationPage(self.driver)
        self.rp.lauch_Automation_Regitration_website(url=website_url)
        self.rp.enter_First_name(first_name=First_name)
        self.rp.enter_Last_name(last_name=Last_name)
        self.rp.enter_Address(address=Address)
        self.rp.enter_Email(email=Email_address)
        self.rp.enter_Phone(phone=Phone)
        time.sleep(5)
        self.rp.select_male_radio()
        time.sleep(5)
        self.rp.select_cricket_checkbox()
        time.sleep(5)
        self.rp.enter_Language(language=Language)
        time.sleep(5)
        self.rp.enter_Skills(skills="Linux")
        time.sleep(10)
