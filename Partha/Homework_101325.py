a = 1
b = 2
print("1.","Sum of a & b is",a+b)
# from where the space is coming after "is" in the print statement?
print("*"*50)

print("Subtraction of a from b is",b-a)
print("Subtraction of b from a is",a-b)
print("*"*50)

print("Multiplication of a & b is",a*b)
print("*"*50)

string = "Hello Player 1 "
print(string*5)
print("*"*50)

a = 33
b = 53
c = 74
print("The Average of", a, b, "and", c, "is", (a+b+c)/3)
print("*"*50)

nlist1 = [10,45,33,76,23,108,92]
slist1 = sorted(nlist1)
x=len(slist1)
print(slist1)
print("Median of nlist1 is",slist1[x//2])
print("*"*50)
nlist2 = [46,104,45,77,19,93]
slist2 = sorted(nlist2)
y=len(slist2)
print(slist2)
print("Median of nlist2 is",(slist2[(y//2)-1]+slist2[y//2])/2)
print("*"*50)