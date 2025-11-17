import json

def read_json(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(data)
        json_data = json.loads(data)
        print(type(json_data))
        print(json_data)

output = read_json("userdata.json")
print(output)






