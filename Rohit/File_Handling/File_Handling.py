"""
read mode(r):
write mode(w):
append mode(a):
"""
def read_file(File_path):
    file = open(File_path,'r')
    date = file.read()
    print(date)
    print("file close before :",file.closed)
    file.close()
    print("file close after :",file.closed)

# read file from current path
read_file('Rohit.txt')

# read file from other path
read_file("D:\\Read folder\\Read_File.txt")

print("-"*50)
################# Context Manager ######################
# read with context manager :  context manager has it own enter and exit
# method, so no need to close file explicitly.
## (Purpose of this method mostly use for big files i.e.1 GB)

def read_file_with_context(filepath):
    with open(filepath, 'r') as file_obj:
        date = file_obj.read()
        print(date)
        print("file close before :",file_obj.closed)
    print("file close after :", file_obj.closed)

read_file_with_context("Rohit.txt")

print("-"*50)
############### write content file with write mode(w)#########
def write_file_with_context(filepath, content):
    with open(filepath, "w") as file_obj:
        file_obj.write(content)

# write to existing file: It will overwrite existing content
write_file_with_context("Write_file.txt", "Hello World")

# write to non-existing file: It will create new file and add content to file
#write_file_with_context("New_File_Write.txt", "Created new file if not")

#created new file in given folder
#write_file_with_context(r"D:\Read folder\Rohit_WriteFile.txt", "Hello Learning Python")

############### append content file with append mode(a)#########
def append_file_with_context(filepath, content):
    with open(filepath, 'a') as file_obj:
        file_obj.write(content)

# write to existing file: It will overwrite existing content
#append_file_with_context("append_file.txt", "Append the content")

# write to non-existing file: It will create new file and add content to file
append_file_with_context("New_Append_file.txt","create new file content")

#created new file in given folder
append_file_with_context(r"D:\Read folder\New_Append_file.txt","Pratice purpose")