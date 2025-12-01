import os

# get current working directory.
print(os.getcwd())
# E:\Trainings\GTM_PS_Batch13_26Sept25\GTM_PS_BATCH13\Deepesh\PythonProgramming\Python_Modules

# create a directory in the current path
# os.mkdir("folder1")
#os.mkdir(r"E:\Filesdata\Batch13\test_os")

# for i in range(1, 6):
#    os.mkdir(fr"E:\Filesdata\Batch13\Test_os{i}")


# remove directory.
# os.rmdir("folder1")
# os.rmdir(r"E:\Filesdata\Batch13\test_os")


# create a folder tree.
# os.makedirs(r"E:\Filesdata\Batch13\fold1\fold2\fold3\fold4\fold5")

# remove folder tree
# os.removedirs(r"E:\Filesdata\Batch13\fold1\fold2\fold3\fold4\fold5")

###### get environment variable value####

#print(os.getenv("path"))
# C:\Python3\Scripts\;C:\Python3\;C:\Users\Deepesh Yadav\AppData\Local\Programs\Python\Python38\Scripts\;C:\Users\Deepesh Yadav\AppData\Local\Programs\Python\Python38\;C:\Program Files\Python38\Scripts\;C:\Program Files\Python38\;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;E:\driver;C:\sqalite3\;C:\Program Files (x86)\dotnet\;E:\Trainings\PythonRobotTavet14Feb2023\RobotframeworkProject\chromedriver_win32\chromedriver.exe;c:\users\deepesh yadav\appdata\roaming\python\python312\;c:\users\deepesh yadav\appdata\roaming\python\python312\Scripts\;C:\Python312\;C:\Python312\Scripts\;C:\Program Files\PuTTY\;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Program Files (x86)\Yarn\bin\;C:\Program Files\Java\jdk-11.0.17\bin;C:\apache-maven-3.9.11-bin\apache-maven-3.9.11\bin;C:\Program Files\Git\cmd;C:\allure-2.35.1\bin;C:\Users\Deepesh Yadav\AppData\Local\Microsoft\WindowsApps;C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.2\bin;;E:\chromedriver_win32;C:\Program Files\Docker Toolbox;C:\Users\Deepesh Yadav\AppData\Local\GitHubDesktop\bin;C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2022.3.2\bin;;C:\Users\Deepesh Yadav\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\Deepesh Yadav\AppData\Roaming\npm;C:\Users\Deepesh Yadav\AppData\Local\Yarn\bin;C:\Users\Deepesh Yadav\AppData\Local\Programs\cursor\resources\app\bin

#print(os.getenv("Browser2")) # Mozilla
#print(os.getenv("OneDrive"))  # C:\Users\Deepesh Yadav\OneDrive



####### join path ######
src_path = r"E:\Filesdata\Batch13"
filename = "count_name.txt"

file_path = os.path.join(src_path, filename)
print("filepath :", file_path)  # E:\Filesdata\Batch13\count_name.txt

####### check given file/folder is available path ######
print("given path is file:", os.path.isfile(file_path))  # given path is file: True
print("given path is folder :", os.path.isdir(src_path)) # given path is folder : True
fol1_path = r"E:\Filesdata\Batch14"
print("given path is available :", os.path.exists(fol1_path))  # given path is available : False


#################################
import shutil
#
path1 = r"E:\Filesdata\Batch13\count_name.txt"
path2 = r"E:\Filesdata\Batch13\test_os1\count_name.txt"
path3 = r"E:\Filesdata\Batch13\test_os1\count_name_new.txt"

shutil.copy(path1, path2)
shutil.copy(path1, path3)

print("_"*40)
############# Get list of all files and folder from path ############
src_path = r"E:\\Filesdata"
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


print("File count :", file_count)  # File count : 40
print("Folder count :", fold_count) # Folder count : 24





