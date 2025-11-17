def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(data)


#read_file("read_data.txt")
read_file("home_file.txt")


# read file with Number of bytes
def read_file_number_bytes(file_path):
    with open(file_path, "r") as file:
        data = file.readline(read_file_number_bytes)
        print(data)
read_file_number_bytes('home_file.txt', 1)


