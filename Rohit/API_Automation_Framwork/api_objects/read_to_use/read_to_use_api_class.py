from ...base.api_base import APIBase
from .read_to_use_api_data import *

class ReadToUseAPI(APIBase):

    def get_list_of_all_objects(self):
        self.log.info("initiated method : get_list_of_all_objects")
        response, status_code = self.get_method(url=server_url)
        return response, status_code

    def get_specific_numbers_of_objects(self, ids_list):
        self.log.info("initiated method : get_specific_numbers_of_objects")
        new_server_url = f"{server_url}?"
        for id in ids_list:
            new_server_url = new_server_url + f"id={id}&"
        # Example final URL: "https://api.restful-api.dev/objects?id=3&id=5&id=10"
        response, status_code = self.get_method(url=new_server_url)
        return response, status_code

    def get_single_object(self, object_id):
        self.log.info("initiated method : get_single_object")
        new_server_url = f"{server_url}/{object_id}"
        response, status_code = self.get_method(url=new_server_url)
        return response, status_code

