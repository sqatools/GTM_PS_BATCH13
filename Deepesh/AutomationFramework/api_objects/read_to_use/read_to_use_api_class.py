from ...base.api_base import APIBase
from .read_to_use_api_data import *


class ReadyToUseAPI(APIBase):

    def get_list_of_all_objects(self):
        self.log.info("initiated method: get_list_of_all_objects ")
        response, st_code = self.get_method(url=server_url)
        return response, st_code

    def get_specific_numbers_of_objects(self, ids_list):
        self.log.info("initiated method: get_specific_numbers_of_objects ")
        new_server_url = f"{server_url}?"
        for id in ids_list:
            new_server_url = new_server_url + f"id={id}&"
        # "https://api.restful-api.dev/objects?id=3&id=5&id=10"
        response, st_code = self.get_method(url=new_server_url)
        return response, st_code


