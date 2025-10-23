"""
print ('1).Find those numbers which are divisible by 7 & multiple of 5, between 1500 & 2700 (both included).')

for i in range (1500,2701):
    if i %7==0 and i %5==0:
        print(i)
"""
print ('2).Python Loops program to construct the following pattern, using a nested for loops.')

for i in range(1,6):
    for j in range(1,i + 1):
        print ('*',end = " ")
    print()
for k in range(6,0,-1):
    for n in range (k):
        print('*', end=" ")
    print()


print ('3). Python Loops program that will add the word from the user to the empty string using python.')

print('4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.')

# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd= 0
for val in numbers:
    if val %2==0:
        even +=1
    else:
        odd+=1

print(even)
print(odd)
