
from ..base.API_base import *
from ..API_Page_object.API_data import *

class API_Page_object(APIBASE):

    def get_user_login_details(self):
        self.log.info("initiated Method : get_user_login_details")
        response, status_code = self.get_method(url=url)
        return response, status_code
