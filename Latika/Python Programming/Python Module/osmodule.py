import os
import shutil

# get current working directory

print(os.getcwd())

# create a directory in current path
#os.mkdir("Folder1")
#os.mkdir(r"D:\filesdata\folder1")

# remove directory

#os.rmdir("Folder1")
#os.rmdir(r"D:\filesdata\folder1")

# create a folder tree

#os.makedirs(r"D:\filesdata\fold1\fold2\fold3")
#os.rmdir(r"D:\filesdata\fold1\fold2\fold3")

#for i in range(1,6):
 #   os.mkdir(fr"D:\filesdata\test{i}")


print(os.getenv("path"))



# returns the path

src_path = r"D:\filesdata"
filename ="abc.txt"

file_path = os.path.join(src_path,filename)
print("File Path:",file_path)


### use of shutil

path1 = r"D:\filesdata\abc.txt"
path2=r"D:\filesdata\fold1\abc.txt"
path3=r"D:\filesdata\fold1\abc_new.txt"

shutil.copy(path1,path2)
shutil.copy(path1,path3)


