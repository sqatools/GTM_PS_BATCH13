import pytest
from ...api_objects.restful_api.restful_api_class import RestfulAPI
from ...api_objects.restful_api.restful_api_data import *


class TestRestfulAPI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.r_api = RestfulAPI()

    @pytest.mark.smoke
    def test_get_all_objects(self):
        response, st_code = self.r_api.get_list_of_all_objects()
        assert isinstance(response, list)
        assert st_code == 200

    @pytest.mark.sanity
    def test_get_specific_object(self):
        # Assuming object with id 1 exists
        response, st_code = self.r_api.get_specific_object(1)
        assert isinstance(response, dict)
        assert st_code == 200
        assert 'id' in response

    @pytest.mark.regression
    def test_create_object(self):
        response, st_code = self.r_api.create_object(sample_object_data)
        assert isinstance(response, dict)
        assert st_code == 200 or st_code == 201
        assert 'id' in response

    @pytest.mark.regression
    def test_update_object(self):
        # First create an object to update
        create_response, create_code = self.r_api.create_object(sample_object_data)
        assert create_code == 200 or create_code == 201
        object_id = create_response['id']

        # Now update it
        update_response, update_code = self.r_api.update_object(object_id, sample_object_data)
        assert update_code == 200
        assert update_response['name'] == sample_object_data['name']

    @pytest.mark.regression
    def test_partial_update_object(self):
        # First create an object
        create_response, create_code = self.r_api.create_object(sample_object_data)
        assert create_code == 200 or create_code == 201
        object_id = create_response['id']

        # Partial update
        patch_response, patch_code = self.r_api.partial_update_object(object_id, partial_update_data)
        assert patch_code == 200
        assert patch_response['name'] == partial_update_data['name']

    def test_delete_object(self):
        # First create an object
        create_response, create_code = self.r_api.create_object(sample_object_data)
        assert create_code == 200 or create_code == 201
        object_id = create_response['id']

        # Delete it
        delete_response, delete_code = self.r_api.delete_object(object_id)
        assert delete_code == 200 or delete_code == 204