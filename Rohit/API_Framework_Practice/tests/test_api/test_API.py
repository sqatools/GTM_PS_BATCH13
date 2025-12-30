import pytest
from ...api_objects.api_class import API
from ...api_objects.api_datafile import *

class TestAPI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.r_api = API()


    def test_get_single_objects_and_Verify(self):
        response, status_code = self.r_api.get_single_object("7")
        assert len(response)== 13
        assert status_code == 200