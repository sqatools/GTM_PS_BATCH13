import os

# get current working directory.
print(os.getcwd())
#C:\Users\Sriram\PycharmProjects\GTM_PS_BATCH13\Gayathri\python_modules

# create a directory in the current path
#os.mkdir("folder1")
#os.mkdir(r"C:\Users\Sriram\PycharmProjects\TestData\test_os")

#if we again try to create the same folder - will get error
#Cannot create a file when that file already exists: 'C:\\Users\\Sriram\\PycharmProjects\\TestData\\test_os'

#how to create multipel folders
#for i in range(1, 6): #create 5 folders
    #os.mkdir(fr"C:\Users\Sriram\PycharmProjects\TestData\test_os\Test_os{i}")
    #here r for raw string to avoid in name any special chars
    #f for formatting the {i} value

# create a folder tree.
#os.makedirs(r"C:\Users\Sriram\PycharmProjects\TestData\fold1\fold2\fold3")

# remove folder tree
#os.removedirs(r"C:\Users\Sriram\PycharmProjects\TestData\fold1\fold2")
#NOTE : If at all in teh folder there is any file - then we cant delete that folder

###### get environment variable value####

#print(os.getenv("path"))
#it prints under path - system varaible - whateever is mentioned
# C:\Python3\Scripts\;C:\Python3\;C:\Users\Deepesh Yadav\AppData\Local\Programs\Python\Python38\Scripts\;C:\Users\Deepesh Yadav\AppData\Local\Programs\Python\Python38\;C:\Program Files\Python38\Scripts\;C:\Program Files\Python38\;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;E:\driver;C:\sqalite3\;C:\Program Files (x86)\dotnet\;E:\Trainings\PythonRobotTavet14Feb2023\RobotframeworkProject\chromedriver_win32\chromedriver.exe;c:\users\deepesh yadav\appdata\roaming\python\python312\;c:\users\deepesh yadav\appdata\roaming\python\python312\Scripts\;C:\Python312\;C:\Python312\Scripts\;C:\Program Files\PuTTY\;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Program Files (x86)\Yarn\bin\;C:\Program Files\Java\jdk-11.0.17\bin;C:\apache-maven-3.9.11-bin\apache-maven-3.9.11\bin;C:\Program Files\Git\cmd;C:\allure-2.35.1\bin;C:\Users\Deepesh Yadav\AppData\Local\Microsoft\WindowsApps;C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.2\bin;;E:\chromedriver_win32;C:\Program Files\Docker Toolbox;C:\Users\Deepesh Yadav\AppData\Local\GitHubDesktop\bin;C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2022.3.2\bin;;C:\Users\Deepesh Yadav\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\Deepesh Yadav\AppData\Roaming\npm;C:\Users\Deepesh Yadav\AppData\Local\Yarn\bin;C:\Users\Deepesh Yadav\AppData\Local\Programs\cursor\resources\app\bin

print(os.getenv("OneDrive")) # C:\Users\Sriram\OneDrive

####### join path ######
src_path = r"C:\Users\Sriram\PycharmProjects\TestData"
filename = "testdata.txt"

file_path = os.path.join(src_path, filename)
print("filepath :", file_path)  # C:\Users\Sriram\PycharmProjects\TestData\testdata.txt

####### check given file/folder is available path ######
print("given path is file:", os.path.isfile(file_path))  # given path is file: True
print("given path is folder :", os.path.isdir(src_path)) # given path is folder : True
fol1_path = r"C:\Users\Sriram\PycharmProjects\TestDat"
print("given path is available :", os.path.exists(fol1_path))  # given path is available : False
#################################

import shutil
#this library/module is required when we have t opy a file from one folder to another
#
path1 = r"C:\Users\Sriram\PycharmProjects\TestData\testdata.txt"
path2 = r"C:\Users\Sriram\PycharmProjects\TestData\test_os\testdata.txt" #copy eith same name
path3 = r"C:\Users\Sriram\PycharmProjects\TestData\test_os\count_name_new.txt" #copy with differnt name

shutil.copy(path1, path2)
shutil.copy(path1, path3)

print("_"*40)

############# Get list of all files and folder from path ############
src_path = r"C:\Users\Sriram\PycharmProjects\GTM_PS_BATCH13"
files_list = os.listdir(src_path)
print(files_list)
#['.git', '.gitignore', '.idea', 'Aishwarya', 'Akansha', 'Akshay', 'Amrutha', 'Anuj', 'Arun', 'Deepesh', 'Divya', 'dwijesh', 'Gayathri', 'Latika', 'Lavanya', 'Maha', 'Partha', 'Pavan', 'Pramod', 'Preeti', 'pull', 'Python_List.py', 'Rahul', 'README.md', 'Rina', 'Rohit', 'Sangeeta', 'Shalaka', 'Shreya', 'Sree', 'swarna', 'Sweety', 'thangam']
file_count = 0
fold_count = 0

for data in files_list:
    data_path = os.path.join(src_path, data)
    print("data path :", data_path) # here it joins the path with the file liek below
    #data path : C:\Users\Sriram\PycharmProjects\GTM_PS_BATCH13\.git
    #data path : C:\Users\Sriram\PycharmProjects\GTM_PS_BATCH13\.gitignore
    if os.path.isfile(data_path):
        file_count += 1
    elif os.path.isdir(data_path):
        fold_count += 1
print("File count :", file_count)  # File count : 4
print("Folder count :", fold_count) # Folder count : 29
