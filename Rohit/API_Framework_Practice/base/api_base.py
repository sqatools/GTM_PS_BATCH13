import requests
import logging

class APIRequest:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url , headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.log.info(f"Method Name : get method")
        self.log.info(f"url : {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {response.status_code}")
        return response.json(), response.status_code

    def post_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("POST", url, headers=headers, data=payload)
        self.log.info(f"Method Name : post method")
        self.log.info(f"url : {url}")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"response : {response}")
        self.log.info(f"status_code : {response.status_code}")
        return response.json(), response.status_code

    def put_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.log.info(f"Method Name : put method")
        self.log.info(f"url : {url}")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"response : {response}")
        self.log.info(f"status_code : {response.status_code}")
        return response.json(), response.status_code

    def patch_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("PATCH", url, headers=headers, data=payload)
        self.log.info(f"Method Name : patch method")
        self.log.info(f"url : {url}")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"response : {response}")
        self.log.info(f"status_code : {response.status_code}")
        return response.json(), response.status_code

    def delete_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        self.log.info(f"Method Name : delete method")
        self.log.info(f"url : {url}")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"response : {response}")
        self.log.info(f"status_code : {response.status_code}")
        # Some DELETE endpoints return no JSON body; attempt to json() safely
        try:
            return response.json(), response.status_code
        except ValueError:
            return {}, response.status_code