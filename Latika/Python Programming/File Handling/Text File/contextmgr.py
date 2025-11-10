# Read with context manager : context manager has it own enter and exist method so no need to close file explicitly

def read_file_with_context(filepath):
    with open(filepath,"r") as file_obj:
        data=file_obj.read()
        print(data)

read_file_with_context("sample.txt")

# Write content file with writemode (w)

def write_file_with_context(file_path,content):
    with open(file_path,"w") as file_obj:
        file_obj.write(content)

write_file_with_context("sample.txt","Learning python and used write function for that")


# Write a non-existing file : it will create new file and add content to file.

write_file_with_context("write.txt","We are learning with new file")

# Append content file with append mode (a)

def append_file_with_context(filePath,content):
    with open(filePath,"a") as file_obj1:
        file_obj1.write(content)
append_file_with_context("append.txt", "Appedning content to the file")



