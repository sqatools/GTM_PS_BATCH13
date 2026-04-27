import requests
import logging
import json

class API_Base:
    def __init__(self,driver):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, headers=None, payload=None):
        response = requests.get(url, headers=headers, params=payload)
        return response.json(), response.status_code


'''
    def get_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        res = requests.get("Get",url, headers=headers,data=payload)
        self.logs.info(f"method name : get method")
        self.logs.info(f"url : {url}")
        self.logs.info(f"headers: {headers}")
        self.logs.info(f"payload: {payload}")
        self.logs.info(f"response: {res}")
        self.logs.info(f"status_code: {res.status_code}")
        return res.json, res.status_code
'''




