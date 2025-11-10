import json

def read_jsonfile(filepath):
    with open(filepath,"r") as x:
        y=x.read()
        print(type(y))
        z= json.loads(y)
        return z
output=read_jsonfile("users_data.json")
print(output)
print(output['user_id'])
print(output['lastName'])
output['occupation'] = "software engineer"
output['country'] = "India"
print(output)
print('-'*50)
def write_j(filepath,data):
    with open(filepath,"w") as x:
        # convert dict data to string with the help of json.dumps() method.
        json_values = json.dumps(data)
        x.write(json_values)

write_j("users_data.json",output)