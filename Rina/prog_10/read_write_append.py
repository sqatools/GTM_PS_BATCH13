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

def write_file_with_context(filepath, context):
    with open(filepath, 'w') as file_obj:
        file_obj.write(context)

write_file_with_context("read.txt", "We are Learning File Handling")



def write_file_with_context(filepath, content):
    with open(filepath, "w") as file_obj:
        file_obj.write(content)
write_file_with_context("read1.txt", "we are learing read, write and append method")

"""

def append_file_with_content(filepath, content):
    with open(filepath, 'a') as file_obj:
        file_obj.write(content)

append_file_with_content("read1.txt" , "\n Adding appending content.")