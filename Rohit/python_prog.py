with open("TestFile.txt","r") as f:
    line = f.read()
    print(len(line))
    print(line)


with open("TestFile.txt","w") as f:
    f.write("I am Leaving in Karad city")

with open("TestFile.txt","a") as f:
    f.write("Now looking job in Python")