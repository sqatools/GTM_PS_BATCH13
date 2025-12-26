from ...base.api_base import APIBase
from .restful_api_data import *


class RestfulAPI(APIBase):

    def get_list_of_all_objects(self):
        self.log.info("Initiated method: get_list_of_all_objects")
        response, st_code = self.get_method(url=server_url)
        return response, st_code

    def get_specific_object(self, object_id):
        self.log.info(f"Initiated method: get_specific_object with id {object_id}")
        url = f"{server_url}/{object_id}"
        response, st_code = self.get_method(url=url)
        return response, st_code

    def create_object(self, data):
        self.log.info("Initiated method: create_object")
        response, st_code = self.post_method(url=server_url, payload=data)
        return response, st_code

    def update_object(self, object_id, data):
        self.log.info(f"Initiated method: update_object with id {object_id}")
        url = f"{server_url}/{object_id}"
        response, st_code = self.put_method(url=url, payload=data)
        return response, st_code

    def partial_update_object(self, object_id, data):
        self.log.info(f"Initiated method: partial_update_object with id {object_id}")
        url = f"{server_url}/{object_id}"
        response, st_code = self.patch_method(url=url, payload=data)
        return response, st_code

    def delete_object(self, object_id):
        self.log.info(f"Initiated method: delete_object with id {object_id}")
        url = f"{server_url}/{object_id}"
        response, st_code = self.delete_method(url=url)
        return response, st_code