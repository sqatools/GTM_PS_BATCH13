"""def read_file(file_path):
    # open file in read mode
    abc=open(file_path,"r")
    # read file content with read() method
    data=abc.read()
    print(data)
    print('File opened successfully:',abc.closed)
    abc.close()
    print('File closed:',abc.closed)



def read_file_with_context(filepath):
    with open(filepath,"r") as file_obj:
        data=file_obj.read()
        print(data)
        print("File close before :", file_obj.closed)
    # outside of context
    print("File close after :", file_obj.closed)

    read_file_with_context("read_data.txt")
    """""

