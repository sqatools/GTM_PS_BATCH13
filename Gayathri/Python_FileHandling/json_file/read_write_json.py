#we have to import this in built module/library to work on json files
#json - java script object notation, always have to have unique keys no duplicates
#also the key and values have to be defined in "" and not singel quotes
import json

def read_json_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(type(data)) #<class 'str'> when it reads from the json file - it reads as a string
        # convert string data into dictionary with the help of json.loads()
        json_data = json.loads(data) #here we are trying to convert the string to dictionary
        print(type(json_data)) #<class 'dict'>
        return json_data

output = read_json_data("user_data.json") #output we are storing in variable, so we can retrive any value
# we want name
print(output['username']) #Mohit
print(output['email']) #mohit.gupta@gmail.com

##########################################################################################################
#update new content - add new entries into the file
output['occupation'] = "software engineer1"
output['country'] = "India"
print(output)

def write_json_file(filepath, json_data):
    with open(filepath, "w") as file: #why not append - as it might change teh structure as it might go to new line
        #so we are overwriting the value in existing file - so w mode

        # convert dict data to string with the help of json.dumps() method.
        json_values = json.dumps(json_data)
        file.write(json_values)
        #file.write(json_data) - without converting if we write to file - then its in dict and it throws error it must be str


write_json_file("user_data.json", output)