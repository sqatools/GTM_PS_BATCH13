#17th Oct - Class
#write a python program to check given number is prime or not
#prime number is only divisible by 1 or itself
#e.x 2,3,5,7,11,13
num = 15
prime = True #initiating a flag to making sure the numebr is prime
for i in range(2, num):  #here we are starting from 2 as we dont want 1 , we are checking above 1 to see if its divisible
    #until num provided(i.e it will be n-1 if num = 13, then it wil be till 12
    print(i)
    if num % i == 0:  # we are checking if the number is divible, if divisible it wont be prime
        prime = False #since its divisible, it will not be prime
        break  #break here, as it need not have to continue i.e in case of 12, 12%2 ==0, prime = False, Then it
        #nned not have to check other numbers - so it will break the loop, it wont go and check if 12%3,12%4
    else:
        continue  #here it will continue with rest of the loop, except when its divisble
        #here above else condition can be removed as its not required

if prime == True:
#above can be defined in a differnt way
#if prime: #we need not have to mention == True, as by default its True
    print("this is a prime number:",num)
else:
    print("this is not a prime number")

#when value given as 12
#2
#this is not a prime number

#when value is 11
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# this is a prime number: 11

#when value is 15
#2
#3
#this is not a prime number
