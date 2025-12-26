import requests
import logging

class APIBase:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.log.info(f"method name: get method")
        self.log.info(f"url: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def post_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        if isinstance(payload, dict):
            headers.update({'Content-Type': 'application/json'})
            response = requests.request("POST", url, headers=headers, json=payload)
        else:
            response = requests.request("POST", url, headers=headers, data=payload)
        self.log.info(f"method name: post method")
        self.log.info(f"url: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        try:
            self.log.info(f"response: {response.json()}")
        except:
            self.log.info(f"response: {response.text}")
        self.log.info(f"status code: {response.status_code}")
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code

    def put_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        if isinstance(payload, dict):
            headers.update({'Content-Type': 'application/json'})
            response = requests.request("PUT", url, headers=headers, json=payload)
        else:
            response = requests.request("PUT", url, headers=headers, data=payload)
        self.log.info(f"method name: put method")
        self.log.info(f"url: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        try:
            self.log.info(f"response: {response.json()}")
        except:
            self.log.info(f"response: {response.text}")
        self.log.info(f"status code: {response.status_code}")
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code

    def patch_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        if isinstance(payload, dict):
            headers.update({'Content-Type': 'application/json'})
            response = requests.request("PATCH", url, headers=headers, json=payload)
        else:
            response = requests.request("PATCH", url, headers=headers, data=payload)
        self.log.info(f"method name: patch method")
        self.log.info(f"url: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        try:
            self.log.info(f"response: {response.json()}")
        except:
            self.log.info(f"response: {response.text}")
        self.log.info(f"status code: {response.status_code}")
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code

    def delete_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        self.log.info(f"method name: delete method")
        self.log.info(f"url: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        try:
            self.log.info(f"response: {response.json()}")
        except:
            self.log.info(f"response: {response.text}")
        self.log.info(f"status code: {response.status_code}")
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code

