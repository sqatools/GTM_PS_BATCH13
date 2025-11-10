def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(data)


#read_file("read_data.txt")
read_file("home_file.txt")