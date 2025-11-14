import random


# generate random number
result1 = random.randint(1, 15)
print("result1 :", result1)  # 9

# get random value from list of data
result2 = random.choice([4, 7, 9, 1, 24])
print("Random choice :", result2)


# shuffle value from given list
list1 = ['a', 'b', 123, 345, 'p', 3.5]
random.shuffle(list1)
print(list1) # [345, 3.5, 'a', 'p', 'b', 123]


