#if we want to get random values, then we can make use of this module

import random

import faker
from faker import Faker

from Shreya.Strings.list_programmes import result_1

#generate random number
result_num = random.randint(1, 100)
#aboce is generate a random number betwen 1-100
print("Random value is : ", result_num)  #Random value is :  97

#get random value from list of values
result2 = random.choice([4, 7, 9, 1, 24])
print("Random choice :", result2)   #Random choice : 4

#from faker - get a list of names and in that get a random value
# Initialize Faker
fake = Faker()
list_names = [] #created the list to store the values

for _ in range(10): #_ bcz i we are not goinhg to use in the loop,
    list_names.append(fake.name())
    print("Faker list names is : ", list_names)

#print the list of names
print("The list of names are : ")
for name in list_names:
    print(name)

# Pick one random name from the generated list
result_list = random.choice(list_names)
print("Randomly selected name is :", result_list)

"""
Faker list names is :  ['Jonathan Romero']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia', 'Christian Burke']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia', 'Christian Burke', 'Julia Kidd']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia', 'Christian Burke', 'Julia Kidd', 'Matthew Adams']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia', 'Christian Burke', 'Julia Kidd', 'Matthew Adams', 'Brian Salinas']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia', 'Christian Burke', 'Julia Kidd', 'Matthew Adams', 'Brian Salinas', 'Crystal Gonzales']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia', 'Christian Burke', 'Julia Kidd', 'Matthew Adams', 'Brian Salinas', 'Crystal Gonzales', 'Jesse Glover']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia', 'Christian Burke', 'Julia Kidd', 'Matthew Adams', 'Brian Salinas', 'Crystal Gonzales', 'Jesse Glover', 'Whitney Perkins']
Faker list names is :  ['Jonathan Romero', 'Ashley Garcia', 'Christian Burke', 'Julia Kidd', 'Matthew Adams', 'Brian Salinas', 'Crystal Gonzales', 'Jesse Glover', 'Whitney Perkins', 'Julie Sharp']

The list is : 
Jonathan Romero
Ashley Garcia
Christian Burke
Julia Kidd
Matthew Adams
Brian Salinas
Crystal Gonzales
Jesse Glover
Whitney Perkins
Julie Sharp

Randomly selected name is : Christian Burke

"""

"""
_ (underscore): This is a variable name, but it is a convention in Python to use a single
 underscore as a placeholder when the value of the loop variable itself is not going to be used
  within the loop's body. It signifies that the programmer does not care about the specific
  iteration number, only that the loop should run a certain amount of times.
  
  range(10): This is a built-in Python function that generates a sequence of numbers.
   When given a single argument (like 10), it produces a sequence of integers starting 
   from 0 up to (but not including) that number. 
   So, range(10) will generate the sequence 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

"""

# shuffle value from given list - chnage the position in the list
list1 = ['a', 'b', 123, 345, 'p', 3.5]
random.shuffle(list1)
print(list1) # [345, 3.5, 'a', 'p', 'b', 123]



