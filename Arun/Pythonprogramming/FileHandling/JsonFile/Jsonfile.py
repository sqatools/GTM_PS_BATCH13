import json

def read_json_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(type(data))
        # convert string data into dictionary with the help of json.loads()
        json_data = json.loads(data)
        print(type(json_data))
        return json_data


output = read_json_data("users_data.json")
print(output['username'])
print(output['email'])

output['occupation'] = "software engineer"
output['country'] = "India"

print(output)

def write_json_file(filepath, json_data):
    with open(filepath, "w") as file:
        # convert dict data to string with the help of json.dumps() method.
        json_values = json.dumps(json_data)
        file.write(json_values)
        file.write(json_data)


write_json_file("users_data.json", output)