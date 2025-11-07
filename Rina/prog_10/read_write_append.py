"""

def read_file(file_path):
    readfile = open(file_path)
    data = readfile.read()
    print(data)
    print("File closed before: ", readfile.closed)
    readfile.close()
    print("File closed after: ", readfile.closed)

read_file("read.txt")

def read_file_with_context(filepath):
    with open(filepath, 'r') as file_obj:
        data = file_obj.read()
        print(data)
        print("File close before :", file_obj.closed)
        print("File close after :", file_obj.closed)
read_file_with_context("read.txt")

"""


