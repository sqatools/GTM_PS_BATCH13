import os


print(os.getcwd())
os.mkdir("folder1")
os.mkdir(r"file path\test_os")

os.rmdir("folder1")
os.rmdir(r"filepath\test_os")

print(os.getenv("path"))
print(os.getenv("browser"))