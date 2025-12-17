import json

class Utils:
    def read_json_data(self, file_path):
        with open(file_path, "r") as file:
            data = file.read()
            json_data = json.loads(data)
        return json_data


if __name__ == "__main__":
    print(__name__)
    obj = Utils()
    print(obj.__module__)
    data = obj.read_json_data(file_path="user_data.json")
    print(data)
    print(data['email'])


