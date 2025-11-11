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
############### write content file with write mode(w)#########
def write_file_with_context(filepath, content):
    with open(filepath, "w") as file_obj:
         file_obj.write(content)


# write to non-existing file: It will create new file and add content to file
write_file_with_context("write_data.txt", "I am writing to the new file")

# write to existing file: It will overwrite existing content
write_file_with_context("write_data.txt", "I am overwriting existing data")

############### append content file with append mode(a)#########

def append_file_with_context(filepath, content):
    with open(filepath, "a") as file_obj:
        file_obj.write(content)
# append to existing file :  it will append at the end existing file content.
append_file_with_context("append_data.txt", "Appending content to the file")

# append to non-existing file :  it will create new and add content to the file.
append_file_with_context("append_data_new.txt", "Appending content to the file")


##################### Different read methods ###############
# 1. read number of bytes.
# 2. read a single line
# 3. read list of lines.

def read_file_no_bytes(filepath, number_of_bytes):
    with open(filepath, "r") as file:
        data = file.read(number_of_bytes)
        print(data)


read_file_no_bytes("read_data.txt", 15) #Python is a hig
print("_"*50)
read_file_no_bytes("read_data.txt", 100)
#Python is a high-level, general-purpose programming language.
#Its design philosophy emphasizes code


print("_"*50)
# read one line at time.

def read_file_no_lines(filepath, no_of_lines):
    with open(filepath, "r") as file:
        for _ in range(no_of_lines):
            data = file.readline()
        print(data)


read_file_no_lines("read_data.txt", 3)


print("_"*50)
# read specific line.

def read_file_specific_line(filepath, line_no):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        print(lines_list)
        print(lines_list[line_no - 1])



read_file_specific_line("read_data.txt", 2)


