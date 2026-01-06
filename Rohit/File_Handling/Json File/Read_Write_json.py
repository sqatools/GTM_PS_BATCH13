import json

def read_json_file(file_path):
    with open(file_path,'r') as file:
        data = file.read()
        print(type(data))
        # convert string data into dictionary with the help of json.loads()
        json_data = json.loads(data)
        print(type(json_data))
        return json_data

#read_json_file("Json1_File.json")

output = read_json_file("Json1_File.json")
print(output['User_name']) # Rohit77
print(output['Email']) # rohit67@gmail.com

# If we want to add new content in Json_file
output['Profile'] = "QA Lead"
output['City'] = "Karad"

print(output)

def write_json_file(file_path,json_data):
    with open(file_path,'w') as file:
        # convert dict data to string with the help of json.dumps() method.
        json_values = json.dumps(json_data)
        file.write(json_values)
        file.write(str(json_data))

write_json_file("Json1_File.json",output)

