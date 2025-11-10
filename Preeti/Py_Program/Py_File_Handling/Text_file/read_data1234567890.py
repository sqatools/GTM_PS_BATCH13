"""File handling : Common modes include:
"r" (read): Opens for reading. Raises FileNotFoundError if the file doesn't exist.
"w" (write): Opens for writing. Creates a new file if it doesn't exist, or truncates (empties) an existing file.
"a" (append): Opens for appending. Creates a new file if it doesn't exist, or adds content to the end of an existing file.
"x" (create): Creates a new file. Raises FileExistsError if the file already exists.
"b" (binary): Used with other modes (e.g., "rb", "wb") for handling binary files like images.
Reading Files:
file.read(): Reads the entire content of the file as a single string.
file.readline(): Reads a single line from the file.
file.readlines(): Reads all lines into a list of strings.
Writing Files:
file.write(string): Writes a string to the file.
file.writelines(list_of_strings): Writes a list of strings to the file.
Closing Files: It is crucial to close files after you are done with them
to release system resources. file.close()
with Statement (Recommended): The with statement provides a more robust and
Pythonic way to handle files,
ensuring they are automatically closed even if errors occur.
with open("filename.txt", "r") as file:
        content = file.read()
    # File is automatically closed here
"""
"""
read mode(r):
write mode(w):
append mode(a):
"""

def read_file(file_path):
    # open file in read mode
    openingfile=open(file_path,"r")
    # read file content with read() method
    data=openingfile.read()
    print(data)
    print("File opened successfully")
    openingfile.close()
    print("File closed")


# read file from current path
#read_file("read_data.txt")
# read file from other path
################# Context Manager ######################
# read with context manager :  context manager has it own enter and exit method,so no need to close file explicitly.

def read_file_with_context(filepath):
    with open(filepath,"r") as file_obj:
        data=file_obj.read()
        print(data)
        print("File close before :", file_obj.closed)
    # outside of context
    print("File close after :", file_obj.closed)

read_file_with_context("read_data.txt")


############### write content file with write mode(w)#########

def write_file_with_context(filepath, content):
    with open(filepath, "w") as file_obj:
        file_obj.write(content)

# write to existing file: It will overwrite existing content
# write_file_with_context("write_data.txt", "We are Learning File Handling")

# write to non-existing file: It will create new file and add content to file
# write_file_with_context("write_data_new.txt", "We are Learning File Handling"


############### append content file with append mode(a)#########

def append_file_with_context(filepath, content):
    with open(filepath, "a") as file_obj:
        file_obj.write(content)


# append to existing file :  it will append at the end existing file content.
#append_file_with_context("append_data.txt", "Appending content to the file")

# append to non-existing file :  it will create new and add content to the file.
append_file_with_context("append_data_new.txt", "Appending content to the file")