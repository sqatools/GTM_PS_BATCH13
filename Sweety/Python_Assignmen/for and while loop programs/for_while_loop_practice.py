#####Practice Programs#####
#1. Print numbers from 1 to 10 using for loop.

for i in range(1, 10):
    print(i)


print("_"*50)
#############################################################################################
#2. Display even numbers between 1 and 20 using while loop
num = 1
while num <= 20:
    num = num+1
    if num % 2 == 0:
        print("even number are:", num)

print("_"*50)
#############################################################################################
#3. Print the multiplication table of 7 using range().
num = 7
for i in range(1, 11):
    mul = num*i
    print(mul)


print("_"*100)
#############################################################################################
#4. Print a pattern of stars using nested for loops.
for i in range(1, 11):
    print("*")
    for j in range(10, 0, -1):
        print("*", end=" ")


print("_"*100)
#############################################################################################
# 5. Find the sum of numbers from 1 to 100 using for loop.
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)


print("_"*100)
#############################################################################################
# 6. Print numbers in reverse order using range().
for i in range(20, 0, -1):
    print(i)


print("_"*100)
#############################################################################################
#7. Display all odd numbers from 1 to 50 using range().
for i in range(1, 51):
  if i % 2 != 0:
   print(i)


print("_"*100)
#############################################################################################
#8. Calculate the factorial of a number using while loop
num = 4
fact = 1
while num > 0:
    fact = fact*num #1*4=4  3*4=12 12*2=24 24*1=24
    num = num-1 #3 2 1 0
print(fact)


print("_"*100)
#############################################################################################
#9. Use range() with step = -1 to print reverse counting.
for i in range(30, 0, -1):
    print(i)


print("_"*100)
#############################################################################################
#10. Iterate over a list using for loop and range().
list1 = [10, 4, 77, 9]
for val in list1:
    print(val)



print("_"*100)
#############################################################################################
#11. Print Fibonacci series using while loop.
a = 0
b = 1
print(a)
print(b)
for i in range(2, 10):
    sum = a+b
    print(sum)
    a = b
    b = sum


print("_"*100)
#############################################################################################
#9. Iterate through a dictionary using for loop.
dict1 = {'a': 123, 'b': 456, 'c': 789}
print(dict1)
for key in dict1:
    print(key, dict1[key])

















