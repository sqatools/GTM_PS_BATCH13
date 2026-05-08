
from ..base.API_base import *
from ..API_Page_object.API_data import *
from ..API_Page_object.API_urls import *


class API_Page_object(APIBASE):

    def get_user_login_details(self):
        self.log.info("initiated Method : get_user_login_details")
        response, status_code = self.get_method(url=API_URLs.get_login_url)
        return response, status_code

    def Add_new_employee(self):
        self.log.info("initiated Method : Add_new_employee")
        headers = {
            "Content-Type": "application/json"
        }

        payload = API_Data.add_employee_payload

        response, status_code = self.post_method(
            url=API_URLs.add_employee_url,
            headers=headers,
            payload=payload
        )

        return response, status_code