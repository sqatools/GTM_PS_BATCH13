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