"""
read mode(r):
write mode(w):
append mode(a):
"""

def read_file(file_path):
    file = open(file_path,'r')
    file_contents = file.read()
    print(file_contents)
    file.close()
#Read file from current path
read_file("read_data.txt")

#read with Context manager

def read_file_with_context(file_path):
    with open(file_path,'r') as file_object:
        file_contents = file_object.read()
        print(file_contents)
        print("File close before :",file_object.closed)
    print("File close after :", file_object.closed)

read_file_with_context("read_data.txt")

#Write content file

def write_file_with_context(file_path, content):
    with open(file_path,'w') as file_object:
        file_object.write(content)

write_file_with_context("write_data.txt", "We arelearning file handling")

#Append content file


def write_file_with_context(file_path, content):
    with open(file_path,'a') as file_object:
        file_object.write(content)
#append to existing file : It will append at the end of file
write_file_with_context("append_data.txt", "Appending to append file")
