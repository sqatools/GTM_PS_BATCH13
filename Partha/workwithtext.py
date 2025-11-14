def read_file(filename):
    open_file = open(filename, 'r')
    read_file = open_file.read()
    open_file.close()
    print(read_file)
    print(open_file.closed)

read_file("users_details.txt")
read_file("D:\\123.txt")

print("*"*50)

def read_file_with_cxt(filename):
    with open(filename, 'r') as f:
        data = f.read()
        print(data)
    print(f.closed)
read_file_with_cxt("D:\\123.txt")

print("*"*50)

def write_file_with_cxt(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
write_file_with_cxt("D:\\123.txt", "Hello World1")
read_file_with_cxt("D:\\123.txt")

print("*"*50)

def write_file(filename, data):
    open_file = open(filename, 'w')
    open_file.write(data)

write_file("D:\\123.txt", "Hello World5")
read_file_with_cxt("D:\\123.txt")