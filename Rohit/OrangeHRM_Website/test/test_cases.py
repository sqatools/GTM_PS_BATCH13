import time
from ..Page_object.class_file import OrangeHRM
from ..Page_object.locator import *
from ..Page_object.data_file import *

import pytest

@pytest.mark.usefixtures('get_driver')

class Test_Orange_website:

    def test_login_functionality(self):
        self.Orange = OrangeHRM(self.driver)
        self.Orange.lanuch_url(url)
        self.Orange.enter_user_name(user_name)
        self.Orange.enter_password(Password)
        self.Orange.click_login()
        time.sleep(10)


    def test_recruitment_functionality(self):
        self.Orange = OrangeHRM(self.driver)
        self.Orange.click_recruitment()
        self.Orange.select_Job_title()
        time.sleep(5)
        self.Orange.select_Vacancy()
        self.Orange.select_Hiring_Manager()
        self.Orange.select_Status()
        self.Orange.select_Candidate_Name()
        self.Orange.select_Keywords()
        self.Orange.select_start_Date_of_Application()
        self.Orange.select_end_Date_of_Application()
        self.Orange.select_Method_of_Application()
        time.sleep(10)