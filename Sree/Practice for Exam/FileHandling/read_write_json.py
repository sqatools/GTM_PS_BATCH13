import json
def Jsreadfun(filepath):
    with open(filepath,"r") as file:
        data=file.read()
        jsondata=json.loads(data)
        return jsondata
output = Jsreadfun("read_data.json")
print(output['username'])
print(output['device_id'])
print("print all jasondata",output)

########### write

def jswritfun(filepath, json_data):
    with open(filepath, "w") as file:
        x = json.dumps(json_data, indent=4)
        file.write(x)

output = {
    "role": "Manager",
    "department": "Sales",
    "employee_id": 1023,
    "status": "Active",
    "username": "john_doe",
    "password": "mypassword123",
    "device_id": "A1B2C3D4",
    "device_type": "Android"

}

jswritfun("users_data.json", output)


