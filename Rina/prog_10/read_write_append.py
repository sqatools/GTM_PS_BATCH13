def read_file(file_path):
    readfile = open(file_path)
    data = readfile.read()
    print(data)
    print("File closed before: ", readfile.closed)
    readfile.close()
    print("File closed after: ", readfile.closed)

read_file("read.txt")
