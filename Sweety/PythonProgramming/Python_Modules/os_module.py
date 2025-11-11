import os

# get current working directory.
print(os.getcwd())
#C:\PythonAutomation\GTM_PS_BATCH13\Sweety\PythonProgramming\Python_Modules

# create a directory in the current path
#os.mkdir("folder1")
#os.mkdir("folder2")
#os.mkdir(r"C:\Python_Selenium Docs\test_os")

#for i in range(1, 6):
#    os.mkdir(fr"C:\Python_Selenium Docs\test_os{i}")
#    os.rmdir(fr"C:\Python_Selenium Docs\test_os{i}")

# remove directory.
#os.rmdir("folder1")
#os.rmdir(r"C:\Python_Selenium Docs\test_os")

# create a folder tree.
#os.makedirs(r"C:\Python_Selenium Docs\fold1\fol2\fol3\fol4\fol5")

# remove folder tree
#os.removedirs(r"C:\Python_Selenium Docs\fold1\fol2\fol3\fol4\fol5")

###### get environment variable value####
print(os.getenv("path"))
#C:\Python3\Scripts\;C:\Python3\;C:\Program Files\Common Files\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\Java\jdk-23\bin;C:\Program Files\Git\cmd;C:\Users\Swity\AppData\Local\Microsoft\WindowsApps;;C:\Program Files\JetBrains\PyCharm 2022.2.2\bin;;C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.2\bin;

print(os.getenv("OneDrive")) #C:\Users\Swity\OneDrive

################## join path #################
src_path = r"C:\Python_Selenium Docs"
file_name = "github_guide (1)"

file_path = os.path.join(src_path, file_name)
print("file_path: ", file_path) #C:\Python_Selenium Docs\github_guide (1)

####### check given file/folder is available path ######
print("Is file available: ", os.path.isfile(file_path))
print("Is folder available: ", os.path.isdir(src_path))
fol1_path = r"E:\Filesdata\Batch14"
print("given path is available :", os.path.exists(fol1_path))

#################################
import shutil
#
#os.mkdir(r"C:\Python_Selenium Docs\count_name.txt")
#os.makedirs(r"C:\Python_Selenium Docs\test_os1\count_name1.txt")
#os.mkdir(r"C:\Python_Selenium Docs\test_os1\count_name_new.txt")

path1 = r"C:\Python_Selenium Docs\count_name.txt"
path2 = r"C:\Python_Selenium Docs\count_name1.txt"
path3 = r"C:\Python_Selenium Docs\test_os1\count_name_new.txt"

#shutil.copy(path1, path2)
#shutil.copy(path1, path3)

"""
print("_"*40)
############# Get list of all files and folder from path ############

src_path = r"C:\Python_Selenium Docs"
files_list = os.listdir(src_path)
print(files_list)
file_count = 0
fold_count = 0

for data in files_list:
    data_path = os.path.join(src_path, data)
    if os.path.isfile(data_path):
        file_count += 1
    elif os.path.isdir(data_path):
        fold_count += 1

print("File count :", file_count)  
print("Folder count :", fold_count)


"""