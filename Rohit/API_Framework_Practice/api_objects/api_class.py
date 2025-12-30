from ..base.api_base import APIRequest
from ..api_objects.api_datafile import *

class API(APIRequest):

      def get_single_object(self):
          self.log.info("initiated method : get_single_object")
          new_server_url = f"{server_url}/{object_id}"
          response, status_code = self.get_method(url=new_server_url)
          return response, status_code

