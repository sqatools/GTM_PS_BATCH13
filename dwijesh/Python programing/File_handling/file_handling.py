#readmode(r),write mode(w),appened mode(a)

def read_file(file_path):
    abc=open(file_path,"r")
    xyz=abc.read()
    print(xyz)
    abc.close()

#read file from current path
read_file("datafile.txt")
#read file fom other path
#read_file("C:\Users\dwijesh badari\Desktop\Python selenum notes.txt")

print("-"*100)
#context manager
#it will close the file its self no need to close from our end

def read_file_with_context(filepath):
    with open(filepath, "r") as file_obj:
        data= file_obj.read()
        print(data)
        print("File close before :", file_obj.closed)
    # outside of context
    print("File close after:", file_obj.closed)


#read_file_with_context("read_data.txt")

############### write content file with write mode(w)#########

def write_file_with_context(filepath, content):
    with open(filepath, "w") as file_obj:
        file_obj.write(content)

        # write to existing file: It will overwrite existing content
        # write_file_with_context("write_data.txt", "We are Learning File Handling")

        # write to non-existing file: It will create new file and add content to file
        # write_file_with_context("write_data_new.txt", "We are Learning File Handling")

        # E:\Filesdata\Batch13
        # write_file_with_context(r"E:\Filesdata\Batch13\write_data_new.txt", "We are Learning File Handling")

############### append content file with append mode(a)#########


def append(filepath, content):
    with open(filepath,"a") as file:
        file.write(content)

# append to existing file :  it will append at the end existing file content.
#append_file_with_context("append_data.txt", "Appending content to the file")

# append to non-existing file :  it will create new and add content to the file.
append_file_with_context("append_data_new.txt", "Appending content to the file")

######Different read meathods

def read(filepath, bytes):




























