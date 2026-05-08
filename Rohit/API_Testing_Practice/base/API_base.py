import requests
import logging

class APIBASE:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self,url,headers=None,payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("Get",url,headers=headers,data=payload)
        self.log.info(f"Method Name: get method")
        self.log.info(f"url: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"responses : {response}")
        self.log.info(f"status_code : {response.status_code}")
        return response.text, response.status_code

