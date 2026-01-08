import pytest
from ...api_objects.read_to_use.read_to_use_api_class import ReadyToUseAPI
from ...api_objects.read_to_use.read_to_use_api_data import *


class TestReadyToUseAPI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.r_api = ReadyToUseAPI()

    @pytest.mark.smoke
    def test_get_all_objects_and_verify(self):
        response, st_code = self.r_api.get_list_of_all_objects()
        assert len(response) == 13
        assert st_code == 200

    @pytest.mark.sanity
    def test_get_specific_object_and_verify(self):
        response, st_code = self.r_api.get_specific_numbers_of_objects(ids_list=object_ids_list)
        assert len(response) == len(object_ids_list)
        assert st_code == 200 and response[0]['id'] in object_ids_list
