
#7th Nov - Class
"""
read mode(r):
write mode(w):
append mode(a):
"""

def read_file(file_path):
    # open file in read mode
    abc = open(file_path, "r")
    # read file content with read() method
    #the objevt that open is returning is from class IO
    #through IO it used all differnt methods for fiel handling
    data = abc.read() #here read method is from class IO which is ued for file handling
    print(data)
    print("File close before :", abc.closed) #flag to check if the file is open or closed
    #if file is closed -it wil return true, else retrun false
    #why we need to clse teh file - it consumes unnecesary memory
    abc.close() #this explicitly close the file
    print("File close after:", abc.closed)

# read file from current path
#read_file("read_data.txt")

print("*"*50)

# read file from other path
#read_file("C:\\Users\\Sriram\\Test Automation\\Selenium Python\\TestData\\")
read_file(r"C:\Users\Sriram\PycharmProjects\TestData\testdata.txt.txt")

################# Context Manager ######################
# read with context manager :  context manager has it own enter and exit method,
# so no need to close file explicitly. hedre we need to provid ethe keyword - with

def read_file_with_context(filepath):
    with open(filepath, "r") as file_obj:
        data= file_obj.read()
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
#write_file_with_context("write_data.txt", "We are Learning File Handling")

# write to non-existing file: It will create new file and add content to file
#write_file_with_context("write_data_new.txt", "We are Learning File Handling")

#write to specific location
#write_file_with_context(r"C:\Users\Sriram\PycharmProjects\TestData\write_data_new.txt", "We are Learning File Handling")
#r - used here to avoid the use of double slash
#r - means convert the string in the raw format. if name has special chaacters then to avoid that use r

############### append content file with append mode(a)#########
#update file having existing content with appending new cotent at end

def append_file_with_context(filepath, content):
    with open(filepath, "a") as file_obj:
        file_obj.write(content)


# append to existing file :  it will append at the end existing file content.
#heer no overwrite happens
#append_file_with_context("append.txt",  "\n "+ "Appending content to the file")

# append to non-existing file :  it will create new and add content to the file.
append_file_with_context("append_data_new.txt", "\n"+ "Appending content to the file")

#write - will overwrite if theer is any content in teh file
#append - will add data at end of the content in existing file - no overwrite