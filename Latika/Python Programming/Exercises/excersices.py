
print("Program 1")
print("Python program to repeat a given string 5 times.")

str1 = "SQATools"
n = 5
print("Result: ", str1*n)
##########################################################################################################

print("Program 2")
print("Program to get the Average of given numbers.")
a=4
b=5
c=3
print("Average of 3 numbers are :",a+b+c/3)

#########################################################################################################

print("Program 3")
print("Program to interchange values between variables.")
p=10
q=5
p,q=q,p
print("Value of p:",p)
print("Value of q:",q)

#############################################################################################################

print("Program 4")
print("Get a string made of first and the last 2 chars")
string="Latika"
if len(string)<2:
    print("true")
else:
    print(string[:2]+string[-2])

###########################################################################################################

print("Program 5")
print("Program to check if a number is divisible by 3")
num=int(input("Please enter the number:"))
if num%3==0:
    print("Number is divisible  by 3",num)
else:
    print("Number is not divisible by 3",num)
################################################################################################

print("Program 6")
print("Addition of Values")
a1=30
a2=40

print("Addition of a1 and a2",a1+a2)
a3=a1+a2
print("Addition of a1 + a2",a3)
#####################################################################################################
print("Program 7")
print("Subtraction")
print("Subtraction of a1-a2",a1-a2)

########################################################################################################
print("Program 8")
print("Multiplication")
print("Multiplication of a1*a2",a1*a2)

#########################################################################################################
print("Program 9")
print("Division")
print("Division with single / of a1/a2",a1/a2)
print("Division with double // of a1//a2",a1//a2)

###########################################################################################################

print("Program 10")
print("Remainder")
print("Remainder value ", a1%a2)




