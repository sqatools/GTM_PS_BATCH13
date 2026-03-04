from http.client import responses
import pytest
from ..API_Objects.read_data.class_file import API_class
from ..API_Objects.read_data.data_file import *

class TestAPI:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.r_api = API_class(driver)

    def test_get_all_product_lits(self):
        res, status_code = self.r_api.get_All_Products_List()
        assert status_code == 200




