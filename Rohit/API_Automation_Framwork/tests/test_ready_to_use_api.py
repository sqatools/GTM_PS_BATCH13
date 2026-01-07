from http.client import responses

import pytest
from ..api_objects.read_to_use.read_to_use_api_class import ReadToUseAPI
from ..api_objects.read_to_use.read_to_use_api_data import *

class TestReadyToUseAPI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.r_api = ReadToUseAPI()

    def test_getting_all_objects_and_verify(self):
        response, status_code = self.r_api.get_list_of_all_objects()
        assert len(response) == 13
        assert status_code == 200


    def test_get_specific_object_and_verify(self):
        response, status_code = self.r_api.get_specific_numbers_of_objects(ids_list=object_ids_list)
        assert len(response) == len(object_ids_list)
        assert status_code == 200

    def test_get_single_object_and_verify(self):
        response, status_code = self.r_api.get_single_object(object_id=single_object_id)
        assert isinstance(response, dict)
        assert int(response.get("id")) == single_object_id
        assert status_code == 200
    
