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
        self.log.info(f"method name : get method")
        self.log.info(f"url : {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response: {res}")
        self.log.info(f"status_code: {res.status_code}")
        return res.json, res.status_code
'''




