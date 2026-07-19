import time

import pytest

from ...Page_objects.naukri_flow.naukri_locator import select_years_dp
from ...base.Naukriselenium import NaukriSelenium
from ...Page_objects.naukri_flow.naukri_datafile import *
from ...Page_objects.naukri_flow.naukri_datafile import *
from ...Page_objects.naukri_flow.naukri_class import Automation

@pytest.mark.usefixtures("get_driver_with_headless")

class Test_Naukri_Website:

    def test_naulri_login_functionality(self):
        self.naukri = Automation(self.driver)
        self.naukri.launch_naukri_url()
        self.naukri.click_naulkri_login()
        self.naukri.enter_naukri_username(nk_username)
        self.naukri.enter_naukri_password(nk_password)
        self.naukri.click_naukri_loginbtn()


    def test_search_profile_functionality(self):
        self.naukri = Automation(self.driver)
        self.naukri.click_on_serach_button()
        self.naukri.enter_keyword(enter_Keyword)
        self.naukri.click_select_experience()
        self.naukri.select_years_from_drop_down(select_years_dp,"10 years")
        self.naukri.enter_location(enter_location)
        self.naukri.click_serach_btn()
        time.sleep(10)
