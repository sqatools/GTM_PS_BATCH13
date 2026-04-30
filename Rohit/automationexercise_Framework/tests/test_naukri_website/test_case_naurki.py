import pytest
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
