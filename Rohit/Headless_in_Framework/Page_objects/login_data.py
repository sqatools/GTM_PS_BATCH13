import os
from ..Utilities.utils_tools import Utils

json_file_path = os.path.join(os.getcwd(),"Page_objects/login_data.json")
jsn_data = Utils().read_json_data(json_file_path)

