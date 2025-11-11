import json

def read_json_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(type(data))
        # convert string data into dictionary with the help of json.loads()
        json_data = json.loads(data)
        print(type(json_data))
        return json_data
output = read_json_data("user_data.json")

print(output['username'])
print(output['email'])

output['occupation'] = "software engineer"
output['country'] = "India"

print(output)

