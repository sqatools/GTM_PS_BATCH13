#1.Python Program How to read a file in reading mode
def read_file(Filepath):
    file = open(Filepath, 'r')
    data = file.read()
    print(data)

    print("Closed file before :",file.closed)
    file.close()
    print("Closed file after :", file.closed)

read_file("Rohit.txt")

print("-"*50)
#################################################################
#2.Python file program to overwrite the existing file content

def write_file(filepath,content):
    with open(filepath, "w") as file_obj:
      file_obj.write(content)

#write_file("Rohit.txt", "overwrite the File content")

print("-"*50)
#################################################################
#3.Python file program to append data to an existing file

#def append_file(filepath,content):
 #   with open(filepath, "a") as file_obj:
  #      file_obj.write(content)

#append_file("append_file.txt", "Line7 : This is Karad city")

print("-"*50)
#################################################################
