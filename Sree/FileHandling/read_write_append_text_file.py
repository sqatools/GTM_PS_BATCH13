"""
read mode(r):
write mode(w):
append mode(a):
"""
def read_file(file_path):
    # open file in read mode
    abc = open(file_path, "r")  # file_path is a variable   : abc is object: it creates space in memory
    # read file content with read() method
    data = abc.read()
    print(data)
    print("File close before :", abc.closed)
    abc.close()
    print("File close after:", abc.closed)

    # read file from current path
read_file("TextFile.txt")
read_file("C:\Sree\Info\Drims_Info.txt")

def write_file_with_context(filepath, content):
    with open(filepath, "w") as file_obj:
        file_obj.write(content)
write_file_with_context("write_data.txt", "We are Learning File Handling")