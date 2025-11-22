"""
read mode(r):
write mode(w):
append mode(a):
"""

def read_file(file_path):
    file = open(file_path, "r")
    data = file.read()
    print(data)
    print("File close before :", file.closed)
    file.close()
    print("file close after:", file.closed)
# read file from current path
#read_file("read_data.txt")

# read file from other path
#read_file("E:\\Filesdata\\count_name.txt")

#read file from other path
read_file("E:\\flat.txt")

################# Context Manager ######################
# read with context manager :  context manager has it own enter and exit method, so no need to close file explicitly.
def read_file_with_context(filepath):
    with open(filepath, "r") as file_obj:
        data = file_obj.read()
        print(data)
        print("File close before :", file_obj.closed)
    # outside of context
    print("File close after:", file_obj.closed)

#read_file_with_context("read_data.txt")


############### write content file with write mode(w)#########

def write_file_with_context(filepath, content):
    with open(filepath, "w") as file_obj:
        file_obj.write(content)

# write to existing file: It will overwrite existing content
# write_file_with_context("write_data.txt", "We are Learning File Handling")

# write to non-existing file: It will create new file and add content to file
# write_file_with_context("write_data_new.txt", "We are Learning File Handling")

# E:\Filesdata\Batch13
# write_file_with_context(r"E:\Filesdata\Batch13\write_data_new.txt", "We are Learning File Handling")

############### append content file with append mode(a)#########

def append_file_with_context(filepath, content):
    with open(filepath, "a") as file_obj:
        file_obj.write(content)


# append to existing file :  it will append at the end existing file content.
#append_file_with_context("append_data.txt", "Appending content to the file")

# append to non-existing file :  it will create new and add content to the file.
append_file_with_context("append_data_new.txt", "Appending content to the file")
