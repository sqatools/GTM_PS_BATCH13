import json

class Util:
    def read_json_data(self, file_path):
        with open(file_path, "r") as file:
            data = file.read()
            json_data = json.loads(data)
            return json_data

if __name__ == '__main__':
    print(__name__)
    obj = Util()
    print(obj.__module__)
    data = obj.read_json_data(file_path="users_data.json")
    print(data)
    print(data['email'])