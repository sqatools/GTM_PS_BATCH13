def read_file(file_path):
    # open the file in read mode
    abc = open(file_path, "r")
    # read file content with read method
    data = abc.read()
    print(data)
    print("File close before :", abc.closed)
    abc.close()
    print("File close after :", abc.closed)

#read file from current path
read_file("sampledata.txt")

