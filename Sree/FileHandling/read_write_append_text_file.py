"""
read mode(r):
write mode(w):
append mode(a):
"""
def read_file(file_path):
    # open file in read mode
    Textfile = open(file_path, "r")  # file_path is a variable   : abc is object: it creates space in memory
    # read file content with read() method
    data = Textfile.read()
    print(data)
    print("File close before :", Textfile.closed)
    Textfile.close()
    print("File close after:", Textfile.closed)

    # read file from current path
read_file("TextFile.txt")
read_file("C:\Sree\Info\Drims_Info.txt")

def write_file_with_context(filepath, content):
    with open(filepath, "w") as file_obj:
        file_obj.write(content)
write_file_with_context("write_data.txt", "We are Learning File Handling")
print('-'*44)
#read method:
def read_file(filepath):
    x=open(filepath,"r")
    y=x.read()
    print(y)
    x.close()
read_file("TextFile.txt")
print('_'*45)
##read_file("C:\Sree\FileHandling\Read()method\Readfile.txt")
print('-'*45)
print("csv file:")
read_file("C:\Sree\FileHandling\FullCsv.csv")
print('-'*45)
def read_fun(filepath):
    file_space =open(filepath,"r")
    file =file_space.read()
    print("csvfile:",file)
    print("File close before :", file_space.closed)
    file_space.close()
    print("File close after:", file_space.closed)
read_fun("C:\Sree\FileHandling\FullCsv.csv")
print('-'*45)
def red_fun(filepath):
    with open(filepath,"r") as x:
        print("with open_read fun:",x.read())
      #  y=x.read()
       # print(y)
        print("File close before :", x.closed)

    print("File close after:", x.closed)  # To close the space in memory, should be outside of "with block"
red_fun("C:\Sree\FileHandling\FullCsv.csv")
print('-'*45)
def write_fun(filepath,content):
    with open(filepath,"w") as fil_obj:
        fil_obj.write(content)

write_fun("write_data.txt","My first write content")
write_fun("write_new_data.txt","My first write content")
write_fun("C:\Sree\FileHandling\writeMethod\write_data.txt","My first write content")
write_fun("C:\Sree\FileHandling\writeMethod\write_data.csv","My first CSV firl write content")
print('appendfunction','-'*44)
def appe_fun(filepath,content):
    with open(filepath,"a") as x:
        x.write(content)
appe_fun("write_data.txt","add append content")
appe_fun("append_data_new.txt","newly added append content")
print('-'*45)
def readlins(filepath):
    with open(filepath,"r") as y:
       x=y.readlines()
       print(x)
## Print first three lines
    for i in x[:3]:
      print("first 3 line:",i)
    for i in x[-3:]:
        print('last 3 lines:',i)
readlins("read_data.txt")
