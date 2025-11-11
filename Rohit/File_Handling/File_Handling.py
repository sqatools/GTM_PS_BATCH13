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
#append_file_with_context("New_Append_file.txt","create new file content")

#created new file in given folder
#append_file_with_context(r"D:\Read folder\New_Append_file.txt","Pratice purpose")

print("-"*50)
#########################Different read methods#####################################################
# 1. read number of bytes.
# 2. read a single line
# 3. read list of lines.

#1. read number of bytes:

def read_file_no_bytes(filepath,no_bytes):
    with open(filepath, "r") as file:
        data = file.read(no_bytes)
        print(data)

#read_file_no_bytes("Rohit.txt",20) # 1.Following the comp

#read_file_no_bytes("Rohit.txt",100)
'''
1.Following the comprehensive win,
2.India have now put themselves in a
3.position where they cannot
'''

print("-"*50)

# 2. read a single line
def read_file_no_lines(filepath, no_lines):
    with open(filepath, "r") as file:
        for _ in range(no_lines):
            data = file.readline()
            print(data)


read_file_no_lines("Rohit.txt", 4)
'''
1.Following the comprehensive win,

2.India have now put themselves in a

3.position where they cannot lose the series

4.Diageo, the owner of the RCB IPL, WPL teams,
'''

# 3. read list of lines.
def read_file_specific_line(filepath,line_no):
    with open(filepath, 'r') as file:
        specific_line = file.readlines()
        #print(specific_line)
        print(specific_line[line_no-1])

read_file_specific_line("Rohit.txt",3)
#3.position where they cannot lose the series