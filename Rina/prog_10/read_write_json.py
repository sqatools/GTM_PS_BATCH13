import json

def read_json_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(type(data))
        # converting string into dictionary
        json_data = json.loads(data)
        print(type(json_data))
        return json_data
read_json_data("users_data.json")


"""
output = read_json_data("users_data.json")
print(output['username'])
print(output['email'])

output['occupation'] = "software engineer"
output['country'] = "India"

print(output)

"""
