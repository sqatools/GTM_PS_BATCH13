"""
read mode (r)
write mode (w)
append mode (a)
"""
def read_file(filepath):
    file = open(filepath, "r")
    data =file.read()
    print(data)
    print("file closed before:", file.close())
    file.close()
    print("file closed after:", file.close())

read_file("sample.txt")
read_file("C:\\File Handlings Data\\testfile.txt")