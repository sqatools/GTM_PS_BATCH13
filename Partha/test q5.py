stucount = input("Enter Student Count: ")
marksdict = {}
avgdict = {}

for i in range(int(stucount)):
    name = input("Enter Student Name: ")
    sub1marks = float(input("Enter Subject 1 Marks: "))
    sub2marks = float(input("Enter Subject 2 Marks: "))
    sub3marks = float(input("Enter Subject 3 Marks: "))
    #summ = sub1marks + sub2marks + sub3marks
    #print(sub1marks, sub2marks, sub3marks, summ)
    avg = round((sub1marks+sub2marks+sub3marks)/3,2)
    #print(f"The average marks for {name} is: {avg}")
    marksdict[name] = [sub1marks, sub2marks, sub3marks]
    avgdict[name] = avg
print(marksdict)
print(avgdict)

