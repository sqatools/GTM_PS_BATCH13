from ...base.api_base import API_Base
from ...API_Objects.read_data.data_file import *

class API_class(API_Base):

    def get_All_Products_List(self):
        response, status_code = self.get_method(url=Url)
        return response, status_code
