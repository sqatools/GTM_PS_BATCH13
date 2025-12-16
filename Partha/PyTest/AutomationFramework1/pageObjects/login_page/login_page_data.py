import os
from ...Utilities.util_tools import Util

json_file_path = os.path.join(os.getcwd(), "pageObjects/login_page/login_data.json")
jsn_data = Util().read_json_data(json_file_path)