import os

# get current working directory i.e. current path
print(os.getcwd())
# C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\Python_Modules

# create a directory in the current path
#os.mkdir("Testfile")
#os.mkdir(r"D:\Test_Folder\Practice\userfolder")

#Folders create by loop
#for i in range (1,6):
 #   os.mkdir(fr"D:\Test_pratice\folder{i}")



# remove directory.
#os.rmdir("Testfile")
#os.rmdir(r"D:\Test_Folder\Practice\userfolder")

# create a folder tree: Mutilple folders with each folders
#os.mkdir(r"D:\Test_Folder\Practice\folder1\folder2\folder3\folder4\folder5")

# remove folder tree
#os.removedirs(r"D:\Test_Folder\Practice\folder1\folder2\folder3\folder4\folder5")

###### get environment variable value####
#print(os.getenv("path"))
# C:\Program Files\Python314\Scripts\;C:\Program Files\Python314\;C:\Program Files\Common Files\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\JMeter\bin;%JAVA_HOME%\bin;C:\Program Files\Git\cmd;C:\Users\SHREE\AppData\Local\Microsoft\WindowsApps;

#print(os.getenv("OneDriveConsumer")) # C:\Users\SHREE\OneDrive

#print(os.getenv("JMETER_HOME")) # C:\Program Files\JMeter

####### join path ######
src_path = r"D:\Test_pratice\folder1"
filename = "Test_data.txt"

file_path = os.path.join(src_path, filename)
print(file_path) # D:\Test_pratice\folder1\Test_data.txt

####### check given file/folder is available path ######
print("Display given path in file :",os.path.isfile(file_path)) # True
print("Display given path in folder :", os.path.isdir(src_path)) # True

fol1_path = r"D:\Test_pratice\Batch14"
print("Given path is available:",os.path.exists(fol1_path)) # Given path is available: False

##################################################
import shutil
# shutil means copy 1 file to another folder

path1 = r"D:\Test_pratice\folder1\Test_data.txt"
path2 = r"D:\Test_pratice\folder2\Test_data.txt"
path3 = r"D:\Test_pratice\folder4\Test_data_new.txt"

shutil.copy(path1, path2)
shutil.copy(path1, path3)

print("-"*50)
################### Get list of all files and folder from path###############################
src_path = r"D:\Study"
files_list = os.listdir(src_path)
print(files_list)
file_count = 0
folder_count = 0

for data in files_list:
  data_path = os.path.join(src_path, data)
  if os.path.isfile(data_path):
      file_count += 1
  elif os.path.isdir(data_path):
      folder_count +=1
  print("Folder_count :", folder_count) # 22
print("File_count :", file_count) # 43


