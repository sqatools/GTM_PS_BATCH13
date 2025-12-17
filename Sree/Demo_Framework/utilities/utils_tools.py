import json



class Util:
    def read_json_data(self, filepath):
        with open(filepath, "r") as file:
            data = file.read()
            json_data = json.loads(data)
        return json_data