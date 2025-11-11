import json

def read_write_json_file(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        print(type(data))
    # convert string data into dictionary with the help of json.loads()
        json_data = json.loads(data)
        print(type(json_data))
        return json_data

result = read_write_json_file("user_read.json")
print(result['name'])
print(result['Ph.no'])

#print("*"*50)

result['address'] = "160 Havenbrook"
result['country'] = "USA"
print(result)

def write_json_file(filepath, json_data):
    with open(filepath, "w") as filename:
        json_values = json.dumps(json_data)
        filename.write(json_values)
        filename.write(json_values)

write_json_file("user_read.json", result)
