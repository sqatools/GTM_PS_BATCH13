import json

class Utils:
    def read_json_data(self, file_path):
        with open(file_path,'r') as file:
            data = file.read()
            json_data = json.loads(data)
            return json_data




