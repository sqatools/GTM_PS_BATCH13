from ..base.api_base import APIRequest
from ..api_objects.api_datafile import *
import json

class API(APIRequest):

      def get_single_object(self, object_id=None):
          self.log.info("initiated method : get_single_object")
          use_id = object_id if object_id is not None else single_object_id
          new_server_url = f"{server_url}/{use_id}"
          response, status_code = self.get_method(url=new_server_url)
          return response, status_code

      def add_object(self, payload=None):
          """Create a new object via POST /objects. If `payload` is None,
          uses `new_object_payload` from the datafile.
          Returns (response_json, status_code).
          """
          self.log.info("initiated method : add_object")
          use_payload = payload if payload is not None else new_object_payload
          headers = {"Content-Type": "application/json"}
          response, status_code = self.post_method(url=server_url, headers=headers, payload=json.dumps(use_payload))
          return response, status_code

      def update_object(self, object_id=None, payload=None, method="put"):
          """Update an existing object. `method` can be 'put' or 'patch'.
          If `object_id` is None, uses `update_object_id` from datafile.
          If `payload` is None, uses corresponding payload from datafile.
          """
          self.log.info("initiated method : update_object")
          use_id = object_id if object_id is not None else update_object_id
          if payload is None:
              use_payload = update_object_payload_put if method == "put" else update_object_payload_patch
          else:
              use_payload = payload
          new_server_url = f"{server_url}/{use_id}"
          headers = {"Content-Type": "application/json"}
          if method == "put":
              response, status_code = self.put_method(url=new_server_url, headers=headers, payload=json.dumps(use_payload))
          else:
              response, status_code = self.patch_method(url=new_server_url, headers=headers, payload=json.dumps(use_payload))
          return response, status_code

      def patch_object(self, object_id=None, payload=None):
          """Convenience wrapper for partial update via PATCH."""
          return self.update_object(object_id=object_id, payload=payload, method="patch")

      def delete_object(self, object_id=None):
          """Delete an object by id. Returns (response_json_or_empty, status_code)."""
          self.log.info("initiated method : delete_object")
          use_id = object_id if object_id is not None else delete_object_id
          new_server_url = f"{server_url}/{use_id}"
          response, status_code = self.delete_method(url=new_server_url)
          return response, status_code





