import time

import pytest
from ..Base.selenium import Selenium_Base
from ..Page_objects.class_file import Practice_Automation
from ..Page_objects.locator import *
from ..Page_objects.Data_file import *

@pytest.mark.usefixtures("get_Driver")

class Test_Website:

    def test_GUI_Element_Functionality(self):
        self.test = Practice_Automation(self.driver)
        self.test.launch_url(url)
        self.test.enter_name(name)
        self.test.enter_email(email)
        self.test.enter_phone(phone)
        self.test.enter_address(address)
        self.test.Click_Gender()
        self.test.Click_Day()
        self.test.select_country(country_name)
        time.sleep(10)
