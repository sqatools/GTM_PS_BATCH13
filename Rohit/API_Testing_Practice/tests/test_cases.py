import pytest
from ..base.API_base import APIBASE
from ..API_Page_object.API_class import API_Page_object
from ..API_Page_object.API_data import *

class Test_API_Automation:

    @pytest.fixture(scope="function",autouse=True)
    def get_setup(self):
        self.A_api = API_Page_object()


    def test_get_login_details(self):
        response, status_code = self.A_api.get_user_login_details()
        assert status_code == 200
