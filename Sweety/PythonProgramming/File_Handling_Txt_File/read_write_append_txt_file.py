"""
read mode(r):
write mode(w):
append mode(a):
"""
def read_file(file_path):
    # open file in read mode
    abc = open(file_path, "r")
    # read file content with read() method
    data = abc.read()
    print(data)
    print("file before closed: ", abc.closed)
    abc.close()
    print("file before closed: ", abc.closed)

    #read file from current path
read_file("read_data.txt")

print("_"*50)

    # read file from other path
read_file("C:\\Python_Selenium Docs\\read_file.txt")

print("_"*50)
################# Context Manager ######################
# read with context manager :  context manager has it own enter and exit method,
# so no need to close file explicitly.

def read_file_with_context(filepath):
    with open(filepath, "r") as file_obj:
        data = file_obj.read()
        print(data)
        print("File before closed", file_obj.closed)
    # outside of context
    print("File close after:", file_obj.closed)
read_file_with_context("readfile_with_context.txt")

print("_"*50)

