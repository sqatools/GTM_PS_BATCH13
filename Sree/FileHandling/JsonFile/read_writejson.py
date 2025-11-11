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
def write_j(filepath, data):
    with open(filepath, "w") as x:
        json.dump(data, x, indent=4)   # indent=4 tells Python to format the JSON with 4 spaces per indentation level so it looks structured and readable.

write_j("users_data.json", output)


