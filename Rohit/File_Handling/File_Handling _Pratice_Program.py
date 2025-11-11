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
#4.Python file program to get the file’s first three and last three lines.
def read_first_last_lines_file(File_path,no_lines):
    with open(File_path, 'r') as file:
        lines = file.readlines()
        for i in (lines[:3]):
            print(i)

        for i in (lines[-3:]):
            print(i)

read_first_last_lines_file("Rohit.txt",3)

print("-"*50)
'''
1.Following the comprehensive win,

2.India have now put themselves in a

3.position where they cannot lose the series

5.informed Bombay Stock Exchange of its intention

6.to undertake what it calls a 'strategic review'

7.of its investment in the non-core business

'''
##########################################################################
#.5