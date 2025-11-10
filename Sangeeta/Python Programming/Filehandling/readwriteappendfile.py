def read_file_with_context(filepath):
    with open(filepath, 'r') as fileobj:
        data = fileobj.read()
        print(data)
        print("File close before :", fileobj.closed)
    print("File close after :", fileobj.closed)

read_file_with_context("sampledata.txt")


def write_file_with_context(filepath, content):
    with open(filepath, 'w') as newfile_obj:
        newfile_obj.write(content)

write_file_with_context("sampledata_new.txt", "Trying the write method in file handling")

def append_file_with_context(filepath, content):
    with open(filepath, 'a') as app_obj:
        app_obj.write(content)

append_file_with_context("sampledata_new.txt", "\n Reading from a file in Python means accessing and retrieving contents of a file,\n whether it be text, binary data or formats like CSV and JSON. ...")
