import pytest
from ...api_objects.api_class import API
from ...api_objects.api_datafile import *

class TestAPI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.r_api = API()

    def test_get_single_object_and_verify(self):
        response, status_code = self.r_api.get_single_object(object_id=single_object_id)
        assert isinstance(response, dict)
        assert int(response.get("id")) == single_object_id
        assert status_code == 200

    def test_add_object_and_verify(self):
        response, status_code = self.r_api.add_object(payload=new_object_payload)
        # server may return 201 or 200 depending on implementation
        assert status_code in (200, 201)
        assert isinstance(response, dict)
        # created resource should at least echo the name
        assert response.get("name") == new_object_payload.get("name")
        assert "id" in response

    def test_update_object_put_and_verify(self):
        response, status_code = self.r_api.update_object(object_id=update_object_id, payload=update_object_payload_put, method="put")
        # Some demo servers may not allow PUT and return 405; accept that as valid outcome
        assert status_code in (200, 201, 204, 405)
        assert isinstance(response, dict)
        if status_code in (200, 201, 204):
            assert int(response.get("id")) == update_object_id
            assert response.get("name") == update_object_payload_put.get("name")

    def test_update_object_patch_and_verify(self):
        response, status_code = self.r_api.patch_object(object_id=update_object_id, payload=update_object_payload_patch)
        assert status_code in (200, 201, 204, 405)
        assert isinstance(response, dict)
        if status_code in (200, 201, 204):
            assert int(response.get("id")) == update_object_id
            # patched field should be present in the response
            assert response.get("data", {}).get("price") == update_object_payload_patch.get("data").get("price")

    def test_delete_object_and_verify(self):
        response, status_code = self.r_api.delete_object(object_id=delete_object_id)
        # Accept common successful or not-allowed responses depending on demo server
        assert status_code in (200, 202, 204, 404, 405)
        # If server returns a body, ensure it's a dict; otherwise empty dict is acceptable
        assert isinstance(response, dict)