str1="Partha Saha"
print(str1[-1:-10:-1])
print(str1[0:5:1])
print(str1[-10:1])
print(str1[:5:-1])

print('*'*50)

name = "Max"
age = 30
city = "New York"

result1 = "My name is "+name+" and age is "+str(age)+", I live in "+city
print(result1,type(result1))

print("My name is "+name+" and age is",age,", I live in "+city)
result2 = "My name is "+name+" and age is ",age,", I live in "+city
print(result2,type(result2))
result3 = f"My name is {name} and age is {age}, I live in {city}"
print(result3,type(result3))

print('*'*50)
str7 = "Partha Saha"
print("After Replacement", str7.replace("Partha","Max"))


print('*'*50)
