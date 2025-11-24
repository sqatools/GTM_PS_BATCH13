"""
read mode(r):
write mode(w):
append mode(a):
"""
def readfun(filepath):
    with open(filepath,"r") as file:
        data=file.read()
        print('readfun:',data)
readfun("read_data.txt")
readfun(r"C:\Sree\FileHandling\Read()method\Readfile.txt")
## write function:
def writefun(filepath,content):
    with open(filepath,"w") as file:
        file.write(content)

writefun("write_data.txt","Adding numbersCollecting user inputs")
# write to non-existing file: It will create new file in out or here and add content to file
writefun(r"C:\Sree\FileHandling\writeMethod\write_data_new.txt", "We are Learning File Handling & taking exam on Tuesday")

############### append content file with append mode(a)#########

def appenfun(filepath,content):
    with open(filepath,"a") as file:
        file.write(content)
appenfun("write_data.txt","Append at the end")

##################### Different read methods ###############
def red_no_bytes(filepath,no_bytes):
    with open(filepath,"r") as file:
        date=file.read(no_bytes)
        print(date)

red_no_bytes("read_data.txt",20)
#####    # read one line at time.  readline()  method
def redlinefun(filepath,No_line):
    with open(filepath,"r") as file:
        for _ in range(No_line):
            data=file.readline()
            print(data)
redlinefun("read_data.txt",3)
##3# read specific line.
def redspecfun(filepath, line_no):
    with open(filepath, "r") as file:
        lines = file.readlines()      # list of all lines
        print("specific line",lines[line_no - 0])     # specific line
redspecfun("read_data.txt", 6)