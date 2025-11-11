###################### Different read methods ###############
# 1. read number of bytes.
# 2. read a single line
# 3. read list of lines.

#1. read number of bytes. - it means no of chars
def read_file_no_bytes(filepath, no_bytes):
    with open(filepath, "r") as file:
        data = file.read(no_bytes)
        print(data)


#read_file_no_bytes("read_data.txt", 20) ## 1.Following the comp - 20 chars read.

#read_file_no_bytes("read_data.txt", 100)
"""
1.Following the comprehensive win,
2.India have now put themselves in a
3.position where they cannot
"""

#2.# read one line at time.
def read_file_no_lines(filepath, no_lines):
    with open(filepath, "r") as file:
        for _ in range(no_lines): #here we are not giving any variable as no variable is passed inside the loop
            #if at all any variable is passed in loop we can use it,else we can give _
            data = file.readline()
            print(data)

#read_file_no_lines("read_data.txt", 3) # if we want 3 lines
"""
1.Following the comprehensive win,

2.India have now put themselves in a

3.position where they cannot lose the series

"""

#3.# read specific line.
def read_file_specific_line(filepath, line_no):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        print(lines_list)
        print(lines_list[line_no-1]) #here to match the line numbers from the data file

read_file_specific_line("read_data.txt", 1) #give me the 1st line
#1.Following the comprehensive win,

#now i want the 5th line
read_file_specific_line("read_data.txt", 5)
#5.informed Bombay Stock Exchange of its intention

#print(lines_list) - here it has added a new line at end of each line - thats teh reason we see a new line and thats how it goes to next line
#['1.Following the comprehensive win,\n', '2.India have now put themselves in a\n', '3.position where they cannot lose the series\n', '4.Diageo, the owner of the RCB IPL, WPL teams,\n', '5.informed Bombay Stock Exchange of its intention\n', "6.to undertake what it calls a 'strategic review'\n", '7.of its investment in the non-core business\n']