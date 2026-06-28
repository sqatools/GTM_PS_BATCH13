"""
API Tool

Responsible for:
1. GET
2. POST
3. PUT
4. DELETE
"""

import requests


class APITool:

    def get_request(self, url):

        response = requests.get(url)

        return {

            "status_code": response.status_code,

            "body": response.json()

        }

    def post_request(

        self,

        url,

        payload

    ):

        response = requests.post(

            url,

            json=payload

        )

        return {

            "status_code": response.status_code,

            "body": response.json()

        }

    def put_request(

        self,

        url,

        payload

    ):

        response = requests.put(

            url,

            json=payload

        )

        return response.status_code

    def delete_request(

        self,

        url

    ):

        response = requests.delete(url)

        return response.status_code