import os

print(os.getcwd())
os.mkdir("folder1")

# create a folder tree.
#os.makedirs(r"C:\Sree\G-mail\fold1\fold2\fold3\fold4\fold5")
###### get environment variable value####
#print(os.getenv("path"))
print(os.getenv("Browser"))
print(os.getenv("OneDrive"))
####### join path ######
src_path = r"C:\Sree\FileHandling"  # it combines file path and folder path -gives full name
filename = "Sree"
file_path = os.path.join(src_path, filename)
print("filepath :", file_path)   # out put filepath : C:\Sree\FileHandling\Sree
####### check given file/folder is available path ######


import shutil
path1 = r"C:\Sree\FileHandling\Sree"
path2 = r"C:\Sree\FileHandling\Read()method\Sree"
path3 = r"C:\Sree\FileHandling\Read()method\Sree_new.txt"

shutil.copy(path1, path2)
#shutil.copy(path1, path3)
